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

import pytest

from google.cloud.ndb import _batch, _eventloop


@pytest.mark.usefixtures("in_context")
class Test_get_batch:
    def test_it(self):
        options = {"foo": "bar"}
        batch = _batch.get_batch(MockBatch, options)
        assert batch.options is options
        assert not batch.idle_called

        different_options = {"food": "barn"}
        assert _batch.get_batch(MockBatch, different_options) is not batch

        assert _batch.get_batch(MockBatch) is not batch

        assert _batch.get_batch(MockBatch, options) is batch

        batch._full = True
        batch2 = _batch.get_batch(MockBatch, options)
        assert batch2 is not batch
        assert not batch2.idle_called

        _eventloop.run()
        assert batch.idle_called
        assert batch2.idle_called


class MockBatch:
    _full = False

    def __init__(self, options):
        self.options = options
        self.idle_called = False

    def idle_callback(self):
        self.idle_called = True

    def full(self):
        return self._full
