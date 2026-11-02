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

import http.client

import mock
import pytest  # type: ignore

from google._async_resumable_media import _helpers
from google.resumable_media import common


def test_do_nothing():
    ret_val = _helpers.do_nothing()
    assert ret_val is None


class Test_header_required(object):
    def _success_helper(self, **kwargs):
        name = "some-header"
        value = "The Right Hand Side"
        headers = {name: value, "other-name": "other-value"}
        response = mock.Mock(
            _headers=headers, headers=headers, spec=["_headers", "headers"]
        )
        result = _helpers.header_required(response, name, _get_headers, **kwargs)
        assert result == value

    def test_success(self):
        self._success_helper()

    def test_success_with_callback(self):
        callback = mock.Mock(spec=[])
        self._success_helper(callback=callback)
        callback.assert_not_called()

    def _failure_helper(self, **kwargs):
        response = mock.Mock(_headers={}, headers={}, spec=["_headers", "headers"])
        name = "any-name"
        with pytest.raises(common.InvalidResponse) as exc_info:
            _helpers.header_required(response, name, _get_headers, **kwargs)

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 2
        assert error.args[1] == name

    def test_failure(self):
        self._failure_helper()

    def test_failure_with_callback(self):
        callback = mock.Mock(spec=[])
        self._failure_helper(callback=callback)
        callback.assert_called_once_with()


class Test_require_status_code(object):
    @staticmethod
    def _get_status_code(response):
        return response.status_code

    def test_success(self):
        status_codes = (http.client.OK, http.client.CREATED)
        acceptable = (
            http.client.OK,
            int(http.client.OK),
            http.client.CREATED,
            int(http.client.CREATED),
        )
        for value in acceptable:
            response = _make_response(value)
            status_code = _helpers.require_status_code(
                response, status_codes, self._get_status_code
            )
            assert value == status_code

    def test_success_with_callback(self):
        status_codes = (http.client.OK,)
        response = _make_response(http.client.OK)
        callback = mock.Mock(spec=[])
        status_code = _helpers.require_status_code(
            response, status_codes, self._get_status_code, callback=callback
        )
        assert status_code == http.client.OK
        callback.assert_not_called()

    def test_failure(self):
        status_codes = (http.client.CREATED, http.client.NO_CONTENT)
        response = _make_response(http.client.OK)
        with pytest.raises(common.InvalidResponse) as exc_info:
            _helpers.require_status_code(response, status_codes, self._get_status_code)

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 5
        assert error.args[1] == response.status_code
        assert error.args[3:] == status_codes

    def test_failure_with_callback(self):
        status_codes = (http.client.OK,)
        response = _make_response(http.client.NOT_FOUND)
        callback = mock.Mock(spec=[])
        with pytest.raises(common.InvalidResponse) as exc_info:
            _helpers.require_status_code(
                response, status_codes, self._get_status_code, callback=callback
            )

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 4
        assert error.args[1] == response.status_code
        assert error.args[3:] == status_codes
        callback.assert_called_once_with()


class Test_calculate_retry_wait(object):
    @mock.patch("random.randint", return_value=125)
    def test_past_limit(self, randint_mock):
        base_wait, wait_time = _helpers.calculate_retry_wait(70.0, 64.0)

        assert base_wait == 64.0
        assert wait_time == 64.125
        randint_mock.assert_called_once_with(0, 1000)

    @mock.patch("random.randint", return_value=250)
    def test_at_limit(self, randint_mock):
        base_wait, wait_time = _helpers.calculate_retry_wait(50.0, 50.0)

        assert base_wait == 50.0
        assert wait_time == 50.25
        randint_mock.assert_called_once_with(0, 1000)

    @mock.patch("random.randint", return_value=875)
    def test_under_limit(self, randint_mock):
        base_wait, wait_time = _helpers.calculate_retry_wait(16.0, 33.0)

        assert base_wait == 32.0
        assert wait_time == 32.875
        randint_mock.assert_called_once_with(0, 1000)


class Test_wait_and_retry(object):
    @pytest.mark.asyncio
    async def test_success_no_retry(self):
        truthy = http.client.OK
        assert truthy not in common.RETRYABLE
        response = _make_response(truthy)

        func = mock.AsyncMock(return_value=response, spec=[])
        retry_strategy = common.RetryStrategy()
        ret_val = await _helpers.wait_and_retry(func, _get_status_code, retry_strategy)

        assert ret_val is response
        func.assert_called_once_with()

    @mock.patch("time.sleep")
    @mock.patch("random.randint")
    @pytest.mark.asyncio
    async def test_success_with_retry(self, randint_mock, sleep_mock):
        randint_mock.side_effect = [125, 625, 375]

        status_codes = (
            http.client.INTERNAL_SERVER_ERROR,
            http.client.BAD_GATEWAY,
            http.client.SERVICE_UNAVAILABLE,
            http.client.NOT_FOUND,
        )
        responses = [_make_response(status_code) for status_code in status_codes]
        func = mock.AsyncMock(side_effect=responses, spec=[])

        retry_strategy = common.RetryStrategy()
        ret_val = await _helpers.wait_and_retry(func, _get_status_code, retry_strategy)

        assert ret_val == responses[-1]
        assert status_codes[-1] not in common.RETRYABLE

        assert func.call_count == 4
        assert func.mock_calls == [mock.call()] * 4

        assert randint_mock.call_count == 3
        assert randint_mock.mock_calls == [mock.call(0, 1000)] * 3

        assert sleep_mock.call_count == 3
        sleep_mock.assert_any_call(1.125)
        sleep_mock.assert_any_call(2.625)
        sleep_mock.assert_any_call(4.375)

    @mock.patch("time.sleep")
    @mock.patch("random.randint")
    @pytest.mark.asyncio
    async def test_success_with_retry_connection_error(self, randint_mock, sleep_mock):
        randint_mock.side_effect = [125, 625, 375]

        response = _make_response(http.client.NOT_FOUND)
        responses = [ConnectionError, ConnectionError, ConnectionError, response]
        func = mock.AsyncMock(side_effect=responses, spec=[])

        retry_strategy = common.RetryStrategy()
        ret_val = await _helpers.wait_and_retry(func, _get_status_code, retry_strategy)

        assert ret_val == responses[-1]

        assert func.call_count == 4
        assert func.mock_calls == [mock.call()] * 4

        assert randint_mock.call_count == 3
        assert randint_mock.mock_calls == [mock.call(0, 1000)] * 3

        assert sleep_mock.call_count == 3
        sleep_mock.assert_any_call(1.125)
        sleep_mock.assert_any_call(2.625)
        sleep_mock.assert_any_call(4.375)

    @mock.patch("time.sleep")
    @mock.patch("random.randint")
    @pytest.mark.asyncio
    async def test_retry_exceeded_reraises_connection_error(
        self, randint_mock, sleep_mock
    ):
        randint_mock.side_effect = [875, 0, 375, 500, 500, 250, 125]

        responses = [ConnectionError] * 8
        func = mock.AsyncMock(side_effect=responses, spec=[])

        retry_strategy = common.RetryStrategy(max_cumulative_retry=100.0)
        with pytest.raises(ConnectionError):
            await _helpers.wait_and_retry(func, _get_status_code, retry_strategy)

        assert func.call_count == 8
        assert func.mock_calls == [mock.call()] * 8

        assert randint_mock.call_count == 7
        assert randint_mock.mock_calls == [mock.call(0, 1000)] * 7

        assert sleep_mock.call_count == 7
        sleep_mock.assert_any_call(1.875)
        sleep_mock.assert_any_call(2.0)
        sleep_mock.assert_any_call(4.375)
        sleep_mock.assert_any_call(8.5)
        sleep_mock.assert_any_call(16.5)
        sleep_mock.assert_any_call(32.25)
        sleep_mock.assert_any_call(64.125)

    @mock.patch("time.sleep")
    @mock.patch("random.randint")
    @pytest.mark.asyncio
    async def test_retry_exceeds_max_cumulative(self, randint_mock, sleep_mock):
        randint_mock.side_effect = [875, 0, 375, 500, 500, 250, 125]

        status_codes = (
            http.client.SERVICE_UNAVAILABLE,
            http.client.GATEWAY_TIMEOUT,
            http.client.TOO_MANY_REQUESTS,
            http.client.INTERNAL_SERVER_ERROR,
            http.client.SERVICE_UNAVAILABLE,
            http.client.BAD_GATEWAY,
            http.client.GATEWAY_TIMEOUT,
            http.client.TOO_MANY_REQUESTS,
        )
        responses = [_make_response(status_code) for status_code in status_codes]
        func = mock.AsyncMock(side_effect=responses, spec=[])

        retry_strategy = common.RetryStrategy(max_cumulative_retry=100.0)
        ret_val = await _helpers.wait_and_retry(func, _get_status_code, retry_strategy)

        assert ret_val == responses[-1]
        assert status_codes[-1] in common.RETRYABLE

        assert func.call_count == 8
        assert func.mock_calls == [mock.call()] * 8

        assert randint_mock.call_count == 7
        assert randint_mock.mock_calls == [mock.call(0, 1000)] * 7

        assert sleep_mock.call_count == 7
        sleep_mock.assert_any_call(1.875)
        sleep_mock.assert_any_call(2.0)
        sleep_mock.assert_any_call(4.375)
        sleep_mock.assert_any_call(8.5)
        sleep_mock.assert_any_call(16.5)
        sleep_mock.assert_any_call(32.25)
        sleep_mock.assert_any_call(64.125)


def _make_response(status_code):
    return mock.AsyncMock(status_code=status_code, spec=["status_code"])


def _get_status_code(response):
    return response.status_code


def _get_headers(response):
    return response._headers
