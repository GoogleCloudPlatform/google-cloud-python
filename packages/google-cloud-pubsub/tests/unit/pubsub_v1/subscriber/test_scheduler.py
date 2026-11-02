# Copyright 2018, Google LLC
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

import concurrent.futures
import queue
import threading
import time
from unittest import mock

import pytest

from google.cloud.pubsub_v1.subscriber import scheduler


def test_subclasses_base_abc():
    assert issubclass(scheduler.ThreadScheduler, scheduler.Scheduler)


def test_constructor_defaults():
    scheduler_ = scheduler.ThreadScheduler()

    assert isinstance(scheduler_.queue, queue.Queue)
    assert isinstance(scheduler_._executor, concurrent.futures.Executor)


def test_constructor_options():
    scheduler_ = scheduler.ThreadScheduler(executor=mock.sentinel.executor)

    assert scheduler_._executor == mock.sentinel.executor


def test_schedule_executes_submitted_items():
    called_with = []
    callback_done_twice = threading.Barrier(3)  # 3 == 2x callback + 1x main thread

    def callback(*args, **kwargs):
        called_with.append((args, kwargs))  # appends are thread-safe
        callback_done_twice.wait()

    scheduler_ = scheduler.ThreadScheduler()

    scheduler_.schedule(callback, "arg1", kwarg1="meep")
    scheduler_.schedule(callback, "arg2", kwarg2="boop")

    callback_done_twice.wait(timeout=3.0)
    result = scheduler_.shutdown()

    assert result == []  # no scheduled items dropped

    expected_calls = [(("arg1",), {"kwarg1": "meep"}), (("arg2",), {"kwarg2": "boop"})]
    assert sorted(called_with) == expected_calls


def test_schedule_after_executor_shutdown_warning():
    def callback(*args, **kwargs):
        pass

    scheduler_ = scheduler.ThreadScheduler()

    scheduler_.schedule(callback, "arg1", kwarg1="meep")
    scheduler_._executor.shutdown()

    with pytest.warns(
        RuntimeWarning, match="Scheduling a callback after executor shutdown"
    ) as warned:
        scheduler_.schedule(callback, "arg2", kwarg2="boop")

    assert len(warned) == 1
    assert issubclass(warned[0].category, RuntimeWarning)
    warning_msg = str(warned[0].message)
    assert "after executor shutdown" in warning_msg


def test_shutdown_nonblocking_by_default():
    called_with = []
    at_least_one_called = threading.Event()
    at_least_one_completed = threading.Event()

    def callback(message):
        called_with.append(message)  # appends are thread-safe
        at_least_one_called.set()
        time.sleep(1.0)
        at_least_one_completed.set()

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    scheduler_ = scheduler.ThreadScheduler(executor=executor)

    scheduler_.schedule(callback, "message_1")
    scheduler_.schedule(callback, "message_2")

    at_least_one_called.wait()
    dropped = scheduler_.shutdown()

    assert len(called_with) == 1
    assert called_with[0] in {"message_1", "message_2"}

    assert len(dropped) == 1
    assert dropped[0] in {"message_1", "message_2"}
    assert dropped[0] != called_with[0]  # the dropped message was not the processed one

    err_msg = (
        "Shutdown should not have waited for the already running callbacks to complete."
    )
    assert not at_least_one_completed.is_set(), err_msg


def test_shutdown_blocking_awaits_running_callbacks():
    called_with = []
    at_least_one_called = threading.Event()
    at_least_one_completed = threading.Event()

    def callback(message):
        called_with.append(message)  # appends are thread-safe
        at_least_one_called.set()
        time.sleep(1.0)
        at_least_one_completed.set()

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    scheduler_ = scheduler.ThreadScheduler(executor=executor)

    scheduler_.schedule(callback, "message_1")
    scheduler_.schedule(callback, "message_2")

    at_least_one_called.wait()
    dropped = scheduler_.shutdown(await_msg_callbacks=True)

    assert len(called_with) == 1
    assert called_with[0] in {"message_1", "message_2"}

    # The work items that have not been started yet should still be dropped.
    assert len(dropped) == 1
    assert dropped[0] in {"message_1", "message_2"}
    assert dropped[0] != called_with[0]  # the dropped message was not the processed one

    err_msg = "Shutdown did not wait for the already running callbacks to complete."
    assert at_least_one_completed.is_set(), err_msg


def test_shutdown_handles_executor_queue_sentinels():
    at_least_one_called = threading.Event()

    def callback(_):
        at_least_one_called.set()
        time.sleep(1.0)

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    scheduler_ = scheduler.ThreadScheduler(executor=executor)

    scheduler_.schedule(callback, "message_1")
    scheduler_.schedule(callback, "message_2")
    scheduler_.schedule(callback, "message_3")

    # Simulate executor shutdown from another thread.
    executor._work_queue.put(None)
    executor._work_queue.put(None)

    at_least_one_called.wait()
    dropped = scheduler_.shutdown(await_msg_callbacks=True)

    assert len(set(dropped)) == 2  # Also test for item uniqueness.
    for msg in dropped:
        assert msg is not None
        assert msg.startswith("message_")
