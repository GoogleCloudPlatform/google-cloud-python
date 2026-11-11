# Copyright 2017, Google LLC
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
from unittest import mock

import pytest

# isort: split
from google.api_core import exceptions
from google.api_core.future import async_future


class AsyncFuture(async_future.AsyncFuture):
    async def done(self):
        return False

    async def cancel(self):
        return True

    async def cancelled(self):
        return False

    async def running(self):
        return True


@pytest.mark.asyncio
async def test_polling_future_constructor():
    future = AsyncFuture()
    assert not await future.done()
    assert not await future.cancelled()
    assert await future.running()
    assert await future.cancel()


@pytest.mark.asyncio
async def test_set_result():
    future = AsyncFuture()

    future.set_result(1)

    assert await future.result() == 1
    callback_called = asyncio.Event()

    def callback(unused_future):
        callback_called.set()

    future.add_done_callback(callback)
    await callback_called.wait()


@pytest.mark.asyncio
async def test_set_exception():
    future = AsyncFuture()
    exception = ValueError("meep")

    future.set_exception(exception)

    assert await future.exception() == exception
    with pytest.raises(ValueError):
        await future.result()

    callback_called = asyncio.Event()

    def callback(unused_future):
        callback_called.set()

    future.add_done_callback(callback)
    await callback_called.wait()


@pytest.mark.asyncio
async def test_invoke_callback_exception():
    future = AsyncFuture()
    future.set_result(42)

    # This should not raise, despite the callback causing an exception.
    callback_called = asyncio.Event()

    def callback(unused_future):
        callback_called.set()
        raise ValueError()

    future.add_done_callback(callback)
    await callback_called.wait()


class AsyncFutureWithPoll(AsyncFuture):
    def __init__(self):
        super().__init__()
        self.poll_count = 0
        self.event = asyncio.Event()

    async def done(self):
        self.poll_count += 1
        await self.event.wait()
        self.set_result(42)
        return True


@pytest.mark.asyncio
async def test_result_with_polling():
    future = AsyncFutureWithPoll()

    future.event.set()
    result = await future.result()

    assert result == 42
    assert future.poll_count == 1
    # Repeated calls should not cause additional polling
    assert await future.result() == result
    assert future.poll_count == 1


class AsyncFutureTimeout(AsyncFutureWithPoll):
    async def done(self):
        await asyncio.sleep(0.2)
        return False


@pytest.mark.asyncio
async def test_result_timeout():
    future = AsyncFutureTimeout()
    with pytest.raises(asyncio.TimeoutError):
        await future.result(timeout=0.2)


@pytest.mark.asyncio
async def test_exception_timeout():
    future = AsyncFutureTimeout()
    with pytest.raises(asyncio.TimeoutError):
        await future.exception(timeout=0.2)


@pytest.mark.asyncio
async def test_result_timeout_with_retry():
    future = AsyncFutureTimeout()
    with pytest.raises(asyncio.TimeoutError):
        await future.exception(timeout=0.4)


class AsyncFutureTransient(AsyncFutureWithPoll):
    def __init__(self, errors):
        super().__init__()
        self._errors = errors

    async def done(self):
        if self._errors:
            error, self._errors = self._errors[0], self._errors[1:]
            raise error("testing")
        self.poll_count += 1
        self.set_result(42)
        return True


@mock.patch("asyncio.sleep", autospec=True)
@pytest.mark.asyncio
async def test_result_transient_error(unused_sleep):
    future = AsyncFutureTransient(
        (
            exceptions.TooManyRequests,
            exceptions.InternalServerError,
            exceptions.BadGateway,
        )
    )
    result = await future.result()
    assert result == 42
    assert future.poll_count == 1
    # Repeated calls should not cause additional polling
    assert await future.result() == result
    assert future.poll_count == 1


@pytest.mark.asyncio
async def test_callback_concurrency():
    future = AsyncFutureWithPoll()

    callback_called = asyncio.Event()

    def callback(unused_future):
        callback_called.set()

    future.add_done_callback(callback)

    # Give the thread a second to poll
    await asyncio.sleep(1)
    assert future.poll_count == 1

    future.event.set()
    await callback_called.wait()


@pytest.mark.asyncio
async def test_double_callback_concurrency():
    future = AsyncFutureWithPoll()

    callback_called = asyncio.Event()

    def callback(unused_future):
        callback_called.set()

    callback_called2 = asyncio.Event()

    def callback2(unused_future):
        callback_called2.set()

    future.add_done_callback(callback)
    future.add_done_callback(callback2)

    # Give the thread a second to poll
    await asyncio.sleep(1)
    future.event.set()

    assert future.poll_count == 1
    await callback_called.wait()
    await callback_called2.wait()


@pytest.mark.asyncio
@pytest.mark.parametrize("error_type", [exceptions.Forbidden, ValueError])
async def test_callback_polling_error(error_type):
    future = AsyncFuture()
    error = error_type("polling failed")
    future.done = mock.AsyncMock(side_effect=error)
    callback = mock.Mock()

    future.add_done_callback(callback)
    await asyncio.gather(future._background_task, return_exceptions=True)
    await asyncio.sleep(0)

    callback.assert_called_once_with(future._future)
    assert await future.exception() is error
    with pytest.raises(error_type) as exc_info:
        await future.result()
    assert exc_info.value is error
    future.done.assert_awaited_once()


@pytest.mark.asyncio
async def test_background_polling_error_after_result():
    future = AsyncFuture()
    polling_started = asyncio.Event()
    finish_polling = asyncio.Event()

    async def done():
        polling_started.set()
        await finish_polling.wait()
        raise ValueError("polling failed after completion")

    future.done = done
    callback = mock.Mock()
    future.add_done_callback(callback)
    await polling_started.wait()
    future.set_result(42)
    finish_polling.set()
    outcomes = await asyncio.gather(future._background_task, return_exceptions=True)
    await asyncio.sleep(0)

    assert outcomes == [None]
    callback.assert_called_once_with(future._future)
    assert await future.result() == 42


@pytest.mark.asyncio
async def test_background_polling_cancelled():
    future = AsyncFutureWithPoll()
    callback = mock.Mock()
    future.add_done_callback(callback)
    await asyncio.sleep(0)
    future._background_task.cancel()

    with pytest.raises(asyncio.CancelledError):
        await future._background_task

    callback.assert_not_called()
    assert not future._future.done()


@pytest.mark.asyncio
async def test_foreground_polling_error():
    future = AsyncFuture()
    error = exceptions.Forbidden("polling failed")
    future.done = mock.AsyncMock(side_effect=error)

    with pytest.raises(exceptions.Forbidden) as exc_info:
        await future.result()

    assert exc_info.value is error
    assert not future._future.done()
