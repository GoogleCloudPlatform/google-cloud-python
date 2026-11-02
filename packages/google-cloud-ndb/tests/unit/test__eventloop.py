# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import collections
from unittest import mock

import grpc
import pytest

from google.cloud.ndb import _eventloop, exceptions


def _Event(when=0, what="foo", args=(), kw={}):
    return _eventloop._Event(when, what, args, kw)


class TestEventLoop:
    @staticmethod
    def _make_one(**attrs):
        loop = _eventloop.EventLoop()
        for name, value in attrs.items():
            setattr(loop, name, value)
        return loop

    def test_constructor(self):
        loop = self._make_one()
        assert loop.current == collections.deque()
        assert loop.idlers == collections.deque()
        assert loop.inactive == 0
        assert loop.queue == []
        assert loop.rpcs == {}

    def test_clear_all(self):
        loop = self._make_one()
        loop.current.append("foo")
        loop.idlers.append("bar")
        loop.queue.append("baz")
        loop.rpcs["qux"] = "quux"
        loop.clear()
        assert not loop.current
        assert not loop.idlers
        assert not loop.queue
        assert not loop.rpcs

        # idemptotence (branch coverage)
        loop.clear()
        assert not loop.current
        assert not loop.idlers
        assert not loop.queue
        assert not loop.rpcs

    def test_clear_current(self):
        loop = self._make_one()
        loop.current.append("foo")
        loop.clear()
        assert not loop.current
        assert not loop.idlers
        assert not loop.queue
        assert not loop.rpcs

    def test_clear_idlers(self):
        loop = self._make_one()
        loop.idlers.append("foo")
        loop.clear()
        assert not loop.current
        assert not loop.idlers
        assert not loop.queue
        assert not loop.rpcs

    def test_insert_event_right_empty_queue(self):
        loop = self._make_one()
        event = _Event()
        loop.insort_event_right(event)
        assert loop.queue == [event]

    def test_insert_event_right_head(self):
        loop = self._make_one(queue=[_Event(1, "bar")])
        loop.insort_event_right(_Event(0, "foo"))
        assert loop.queue == [_Event(0, "foo"), _Event(1, "bar")]

    def test_insert_event_right_tail(self):
        loop = self._make_one(queue=[_Event(0, "foo")])
        loop.insort_event_right(_Event(1, "bar"))
        assert loop.queue == [_Event(0, "foo"), _Event(1, "bar")]

    def test_insert_event_right_middle(self):
        loop = self._make_one(queue=[_Event(0, "foo"), _Event(2, "baz")])
        loop.insort_event_right(_Event(1, "bar"))
        assert loop.queue == [
            _Event(0, "foo"),
            _Event(1, "bar"),
            _Event(2, "baz"),
        ]

    def test_insert_event_right_collision(self):
        loop = self._make_one(
            queue=[_Event(0, "foo"), _Event(1, "bar"), _Event(2, "baz")]
        )
        loop.insort_event_right(_Event(1, "barbar"))
        assert loop.queue == [
            _Event(0, "foo"),
            _Event(1, "bar"),
            _Event(1, "barbar"),
            _Event(2, "baz"),
        ]

    def test_call_soon(self):
        loop = self._make_one()
        loop.call_soon("foo", "bar", baz="qux")
        assert list(loop.current) == [("foo", ("bar",), {"baz": "qux"})]
        assert not loop.queue

    @mock.patch("google.cloud.ndb._eventloop.time")
    def test_queue_call_delay(self, time):
        loop = self._make_one()
        time.time.return_value = 5
        loop.queue_call(5, "foo", "bar", baz="qux")
        assert not loop.current
        assert loop.queue == [_Event(10, "foo", ("bar",), {"baz": "qux"})]

    @mock.patch("google.cloud.ndb._eventloop.time")
    def test_queue_call_absolute(self, time):
        loop = self._make_one()
        time.time.return_value = 5
        loop.queue_call(10e10, "foo", "bar", baz="qux")
        assert not loop.current
        assert loop.queue == [_Event(10e10, "foo", ("bar",), {"baz": "qux"})]

    def test_queue_rpc(self):
        loop = self._make_one()
        callback = mock.Mock(spec=())
        rpc = mock.Mock(spec=grpc.Future)
        loop.queue_rpc(rpc, callback)
        assert list(loop.rpcs.values()) == [callback]

        rpc_callback = rpc.add_done_callback.call_args[0][0]
        rpc_callback(rpc)
        rpc_id, rpc_result = loop.rpc_results.get()
        assert rpc_result is rpc
        assert loop.rpcs[rpc_id] is callback

    def test_add_idle(self):
        loop = self._make_one()
        loop.add_idle("foo", "bar", baz="qux")
        assert list(loop.idlers) == [("foo", ("bar",), {"baz": "qux"})]

    def test_run_idle_no_idlers(self):
        loop = self._make_one()
        assert loop.run_idle() is False

    def test_run_idle_all_inactive(self):
        loop = self._make_one()
        loop.add_idle("foo")
        loop.inactive = 1
        assert loop.run_idle() is False

    def test_run_idle_remove_callback(self):
        callback = mock.Mock(__name__="callback")
        callback.return_value = None
        loop = self._make_one()
        loop.add_idle(callback, "foo", bar="baz")
        loop.add_idle("foo")
        assert loop.run_idle() is True
        callback.assert_called_once_with("foo", bar="baz")
        assert len(loop.idlers) == 1
        assert loop.inactive == 0

    def test_run_idle_did_work(self):
        callback = mock.Mock(__name__="callback")
        callback.return_value = True
        loop = self._make_one()
        loop.add_idle(callback, "foo", bar="baz")
        loop.add_idle("foo")
        loop.inactive = 1
        assert loop.run_idle() is True
        callback.assert_called_once_with("foo", bar="baz")
        assert len(loop.idlers) == 2
        assert loop.inactive == 0

    def test_run_idle_did_no_work(self):
        callback = mock.Mock(__name__="callback")
        callback.return_value = False
        loop = self._make_one()
        loop.add_idle(callback, "foo", bar="baz")
        loop.add_idle("foo")
        loop.inactive = 1
        assert loop.run_idle() is True
        callback.assert_called_once_with("foo", bar="baz")
        assert len(loop.idlers) == 2
        assert loop.inactive == 2

    def test_run0_nothing_to_do(self):
        loop = self._make_one()
        assert loop.run0() is None

    def test_run0_current(self):
        callback = mock.Mock(__name__="callback")
        loop = self._make_one()
        loop.call_soon(callback, "foo", bar="baz")
        loop.inactive = 88
        assert loop.run0() == 0
        callback.assert_called_once_with("foo", bar="baz")
        assert len(loop.current) == 0
        assert loop.inactive == 0

    def test_run0_idler(self):
        callback = mock.Mock(__name__="callback")
        loop = self._make_one()
        loop.add_idle(callback, "foo", bar="baz")
        assert loop.run0() == 0
        callback.assert_called_once_with("foo", bar="baz")

    @mock.patch("google.cloud.ndb._eventloop.time")
    def test_run0_next_later(self, time):
        time.time.return_value = 0
        callback = mock.Mock(__name__="callback")
        loop = self._make_one()
        loop.queue_call(5, callback, "foo", bar="baz")
        loop.inactive = 88
        assert loop.run0() == 5
        callback.assert_not_called()
        assert len(loop.queue) == 1
        assert loop.inactive == 88

    @mock.patch("google.cloud.ndb._eventloop.time")
    def test_run0_next_now(self, time):
        time.time.return_value = 0
        callback = mock.Mock(__name__="callback")
        loop = self._make_one()
        loop.queue_call(6, "foo")
        loop.queue_call(5, callback, "foo", bar="baz")
        loop.inactive = 88
        time.time.return_value = 10
        assert loop.run0() == 0
        callback.assert_called_once_with("foo", bar="baz")
        assert len(loop.queue) == 1
        assert loop.inactive == 0

    @pytest.mark.usefixtures("in_context")
    def test_run0_rpc(self):
        rpc = mock.Mock(spec=grpc.Future)
        callback = mock.Mock(spec=())

        loop = self._make_one()
        loop.rpcs["foo"] = callback
        loop.rpc_results.put(("foo", rpc))

        loop.run0()
        assert len(loop.rpcs) == 0
        assert loop.rpc_results.empty()
        callback.assert_called_once_with(rpc)

    def test_run1_nothing_to_do(self):
        loop = self._make_one()
        assert loop.run1() is False

    @mock.patch("google.cloud.ndb._eventloop.time")
    def test_run1_has_work_now(self, time):
        callback = mock.Mock(__name__="callback")
        loop = self._make_one()
        loop.call_soon(callback)
        assert loop.run1() is True
        time.sleep.assert_not_called()
        callback.assert_called_once_with()

    @mock.patch("google.cloud.ndb._eventloop.time")
    def test_run1_has_work_later(self, time):
        time.time.return_value = 0
        callback = mock.Mock(__name__="callback")
        loop = self._make_one()
        loop.queue_call(5, callback)
        assert loop.run1() is True
        time.sleep.assert_called_once_with(5)
        callback.assert_not_called()

    @mock.patch("google.cloud.ndb._eventloop.time")
    def test_run(self, time):
        time.time.return_value = 0

        def mock_sleep(seconds):
            time.time.return_value += seconds

        time.sleep = mock_sleep
        idler = mock.Mock(__name__="idler")
        idler.return_value = None
        runnow = mock.Mock(__name__="runnow")
        runlater = mock.Mock(__name__="runlater")
        loop = self._make_one()
        loop.add_idle(idler)
        loop.call_soon(runnow)
        loop.queue_call(5, runlater)
        loop.run()
        idler.assert_called_once_with()
        runnow.assert_called_once_with()
        runlater.assert_called_once_with()


def test_get_event_loop(context):
    with pytest.raises(exceptions.ContextError):
        _eventloop.get_event_loop()
    with context.use():
        loop = _eventloop.get_event_loop()
        assert isinstance(loop, _eventloop.EventLoop)
        assert _eventloop.get_event_loop() is loop


def test_add_idle(context):
    loop = mock.Mock(spec=("run", "add_idle"))
    with context.new(eventloop=loop).use():
        _eventloop.add_idle("foo", "bar", baz="qux")
        loop.add_idle.assert_called_once_with("foo", "bar", baz="qux")


def test_call_soon(context):
    loop = mock.Mock(spec=("run", "call_soon"))
    with context.new(eventloop=loop).use():
        _eventloop.call_soon("foo", "bar", baz="qux")
        loop.call_soon.assert_called_once_with("foo", "bar", baz="qux")


def test_queue_call(context):
    loop = mock.Mock(spec=("run", "queue_call"))
    with context.new(eventloop=loop).use():
        _eventloop.queue_call(42, "foo", "bar", baz="qux")
        loop.queue_call.assert_called_once_with(42, "foo", "bar", baz="qux")


def test_queue_rpc(context):
    loop = mock.Mock(spec=("run", "queue_rpc"))
    with context.new(eventloop=loop).use():
        _eventloop.queue_rpc("foo", "bar")
        loop.queue_rpc.assert_called_once_with("foo", "bar")


def test_run(context):
    loop = mock.Mock(spec=("run",))
    with context.new(eventloop=loop).use():
        _eventloop.run()
        loop.run.assert_called_once_with()


def test_run1(context):
    loop = mock.Mock(spec=("run", "run1"))
    with context.new(eventloop=loop).use():
        _eventloop.run1()
        loop.run1.assert_called_once_with()
