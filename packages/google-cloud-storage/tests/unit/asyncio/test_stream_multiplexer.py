# Copyright 2026 Google LLC
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
from unittest.mock import AsyncMock

import grpc
import pytest

from google.cloud import _storage_v2
from google.cloud.storage.asyncio._stream_multiplexer import (
    _DEFAULT_QUEUE_MAX_SIZE,
    _StreamEnd,
    _StreamError,
    _StreamMultiplexer,
)


class TestSentinelTypes:
    def test_stream_error_stores_exception_and_generation(self):
        # Given an exception and a generation
        exc = ValueError("test")

        # When a StreamError is created
        error = _StreamError(exc, generation=3)

        # Then it stores the exception and generation
        assert error.exception is exc
        assert error.generation == 3


class TestStreamMultiplexerInit:
    def test_init_sets_stream_and_defaults(self):
        # Given a mock stream
        mock_stream = AsyncMock()

        # When a multiplexer is created
        mux = _StreamMultiplexer(mock_stream)

        # Then it sets the stream and defaults
        assert mux._stream is mock_stream
        assert mux.stream_generation == 0
        assert mux._queues == {}
        assert mux._recv_task is None
        assert mux._queue_max_size == _DEFAULT_QUEUE_MAX_SIZE

    def test_init_custom_queue_size(self):
        # Given a mock stream
        mock_stream = AsyncMock()

        # When a multiplexer is created with a custom queue size
        mux = _StreamMultiplexer(mock_stream, queue_max_size=50)

        # Then it sets the custom queue size
        assert mux._queue_max_size == 50


def _make_response(read_id, data=b"data", range_end=False):
    return _storage_v2.BidiReadObjectResponse(
        object_data_ranges=[
            _storage_v2.ObjectRangeData(
                checksummed_data=_storage_v2.ChecksummedData(content=data),
                read_range=_storage_v2.ReadRange(
                    read_id=read_id, read_offset=0, read_length=len(data)
                ),
                range_end=range_end,
            )
        ]
    )


def _make_multi_range_response(read_ids, data=b"data"):
    ranges = []
    for rid in read_ids:
        ranges.append(
            _storage_v2.ObjectRangeData(
                checksummed_data=_storage_v2.ChecksummedData(content=data),
                read_range=_storage_v2.ReadRange(
                    read_id=rid, read_offset=0, read_length=len(data)
                ),
            )
        )
    return _storage_v2.BidiReadObjectResponse(object_data_ranges=ranges)


class TestRegisterUnregister:
    def _make_multiplexer(self):
        mock_stream = AsyncMock()
        mock_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        return _StreamMultiplexer(mock_stream), mock_stream

    @pytest.mark.asyncio
    async def test_register_returns_bounded_queue(self):
        # Given a multiplexer
        mux, _ = self._make_multiplexer()

        # When registering read IDs
        queue = mux.register({1, 2, 3})

        # Then a bounded queue is returned
        assert isinstance(queue, asyncio.Queue)
        assert queue.maxsize == _DEFAULT_QUEUE_MAX_SIZE

    @pytest.mark.asyncio
    async def test_register_maps_read_ids_to_same_queue(self):
        # Given a multiplexer
        mux, _ = self._make_multiplexer()

        # When registering multiple read IDs
        queue = mux.register({10, 20})

        # Then they map to the same queue
        assert mux._queues[10] is queue
        assert mux._queues[20] is queue

    @pytest.mark.asyncio
    async def test_register_does_not_start_recv_loop(self):
        # Given a multiplexer
        mux, _ = self._make_multiplexer()

        # When registering a read ID
        mux.register({1})

        # Then the receive loop is not started
        assert mux._recv_task is None

    @pytest.mark.asyncio
    async def test_two_registers_get_separate_queues(self):
        # Given a multiplexer
        mux, _ = self._make_multiplexer()

        # When registering different read IDs separately
        q1 = mux.register({1})
        q2 = mux.register({2})

        # Then separate queues are returned
        assert q1 is not q2
        assert mux._queues[1] is q1
        assert mux._queues[2] is q2

    @pytest.mark.asyncio
    async def test_unregister_removes_read_ids(self):
        # Given a multiplexer with registered read IDs
        mux, _ = self._make_multiplexer()
        mux.register({1, 2})

        # When unregistering a read ID
        mux.unregister({1})

        # Then it is removed from the mapping
        assert 1 not in mux._queues
        assert 2 in mux._queues

    @pytest.mark.asyncio
    async def test_unregister_all_does_not_stop_recv_loop(self):
        # Given a multiplexer with an active receive loop
        mux, _ = self._make_multiplexer()
        mux.register({1})
        mux._ensure_recv_loop()
        recv_task = mux._recv_task

        # When unregistering the read ID
        mux.unregister({1})

        # Then the receive loop is not cancelled
        await asyncio.sleep(0)
        assert not recv_task.cancelled()

    @pytest.mark.asyncio
    async def test_unregister_nonexistent_is_noop(self):
        # Given a multiplexer with a registered read ID
        mux, _ = self._make_multiplexer()
        mux.register({1})

        # When unregistering a non-existent read ID
        mux.unregister({999})

        # Then the existing registration remains
        assert 1 in mux._queues


class TestRecvLoop:
    @pytest.mark.asyncio
    async def test_routes_response_by_read_id(self):
        # Given a multiplexer with registered queues for read IDs 10 and 20
        mock_stream = AsyncMock()
        resp1 = _make_response(read_id=10, data=b"hello")
        resp2 = _make_response(read_id=20, data=b"world")
        mock_stream.recv = AsyncMock(side_effect=[resp1, resp2, grpc.aio.EOF])

        mux = _StreamMultiplexer(mock_stream)
        q1 = mux.register({10})
        q2 = mux.register({20})

        # When the receive loop is started
        mux._ensure_recv_loop()

        # Then responses are routed to the corresponding queues and stream ends are sent
        item1 = await asyncio.wait_for(q1.get(), timeout=1)
        item2 = await asyncio.wait_for(q2.get(), timeout=1)

        assert item1 is resp1
        assert item2 is resp2

        end1 = await asyncio.wait_for(q1.get(), timeout=1)
        end2 = await asyncio.wait_for(q2.get(), timeout=1)
        assert isinstance(end1, _StreamEnd)
        assert isinstance(end2, _StreamEnd)

    @pytest.mark.asyncio
    async def test_deduplicates_when_multiple_read_ids_map_to_same_queue(self):
        # Given a multiplexer with multiple read IDs mapped to the same queue
        mock_stream = AsyncMock()
        resp = _make_multi_range_response([10, 11])
        mock_stream.recv = AsyncMock(side_effect=[resp, grpc.aio.EOF])

        mux = _StreamMultiplexer(mock_stream)
        queue = mux.register({10, 11})

        # When the receive loop is started
        mux._ensure_recv_loop()

        # Then the response is put into the queue only once
        item = await asyncio.wait_for(queue.get(), timeout=1)
        assert item is resp

        end = await asyncio.wait_for(queue.get(), timeout=1)
        assert isinstance(end, _StreamEnd)

    @pytest.mark.asyncio
    async def test_metadata_only_response_broadcast_to_all(self):
        # Given a multiplexer with multiple registered queues
        mock_stream = AsyncMock()
        metadata_resp = _storage_v2.BidiReadObjectResponse(
            read_handle=_storage_v2.BidiReadHandle(handle=b"handle")
        )
        mock_stream.recv = AsyncMock(side_effect=[metadata_resp, grpc.aio.EOF])

        mux = _StreamMultiplexer(mock_stream)
        q1 = mux.register({10})
        q2 = mux.register({20})

        # When the receive loop is started
        mux._ensure_recv_loop()

        # Then the metadata-only response is broadcast to all queues
        item1 = await asyncio.wait_for(q1.get(), timeout=1)
        item2 = await asyncio.wait_for(q2.get(), timeout=1)
        assert item1 is metadata_resp
        assert item2 is metadata_resp

    @pytest.mark.asyncio
    async def test_stream_end_sends_sentinel_to_all_queues(self):
        # Given a multiplexer with multiple registered queues and a stream that ends immediately
        mock_stream = AsyncMock()
        mock_stream.recv = AsyncMock(return_value=grpc.aio.EOF)

        mux = _StreamMultiplexer(mock_stream)
        q1 = mux.register({10})
        q2 = mux.register({20})

        # When the receive loop is started
        mux._ensure_recv_loop()

        # Then a StreamEnd sentinel is sent to all queues
        end1 = await asyncio.wait_for(q1.get(), timeout=1)
        end2 = await asyncio.wait_for(q2.get(), timeout=1)
        assert isinstance(end1, _StreamEnd)
        assert isinstance(end2, _StreamEnd)

    @pytest.mark.asyncio
    async def test_error_broadcasts_stream_error_to_all_queues(self):
        # Given a multiplexer with multiple registered queues and a stream that raises an error
        mock_stream = AsyncMock()
        exc = RuntimeError("stream broke")
        mock_stream.recv = AsyncMock(side_effect=exc)

        mux = _StreamMultiplexer(mock_stream)
        q1 = mux.register({10})
        q2 = mux.register({20})

        # When the receive loop is started
        mux._ensure_recv_loop()
        await asyncio.sleep(0.05)

        # Then a StreamError is broadcast to all queues
        err1 = q1.get_nowait()
        err2 = q2.get_nowait()
        assert isinstance(err1, _StreamError)
        assert err1.exception is exc
        assert err1.generation == 0
        assert isinstance(err2, _StreamError)
        assert err2.exception is exc

    @pytest.mark.asyncio
    async def test_error_uses_put_nowait(self):
        # Given a multiplexer with a full queue and a stream that raises an error
        mock_stream = AsyncMock()
        exc = RuntimeError("broke")
        mock_stream.recv = AsyncMock(side_effect=exc)

        mux = _StreamMultiplexer(mock_stream, queue_max_size=1)
        queue = mux.register({10})
        queue.put_nowait("filler")

        # When the receive loop is started
        mux._ensure_recv_loop()
        await asyncio.sleep(0.05)

        # Then the error is recorded even if the queue was full
        assert queue.qsize() == 1
        err = queue.get_nowait()
        assert isinstance(err, _StreamError)
        assert err.exception is exc

    @pytest.mark.asyncio
    async def test_unknown_read_id_is_dropped(self, caplog):
        # Given a multiplexer and a response with an unknown read ID
        mock_stream = AsyncMock()
        resp = _make_response(read_id=999)
        mock_stream.recv = AsyncMock(side_effect=[resp, grpc.aio.EOF])

        mux = _StreamMultiplexer(mock_stream)
        queue = mux.register({10})

        # When the receive loop is started
        mux._ensure_recv_loop()

        # Then the response is dropped and only StreamEnd is received
        end = await asyncio.wait_for(queue.get(), timeout=1)
        assert isinstance(end, _StreamEnd)

        # And a warning is logged
        assert "Received data for unregistered read_id: 999" in caplog.text


class TestSend:
    @pytest.mark.asyncio
    async def test_send_forwards_to_stream(self):
        # Given a multiplexer and a request
        mock_stream = AsyncMock()
        mock_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        mux = _StreamMultiplexer(mock_stream)
        request = _storage_v2.BidiReadObjectRequest(
            read_ranges=[
                _storage_v2.ReadRange(read_id=1, read_offset=0, read_length=10)
            ]
        )

        # When sending the request
        gen = await mux.send(request)

        # Then it is forwarded to the stream and current generation is returned
        mock_stream.send.assert_called_once_with(request)
        assert gen == 0

    @pytest.mark.asyncio
    async def test_send_returns_current_generation(self):
        # Given a multiplexer at generation 5
        mock_stream = AsyncMock()
        mock_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        mux = _StreamMultiplexer(mock_stream)
        mux._stream_generation = 5
        request = _storage_v2.BidiReadObjectRequest()

        # When sending a request
        gen = await mux.send(request)

        # Then it returns the current generation
        assert gen == 5

    @pytest.mark.asyncio
    async def test_send_propagates_exception(self):
        # Given a multiplexer where send fails
        mock_stream = AsyncMock()
        mock_stream.send = AsyncMock(side_effect=RuntimeError("send failed"))
        mock_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        mux = _StreamMultiplexer(mock_stream)

        # When sending a request
        # Then the exception is propagated
        with pytest.raises(RuntimeError, match="send failed"):
            await mux.send(_storage_v2.BidiReadObjectRequest())


class TestReopenStream:
    @pytest.mark.asyncio
    async def test_reopen_bumps_generation_and_replaces_stream(self):
        # Given a multiplexer with a registered queue
        old_stream = AsyncMock()
        old_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        mux = _StreamMultiplexer(old_stream)
        mux.register({1})

        new_stream = AsyncMock()
        new_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        factory = AsyncMock(return_value=new_stream)

        # When the stream is reopened with the correct generation
        await mux.reopen_stream(0, factory)

        # Then the generation is bumped and the stream is replaced
        assert mux.stream_generation == 1
        assert mux._stream is new_stream
        factory.assert_called_once()

    @pytest.mark.asyncio
    async def test_reopen_skips_if_generation_mismatch(self):
        # Given a multiplexer at generation 5
        mock_stream = AsyncMock()
        mock_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        mux = _StreamMultiplexer(mock_stream)
        mux._stream_generation = 5
        mux.register({1})

        factory = AsyncMock()

        # When reopen is called with a mismatched generation (3)
        await mux.reopen_stream(3, factory)

        # Then the reopen is skipped and generation remains unchanged
        assert mux.stream_generation == 5
        factory.assert_not_called()

    @pytest.mark.asyncio
    async def test_reopen_broadcasts_error_before_bump(self):
        # Given a multiplexer with a registered queue
        old_stream = AsyncMock()
        old_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        mux = _StreamMultiplexer(old_stream)
        queue = mux.register({1})

        new_stream = AsyncMock()
        new_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        factory = AsyncMock(return_value=new_stream)

        # When the stream is reopened
        await mux.reopen_stream(0, factory)

        # Then a StreamError is broadcast to the queue before the bump
        err = queue.get_nowait()
        assert isinstance(err, _StreamError)
        assert err.generation == 0

    @pytest.mark.asyncio
    async def test_reopen_starts_new_recv_loop(self):
        # Given a multiplexer with a registered queue and an active recv task
        old_stream = AsyncMock()
        old_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        mux = _StreamMultiplexer(old_stream)
        mux.register({1})
        old_recv_task = mux._recv_task

        new_stream = AsyncMock()
        new_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        factory = AsyncMock(return_value=new_stream)

        # When the stream is reopened
        await mux.reopen_stream(0, factory)

        # Then a new receive loop task is started
        assert mux._recv_task is not old_recv_task
        assert not mux._recv_task.done()

    @pytest.mark.asyncio
    async def test_reopen_closes_old_stream_best_effort(self):
        # Given a multiplexer where closing the old stream raises an error
        old_stream = AsyncMock()
        old_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        old_stream.close = AsyncMock(side_effect=RuntimeError("close failed"))
        mux = _StreamMultiplexer(old_stream)
        mux.register({1})

        new_stream = AsyncMock()
        new_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        factory = AsyncMock(return_value=new_stream)

        # When the stream is reopened
        await mux.reopen_stream(0, factory)

        # Then the reopen still succeeds
        assert mux.stream_generation == 1

    @pytest.mark.asyncio
    async def test_concurrent_reopen_only_one_wins(self):
        # Given a multiplexer and a counting factory
        old_stream = AsyncMock()
        old_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        mux = _StreamMultiplexer(old_stream)
        mux.register({1})

        call_count = 0

        async def counting_factory():
            nonlocal call_count
            call_count += 1
            new_stream = AsyncMock()
            new_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
            return new_stream

        # When concurrent reopen calls are made
        await asyncio.gather(
            mux.reopen_stream(0, counting_factory),
            mux.reopen_stream(0, counting_factory),
        )

        # Then only one factory call is made and generation is bumped once
        assert call_count == 1
        assert mux.stream_generation == 1

    @pytest.mark.asyncio
    async def test_reopen_factory_failure_leaves_generation_unchanged(self):
        """If stream_factory raises, generation is not bumped and recv loop
        is not restarted. The caller's retry manager will re-attempt reopen
        with the same generation, which will succeed because the generation
        check still matches."""
        # Given a multiplexer and a failing factory
        old_stream = AsyncMock()
        old_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        mux = _StreamMultiplexer(old_stream)
        mux.register({1})

        failing_factory = AsyncMock(side_effect=RuntimeError("open failed"))

        # When reopen fails
        with pytest.raises(RuntimeError, match="open failed"):
            await mux.reopen_stream(0, failing_factory)

        # Then generation is NOT bumped and recv loop is stopped
        assert mux.stream_generation == 0
        assert mux._recv_task is None or mux._recv_task.done()

        # Given a subsequent successful reopen
        new_stream = AsyncMock()
        new_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        ok_factory = AsyncMock(return_value=new_stream)

        # When reopen is called again with the same generation
        await mux.reopen_stream(0, ok_factory)

        # Then it succeeds
        assert mux.stream_generation == 1
        assert mux._stream is new_stream
        assert mux._recv_task is not None and not mux._recv_task.done()


class TestClose:
    @pytest.mark.asyncio
    async def test_close_cancels_recv_loop(self):
        # Given a multiplexer with an active receive loop
        mock_stream = AsyncMock()
        mock_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        mux = _StreamMultiplexer(mock_stream)
        mux.register({1})
        mux._ensure_recv_loop()
        recv_task = mux._recv_task

        # When closing the multiplexer
        await mux.close()

        # Then the receive loop task is cancelled
        assert recv_task.cancelled()

    @pytest.mark.asyncio
    async def test_close_broadcasts_terminal_error(self):
        # Given a multiplexer with registered queues
        mock_stream = AsyncMock()
        mock_stream.recv = AsyncMock(side_effect=asyncio.Event().wait)
        mux = _StreamMultiplexer(mock_stream)
        q1 = mux.register({1})
        q2 = mux.register({2})

        # When closing the multiplexer
        await mux.close()

        # Then a terminal StreamError is broadcast to all queues
        err1 = q1.get_nowait()
        err2 = q2.get_nowait()
        assert isinstance(err1, _StreamError)
        assert isinstance(err2, _StreamError)

    @pytest.mark.asyncio
    async def test_close_with_no_tasks_is_noop(self):
        # Given a multiplexer with no active tasks
        mock_stream = AsyncMock()
        mux = _StreamMultiplexer(mock_stream)

        # When closing the multiplexer
        # Then it should not raise any error
        await mux.close()  # should not raise
