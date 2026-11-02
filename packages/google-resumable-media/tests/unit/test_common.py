# Copyright 2017 Google Inc.
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

from unittest import mock

import pytest  # type: ignore

from google.resumable_media import common


class TestInvalidResponse(object):
    def test_constructor(self):
        response = mock.sentinel.response
        error = common.InvalidResponse(response, 1, "a", [b"m"], True)

        assert error.response is response
        assert error.args == (1, "a", [b"m"], True)


class TestRetryStrategy(object):
    def test_constructor_defaults(self):
        retry_strategy = common.RetryStrategy()
        assert retry_strategy.max_sleep == common.MAX_SLEEP
        assert retry_strategy.max_cumulative_retry == common.MAX_CUMULATIVE_RETRY
        assert retry_strategy.max_retries is None

    def test_constructor_failure(self):
        with pytest.raises(ValueError) as exc_info:
            common.RetryStrategy(max_cumulative_retry=600.0, max_retries=12)

        exc_info.match(common._SLEEP_RETRY_ERROR_MSG)

    def test_constructor_custom_delay_and_multiplier(self):
        retry_strategy = common.RetryStrategy(initial_delay=3.0, multiplier=4)
        assert retry_strategy.max_sleep == common.MAX_SLEEP
        assert retry_strategy.max_cumulative_retry == common.MAX_CUMULATIVE_RETRY
        assert retry_strategy.max_retries is None
        assert retry_strategy.initial_delay == 3.0
        assert retry_strategy.multiplier == 4

    def test_constructor_explicit_bound_cumulative(self):
        max_sleep = 10.0
        max_cumulative_retry = 100.0
        retry_strategy = common.RetryStrategy(
            max_sleep=max_sleep, max_cumulative_retry=max_cumulative_retry
        )

        assert retry_strategy.max_sleep == max_sleep
        assert retry_strategy.max_cumulative_retry == max_cumulative_retry
        assert retry_strategy.max_retries is None

    def test_constructor_explicit_bound_retries(self):
        max_sleep = 13.75
        max_retries = 14
        retry_strategy = common.RetryStrategy(
            max_sleep=max_sleep, max_retries=max_retries
        )

        assert retry_strategy.max_sleep == max_sleep
        assert retry_strategy.max_cumulative_retry is None
        assert retry_strategy.max_retries == max_retries

    def test_retry_allowed_bound_cumulative(self):
        retry_strategy = common.RetryStrategy(max_cumulative_retry=100.0)
        assert retry_strategy.retry_allowed(50.0, 10)
        assert retry_strategy.retry_allowed(99.0, 7)
        assert retry_strategy.retry_allowed(100.0, 4)
        assert not retry_strategy.retry_allowed(101.0, 11)
        assert not retry_strategy.retry_allowed(200.0, 6)

    def test_retry_allowed_bound_retries(self):
        retry_strategy = common.RetryStrategy(max_retries=6)
        assert retry_strategy.retry_allowed(1000.0, 5)
        assert retry_strategy.retry_allowed(99.0, 6)
        assert not retry_strategy.retry_allowed(625.5, 7)
