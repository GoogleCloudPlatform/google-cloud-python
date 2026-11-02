# Copyright 2025, Google LLC All rights reserved.
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
import sys
from unittest import mock

try:
    from unittest.mock import AsyncMock
except ImportError:  # pragma: NO COVER
    from mock import AsyncMock  # type: ignore


import pytest

try:
    from grpc import aio
except ImportError:  # pragma: NO COVER
    pytest.skip("No GRPC", allow_module_level=True)

from google.api_core import bidi_async, exceptions

if sys.version_info < (3, 10):  # type: ignore[operator]

    def aiter(obj):
        return obj.__aiter__()

    async def anext(obj):
        return await obj.__anext__()


@pytest.mark.asyncio
class Test_AsyncRequestQueueGenerator:
    async def test_bounded_consume(self):
        call = mock.create_autospec(aio.Call, instance=True)
        call.done.return_value = False

        q = asyncio.Queue()
        await q.put(mock.sentinel.A)
        await q.put(mock.sentinel.B)

        generator = bidi_async._AsyncRequestQueueGenerator(q)
        generator.call = call

        items = []
        gen_aiter = aiter(generator)

        items.append(await anext(gen_aiter))
        items.append(await anext(gen_aiter))

        # At this point, the queue is empty. The next call to anext will sleep.
        # We make the call inactive.
        call.done.return_value = True

        with pytest.raises(asyncio.TimeoutError):
            await asyncio.wait_for(anext(gen_aiter), timeout=1)

        assert items == [mock.sentinel.A, mock.sentinel.B]

    async def test_yield_initial_and_exit(self):
        q = asyncio.Queue()
        call = mock.create_autospec(aio.Call, instance=True)
        call.done.return_value = True

        generator = bidi_async._AsyncRequestQueueGenerator(
            q, initial_request=mock.sentinel.A
        )
        generator.call = call

        assert await anext(aiter(generator)) == mock.sentinel.A

    async def test_yield_initial_callable_and_exit(self):
        q = asyncio.Queue()
        call = mock.create_autospec(aio.Call, instance=True)
        call.done.return_value = True

        generator = bidi_async._AsyncRequestQueueGenerator(
            q, initial_request=lambda: mock.sentinel.A
        )
        generator.call = call

        assert await anext(aiter(generator)) == mock.sentinel.A

    async def test_exit_when_inactive_with_item(self):
        q = asyncio.Queue()
        await q.put(mock.sentinel.A)

        call = mock.create_autospec(aio.Call, instance=True)
        call.done.return_value = True

        generator = bidi_async._AsyncRequestQueueGenerator(q)
        generator.call = call

        with pytest.raises(StopAsyncIteration) as exc_info:
            assert await anext(aiter(generator))
            assert (
                exc_info.value.args[0]
                == "Inactive call, replacing item on queue and exiting request generator."
            )

        # Make sure it put the item back.
        assert not q.empty()
        assert await q.get() == mock.sentinel.A

    async def test_exit_when_inactive_empty(self):
        q = asyncio.Queue()
        call = mock.create_autospec(aio.Call, instance=True)
        call.done.return_value = True

        generator = bidi_async._AsyncRequestQueueGenerator(q)
        generator.call = call

        with pytest.raises(asyncio.TimeoutError):
            await asyncio.wait_for(anext(aiter(generator)), timeout=1)

    async def test_exit_with_stop(self):
        q = asyncio.Queue()
        await q.put(None)
        call = mock.create_autospec(aio.Call, instance=True)
        call.done.return_value = False

        generator = bidi_async._AsyncRequestQueueGenerator(q)
        generator.call = call

        with pytest.raises(StopAsyncIteration) as exc_info:
            assert await anext(aiter(generator))
            assert exc_info.value.args[0] == "Cleanly exiting request generator."


def make_async_rpc():
    """Makes a mock async RPC used to test Bidi classes."""
    call = mock.create_autospec(aio.StreamStreamCall, instance=True)
    rpc = AsyncMock()

    def rpc_side_effect(request, metadata=None):
        call.done.return_value = False
        return call

    rpc.side_effect = rpc_side_effect

    def cancel_side_effect():
        call.done.return_value = True
        return True

    call.cancel.side_effect = cancel_side_effect
    call.read = AsyncMock()

    return rpc, call


class AsyncClosedCall:
    def __init__(self, exception):
        self.exception = exception

    def done(self):
        return True

    async def read(self):
        raise self.exception


class TestAsyncBidiRpc:
    def test_initial_state(self):
        bidi_rpc = bidi_async.AsyncBidiRpc(None)
        assert bidi_rpc.is_active is False

    def test_done_callbacks(self):
        bidi_rpc = bidi_async.AsyncBidiRpc(None)
        callback = mock.Mock(spec=["__call__"])

        bidi_rpc.add_done_callback(callback)
        bidi_rpc._on_call_done(mock.sentinel.future)

        callback.assert_called_once_with(mock.sentinel.future)

    @pytest.mark.asyncio
    @pytest.mark.skipif(
        sys.version_info < (3, 8),  # type: ignore[operator]
        reason="Python 3.8 below doesnt provide support for assert_awaited_once",
    )
    async def test_metadata(self):
        rpc, call = make_async_rpc()
        bidi_rpc = bidi_async.AsyncBidiRpc(rpc, metadata=mock.sentinel.A)
        assert bidi_rpc._rpc_metadata == mock.sentinel.A

        await bidi_rpc.open()
        assert bidi_rpc.call == call
        rpc.assert_awaited_once()
        assert rpc.call_args.kwargs["metadata"] == mock.sentinel.A

    @pytest.mark.asyncio
    async def test_open(self):
        rpc, call = make_async_rpc()
        bidi_rpc = bidi_async.AsyncBidiRpc(rpc)

        await bidi_rpc.open()

        assert bidi_rpc.call == call
        assert bidi_rpc.is_active
        call.add_done_callback.assert_called_once_with(bidi_rpc._on_call_done)

    @pytest.mark.asyncio
    async def test_open_error_already_open(self):
        rpc, _ = make_async_rpc()
        bidi_rpc = bidi_async.AsyncBidiRpc(rpc)

        await bidi_rpc.open()

        with pytest.raises(ValueError):
            await bidi_rpc.open()

    @pytest.mark.asyncio
    async def test_open_error_call_error(self):
        rpc, _ = make_async_rpc()
        expected_exception = exceptions.GoogleAPICallError(
            "test", response=mock.sentinel.response
        )
        rpc.side_effect = expected_exception
        bidi_rpc = bidi_async.AsyncBidiRpc(rpc)
        callback = mock.Mock(spec=["__call__"])
        bidi_rpc.add_done_callback(callback)

        with pytest.raises(exceptions.GoogleAPICallError) as exc_info:
            await bidi_rpc.open()

        assert exc_info.value == expected_exception
        callback.assert_called_once_with(mock.sentinel.response)

    @pytest.mark.asyncio
    async def test_close(self):
        rpc, call = make_async_rpc()
        bidi_rpc = bidi_async.AsyncBidiRpc(rpc)
        await bidi_rpc.open()

        await bidi_rpc.close()

        call.cancel.assert_called_once()
        assert bidi_rpc.call is call
        assert bidi_rpc.is_active is False
        # ensure the request queue was signaled to stop.
        assert bidi_rpc.pending_requests == 1
        assert await bidi_rpc._request_queue.get() is None
        # ensure request and callbacks are cleaned up
        assert bidi_rpc._initial_request is None
        assert not bidi_rpc._callbacks

    @pytest.mark.asyncio
    async def test_close_no_rpc(self):
        bidi_rpc = bidi_async.AsyncBidiRpc(None)
        await bidi_rpc.close()

    @pytest.mark.asyncio
    async def test_send(self):
        rpc, call = make_async_rpc()
        bidi_rpc = bidi_async.AsyncBidiRpc(rpc)
        await bidi_rpc.open()

        await bidi_rpc.send(mock.sentinel.request)

        assert bidi_rpc.pending_requests == 1
        assert await bidi_rpc._request_queue.get() is mock.sentinel.request

    @pytest.mark.asyncio
    async def test_send_not_open(self):
        bidi_rpc = bidi_async.AsyncBidiRpc(None)

        with pytest.raises(ValueError):
            await bidi_rpc.send(mock.sentinel.request)

    @pytest.mark.asyncio
    async def test_send_dead_rpc(self):
        error = ValueError()
        bidi_rpc = bidi_async.AsyncBidiRpc(None)
        bidi_rpc.call = AsyncClosedCall(error)

        with pytest.raises(ValueError) as exc_info:
            await bidi_rpc.send(mock.sentinel.request)

        assert exc_info.value == error

    @pytest.mark.asyncio
    async def test_recv(self):
        bidi_rpc = bidi_async.AsyncBidiRpc(None)
        bidi_rpc.call = mock.create_autospec(aio.Call, instance=True)
        bidi_rpc.call.read = AsyncMock(return_value=mock.sentinel.response)

        response = await bidi_rpc.recv()

        assert response == mock.sentinel.response

    @pytest.mark.asyncio
    async def test_recv_not_open(self):
        bidi_rpc = bidi_async.AsyncBidiRpc(None)

        with pytest.raises(ValueError):
            await bidi_rpc.recv()
