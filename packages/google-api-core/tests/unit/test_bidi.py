# Copyright 2018, Google LLC All rights reserved.
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
import logging
import queue
import threading
import time

try:
    from unittest import mock
    from unittest.mock import AsyncMock  # pragma: NO COVER  # noqa: F401
except ImportError:  # pragma: NO COVER
    import mock  # type: ignore

import pytest

try:
    import grpc
except ImportError:  # pragma: NO COVER
    pytest.skip("No GRPC", allow_module_level=True)

from google.api_core import bidi, exceptions


class Test_RequestQueueGenerator(object):
    def test_bounded_consume(self):
        call = mock.create_autospec(grpc.Call, instance=True)
        call.is_active.return_value = True

        def queue_generator(rpc):
            yield mock.sentinel.A
            yield queue.Empty()
            yield mock.sentinel.B
            rpc.is_active.return_value = False
            yield mock.sentinel.C

        q = mock.create_autospec(queue.Queue, instance=True)
        q.get.side_effect = queue_generator(call)

        generator = bidi._RequestQueueGenerator(q)
        generator.call = call

        items = list(generator)

        assert items == [mock.sentinel.A, mock.sentinel.B]

    def test_yield_initial_and_exit(self):
        q = mock.create_autospec(queue.Queue, instance=True)
        q.get.side_effect = queue.Empty()
        call = mock.create_autospec(grpc.Call, instance=True)
        call.is_active.return_value = False

        generator = bidi._RequestQueueGenerator(q, initial_request=mock.sentinel.A)
        generator.call = call

        items = list(generator)

        assert items == [mock.sentinel.A]

    def test_yield_initial_callable_and_exit(self):
        q = mock.create_autospec(queue.Queue, instance=True)
        q.get.side_effect = queue.Empty()
        call = mock.create_autospec(grpc.Call, instance=True)
        call.is_active.return_value = False

        generator = bidi._RequestQueueGenerator(
            q, initial_request=lambda: mock.sentinel.A
        )
        generator.call = call

        items = list(generator)

        assert items == [mock.sentinel.A]

    def test_exit_when_inactive_with_item(self):
        q = mock.create_autospec(queue.Queue, instance=True)
        q.get.side_effect = [mock.sentinel.A, queue.Empty()]
        call = mock.create_autospec(grpc.Call, instance=True)
        call.is_active.return_value = False

        generator = bidi._RequestQueueGenerator(q)
        generator.call = call

        items = list(generator)

        assert items == []
        # Make sure it put the item back.
        q.put.assert_called_once_with(mock.sentinel.A)

    def test_exit_when_inactive_empty(self):
        q = mock.create_autospec(queue.Queue, instance=True)
        q.get.side_effect = queue.Empty()
        call = mock.create_autospec(grpc.Call, instance=True)
        call.is_active.return_value = False

        generator = bidi._RequestQueueGenerator(q)
        generator.call = call

        items = list(generator)

        assert items == []

    def test_exit_with_stop(self):
        q = mock.create_autospec(queue.Queue, instance=True)
        q.get.side_effect = [None, queue.Empty()]
        call = mock.create_autospec(grpc.Call, instance=True)
        call.is_active.return_value = True

        generator = bidi._RequestQueueGenerator(q)
        generator.call = call

        items = list(generator)

        assert items == []


class Test_Throttle(object):
    def test_repr(self):
        delta = datetime.timedelta(seconds=4.5)
        instance = bidi._Throttle(access_limit=42, time_window=delta)
        assert repr(instance) == "_Throttle(access_limit=42, time_window={})".format(
            repr(delta)
        )

    def test_raises_error_on_invalid_init_arguments(self):
        with pytest.raises(ValueError) as exc_info:
            bidi._Throttle(access_limit=10, time_window=datetime.timedelta(seconds=0.0))
        assert "time_window" in str(exc_info.value)
        assert "must be a positive timedelta" in str(exc_info.value)

        with pytest.raises(ValueError) as exc_info:
            bidi._Throttle(access_limit=0, time_window=datetime.timedelta(seconds=10))
        assert "access_limit" in str(exc_info.value)
        assert "must be positive" in str(exc_info.value)

    def test_does_not_delay_entry_attempts_under_threshold(self):
        throttle = bidi._Throttle(
            access_limit=3, time_window=datetime.timedelta(seconds=1)
        )
        entries = []

        for _ in range(3):
            with throttle as time_waited:
                entry_info = {
                    "entered_at": datetime.datetime.now(),
                    "reported_wait": time_waited,
                }
                entries.append(entry_info)

        # check the reported wait times ...
        assert all(entry["reported_wait"] == 0.0 for entry in entries)

        # .. and the actual wait times
        delta = entries[1]["entered_at"] - entries[0]["entered_at"]
        assert delta.total_seconds() < 0.1
        delta = entries[2]["entered_at"] - entries[1]["entered_at"]
        assert delta.total_seconds() < 0.1

    def test_delays_entry_attempts_above_threshold(self):
        throttle = bidi._Throttle(
            access_limit=3, time_window=datetime.timedelta(seconds=1)
        )
        entries = []

        for _ in range(6):
            with throttle as time_waited:
                entry_info = {
                    "entered_at": datetime.datetime.now(),
                    "reported_wait": time_waited,
                }
                entries.append(entry_info)

        # For each group of 4 consecutive entries the time difference between
        # the first and the last entry must have been greater than time_window,
        # because a maximum of 3 are allowed in each time_window.
        for i, entry in enumerate(entries[3:], start=3):
            first_entry = entries[i - 3]
            delta = entry["entered_at"] - first_entry["entered_at"]
            assert delta.total_seconds() > 1.0

        # check the reported wait times
        # (NOTE: not using assert all(...), b/c the coverage check would complain)
        for i, entry in enumerate(entries):
            if i != 3:
                assert entry["reported_wait"] == 0.0

        # The delayed entry is expected to have been delayed for a significant
        # chunk of the full second, and the actual and reported delay times
        # should reflect that.
        assert entries[3]["reported_wait"] > 0.7
        delta = entries[3]["entered_at"] - entries[2]["entered_at"]
        assert delta.total_seconds() > 0.7


class _CallAndFuture(grpc.Call, grpc.Future):
    pass


def make_rpc():
    """Makes a mock RPC used to test Bidi classes."""
    call = mock.create_autospec(_CallAndFuture, instance=True)
    rpc = mock.create_autospec(grpc.StreamStreamMultiCallable, instance=True)

    def rpc_side_effect(request, metadata=None):
        call.is_active.return_value = True
        call.request = request
        call.metadata = metadata
        return call

    rpc.side_effect = rpc_side_effect

    def cancel_side_effect():
        call.is_active.return_value = False

    call.cancel.side_effect = cancel_side_effect

    return rpc, call


class ClosedCall(object):
    def __init__(self, exception):
        self.exception = exception

    def __next__(self):
        raise self.exception

    def is_active(self):
        return False


class TestBidiRpc(object):
    def test_initial_state(self):
        bidi_rpc = bidi.BidiRpc(None)

        assert bidi_rpc.is_active is False

    def test_done_callbacks(self):
        bidi_rpc = bidi.BidiRpc(None)
        callback = mock.Mock(spec=["__call__"])

        bidi_rpc.add_done_callback(callback)
        bidi_rpc._on_call_done(mock.sentinel.future)

        callback.assert_called_once_with(mock.sentinel.future)

    def test_metadata(self):
        rpc, call = make_rpc()
        bidi_rpc = bidi.BidiRpc(rpc, metadata=mock.sentinel.A)
        assert bidi_rpc._rpc_metadata == mock.sentinel.A

        bidi_rpc.open()
        assert bidi_rpc.call == call
        assert bidi_rpc.call.metadata == mock.sentinel.A

    def test_open(self):
        rpc, call = make_rpc()
        bidi_rpc = bidi.BidiRpc(rpc)

        bidi_rpc.open()

        assert bidi_rpc.call == call
        assert bidi_rpc.is_active
        call.add_done_callback.assert_called_once_with(bidi_rpc._on_call_done)

    def test_open_error_already_open(self):
        rpc, _ = make_rpc()
        bidi_rpc = bidi.BidiRpc(rpc)

        bidi_rpc.open()

        with pytest.raises(ValueError):
            bidi_rpc.open()

    def test_close(self):
        rpc, call = make_rpc()
        bidi_rpc = bidi.BidiRpc(rpc)
        bidi_rpc.open()

        bidi_rpc.close()

        call.cancel.assert_called_once()
        assert bidi_rpc.call == call
        assert bidi_rpc.is_active is False
        # ensure the request queue was signaled to stop.
        assert bidi_rpc.pending_requests == 1
        assert bidi_rpc._request_queue.get() is None
        # ensure request and callbacks are cleaned up
        assert bidi_rpc._initial_request is None
        assert not bidi_rpc._callbacks

    def test_close_with_no_rpc(self):
        bidi_rpc = bidi.BidiRpc(None)
        bidi_rpc.close()

        assert bidi_rpc.call is None
        assert bidi_rpc.is_active is False
        # ensure the request queue was signaled to stop.
        assert bidi_rpc.pending_requests == 1
        assert bidi_rpc._request_queue.get() is None
        # ensure request and callbacks are cleaned up
        assert bidi_rpc._initial_request is None
        assert not bidi_rpc._callbacks

    def test_send(self):
        rpc, call = make_rpc()
        bidi_rpc = bidi.BidiRpc(rpc)
        bidi_rpc.open()

        bidi_rpc.send(mock.sentinel.request)

        assert bidi_rpc.pending_requests == 1
        assert bidi_rpc._request_queue.get() is mock.sentinel.request

    def test_send_not_open(self):
        rpc, call = make_rpc()
        bidi_rpc = bidi.BidiRpc(rpc)

        with pytest.raises(ValueError):
            bidi_rpc.send(mock.sentinel.request)

    def test_send_dead_rpc(self):
        error = ValueError()
        bidi_rpc = bidi.BidiRpc(None)
        bidi_rpc.call = ClosedCall(error)

        with pytest.raises(ValueError) as exc_info:
            bidi_rpc.send(mock.sentinel.request)

        assert exc_info.value == error

    def test_recv(self):
        bidi_rpc = bidi.BidiRpc(None)
        bidi_rpc.call = iter([mock.sentinel.response])

        response = bidi_rpc.recv()

        assert response == mock.sentinel.response

    def test_recv_not_open(self):
        rpc, call = make_rpc()
        bidi_rpc = bidi.BidiRpc(rpc)

        with pytest.raises(ValueError):
            bidi_rpc.recv()


class CallStub(object):
    def __init__(self, values, active=True):
        self.values = iter(values)
        self._is_active = active
        self.cancelled = False

    def __next__(self):
        item = next(self.values)
        if isinstance(item, Exception):
            self._is_active = False
            raise item
        return item

    def is_active(self):
        return self._is_active

    def add_done_callback(self, callback):
        pass

    def cancel(self):
        self.cancelled = True


class TestResumableBidiRpc(object):
    def test_ctor_defaults(self):
        start_rpc = mock.Mock()
        should_recover = mock.Mock()
        bidi_rpc = bidi.ResumableBidiRpc(start_rpc, should_recover)

        assert bidi_rpc.is_active is False
        assert bidi_rpc._finalized is False
        assert bidi_rpc._start_rpc is start_rpc
        assert bidi_rpc._should_recover is should_recover
        assert bidi_rpc._should_terminate is bidi._never_terminate
        assert bidi_rpc._initial_request is None
        assert bidi_rpc._rpc_metadata is None
        assert bidi_rpc._reopen_throttle is None

    def test_ctor_explicit(self):
        start_rpc = mock.Mock()
        should_recover = mock.Mock()
        should_terminate = mock.Mock()
        initial_request = mock.Mock()
        metadata = {"x-foo": "bar"}
        bidi_rpc = bidi.ResumableBidiRpc(
            start_rpc,
            should_recover,
            should_terminate=should_terminate,
            initial_request=initial_request,
            metadata=metadata,
            throttle_reopen=True,
        )

        assert bidi_rpc.is_active is False
        assert bidi_rpc._finalized is False
        assert bidi_rpc._should_recover is should_recover
        assert bidi_rpc._should_terminate is should_terminate
        assert bidi_rpc._initial_request is initial_request
        assert bidi_rpc._rpc_metadata == metadata
        assert isinstance(bidi_rpc._reopen_throttle, bidi._Throttle)

    def test_done_callbacks_terminate(self):
        cancellation = mock.Mock()
        start_rpc = mock.Mock()
        should_recover = mock.Mock(spec=["__call__"], return_value=True)
        should_terminate = mock.Mock(spec=["__call__"], return_value=True)
        bidi_rpc = bidi.ResumableBidiRpc(
            start_rpc, should_recover, should_terminate=should_terminate
        )
        callback = mock.Mock(spec=["__call__"])

        bidi_rpc.add_done_callback(callback)
        bidi_rpc._on_call_done(cancellation)

        should_terminate.assert_called_once_with(cancellation)
        should_recover.assert_not_called()
        callback.assert_called_once_with(cancellation)
        assert not bidi_rpc.is_active

    def test_done_callbacks_recoverable(self):
        start_rpc = mock.create_autospec(grpc.StreamStreamMultiCallable, instance=True)
        should_recover = mock.Mock(spec=["__call__"], return_value=True)
        bidi_rpc = bidi.ResumableBidiRpc(start_rpc, should_recover)
        callback = mock.Mock(spec=["__call__"])

        bidi_rpc.add_done_callback(callback)
        bidi_rpc._on_call_done(mock.sentinel.future)

        callback.assert_not_called()
        start_rpc.assert_called_once()
        should_recover.assert_called_once_with(mock.sentinel.future)
        assert bidi_rpc.is_active

    def test_done_callbacks_non_recoverable(self):
        start_rpc = mock.create_autospec(grpc.StreamStreamMultiCallable, instance=True)
        should_recover = mock.Mock(spec=["__call__"], return_value=False)
        bidi_rpc = bidi.ResumableBidiRpc(start_rpc, should_recover)
        callback = mock.Mock(spec=["__call__"])

        bidi_rpc.add_done_callback(callback)
        bidi_rpc._on_call_done(mock.sentinel.future)

        callback.assert_called_once_with(mock.sentinel.future)
        should_recover.assert_called_once_with(mock.sentinel.future)
        assert not bidi_rpc.is_active

    def test_send_terminate(self):
        cancellation = ValueError()
        call_1 = CallStub([cancellation], active=False)
        call_2 = CallStub([])
        start_rpc = mock.create_autospec(
            grpc.StreamStreamMultiCallable, instance=True, side_effect=[call_1, call_2]
        )
        should_recover = mock.Mock(spec=["__call__"], return_value=False)
        should_terminate = mock.Mock(spec=["__call__"], return_value=True)
        bidi_rpc = bidi.ResumableBidiRpc(
            start_rpc, should_recover, should_terminate=should_terminate
        )

        bidi_rpc.open()

        bidi_rpc.send(mock.sentinel.request)

        assert bidi_rpc.pending_requests == 1
        assert bidi_rpc._request_queue.get() is None

        should_recover.assert_not_called()
        should_terminate.assert_called_once_with(cancellation)
        assert bidi_rpc.call == call_1
        assert bidi_rpc.is_active is False
        assert call_1.cancelled is True

    def test_send_recover(self):
        error = ValueError()
        call_1 = CallStub([error], active=False)
        call_2 = CallStub([])
        start_rpc = mock.create_autospec(
            grpc.StreamStreamMultiCallable, instance=True, side_effect=[call_1, call_2]
        )
        should_recover = mock.Mock(spec=["__call__"], return_value=True)
        bidi_rpc = bidi.ResumableBidiRpc(start_rpc, should_recover)

        bidi_rpc.open()

        bidi_rpc.send(mock.sentinel.request)

        assert bidi_rpc.pending_requests == 1
        assert bidi_rpc._request_queue.get() is mock.sentinel.request

        should_recover.assert_called_once_with(error)
        assert bidi_rpc.call == call_2
        assert bidi_rpc.is_active is True

    def test_send_failure(self):
        error = ValueError()
        call = CallStub([error], active=False)
        start_rpc = mock.create_autospec(
            grpc.StreamStreamMultiCallable, instance=True, return_value=call
        )
        should_recover = mock.Mock(spec=["__call__"], return_value=False)
        bidi_rpc = bidi.ResumableBidiRpc(start_rpc, should_recover)

        bidi_rpc.open()

        with pytest.raises(ValueError) as exc_info:
            bidi_rpc.send(mock.sentinel.request)

        assert exc_info.value == error
        should_recover.assert_called_once_with(error)
        assert bidi_rpc.call == call
        assert bidi_rpc.is_active is False
        assert call.cancelled is True
        assert bidi_rpc.pending_requests == 1
        assert bidi_rpc._request_queue.get() is None

    def test_recv_terminate(self):
        cancellation = ValueError()
        call = CallStub([cancellation])
        start_rpc = mock.create_autospec(
            grpc.StreamStreamMultiCallable, instance=True, return_value=call
        )
        should_recover = mock.Mock(spec=["__call__"], return_value=False)
        should_terminate = mock.Mock(spec=["__call__"], return_value=True)
        bidi_rpc = bidi.ResumableBidiRpc(
            start_rpc, should_recover, should_terminate=should_terminate
        )

        bidi_rpc.open()

        bidi_rpc.recv()

        should_recover.assert_not_called()
        should_terminate.assert_called_once_with(cancellation)
        assert bidi_rpc.call == call
        assert bidi_rpc.is_active is False
        assert call.cancelled is True

    def test_recv_recover(self):
        error = ValueError()
        call_1 = CallStub([1, error])
        call_2 = CallStub([2, 3])
        start_rpc = mock.create_autospec(
            grpc.StreamStreamMultiCallable, instance=True, side_effect=[call_1, call_2]
        )
        should_recover = mock.Mock(spec=["__call__"], return_value=True)
        bidi_rpc = bidi.ResumableBidiRpc(start_rpc, should_recover)

        bidi_rpc.open()

        values = []
        for n in range(3):
            values.append(bidi_rpc.recv())

        assert values == [1, 2, 3]
        should_recover.assert_called_once_with(error)
        assert bidi_rpc.call == call_2
        assert bidi_rpc.is_active is True

    def test_recv_recover_already_recovered(self):
        call_1 = CallStub([])
        call_2 = CallStub([])
        start_rpc = mock.create_autospec(
            grpc.StreamStreamMultiCallable, instance=True, side_effect=[call_1, call_2]
        )
        callback = mock.Mock()
        callback.return_value = True
        bidi_rpc = bidi.ResumableBidiRpc(start_rpc, callback)

        bidi_rpc.open()

        bidi_rpc._reopen()

        assert bidi_rpc.call is call_1
        assert bidi_rpc.is_active is True

    def test_recv_failure(self):
        error = ValueError()
        call = CallStub([error])
        start_rpc = mock.create_autospec(
            grpc.StreamStreamMultiCallable, instance=True, return_value=call
        )
        should_recover = mock.Mock(spec=["__call__"], return_value=False)
        bidi_rpc = bidi.ResumableBidiRpc(start_rpc, should_recover)

        bidi_rpc.open()

        with pytest.raises(ValueError) as exc_info:
            bidi_rpc.recv()

        assert exc_info.value == error
        should_recover.assert_called_once_with(error)
        assert bidi_rpc.call == call
        assert bidi_rpc.is_active is False
        assert call.cancelled is True

    def test_close(self):
        call = mock.create_autospec(_CallAndFuture, instance=True)

        def cancel_side_effect():
            call.is_active.return_value = False

        call.cancel.side_effect = cancel_side_effect
        start_rpc = mock.create_autospec(
            grpc.StreamStreamMultiCallable, instance=True, return_value=call
        )
        should_recover = mock.Mock(spec=["__call__"], return_value=False)
        bidi_rpc = bidi.ResumableBidiRpc(start_rpc, should_recover)
        bidi_rpc.open()

        bidi_rpc.close()

        should_recover.assert_not_called()
        call.cancel.assert_called_once()
        assert bidi_rpc.call == call
        assert bidi_rpc.is_active is False
        # ensure the request queue was signaled to stop.
        assert bidi_rpc.pending_requests == 1
        assert bidi_rpc._request_queue.get() is None
        assert bidi_rpc._finalized
        assert bidi_rpc._initial_request is None
        assert not bidi_rpc._callbacks

    def test_reopen_failure_on_rpc_restart(self):
        error1 = ValueError("1")
        error2 = ValueError("2")
        call = CallStub([error1])
        # Invoking start RPC a second time will trigger an error.
        start_rpc = mock.create_autospec(
            grpc.StreamStreamMultiCallable, instance=True, side_effect=[call, error2]
        )
        should_recover = mock.Mock(spec=["__call__"], return_value=True)
        callback = mock.Mock(spec=["__call__"])

        bidi_rpc = bidi.ResumableBidiRpc(start_rpc, should_recover)
        bidi_rpc.add_done_callback(callback)

        bidi_rpc.open()

        with pytest.raises(ValueError) as exc_info:
            bidi_rpc.recv()

        assert exc_info.value == error2
        should_recover.assert_called_once_with(error1)
        assert bidi_rpc.call is None
        assert bidi_rpc.is_active is False
        callback.assert_called_once_with(error2)

    def test_using_throttle_on_reopen_requests(self):
        call = CallStub([])
        start_rpc = mock.create_autospec(
            grpc.StreamStreamMultiCallable, instance=True, return_value=call
        )
        should_recover = mock.Mock(spec=["__call__"], return_value=True)
        bidi_rpc = bidi.ResumableBidiRpc(
            start_rpc, should_recover, throttle_reopen=True
        )

        patcher = mock.patch.object(bidi_rpc._reopen_throttle.__class__, "__enter__")
        with patcher as mock_enter:
            bidi_rpc._reopen()

        mock_enter.assert_called_once()

    def test_send_not_open(self):
        bidi_rpc = bidi.ResumableBidiRpc(None, lambda _: False)

        with pytest.raises(ValueError):
            bidi_rpc.send(mock.sentinel.request)

    def test_recv_not_open(self):
        bidi_rpc = bidi.ResumableBidiRpc(None, lambda _: False)

        with pytest.raises(ValueError):
            bidi_rpc.recv()

    def test_finalize_idempotent(self):
        error1 = ValueError("1")
        error2 = ValueError("2")
        callback = mock.Mock(spec=["__call__"])
        should_recover = mock.Mock(spec=["__call__"], return_value=False)

        bidi_rpc = bidi.ResumableBidiRpc(mock.sentinel.start_rpc, should_recover)

        bidi_rpc.add_done_callback(callback)

        bidi_rpc._on_call_done(error1)
        bidi_rpc._on_call_done(error2)

        callback.assert_called_once_with(error1)


class TestBackgroundConsumer(object):
    def test_consume_once_then_exit(self):
        bidi_rpc = mock.create_autospec(bidi.BidiRpc, instance=True)
        bidi_rpc.is_active = True
        bidi_rpc.recv.side_effect = [mock.sentinel.response_1]
        recved = threading.Event()

        def on_response(response):
            assert response == mock.sentinel.response_1
            bidi_rpc.is_active = False
            recved.set()

        consumer = bidi.BackgroundConsumer(bidi_rpc, on_response)

        consumer.start()

        recved.wait()

        bidi_rpc.recv.assert_called_once()
        assert bidi_rpc.is_active is False

        consumer.stop()

        bidi_rpc.close.assert_called_once()
        assert consumer.is_active is False

    def test_pause_resume_and_close(self):
        # This test is relatively complex. It attempts to start the consumer,
        # consume one item, pause the consumer, check the state of the world,
        # then resume the consumer. Doing this in a deterministic fashion
        # requires a bit more mocking and patching than usual.

        bidi_rpc = mock.create_autospec(bidi.BidiRpc, instance=True)
        bidi_rpc.is_active = True

        def close_side_effect():
            bidi_rpc.is_active = False

        bidi_rpc.close.side_effect = close_side_effect

        # These are used to coordinate the two threads to ensure deterministic
        # execution.
        should_continue = threading.Event()
        responses_and_events = {
            mock.sentinel.response_1: threading.Event(),
            mock.sentinel.response_2: threading.Event(),
        }
        bidi_rpc.recv.side_effect = [mock.sentinel.response_1, mock.sentinel.response_2]

        recved_responses = []
        consumer = None

        def on_response(response):
            if response == mock.sentinel.response_1:
                consumer.pause()

            recved_responses.append(response)
            responses_and_events[response].set()
            should_continue.wait()

        consumer = bidi.BackgroundConsumer(bidi_rpc, on_response)

        consumer.start()

        # Wait for the first response to be recved.
        responses_and_events[mock.sentinel.response_1].wait()

        # Ensure only one item has been recved and that the consumer is paused.
        assert recved_responses == [mock.sentinel.response_1]
        assert consumer.is_paused is True
        assert consumer.is_active is True

        # Unpause the consumer, wait for the second item, then close the
        # consumer.
        should_continue.set()
        consumer.resume()

        responses_and_events[mock.sentinel.response_2].wait()

        assert recved_responses == [mock.sentinel.response_1, mock.sentinel.response_2]

        consumer.stop()

        assert consumer.is_active is False
        assert consumer._on_response is None

    def test_wake_on_error(self):
        should_continue = threading.Event()

        bidi_rpc = mock.create_autospec(bidi.BidiRpc, instance=True)
        bidi_rpc.is_active = True
        bidi_rpc.add_done_callback.side_effect = lambda _: should_continue.set()

        consumer = bidi.BackgroundConsumer(bidi_rpc, mock.sentinel.on_response)

        # Start the consumer paused, which should immediately put it into wait
        # state.
        consumer.pause()
        consumer.start()

        # Wait for add_done_callback to be called
        should_continue.wait()
        bidi_rpc.add_done_callback.assert_called_once_with(consumer._on_call_done)

        # The consumer should now be blocked on waiting to be unpaused.
        assert consumer.is_active
        assert consumer.is_paused

        # Trigger the done callback, it should unpause the consumer and cause
        # it to exit.
        bidi_rpc.is_active = False
        consumer._on_call_done(bidi_rpc)

        # It may take a few cycles for the thread to exit.
        while consumer.is_active:
            pass

    def test_rpc_callback_fires_when_consumer_start_fails(self):
        expected_exception = exceptions.InvalidArgument(
            "test", response=grpc.StatusCode.INVALID_ARGUMENT
        )
        callback = mock.Mock(spec=["__call__"])

        rpc, _ = make_rpc()
        bidi_rpc = bidi.BidiRpc(rpc)
        bidi_rpc.add_done_callback(callback)
        bidi_rpc._start_rpc.side_effect = expected_exception

        consumer = bidi.BackgroundConsumer(bidi_rpc, on_response=None)

        consumer.start()

        # Wait for the consumer's thread to exit.
        while consumer.is_active:
            pass  # pragma: NO COVER

        assert callback.call_args.args[0] == grpc.StatusCode.INVALID_ARGUMENT

    def test_consumer_expected_error(self, caplog):
        caplog.set_level(logging.DEBUG)

        bidi_rpc = mock.create_autospec(bidi.BidiRpc, instance=True)
        bidi_rpc.is_active = True
        bidi_rpc.recv.side_effect = exceptions.ServiceUnavailable("Gone away")

        on_response = mock.Mock(spec=["__call__"])

        consumer = bidi.BackgroundConsumer(bidi_rpc, on_response)

        consumer.start()

        # Wait for the consumer's thread to exit.
        while consumer.is_active:
            pass

        on_response.assert_not_called()
        bidi_rpc.recv.assert_called_once()
        assert "caught error" in caplog.text

    def test_consumer_unexpected_error(self, caplog):
        caplog.set_level(logging.DEBUG)

        bidi_rpc = mock.create_autospec(bidi.BidiRpc, instance=True)
        bidi_rpc.is_active = True
        bidi_rpc.recv.side_effect = ValueError()

        on_response = mock.Mock(spec=["__call__"])

        consumer = bidi.BackgroundConsumer(bidi_rpc, on_response)

        consumer.start()

        # Wait for the consumer's thread to exit.
        while consumer.is_active:
            pass  # pragma: NO COVER (race condition)

        on_response.assert_not_called()
        bidi_rpc.recv.assert_called_once()
        assert "caught unexpected exception" in caplog.text

    def test_double_stop(self, caplog):
        caplog.set_level(logging.DEBUG)
        bidi_rpc = mock.create_autospec(bidi.BidiRpc, instance=True)
        bidi_rpc.is_active = True
        on_response = mock.Mock(spec=["__call__"])

        def close_side_effect():
            bidi_rpc.is_active = False

        bidi_rpc.close.side_effect = close_side_effect

        consumer = bidi.BackgroundConsumer(bidi_rpc, on_response)

        consumer.start()
        assert consumer.is_active is True

        consumer.stop()
        assert consumer.is_active is False
        assert consumer._on_response is None

        # calling stop twice should not result in an error.
        consumer.stop()

    def test_stop_error_logs(self, caplog):
        """
        Closing the client should result in no internal error logs

        https://github.com/googleapis/python-api-core/issues/788
        """
        caplog.set_level(logging.DEBUG)
        bidi_rpc = mock.create_autospec(bidi.BidiRpc, instance=True)
        bidi_rpc.is_active = True
        on_response = mock.Mock(spec=["__call__"])

        consumer = bidi.BackgroundConsumer(bidi_rpc, on_response)

        consumer.start()
        consumer.stop()
        # let the background thread run for a while before exiting
        time.sleep(0.1)
        bidi_rpc.is_active = False
        # running thread should not result in error logs
        error_logs = [r.message for r in caplog.records if r.levelname == "ERROR"]
        assert not error_logs, f"Found unexpected ERROR logs: {error_logs}"
        bidi_rpc.is_active = False

    def test_fatal_exceptions_can_inform_consumer(self, caplog):
        """
        https://github.com/googleapis/python-api-core/issues/820
        Exceptions thrown in the BackgroundConsumer not caught by `should_recover` / `should_terminate`
        on the RPC should be bubbled back to the caller through `on_fatal_exception`, if passed.
        """
        caplog.set_level(logging.DEBUG)

        for fatal_exception in (
            ValueError("some non-api error"),
            exceptions.PermissionDenied("some api error"),
        ):
            bidi_rpc = mock.create_autospec(bidi.ResumableBidiRpc, instance=True)
            bidi_rpc.is_active = True
            on_response = mock.Mock(spec=["__call__"])

            on_fatal_exception = mock.Mock(spec=["__call__"])

            bidi_rpc.open.side_effect = fatal_exception

            consumer = bidi.BackgroundConsumer(
                bidi_rpc, on_response, on_fatal_exception
            )

            consumer.start()
            # let the background thread run for a while before exiting
            time.sleep(0.1)

            on_fatal_exception.assert_called_once_with(fatal_exception)
