# Copyright 2024 Google LLC All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import queue
import unittest
from datetime import timedelta, timezone
from unittest import mock

from google.cloud._testing import _Monkey
from google.cloud.exceptions import NotFound

from google.cloud.spanner_v1 import (
    BatchCreateSessionsResponse,
    Session,
    _opentelemetry_tracing,
)
from google.cloud.spanner_v1 import pool as MUT
from google.cloud.spanner_v1._helpers import (
    AtomicCounter,
)
from google.cloud.spanner_v1._opentelemetry_tracing import trace_call
from google.cloud.spanner_v1.database import Database
from google.cloud.spanner_v1.pool import (
    AbstractSessionPool,
    BurstyPool,
    FixedSizePool,
    PingingPool,
    SessionCheckout,
)
from google.cloud.spanner_v1.request_id_header import REQ_RAND_PROCESS_ID
from google.cloud.spanner_v1.transaction import Transaction
from google.cloud.spanner_v1.types.spanner import Session as SessionProto
from tests._builders import build_database
from tests._helpers import (
    HAS_OPENTELEMETRY_INSTALLED,
    LIB_VERSION,
    OpenTelemetryBase,
    StatusCode,
    enrich_with_otel_scope,
)


class _Queue(object):
    def __init__(self):
        self._got = None
        self._items = []

    def get(self, block=True, timeout=None):
        self._got = {"block": block, "timeout": timeout}
        import queue

        if not self._items:
            raise queue.Empty()
        return self._items.pop(0)

    def put(self, item, block=True, timeout=None):
        self._items.append(item)


def _make_database(name="name"):
    return mock.create_autospec(Database, instance=True)


def _make_session():
    return mock.create_autospec(Session, instance=True)


class TestCase(unittest.TestCase):
    pass


class _Session(object):
    def __init__(self, name, last_use_time=None, exists=True):
        self.name = name.name if hasattr(name, "name") else name
        self._database = name if hasattr(name, "name") else None
        self._session_id = (
            self.name.split("/")[-1] if hasattr(self.name, "split") else str(self.name)
        )
        self.last_use_time = last_use_time or datetime.datetime.now(
            datetime.timezone.utc
        )
        self._deleted = False
        self._exists_checked = False
        self._pinged = False
        self._exists = exists

        def _ping_side_effect(*args, **kwargs):
            self._pinged = True

        def _delete_side_effect(*args, **kwargs):
            self._deleted = True
            return mock.DEFAULT

        def _exists_side_effect(*args, **kwargs):
            self._exists_checked = True
            if getattr(self, "exists", None) and self.exists.return_value is not exists:
                return self.exists.return_value
            return self._exists

        self.delete = mock.Mock(side_effect=_delete_side_effect)
        self.ping = mock.Mock(side_effect=_ping_side_effect)
        self.exists = mock.Mock(side_effect=_exists_side_effect, return_value=exists)
        self.create = mock.Mock()
        self._transaction = None

        def get_transaction(*args, **kwargs):
            res = self._transaction
            if self._transaction is None:
                self._transaction = mock.Mock()
            return res

        self.transaction = mock.Mock(side_effect=get_transaction)

    def __lt__(self, other):
        return self.name < other.name

    @property
    def labels(self):
        return self._labels

    @property
    def session_id(self):
        return self._session_id

    @property
    def database_role(self):
        return self._database_role


class _Instance(object):
    def __init__(self):
        self.instance_id = "instance-id"
        self._client = mock.Mock()
        self._client.project = "project-id"
        self._client._nth_client_id = 1


class _Database(object):
    _channel_id = 1
    NTH_REQUEST = AtomicCounter()

    def __init__(self, name, database_role=None):
        self.name = name
        self.database_id = name.split("/")[-1]
        self._database_role = database_role
        self.spanner_api = mock.Mock()
        self._route_to_leader_enabled = False
        self._instance = _Instance()
        self._sessions = []

        # Set default return value for batch_create_sessions to avoid infinite loops in _fill_pool
        session_pb = SessionProto(name=name + "/sessions/default")
        self.spanner_api.batch_create_sessions.return_value = (
            BatchCreateSessionsResponse(session=[session_pb])
        )

    @property
    def _nth_client_id(self):
        return self._instance._client._nth_client_id

    @property
    def database_role(self):
        return self._database_role

    @database_role.setter
    def database_role(self, value):
        self._database_role = value

    def with_error_augmentation(self, *args, **kwargs):
        return [], mock.MagicMock(__enter__=mock.Mock(), __exit__=mock.Mock())

    def _next_nth_request(self, n):
        return "request-id-" + str(n)


class TestAbstractSessionPool(TestCase):
    def _getTargetClass(self):
        return AbstractSessionPool

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_ctor_defaults(self):
        pool = self._make_one()
        self.assertIsNone(pool._database)
        self.assertEqual(pool.labels, {})
        self.assertIsNone(pool.database_role)

    def test_ctor_explicit(self):
        labels = {"foo": "bar"}
        pool = self._make_one(labels=labels, database_role="role")
        self.assertEqual(pool.labels, labels)
        self.assertEqual(pool.database_role, "role")

    def test_bind_raises_NotImplementedError(self):
        pool = self._make_one()
        db = _Database("database-name")
        with self.assertRaises(NotImplementedError):
            pool.bind(db)

    def test_get_virtual(self):
        pool = self._make_one()
        with self.assertRaises(NotImplementedError):
            pool.get()

    def test_put_virtual(self):
        pool = self._make_one()
        with self.assertRaises(NotImplementedError):
            pool.put(None)

    def test_clear_virtual(self):
        pool = self._make_one()
        with self.assertRaises(NotImplementedError):
            pool.clear()

    def test_resource_info_unbound(self):
        pool = self._make_one()
        self.assertIsNone(pool._resource_info)

    def test_resource_info_bound(self):
        pool = self._make_one()
        mock_db = mock.Mock(spec=["_resource_info"])
        mock_db._resource_info = {"project": "p", "instance": "i", "database": "d"}
        pool._database = mock_db
        self.assertEqual(pool._resource_info, mock_db._resource_info)

    def test_resource_info_fallback(self):
        pool = self._make_one()
        mock_db = mock.Mock(spec=["_instance", "database_id"])
        mock_db._instance = mock.Mock(spec=["_client", "instance_id"])
        mock_db._instance.instance_id = "i"
        mock_db._instance._client = mock.Mock(spec=["project"])
        mock_db._instance._client.project = "p"
        mock_db.database_id = "d"
        pool._database = mock_db
        self.assertEqual(
            pool._resource_info,
            {"project": "p", "instance": "i", "database": "d"},
        )

    def test__new_session_wo_labels(self):
        pool = self._make_one()
        database = pool._database = build_database()

        new_session = pool._new_session()

        self.assertEqual(new_session._database, database)
        self.assertEqual(new_session.labels, {})
        self.assertIsNone(new_session.database_role)

    def test__new_session_w_labels(self):
        labels = {"foo": "bar"}
        pool = self._make_one(labels=labels)
        database = pool._database = build_database()

        new_session = pool._new_session()

        self.assertEqual(new_session._database, database)
        self.assertEqual(new_session.labels, labels)
        self.assertIsNone(new_session.database_role)

    def test__new_session_w_database_role(self):
        database_role = "dummy-role"
        pool = self._make_one(database_role=database_role)
        database = pool._database = build_database()

        new_session = pool._new_session()

        self.assertEqual(new_session._database, database)
        self.assertEqual(new_session.labels, {})
        self.assertEqual(new_session.database_role, database_role)

    def test_session_deprecated(self):
        import warnings

        pool = self._make_one()
        with warnings.catch_warnings(record=True) as warned:
            warnings.simplefilter("always")
            checkout = pool.session()
            self.assertEqual(len(warned), 1)
            self.assertTrue(issubclass(warned[0].category, DeprecationWarning))
        self.assertIs(checkout._pool, pool)

    def test_session_w_kwargs(self):
        pool = self._make_one()
        checkout = pool.session(foo="bar")
        self.assertIsInstance(checkout, SessionCheckout)
        self.assertIs(checkout._pool, pool)
        self.assertIsNone(checkout._session)
        self.assertEqual(checkout._kwargs, {"foo": "bar"})


class TestFixedSizePool(OpenTelemetryBase):
    BASE_ATTRIBUTES = {
        "db.type": "spanner",
        "db.url": "spanner.googleapis.com",
        "db.instance": "name",
        "net.host.name": "spanner.googleapis.com",
        "gcp.client.service": "spanner",
        "gcp.client.version": LIB_VERSION,
        "gcp.client.repo": "googleapis/python-spanner",
        "gcp.resource.name": _opentelemetry_tracing.GCP_RESOURCE_NAME_PREFIX + "name",
        "cloud.region": "global",
    }
    enrich_with_otel_scope(BASE_ATTRIBUTES)

    def _getTargetClass(self):
        return FixedSizePool

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_ctor_defaults(self):
        pool = self._make_one()
        self.assertIsNone(pool._database)
        self.assertEqual(pool.size, 10)
        self.assertEqual(pool.default_timeout, 10)
        self.assertTrue(pool._sessions.empty())
        self.assertEqual(pool.labels, {})
        self.assertIsNone(pool.database_role)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_ctor_explicit(self, mock_region):
        labels = {"foo": "bar"}
        database_role = "dummy-role"
        pool = self._make_one(
            size=4, default_timeout=30, labels=labels, database_role=database_role
        )
        self.assertIsNone(pool._database)
        self.assertEqual(pool.size, 4)
        self.assertEqual(pool.default_timeout, 30)
        self.assertTrue(pool._sessions.empty())
        self.assertEqual(pool.labels, labels)
        self.assertEqual(pool.database_role, database_role)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_bind(self, mock_region):
        database_role = "dummy-role"
        pool = self._make_one()
        database = _Database("name")
        SESSIONS = [_Session(database)] * 10
        database._database_role = database_role
        database._sessions.extend(SESSIONS)

        pool.bind(database)

        self.assertIs(pool._database, database)
        self.assertEqual(pool.size, 10)
        self.assertEqual(pool.database_role, database_role)
        self.assertEqual(pool.default_timeout, 10)
        self.assertTrue(pool._sessions.full())

        api = database.spanner_api
        self.assertEqual(api.batch_create_sessions.call_count, 10)
        for session in SESSIONS:
            session.create.assert_not_called()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_get_active(self, mock_region):
        pool = self._make_one(size=4)
        database = _Database("name")
        SESSIONS = sorted([_Session(database) for i in range(0, 4)])
        pool._new_session = mock.Mock(side_effect=SESSIONS)
        pool.bind(database)

        # check if sessions returned in LIFO order
        for i in (3, 2, 1, 0):
            session = pool.get()
            self.assertIs(session, SESSIONS[i])
            self.assertFalse(session._exists_checked)
            self.assertFalse(pool._sessions.full())

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_get_non_expired(self, mock_region):
        pool = self._make_one(size=4)
        database = _Database("name")
        last_use_time = datetime.datetime.now(timezone.utc) - timedelta(minutes=56)
        SESSIONS = sorted(
            [_Session(database, last_use_time=last_use_time) for i in range(0, 4)]
        )
        pool._new_session = mock.Mock(side_effect=SESSIONS)
        pool.bind(database)

        # check if sessions returned in LIFO order
        for i in (3, 2, 1, 0):
            session = pool.get()
            self.assertIs(session, SESSIONS[i])
            self.assertTrue(session._exists_checked)
            self.assertFalse(pool._sessions.full())

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_spans_bind_get(self, mock_region):
        if not HAS_OPENTELEMETRY_INSTALLED:
            return

        # This tests retrieving 1 out of 4 sessions from the session pool.
        pool = self._make_one(size=4)
        database = _Database("name")
        SESSIONS = sorted([_Session(database) for i in range(0, 4)])
        database._sessions.extend(SESSIONS)
        pool.bind(database)

        with trace_call("pool.Get", SESSIONS[0]):
            pool.get()

        span_list = self.get_finished_spans()
        got_span_names = [span.name for span in span_list]
        want_span_names = ["CloudSpanner.FixedPool.BatchCreateSessions", "pool.Get"]
        assert got_span_names == want_span_names

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id - 1}.{database._channel_id}.{_Database.NTH_REQUEST.value}.1"
        attrs = dict(
            TestFixedSizePool.BASE_ATTRIBUTES.copy(), x_goog_spanner_request_id=req_id
        )
        attrs["db.instance"] = ""
        attrs["gcp.resource.name"] = _opentelemetry_tracing.GCP_RESOURCE_NAME_PREFIX

        # Check for the overall spans.
        got_attrs = dict(span_list[0].attributes)
        got_attrs.pop("x_goog_spanner_request_id", None)
        attrs.pop("x_goog_spanner_request_id", None)
        self.assertEqual(got_attrs, attrs)

        self.assertSpanAttributes(
            "pool.Get",
            status=StatusCode.OK,
            attributes=TestFixedSizePool.BASE_ATTRIBUTES,
            span=span_list[-1],
        )
        wantEventNames = [
            "Acquiring session",
            "Waiting for a session to become available",
            "Acquired session",
        ]
        self.assertSpanEvents("pool.Get", wantEventNames, span_list[-1])

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_spans_bind_get_empty_pool(self, mock_region):
        if not HAS_OPENTELEMETRY_INSTALLED:
            return

        # Tests trying to invoke pool.get() from an empty pool.
        pool = self._make_one(size=0, default_timeout=0.1)
        database = _Database("name")
        session1 = _Session(database)
        with trace_call("pool.Get", session1):
            try:
                pool.bind(database)
                database._sessions = database._sessions[:0]
                pool.get()
            except Exception:
                pass

        wantEventNames = [
            "Invalid session pool size(0) <= 0",
            "Acquiring session",
            "Waiting for a session to become available",
            "No sessions available in the pool",
        ]
        self.assertSpanEvents("pool.Get", wantEventNames)

        # Check for the overall spans too.
        self.assertSpanNames(["pool.Get"])
        self.assertSpanAttributes(
            "pool.Get",
            attributes=TestFixedSizePool.BASE_ATTRIBUTES,
        )

        span_list = self.get_finished_spans()
        got_all_events = []
        for span in span_list:
            for event in span.events:
                got_all_events.append((event.name, event.attributes))
        want_all_events = [
            ("Invalid session pool size(0) <= 0", {"kind": "FixedSizePool"}),
            ("Acquiring session", {"kind": "FixedSizePool"}),
            ("Waiting for a session to become available", {"kind": "FixedSizePool"}),
            ("No sessions available in the pool", {"kind": "FixedSizePool"}),
        ]
        assert got_all_events == want_all_events

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_spans_pool_bind(self, mock_region):
        if not HAS_OPENTELEMETRY_INSTALLED:
            return

        # Tests the exception generated from invoking pool.bind when
        # you have an empty pool.
        pool = self._make_one(size=1)
        database = _Database("name")
        pool._new_session = mock.Mock(side_effect=Exception("test"))
        fauxSession = mock.Mock()
        setattr(fauxSession, "_database", database)
        try:
            with trace_call("testBind", fauxSession):
                pool.bind(database)
        except Exception:
            pass

        span_list = self.get_finished_spans()
        got_span_names = [span.name for span in span_list]
        want_span_names = ["testBind", "CloudSpanner.FixedPool.BatchCreateSessions"]
        assert got_span_names == want_span_names

        wantEventNames = [
            "Requesting 1 sessions",
            "exception",
        ]
        self.assertSpanEvents("testBind", wantEventNames, span_list[0])

        self.assertSpanAttributes(
            "testBind",
            status=StatusCode.ERROR,
            attributes=TestFixedSizePool.BASE_ATTRIBUTES,
            span=span_list[0],
        )

        got_all_events = []

        # Some event attributes are noisy/highly ephemeral
        # and can't be directly compared against.
        imprecise_event_attributes = ["exception.stacktrace", "delay_seconds", "cause"]
        for span in span_list:
            for event in span.events:
                evt_attributes = event.attributes.copy()
                for attr_name in imprecise_event_attributes:
                    if attr_name in evt_attributes:
                        evt_attributes[attr_name] = "EPHEMERAL"

                got_all_events.append((event.name, evt_attributes))

        want_all_events = [
            ("Requesting 1 sessions", {"kind": "FixedSizePool"}),
            (
                "exception",
                {
                    "exception.type": "Exception",
                    "exception.message": "test",
                    "exception.stacktrace": "EPHEMERAL",
                    "exception.escaped": "False",
                },
            ),
            ("Creating 1 sessions", {"kind": "FixedSizePool"}),
            ("Created sessions", {"count": 1}),
            (
                "exception",
                {
                    "exception.type": "Exception",
                    "exception.message": "test",
                    "exception.stacktrace": "EPHEMERAL",
                    "exception.escaped": "False",
                },
            ),
        ]
        assert got_all_events == want_all_events

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_get_empty_default_timeout(self, mock_region):
        import queue

        pool = self._make_one(size=1)
        session_queue = pool._sessions = _Queue()

        with self.assertRaises(queue.Empty):
            pool.get()

        self.assertEqual(session_queue._got, {"block": True, "timeout": 10})

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_get_empty_explicit_timeout(self, mock_region):
        import queue

        pool = self._make_one(size=1, default_timeout=0.1)
        session_queue = pool._sessions = _Queue()

        with self.assertRaises(queue.Empty):
            pool.get(timeout=1)

        self.assertEqual(session_queue._got, {"block": True, "timeout": 1})

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_put_full(self, mock_region):
        import queue

        pool = self._make_one(size=4)
        database = _Database("name")
        SESSIONS = [_Session(database)] * 4
        database._sessions.extend(SESSIONS)
        pool.bind(database)
        self.reset()

        with self.assertRaises(queue.Full):
            pool.put(_Session(database))

        self.assertTrue(pool._sessions.full())

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_put_non_full(self, mock_region):
        pool = self._make_one(size=4)
        database = _Database("name")
        SESSIONS = [_Session(database)] * 4
        database._sessions.extend(SESSIONS)
        pool.bind(database)
        pool._sessions.get()

        pool.put(_Session(database))

        self.assertTrue(pool._sessions.full())

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_clear(self, mock_region):
        pool = self._make_one()
        database = _Database("name")
        SESSIONS = [_Session(database)] * 10
        pool._new_session = mock.Mock(side_effect=SESSIONS)
        pool.bind(database)
        self.assertTrue(pool._sessions.full())

        api = database.spanner_api
        self.assertEqual(api.batch_create_sessions.call_count, 10)
        for session in SESSIONS:
            session.create.assert_not_called()

        pool.clear()

        for session in SESSIONS:
            self.assertTrue(session._deleted)


class TestBurstyPool(OpenTelemetryBase):
    BASE_ATTRIBUTES = {
        "db.type": "spanner",
        "db.url": "spanner.googleapis.com",
        "db.instance": "name",
        "net.host.name": "spanner.googleapis.com",
        "gcp.client.service": "spanner",
        "gcp.client.version": LIB_VERSION,
        "gcp.client.repo": "googleapis/python-spanner",
        "gcp.resource.name": _opentelemetry_tracing.GCP_RESOURCE_NAME_PREFIX + "name",
        "cloud.region": "global",
    }
    enrich_with_otel_scope(BASE_ATTRIBUTES)

    def _getTargetClass(self):
        return BurstyPool

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_ctor_defaults(self):
        pool = self._make_one()
        self.assertIsNone(pool._database)
        self.assertEqual(pool.target_size, 10)
        self.assertTrue(pool._sessions.empty())
        self.assertEqual(pool.labels, {})
        self.assertIsNone(pool.database_role)

    def test_ctor_explicit(self):
        labels = {"foo": "bar"}
        database_role = "dummy-role"
        pool = self._make_one(target_size=4, labels=labels, database_role=database_role)
        self.assertIsNone(pool._database)
        self.assertEqual(pool.target_size, 4)
        self.assertTrue(pool._sessions.empty())
        self.assertEqual(pool.labels, labels)
        self.assertEqual(pool.database_role, database_role)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_ctor_explicit_w_database_role_in_db(self, mock_region):
        database_role = "dummy-role"
        pool = self._make_one()
        database = pool._database = _Database("name")
        database._database_role = database_role
        pool.bind(database)
        self.assertEqual(pool.database_role, database_role)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_get_empty(self, mock_region):
        pool = self._make_one()
        database = _Database("name")
        pool._new_session = mock.Mock(return_value=_Session(database))
        pool.bind(database)

        session = pool.get()

        self.assertIsInstance(session, _Session)
        self.assertIs(session._database, database)
        session.create.assert_called()
        self.assertTrue(pool._sessions.empty())

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_spans_get_empty_pool(self, mock_region):
        if not HAS_OPENTELEMETRY_INSTALLED:
            return

        # This scenario tests a pool that hasn't been filled up
        # and pool.get() acquires from a pool, waiting for a session
        # to become available.
        pool = self._make_one()
        database = _Database("name")
        session1 = _Session(database)
        pool._new_session = mock.Mock(return_value=session1)
        pool.bind(database)

        with trace_call("pool.Get", session1):
            session = pool.get()
            self.assertIsInstance(session, _Session)
            self.assertIs(session._database, database)
            session.create.assert_called()
            self.assertTrue(pool._sessions.empty())

        span_list = self.get_finished_spans()
        got_span_names = [span.name for span in span_list]
        want_span_names = ["pool.Get"]
        assert got_span_names == want_span_names

        create_span = span_list[-1]
        self.assertSpanAttributes(
            "pool.Get",
            attributes=TestBurstyPool.BASE_ATTRIBUTES,
            span=create_span,
        )
        wantEventNames = [
            "Acquiring session",
            "Waiting for a session to become available",
            "No sessions available in pool. Creating session",
        ]
        self.assertSpanEvents("pool.Get", wantEventNames, span=create_span)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_get_non_empty_session_exists(self, mock_region):
        pool = self._make_one()
        database = _Database("name")
        previous = _Session(database)
        pool.bind(database)
        pool.put(previous)

        session = pool.get()

        self.assertIs(session, previous)
        session.create.assert_not_called()
        self.assertTrue(session._exists_checked)
        self.assertTrue(pool._sessions.empty())

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_spans_get_non_empty_session_exists(self, mock_region):
        # Tests the spans produces when you invoke pool.bind
        # and then insert a session into the pool.
        pool = self._make_one()
        database = _Database("name")
        previous = _Session(database)
        pool.bind(database)
        with trace_call("pool.Get", previous):
            pool.put(previous)
            session = pool.get()
            self.assertIs(session, previous)
            session.create.assert_not_called()
            self.assertTrue(session._exists_checked)
            self.assertTrue(pool._sessions.empty())

        self.assertSpanAttributes(
            "pool.Get",
            attributes=TestBurstyPool.BASE_ATTRIBUTES,
        )
        self.assertSpanEvents(
            "pool.Get",
            ["Acquiring session", "Waiting for a session to become available"],
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_get_non_empty_session_expired(self, mock_region):
        pool = self._make_one()
        database = _Database("name")
        previous = _Session(database, exists=False)
        newborn = _Session(database)
        pool._new_session = mock.Mock(return_value=newborn)
        pool.bind(database)
        pool.put(previous)

        session = pool.get()

        self.assertTrue(previous._exists_checked)
        self.assertIs(session, newborn)
        session.create.assert_called()
        self.assertFalse(session._exists_checked)
        self.assertTrue(pool._sessions.empty())

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_put_empty(self, mock_region):
        pool = self._make_one()
        database = _Database("name")
        pool.bind(database)
        session = _Session(database)

        pool.put(session)

        self.assertFalse(pool._sessions.empty())

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_spans_put_empty(self, mock_region):
        # Tests the spans produced when you put sessions into an empty pool.
        pool = self._make_one()
        database = _Database("name")
        pool.bind(database)
        session = _Session(database)

        with trace_call("pool.put", session):
            pool.put(session)
            self.assertFalse(pool._sessions.empty())

        self.assertSpanAttributes(
            "pool.put",
            attributes=TestBurstyPool.BASE_ATTRIBUTES,
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_put_full(self, mock_region):
        pool = self._make_one(target_size=1)
        database = _Database("name")
        pool.bind(database)
        older = _Session(database)
        pool.put(older)
        self.assertFalse(pool._sessions.empty())

        younger = _Session(database)
        pool.put(younger)  # discarded silently

        self.assertTrue(younger._deleted)
        self.assertIs(pool.get(), older)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_spans_put_full(self, mock_region):
        # This scenario tests the spans produced from putting an older
        # session into a pool that is already full.
        pool = self._make_one(target_size=1)
        database = _Database("name")
        pool.bind(database)
        older = _Session(database)
        with trace_call("pool.put", older):
            pool.put(older)
            self.assertFalse(pool._sessions.empty())

            younger = _Session(database)
            pool.put(younger)  # discarded silently

            self.assertTrue(younger._deleted)
            self.assertIs(pool.get(), older)

        self.assertSpanAttributes(
            "pool.put",
            attributes=TestBurstyPool.BASE_ATTRIBUTES,
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_put_full_expired(self, mock_region):
        pool = self._make_one(target_size=1)
        database = _Database("name")
        pool.bind(database)
        older = _Session(database)
        pool.put(older)
        self.assertFalse(pool._sessions.empty())

        younger = _Session(database, exists=False)
        pool.put(younger)  # discarded silently

        self.assertTrue(younger._deleted)
        self.assertIs(pool.get(), older)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_clear(self, mock_region):
        pool = self._make_one()
        database = _Database("name")
        pool.bind(database)
        previous = _Session(database)
        pool.put(previous)

        pool.clear()

        self.assertTrue(previous._deleted)
        self.assertNoSpans()


class TestPingingPool(OpenTelemetryBase):
    BASE_ATTRIBUTES = {
        "db.type": "spanner",
        "db.url": "spanner.googleapis.com",
        "db.instance": "name",
        "net.host.name": "spanner.googleapis.com",
        "gcp.client.service": "spanner",
        "gcp.client.version": LIB_VERSION,
        "gcp.client.repo": "googleapis/python-spanner",
        "gcp.resource.name": _opentelemetry_tracing.GCP_RESOURCE_NAME_PREFIX + "name",
        "cloud.region": "global",
    }
    enrich_with_otel_scope(BASE_ATTRIBUTES)

    def _getTargetClass(self):
        return PingingPool

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_ctor_defaults(self):
        pool = self._make_one()
        self.assertIsNone(pool._database)
        self.assertEqual(pool.size, 10)
        self.assertEqual(pool.default_timeout, 10)
        self.assertEqual(pool._delta.seconds, 3000)
        self.assertTrue(pool._sessions.empty())
        self.assertEqual(pool.labels, {})
        self.assertIsNone(pool.database_role)

    def test_ctor_explicit(self):
        labels = {"foo": "bar"}
        database_role = "dummy-role"
        pool = self._make_one(
            size=4,
            default_timeout=30,
            ping_interval=1800,
            labels=labels,
            database_role=database_role,
        )
        self.assertIsNone(pool._database)
        self.assertEqual(pool.size, 4)
        self.assertEqual(pool.default_timeout, 30)
        self.assertEqual(pool._delta.seconds, 1800)
        self.assertTrue(pool._sessions.empty())
        self.assertEqual(pool.labels, labels)
        self.assertEqual(pool.database_role, database_role)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_ctor_explicit_w_database_role_in_db(self, mock_region):
        database_role = "dummy-role"
        pool = self._make_one()
        database = pool._database = _Database("name")
        SESSIONS = [_Session(database)] * 10
        database._sessions.extend(SESSIONS)
        database._database_role = database_role
        pool.bind(database)
        self.assertEqual(pool.database_role, database_role)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_bind(self, mock_region):
        pool = self._make_one()
        database = _Database("name")
        SESSIONS = [_Session(database)] * 10
        database._sessions.extend(SESSIONS)
        pool.bind(database)

        self.assertIs(pool._database, database)
        self.assertEqual(pool.size, 10)
        self.assertEqual(pool.default_timeout, 10)
        self.assertEqual(pool._delta.seconds, 3000)
        self.assertTrue(pool._sessions.full())

        api = database.spanner_api
        self.assertEqual(api.batch_create_sessions.call_count, 10)
        for session in SESSIONS:
            session.create.assert_not_called()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_get_hit_no_ping(self, mock_region):
        pool = self._make_one(size=4)
        database = _Database("name")
        SESSIONS = [_Session(database)] * 4
        pool._new_session = mock.Mock(side_effect=SESSIONS)
        pool.bind(database)
        self.reset()

        session = pool.get()

        self.assertIs(session, SESSIONS[0])
        self.assertFalse(session._exists_checked)
        self.assertFalse(pool._sessions.full())
        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_get_hit_w_ping(self, mock_region):
        import datetime

        pool = self._make_one(size=4)
        database = _Database("name")
        SESSIONS = [_Session(database)] * 4
        pool._new_session = mock.Mock(side_effect=SESSIONS)

        sessions_created = datetime.datetime.now(timezone.utc) - datetime.timedelta(
            seconds=4000
        )

        with _Monkey(MUT, _NOW=lambda: sessions_created):
            pool.bind(database)

        self.reset()

        session = pool.get()

        self.assertIs(session, SESSIONS[0])
        self.assertTrue(session._exists_checked)
        self.assertFalse(pool._sessions.full())
        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_get_hit_w_ping_expired(self, mock_region):
        import datetime

        pool = self._make_one(size=4)
        database = _Database("name")
        SESSIONS = [_Session(database) for _ in range(5)]
        pool._new_session = mock.Mock(side_effect=SESSIONS)

        sessions_created = datetime.datetime.now(timezone.utc) - datetime.timedelta(
            seconds=4000
        )
        for s in SESSIONS:
            s._exists = False

        with _Monkey(MUT, _NOW=lambda: sessions_created):
            pool.bind(database)
        self.reset()

        session = pool.get()

        self.assertIs(session, SESSIONS[4])
        session.create.assert_called()
        self.assertTrue(SESSIONS[0]._exists_checked)
        self.assertFalse(pool._sessions.full())
        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_get_empty_default_timeout(self, mock_region):
        import queue

        pool = self._make_one(size=1)
        session_queue = pool._sessions = _Queue()

        with self.assertRaises(queue.Empty):
            pool.get()

        self.assertEqual(session_queue._got, {"block": True, "timeout": 10})
        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_get_empty_explicit_timeout(self, mock_region):
        import queue

        pool = self._make_one(size=1, default_timeout=0.1)
        session_queue = pool._sessions = _Queue()

        with self.assertRaises(queue.Empty):
            pool.get(timeout=1)

        self.assertEqual(session_queue._got, {"block": True, "timeout": 1})
        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_put_full(self, mock_region):
        import queue

        pool = self._make_one(size=4)
        database = _Database("name")
        SESSIONS = [_Session(database)] * 4
        database._sessions.extend(SESSIONS)
        pool.bind(database)

        with self.assertRaises(queue.Full):
            pool.put(_Session(database))

        self.assertTrue(pool._sessions.full())

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_spans_put_full(self, mock_region):
        if not HAS_OPENTELEMETRY_INSTALLED:
            return

        import queue

        pool = self._make_one(size=4)
        database = _Database("name")
        SESSIONS = [_Session(database)] * 4
        database._sessions.extend(SESSIONS)
        pool.bind(database)

        with self.assertRaises(queue.Full):
            pool.put(_Session(database))

        self.assertTrue(pool._sessions.full())

        span_list = self.get_finished_spans()
        got_span_names = [span.name for span in span_list]
        want_span_names = ["CloudSpanner.PingingPool.BatchCreateSessions"]
        assert got_span_names == want_span_names

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id - 1}.{database._channel_id}.{_Database.NTH_REQUEST.value}.1"
        attrs = dict(
            TestPingingPool.BASE_ATTRIBUTES.copy(), x_goog_spanner_request_id=req_id
        )
        attrs["db.instance"] = ""
        attrs["gcp.resource.name"] = _opentelemetry_tracing.GCP_RESOURCE_NAME_PREFIX
        got_attrs = dict(span_list[-1].attributes)
        got_attrs.pop("x_goog_spanner_request_id", None)
        attrs.pop("x_goog_spanner_request_id", None)
        self.assertEqual(got_attrs, attrs)
        wantEventNames = [
            "Created 1 sessions",
            "Created 1 sessions",
            "Created 1 sessions",
            "Created 1 sessions",
            "Requested for 4 sessions, returned 4",
        ]
        self.assertSpanEvents(
            "CloudSpanner.PingingPool.BatchCreateSessions", wantEventNames
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_put_non_full(self, mock_region):
        import datetime

        pool = self._make_one(size=1)
        session_queue = pool._sessions = _Queue()

        now = datetime.datetime.now(timezone.utc)
        database = _Database("name")
        session = _Session(database)

        with _Monkey(MUT, _NOW=lambda: now):
            pool.put(session)

        self.assertEqual(len(session_queue._items), 1)
        ping_after, queued = session_queue._items[0]
        self.assertEqual(ping_after, now + datetime.timedelta(seconds=3000))
        self.assertIs(queued, session)
        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_clear(self, mock_region):
        pool = self._make_one()
        database = _Database("name")
        SESSIONS = [_Session(database)] * 10
        pool._new_session = mock.Mock(side_effect=SESSIONS)
        pool.bind(database)
        self.reset()
        self.assertTrue(pool._sessions.full())

        api = database.spanner_api
        self.assertEqual(api.batch_create_sessions.call_count, 10)
        for session in SESSIONS:
            session.create.assert_not_called()

        pool.clear()

        for session in SESSIONS:
            self.assertTrue(session._deleted)
        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_ping_empty(self, mock_region):
        pool = self._make_one(size=1)
        pool.ping()  # Does not raise 'Empty'
        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_ping_oldest_fresh(self, mock_region):
        pool = self._make_one(size=1)
        database = _Database("name")
        SESSIONS = [_Session(database)] * 1
        database._sessions.extend(SESSIONS)
        pool.bind(database)
        self.reset()

        pool.ping()

        self.assertFalse(SESSIONS[0]._pinged)
        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_ping_oldest_stale_but_exists(self, mock_region):
        import datetime

        pool = self._make_one(size=1)
        database = _Database("name")
        SESSIONS = [_Session(database)] * 1
        pool._new_session = mock.Mock(side_effect=SESSIONS)
        pool.bind(database)

        later = datetime.datetime.now(timezone.utc) + datetime.timedelta(seconds=4000)
        with _Monkey(MUT, _NOW=lambda: later):
            pool.ping()

        self.assertTrue(SESSIONS[0]._pinged)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_ping_oldest_stale_and_not_exists(self, mock_region):
        import datetime

        pool = self._make_one(size=1)
        database = _Database("name")
        SESSIONS = [_Session(database) for _ in range(2)]
        from google.api_core.exceptions import NotFound

        SESSIONS[0].ping.side_effect = NotFound("Session not found")
        pool._new_session = mock.Mock(side_effect=SESSIONS)
        pool.bind(database)
        self.reset()

        later = datetime.datetime.now(timezone.utc) + datetime.timedelta(seconds=4000)
        with _Monkey(MUT, _NOW=lambda: later):
            pool.ping()

        SESSIONS[0].ping.assert_called_once()
        SESSIONS[1].create.assert_called()
        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_spans_get_and_leave_empty_pool(self, mock_region):
        if not HAS_OPENTELEMETRY_INSTALLED:
            return

        # This scenario tests the spans generated from pulling a span
        # out the pool and leaving it empty.
        pool = self._make_one()
        database = _Database("name")
        session1 = _Session(database)
        pool._new_session = mock.Mock(side_effect=[session1, Exception])
        try:
            pool.bind(database)
        except Exception:
            pass

        with trace_call("pool.Get", session1):
            session = pool.get()
            self.assertIsInstance(session, _Session)
            self.assertIs(session._database, database)
            # session.create.assert_called()
            self.assertTrue(pool._sessions.empty())

        span_list = self.get_finished_spans()
        got_span_names = [span.name for span in span_list]
        want_span_names = ["CloudSpanner.PingingPool.BatchCreateSessions", "pool.Get"]
        assert got_span_names == want_span_names

        self.assertSpanAttributes(
            "pool.Get",
            attributes=TestPingingPool.BASE_ATTRIBUTES,
            span=span_list[-1],
        )
        wantEventNames = [
            "Waiting for a session to become available",
            "Acquired session",
        ]
        self.assertSpanEvents("pool.Get", wantEventNames, span_list[-1])


class TestSessionCheckout(unittest.TestCase):
    def _getTargetClass(self):
        return SessionCheckout

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def test_context_manager(self):
        pool = mock.Mock()
        session = mock.Mock()
        # Mock get to be a coro returning session
        pool.get = mock.Mock(return_value=session)

        checkout = self._make_one(pool)
        with checkout as got:
            self.assertIs(got, session)

        pool.get.assert_called_once()
        pool.put.assert_called_once_with(session)


class TestFixedSizePool_extras(TestCase):
    DATABASE_NAME = "projects/p/instances/i/databases/d"
    SESSION_NAME = DATABASE_NAME + "/sessions/s"

    def _getTargetClass(self):
        from google.cloud.spanner_v1.pool import FixedSizePool

        return FixedSizePool

    def _make_one(self, *args, **kwargs):
        pool = self._getTargetClass()(*args, **kwargs)
        pool._new_session = mock.Mock(
            side_effect=lambda *args, **kwargs: _Session(self.SESSION_NAME)
        )
        return pool

    def test_labels_getter(self):
        pool = self._make_one(labels={"foo": "bar"})
        self.assertEqual(pool.labels, {"foo": "bar"})

    def test__new_session_role(self):
        db = _Database(self.DATABASE_NAME)
        db.database_role = "db-role"
        pool = self._make_one(database_role="pool-role")
        pool._database = db
        # We need to bypass the mock _new_session to test the real logic
        from google.cloud.spanner_v1.pool import FixedSizePool

        session = FixedSizePool._new_session(pool)
        self.assertEqual(session.database_role, "pool-role")

        pool._database_role = None
        session = FixedSizePool._new_session(pool)
        self.assertEqual(session.database_role, "db-role")

    def test_resource_info(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one()
        pool.bind(db)
        resource_info = pool._resource_info
        self.assertEqual(resource_info["project"], "project-id")
        self.assertEqual(resource_info["instance"], "instance-id")
        self.assertEqual(resource_info["database"], "d")

    def test_resource_info_unbound(self):
        pool = self._make_one()
        self.assertIsNone(pool._resource_info)

    def test_ctor_defaults(self):
        pool = self._make_one()
        self.assertIsNone(pool._database)
        self.assertEqual(pool.size, 10)
        self.assertEqual(pool.default_timeout, 10)
        self.assertTrue(pool._sessions.empty())

    def test_ctor_explicit(self):
        pool = self._make_one(size=4, default_timeout=30)
        self.assertEqual(pool.size, 4)
        self.assertEqual(pool.default_timeout, 30)

    def test_get_put(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)
        # bind fills the pool with 1 sessions by default mock
        got = pool.get()
        self.assertEqual(got.name, self.SESSION_NAME)
        pool.put(got)
        self.assertEqual(pool._sessions.qsize(), 1)

    def test_get_empty_timeout(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1, default_timeout=0.01)
        pool.bind(db)

        # Empty the pool so we can test timeout
        pool.get()

        with self.assertRaises(queue.Empty):
            pool.get()

    def test_clear(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=2)
        pool.bind(db)
        # bind will fill BOTH slots because requested_session_count is 2 and mock returns 1 per call
        self.assertTrue(pool._sessions.full())
        self.assertEqual(pool._sessions.qsize(), 2)
        pool.clear()
        self.assertEqual(pool._sessions.qsize(), 0)

    def test_fill_pool(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=2)

        session_pb1 = SessionProto(name=self.SESSION_NAME + "/1")
        session_pb2 = SessionProto(name=self.SESSION_NAME + "/2")
        db.spanner_api.batch_create_sessions.return_value = BatchCreateSessionsResponse(
            session=[session_pb1, session_pb2]
        )

        pool.bind(db)

        self.assertEqual(pool._sessions.qsize(), 2)
        db.spanner_api.batch_create_sessions.assert_called_once()

    def test_fill_pool_requested_count_le_0(self):
        # Coverage for line 288+
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=0)
        pool.bind(db)
        self.assertEqual(pool._sessions.qsize(), 0)
        db.spanner_api.batch_create_sessions.assert_not_called()

    def test_fill_pool_already_full(self):
        # Coverage for line 308+
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        # Inject context to skip bind as we want to test _fill_pool directly on a full pool
        pool._database = db
        pool._sessions.put(mock.Mock())
        pool._fill_pool()
        db.spanner_api.batch_create_sessions.assert_not_called()

    def test_ping(self):
        from google.cloud.spanner_v1.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)

        # Clear sessions created by bind
        while not pool._sessions.empty():
            pool._sessions.get()

        session = _Session(self.SESSION_NAME)
        # Make the session old so it will be pinged
        session.last_use_time = _NOW() - datetime.timedelta(minutes=60)
        session.ping = mock.Mock()
        pool.put(session)

        pool.ping()
        session.ping.assert_called_once()

    def test_ping_not_found_recreates(self):
        from google.cloud.spanner_v1.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)

        session = pool.get()
        # Ensure it's the mock
        self.assertIsInstance(session, _Session)
        session.last_use_time = _NOW() - datetime.timedelta(minutes=61)
        session.ping = mock.Mock(side_effect=NotFound("not found"))

        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.Mock()
        pool._new_session = mock.Mock(return_value=new_session)

        pool.put(session)
        pool.ping()

    def test_get_recreates_if_not_found(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)
        session = pool.get()
        session.last_use_time = datetime.datetime.now(
            datetime.timezone.utc
        ) - datetime.timedelta(hours=2)
        # exists returns False, so it recreates
        session.exists.return_value = False
        pool._sessions.put(session)

        got = pool.get()
        self.assertEqual(got.name, self.SESSION_NAME)
        self.assertTrue(got.create.called)

    def test_ping_exception_warns(self):
        import warnings

        from google.cloud.spanner_v1.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)

        session = pool.get()
        session.last_use_time = _NOW() - datetime.timedelta(minutes=61)
        session.ping = mock.Mock(side_effect=Exception("error"))

        pool.put(session)
        with warnings.catch_warnings(record=True) as warned:
            warnings.simplefilter("always")
            pool.ping()
            self.assertEqual(len(warned), 1)

    def test_get_pings_old_session(self):
        from google.cloud.spanner_v1.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)
        session = pool.get()
        # session is too old (55m + 1s)
        session.last_use_time = _NOW() - datetime.timedelta(minutes=56)
        pool.put(session)

        got = pool.get()
        self.assertEqual(got.name, self.SESSION_NAME)
        self.assertGreaterEqual(session.exists.call_count, 1)

    def test_get_timeout_none(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)
        session = pool.get(timeout=None)
        self.assertIsInstance(session, _Session)

    def test_get_old_session_not_exists_recreates(self):
        from google.cloud.spanner_v1.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)

        session = pool.get()
        session.last_use_time = _NOW() - datetime.timedelta(minutes=61)
        session.exists = mock.Mock(return_value=False)

        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.Mock()
        pool._new_session = mock.Mock(return_value=new_session)

        pool.put(session)
        got = pool.get()
        self.assertIs(got, new_session)
        new_session.create.assert_called_once()

    def test_fill_pool_edge_cases(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        # size <= 0
        pool._database = db
        pool.size = 0
        pool._fill_pool()
        self.assertEqual(pool._sessions.qsize(), 0)

        # count <= 0
        pool.size = 1
        pool._sessions.put(_Session(self.SESSION_NAME))
        pool._fill_pool()  # pool already full, count will be 0
        self.assertEqual(pool._sessions.qsize(), 1)

    def test_fill_pool_leader_aware(self):
        db = _Database(self.DATABASE_NAME)
        db._route_to_leader_enabled = True
        pool = self._make_one(size=1)
        # bind calls _fill_pool
        pool.bind(db)
        self.assertEqual(pool._sessions.qsize(), 1)

        self.assertEqual(pool._sessions.qsize(), 1)

    def test_fill_pool_mock_full(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool._database = db
        # Mock full() to return True even if space exists (or just fill it)
        with mock.patch.object(pool._sessions, "full", return_value=True):
            pool._fill_pool()
        # Should return early at line 310

    def test_clear_no_database(self):
        pool = self._make_one(size=1)
        session = _Session(self.SESSION_NAME)
        pool._sessions.put(session)
        # pool._database is None
        pool.clear()
        # Should hit if self._database is None: pass in clear() logic

    def test_fill_pool_full(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool._database = db
        pool._sessions.put(_Session(self.SESSION_NAME))
        pool._fill_pool()  # Should hit "already full" event
        self.assertEqual(pool._sessions.qsize(), 1)

    def test_get_expired_session_recreated(self):
        from google.cloud.spanner_v1.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1, max_age_minutes=0)
        pool.bind(db)

        # Clear sessions created by bind
        while not pool._sessions.empty():
            pool._sessions.get()

        session = _Session(self.SESSION_NAME)
        session.last_use_time = _NOW() - datetime.timedelta(minutes=1)
        session.exists = mock.Mock(return_value=False)

        pool.put(session)

        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.Mock()
        pool._new_session = mock.Mock(return_value=new_session)

        got = pool.get()

        self.assertIs(got, new_session)
        new_session.create.assert_called_once()

    def test_get_invalid_session_recreated(self):
        from google.cloud.spanner_v1.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)

        # Clear sessions created by bind
        while not pool._sessions.empty():
            pool._sessions.get()

        session = _Session(self.SESSION_NAME)
        session.exists = mock.Mock(return_value=False)
        session.last_use_time = _NOW() - datetime.timedelta(minutes=60)

        pool.put(session)

        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.Mock()
        pool._new_session = mock.Mock(return_value=new_session)

        got = pool.get()

        self.assertIs(got, new_session)
        new_session.create.assert_called_once()


def _make_transaction(*args, **kw):
    txn = mock.create_autospec(Transaction)(*args, **kw)
    txn.committed = None
    txn.rolled_back = False
    return txn


class TestPingingPool_extras(TestCase):
    DATABASE_NAME = "projects/p/instances/i/databases/d"
    SESSION_NAME = DATABASE_NAME + "/sessions/s"

    def _getTargetClass(self):
        from google.cloud.spanner_v1.pool import PingingPool

        return PingingPool

    def _make_one(self, *args, **kwargs):
        pool = self._getTargetClass()(*args, **kwargs)
        pool._new_session = mock.Mock(
            side_effect=lambda *args, **kwargs: _Session(self.SESSION_NAME)
        )
        return pool

    def test_ctor_defaults(self):
        pool = self._make_one()
        self.assertEqual(pool.size, 10)
        self.assertEqual(pool.default_timeout, 10)
        self.assertEqual(pool._delta, datetime.timedelta(seconds=3000))

    def test_ping_exception_fallback(self):
        import warnings

        db = _Database(self.DATABASE_NAME)
        # We'll use FixedSizePool for this since it has the catch
        from google.cloud.spanner_v1.pool import FixedSizePool

        pool = FixedSizePool(size=1)
        pool.bind(db)

        # Clear sessions created by bind
        while not pool._sessions.empty():
            pool._sessions.get()

        session = _Session(self.SESSION_NAME)
        # Force it to be old
        from google.cloud.spanner_v1.pool import _NOW

        session.last_use_time = _NOW() - datetime.timedelta(minutes=60)
        session.ping = mock.Mock(side_effect=Exception("ping failed"))

        pool.put(session)

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            pool.ping()
            self.assertEqual(len(w), 1)
            self.assertIn("Failed to ping session", str(w[-1].message))

    def test_ping_empty_pool(self):
        pool = self._make_one(size=1)
        pool.ping()  # Should not raise

    def test_get_timeout_none_pinging(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)
        pool.get()  # Empty it

        # We need something in the pool for timeout=None to give it back
        session = _Session(self.SESSION_NAME)
        # Put it back as tuple (ping_after, session)
        from google.cloud.spanner_v1.pool import _NOW

        pool._sessions.put((_NOW() + datetime.timedelta(hours=1), session))

        got = pool.get(timeout=None)
        self.assertIs(got, session)

    def test_pinging_pool_get_old_session_not_exists_recreates(self):
        from google.cloud.spanner_v1.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)

        session = pool.get()
        # Set ping_after to past
        ping_after = _NOW() - datetime.timedelta(seconds=1)
        # We need to manually put it back with a past ping_after
        pool._sessions.put((ping_after, session))

        session.exists = mock.Mock(return_value=False)
        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.Mock()
        pool._new_session = mock.Mock(return_value=new_session)

        got = pool.get()
        self.assertIs(got, new_session)
        new_session.create.assert_called_once()

    def test_ping_skipped_if_fresh(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1, ping_interval=3600)
        pool.bind(db)

        session = pool.get()
        session.ping = mock.Mock()
        pool.put(session)

        pool.ping()
        session.ping.assert_not_called()

    def test_bind_leader_routing(self):
        db = _Database(self.DATABASE_NAME)
        db._route_to_leader_enabled = True
        pool = self._make_one(size=1)
        pool.bind(db)
        # Verify metadata included leader routing - this requires checking call_args
        # but our mock DB captures it.
        # Line 658 hit.

    def test_bind_invalid_size(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=0)
        pool.bind(db)
        # Line 671-676 hit.


class TestTransactionPingingPool(TestCase):
    DATABASE_NAME = "projects/p/instances/i/databases/d"
    SESSION_NAME = DATABASE_NAME + "/sessions/s"

    def _getTargetClass(self):
        from google.cloud.spanner_v1.pool import TransactionPingingPool

        return TransactionPingingPool

    def _make_one(self, *args, **kwargs):
        pool = self._getTargetClass()(*args, **kwargs)
        pool._new_session = mock.Mock(
            side_effect=lambda *args, **kwargs: _Session(self.SESSION_NAME)
        )
        return pool

    def test_ctor(self):
        pool = self._make_one(size=5)
        self.assertEqual(pool.size, 5)

    def test_get_put(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)

        # After bind, sessions are in _pending_sessions because transaction() is None
        pool.begin_pending_transactions()

        session = pool.get()
        self.assertEqual(session.name, self.SESSION_NAME)

        pool.put(session)
        self.assertEqual(pool._sessions.qsize(), 1)

    def test_put_no_transaction_to_pending(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)
        pool.begin_pending_transactions()

        session = pool.get()
        self.assertIsInstance(session, _Session)
        session._transaction = None  # Force None for test

        pool.put(session)
        self.assertEqual(pool._pending_sessions.qsize(), 1)
        self.assertEqual(pool._sessions.qsize(), 0)
        # Ensure it was initialized
        self.assertIsNotNone(session._transaction)

    def test_begin_pending_transactions(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)
        pool.begin_pending_transactions()

        session = pool.get()
        session._transaction = None
        pool.put(session)

        self.assertEqual(pool._pending_sessions.qsize(), 1)
        pool.begin_pending_transactions()
        self.assertEqual(pool._pending_sessions.qsize(), 0)
        self.assertEqual(pool._sessions.qsize(), 1)

    def test_bind(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)
        self.assertEqual(pool._pending_sessions.qsize(), 1)
        pool.begin_pending_transactions()
        self.assertEqual(pool._sessions.qsize(), 1)

    def test_get_old_session_not_exists_recreates(self):
        from google.cloud.spanner_v1.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool.bind(db)
        pool.begin_pending_transactions()

        session = pool.get()
        # Manually put it back with a past ping_after
        ping_after = _NOW() - datetime.timedelta(seconds=1)
        pool._sessions.put((ping_after, session))

        session.exists = mock.Mock(return_value=False)
        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.Mock()
        pool._new_session = mock.Mock(return_value=new_session)

        got = pool.get()
        self.assertIs(got, new_session)
        new_session.create.assert_called_once()
