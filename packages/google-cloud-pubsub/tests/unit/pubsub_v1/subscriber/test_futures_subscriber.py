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

from __future__ import absolute_import

from unittest import mock

import pytest

from google.cloud.pubsub_v1.subscriber import futures
from google.cloud.pubsub_v1.subscriber._protocol import streaming_pull_manager
from google.cloud.pubsub_v1.subscriber.exceptions import (
    AcknowledgeError,
    AcknowledgeStatus,
)


class TestStreamingPullFuture(object):
    def make_future(self):
        manager = mock.create_autospec(
            streaming_pull_manager.StreamingPullManager, instance=True
        )
        future = futures.StreamingPullFuture(manager)
        return future

    def test_default_state(self):
        future = self.make_future()
        manager = future._StreamingPullFuture__manager

        assert future.running()
        assert not future.done()
        assert not future.cancelled()
        manager.add_close_callback.assert_called_once_with(future._on_close_callback)

    def test__on_close_callback_success(self):
        future = self.make_future()

        future._on_close_callback(mock.sentinel.manager, None)

        assert future.result() is True
        assert not future.running()

    def test__on_close_callback_failure(self):
        future = self.make_future()

        future._on_close_callback(mock.sentinel.manager, ValueError("meep"))

        with pytest.raises(ValueError):
            future.result()

        assert not future.running()

    def test__on_close_callback_future_already_done(self):
        future = self.make_future()

        future.set_result("foo")
        assert future.done()

        # invoking on close callback should not result in an error
        future._on_close_callback(mock.sentinel.manager, "bar")

        result = future.result()
        assert result == "foo"  # on close callback was a no-op

    def test_cancel(self):
        future = self.make_future()
        manager = future._StreamingPullFuture__manager

        future.cancel()

        manager.close.assert_called_once()
        assert future.cancelled()


class TestFuture(object):
    def test_cancel(self):
        future = futures.Future()
        assert future.cancel() is False

    def test_cancelled(self):
        future = futures.Future()
        assert future.cancelled() is False

    def test_result_on_success(self):
        future = futures.Future()
        future.set_result(AcknowledgeStatus.SUCCESS)
        assert future.result() == AcknowledgeStatus.SUCCESS

    def test_result_on_failure(self):
        future = futures.Future()
        future.set_exception(
            AcknowledgeError(
                AcknowledgeStatus.PERMISSION_DENIED, "Something bad happened."
            )
        )
        with pytest.raises(AcknowledgeError) as e:
            future.result()
        assert e.value.error_code == AcknowledgeStatus.PERMISSION_DENIED
        assert e.value.info == "Something bad happened."
