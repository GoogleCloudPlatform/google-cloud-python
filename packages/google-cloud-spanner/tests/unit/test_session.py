# Copyright 2016 Google LLC All rights reserved.
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
import threading
from datetime import timezone

import google.api_core.gapic_v1.method
import grpc
import mock
from google.api_core.exceptions import Aborted, Cancelled, NotFound, Unknown
from google.cloud._helpers import UTC, _datetime_to_pb_timestamp
from google.protobuf.duration_pb2 import Duration
from google.protobuf.struct_pb2 import Struct, Value
from google.rpc.error_details_pb2 import RetryInfo

from google.cloud.spanner_v1 import (
    BeginTransactionRequest,
    CommitRequest,
    CommitResponse,
    CreateSessionRequest,
    DefaultTransactionOptions,
    ExecuteSqlRequest,
    RequestOptions,
    SpannerClient,
    TransactionOptions,
    TypeCode,
)
from google.cloud.spanner_v1 import Session as SessionRequestProto
from google.cloud.spanner_v1 import Transaction as TransactionPB
from google.cloud.spanner_v1._helpers import (
    AtomicCounter,
    _delay_until_retry,
    _metadata_with_request_id,
)
from google.cloud.spanner_v1._opentelemetry_tracing import (
    GCP_RESOURCE_NAME_PREFIX,
    trace_call,
)
from google.cloud.spanner_v1.batch import Batch
from google.cloud.spanner_v1.database import Database
from google.cloud.spanner_v1.keyset import KeySet
from google.cloud.spanner_v1.request_id_header import REQ_RAND_PROCESS_ID
from google.cloud.spanner_v1.session import Session
from google.cloud.spanner_v1.snapshot import Snapshot
from google.cloud.spanner_v1.transaction import Transaction
from tests._builders import (
    build_commit_response_pb,
    build_session,
    build_spanner_api,
    build_transaction_pb,
)
from tests._helpers import (
    LIB_VERSION,
    OpenTelemetryBase,
    StatusCode,
    enrich_with_otel_scope,
)

TABLE_NAME = "citizens"
COLUMNS = ["email", "first_name", "last_name", "age"]
VALUES = [
    ["phred@exammple.com", "Phred", "Phlyntstone", 32],
    ["bharney@example.com", "Bharney", "Rhubble", 31],
]
KEYS = ["bharney@example.com", "phred@example.com"]
KEYSET = KeySet(keys=KEYS)
TRANSACTION_ID = b"FACEDACE"


def _make_rpc_error(error_cls, trailing_metadata=[]):
    grpc_error = mock.create_autospec(grpc.Call, instance=True)
    grpc_error.trailing_metadata.return_value = trailing_metadata
    return error_cls("error", errors=(grpc_error,))


NTH_CLIENT_ID = AtomicCounter()


def inject_into_mock_database(mockdb):
    setattr(mockdb, "_nth_request", AtomicCounter())
    nth_client_id = NTH_CLIENT_ID.increment()
    setattr(mockdb, "_nth_client_id", nth_client_id)
    channel_id = 1
    setattr(mockdb, "_channel_id", channel_id)

    def metadata_with_request_id(
        nth_request, nth_attempt, prior_metadata=[], span=None
    ):
        # Handle both cases: nth_request as an integer or as a property descriptor
        if isinstance(nth_request, int):
            nth_req = nth_request
        else:
            nth_req = nth_request.fget(mockdb)
        return _metadata_with_request_id(
            nth_client_id,
            channel_id,
            nth_req,
            nth_attempt,
            prior_metadata,
            span,
        )

    setattr(mockdb, "metadata_with_request_id", metadata_with_request_id)

    # Create a property-like object using type() to make it work with mock
    type(mockdb)._next_nth_request = property(
        lambda self: self._nth_request.increment()
    )

    # Use a closure to capture nth_client_id and channel_id
    def make_with_error_augmentation(db_nth_client_id, db_channel_id):
        def with_error_augmentation(
            nth_request, nth_attempt, prior_metadata=[], span=None
        ):
            """Context manager for gRPC calls with error augmentation."""
            from google.cloud.spanner_v1._helpers import (
                _augment_errors_with_request_id,
                _metadata_with_request_id_and_req_id,
            )

            if span is None:
                from google.cloud.spanner_v1._opentelemetry_tracing import (
                    get_current_span,
                )

                span = get_current_span()

            metadata, request_id = _metadata_with_request_id_and_req_id(
                db_nth_client_id,
                db_channel_id,
                nth_request,
                nth_attempt,
                prior_metadata,
                span,
            )

            return metadata, _augment_errors_with_request_id(request_id)

        return with_error_augmentation

    mockdb.with_error_augmentation = make_with_error_augmentation(
        nth_client_id, channel_id
    )

    return mockdb


class TestSession(OpenTelemetryBase):
    PROJECT_ID = "project-id"
    INSTANCE_ID = "instance-id"
    INSTANCE_NAME = "projects/" + PROJECT_ID + "/instances/" + INSTANCE_ID
    DATABASE_ID = "database-id"
    DATABASE_NAME = INSTANCE_NAME + "/databases/" + DATABASE_ID
    SESSION_ID = "session-id"
    SESSION_NAME = DATABASE_NAME + "/sessions/" + SESSION_ID
    DATABASE_ROLE = "dummy-role"
    BASE_ATTRIBUTES = {
        "db.type": "spanner",
        "db.url": "spanner.googleapis.com",
        "db.instance": DATABASE_NAME,
        "net.host.name": "spanner.googleapis.com",
        "gcp.client.service": "spanner",
        "gcp.client.version": LIB_VERSION,
        "gcp.client.repo": "googleapis/python-spanner",
        "gcp.resource.name": GCP_RESOURCE_NAME_PREFIX + DATABASE_NAME,
        "cloud.region": "global",
    }
    enrich_with_otel_scope(BASE_ATTRIBUTES)

    def _getTargetClass(self):
        return Session

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    @staticmethod
    def _make_database(
        name=DATABASE_NAME,
        database_role=None,
        default_transaction_options=DefaultTransactionOptions(),
    ):
        database = mock.create_autospec(Database, instance=True)
        database.name = name
        database.database_id = name.split("/")[-1]
        database.log_commit_stats = False
        database.database_role = database_role
        database._route_to_leader_enabled = True
        database.default_transaction_options = default_transaction_options
        database._instance = mock.Mock()
        database._instance.instance_id = name.split("/")[3]
        database._instance._client = mock.Mock()
        database._instance._client.project = name.split("/")[1]
        database._instance._client._client_context = None
        inject_into_mock_database(database)

        return database

    @staticmethod
    def _make_session_pb(name, labels=None, database_role=None):
        return SessionRequestProto(name=name, labels=labels, creator_role=database_role)

    def _make_spanner_api(self):
        return mock.Mock(autospec=SpannerClient, instance=True)

    def test_constructor_wo_labels(self):
        database = self._make_database()
        session = self._make_one(database)
        self.assertIs(session.session_id, None)
        self.assertIs(session._database, database)
        self.assertEqual(session.labels, {})

    def test_constructor_w_database_role(self):
        database = self._make_database(database_role=self.DATABASE_ROLE)
        session = self._make_one(database, database_role=self.DATABASE_ROLE)
        self.assertIs(session.session_id, None)
        self.assertIs(session._database, database)
        self.assertEqual(session.database_role, self.DATABASE_ROLE)

    def test_constructor_wo_database_role(self):
        database = self._make_database()
        session = self._make_one(database)
        self.assertIs(session.session_id, None)
        self.assertIs(session._database, database)
        self.assertIs(session.database_role, None)

    def test_constructor_w_labels(self):
        database = self._make_database()
        labels = {"foo": "bar"}
        session = self._make_one(database, labels=labels)
        self.assertIs(session.session_id, None)
        self.assertIs(session._database, database)
        self.assertEqual(session.labels, labels)

    def test___lt___(self):
        database = self._make_database()
        lhs = self._make_one(database)
        lhs._session_id = b"123"
        rhs = self._make_one(database)
        rhs._session_id = b"234"
        self.assertTrue(lhs < rhs)

    def test_name_property_wo_session_id(self):
        database = self._make_database()
        session = self._make_one(database)

        with self.assertRaises(ValueError):
            (session.name)

    def test_name_property_w_session_id(self):
        database = self._make_database()
        session = self._make_one(database)
        session._session_id = self.SESSION_ID
        self.assertEqual(session.name, self.SESSION_NAME)

    def test_create_w_session_id(self):
        database = self._make_database()
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        with self.assertRaises(ValueError):
            session.create()

        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_create_w_database_role(self, mock_region):
        session_pb = self._make_session_pb(
            self.SESSION_NAME, database_role=self.DATABASE_ROLE
        )
        gax_api = self._make_spanner_api()
        gax_api.create_session.return_value = session_pb
        database = self._make_database(database_role=self.DATABASE_ROLE)
        database.spanner_api = gax_api
        session = self._make_one(database, database_role=self.DATABASE_ROLE)

        session.create()

        self.assertEqual(session.session_id, self.SESSION_ID)
        self.assertEqual(session.database_role, self.DATABASE_ROLE)
        session_template = SessionRequestProto(creator_role=self.DATABASE_ROLE)

        request = CreateSessionRequest(
            database=database.name,
            session=session_template,
        )

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        gax_api.create_session.assert_called_once_with(
            request=request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    req_id,
                ),
            ],
        )

        self.assertSpanAttributes(
            "CloudSpanner.CreateSession",
            attributes=dict(
                TestSession.BASE_ATTRIBUTES, x_goog_spanner_request_id=req_id
            ),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_create_session_span_annotations(self, mock_region):
        session_pb = self._make_session_pb(
            self.SESSION_NAME, database_role=self.DATABASE_ROLE
        )

        gax_api = self._make_spanner_api()
        gax_api.create_session.return_value = session_pb
        database = self._make_database(database_role=self.DATABASE_ROLE)
        database.spanner_api = gax_api
        session = self._make_one(database, database_role=self.DATABASE_ROLE)

        with trace_call("TestSessionSpan", session) as span:
            session.create()

            self.assertEqual(session.session_id, self.SESSION_ID)
            self.assertEqual(session.database_role, self.DATABASE_ROLE)
            session_template = SessionRequestProto(creator_role=self.DATABASE_ROLE)

            request = CreateSessionRequest(
                database=database.name,
                session=session_template,
            )

            gax_api.create_session.assert_called_once_with(
                request=request,
                metadata=[
                    ("google-cloud-resource-prefix", database.name),
                    ("x-goog-spanner-route-to-leader", "true"),
                    (
                        "x-goog-spanner-request-id",
                        f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                    ),
                ],
            )

            wantEventNames = ["Creating Session"]
            self.assertSpanEvents("TestSessionSpan", wantEventNames, span)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_create_wo_database_role(self, mock_region):
        session_pb = self._make_session_pb(self.SESSION_NAME)
        gax_api = self._make_spanner_api()
        gax_api.create_session.return_value = session_pb
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session.create()

        self.assertEqual(session.session_id, self.SESSION_ID)
        self.assertIsNone(session.database_role)

        request = CreateSessionRequest(
            database=database.name,
        )

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        gax_api.create_session.assert_called_once_with(
            request=request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

        self.assertSpanAttributes(
            "CloudSpanner.CreateSession",
            attributes=dict(
                TestSession.BASE_ATTRIBUTES, x_goog_spanner_request_id=req_id
            ),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_create_ok(self, mock_region):
        session_pb = self._make_session_pb(self.SESSION_NAME)
        gax_api = self._make_spanner_api()
        gax_api.create_session.return_value = session_pb
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)

        session.create()

        self.assertEqual(session.session_id, self.SESSION_ID)

        request = CreateSessionRequest(
            database=database.name,
        )

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        gax_api.create_session.assert_called_once_with(
            request=request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    req_id,
                ),
            ],
        )

        self.assertSpanAttributes(
            "CloudSpanner.CreateSession",
            attributes=dict(
                TestSession.BASE_ATTRIBUTES, x_goog_spanner_request_id=req_id
            ),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_create_w_labels(self, mock_region):
        labels = {"foo": "bar"}
        session_pb = self._make_session_pb(self.SESSION_NAME, labels=labels)
        gax_api = self._make_spanner_api()
        gax_api.create_session.return_value = session_pb
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database, labels=labels)

        session.create()

        self.assertEqual(session.session_id, self.SESSION_ID)

        request = CreateSessionRequest(
            database=database.name,
            session=SessionRequestProto(labels=labels),
        )

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        gax_api.create_session.assert_called_once_with(
            request=request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    req_id,
                ),
            ],
        )

        self.assertSpanAttributes(
            "CloudSpanner.CreateSession",
            attributes=dict(
                TestSession.BASE_ATTRIBUTES, foo="bar", x_goog_spanner_request_id=req_id
            ),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_create_error(self, mock_region):
        gax_api = self._make_spanner_api()
        gax_api.create_session.side_effect = Unknown("error")
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)

        # Exception has request_id attribute added
        with self.assertRaises(Unknown) as cm:
            session.create()
        # Verify the exception has request_id attribute
        self.assertTrue(hasattr(cm.exception, "request_id"))

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        self.assertSpanAttributes(
            "CloudSpanner.CreateSession",
            status=StatusCode.ERROR,
            attributes=dict(
                TestSession.BASE_ATTRIBUTES, x_goog_spanner_request_id=req_id
            ),
        )

    def test_exists_wo_session_id(self):
        database = self._make_database()
        session = self._make_one(database)
        self.assertFalse(session.exists())

        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_exists_hit(self, mock_region):
        session_pb = self._make_session_pb(self.SESSION_NAME)
        gax_api = self._make_spanner_api()
        gax_api.get_session.return_value = session_pb
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        self.assertTrue(session.exists())

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        gax_api.get_session.assert_called_once_with(
            name=self.SESSION_NAME,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    req_id,
                ),
            ],
        )

        self.assertSpanAttributes(
            "CloudSpanner.GetSession",
            attributes=dict(
                TestSession.BASE_ATTRIBUTES,
                session_found=True,
                x_goog_spanner_request_id=req_id,
            ),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_exists_miss(self, mock_region):
        gax_api = self._make_spanner_api()
        gax_api.get_session.side_effect = NotFound("testing")
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        self.assertFalse(session.exists())

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        gax_api.get_session.assert_called_once_with(
            name=self.SESSION_NAME,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    req_id,
                ),
            ],
        )

        self.assertSpanAttributes(
            "CloudSpanner.GetSession",
            attributes=dict(
                TestSession.BASE_ATTRIBUTES,
                session_found=False,
                x_goog_spanner_request_id=req_id,
            ),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_exists_error(self, mock_region):
        gax_api = self._make_spanner_api()
        gax_api.get_session.side_effect = Unknown("testing")
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        # Exception has request_id attribute added
        with self.assertRaises(Unknown) as cm:
            session.exists()
        # Verify the exception has request_id attribute
        self.assertTrue(hasattr(cm.exception, "request_id"))

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        gax_api.get_session.assert_called_once_with(
            name=self.SESSION_NAME,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    req_id,
                ),
            ],
        )

        self.assertSpanAttributes(
            "CloudSpanner.GetSession",
            status=StatusCode.ERROR,
            attributes=dict(
                TestSession.BASE_ATTRIBUTES, x_goog_spanner_request_id=req_id
            ),
        )

    def test_ping_wo_session_id(self):
        database = self._make_database()
        session = self._make_one(database)
        with self.assertRaises(ValueError):
            session.ping()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_ping_hit(self, mock_region):
        gax_api = self._make_spanner_api()
        gax_api.execute_sql.return_value = "1"
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        session.ping()

        request = ExecuteSqlRequest(
            session=self.SESSION_NAME,
            sql="SELECT 1",
        )

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        gax_api.execute_sql.assert_called_once_with(
            request=request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                (
                    "x-goog-spanner-request-id",
                    req_id,
                ),
            ],
        )

        self.assertSpanAttributes(
            "CloudSpanner.Session.ping",
            attributes=dict(self.BASE_ATTRIBUTES, x_goog_spanner_request_id=req_id),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_ping_invokes_metrics_capture(self, mock_region):
        gax_api = self._make_spanner_api()
        gax_api.execute_sql.return_value = "1"
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        with mock.patch(
            "google.cloud.spanner_v1.session.MetricsCapture"
        ) as mock_capture:
            session.ping()
            mock_capture.assert_called_once_with(session._resource_info)

    def test_resource_info_fallback_when_database_lacks_resource_info(self):
        database = mock.Mock(spec=["_instance", "database_id"])
        database.database_id = "test-db"
        instance = mock.Mock(spec=["_client", "instance_id"])
        instance.instance_id = "test-inst"
        client = mock.Mock(spec=["project"])
        client.project = "test-proj"
        instance._client = client
        database._instance = instance

        session = self._make_one(database)
        self.assertEqual(
            session._resource_info,
            {"project": "test-proj", "instance": "test-inst", "database": "test-db"},
        )

        session._database = None
        self.assertIsNone(session._resource_info)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_ping_miss(self, mock_region):
        gax_api = self._make_spanner_api()
        gax_api.execute_sql.side_effect = NotFound("testing")
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        with self.assertRaises(NotFound):
            session.ping()

        request = ExecuteSqlRequest(
            session=self.SESSION_NAME,
            sql="SELECT 1",
        )

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        gax_api.execute_sql.assert_called_once_with(
            request=request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                (
                    "x-goog-spanner-request-id",
                    req_id,
                ),
            ],
        )

        self.assertSpanAttributes(
            "CloudSpanner.Session.ping",
            status=StatusCode.ERROR,
            attributes=dict(self.BASE_ATTRIBUTES, x_goog_spanner_request_id=req_id),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_ping_error(self, mock_region):
        gax_api = self._make_spanner_api()
        gax_api.execute_sql.side_effect = Unknown("testing")
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        with self.assertRaises(Unknown):
            session.ping()

        request = ExecuteSqlRequest(
            session=self.SESSION_NAME,
            sql="SELECT 1",
        )

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        gax_api.execute_sql.assert_called_once_with(
            request=request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                (
                    "x-goog-spanner-request-id",
                    req_id,
                ),
            ],
        )

        self.assertSpanAttributes(
            "CloudSpanner.Session.ping",
            status=StatusCode.ERROR,
            attributes=dict(self.BASE_ATTRIBUTES, x_goog_spanner_request_id=req_id),
        )

    def test_delete_wo_session_id(self):
        database = self._make_database()
        session = self._make_one(database)

        with self.assertRaises(ValueError):
            session.delete()

        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_delete_hit(self, mock_region):
        gax_api = self._make_spanner_api()
        gax_api.delete_session.return_value = None
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        session.delete()

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        gax_api.delete_session.assert_called_once_with(
            name=self.SESSION_NAME,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                (
                    "x-goog-spanner-request-id",
                    req_id,
                ),
            ],
        )

        attrs = {"session.id": session._session_id, "session.name": session.name}
        attrs.update(TestSession.BASE_ATTRIBUTES)
        self.assertSpanAttributes(
            "CloudSpanner.DeleteSession",
            attributes=dict(attrs, x_goog_spanner_request_id=req_id),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_delete_miss(self, mock_region):
        gax_api = self._make_spanner_api()
        gax_api.delete_session.side_effect = NotFound("testing")
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        with self.assertRaises(NotFound):
            session.delete()

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        gax_api.delete_session.assert_called_once_with(
            name=self.SESSION_NAME,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                (
                    "x-goog-spanner-request-id",
                    req_id,
                ),
            ],
        )

        attrs = {
            "session.id": session._session_id,
            "session.name": session.name,
            "x_goog_spanner_request_id": req_id,
        }
        attrs.update(TestSession.BASE_ATTRIBUTES)

        self.assertSpanAttributes(
            "CloudSpanner.DeleteSession",
            status=StatusCode.ERROR,
            attributes=attrs,
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_delete_error(self, mock_region):
        gax_api = self._make_spanner_api()
        gax_api.delete_session.side_effect = Unknown("testing")
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        with self.assertRaises(Unknown):
            session.delete()

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        gax_api.delete_session.assert_called_once_with(
            name=self.SESSION_NAME,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                (
                    "x-goog-spanner-request-id",
                    req_id,
                ),
            ],
        )

        attrs = {
            "session.id": session._session_id,
            "session.name": session.name,
            "x_goog_spanner_request_id": req_id,
        }
        attrs.update(TestSession.BASE_ATTRIBUTES)

        self.assertSpanAttributes(
            "CloudSpanner.DeleteSession",
            status=StatusCode.ERROR,
            attributes=attrs,
        )

    def test_snapshot_not_created(self):
        database = self._make_database()
        session = self._make_one(database)

        with self.assertRaises(ValueError):
            session.snapshot()

    def test_snapshot_created(self):
        database = self._make_database()
        session = self._make_one(database)
        session._session_id = "DEADBEEF"  # emulate 'session.create()'

        snapshot = session.snapshot()

        self.assertIsInstance(snapshot, Snapshot)
        self.assertIs(snapshot._session, session)
        self.assertTrue(snapshot._strong)
        self.assertFalse(snapshot._multi_use)

    def test_snapshot_created_w_multi_use(self):
        database = self._make_database()
        session = self._make_one(database)
        session._session_id = "DEADBEEF"  # emulate 'session.create()'

        snapshot = session.snapshot(multi_use=True)

        self.assertIsInstance(snapshot, Snapshot)
        self.assertTrue(snapshot._session is session)
        self.assertTrue(snapshot._strong)
        self.assertTrue(snapshot._multi_use)

    def test_read_not_created(self):
        TABLE_NAME = "citizens"
        COLUMNS = ["email", "first_name", "last_name", "age"]
        KEYS = ["bharney@example.com", "phred@example.com"]
        KEYSET = KeySet(keys=KEYS)
        database = self._make_database()
        session = self._make_one(database)

        with self.assertRaises(ValueError):
            session.read(TABLE_NAME, COLUMNS, KEYSET)

    def test_read(self):
        TABLE_NAME = "citizens"
        COLUMNS = ["email", "first_name", "last_name", "age"]
        KEYS = ["bharney@example.com", "phred@example.com"]
        KEYSET = KeySet(keys=KEYS)
        INDEX = "email-address-index"
        LIMIT = 20
        database = self._make_database()
        session = self._make_one(database)
        session._session_id = "DEADBEEF"

        with mock.patch("google.cloud.spanner_v1.session.Snapshot") as snapshot:
            found = session.read(TABLE_NAME, COLUMNS, KEYSET, index=INDEX, limit=LIMIT)

        self.assertIs(found, snapshot().read.return_value)

        snapshot().read.assert_called_once_with(
            TABLE_NAME,
            COLUMNS,
            KEYSET,
            INDEX,
            LIMIT,
            column_info=None,
        )

    def test_execute_sql_not_created(self):
        SQL = "SELECT first_name, age FROM citizens"
        database = self._make_database()
        session = self._make_one(database)

        with self.assertRaises(ValueError):
            session.execute_sql(SQL)

    def test_execute_sql_defaults(self):
        SQL = "SELECT first_name, age FROM citizens"
        database = self._make_database()
        session = self._make_one(database)
        session._session_id = "DEADBEEF"

        with mock.patch("google.cloud.spanner_v1.session.Snapshot") as snapshot:
            found = session.execute_sql(SQL)

        self.assertIs(found, snapshot().execute_sql.return_value)

        snapshot().execute_sql.assert_called_once_with(
            SQL,
            None,
            None,
            None,
            query_options=None,
            request_options=None,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            column_info=None,
        )

    def test_execute_sql_non_default_retry(self):
        SQL = "SELECT first_name, age FROM citizens"
        database = self._make_database()
        session = self._make_one(database)
        session._session_id = "DEADBEEF"

        params = Struct(fields={"foo": Value(string_value="bar")})
        param_types = {"foo": TypeCode.STRING}

        with mock.patch("google.cloud.spanner_v1.session.Snapshot") as snapshot:
            found = session.execute_sql(
                SQL, params, param_types, "PLAN", retry=None, timeout=None
            )

        self.assertIs(found, snapshot().execute_sql.return_value)

        snapshot().execute_sql.assert_called_once_with(
            SQL,
            params,
            param_types,
            "PLAN",
            query_options=None,
            request_options=None,
            timeout=None,
            retry=None,
            column_info=None,
        )

    def test_execute_sql_explicit(self):
        SQL = "SELECT first_name, age FROM citizens"
        database = self._make_database()
        session = self._make_one(database)
        session._session_id = "DEADBEEF"

        params = Struct(fields={"foo": Value(string_value="bar")})
        param_types = {"foo": TypeCode.STRING}

        with mock.patch("google.cloud.spanner_v1.session.Snapshot") as snapshot:
            found = session.execute_sql(SQL, params, param_types, "PLAN")

        self.assertIs(found, snapshot().execute_sql.return_value)

        snapshot().execute_sql.assert_called_once_with(
            SQL,
            params,
            param_types,
            "PLAN",
            query_options=None,
            request_options=None,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            column_info=None,
        )

    def test_batch_not_created(self):
        database = self._make_database()
        session = self._make_one(database)

        with self.assertRaises(ValueError):
            session.batch()

    def test_batch_created(self):
        database = self._make_database()
        session = self._make_one(database)
        session._session_id = "DEADBEEF"

        batch = session.batch()

        self.assertIsInstance(batch, Batch)
        self.assertIs(batch._session, session)

    def test_transaction_not_created(self):
        database = self._make_database()
        session = self._make_one(database)

        with self.assertRaises(ValueError):
            session.transaction()

    def test_transaction_created(self):
        database = self._make_database()
        session = self._make_one(database)
        session._session_id = "DEADBEEF"

        transaction = session.transaction()

        self.assertIsInstance(transaction, Transaction)
        self.assertIs(transaction._session, session)

    def test_run_in_transaction_callback_raises_non_gax_error(self):
        TABLE_NAME = "citizens"
        COLUMNS = ["email", "first_name", "last_name", "age"]
        VALUES = [
            ["phred@exammple.com", "Phred", "Phlyntstone", 32],
            ["bharney@example.com", "Bharney", "Rhubble", 31],
        ]
        TRANSACTION_ID = b"FACEDACE"
        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.rollback.return_value = None
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        called_with = []

        class Testing(Exception):
            pass

        def unit_of_work(txn, *args, **kw):
            called_with.append((txn, args, kw))
            txn.insert(TABLE_NAME, COLUMNS, VALUES)
            raise Testing()

        with self.assertRaises(Testing):
            session.run_in_transaction(unit_of_work)

        self.assertEqual(len(called_with), 1)
        txn, args, kw = called_with[0]
        self.assertIsInstance(txn, Transaction)
        self.assertIsNone(txn.committed)
        self.assertTrue(txn.rolled_back)
        self.assertEqual(args, ())
        self.assertEqual(kw, {})
        # Transaction only has mutation operations.
        # Exception was raised before commit, hence transaction did not begin.
        # Therefore rollback and begin transaction were not called.
        gax_api.rollback.assert_not_called()
        gax_api.begin_transaction.assert_not_called()

    def test_run_in_transaction_callback_raises_non_abort_rpc_error(self):
        TABLE_NAME = "citizens"
        COLUMNS = ["email", "first_name", "last_name", "age"]
        VALUES = [
            ["phred@exammple.com", "Phred", "Phlyntstone", 32],
            ["bharney@example.com", "Bharney", "Rhubble", 31],
        ]
        TRANSACTION_ID = b"FACEDACE"
        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.rollback.return_value = None
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        called_with = []

        def unit_of_work(txn, *args, **kw):
            called_with.append((txn, args, kw))
            txn.insert(TABLE_NAME, COLUMNS, VALUES)
            raise Cancelled("error")

        with self.assertRaises(Cancelled):
            session.run_in_transaction(unit_of_work)

        self.assertEqual(len(called_with), 1)
        txn, args, kw = called_with[0]
        self.assertIsInstance(txn, Transaction)
        self.assertIsNone(txn.committed)
        self.assertFalse(txn.rolled_back)
        self.assertEqual(args, ())
        self.assertEqual(kw, {})

        gax_api.rollback.assert_not_called()

    def test_run_in_transaction_retry_callback_raises_abort(self):
        session = build_session()
        database = session._database

        # Build API responses.
        api = database.spanner_api
        begin_transaction = api.begin_transaction
        streaming_read = api.streaming_read
        streaming_read.side_effect = [_make_rpc_error(Aborted), []]

        # Run in transaction.
        def unit_of_work(transaction):
            transaction.begin()
            list(transaction.read(TABLE_NAME, COLUMNS, KEYSET))

        session.create()
        with mock.patch("google.cloud.spanner_v1._helpers.time.sleep") as sleep_mock:
            session.run_in_transaction(unit_of_work)

        self.assertEqual(begin_transaction.call_count, 2)
        sleep_mock.assert_called_once()

        begin_transaction.assert_called_with(
            request=BeginTransactionRequest(
                session=session.name,
                options=TransactionOptions(read_write=TransactionOptions.ReadWrite()),
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.4.1",
                ),
            ],
        )

    def test_run_in_transaction_retry_callback_raises_abort_multiplexed(self):
        session = build_session(is_multiplexed=True)
        database = session._database
        api = database.spanner_api

        # Build API responses
        previous_transaction_id = b"transaction-id"
        begin_transaction = api.begin_transaction
        begin_transaction.return_value = build_transaction_pb(
            id=previous_transaction_id
        )

        streaming_read = api.streaming_read
        streaming_read.side_effect = [_make_rpc_error(Aborted), []]

        # Run in transaction.
        def unit_of_work(transaction):
            transaction.begin()
            list(transaction.read(TABLE_NAME, COLUMNS, KEYSET))

        session.create()
        with mock.patch("google.cloud.spanner_v1._helpers.time.sleep") as sleep_mock:
            session.run_in_transaction(unit_of_work)

        # Verify retried BeginTransaction API call.
        self.assertEqual(begin_transaction.call_count, 2)
        sleep_mock.assert_called_once()

        begin_transaction.assert_called_with(
            request=BeginTransactionRequest(
                session=session.name,
                options=TransactionOptions(
                    read_write=TransactionOptions.ReadWrite(
                        multiplexed_session_previous_transaction_id=previous_transaction_id
                    )
                ),
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.4.1",
                ),
            ],
        )

    def test_run_in_transaction_retry_commit_raises_abort_multiplexed(self):
        session = build_session(is_multiplexed=True)
        database = session._database

        # Build API responses
        api = database.spanner_api
        previous_transaction_id = b"transaction-id"
        begin_transaction = api.begin_transaction
        begin_transaction.return_value = build_transaction_pb(
            id=previous_transaction_id
        )

        commit = api.commit
        commit.side_effect = [_make_rpc_error(Aborted), build_commit_response_pb()]

        # Run in transaction.
        def unit_of_work(transaction):
            transaction.begin()
            list(transaction.read(TABLE_NAME, COLUMNS, KEYSET))

        session.create()
        with mock.patch("google.cloud.spanner_v1._helpers.time.sleep") as sleep_mock:
            session.run_in_transaction(unit_of_work)

        # Verify retried BeginTransaction API call.
        self.assertEqual(begin_transaction.call_count, 2)
        sleep_mock.assert_called_once()

        begin_transaction.assert_called_with(
            request=BeginTransactionRequest(
                session=session.name,
                options=TransactionOptions(
                    read_write=TransactionOptions.ReadWrite(
                        multiplexed_session_previous_transaction_id=previous_transaction_id
                    )
                ),
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.5.1",
                ),
            ],
        )

    def test_run_in_transaction_w_args_w_kwargs_wo_abort(self):
        VALUES = [
            ["phred@exammple.com", "Phred", "Phlyntstone", 32],
            ["bharney@example.com", "Bharney", "Rhubble", 31],
        ]
        TRANSACTION_ID = b"FACEDACE"
        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        response = CommitResponse(commit_timestamp=now_pb)
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.commit.return_value = response
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        called_with = []

        def unit_of_work(txn, *args, **kw):
            called_with.append((txn, args, kw))
            txn.insert(TABLE_NAME, COLUMNS, VALUES)
            return 42

        return_value = session.run_in_transaction(unit_of_work, "abc", some_arg="def")

        self.assertEqual(len(called_with), 1)
        txn, args, kw = called_with[0]
        self.assertIsInstance(txn, Transaction)
        self.assertEqual(return_value, 42)
        self.assertEqual(args, ("abc",))
        self.assertEqual(kw, {"some_arg": "def"})

        expected_options = TransactionOptions(read_write=TransactionOptions.ReadWrite())
        gax_api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )
        request = CommitRequest(
            session=self.SESSION_NAME,
            mutations=txn._mutations,
            transaction_id=TRANSACTION_ID,
        )
        gax_api.commit.assert_called_once_with(
            request=request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                ),
            ],
        )

    def test_run_in_transaction_w_commit_error(self):
        TABLE_NAME = "citizens"
        COLUMNS = ["email", "first_name", "last_name", "age"]
        VALUES = [
            ["phred@exammple.com", "Phred", "Phlyntstone", 32],
            ["bharney@example.com", "Bharney", "Rhubble", 31],
        ]
        database = self._make_database()

        api = database.spanner_api = build_spanner_api()
        begin_transaction = api.begin_transaction
        commit = api.commit

        commit.side_effect = Unknown("error")

        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        called_with = []

        def unit_of_work(txn, *args, **kw):
            called_with.append((txn, args, kw))
            txn.insert(TABLE_NAME, COLUMNS, VALUES)

        # Exception has request_id attribute added
        with self.assertRaises(Unknown) as context:
            session.run_in_transaction(unit_of_work)
        self.assertTrue(hasattr(context.exception, "request_id"))

        self.assertEqual(len(called_with), 1)
        txn, args, kw = called_with[0]
        self.assertEqual(txn.committed, None)
        self.assertEqual(args, ())
        self.assertEqual(kw, {})

        begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=session.name,
                options=TransactionOptions(read_write=TransactionOptions.ReadWrite()),
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

        api.commit.assert_called_once_with(
            request=CommitRequest(
                session=session.name,
                mutations=txn._mutations,
                transaction_id=begin_transaction.return_value.id,
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                ),
            ],
        )

    def test_run_in_transaction_w_abort_no_retry_metadata(self):
        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        aborted = _make_rpc_error(Aborted, trailing_metadata=[])
        response = CommitResponse(commit_timestamp=now_pb)
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.commit.side_effect = [aborted, response]
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        called_with = []

        def unit_of_work(txn, *args, **kw):
            called_with.append((txn, args, kw))
            txn.insert(TABLE_NAME, COLUMNS, VALUES)
            return "answer"

        return_value = session.run_in_transaction(
            unit_of_work, "abc", some_arg="def", default_retry_delay=0
        )

        self.assertEqual(len(called_with), 2)
        for index, (txn, args, kw) in enumerate(called_with):
            self.assertIsInstance(txn, Transaction)
            self.assertEqual(return_value, "answer")
            self.assertEqual(args, ("abc",))
            self.assertEqual(kw, {"some_arg": "def"})

        self.assertEqual(
            gax_api.begin_transaction.call_args_list,
            [
                mock.call(
                    request=BeginTransactionRequest(
                        session=session.name,
                        options=TransactionOptions(
                            read_write=TransactionOptions.ReadWrite()
                        ),
                    ),
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                        ),
                    ],
                ),
                mock.call(
                    request=BeginTransactionRequest(
                        session=session.name,
                        options=TransactionOptions(
                            read_write=TransactionOptions.ReadWrite()
                        ),
                    ),
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.3.1",
                        ),
                    ],
                ),
            ],
        )
        request = CommitRequest(
            session=self.SESSION_NAME,
            mutations=txn._mutations,
            transaction_id=TRANSACTION_ID,
        )
        self.assertEqual(
            gax_api.commit.call_args_list,
            [
                mock.call(
                    request=request,
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                        ),
                    ],
                ),
                mock.call(
                    request=request,
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.4.1",
                        ),
                    ],
                ),
            ],
        )

    def test_run_in_transaction_w_abort_w_retry_metadata(self):
        RETRY_SECONDS = 12
        RETRY_NANOS = 3456
        retry_info = RetryInfo(
            retry_delay=Duration(seconds=RETRY_SECONDS, nanos=RETRY_NANOS)
        )
        trailing_metadata = [
            ("google.rpc.retryinfo-bin", retry_info.SerializeToString())
        ]
        aborted = _make_rpc_error(Aborted, trailing_metadata=trailing_metadata)
        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        response = CommitResponse(commit_timestamp=now_pb)
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.commit.side_effect = [aborted, response]
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        called_with = []

        def unit_of_work(txn, *args, **kw):
            called_with.append((txn, args, kw))
            txn.insert(TABLE_NAME, COLUMNS, VALUES)

        with mock.patch("google.cloud.spanner_v1._helpers.time.sleep") as sleep_mock:
            session.run_in_transaction(unit_of_work, "abc", some_arg="def")

        sleep_mock.assert_called_once_with(RETRY_SECONDS + RETRY_NANOS / 1.0e9)
        self.assertEqual(len(called_with), 2)

        for index, (txn, args, kw) in enumerate(called_with):
            self.assertIsInstance(txn, Transaction)
            if index == 1:
                self.assertEqual(txn.committed, now)
            else:
                self.assertIsNone(txn.committed)
            self.assertEqual(args, ("abc",))
            self.assertEqual(kw, {"some_arg": "def"})

        self.assertEqual(
            gax_api.begin_transaction.call_args_list,
            [
                mock.call(
                    request=BeginTransactionRequest(
                        session=session.name,
                        options=TransactionOptions(
                            read_write=TransactionOptions.ReadWrite()
                        ),
                    ),
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                        ),
                    ],
                ),
                mock.call(
                    request=BeginTransactionRequest(
                        session=session.name,
                        options=TransactionOptions(
                            read_write=TransactionOptions.ReadWrite()
                        ),
                    ),
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.3.1",
                        ),
                    ],
                ),
            ],
        )
        request = CommitRequest(
            session=self.SESSION_NAME,
            mutations=txn._mutations,
            transaction_id=TRANSACTION_ID,
        )
        self.assertEqual(
            gax_api.commit.call_args_list,
            [
                mock.call(
                    request=request,
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                        ),
                    ],
                ),
                mock.call(
                    request=request,
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.4.1",
                        ),
                    ],
                ),
            ],
        )

    def test_run_in_transaction_w_callback_raises_abort_wo_metadata(self):
        RETRY_SECONDS = 1
        RETRY_NANOS = 3456
        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        response = CommitResponse(commit_timestamp=now_pb)
        retry_info = RetryInfo(
            retry_delay=Duration(seconds=RETRY_SECONDS, nanos=RETRY_NANOS)
        )
        trailing_metadata = [
            ("google.rpc.retryinfo-bin", retry_info.SerializeToString())
        ]
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.commit.side_effect = [response]
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        called_with = []

        def unit_of_work(txn, *args, **kw):
            called_with.append((txn, args, kw))
            if len(called_with) < 2:
                raise _make_rpc_error(Aborted, trailing_metadata)
            txn.insert(TABLE_NAME, COLUMNS, VALUES)

        with mock.patch("google.cloud.spanner_v1._helpers.time.sleep") as sleep_mock:
            session.run_in_transaction(unit_of_work)

        sleep_mock.assert_called_once_with(RETRY_SECONDS + RETRY_NANOS / 1.0e9)
        self.assertEqual(len(called_with), 2)
        for index, (txn, args, kw) in enumerate(called_with):
            self.assertIsInstance(txn, Transaction)
            if index == 0:
                self.assertIsNone(txn.committed)
            else:
                self.assertEqual(txn.committed, now)
            self.assertEqual(args, ())
            self.assertEqual(kw, {})

        expected_options = TransactionOptions(read_write=TransactionOptions.ReadWrite())

        # First call was aborted before commit operation, therefore no begin rpc was made during first attempt.
        gax_api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )
        request = CommitRequest(
            session=self.SESSION_NAME,
            mutations=txn._mutations,
            transaction_id=TRANSACTION_ID,
        )
        gax_api.commit.assert_called_once_with(
            request=request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                ),
            ],
        )

    def test_run_in_transaction_w_abort_w_retry_metadata_deadline(self):
        RETRY_SECONDS = 1
        RETRY_NANOS = 3456
        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        response = CommitResponse(commit_timestamp=now_pb)
        retry_info = RetryInfo(
            retry_delay=Duration(seconds=RETRY_SECONDS, nanos=RETRY_NANOS)
        )
        trailing_metadata = [
            ("google.rpc.retryinfo-bin", retry_info.SerializeToString())
        ]
        aborted = _make_rpc_error(Aborted, trailing_metadata=trailing_metadata)
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.commit.side_effect = [aborted, response]
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        called_with = []

        def unit_of_work(txn, *args, **kw):
            called_with.append((txn, args, kw))
            txn.insert(TABLE_NAME, COLUMNS, VALUES)

        main_thread = threading.current_thread()
        _results = [1, 1.5]

        # retry once w/ timeout_secs=1
        def _time():
            if threading.current_thread() is main_thread:
                if len(_results) > 1:
                    return _results.pop(0)
                return _results[0]
            return 1.0

        with mock.patch("google.cloud.spanner_v1._helpers.time.time", _time):
            with mock.patch(
                "google.cloud.spanner_v1._helpers.time.sleep"
            ) as sleep_mock:
                # Exception has request_id attribute added
                with self.assertRaises(Aborted) as context:
                    session.run_in_transaction(unit_of_work, "abc", timeout_secs=1)
                self.assertTrue(hasattr(context.exception, "request_id"))

        sleep_mock.assert_not_called()

        self.assertEqual(len(called_with), 1)
        txn, args, kw = called_with[0]
        self.assertIsInstance(txn, Transaction)
        self.assertIsNone(txn.committed)
        self.assertEqual(args, ("abc",))
        self.assertEqual(kw, {})

        expected_options = TransactionOptions(read_write=TransactionOptions.ReadWrite())
        gax_api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )
        request = CommitRequest(
            session=self.SESSION_NAME,
            mutations=txn._mutations,
            transaction_id=TRANSACTION_ID,
        )
        gax_api.commit.assert_called_once_with(
            request=request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                ),
            ],
        )

    def test_run_in_transaction_w_timeout(self):
        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        aborted = _make_rpc_error(Aborted, trailing_metadata=[])
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.commit.side_effect = aborted
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        called_with = []

        def unit_of_work(txn, *args, **kw):
            called_with.append((txn, args, kw))
            txn.insert(TABLE_NAME, COLUMNS, VALUES)

        main_thread = threading.current_thread()
        _results = [1, 2, 4, 8]

        # retry several times to check backoff
        def _time():
            if threading.current_thread() is main_thread:
                if len(_results) > 1:
                    return _results.pop(0)
                return _results[0]
            return 1.0

        with (
            mock.patch("google.cloud.spanner_v1._helpers.time.time", _time),
            mock.patch(
                "google.cloud.spanner_v1._helpers.random.random", return_value=0
            ),
            mock.patch("google.cloud.spanner_v1._helpers.time.sleep") as sleep_mock,
        ):
            # Exception has request_id attribute added
            with self.assertRaises(Aborted) as context:
                session.run_in_transaction(unit_of_work, timeout_secs=8)
            self.assertTrue(hasattr(context.exception, "request_id"))

        # unpacking call args into list
        call_args = [call_[0][0] for call_ in sleep_mock.call_args_list]
        call_args = list(map(int, call_args))
        assert call_args == [2, 4]
        assert sleep_mock.call_count == 2

        self.assertEqual(len(called_with), 3)
        for txn, args, kw in called_with:
            self.assertIsInstance(txn, Transaction)
            self.assertIsNone(txn.committed)
            self.assertEqual(args, ())
            self.assertEqual(kw, {})

        self.assertEqual(
            gax_api.begin_transaction.call_args_list,
            [
                mock.call(
                    request=BeginTransactionRequest(
                        session=session.name,
                        options=TransactionOptions(
                            read_write=TransactionOptions.ReadWrite()
                        ),
                    ),
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                        ),
                    ],
                ),
                mock.call(
                    request=BeginTransactionRequest(
                        session=session.name,
                        options=TransactionOptions(
                            read_write=TransactionOptions.ReadWrite()
                        ),
                    ),
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.3.1",
                        ),
                    ],
                ),
                mock.call(
                    request=BeginTransactionRequest(
                        session=session.name,
                        options=TransactionOptions(
                            read_write=TransactionOptions.ReadWrite()
                        ),
                    ),
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.5.1",
                        ),
                    ],
                ),
            ],
        )
        request = CommitRequest(
            session=self.SESSION_NAME,
            mutations=txn._mutations,
            transaction_id=TRANSACTION_ID,
        )
        self.assertEqual(
            gax_api.commit.call_args_list,
            [
                mock.call(
                    request=request,
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                        ),
                    ],
                ),
                mock.call(
                    request=request,
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.4.1",
                        ),
                    ],
                ),
                mock.call(
                    request=request,
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.6.1",
                        ),
                    ],
                ),
            ],
        )

    def test_run_in_transaction_w_commit_stats_success(self):
        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        commit_stats = CommitResponse.CommitStats(mutation_count=4)
        response = CommitResponse(commit_timestamp=now_pb, commit_stats=commit_stats)
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.commit.return_value = response
        database = self._make_database()
        database.log_commit_stats = True
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        called_with = []

        def unit_of_work(txn, *args, **kw):
            called_with.append((txn, args, kw))
            txn.insert(TABLE_NAME, COLUMNS, VALUES)
            return 42

        return_value = session.run_in_transaction(unit_of_work, "abc", some_arg="def")

        self.assertEqual(len(called_with), 1)
        txn, args, kw = called_with[0]
        self.assertIsInstance(txn, Transaction)
        self.assertEqual(return_value, 42)
        self.assertEqual(args, ("abc",))
        self.assertEqual(kw, {"some_arg": "def"})

        expected_options = TransactionOptions(read_write=TransactionOptions.ReadWrite())
        gax_api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )
        request = CommitRequest(
            session=self.SESSION_NAME,
            mutations=txn._mutations,
            transaction_id=TRANSACTION_ID,
            return_commit_stats=True,
        )
        gax_api.commit.assert_called_once_with(
            request=request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                ),
            ],
        )
        database.logger.info.assert_called_once_with(
            "CommitStats: mutation_count: 4\n", extra={"commit_stats": commit_stats}
        )

    def test_run_in_transaction_w_commit_stats_error(self):
        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.commit.side_effect = Unknown("testing")
        database = self._make_database()
        database.log_commit_stats = True
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        called_with = []

        def unit_of_work(txn, *args, **kw):
            called_with.append((txn, args, kw))
            txn.insert(TABLE_NAME, COLUMNS, VALUES)
            return 42

        # Exception has request_id attribute added
        with self.assertRaises(Unknown) as context:
            session.run_in_transaction(unit_of_work, "abc", some_arg="def")
        self.assertTrue(hasattr(context.exception, "request_id"))

        self.assertEqual(len(called_with), 1)
        txn, args, kw = called_with[0]
        self.assertIsInstance(txn, Transaction)
        self.assertEqual(args, ("abc",))
        self.assertEqual(kw, {"some_arg": "def"})

        expected_options = TransactionOptions(read_write=TransactionOptions.ReadWrite())
        gax_api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )
        request = CommitRequest(
            session=self.SESSION_NAME,
            mutations=txn._mutations,
            transaction_id=TRANSACTION_ID,
            return_commit_stats=True,
        )
        gax_api.commit.assert_called_once_with(
            request=request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                ),
            ],
        )
        database.logger.info.assert_not_called()

    def test_run_in_transaction_w_transaction_tag(self):
        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        commit_stats = CommitResponse.CommitStats(mutation_count=4)
        response = CommitResponse(commit_timestamp=now_pb, commit_stats=commit_stats)
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.commit.return_value = response
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        called_with = []

        def unit_of_work(txn, *args, **kw):
            called_with.append((txn, args, kw))
            txn.insert(TABLE_NAME, COLUMNS, VALUES)
            return 42

        transaction_tag = "transaction_tag"
        return_value = session.run_in_transaction(
            unit_of_work, "abc", some_arg="def", transaction_tag=transaction_tag
        )

        self.assertEqual(len(called_with), 1)
        txn, args, kw = called_with[0]
        self.assertIsInstance(txn, Transaction)
        self.assertEqual(return_value, 42)
        self.assertEqual(args, ("abc",))
        self.assertEqual(kw, {"some_arg": "def"})

        expected_options = TransactionOptions(read_write=TransactionOptions.ReadWrite())
        expected_request_options = RequestOptions(transaction_tag=transaction_tag)
        gax_api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME,
                options=expected_options,
                request_options=expected_request_options,
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )
        request = CommitRequest(
            session=self.SESSION_NAME,
            mutations=txn._mutations,
            transaction_id=TRANSACTION_ID,
            request_options=RequestOptions(transaction_tag=transaction_tag),
        )
        gax_api.commit.assert_called_once_with(
            request=request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                ),
            ],
        )

    def test_run_in_transaction_w_exclude_txn_from_change_streams(self):
        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        commit_stats = CommitResponse.CommitStats(mutation_count=4)
        response = CommitResponse(commit_timestamp=now_pb, commit_stats=commit_stats)
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.commit.return_value = response
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        called_with = []

        def unit_of_work(txn, *args, **kw):
            called_with.append((txn, args, kw))
            txn.insert(TABLE_NAME, COLUMNS, VALUES)
            return 42

        return_value = session.run_in_transaction(
            unit_of_work, "abc", exclude_txn_from_change_streams=True
        )

        self.assertEqual(len(called_with), 1)
        txn, args, kw = called_with[0]
        self.assertIsInstance(txn, Transaction)
        self.assertEqual(return_value, 42)
        self.assertEqual(args, ("abc",))

        expected_options = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(),
            exclude_txn_from_change_streams=True,
        )
        gax_api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )
        request = CommitRequest(
            session=self.SESSION_NAME,
            mutations=txn._mutations,
            transaction_id=TRANSACTION_ID,
        )
        gax_api.commit.assert_called_once_with(
            request=request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                ),
            ],
        )

    def test_run_in_transaction_w_abort_w_retry_metadata_w_exclude_txn_from_change_streams(
        self,
    ):
        RETRY_SECONDS = 12
        RETRY_NANOS = 3456
        retry_info = RetryInfo(
            retry_delay=Duration(seconds=RETRY_SECONDS, nanos=RETRY_NANOS)
        )
        trailing_metadata = [
            ("google.rpc.retryinfo-bin", retry_info.SerializeToString())
        ]
        aborted = _make_rpc_error(Aborted, trailing_metadata=trailing_metadata)
        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        response = CommitResponse(commit_timestamp=now_pb)
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.commit.side_effect = [aborted, response]
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        called_with = []

        def unit_of_work(txn, *args, **kw):
            called_with.append((txn, args, kw))
            txn.insert(TABLE_NAME, COLUMNS, VALUES)

        with mock.patch("google.cloud.spanner_v1._helpers.time.sleep") as sleep_mock:
            session.run_in_transaction(
                unit_of_work,
                "abc",
                some_arg="def",
                exclude_txn_from_change_streams=True,
            )

        sleep_mock.assert_called_once_with(RETRY_SECONDS + RETRY_NANOS / 1.0e9)
        self.assertEqual(len(called_with), 2)

        for index, (txn, args, kw) in enumerate(called_with):
            self.assertIsInstance(txn, Transaction)
            if index == 1:
                self.assertEqual(txn.committed, now)
            else:
                self.assertIsNone(txn.committed)
            self.assertEqual(args, ("abc",))
            self.assertEqual(kw, {"some_arg": "def"})

        self.assertEqual(
            gax_api.begin_transaction.call_args_list,
            [
                mock.call(
                    request=BeginTransactionRequest(
                        session=session.name,
                        options=TransactionOptions(
                            read_write=TransactionOptions.ReadWrite(),
                            exclude_txn_from_change_streams=True,
                        ),
                    ),
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                        ),
                    ],
                ),
                mock.call(
                    request=BeginTransactionRequest(
                        session=session.name,
                        options=TransactionOptions(
                            read_write=TransactionOptions.ReadWrite(),
                            exclude_txn_from_change_streams=True,
                        ),
                    ),
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.3.1",
                        ),
                    ],
                ),
            ],
        )
        request = CommitRequest(
            session=self.SESSION_NAME,
            mutations=txn._mutations,
            transaction_id=TRANSACTION_ID,
        )
        self.assertEqual(
            gax_api.commit.call_args_list,
            [
                mock.call(
                    request=request,
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.2.1",
                        ),
                    ],
                ),
                mock.call(
                    request=request,
                    metadata=[
                        ("google-cloud-resource-prefix", database.name),
                        ("x-goog-spanner-route-to-leader", "true"),
                        (
                            "x-goog-spanner-request-id",
                            f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.4.1",
                        ),
                    ],
                ),
            ],
        )

    def test_run_in_transaction_w_isolation_level_at_request(self):
        database = self._make_database()
        api = database.spanner_api = build_spanner_api()
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        def unit_of_work(txn, *args, **kw):
            txn.insert("test", [], [])
            return 42

        return_value = session.run_in_transaction(
            unit_of_work, "abc", isolation_level="SERIALIZABLE"
        )

        self.assertEqual(return_value, 42)

        expected_options = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(),
            isolation_level=TransactionOptions.IsolationLevel.SERIALIZABLE,
        )
        api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

    def test_run_in_transaction_w_isolation_level_at_client(self):
        database = self._make_database(
            default_transaction_options=DefaultTransactionOptions(
                isolation_level="SERIALIZABLE"
            )
        )
        api = database.spanner_api = build_spanner_api()
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        def unit_of_work(txn, *args, **kw):
            txn.insert("test", [], [])
            return 42

        return_value = session.run_in_transaction(unit_of_work, "abc")

        self.assertEqual(return_value, 42)

        expected_options = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(),
            isolation_level=TransactionOptions.IsolationLevel.SERIALIZABLE,
        )
        api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

    def test_run_in_transaction_w_isolation_level_at_request_overrides_client(self):
        database = self._make_database(
            default_transaction_options=DefaultTransactionOptions(
                isolation_level="SERIALIZABLE"
            )
        )
        api = database.spanner_api = build_spanner_api()
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        def unit_of_work(txn, *args, **kw):
            txn.insert("test", [], [])
            return 42

        return_value = session.run_in_transaction(
            unit_of_work,
            "abc",
            isolation_level=TransactionOptions.IsolationLevel.REPEATABLE_READ,
        )

        self.assertEqual(return_value, 42)

        expected_options = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(),
            isolation_level=TransactionOptions.IsolationLevel.REPEATABLE_READ,
        )
        api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

    def test_run_in_transaction_w_read_lock_mode_at_request(self):
        database = self._make_database()
        api = database.spanner_api = build_spanner_api()
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        def unit_of_work(txn, *args, **kw):
            txn.insert("test", [], [])
            return 42

        return_value = session.run_in_transaction(
            unit_of_work, "abc", read_lock_mode="OPTIMISTIC"
        )

        self.assertEqual(return_value, 42)

        expected_options = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
            ),
        )
        api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

    def test_run_in_transaction_w_read_lock_mode_at_client(self):
        database = self._make_database(
            default_transaction_options=DefaultTransactionOptions(
                read_lock_mode="OPTIMISTIC"
            )
        )
        api = database.spanner_api = build_spanner_api()
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        def unit_of_work(txn, *args, **kw):
            txn.insert("test", [], [])
            return 42

        return_value = session.run_in_transaction(unit_of_work, "abc")

        self.assertEqual(return_value, 42)

        expected_options = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
            ),
        )
        api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

    def test_run_in_transaction_w_read_lock_mode_at_request_overrides_client(self):
        database = self._make_database(
            default_transaction_options=DefaultTransactionOptions(
                read_lock_mode="PESSIMISTIC"
            )
        )
        api = database.spanner_api = build_spanner_api()
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        def unit_of_work(txn, *args, **kw):
            txn.insert("test", [], [])
            return 42

        return_value = session.run_in_transaction(
            unit_of_work,
            "abc",
            read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
        )

        self.assertEqual(return_value, 42)

        expected_options = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
            ),
        )
        api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

    def test_run_in_transaction_w_isolation_level_and_read_lock_mode_at_request(self):
        database = self._make_database()
        api = database.spanner_api = build_spanner_api()
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        def unit_of_work(txn, *args, **kw):
            txn.insert("test", [], [])
            return 42

        return_value = session.run_in_transaction(
            unit_of_work,
            "abc",
            read_lock_mode="PESSIMISTIC",
            isolation_level="REPEATABLE_READ",
        )

        self.assertEqual(return_value, 42)

        expected_options = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.PESSIMISTIC,
            ),
            isolation_level=TransactionOptions.IsolationLevel.REPEATABLE_READ,
        )
        api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

    def test_run_in_transaction_w_isolation_level_and_read_lock_mode_at_client(self):
        database = self._make_database(
            default_transaction_options=DefaultTransactionOptions(
                read_lock_mode="PESSIMISTIC",
                isolation_level="REPEATABLE_READ",
            )
        )
        api = database.spanner_api = build_spanner_api()
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        def unit_of_work(txn, *args, **kw):
            txn.insert("test", [], [])
            return 42

        return_value = session.run_in_transaction(unit_of_work, "abc")

        self.assertEqual(return_value, 42)

        expected_options = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.PESSIMISTIC,
            ),
            isolation_level=TransactionOptions.IsolationLevel.REPEATABLE_READ,
        )
        api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

    def test_run_in_transaction_w_isolation_level_and_read_lock_mode_at_request_overrides_client(
        self,
    ):
        database = self._make_database(
            default_transaction_options=DefaultTransactionOptions(
                read_lock_mode="PESSIMISTIC",
                isolation_level="REPEATABLE_READ",
            )
        )
        api = database.spanner_api = build_spanner_api()
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        def unit_of_work(txn, *args, **kw):
            txn.insert("test", [], [])
            return 42

        return_value = session.run_in_transaction(
            unit_of_work,
            "abc",
            read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
            isolation_level=TransactionOptions.IsolationLevel.SERIALIZABLE,
        )

        self.assertEqual(return_value, 42)

        expected_options = TransactionOptions(
            read_write=TransactionOptions.ReadWrite(
                read_lock_mode=TransactionOptions.ReadWrite.ReadLockMode.OPTIMISTIC,
            ),
            isolation_level=TransactionOptions.IsolationLevel.SERIALIZABLE,
        )
        api.begin_transaction.assert_called_once_with(
            request=BeginTransactionRequest(
                session=self.SESSION_NAME, options=expected_options
            ),
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                ),
            ],
        )

    def test_delay_helper_w_no_delay(self):
        metadata_mock = mock.Mock()
        metadata_mock.trailing_metadata.return_value = {}

        exc_mock = mock.Mock(errors=[metadata_mock])

        def _time_func():
            return 3

        # check if current time > deadline
        with mock.patch("google.cloud.spanner_v1._helpers.time.time", _time_func):
            with self.assertRaises(Exception):
                _delay_until_retry(exc_mock, 2, 1, default_retry_delay=0)

        with mock.patch("google.cloud.spanner_v1._helpers.time.time", _time_func):
            with mock.patch(
                "google.cloud.spanner_v1._helpers._get_retry_delay"
            ) as get_retry_delay_mock:
                with mock.patch(
                    "google.cloud.spanner_v1._helpers.time.sleep"
                ) as sleep_mock:
                    get_retry_delay_mock.return_value = None

                    _delay_until_retry(exc_mock, 6, 1)
                    sleep_mock.assert_not_called()

    def test_run_in_transaction_tracing_events_attached_to_parent_span(self):
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )
        from opentelemetry.sdk.trace.sampling import ALWAYS_ON

        tracer_provider = TracerProvider(sampler=ALWAYS_ON)
        trace_exporter = InMemorySpanExporter()
        tracer_provider.add_span_processor(SimpleSpanProcessor(trace_exporter))
        tracer = tracer_provider.get_tracer("test")

        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        aborted = _make_rpc_error(Aborted, trailing_metadata=[])
        response = CommitResponse(commit_timestamp=now_pb)
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.commit.side_effect = [aborted, response]
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        def unit_of_work(transaction, *args, **kwargs):
            transaction.insert(TABLE_NAME, COLUMNS, VALUES)
            return "answer"

        with tracer.start_as_current_span("ParentSpan"):
            return_value = session.run_in_transaction(
                unit_of_work,
                transaction_tag="test-tag",
                default_retry_delay=0,
            )

        self.assertEqual(return_value, "answer")
        finished_spans = trace_exporter.get_finished_spans()
        self.assertEqual(len(finished_spans), 1)
        parent_span = finished_spans[0]
        self.assertEqual(parent_span.name, "ParentSpan")
        self.assertIsNone(parent_span.attributes.get("transaction.tag"))
        event_names = [event.name for event in parent_span.events]
        self.assertIn(
            "Transaction was aborted during commit, retrying",
            event_names,
        )
        retry_event = next(
            event
            for event in parent_span.events
            if event.name == "Transaction was aborted during commit, retrying"
        )
        self.assertEqual(retry_event.attributes.get("attempt"), 1)

    def test_run_in_transaction_tracing_events_aborted_without_inner_errors(
        self,
    ):
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )
        from opentelemetry.sdk.trace.sampling import ALWAYS_ON

        tracer_provider = TracerProvider(sampler=ALWAYS_ON)
        trace_exporter = InMemorySpanExporter()
        tracer_provider.add_span_processor(SimpleSpanProcessor(trace_exporter))
        tracer = tracer_provider.get_tracer("test")

        transaction_pb = TransactionPB(id=TRANSACTION_ID)
        now = datetime.datetime.now(timezone.utc).replace(tzinfo=UTC)
        now_pb = _datetime_to_pb_timestamp(now)
        # Aborted raised without inner errors (defaults to empty tuple in GoogleAPICallError)
        aborted = Aborted("aborted without inner errors")
        response = CommitResponse(commit_timestamp=now_pb)
        gax_api = self._make_spanner_api()
        gax_api.begin_transaction.return_value = transaction_pb
        gax_api.commit.side_effect = [aborted, response]
        database = self._make_database()
        database.spanner_api = gax_api
        session = self._make_one(database)
        session._session_id = self.SESSION_ID

        def unit_of_work(transaction, *args, **kwargs):
            transaction.insert(TABLE_NAME, COLUMNS, VALUES)
            return "answer"

        with tracer.start_as_current_span("ParentSpan"):
            return_value = session.run_in_transaction(
                unit_of_work,
                default_retry_delay=0,
            )

        self.assertEqual(return_value, "answer")
        finished_spans = trace_exporter.get_finished_spans()
        self.assertEqual(len(finished_spans), 1)
        parent_span = finished_spans[0]
        event_names = [event.name for event in parent_span.events]
        self.assertIn(
            "Transaction was aborted during commit, retrying",
            event_names,
        )
        retry_event = next(
            event
            for event in parent_span.events
            if event.name == "Transaction was aborted during commit, retrying"
        )
        self.assertEqual(retry_event.attributes.get("attempt"), 1)
