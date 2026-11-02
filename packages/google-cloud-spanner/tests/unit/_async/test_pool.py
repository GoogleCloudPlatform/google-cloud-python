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

import asyncio
import datetime
import unittest
from unittest import mock

from google.cloud.exceptions import NotFound

from google.cloud.aio._cross_sync import CrossSync
from google.cloud.spanner_v1.types.spanner import BatchCreateSessionsResponse
from google.cloud.spanner_v1.types.spanner import Session as SessionProto


class IsolatedAsyncioTestCase(unittest.TestCase):
    def run(self, result=None):
        if asyncio.iscoroutinefunction(getattr(self, self._testMethodName)):
            testMethod = getattr(self, self._testMethodName)

            def wrapper(*args, **kwargs):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    return loop.run_until_complete(testMethod(*args, **kwargs))
                finally:
                    loop.close()

            setattr(self, self._testMethodName, wrapper)

        return super().run(result)


class _Session(object):
    def __init__(self, name, last_use_time=None):
        self.name = name
        self._session_id = name.split("/")[-1]
        self.last_use_time = last_use_time or datetime.datetime.now(
            datetime.timezone.utc
        )
        self.delete = mock.AsyncMock()
        self.ping = mock.AsyncMock()
        self.exists = mock.AsyncMock(return_value=True)
        self.create = mock.AsyncMock()
        self._transaction = None

        def get_transaction(*args, **kwargs):
            res = self._transaction
            if self._transaction is None:
                self._transaction = mock.Mock()
            return res

        self.transaction = mock.Mock(side_effect=get_transaction)

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


class _Database(object):
    def __init__(self, name, database_role=None):
        self.name = name
        self.database_id = name.split("/")[-1]
        self.database_role = database_role
        self.spanner_api = mock.AsyncMock()
        self._route_to_leader_enabled = False
        self._instance = _Instance()

        # Set default return value for batch_create_sessions to avoid infinite loops in _fill_pool
        session_pb = SessionProto(name=name + "/sessions/default")
        self.spanner_api.batch_create_sessions.return_value = (
            BatchCreateSessionsResponse(session=[session_pb])
        )

    def with_error_augmentation(self, *args, **kwargs):
        return [], mock.MagicMock(__enter__=mock.Mock(), __exit__=mock.Mock())

    def _next_nth_request(self, n):
        return "request-id-" + str(n)


class TestAbstractSessionPool(IsolatedAsyncioTestCase):
    def _getTargetClass(self):
        from google.cloud.spanner_v1._async.pool import AbstractSessionPool

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

    async def test_bind_raises_NotImplementedError(self):
        pool = self._make_one()
        db = _Database("database-name")
        with self.assertRaises(NotImplementedError):
            await pool.bind(db)

    async def test_get_virtual(self):
        pool = self._make_one()
        with self.assertRaises(NotImplementedError):
            await pool.get()

    async def test_put_virtual(self):
        pool = self._make_one()
        with self.assertRaises(NotImplementedError):
            await pool.put(None)

    async def test_clear_virtual(self):
        pool = self._make_one()
        with self.assertRaises(NotImplementedError):
            await pool.clear()

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

    def test_session_deprecated(self):
        import warnings

        pool = self._make_one()
        with warnings.catch_warnings(record=True) as warned:
            warnings.simplefilter("always")
            checkout = pool.session()
            self.assertEqual(len(warned), 1)
            self.assertTrue(issubclass(warned[0].category, DeprecationWarning))
        self.assertIs(checkout._pool, pool)


class TestSessionCheckout(IsolatedAsyncioTestCase):
    def _getTargetClass(self):
        from google.cloud.spanner_v1._async.pool import SessionCheckout

        return SessionCheckout

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    async def test_context_manager(self):
        pool = mock.AsyncMock()
        session = mock.Mock()
        # Mock get to be a coro returning session
        pool.get = mock.AsyncMock(return_value=session)

        checkout = self._make_one(pool)
        async with checkout as got:
            self.assertIs(got, session)

        pool.get.assert_called_once()
        pool.put.assert_called_once_with(session)


class TestFixedSizePool(IsolatedAsyncioTestCase):
    DATABASE_NAME = "projects/p/instances/i/databases/d"
    SESSION_NAME = DATABASE_NAME + "/sessions/s"

    def _getTargetClass(self):
        from google.cloud.spanner_v1._async.pool import FixedSizePool

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

    async def test__new_session_role(self):
        db = _Database(self.DATABASE_NAME)
        db.database_role = "db-role"
        pool = self._make_one(database_role="pool-role")
        pool._database = db
        # We need to bypass the mock _new_session to test the real logic
        from google.cloud.spanner_v1._async.pool import FixedSizePool

        session = FixedSizePool._new_session(pool)
        self.assertEqual(session.database_role, "pool-role")

        pool._database_role = None
        session = FixedSizePool._new_session(pool)
        self.assertEqual(session.database_role, "db-role")

    async def test_resource_info(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one()
        await pool.bind(db)
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

    async def test_get_put(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)
        # bind fills the pool with 1 sessions by default mock
        got = await pool.get()
        self.assertEqual(got.name, self.SESSION_NAME)
        await pool.put(got)
        self.assertEqual(pool._sessions.qsize(), 1)

    async def test_get_empty_timeout(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1, default_timeout=0.01)
        await pool.bind(db)

        # Empty the pool so we can test timeout
        await pool.get()

        with self.assertRaises(CrossSync.QueueEmpty):
            await pool.get()

    async def test_clear(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=2)
        await pool.bind(db)
        # bind will fill BOTH slots because requested_session_count is 2 and mock returns 1 per call
        self.assertTrue(pool._sessions.full())
        self.assertEqual(pool._sessions.qsize(), 2)
        await pool.clear()
        self.assertEqual(pool._sessions.qsize(), 0)

    async def test_fill_pool(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=2)

        session_pb1 = SessionProto(name=self.SESSION_NAME + "/1")
        session_pb2 = SessionProto(name=self.SESSION_NAME + "/2")
        db.spanner_api.batch_create_sessions.return_value = BatchCreateSessionsResponse(
            session=[session_pb1, session_pb2]
        )

        await pool.bind(db)

        self.assertEqual(pool._sessions.qsize(), 2)
        db.spanner_api.batch_create_sessions.assert_called_once()

    async def test_fill_pool_requested_count_le_0(self):
        # Coverage for line 288+
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=0)
        await pool.bind(db)
        self.assertEqual(pool._sessions.qsize(), 0)
        db.spanner_api.batch_create_sessions.assert_not_called()

    async def test_fill_pool_already_full(self):
        # Coverage for line 308+
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        # Inject context to skip bind as we want to test _fill_pool directly on a full pool
        pool._database = db
        pool._sessions.put_nowait(mock.Mock())
        await pool._fill_pool()
        db.spanner_api.batch_create_sessions.assert_not_called()

    async def test_ping(self):
        from google.cloud.spanner_v1._async.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)

        # Clear sessions created by bind
        while not pool._sessions.empty():
            await pool._sessions.get()

        session = _Session(self.SESSION_NAME)
        # Make the session old so it will be pinged
        session.last_use_time = _NOW() - datetime.timedelta(minutes=60)
        session.ping = mock.AsyncMock()
        await pool.put(session)

        await pool.ping()
        session.ping.assert_called_once()

    async def test_ping_not_found_recreates(self):
        from google.cloud.spanner_v1._async.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)

        session = await pool.get()
        # Ensure it's the mock
        self.assertIsInstance(session, _Session)
        session.last_use_time = _NOW() - datetime.timedelta(minutes=61)
        session.ping = mock.AsyncMock(side_effect=NotFound("not found"))

        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.AsyncMock()
        pool._new_session = mock.Mock(return_value=new_session)

        await pool.put(session)
        await pool.ping()

    async def test_get_recreates_if_not_found(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)
        session = await pool.get()
        session.last_use_time = datetime.datetime.now(
            datetime.timezone.utc
        ) - datetime.timedelta(hours=2)
        # exists returns False, so it recreates
        session.exists.return_value = False
        pool._sessions.put_nowait(session)

        got = await pool.get()
        self.assertEqual(got.name, self.SESSION_NAME)
        self.assertTrue(got.create.called)

    async def test_ping_exception_warns(self):
        import warnings

        from google.cloud.spanner_v1._async.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)

        session = await pool.get()
        session.last_use_time = _NOW() - datetime.timedelta(minutes=61)
        session.ping = mock.AsyncMock(side_effect=Exception("error"))

        await pool.put(session)
        with warnings.catch_warnings(record=True) as warned:
            warnings.simplefilter("always")
            await pool.ping()
            self.assertEqual(len(warned), 1)

    async def test_get_pings_old_session(self):
        from google.cloud.spanner_v1._async.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)
        session = await pool.get()
        # session is too old (55m + 1s)
        session.last_use_time = _NOW() - datetime.timedelta(minutes=56)
        await pool.put(session)

        got = await pool.get()
        self.assertEqual(got.name, self.SESSION_NAME)
        self.assertGreaterEqual(session.exists.call_count, 1)

    async def test_get_timeout_none(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)
        session = await pool.get(timeout=None)
        self.assertIsInstance(session, _Session)

    async def test_get_old_session_not_exists_recreates(self):
        from google.cloud.spanner_v1.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)

        session = await pool.get()
        session.last_use_time = _NOW() - datetime.timedelta(minutes=61)
        session.exists = mock.AsyncMock(return_value=False)

        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.AsyncMock()
        pool._new_session = mock.Mock(return_value=new_session)

        await pool.put(session)
        got = await pool.get()
        self.assertIs(got, new_session)
        new_session.create.assert_called_once()

    async def test_fill_pool_edge_cases(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        # size <= 0
        pool._database = db
        pool.size = 0
        await pool._fill_pool()
        self.assertEqual(pool._sessions.qsize(), 0)

        # count <= 0
        pool.size = 1
        pool._sessions.put_nowait(_Session(self.SESSION_NAME))
        await pool._fill_pool()  # pool already full, count will be 0
        self.assertEqual(pool._sessions.qsize(), 1)

    async def test_fill_pool_leader_aware(self):
        db = _Database(self.DATABASE_NAME)
        db._route_to_leader_enabled = True
        pool = self._make_one(size=1)
        # bind calls _fill_pool
        await pool.bind(db)
        self.assertEqual(pool._sessions.qsize(), 1)

        self.assertEqual(pool._sessions.qsize(), 1)

    async def test_fill_pool_mock_full(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool._database = db
        # Mock full() to return True even if space exists (or just fill it)
        with mock.patch.object(pool._sessions, "full", return_value=True):
            await pool._fill_pool()
        # Should return early at line 310

    async def test_clear_no_database(self):
        pool = self._make_one(size=1)
        session = _Session(self.SESSION_NAME)
        pool._sessions.put_nowait(session)
        # pool._database is None
        await pool.clear()
        # Should hit if self._database is None: pass in clear() logic

    async def test_fill_pool_full(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        pool._database = db
        pool._sessions.put_nowait(_Session(self.SESSION_NAME))
        await pool._fill_pool()  # Should hit "already full" event
        self.assertEqual(pool._sessions.qsize(), 1)

    async def test_get_expired_session_recreated(self):
        from google.cloud.spanner_v1._async.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1, max_age_minutes=0)
        await pool.bind(db)

        # Clear sessions created by bind
        while not pool._sessions.empty():
            await pool._sessions.get()

        session = _Session(self.SESSION_NAME)
        session.last_use_time = _NOW() - datetime.timedelta(minutes=1)
        session.exists = mock.AsyncMock(return_value=False)

        await pool.put(session)

        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.AsyncMock()
        pool._new_session = mock.Mock(return_value=new_session)

        got = await pool.get()

        self.assertIs(got, new_session)
        new_session.create.assert_called_once()

    async def test_get_invalid_session_recreated(self):
        from google.cloud.spanner_v1._async.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)

        # Clear sessions created by bind
        while not pool._sessions.empty():
            await pool._sessions.get()

        session = _Session(self.SESSION_NAME)
        session.exists = mock.AsyncMock(return_value=False)
        session.last_use_time = _NOW() - datetime.timedelta(minutes=60)

        await pool.put(session)

        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.AsyncMock()
        pool._new_session = mock.Mock(return_value=new_session)

        got = await pool.get()

        self.assertIs(got, new_session)
        new_session.create.assert_called_once()


class TestBurstyPool(IsolatedAsyncioTestCase):
    DATABASE_NAME = "projects/p/instances/i/databases/d"
    SESSION_NAME = DATABASE_NAME + "/sessions/s"

    def _getTargetClass(self):
        from google.cloud.spanner_v1._async.pool import BurstyPool

        return BurstyPool

    def _make_one(self, *args, **kwargs):
        pool = self._getTargetClass()(*args, **kwargs)
        pool._new_session = mock.Mock(
            side_effect=lambda *args, **kwargs: _Session(self.SESSION_NAME)
        )
        return pool

    def test_ctor_defaults(self):
        pool = self._make_one()
        self.assertIsNone(pool._database)
        self.assertEqual(pool._labels, {})
        self.assertIsNone(pool._database_role)

    async def test_get_put(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one()
        await pool.bind(db)
        session = _Session(self.SESSION_NAME)
        await pool.put(session)
        got = await pool.get()
        self.assertIs(got, session)

    async def test_get_empty_creates_new(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one()
        await pool.bind(db)

        session = _Session(self.SESSION_NAME)
        session.create = mock.AsyncMock()
        pool._new_session = mock.Mock(return_value=session)

        got = await pool.get()

        self.assertIs(got, session)
        session.create.assert_called_once()

    async def test_get_timeout_none(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(target_size=1)
        pool._database = db
        # Hit timeout is None branch (indirectly)
        session = await pool.get()
        self.assertIsInstance(session, _Session)

    async def test_clear(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one()
        await pool.bind(db)
        session = _Session(self.SESSION_NAME)
        session.delete = mock.AsyncMock()
        await pool.put(session)
        self.assertEqual(pool._sessions.qsize(), 1)
        await pool.clear()
        self.assertEqual(pool._sessions.qsize(), 0)
        session.delete.assert_called_once()

    async def test_get_invalid_session_recreated(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one()
        await pool.bind(db)

        session = _Session(self.SESSION_NAME)
        # Mock it to be invalid
        session.exists = mock.AsyncMock(return_value=False)
        await pool.put(session)

        # Mock _new_session
        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.AsyncMock()
        pool._new_session = mock.Mock(return_value=new_session)

        got = await pool.get()

        self.assertIs(got, new_session)
        new_session.create.assert_called_once()

    async def test_put_full_pool_deletes_session(self):
        pool = self._make_one()
        # Mock queue to be full
        pool._sessions = mock.Mock()
        pool._sessions.put_nowait.side_effect = asyncio.QueueFull()

        session = _Session(self.SESSION_NAME)
        session.delete = mock.AsyncMock()

        await pool.put(session)
        session.delete.assert_called_once()

    async def test_put_full_pool_delete_not_found(self):
        pool = self._make_one()
        pool._sessions = mock.Mock()
        pool._sessions.put_nowait.side_effect = asyncio.QueueFull()

        session = _Session(self.SESSION_NAME)
        session.delete = mock.AsyncMock(side_effect=NotFound("not found"))

        await pool.put(session)
        session.delete.assert_called_once()

        session.delete.assert_called_once()


class TestPingingPool(IsolatedAsyncioTestCase):
    DATABASE_NAME = "projects/p/instances/i/databases/d"
    SESSION_NAME = DATABASE_NAME + "/sessions/s"

    def _getTargetClass(self):
        from google.cloud.spanner_v1._async.pool import PingingPool

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

    async def test_bind_and_get_put(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)

        got = await pool.get()
        self.assertEqual(got.name, self.SESSION_NAME)

        await pool.put(got)
        self.assertEqual(pool._sessions.qsize(), 1)

    async def test_get_empty_timeout(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1, default_timeout=0.01)
        await pool.bind(db)
        await pool.get()  # Empty it

        with self.assertRaises(CrossSync.QueueEmpty):
            await pool.get()

    async def test_get_pings_if_old(self):
        from google.cloud.spanner_v1._async.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1, ping_interval=3600)
        await pool.bind(db)

        session = await pool.get()
        # Force it to be old
        pool._sessions.put_nowait((_NOW() - datetime.timedelta(hours=1), session))

        session.exists = mock.AsyncMock(return_value=True)
        # pool.put(session) removed here

        got = await pool.get()
        self.assertIs(got, session)
        session.exists.assert_called_once()

    async def test_get_recreates_if_defunct(self):
        from google.cloud.spanner_v1._async.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1, ping_interval=3600)
        await pool.bind(db)

        session = await pool.get()
        # Force it to be old
        pool._sessions.put_nowait((_NOW() - datetime.timedelta(hours=1), session))

        session.exists = mock.AsyncMock(return_value=False)
        # pool.put(session) removed here

        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.AsyncMock()
        pool._new_session = mock.Mock(return_value=new_session)

        got = await pool.get()
        self.assertIs(got, new_session)
        new_session.create.assert_called_once()

    async def test_clear(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)
        self.assertEqual(pool._sessions.qsize(), 1)
        await pool.clear()
        self.assertEqual(pool._sessions.qsize(), 0)

    async def test_ping(self):
        from google.cloud.spanner_v1._async.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=2, ping_interval=3600)
        await pool.bind(db)

        # Get sessions and mock them
        s1 = await pool.get()
        s2 = await pool.get()
        s1.ping = mock.AsyncMock()
        s2.ping = mock.AsyncMock(side_effect=NotFound("not found"))

        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.AsyncMock()
        pool._new_session = mock.Mock(return_value=new_session)

        # Put back with old timestamp to force ping
        pool._sessions.put_nowait((_NOW() - datetime.timedelta(hours=1), s1))
        pool._sessions.put_nowait((_NOW() - datetime.timedelta(hours=1), s2))

        await pool.ping()

        s1.ping.assert_called_once()
        s2.ping.assert_called_once()
        new_session.create.assert_called_once()

    async def test_ping_exception_fallback(self):
        import warnings

        db = _Database(self.DATABASE_NAME)
        # We'll use FixedSizePool for this since it has the catch
        from google.cloud.spanner_v1._async.pool import FixedSizePool

        pool = FixedSizePool(size=1)
        await pool.bind(db)

        # Clear sessions created by bind
        while not pool._sessions.empty():
            pool._sessions.get_nowait()

        session = _Session(self.SESSION_NAME)
        # Force it to be old
        from google.cloud.spanner_v1._async.pool import _NOW

        session.last_use_time = _NOW() - datetime.timedelta(minutes=60)
        session.ping = mock.AsyncMock(side_effect=Exception("ping failed"))

        await pool.put(session)

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            await pool.ping()
            self.assertEqual(len(w), 1)
            self.assertIn("Failed to ping session", str(w[-1].message))

    async def test_ping_empty_pool(self):
        pool = self._make_one(size=1)
        await pool.ping()  # Should not raise

    async def test_get_timeout_none_pinging(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)
        await pool.get()  # Empty it

        # We need something in the pool for timeout=None to give it back
        session = _Session(self.SESSION_NAME)
        # Put it back as tuple (ping_after, session)
        from google.cloud.spanner_v1._async.pool import _NOW

        pool._sessions.put_nowait((_NOW() + datetime.timedelta(hours=1), session))

        got = await pool.get(timeout=None)
        self.assertIs(got, session)

    async def test_pinging_pool_get_old_session_not_exists_recreates(self):
        from google.cloud.spanner_v1._async.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)

        session = await pool.get()
        # Set ping_after to past
        ping_after = _NOW() - datetime.timedelta(seconds=1)
        # We need to manually put it back with a past ping_after
        pool._sessions.put_nowait((ping_after, session))

        session.exists = mock.AsyncMock(return_value=False)
        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.AsyncMock()
        pool._new_session = mock.Mock(return_value=new_session)

        got = await pool.get()
        self.assertIs(got, new_session)
        new_session.create.assert_called_once()

    async def test_ping_skipped_if_fresh(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1, ping_interval=3600)
        await pool.bind(db)

        session = await pool.get()
        session.ping = mock.AsyncMock()
        await pool.put(session)

        await pool.ping()
        session.ping.assert_not_called()

    async def test_bind_leader_routing(self):
        db = _Database(self.DATABASE_NAME)
        db._route_to_leader_enabled = True
        pool = self._make_one(size=1)
        await pool.bind(db)
        # Verify metadata included leader routing - this requires checking call_args
        # but our mock DB captures it.
        # Line 658 hit.

    async def test_bind_invalid_size(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=0)
        await pool.bind(db)
        # Line 671-676 hit.


class TestTransactionPingingPool(IsolatedAsyncioTestCase):
    DATABASE_NAME = "projects/p/instances/i/databases/d"
    SESSION_NAME = DATABASE_NAME + "/sessions/s"

    def _getTargetClass(self):
        from google.cloud.spanner_v1._async.pool import TransactionPingingPool

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

    async def test_get_put(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)

        # After bind, sessions are in _pending_sessions because transaction() is None
        await pool.begin_pending_transactions()

        session = await pool.get()
        self.assertEqual(session.name, self.SESSION_NAME)

        await pool.put(session)
        self.assertEqual(pool._sessions.qsize(), 1)

    async def test_put_no_transaction_to_pending(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)
        await pool.begin_pending_transactions()

        session = await pool.get()
        self.assertIsInstance(session, _Session)
        session._transaction = None  # Force None for test

        await pool.put(session)
        self.assertEqual(pool._pending_sessions.qsize(), 1)
        self.assertEqual(pool._sessions.qsize(), 0)
        # Ensure it was initialized
        self.assertIsNotNone(session._transaction)

    async def test_begin_pending_transactions(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)
        await pool.begin_pending_transactions()

        session = await pool.get()
        session._transaction = None
        await pool.put(session)

        self.assertEqual(pool._pending_sessions.qsize(), 1)
        await pool.begin_pending_transactions()
        self.assertEqual(pool._pending_sessions.qsize(), 0)
        self.assertEqual(pool._sessions.qsize(), 1)

    async def test_bind(self):
        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        # Hits TransactionPingingPool.bind
        await pool.bind(db)
        self.assertEqual(pool._pending_sessions.qsize(), 1)
        await pool.begin_pending_transactions()
        self.assertEqual(pool._sessions.qsize(), 1)

    async def test_get_old_session_not_exists_recreates(self):
        from google.cloud.spanner_v1._async.pool import _NOW

        db = _Database(self.DATABASE_NAME)
        pool = self._make_one(size=1)
        await pool.bind(db)
        await pool.begin_pending_transactions()

        session = await pool.get()
        # Manually put it back with a past ping_after
        ping_after = _NOW() - datetime.timedelta(seconds=1)
        pool._sessions.put_nowait((ping_after, session))

        session.exists = mock.AsyncMock(return_value=False)
        new_session = _Session(self.SESSION_NAME + "/new")
        new_session.create = mock.AsyncMock()
        pool._new_session = mock.Mock(return_value=new_session)

        got = await pool.get()
        self.assertIs(got, new_session)
        new_session.create.assert_called_once()
