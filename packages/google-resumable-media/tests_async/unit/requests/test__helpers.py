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
import io

import aiohttp  # type: ignore
import mock
import pytest  # type: ignore

from google._async_resumable_media.requests import _request_helpers as _helpers

# async version takes a single timeout, not a tuple of connect, read timeouts.
EXPECTED_TIMEOUT = aiohttp.ClientTimeout(connect=61, sock_read=60)


class TestRequestsMixin(object):
    def test__get_status_code(self):
        status_code = int(http.client.OK)
        response = _make_response(status_code)
        assert status_code == _helpers.RequestsMixin._get_status_code(response)

    def test__get_headers(self):
        headers = {"fruit": "apple"}
        response = mock.Mock(
            _headers=headers, headers=headers, spec=["_headers", "headers"]
        )
        assert headers == _helpers.RequestsMixin._get_headers(response)

    @pytest.mark.asyncio
    async def test__get_body(self):
        body = b"This is the payload."
        content_stream = mock.AsyncMock(spec=["__call__", "read"])
        content_stream.read = mock.AsyncMock(spec=["__call__"], return_value=body)
        response = mock.AsyncMock(
            content=content_stream,
            spec=["__call__", "content"],
        )
        temp = await _helpers.RequestsMixin._get_body(response)
        assert body == temp


class TestRawRequestsMixin(object):
    class AsyncByteStream:
        def __init__(self, bytes):
            self._byte_stream = io.BytesIO(bytes)

        async def read(self):
            return self._byte_stream.read()

    @pytest.mark.asyncio
    async def test__get_body(self):
        body = b"This is the payload."
        response = mock.Mock(
            content=TestRawRequestsMixin.AsyncByteStream(body), spec=["content"]
        )
        assert body == await _helpers.RawRequestsMixin._get_body(response)


@pytest.mark.asyncio
async def test_http_request():
    transport, response = _make_transport(http.client.OK)
    method = "POST"
    url = "http://test.invalid"
    data = mock.sentinel.data
    headers = {"one": "fish", "blue": "fish"}
    timeout = mock.sentinel.timeout
    ret_val = await _helpers.http_request(
        transport,
        method,
        url,
        data=data,
        headers=headers,
        extra1=b"work",
        extra2=125.5,
        timeout=timeout,
    )

    assert ret_val is response
    transport.request.assert_called_once_with(
        method,
        url,
        data=data,
        headers=headers,
        extra1=b"work",
        extra2=125.5,
        timeout=timeout,
    )


@pytest.mark.asyncio
async def test_http_request_defaults():
    transport, response = _make_transport(http.client.OK)
    method = "POST"
    url = "http://test.invalid"

    ret_val = await _helpers.http_request(transport, method, url)
    assert ret_val is response
    transport.request.assert_called_once_with(
        method, url, data=None, headers=None, timeout=EXPECTED_TIMEOUT
    )


def _make_response(status_code):
    return mock.AsyncMock(status=status_code, spec=["status"])


def _make_transport(status_code):
    response = _make_response(status_code)
    transport = mock.AsyncMock(spec=["request"])
    transport.request = mock.AsyncMock(spec=["__call__"], return_value=response)
    return transport, response
