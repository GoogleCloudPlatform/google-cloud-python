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
import unittest
from unittest import mock

from google.cloud.spanner_v1._async.database_sessions_manager import (
    DatabaseSessionsManager,
    TransactionType,
)


class TestSessionsManagerExtra(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.database = mock.Mock()
        self.database.logger = mock.Mock()
        self.pool = mock.Mock()

    async def test_use_multiplexed_unsupported(self):
        # coverage for line 213
        with self.assertRaises(ValueError):
            DatabaseSessionsManager._use_multiplexed("invalid")

    async def test_get_session_experimental_host(self):
        # coverage for line 87 (experimental host branch)
        self.database._experimental_host = "experimental"
        manager = DatabaseSessionsManager(self.database, self.pool)
        session = mock.Mock()
        session.is_multiplexed = True
        session.session_id = "sid"

        with mock.patch.object(
            manager, "_get_multiplexed_session", return_value=session
        ):
            res = await manager.get_session(TransactionType.READ_WRITE)
            self.assertEqual(res, session)

    async def test_maintenance_thread_sync_branch(self):
        # coverage for line 127 and 158
        manager = DatabaseSessionsManager(self.database, self.pool)
        session = mock.Mock()
        session.session_id = "sid"

        with mock.patch(
            "google.cloud.spanner_v1._async.database_sessions_manager.CrossSync.is_async",
            False,
        ):
            with mock.patch.object(
                manager, "_build_multiplexed_session", return_value=session
            ):
                with mock.patch(
                    "google.cloud.spanner_v1._async.database_sessions_manager.Thread"
                ) as mock_thread:
                    await manager._get_multiplexed_session()
                    self.assertTrue(mock_thread.called)

    async def test_maintain_multiplexed_session_terminate(self):
        # coverage for line 191-193
        manager = DatabaseSessionsManager(self.database, self.pool)
        manager._multiplexed_session_terminate_event = asyncio.Event()
        manager._multiplexed_session_terminate_event.set()

        from weakref import ref

        # Should return immediately
        await manager._maintain_multiplexed_session(ref(manager))

    async def test_maintain_multiplexed_session_manager_gone(self):
        # coverage for line 178
        from weakref import ref

        class Fake:
            pass

        fake = Fake()
        r = ref(fake)
        del fake
        await DatabaseSessionsManager._maintain_multiplexed_session(r)

    async def test_close_branches(self):
        # coverage for line 225-234
        manager = DatabaseSessionsManager(self.database, self.pool)

        # Branch where thread is None
        await manager.close()

        # Branch where thread is not None
        async def fake_coro():
            try:
                await asyncio.sleep(10)
            except asyncio.CancelledError:
                pass

        task = asyncio.create_task(fake_coro())
        manager._multiplexed_session_thread = task
        mock_session = mock.AsyncMock()
        manager._multiplexed_session = mock_session
        manager._multiplexed_session_terminate_event = mock.Mock()

        with mock.patch(
            "google.cloud.spanner_v1._async.database_sessions_manager.CrossSync.is_async",
            True,
        ):
            await manager.close()
            # task is cancelled and awaited in close()
            self.assertTrue(task.done())
            manager._multiplexed_session_terminate_event.set.assert_called_once()
            self.assertIsNone(manager._multiplexed_session)
            mock_session.delete.assert_not_called()

        # Sync branch of close
        manager._multiplexed_session_thread = mock.Mock()
        mock_session_sync = mock.AsyncMock()
        manager._multiplexed_session = mock_session_sync
        manager._multiplexed_session_terminate_event = mock.Mock()
        with mock.patch(
            "google.cloud.spanner_v1._async.database_sessions_manager.CrossSync.is_async",
            False,
        ):
            await manager.close()
            self.assertTrue(manager._multiplexed_session_thread.join.called)
            manager._multiplexed_session_terminate_event.set.assert_called_once()
            self.assertIsNone(manager._multiplexed_session)
            mock_session_sync.delete.assert_not_called()

    async def test_maintain_multiplexed_session_refresh(self):
        # coverage for line 196-202
        manager = DatabaseSessionsManager(self.database, self.pool)
        manager._multiplexed_session_lock = asyncio.Lock()
        manager._multiplexed_session_terminate_event = asyncio.Event()
        manager._multiplexed_session = mock.AsyncMock()

        # We need to simulate time passing and then terminating
        refresh_interval = manager._MAINTENANCE_THREAD_REFRESH_INTERVAL.total_seconds()

        import time
        from weakref import ref

        start_time = time.monotonic()

        call_count = 0

        def mock_time():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return start_time
            if call_count >= 2:
                # Trigger refresh
                return start_time + refresh_interval + 10
            return start_time

        with mock.patch(
            "google.cloud.spanner_v1._async.database_sessions_manager.time.monotonic",
            side_effect=mock_time,
        ):

            async def mock_build():
                manager._multiplexed_session_terminate_event.set()
                return mock.AsyncMock()

            with mock.patch.object(
                manager, "_build_multiplexed_session", side_effect=mock_build
            ):
                await manager._maintain_multiplexed_session(ref(manager))

        self.assertTrue(manager._multiplexed_session_terminate_event.is_set())

    async def test_maintain_multiplexed_session_manager_gone_in_loop(self):
        # Mock session_manager_ref() within the loop
        manager = DatabaseSessionsManager(self.database, self.pool)
        call_count = 0

        def mock_ref():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return manager
            return None

        with mock.patch(
            "google.cloud.spanner_v1._async.database_sessions_manager.time.monotonic",
            return_value=0,
        ):
            r = mock.Mock(side_effect=mock_ref)
            await DatabaseSessionsManager._maintain_multiplexed_session(r)
            self.assertEqual(call_count, 2)

    async def test_maintain_multiplexed_session_loop_sleep(self):
        manager = DatabaseSessionsManager(self.database, self.pool)
        manager._multiplexed_session_lock = asyncio.Lock()
        manager._multiplexed_session_terminate_event = asyncio.Event()
        call_count = 0

        def mock_time():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return 0  # start_time
            if call_count == 2:
                return 1  # within refresh interval
            # terminate
            manager._multiplexed_session_terminate_event.set()
            return 1000

        from weakref import ref

        async def mock_wait(event, timeout=None):
            event.set()

        with mock.patch(
            "google.cloud.spanner_v1._async.database_sessions_manager.time.monotonic",
            side_effect=mock_time,
        ):
            with mock.patch(
                "google.cloud.spanner_v1._async.database_sessions_manager.CrossSync.event_wait",
                side_effect=mock_wait,
            ) as mock_event_wait:
                await manager._maintain_multiplexed_session(ref(manager))
                mock_event_wait.assert_called_once()

    async def test_get_multiplexed_session_fast_path(self):
        manager = DatabaseSessionsManager(self.database, self.pool)
        mock_session = mock.Mock()
        manager._multiplexed_session = mock_session
        manager._init_lock = mock.Mock(wraps=manager._init_lock)

        session = await manager._get_multiplexed_session()
        self.assertIs(session, mock_session)
        manager._init_lock.acquire.assert_not_called()
        self.assertIsNone(manager._multiplexed_session_lock)

    async def test_get_multiplexed_session_fast_path_lock_already_created(self):
        manager = DatabaseSessionsManager(self.database, self.pool)
        mock_session = mock.Mock()
        manager._multiplexed_session = mock_session
        mock_lock = mock.AsyncMock()
        manager._multiplexed_session_lock = mock_lock
        manager._init_lock = mock.Mock(wraps=manager._init_lock)

        session = await manager._get_multiplexed_session()
        self.assertIs(session, mock_session)
        manager._init_lock.acquire.assert_not_called()
        mock_lock.acquire.assert_not_called()
        mock_lock.__aenter__.assert_not_called()

    async def test_maintain_multiplexed_session_rotates_session(self):
        from weakref import ref

        manager = DatabaseSessionsManager(self.database, self.pool)
        manager._multiplexed_session_lock = asyncio.Lock()
        manager._multiplexed_session_terminate_event = mock.Mock()
        manager._multiplexed_session_terminate_event.is_set.side_effect = [
            False,
            True,
        ]

        old_session = mock.AsyncMock()
        new_session = mock.AsyncMock()
        manager._multiplexed_session = old_session

        refresh_interval = manager._MAINTENANCE_THREAD_REFRESH_INTERVAL.total_seconds()
        call_count = 0

        def mock_time():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return 0
            return refresh_interval + 100

        with mock.patch(
            "google.cloud.spanner_v1._async.database_sessions_manager.time.monotonic",
            side_effect=mock_time,
        ):
            with mock.patch.object(
                manager, "_build_multiplexed_session", return_value=new_session
            ) as mock_build:
                await DatabaseSessionsManager._maintain_multiplexed_session(
                    ref(manager)
                )
                mock_build.assert_called_once()
                old_session.delete.assert_not_called()
                new_session.delete.assert_not_called()
                self.assertIs(manager._multiplexed_session, new_session)

    async def test_maintain_multiplexed_session_handles_build_failure(self):
        from weakref import ref

        manager = DatabaseSessionsManager(self.database, self.pool)
        manager._multiplexed_session_lock = asyncio.Lock()
        manager._multiplexed_session_terminate_event = asyncio.Event()

        current_session = mock.AsyncMock()
        manager._multiplexed_session = current_session

        refresh_interval = manager._MAINTENANCE_THREAD_REFRESH_INTERVAL.total_seconds()
        call_count = 0

        def mock_time():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return 0
            return refresh_interval + 100

        async def mock_event_wait(event, timeout=None):
            manager._multiplexed_session_terminate_event.set()

        with mock.patch(
            "google.cloud.spanner_v1._async.database_sessions_manager.time.monotonic",
            side_effect=mock_time,
        ):
            with mock.patch.object(
                manager,
                "_build_multiplexed_session",
                side_effect=Exception("network error"),
            ) as mock_build:
                with mock.patch(
                    "google.cloud.spanner_v1._async.database_sessions_manager.CrossSync.event_wait",
                    side_effect=mock_event_wait,
                ) as mock_event_wait_call:
                    await DatabaseSessionsManager._maintain_multiplexed_session(
                        ref(manager)
                    )
                    mock_build.assert_called_once()
                    mock_event_wait_call.assert_called_once()
                    current_session.delete.assert_not_called()
                    self.assertIs(manager._multiplexed_session, current_session)

    async def test_maintain_multiplexed_session_old_session_none(self):
        from weakref import ref

        manager = DatabaseSessionsManager(self.database, self.pool)
        manager._multiplexed_session_lock = asyncio.Lock()
        manager._multiplexed_session_terminate_event = asyncio.Event()

        new_session = mock.AsyncMock()
        manager._multiplexed_session = None

        refresh_interval = manager._MAINTENANCE_THREAD_REFRESH_INTERVAL.total_seconds()
        call_count = 0

        def mock_time():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return 0
            return refresh_interval + 100

        async def mock_event_wait(event, timeout=None):
            manager._multiplexed_session_terminate_event.set()

        with mock.patch(
            "google.cloud.spanner_v1._async.database_sessions_manager.time.monotonic",
            side_effect=mock_time,
        ):
            with mock.patch.object(
                manager, "_build_multiplexed_session", return_value=new_session
            ):
                with mock.patch(
                    "google.cloud.spanner_v1._async.database_sessions_manager.CrossSync.event_wait",
                    side_effect=mock_event_wait,
                ):

                    async def build_and_terminate():
                        manager._multiplexed_session_terminate_event.set()
                        return new_session

                    manager._build_multiplexed_session = build_and_terminate
                    await DatabaseSessionsManager._maintain_multiplexed_session(
                        ref(manager)
                    )
                    self.assertIs(manager._multiplexed_session, new_session)

    async def test_get_multiplexed_session_initial_failure_allows_retry(self):
        manager = DatabaseSessionsManager(self.database, self.pool)
        manager._multiplexed_session = None

        with mock.patch.object(
            manager,
            "_build_multiplexed_session",
            side_effect=Exception("create failed"),
        ):
            with self.assertRaises(Exception):
                await manager._get_multiplexed_session()
            self.assertIsNone(manager._multiplexed_session)

        # Subsequent call succeeds and creates session and maintenance thread
        mock_session = mock.Mock()
        with mock.patch.object(
            manager, "_build_multiplexed_session", return_value=mock_session
        ):
            with mock.patch.object(manager, "_build_maintenance_thread"):
                session = await manager._get_multiplexed_session()
                self.assertIs(session, mock_session)

    async def test_get_multiplexed_session_concurrent_initialization_double_checked(
        self,
    ):
        manager = DatabaseSessionsManager(self.database, self.pool)
        manager._multiplexed_session = None

        concurrent_session = mock.Mock()
        mock_lock = mock.AsyncMock()

        async def lock_enter():
            manager._multiplexed_session = concurrent_session
            return mock_lock

        mock_lock.__aenter__.side_effect = lock_enter

        with mock.patch.object(manager, "_build_multiplexed_session") as mock_build:
            with mock.patch(
                "google.cloud.spanner_v1._async.database_sessions_manager.CrossSync.Lock",
                return_value=mock_lock,
            ):
                session = await manager._get_multiplexed_session()
                self.assertIs(session, concurrent_session)
                mock_build.assert_not_called()

    async def test_get_multiplexed_session_maintenance_thread_failure_allows_retry(
        self,
    ):
        manager = DatabaseSessionsManager(self.database, self.pool)
        manager._multiplexed_session = None

        mock_session = mock.Mock()
        with mock.patch.object(
            manager, "_build_multiplexed_session", return_value=mock_session
        ):
            with mock.patch.object(
                manager,
                "_build_maintenance_thread",
                side_effect=RuntimeError("thread spawn failed"),
            ):
                with self.assertRaises(RuntimeError):
                    await manager._get_multiplexed_session()
                self.assertIsNone(manager._multiplexed_session)

    async def test_build_maintenance_thread(self):
        manager = DatabaseSessionsManager(self.database, self.pool)
        mock_session = mock.Mock()
        mock_session.session_id = "test-session-123"

        task = manager._build_maintenance_thread(mock_session)
        self.assertIsNotNone(task)
        task.cancel()

        # Backward compatibility when session is omitted
        manager._multiplexed_session = mock_session
        task_default = manager._build_maintenance_thread()
        self.assertIsNotNone(task_default)
        task_default.cancel()

    async def test_build_multiplexed_session(self):
        manager = DatabaseSessionsManager(self.database, self.pool)
        with mock.patch(
            "google.cloud.spanner_v1._async.database_sessions_manager.Session"
        ) as mock_session_class:
            mock_session_instance = mock.AsyncMock()
            mock_session_class.return_value = mock_session_instance
            session = await manager._build_multiplexed_session()
            self.assertIs(session, mock_session_instance)
            mock_session_instance.create.assert_called_once()

    async def test_put_session_multiplexed_and_regular(self):
        manager = DatabaseSessionsManager(self.database, self.pool)
        multiplexed_session = mock.Mock()
        multiplexed_session.is_multiplexed = True
        multiplexed_session.session_id = "multi-1"
        await manager.put_session(multiplexed_session)
        self.pool.put.assert_not_called()

        regular_session = mock.Mock()
        regular_session.is_multiplexed = False
        regular_session.session_id = "reg-1"
        await manager.put_session(regular_session)
        self.pool.put.assert_called_once_with(regular_session)

    def test_use_multiplexed_read_only(self):
        from google.cloud.spanner_v1._async.database_sessions_manager import (
            TransactionType,
        )

        with mock.patch.dict(
            "os.environ", {DatabaseSessionsManager._ENV_VAR_MULTIPLEXED: "false"}
        ):
            self.assertFalse(
                DatabaseSessionsManager._use_multiplexed(TransactionType.READ_ONLY)
            )
        with mock.patch.dict(
            "os.environ", {DatabaseSessionsManager._ENV_VAR_MULTIPLEXED: "true"}
        ):
            self.assertTrue(
                DatabaseSessionsManager._use_multiplexed(TransactionType.READ_ONLY)
            )

    def test_use_multiplexed_partitioned(self):
        from google.cloud.spanner_v1._async.database_sessions_manager import (
            TransactionType,
        )

        with mock.patch.dict(
            "os.environ",
            {DatabaseSessionsManager._ENV_VAR_MULTIPLEXED_PARTITIONED: "false"},
        ):
            self.assertFalse(
                DatabaseSessionsManager._use_multiplexed(TransactionType.PARTITIONED)
            )
        with mock.patch.dict(
            "os.environ",
            {DatabaseSessionsManager._ENV_VAR_MULTIPLEXED_PARTITIONED: "true"},
        ):
            self.assertTrue(
                DatabaseSessionsManager._use_multiplexed(TransactionType.PARTITIONED)
            )

    async def test_rotate_multiplexed_session_success(self):
        manager = DatabaseSessionsManager(self.database, self.pool)
        manager._multiplexed_session_lock = asyncio.Lock()
        old_session = mock.AsyncMock()
        new_session = mock.AsyncMock()
        manager._multiplexed_session = old_session

        with mock.patch.object(
            manager, "_build_multiplexed_session", return_value=new_session
        ):
            result = await manager._rotate_multiplexed_session()
            self.assertTrue(result)
            self.assertIs(manager._multiplexed_session, new_session)
            old_session.delete.assert_not_called()
            new_session.delete.assert_not_called()

    async def test_rotate_multiplexed_session_build_failure(self):
        manager = DatabaseSessionsManager(self.database, self.pool)
        manager._multiplexed_session_lock = asyncio.Lock()
        current_session = mock.AsyncMock()
        manager._multiplexed_session = current_session

        with mock.patch.object(
            manager,
            "_build_multiplexed_session",
            side_effect=Exception("network down"),
        ):
            result = await manager._rotate_multiplexed_session()
            self.assertFalse(result)
            self.assertIs(manager._multiplexed_session, current_session)
            current_session.delete.assert_not_called()
