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
from unittest import mock

import pytest  # type: ignore
import requests.exceptions
import urllib3.exceptions  # type: ignore

from google.resumable_media import common
from google.resumable_media.requests import _request_helpers

EXPECTED_TIMEOUT = (61, 60)


class TestRequestsMixin(object):
    def test__get_status_code(self):
        status_code = int(http.client.OK)
        response = _make_response(status_code)
        assert status_code == _request_helpers.RequestsMixin._get_status_code(response)

    def test__get_headers(self):
        headers = {"fruit": "apple"}
        response = mock.Mock(headers=headers, spec=["headers"])
        assert headers == _request_helpers.RequestsMixin._get_headers(response)

    def test__get_body(self):
        body = b"This is the payload."
        response = mock.Mock(content=body, spec=["content"])
        assert body == _request_helpers.RequestsMixin._get_body(response)


class TestRawRequestsMixin(object):
    def test__get_body_wo_content_consumed(self):
        body = b"This is the payload."
        raw = mock.Mock(spec=["stream"])
        raw.stream.return_value = iter([body])
        response = mock.Mock(raw=raw, _content=False, spec=["raw", "_content"])
        assert body == _request_helpers.RawRequestsMixin._get_body(response)
        raw.stream.assert_called_once_with(
            _request_helpers._SINGLE_GET_CHUNK_SIZE, decode_content=False
        )

    def test__get_body_w_content_consumed(self):
        body = b"This is the payload."
        response = mock.Mock(_content=body, spec=["_content"])
        assert body == _request_helpers.RawRequestsMixin._get_body(response)


def _make_response(status_code):
    return mock.Mock(status_code=status_code, spec=["status_code"])


def _get_status_code(response):
    return response.status_code


class Test_wait_and_retry(object):
    def test_success_no_retry(self):
        truthy = http.client.OK
        assert truthy not in common.RETRYABLE
        response = _make_response(truthy)

        func = mock.Mock(return_value=response, spec=[])
        retry_strategy = common.RetryStrategy()
        ret_val = _request_helpers.wait_and_retry(
            func, _get_status_code, retry_strategy
        )

        assert ret_val is response
        func.assert_called_once_with()

    @mock.patch("time.sleep")
    @mock.patch("random.randint")
    def test_success_with_retry(self, randint_mock, sleep_mock):
        randint_mock.side_effect = [125, 625, 375]

        status_codes = (
            http.client.INTERNAL_SERVER_ERROR,
            http.client.BAD_GATEWAY,
            http.client.SERVICE_UNAVAILABLE,
            http.client.NOT_FOUND,
        )
        responses = [_make_response(status_code) for status_code in status_codes]

        def raise_response():
            raise common.InvalidResponse(responses.pop(0))

        func = mock.Mock(side_effect=raise_response)

        retry_strategy = common.RetryStrategy()
        try:
            _request_helpers.wait_and_retry(func, _get_status_code, retry_strategy)
        except common.InvalidResponse as e:
            ret_val = e.response

        assert ret_val.status_code == status_codes[-1]
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
    def test_success_with_retry_custom_delay(self, randint_mock, sleep_mock):
        randint_mock.side_effect = [125, 625, 375]

        status_codes = (
            http.client.INTERNAL_SERVER_ERROR,
            http.client.BAD_GATEWAY,
            http.client.SERVICE_UNAVAILABLE,
            http.client.NOT_FOUND,
        )
        responses = [_make_response(status_code) for status_code in status_codes]

        def raise_response():
            raise common.InvalidResponse(responses.pop(0))

        func = mock.Mock(side_effect=raise_response)

        retry_strategy = common.RetryStrategy(initial_delay=3.0, multiplier=4)
        try:
            _request_helpers.wait_and_retry(func, _get_status_code, retry_strategy)
        except common.InvalidResponse as e:
            ret_val = e.response

        assert ret_val.status_code == status_codes[-1]
        assert status_codes[-1] not in common.RETRYABLE

        assert func.call_count == 4
        assert func.mock_calls == [mock.call()] * 4

        assert randint_mock.call_count == 3
        assert randint_mock.mock_calls == [mock.call(0, 1000)] * 3

        assert sleep_mock.call_count == 3
        sleep_mock.assert_any_call(3.125)  # initial delay 3 + jitter 0.125
        sleep_mock.assert_any_call(
            12.625
        )  # previous delay 3 * multiplier 4 + jitter 0.625
        sleep_mock.assert_any_call(
            48.375
        )  # previous delay 12 * multiplier 4 + jitter 0.375

    @mock.patch("time.sleep")
    @mock.patch("random.randint")
    def test_retry_success_http_standard_lib_connection_errors(
        self, randint_mock, sleep_mock
    ):
        randint_mock.side_effect = [125, 625, 500, 875, 375]

        status_code = int(http.client.OK)
        response = _make_response(status_code)
        responses = [
            http.client.BadStatusLine(""),
            http.client.IncompleteRead(""),
            http.client.ResponseNotReady,
            ConnectionError,
            response,
        ]
        func = mock.Mock(side_effect=responses, spec=[])

        retry_strategy = common.RetryStrategy()
        ret_val = _request_helpers.wait_and_retry(
            func, _get_status_code, retry_strategy
        )

        assert ret_val == responses[-1]
        assert func.call_count == 5
        assert func.mock_calls == [mock.call()] * 5
        assert randint_mock.call_count == 4
        assert randint_mock.mock_calls == [mock.call(0, 1000)] * 4
        assert sleep_mock.call_count == 4
        sleep_mock.assert_any_call(1.125)
        sleep_mock.assert_any_call(2.625)
        sleep_mock.assert_any_call(4.500)
        sleep_mock.assert_any_call(8.875)

    @mock.patch("time.sleep")
    @mock.patch("random.randint")
    def test_retry_success_requests_lib_connection_errors(
        self, randint_mock, sleep_mock
    ):
        randint_mock.side_effect = [125, 625, 500, 875]

        status_code = int(http.client.OK)
        response = _make_response(status_code)
        responses = [
            requests.exceptions.ConnectionError,
            requests.exceptions.ChunkedEncodingError,
            requests.exceptions.Timeout,
            response,
        ]
        func = mock.Mock(side_effect=responses, spec=[])

        retry_strategy = common.RetryStrategy()
        ret_val = _request_helpers.wait_and_retry(
            func, _get_status_code, retry_strategy
        )

        assert ret_val == responses[-1]
        assert func.call_count == 4
        assert func.mock_calls == [mock.call()] * 4
        assert randint_mock.call_count == 3
        assert randint_mock.mock_calls == [mock.call(0, 1000)] * 3
        assert sleep_mock.call_count == 3
        sleep_mock.assert_any_call(1.125)
        sleep_mock.assert_any_call(2.625)
        sleep_mock.assert_any_call(4.500)

    @mock.patch("time.sleep")
    @mock.patch("random.randint")
    def test_retry_success_urllib3_connection_errors(self, randint_mock, sleep_mock):
        randint_mock.side_effect = [125, 625, 500, 875, 375]

        status_code = int(http.client.OK)
        response = _make_response(status_code)
        responses = [
            urllib3.exceptions.PoolError(None, ""),
            urllib3.exceptions.ProtocolError,
            urllib3.exceptions.SSLError,
            urllib3.exceptions.TimeoutError,
            response,
        ]
        func = mock.Mock(side_effect=responses, spec=[])

        retry_strategy = common.RetryStrategy()
        ret_val = _request_helpers.wait_and_retry(
            func, _get_status_code, retry_strategy
        )

        assert ret_val == responses[-1]
        assert func.call_count == 5
        assert func.mock_calls == [mock.call()] * 5
        assert randint_mock.call_count == 4
        assert randint_mock.mock_calls == [mock.call(0, 1000)] * 4
        assert sleep_mock.call_count == 4
        sleep_mock.assert_any_call(1.125)
        sleep_mock.assert_any_call(2.625)
        sleep_mock.assert_any_call(4.500)
        sleep_mock.assert_any_call(8.875)

    @mock.patch("time.sleep")
    @mock.patch("random.randint")
    def test_retry_exceeds_max_cumulative(self, randint_mock, sleep_mock):
        randint_mock.side_effect = [875, 0, 375, 500, 500, 250, 125]

        status_codes = (
            http.client.SERVICE_UNAVAILABLE,
            http.client.GATEWAY_TIMEOUT,
            common.TOO_MANY_REQUESTS,
            http.client.INTERNAL_SERVER_ERROR,
            http.client.SERVICE_UNAVAILABLE,
            http.client.BAD_GATEWAY,
            common.TOO_MANY_REQUESTS,
        )
        responses = [_make_response(status_code) for status_code in status_codes]

        def raise_response():
            raise common.InvalidResponse(responses.pop(0))

        func = mock.Mock(side_effect=raise_response)

        retry_strategy = common.RetryStrategy(max_cumulative_retry=100.0)
        try:
            _request_helpers.wait_and_retry(func, _get_status_code, retry_strategy)
        except common.InvalidResponse as e:
            ret_val = e.response

        assert ret_val.status_code == status_codes[-1]
        assert status_codes[-1] in common.RETRYABLE

        assert func.call_count == 7
        assert func.mock_calls == [mock.call()] * 7

        assert randint_mock.call_count == 7
        assert randint_mock.mock_calls == [mock.call(0, 1000)] * 7

        assert sleep_mock.call_count == 6
        sleep_mock.assert_any_call(1.875)
        sleep_mock.assert_any_call(2.0)
        sleep_mock.assert_any_call(4.375)
        sleep_mock.assert_any_call(8.5)
        sleep_mock.assert_any_call(16.5)
        sleep_mock.assert_any_call(32.25)

    @mock.patch("time.sleep")
    @mock.patch("random.randint")
    def test_retry_exceeds_max_retries(self, randint_mock, sleep_mock):
        randint_mock.side_effect = [875, 0, 375, 500, 500, 250, 125]

        status_codes = (
            http.client.SERVICE_UNAVAILABLE,
            http.client.GATEWAY_TIMEOUT,
            common.TOO_MANY_REQUESTS,
            http.client.INTERNAL_SERVER_ERROR,
            http.client.SERVICE_UNAVAILABLE,
            http.client.BAD_GATEWAY,
            common.TOO_MANY_REQUESTS,
        )
        responses = [_make_response(status_code) for status_code in status_codes]

        def raise_response():
            raise common.InvalidResponse(responses.pop(0))

        func = mock.Mock(side_effect=raise_response)

        retry_strategy = common.RetryStrategy(max_retries=6)
        try:
            _request_helpers.wait_and_retry(func, _get_status_code, retry_strategy)
        except common.InvalidResponse as e:
            ret_val = e.response

        assert ret_val.status_code == status_codes[-1]
        assert status_codes[-1] in common.RETRYABLE

        assert func.call_count == 7
        assert func.mock_calls == [mock.call()] * 7

        assert randint_mock.call_count == 7
        assert randint_mock.mock_calls == [mock.call(0, 1000)] * 7

        assert sleep_mock.call_count == 6
        sleep_mock.assert_any_call(1.875)
        sleep_mock.assert_any_call(2.0)
        sleep_mock.assert_any_call(4.375)
        sleep_mock.assert_any_call(8.5)
        sleep_mock.assert_any_call(16.5)
        sleep_mock.assert_any_call(32.25)

    @mock.patch("time.sleep")
    @mock.patch("random.randint")
    def test_retry_zero_max_retries(self, randint_mock, sleep_mock):
        randint_mock.side_effect = [875, 0, 375]

        status_codes = (
            http.client.SERVICE_UNAVAILABLE,
            http.client.GATEWAY_TIMEOUT,
            common.TOO_MANY_REQUESTS,
        )
        responses = [_make_response(status_code) for status_code in status_codes]

        def raise_response():
            raise common.InvalidResponse(responses.pop(0))

        func = mock.Mock(side_effect=raise_response)

        retry_strategy = common.RetryStrategy(max_retries=0)
        try:
            _request_helpers.wait_and_retry(func, _get_status_code, retry_strategy)
        except common.InvalidResponse as e:
            ret_val = e.response

        assert func.call_count == 1
        assert func.mock_calls == [mock.call()] * 1
        assert ret_val.status_code == status_codes[0]

        assert randint_mock.call_count == 1
        assert sleep_mock.call_count == 0

    @mock.patch("time.sleep")
    @mock.patch("random.randint")
    def test_retry_exceeded_reraises_connection_error(self, randint_mock, sleep_mock):
        randint_mock.side_effect = [875, 0, 375, 500, 500, 250, 125]

        responses = [requests.exceptions.ConnectionError] * 7
        func = mock.Mock(side_effect=responses, spec=[])

        retry_strategy = common.RetryStrategy(max_cumulative_retry=100.0)
        with pytest.raises(requests.exceptions.ConnectionError):
            _request_helpers.wait_and_retry(func, _get_status_code, retry_strategy)

        assert func.call_count == 7
        assert func.mock_calls == [mock.call()] * 7

        assert randint_mock.call_count == 7
        assert randint_mock.mock_calls == [mock.call(0, 1000)] * 7

        assert sleep_mock.call_count == 6
        sleep_mock.assert_any_call(1.875)
        sleep_mock.assert_any_call(2.0)
        sleep_mock.assert_any_call(4.375)
        sleep_mock.assert_any_call(8.5)
        sleep_mock.assert_any_call(16.5)
        sleep_mock.assert_any_call(32.25)
