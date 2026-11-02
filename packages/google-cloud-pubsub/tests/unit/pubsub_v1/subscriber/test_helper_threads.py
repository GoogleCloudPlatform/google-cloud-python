# Copyright 2017, Google LLC All rights reserved.
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

import queue
from unittest import mock

from google.cloud.pubsub_v1.subscriber._protocol import helper_threads


def test_queue_callback_worker():
    queue_ = queue.Queue()
    callback = mock.Mock(spec=())
    qct = helper_threads.QueueCallbackWorker(queue_, callback)

    # Set up an appropriate mock for the queue, and call the queue callback
    # thread.
    with mock.patch.object(queue.Queue, "get") as get:
        get.side_effect = (mock.sentinel.A, helper_threads.STOP, queue.Empty())
        qct()

        # Assert that we got the expected calls.
        assert get.call_count == 3
        callback.assert_called_once_with([mock.sentinel.A])


def test_queue_callback_worker_stop_with_extra_items():
    queue_ = queue.Queue()
    callback = mock.Mock(spec=())
    qct = helper_threads.QueueCallbackWorker(queue_, callback)

    # Set up an appropriate mock for the queue, and call the queue callback
    # thread.
    with mock.patch.object(queue.Queue, "get") as get:
        get.side_effect = (
            mock.sentinel.A,
            helper_threads.STOP,
            mock.sentinel.B,
            queue.Empty(),
        )
        qct()

        # Assert that we got the expected calls.
        assert get.call_count == 4
        callback.assert_called_once_with([mock.sentinel.A])


def test_queue_callback_worker_get_many():
    queue_ = queue.Queue()
    callback = mock.Mock(spec=())
    qct = helper_threads.QueueCallbackWorker(queue_, callback)

    # Set up an appropriate mock for the queue, and call the queue callback
    # thread.
    with mock.patch.object(queue.Queue, "get") as get:
        get.side_effect = (
            mock.sentinel.A,
            queue.Empty(),
            mock.sentinel.B,
            helper_threads.STOP,
            queue.Empty(),
        )
        qct()

        # Assert that we got the expected calls.
        assert get.call_count == 5
        callback.assert_has_calls(
            [mock.call([(mock.sentinel.A)]), mock.call([(mock.sentinel.B)])]
        )


def test_queue_callback_worker_max_items():
    queue_ = queue.Queue()
    callback = mock.Mock(spec=())
    qct = helper_threads.QueueCallbackWorker(queue_, callback, max_items=1)

    # Set up an appropriate mock for the queue, and call the queue callback
    # thread.
    with mock.patch.object(queue.Queue, "get") as get:
        get.side_effect = (
            mock.sentinel.A,
            mock.sentinel.B,
            helper_threads.STOP,
            queue.Empty(),
        )
        qct()

        # Assert that we got the expected calls.
        assert get.call_count == 3
        callback.assert_has_calls(
            [mock.call([(mock.sentinel.A)]), mock.call([(mock.sentinel.B)])]
        )


def test_queue_callback_worker_exception():
    queue_ = queue.Queue()
    callback = mock.Mock(spec=(), side_effect=(Exception,))
    qct = helper_threads.QueueCallbackWorker(queue_, callback)

    # Set up an appropriate mock for the queue, and call the queue callback
    # thread.
    with mock.patch.object(queue.Queue, "get") as get:
        get.side_effect = (mock.sentinel.A, helper_threads.STOP, queue.Empty())
        qct()

        # Assert that we got the expected calls.
        assert get.call_count == 3
        callback.assert_called_once_with([mock.sentinel.A])
