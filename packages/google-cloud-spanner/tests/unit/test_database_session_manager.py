# Copyright 2025 Google LLC All rights reserved.
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
import threading
from datetime import timedelta
from os import environ
from unittest import TestCase

from google.api_core.exceptions import BadRequest, FailedPrecondition
from mock import DEFAULT, MagicMock, Mock, patch

from google.cloud.spanner_v1.database_sessions_manager import (
    DatabaseSessionsManager,
    TransactionType,
)
from tests._builders import build_database


class TestDatabaseSessionManager(TestCase):
    @classmethod
    def setUpClass(cls):
        # Save the original environment variables.
        cls._original_env = dict(environ)

    @classmethod
    def tearDownClass(cls):
        # Restore environment variables.
        environ.clear()
        environ.update(cls._original_env)

    def setUp(self):
        # Build session manager.
        database = build_database()
        self._manager = database._sessions_manager

        # Mock the session pool.
        pool = self._manager._pool
        pool.get = Mock(wraps=pool.get)
        pool.put = Mock(wraps=pool.put)

    def tearDown(self):
        # If the maintenance thread is still alive, set the event and wait
        # for the thread to terminate. We need to do this to ensure that the
        # thread does not interfere with other tests.
        manager = self._manager
        thread = manager._multiplexed_session_thread

        if thread and thread.is_alive():
            manager._multiplexed_session_terminate_event.set()
            thread.join(timeout=10)
            self.assertFalse(thread.is_alive())

    def test_read_only_pooled(self):
        manager = self._manager
        pool = manager._pool

        self._disable_multiplexed_sessions()

        # Get session from pool.
        session = manager.get_session(TransactionType.READ_ONLY)
        self.assertFalse(session.is_multiplexed)
        pool.get.assert_called_once()

        # Return session to pool.
        manager.put_session(session)
        pool.put.assert_called_once_with(session)

    def test_read_only_multiplexed(self):
        manager = self._manager
        pool = manager._pool

        self._enable_multiplexed_sessions()

        # Session is created.
        session_1 = manager.get_session(TransactionType.READ_ONLY)
        self.assertTrue(session_1.is_multiplexed)
        manager.put_session(session_1)

        # Session is re-used.
        session_2 = manager.get_session(TransactionType.READ_ONLY)
        self.assertEqual(session_1, session_2)
        manager.put_session(session_2)

        # Verify that pool was not used.
        pool.get.assert_not_called()
        pool.put.assert_not_called()

        # Verify create_session was called.
        manager._database.spanner_api.create_session.assert_called_once()

    def test_partitioned_pooled(self):
        manager = self._manager
        pool = manager._pool

        self._disable_multiplexed_sessions()

        # Get session from pool.
        session = manager.get_session(TransactionType.PARTITIONED)
        self.assertFalse(session.is_multiplexed)
        pool.get.assert_called_once()

        # Return session to pool.
        manager.put_session(session)
        pool.put.assert_called_once_with(session)

    def test_partitioned_multiplexed(self):
        manager = self._manager
        pool = manager._pool

        self._enable_multiplexed_sessions()

        # Session is created.
        session_1 = manager.get_session(TransactionType.PARTITIONED)
        self.assertTrue(session_1.is_multiplexed)
        manager.put_session(session_1)

        # Session is re-used.
        session_2 = manager.get_session(TransactionType.PARTITIONED)
        self.assertEqual(session_1, session_2)
        manager.put_session(session_2)

        # Verify that pool was not used.
        pool.get.assert_not_called()
        pool.put.assert_not_called()

        # Verify create_session was called.
        manager._database.spanner_api.create_session.assert_called_once()

    def test_read_write_pooled(self):
        manager = self._manager
        pool = manager._pool

        self._disable_multiplexed_sessions()

        # Get session from pool.
        session = manager.get_session(TransactionType.READ_WRITE)
        self.assertFalse(session.is_multiplexed)
        pool.get.assert_called_once()

        # Return session to pool.
        manager.put_session(session)
        pool.put.assert_called_once_with(session)

    def test_read_write_multiplexed(self):
        manager = self._manager
        pool = manager._pool

        self._enable_multiplexed_sessions()

        # Session is created.
        session_1 = manager.get_session(TransactionType.READ_WRITE)
        self.assertTrue(session_1.is_multiplexed)
        manager.put_session(session_1)

        # Session is re-used.
        session_2 = manager.get_session(TransactionType.READ_WRITE)
        self.assertEqual(session_1, session_2)
        manager.put_session(session_2)

        # Verify that pool was not used.
        pool.get.assert_not_called()
        pool.put.assert_not_called()

        # Verify create_session was called.
        manager._database.spanner_api.create_session.assert_called_once()

    @patch.multiple(
        DatabaseSessionsManager,
        _MAINTENANCE_THREAD_POLLING_INTERVAL=timedelta(milliseconds=5),
        _MAINTENANCE_THREAD_REFRESH_INTERVAL=timedelta(milliseconds=10),
    )
    def test_multiplexed_maintenance(self):
        manager = self._manager
        self._enable_multiplexed_sessions()

        rotated = threading.Event()

        def on_create_session(*args, **kwargs):
            if manager._database.spanner_api.create_session.call_count > 1:
                rotated.set()
            return DEFAULT

        manager._database.spanner_api.create_session.side_effect = on_create_session

        # Maintenance thread is started.
        session_1 = manager.get_session(TransactionType.READ_ONLY)
        self.assertTrue(session_1.is_multiplexed)
        self.assertTrue(manager._multiplexed_session_thread.is_alive())

        # Wait for maintenance thread to execute without polling.
        self.assertTrue(rotated.wait(timeout=10.0))

        # Verify that maintenance thread created new multiplexed session.
        session_2 = manager.get_session(TransactionType.READ_ONLY)
        self.assertTrue(session_2.is_multiplexed)
        self.assertNotEqual(session_1, session_2)

    def test_concurrent_get_multiplexed_session_no_deadlock(self):
        """Verify that concurrent _get_multiplexed_session calls do not deadlock.
        This tests that holding the lock across suspension points (like asyncio.sleep)
        doesn't freeze the event loop for subsequent lock seekers using CrossSync.Lock.
        """
        import asyncio
        from os import environ

        from google.cloud.spanner_v1._async.database_sessions_manager import (
            DatabaseSessionsManager,
        )

        # Build fresh async manager decoupling from test suite setup
        db = Mock()
        db._experimental_host = None
        db.database_role = "reader"
        pool = Mock()

        manager = DatabaseSessionsManager(db, pool)

        # Mock maintenance thread creation to avoid spawning background tasks
        manager._build_maintenance_thread = Mock(return_value=Mock())

        # Enable multiplexed sessions in environment for verification
        environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED] = "true"

        async def run_concurrent():
            entered_slow_build = asyncio.Event()
            release_slow_build = asyncio.Event()

            # Mock _build_multiplexed_session to include a suspension point
            async def slow_build():
                entered_slow_build.set()
                await release_slow_build.wait()
                return Mock()

            manager._build_multiplexed_session = slow_build

            # Trigger Coroutine 1
            task1 = asyncio.create_task(manager._get_multiplexed_session())
            # Wait until Coroutine 1 has acquired the lock and suspended
            await entered_slow_build.wait()

            # Trigger Coroutine 2 while Coroutine 1 holds the lock
            task2 = asyncio.create_task(manager._get_multiplexed_session())

            # Release Coroutine 1 to complete
            release_slow_build.set()

            await asyncio.gather(task1, task2)

        try:
            asyncio.run(asyncio.wait_for(run_concurrent(), timeout=5.0))
        except asyncio.TimeoutError:
            self.fail(
                "test_concurrent_get_multiplexed_session_no_deadlock timed out (DEADLOCK)!"
            )

    def test_get_multiplexed_session_fast_path(self):
        manager = self._manager
        mock_session = Mock()
        manager._multiplexed_session = mock_session
        manager._init_lock = Mock(wraps=manager._init_lock)

        session = manager._get_multiplexed_session()
        self.assertIs(session, mock_session)
        manager._init_lock.acquire.assert_not_called()
        self.assertIsNone(manager._multiplexed_session_lock)

    def test_get_multiplexed_session_fast_path_lock_already_created(self):
        manager = self._manager
        mock_session = Mock()
        manager._multiplexed_session = mock_session
        mock_lock = MagicMock()
        manager._multiplexed_session_lock = mock_lock
        manager._init_lock = Mock(wraps=manager._init_lock)

        session = manager._get_multiplexed_session()
        self.assertIs(session, mock_session)
        manager._init_lock.acquire.assert_not_called()
        mock_lock.acquire.assert_not_called()
        mock_lock.__enter__.assert_not_called()

    def test_maintain_multiplexed_session_rotates_session(self):
        import threading
        from weakref import ref

        manager = DatabaseSessionsManager(self._manager._database, self._manager._pool)
        manager._multiplexed_session_lock = threading.Lock()
        manager._multiplexed_session_terminate_event = Mock()
        manager._multiplexed_session_terminate_event.is_set.side_effect = [False, True]

        old_session = Mock()
        new_session = Mock()
        manager._multiplexed_session = old_session

        call_count = 0

        def mock_time():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return 0
            return 1000000

        with patch(
            "google.cloud.spanner_v1.database_sessions_manager.time.monotonic",
            side_effect=mock_time,
        ):
            with patch.object(
                manager, "_build_multiplexed_session", return_value=new_session
            ) as mock_build:
                DatabaseSessionsManager._maintain_multiplexed_session(ref(manager))
                mock_build.assert_called_once()
                old_session.delete.assert_not_called()
                new_session.delete.assert_not_called()
                self.assertIs(manager._multiplexed_session, new_session)

    def test_close_branches(self):
        manager = DatabaseSessionsManager(self._manager._database, self._manager._pool)

        # Branch where thread is None
        manager.close()

        # Branch where thread is not None
        mock_thread = Mock()
        mock_session = Mock()
        manager._multiplexed_session_thread = mock_thread
        manager._multiplexed_session = mock_session
        manager._multiplexed_session_terminate_event = Mock()

        manager.close()
        manager._multiplexed_session_terminate_event.set.assert_called_once()
        mock_thread.join.assert_called_once()
        self.assertIsNone(manager._multiplexed_session)
        mock_session.delete.assert_not_called()

    def test_maintain_multiplexed_session_handles_build_failure(self):
        import threading
        from weakref import ref

        manager = DatabaseSessionsManager(self._manager._database, self._manager._pool)
        manager._multiplexed_session_lock = threading.Lock()
        manager._multiplexed_session_terminate_event = Mock()
        manager._multiplexed_session_terminate_event.is_set.side_effect = [
            False,
            True,
        ]

        current_session = Mock()
        manager._multiplexed_session = current_session

        call_count = 0

        def mock_time():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return 0
            return 1000000

        with patch(
            "google.cloud.spanner_v1.database_sessions_manager.time.monotonic",
            side_effect=mock_time,
        ):
            with patch.object(
                manager,
                "_build_multiplexed_session",
                side_effect=Exception("network error"),
            ) as mock_build:
                with patch(
                    "google.cloud.spanner_v1.database_sessions_manager.CrossSync._Sync_Impl.event_wait"
                ) as mock_event_wait:
                    DatabaseSessionsManager._maintain_multiplexed_session(ref(manager))
                    mock_build.assert_called_once()
                    mock_event_wait.assert_called_once()
                    current_session.delete.assert_not_called()
                    self.assertIs(manager._multiplexed_session, current_session)

    def test_maintain_multiplexed_session_old_session_none(self):
        import threading
        from weakref import ref

        manager = DatabaseSessionsManager(self._manager._database, self._manager._pool)
        manager._multiplexed_session_lock = threading.Lock()
        manager._multiplexed_session_terminate_event = Mock()
        manager._multiplexed_session_terminate_event.is_set.side_effect = [False, True]

        new_session = Mock()
        manager._multiplexed_session = None

        call_count = 0

        def mock_time():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return 0
            return 1000000

        with patch(
            "google.cloud.spanner_v1.database_sessions_manager.time.monotonic",
            side_effect=mock_time,
        ):
            with patch.object(
                manager, "_build_multiplexed_session", return_value=new_session
            ):
                DatabaseSessionsManager._maintain_multiplexed_session(ref(manager))
                self.assertIs(manager._multiplexed_session, new_session)

    def test_get_multiplexed_session_initial_failure_allows_retry(self):
        manager = DatabaseSessionsManager(self._manager._database, self._manager._pool)
        manager._multiplexed_session = None

        with patch.object(
            manager,
            "_build_multiplexed_session",
            side_effect=Exception("create failed"),
        ):
            with self.assertRaises(Exception):
                manager._get_multiplexed_session()
            self.assertIsNone(manager._multiplexed_session)

        # Subsequent call succeeds and creates session and maintenance thread
        mock_session = Mock()
        mock_thread = Mock()
        mock_thread.is_alive.return_value = False
        with patch.object(
            manager, "_build_multiplexed_session", return_value=mock_session
        ):
            with patch.object(
                manager, "_build_maintenance_thread", return_value=mock_thread
            ):
                session = manager._get_multiplexed_session()
                self.assertIs(session, mock_session)
                mock_thread.start.assert_called_once()

    def test_get_multiplexed_session_concurrent_initialization_double_checked(
        self,
    ):
        manager = DatabaseSessionsManager(self._manager._database, self._manager._pool)
        manager._multiplexed_session = None

        concurrent_session = Mock()
        mock_lock = MagicMock()

        def lock_enter():
            manager._multiplexed_session = concurrent_session
            return mock_lock

        mock_lock.__enter__.side_effect = lock_enter

        with patch.object(manager, "_build_multiplexed_session") as mock_build:
            with patch(
                "google.cloud.spanner_v1.database_sessions_manager.CrossSync._Sync_Impl.Lock",
                return_value=mock_lock,
            ):
                session = manager._get_multiplexed_session()
                self.assertIs(session, concurrent_session)
                mock_build.assert_not_called()

    def test_get_multiplexed_session_maintenance_thread_failure_allows_retry(
        self,
    ):
        manager = DatabaseSessionsManager(self._manager._database, self._manager._pool)
        manager._multiplexed_session = None

        mock_session = Mock()
        with patch.object(
            manager, "_build_multiplexed_session", return_value=mock_session
        ):
            with patch.object(
                manager,
                "_build_maintenance_thread",
                side_effect=RuntimeError("thread spawn failed"),
            ):
                with self.assertRaises(RuntimeError):
                    manager._get_multiplexed_session()
                self.assertIsNone(manager._multiplexed_session)

    def test_build_maintenance_thread(self):
        manager = DatabaseSessionsManager(self._manager._database, self._manager._pool)
        mock_session = Mock()
        mock_session.session_id = "sync-test-session-456"

        thread = manager._build_maintenance_thread(mock_session)
        self.assertIsNotNone(thread)
        self.assertEqual(
            thread.name, "maintenance-multiplexed-session-sync-test-session-456"
        )
        self.assertTrue(thread.daemon)

        # Backward compatibility when session is omitted
        manager._multiplexed_session = mock_session
        thread_default = manager._build_maintenance_thread()
        self.assertIsNotNone(thread_default)
        self.assertEqual(
            thread_default.name,
            "maintenance-multiplexed-session-sync-test-session-456",
        )
        self.assertTrue(thread_default.daemon)

    def test_maintain_multiplexed_session_manager_gone(self):
        from weakref import ref

        class Fake:
            pass

        fake = Fake()
        reference = ref(fake)
        del fake
        DatabaseSessionsManager._maintain_multiplexed_session(reference)

    def test_maintain_multiplexed_session_manager_collected_in_loop(self):
        manager = DatabaseSessionsManager(self._manager._database, self._manager._pool)
        call_count = 0

        def mock_ref():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return manager
            return None

        DatabaseSessionsManager._maintain_multiplexed_session(mock_ref)
        self.assertGreaterEqual(call_count, 2)

    def test_exception_bad_request(self):
        manager = self._manager
        api = manager._database.spanner_api
        api.create_session.side_effect = BadRequest("")

        # Exception has request_id attribute added
        with self.assertRaises(BadRequest) as cm:
            manager.get_session(TransactionType.READ_ONLY)
        # Verify the exception has request_id attribute
        self.assertTrue(hasattr(cm.exception, "request_id"))

    def test_exception_failed_precondition(self):
        manager = self._manager
        api = manager._database.spanner_api
        api.create_session.side_effect = FailedPrecondition("")

        # Exception has request_id attribute added
        with self.assertRaises(FailedPrecondition) as cm:
            manager.get_session(TransactionType.READ_ONLY)
        # Verify the exception has request_id attribute
        self.assertTrue(hasattr(cm.exception, "request_id"))

    def test__use_multiplexed_read_only(self):
        transaction_type = TransactionType.READ_ONLY

        environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED] = "false"
        self.assertFalse(DatabaseSessionsManager._use_multiplexed(transaction_type))

        environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED] = "true"
        self.assertTrue(DatabaseSessionsManager._use_multiplexed(transaction_type))

    def test__use_multiplexed_partitioned(self):
        transaction_type = TransactionType.PARTITIONED

        environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED_PARTITIONED] = "false"
        self.assertFalse(DatabaseSessionsManager._use_multiplexed(transaction_type))

        environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED_PARTITIONED] = "true"
        self.assertTrue(DatabaseSessionsManager._use_multiplexed(transaction_type))

        # Test default behavior (should be enabled)
        del environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED_PARTITIONED]
        self.assertTrue(DatabaseSessionsManager._use_multiplexed(transaction_type))

    def test__use_multiplexed_read_write(self):
        transaction_type = TransactionType.READ_WRITE

        environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED_READ_WRITE] = "false"
        self.assertFalse(DatabaseSessionsManager._use_multiplexed(transaction_type))

        environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED_READ_WRITE] = "true"
        self.assertTrue(DatabaseSessionsManager._use_multiplexed(transaction_type))

        # Test default behavior (should be enabled)
        del environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED_READ_WRITE]
        self.assertTrue(DatabaseSessionsManager._use_multiplexed(transaction_type))

    def test__use_multiplexed_unsupported_transaction_type(self):
        unsupported_type = "UNSUPPORTED_TRANSACTION_TYPE"

        with self.assertRaises(ValueError):
            DatabaseSessionsManager._use_multiplexed(unsupported_type)

    def test__getenv(self):
        true_values = ["1", " 1", " 1", "true", "True", "TRUE", " true "]
        for value in true_values:
            environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED] = value
            self.assertTrue(
                DatabaseSessionsManager._use_multiplexed(TransactionType.READ_ONLY)
            )

        false_values = ["false", "False", "FALSE", " false "]
        for value in false_values:
            environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED] = value
            self.assertFalse(
                DatabaseSessionsManager._use_multiplexed(TransactionType.READ_ONLY)
            )

        # Test that empty string and "0" are now treated as true (default enabled)
        default_true_values = ["", "0", "anything", "random"]
        for value in default_true_values:
            environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED] = value
            self.assertTrue(
                DatabaseSessionsManager._use_multiplexed(TransactionType.READ_ONLY)
            )

        del environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED]
        self.assertTrue(
            DatabaseSessionsManager._use_multiplexed(TransactionType.READ_ONLY)
        )

    def test_rotate_multiplexed_session_success(self):
        import threading

        manager = DatabaseSessionsManager(self._manager._database, self._manager._pool)
        manager._multiplexed_session_lock = threading.Lock()
        old_session = Mock()
        new_session = Mock()
        manager._multiplexed_session = old_session

        with patch.object(
            manager, "_build_multiplexed_session", return_value=new_session
        ):
            result = manager._rotate_multiplexed_session()
            self.assertTrue(result)
            self.assertIs(manager._multiplexed_session, new_session)
            old_session.delete.assert_not_called()
            new_session.delete.assert_not_called()

    def test_rotate_multiplexed_session_build_failure(self):
        import threading

        manager = DatabaseSessionsManager(self._manager._database, self._manager._pool)
        manager._multiplexed_session_lock = threading.Lock()
        current_session = Mock()
        manager._multiplexed_session = current_session

        with patch.object(
            manager,
            "_build_multiplexed_session",
            side_effect=Exception("network down"),
        ):
            result = manager._rotate_multiplexed_session()
            self.assertFalse(result)
            self.assertIs(manager._multiplexed_session, current_session)
            current_session.delete.assert_not_called()

    @staticmethod
    def _disable_multiplexed_sessions() -> None:
        """Sets environment variables to disable multiplexed sessions for all transactions types."""

        environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED] = "false"
        environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED_PARTITIONED] = "false"
        environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED_READ_WRITE] = "false"

    @staticmethod
    def _enable_multiplexed_sessions() -> None:
        """Sets environment variables to enable multiplexed sessions for all transaction types."""

        environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED] = "true"
        environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED_PARTITIONED] = "true"
        environ[DatabaseSessionsManager._ENV_VAR_MULTIPLEXED_READ_WRITE] = "true"
