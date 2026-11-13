# Copyright 2024 Google LLC
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
import concurrent.futures
import functools
import queue
import threading
import time
import typing
from unittest import mock
from unittest.mock import AsyncMock  # type: ignore

import pytest
import pytest_asyncio

from google import api_core
from google.cloud.bigtable.data._cross_sync.cross_sync import CrossSync, T


class TestCrossSync:
    async def async_iter(self, in_list):
        for i in in_list:
            yield i

    @pytest.fixture
    def cs_sync(self):
        return CrossSync._Sync_Impl

    @pytest_asyncio.fixture
    def cs_async(self):
        return CrossSync

    @pytest.mark.parametrize(
        "attr, async_version, sync_version",
        [
            ("is_async", True, False),
            ("sleep", asyncio.sleep, time.sleep),
            (
                "retry_target",
                api_core.retry.retry_target_async,
                api_core.retry.retry_target,
            ),
            (
                "retry_target_stream",
                api_core.retry.retry_target_stream_async,
                api_core.retry.retry_target_stream,
            ),
            ("Retry", api_core.retry.AsyncRetry, api_core.retry.Retry),
            ("Queue", asyncio.Queue, queue.Queue),
            ("Condition", asyncio.Condition, threading.Condition),
            ("Future", asyncio.Future, concurrent.futures.Future),
            ("Task", asyncio.Task, concurrent.futures.Future),
            ("Event", asyncio.Event, threading.Event),
            ("Semaphore", asyncio.Semaphore, threading.Semaphore),
            ("StopIteration", StopAsyncIteration, StopIteration),
            # types
            ("Awaitable", typing.Awaitable, typing.Union[T]),
            ("Iterable", typing.AsyncIterable, typing.Iterable),
            ("Iterator", typing.AsyncIterator, typing.Iterator),
            ("Generator", typing.AsyncGenerator, typing.Generator),
        ],
    )
    def test_alias_attributes(
        self, attr, async_version, sync_version, cs_sync, cs_async
    ):
        """
        Test basic alias attributes, to ensure they point to the right place
        in both sync and async versions.
        """
        assert getattr(cs_async, attr) == async_version, (
            f"Failed async version for {attr}"
        )
        assert getattr(cs_sync, attr) == sync_version, f"Failed sync version for {attr}"

    @pytest.mark.asyncio
    async def test_Mock(self, cs_sync, cs_async):
        """
        Test Mock class in both sync and async versions
        """
        import unittest.mock

        assert isinstance(cs_async.Mock(), AsyncMock)
        assert isinstance(cs_sync.Mock(), unittest.mock.Mock)
        # test with return value
        assert await cs_async.Mock(return_value=1)() == 1
        assert cs_sync.Mock(return_value=1)() == 1

    def test_next(self, cs_sync):
        """
        Test sync version of CrossSync.next()
        """
        it = iter([1, 2, 3])
        assert cs_sync.next(it) == 1
        assert cs_sync.next(it) == 2
        assert cs_sync.next(it) == 3
        with pytest.raises(StopIteration):
            cs_sync.next(it)
        with pytest.raises(cs_sync.StopIteration):
            cs_sync.next(it)

    @pytest.mark.asyncio
    async def test_next_async(self, cs_async):
        """
        test async version of CrossSync.next()
        """
        async_it = self.async_iter([1, 2, 3])
        assert await cs_async.next(async_it) == 1
        assert await cs_async.next(async_it) == 2
        assert await cs_async.next(async_it) == 3
        with pytest.raises(StopAsyncIteration):
            await cs_async.next(async_it)
        with pytest.raises(cs_async.StopIteration):
            await cs_async.next(async_it)

    def test_gather_partials(self, cs_sync):
        """
        Test sync version of CrossSync.gather_partials()
        """
        with concurrent.futures.ThreadPoolExecutor() as e:
            partials = [lambda i=i: i + 1 for i in range(5)]
            results = cs_sync.gather_partials(partials, sync_executor=e)
            assert results == [1, 2, 3, 4, 5]

    def test_gather_partials_with_excepptions(self, cs_sync):
        """
        Test sync version of CrossSync.gather_partials() with exceptions
        """
        with concurrent.futures.ThreadPoolExecutor() as e:
            partials = [lambda i=i: i + 1 if i != 3 else 1 / 0 for i in range(5)]
            with pytest.raises(ZeroDivisionError):
                cs_sync.gather_partials(partials, sync_executor=e)

    def test_gather_partials_return_exceptions(self, cs_sync):
        """
        Test sync version of CrossSync.gather_partials() with return_exceptions=True
        """
        with concurrent.futures.ThreadPoolExecutor() as e:
            partials = [lambda i=i: i + 1 if i != 3 else 1 / 0 for i in range(5)]
            results = cs_sync.gather_partials(
                partials, return_exceptions=True, sync_executor=e
            )
            assert len(results) == 5
            assert results[0] == 1
            assert results[1] == 2
            assert results[2] == 3
            assert isinstance(results[3], ZeroDivisionError)
            assert results[4] == 5

    def test_gather_partials_no_executor(self, cs_sync):
        """
        Test sync version of CrossSync.gather_partials() without an executor
        """
        partials = [lambda i=i: i + 1 for i in range(5)]
        with pytest.raises(ValueError) as e:
            cs_sync.gather_partials(partials)
        assert "sync_executor is required" in str(e.value)

    @pytest.mark.asyncio
    async def test_gather_partials_async(self, cs_async):
        """
        Test async version of CrossSync.gather_partials()
        """

        async def coro(i):
            return i + 1

        partials = [functools.partial(coro, i) for i in range(5)]
        results = await cs_async.gather_partials(partials)
        assert results == [1, 2, 3, 4, 5]

    @pytest.mark.asyncio
    async def test_gather_partials_async_with_exceptions(self, cs_async):
        """
        Test async version of CrossSync.gather_partials() with exceptions
        """

        async def coro(i):
            return i + 1 if i != 3 else 1 / 0

        partials = [functools.partial(coro, i) for i in range(5)]
        with pytest.raises(ZeroDivisionError):
            await cs_async.gather_partials(partials)

    @pytest.mark.asyncio
    async def test_gather_partials_async_return_exceptions(self, cs_async):
        """
        Test async version of CrossSync.gather_partials() with return_exceptions=True
        """

        async def coro(i):
            return i + 1 if i != 3 else 1 / 0

        partials = [functools.partial(coro, i) for i in range(5)]
        results = await cs_async.gather_partials(partials, return_exceptions=True)
        assert len(results) == 5
        assert results[0] == 1
        assert results[1] == 2
        assert results[2] == 3
        assert isinstance(results[3], ZeroDivisionError)
        assert results[4] == 5

    @pytest.mark.asyncio
    async def test_gather_partials_async_uses_asyncio_gather(self, cs_async):
        """
        CrossSync.gather_partials() should use asyncio.gather() internally
        """

        async def coro(i):
            return i + 1

        return_exceptions = object()
        partials = [functools.partial(coro, i) for i in range(5)]
        with mock.patch.object(asyncio, "gather", AsyncMock()) as gather:
            await cs_async.gather_partials(
                partials, return_exceptions=return_exceptions
            )
            gather.assert_called_once()
            found_args, found_kwargs = gather.call_args
            assert found_kwargs["return_exceptions"] == return_exceptions
            for coro in found_args:
                await coro

    def test_wait(self, cs_sync):
        """
        Test sync version of CrossSync.wait()

        If future is complete, it should be in the first (complete) set
        """
        future = concurrent.futures.Future()
        future.set_result(1)
        s1, s2 = cs_sync.wait([future])
        assert s1 == {future}
        assert s2 == set()

    def test_wait_timeout(self, cs_sync):
        """
        If timeout occurs, future should be in the second (incomplete) set
        """
        future = concurrent.futures.Future()
        timeout = 0.1
        start_time = time.monotonic()
        s1, s2 = cs_sync.wait([future], timeout)
        end_time = time.monotonic()
        assert abs((end_time - start_time) - timeout) < 0.01
        assert s1 == set()
        assert s2 == {future}

    def test_wait_passthrough(self, cs_sync):
        """
        sync version of CrossSync.wait() should pass through to concurrent.futures.wait()
        """
        future = object()
        timeout = object()
        with mock.patch.object(concurrent.futures, "wait", mock.Mock()) as wait:
            result = cs_sync.wait([future], timeout)
            assert wait.call_count == 1
            assert wait.call_args == (([future],), {"timeout": timeout})
            assert result == wait.return_value

    def test_wait_empty_input(self, cs_sync):
        """
        If no futures are provided, return empty sets
        """
        s1, s2 = cs_sync.wait([])
        assert s1 == set()
        assert s2 == set()

    @pytest.mark.asyncio
    async def test_wait_async(self, cs_async):
        """
        Test async version of CrossSync.wait()
        """
        future = asyncio.Future()
        future.set_result(1)
        s1, s2 = await cs_async.wait([future])
        assert s1 == {future}
        assert s2 == set()

    @pytest.mark.asyncio
    async def test_wait_async_timeout(self, cs_async):
        """
        If timeout occurs, future should be in the second (incomplete) set
        """
        future = asyncio.Future()
        timeout = 0.1
        start_time = time.monotonic()
        s1, s2 = await cs_async.wait([future], timeout)
        end_time = time.monotonic()
        assert abs((end_time - start_time) - timeout) < 0.01
        assert s1 == set()
        assert s2 == {future}

    @pytest.mark.asyncio
    async def test_wait_async_passthrough(self, cs_async):
        """
        async version of CrossSync.wait() should pass through to asyncio.wait()
        """
        future = object()
        timeout = object()
        with mock.patch.object(asyncio, "wait", AsyncMock()) as wait:
            result = await cs_async.wait([future], timeout)
            assert wait.call_count == 1
            assert wait.call_args == (([future],), {"timeout": timeout})
            assert result == wait.return_value

    @pytest.mark.asyncio
    async def test_wait_async_empty_input(self, cs_async):
        """
        If no futures are provided, return empty sets
        """
        s1, s2 = await cs_async.wait([])
        assert s1 == set()
        assert s2 == set()

    def test_event_wait_passthrough(self, cs_sync):
        """
        Test sync version of CrossSync.event_wait()
        should pass through timeout directly to the event.wait() call
        """
        event = mock.Mock()
        timeout = object()
        cs_sync.event_wait(event, timeout)
        event.wait.assert_called_once_with(timeout=timeout)

    @pytest.mark.parametrize("timeout", [0, 0.01, 0.05])
    def test_event_wait_timeout_exceeded(self, cs_sync, timeout):
        """
        Test sync version of CrossSync.event_wait()
        """
        event = threading.Event()
        start_time = time.monotonic()
        cs_sync.event_wait(event, timeout=timeout)
        end_time = time.monotonic()
        assert abs((end_time - start_time) - timeout) < 0.01

    def test_event_wait_already_set(self, cs_sync):
        """
        if event is already set, do not block
        """
        event = threading.Event()
        event.set()
        start_time = time.monotonic()
        cs_sync.event_wait(event, timeout=10)
        end_time = time.monotonic()
        assert end_time - start_time < 0.01

    @pytest.mark.parametrize("break_early", [True, False])
    @pytest.mark.asyncio
    async def test_event_wait_async(self, cs_async, break_early):
        """
        With no timeout, call event.wait() with no arguments
        """
        event = AsyncMock()
        await cs_async.event_wait(event, async_break_early=break_early)
        event.wait.assert_called_once_with()

    @pytest.mark.asyncio
    async def test_event_wait_async_with_timeout(self, cs_async):
        """
        In with timeout set, should call event.wait(), wrapped in wait_for()
        for the timeout
        """
        event = mock.Mock()
        event.wait.return_value = object()
        timeout = object()
        with mock.patch.object(asyncio, "wait_for", AsyncMock()) as wait_for:
            await cs_async.event_wait(event, timeout=timeout)
            assert wait_for.await_count == 1
            assert wait_for.call_count == 1
            wait_for.assert_called_once_with(event.wait(), timeout=timeout)

    @pytest.mark.asyncio
    async def test_event_wait_async_timeout_exceeded(self, cs_async):
        """
        If tiemout exceeded, break without throwing exception
        """
        event = asyncio.Event()
        timeout = 0.5
        start_time = time.monotonic()
        await cs_async.event_wait(event, timeout=timeout)
        end_time = time.monotonic()
        assert abs((end_time - start_time) - timeout) < 0.01

    @pytest.mark.parametrize("break_early", [True, False])
    @pytest.mark.asyncio
    async def test_event_wait_async_already_set(self, cs_async, break_early):
        """
        if event is already set, return immediately
        """
        event = AsyncMock()
        event.is_set = lambda: True
        start_time = time.monotonic()
        await cs_async.event_wait(event, async_break_early=break_early)
        end_time = time.monotonic()
        assert abs(end_time - start_time) < 0.01

    @pytest.mark.asyncio
    async def test_event_wait_no_break_early(self, cs_async):
        """
        if async_break_early is False, and the event is not set,
        simply sleep for the timeout
        """
        event = mock.Mock()
        event.is_set.return_value = False
        timeout = object()
        with mock.patch.object(asyncio, "sleep", AsyncMock()) as sleep:
            await cs_async.event_wait(event, timeout=timeout, async_break_early=False)
            sleep.assert_called_once_with(timeout)

    def test_create_task(self, cs_sync):
        """
        Test creating Future using create_task()
        """
        executor = concurrent.futures.ThreadPoolExecutor()
        fn = lambda x, y: x + y  # noqa: E731
        result = cs_sync.create_task(fn, 1, y=4, sync_executor=executor)
        assert isinstance(result, cs_sync.Task)
        assert result.result() == 5

    def test_create_task_passthrough(self, cs_sync):
        """
        sync version passed through to executor.submit()
        """
        fn = object()
        executor = mock.Mock()
        executor.submit.return_value = object()
        args = [1, 2, 3]
        kwargs = {"a": 1, "b": 2}
        result = cs_sync.create_task(fn, *args, **kwargs, sync_executor=executor)
        assert result == executor.submit.return_value
        assert executor.submit.call_count == 1
        assert executor.submit.call_args == ((fn, *args), kwargs)

    def test_create_task_no_executor(self, cs_sync):
        """
        if no executor is provided, raise an exception
        """
        with pytest.raises(ValueError) as e:
            cs_sync.create_task(lambda: None)
        assert "sync_executor is required" in str(e.value)

    def test_create_daemon_task(self, cs_sync):
        """
        create_daemon_task should run on a daemon thread and return a Future
        """
        result = cs_sync.create_daemon_task(
            lambda x, y: (x + y, threading.current_thread().daemon),
            2,
            y=3,
            task_name="test-daemon",
        )
        assert isinstance(result, cs_sync.Task)
        assert result.result(timeout=5) == (5, True)

    def test_create_daemon_task_exception(self, cs_sync):
        """
        create_daemon_task should propagate exceptions onto the returned Future
        """

        def fail():
            raise ValueError("boom")

        result = cs_sync.create_daemon_task(fail)
        with pytest.raises(ValueError, match="boom"):
            result.result(timeout=5)

    @pytest.mark.asyncio
    async def test_create_daemon_task_async(self, cs_async):
        """
        Async create_daemon_task should create an asyncio.Task
        """

        async def coro_fn(x, y):
            return x + y

        result = cs_async.create_daemon_task(coro_fn, 2, y=3, task_name="async-daemon")
        assert isinstance(result, asyncio.Task)
        assert result.get_name() == "async-daemon"
        assert await result == 5

    @pytest.mark.asyncio
    async def test_create_task_async(self, cs_async):
        """
        Test creating Future using create_task()
        """

        async def coro_fn(x, y):
            return x + y

        result = cs_async.create_task(coro_fn, 1, y=4)
        assert isinstance(result, asyncio.Task)
        assert await result == 5

    @pytest.mark.asyncio
    async def test_create_task_async_passthrough(self, cs_async):
        """
        async version passed through to asyncio.create_task()
        """
        coro_fn = mock.Mock()
        coro_fn.return_value = object()
        args = [1, 2, 3]
        kwargs = {"a": 1, "b": 2}
        with mock.patch.object(asyncio, "create_task", mock.Mock()) as create_task:
            cs_async.create_task(coro_fn, *args, **kwargs)
            create_task.assert_called_once()
            create_task.assert_called_once_with(coro_fn.return_value)
            coro_fn.assert_called_once_with(*args, **kwargs)

    @pytest.mark.asyncio
    async def test_create_task_async_with_name(self, cs_async):
        """
        Test creating a task with a name
        """

        async def coro_fn():
            return None

        name = "test-name-456"
        result = cs_async.create_task(coro_fn, task_name=name)
        assert isinstance(result, asyncio.Task)
        assert result.get_name() == name

    def test_yeild_to_event_loop(self, cs_sync):
        """
        no-op in sync version
        """
        assert cs_sync.yield_to_event_loop() is None

    @pytest.mark.asyncio
    async def test_yield_to_event_loop_async(self, cs_async):
        """
        should call await asyncio.sleep(0)
        """
        with mock.patch.object(asyncio, "sleep", AsyncMock()) as sleep:
            await cs_async.yield_to_event_loop()
            sleep.assert_called_once_with(0)

    def test_verify_async_event_loop(self, cs_sync):
        """
        no-op in sync version
        """
        assert cs_sync.verify_async_event_loop() is None

    @pytest.mark.asyncio
    async def test_verify_async_event_loop_async(self, cs_async):
        """
        should call asyncio.get_running_loop()
        """
        with mock.patch.object(asyncio, "get_running_loop") as get_running_loop:
            cs_async.verify_async_event_loop()
            get_running_loop.assert_called_once()

    def test_verify_async_event_loop_no_event_loop(self, cs_async):
        """
        Should raise an exception if no event loop is running
        """
        with pytest.raises(RuntimeError) as e:
            cs_async.verify_async_event_loop()
        assert "no running event loop" in str(e.value)

    def test_rmaio(self, cs_async):
        """
        rm_aio should return whatever is passed to it
        """
        assert cs_async.rm_aio(1) == 1
        assert cs_async.rm_aio("test") == "test"
        obj = object()
        assert cs_async.rm_aio(obj) == obj

    def test_add_mapping(self, cs_sync, cs_async):
        """
        Add dynamic attributes to each class using add_mapping()
        """
        for cls in [cs_sync, cs_async]:
            cls.add_mapping("test", 1)
            assert cls.test == 1
            assert cls._runtime_replacements[(cls, "test")] == 1

    def test_add_duplicate_mapping(self, cs_sync, cs_async):
        """
        Adding the same attribute twice should raise an exception
        """
        for cls in [cs_sync, cs_async]:
            cls.add_mapping("duplicate", 1)
            with pytest.raises(AttributeError) as e:
                cls.add_mapping("duplicate", 2)
                assert "Conflicting assignments" in str(e.value)

    def test_add_mapping_decorator(self, cs_sync, cs_async):
        """
        add_mapping_decorator should allow wrapping classes with add_mapping()
        """
        for cls in [cs_sync, cs_async]:

            @cls.add_mapping_decorator("decorated")
            class Decorated:
                pass

            assert cls.decorated == Decorated
