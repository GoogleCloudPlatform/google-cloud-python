# Copyright 2019, Google LLC All rights reserved.
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

import pytest

from google.cloud.pubsub_v1.publisher import futures


class TestFuture(object):
    def test_cancel(self):
        future = futures.Future()
        assert future.cancel() is False

    def test_cancelled(self):
        future = futures.Future()
        assert future.cancelled() is False

    def test_result_on_success(self):
        future = futures.Future()
        future.set_result("570307942214048")
        assert future.result() == "570307942214048"

    def test_result_on_failure(self):
        future = futures.Future()
        future.set_exception(RuntimeError("Something bad happened."))
        with pytest.raises(RuntimeError):
            future.result()
