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
import json

import aiohttp  # type: ignore
import mock  # type: ignore
import pytest  # type: ignore

import google._async_resumable_media.requests.upload as upload_mod
from tests.unit.requests import test_upload as sync_test

SIMPLE_URL = sync_test.SIMPLE_URL
MULTIPART_URL = sync_test.MULTIPART_URL
RESUMABLE_URL = sync_test.RESUMABLE_URL
ONE_MB = sync_test.ONE_MB
BASIC_CONTENT = sync_test.BASIC_CONTENT
JSON_TYPE = sync_test.JSON_TYPE
JSON_TYPE_LINE = sync_test.JSON_TYPE_LINE
EXPECTED_TIMEOUT = aiohttp.ClientTimeout(
    total=None, connect=61, sock_read=60, sock_connect=None
)


class TestSimpleUpload(object):
    @pytest.mark.asyncio
    async def test_transmit(self):
        data = b"I have got a lovely bunch of coconuts."
        content_type = BASIC_CONTENT
        upload = upload_mod.SimpleUpload(SIMPLE_URL)

        transport = mock.AsyncMock(spec=["request"])
        transport.request = mock.AsyncMock(
            spec=["__call__"], return_value=_make_response()
        )

        assert not upload.finished

        ret_val = await upload.transmit(transport, data, content_type)

        assert ret_val is transport.request.return_value

        upload_headers = {"content-type": content_type}
        transport.request.assert_called_once_with(
            "POST",
            SIMPLE_URL,
            data=data,
            headers=upload_headers,
            timeout=EXPECTED_TIMEOUT,
        )

        assert upload.finished

    @pytest.mark.asyncio
    async def test_transmit_w_custom_timeout(self):
        data = b"I have got a lovely bunch of coconuts."
        content_type = BASIC_CONTENT
        upload = upload_mod.SimpleUpload(SIMPLE_URL)

        transport = mock.AsyncMock(spec=["request"])
        transport.request = mock.AsyncMock(
            spec=["__call__"], return_value=_make_response()
        )

        assert not upload.finished

        ret_val = await upload.transmit(transport, data, content_type, timeout=12.6)

        assert ret_val is transport.request.return_value

        upload_headers = {"content-type": content_type}
        transport.request.assert_called_once_with(
            "POST",
            SIMPLE_URL,
            data=data,
            headers=upload_headers,
            timeout=12.6,
        )

        assert upload.finished


class TestMultipartUpload(object):
    @mock.patch(
        "google._async_resumable_media._upload.get_boundary", return_value=b"==4=="
    )
    @pytest.mark.asyncio
    async def test_transmit(self, mock_get_boundary):
        data = b"Mock data here and there."
        metadata = {"Hey": "You", "Guys": "90909"}
        content_type = BASIC_CONTENT
        upload = upload_mod.MultipartUpload(MULTIPART_URL)

        transport = mock.AsyncMock(spec=["request"])
        transport.request = mock.AsyncMock(
            spec=["__call__"], return_value=_make_response()
        )

        assert not upload.finished

        ret_val = await upload.transmit(transport, data, metadata, content_type)

        assert ret_val is transport.request.return_value

        expected_payload = (
            b"--==4==\r\n"
            + JSON_TYPE_LINE
            + b"\r\n"
            + json.dumps(metadata).encode("utf-8")
            + b"\r\n"
            + b"--==4==\r\n"
            b"content-type: text/plain\r\n"
            b"\r\n"
            b"Mock data here and there.\r\n"
            b"--==4==--"
        )
        multipart_type = b'multipart/related; boundary="==4=="'
        upload_headers = {"content-type": multipart_type}
        transport.request.assert_called_once_with(
            "POST",
            MULTIPART_URL,
            data=expected_payload,
            headers=upload_headers,
            timeout=EXPECTED_TIMEOUT,
        )
        assert upload.finished
        mock_get_boundary.assert_called_once_with()

    @mock.patch(
        "google._async_resumable_media._upload.get_boundary", return_value=b"==4=="
    )
    @pytest.mark.asyncio
    async def test_transmit_w_custom_timeout(self, mock_get_boundary):
        data = b"Mock data here and there."
        metadata = {"Hey": "You", "Guys": "90909"}
        content_type = BASIC_CONTENT
        upload = upload_mod.MultipartUpload(MULTIPART_URL)

        transport = mock.AsyncMock(spec=["request"])
        transport.request = mock.AsyncMock(
            spec=["__call__"], return_value=_make_response()
        )

        await upload.transmit(transport, data, metadata, content_type, timeout=12.6)

        expected_payload = (
            b"--==4==\r\n"
            + JSON_TYPE_LINE
            + b"\r\n"
            + json.dumps(metadata).encode("utf-8")
            + b"\r\n"
            + b"--==4==\r\n"
            b"content-type: text/plain\r\n"
            b"\r\n"
            b"Mock data here and there.\r\n"
            b"--==4==--"
        )
        multipart_type = b'multipart/related; boundary="==4=="'
        upload_headers = {"content-type": multipart_type}

        transport.request.assert_called_once_with(
            "POST",
            MULTIPART_URL,
            data=expected_payload,
            headers=upload_headers,
            timeout=12.6,
        )
        assert upload.finished
        mock_get_boundary.assert_called_once_with()


class TestResumableUpload(object):
    @pytest.mark.asyncio
    async def test_initiate(self):
        upload = upload_mod.ResumableUpload(RESUMABLE_URL, ONE_MB)
        data = b"Knock knock who is there"
        stream = io.BytesIO(data)
        metadata = {"name": "got-jokes.txt"}

        transport = mock.AsyncMock(spec=["request"])
        location = ("http://test.invalid?upload_id=AACODBBBxuw9u3AA",)
        response_headers = {"location": location}
        transport.request = mock.AsyncMock(
            spec=["__call__"], return_value=_make_response(headers=response_headers)
        )

        # Check resumable_url before.
        assert upload._resumable_url is None
        # Make request and check the return value (against the mock).
        total_bytes = 100
        assert total_bytes > len(data)
        response = await upload.initiate(
            transport,
            stream,
            metadata,
            BASIC_CONTENT,
            total_bytes=total_bytes,
            stream_final=False,
        )
        assert response is transport.request.return_value
        # Check resumable_url after.
        assert upload._resumable_url == location
        # Make sure the mock was called as expected.
        json_bytes = b'{"name": "got-jokes.txt"}'
        expected_headers = {
            "content-type": JSON_TYPE,
            "x-upload-content-type": BASIC_CONTENT,
            "x-upload-content-length": "{:d}".format(total_bytes),
        }
        transport.request.assert_called_once_with(
            "POST",
            RESUMABLE_URL,
            data=json_bytes,
            headers=expected_headers,
            timeout=EXPECTED_TIMEOUT,
        )

    @pytest.mark.asyncio
    async def test_initiate_w_custom_timeout(self):
        upload = upload_mod.ResumableUpload(RESUMABLE_URL, ONE_MB)
        data = b"Knock knock who is there"
        stream = io.BytesIO(data)
        metadata = {"name": "got-jokes.txt"}

        transport = mock.AsyncMock(spec=["request"])
        location = ("http://test.invalid?upload_id=AACODBBBxuw9u3AA",)
        response_headers = {"location": location}
        transport.request = mock.AsyncMock(
            spec=["__call__"], return_value=_make_response(headers=response_headers)
        )

        # Check resumable_url before.
        assert upload._resumable_url is None
        # Make request and check the return value (against the mock).
        total_bytes = 100
        assert total_bytes > len(data)
        response = await upload.initiate(
            transport,
            stream,
            metadata,
            BASIC_CONTENT,
            total_bytes=total_bytes,
            stream_final=False,
            timeout=12.6,
        )
        assert response is transport.request.return_value
        # Check resumable_url after.
        assert upload._resumable_url == location
        # Make sure the mock was called as expected.
        json_bytes = b'{"name": "got-jokes.txt"}'
        expected_headers = {
            "content-type": JSON_TYPE,
            "x-upload-content-type": BASIC_CONTENT,
            "x-upload-content-length": "{:d}".format(total_bytes),
        }
        transport.request.assert_called_once_with(
            "POST",
            RESUMABLE_URL,
            data=json_bytes,
            headers=expected_headers,
            timeout=12.6,
        )

    @staticmethod
    def _upload_in_flight(data, headers=None):
        upload = upload_mod.ResumableUpload(RESUMABLE_URL, ONE_MB, headers=headers)
        upload._stream = io.BytesIO(data)
        upload._content_type = BASIC_CONTENT
        upload._total_bytes = len(data)
        upload._resumable_url = "http://test.invalid?upload_id=not-none"
        return upload

    @staticmethod
    def _chunk_mock(status_code, response_headers):
        transport = mock.AsyncMock(spec=["request"])
        put_response = _make_response(status_code=status_code, headers=response_headers)
        transport.request = mock.AsyncMock(spec=["__call__"], return_value=put_response)

        return transport

    @pytest.mark.asyncio
    async def test_transmit_next_chunk(self):
        data = b"This time the data is official."
        upload = self._upload_in_flight(data)
        # Make a fake chunk size smaller than 256 KB.
        chunk_size = 10
        assert chunk_size < len(data)
        upload._chunk_size = chunk_size
        # Make a fake 308 response.
        response_headers = {"range": "bytes=0-{:d}".format(chunk_size - 1)}
        transport = self._chunk_mock(http.client.PERMANENT_REDIRECT, response_headers)
        # Check the state before the request.
        assert upload._bytes_uploaded == 0

        # Make request and check the return value (against the mock).
        response = await upload.transmit_next_chunk(transport)
        assert response is transport.request.return_value
        # Check that the state has been updated.
        assert upload._bytes_uploaded == chunk_size
        # Make sure the mock was called as expected.
        payload = data[:chunk_size]
        content_range = "bytes 0-{:d}/{:d}".format(chunk_size - 1, len(data))
        expected_headers = {
            "content-range": content_range,
            "content-type": BASIC_CONTENT,
        }
        transport.request.assert_called_once_with(
            "PUT",
            upload.resumable_url,
            data=payload,
            headers=expected_headers,
            timeout=EXPECTED_TIMEOUT,
        )

    @pytest.mark.asyncio
    async def test_transmit_next_chunk_w_custom_timeout(self):
        data = b"This time the data is official."
        upload = self._upload_in_flight(data)
        # Make a fake chunk size smaller than 256 KB.
        chunk_size = 10
        assert chunk_size < len(data)
        upload._chunk_size = chunk_size
        # Make a fake 308 response.
        response_headers = {"range": "bytes=0-{:d}".format(chunk_size - 1)}
        transport = self._chunk_mock(http.client.PERMANENT_REDIRECT, response_headers)
        # Check the state before the request.
        assert upload._bytes_uploaded == 0

        # Make request and check the return value (against the mock).
        response = await upload.transmit_next_chunk(transport, timeout=12.6)
        assert response is transport.request.return_value
        # Check that the state has been updated.
        assert upload._bytes_uploaded == chunk_size
        # Make sure the mock was called as expected.
        payload = data[:chunk_size]
        content_range = "bytes 0-{:d}/{:d}".format(chunk_size - 1, len(data))
        expected_headers = {
            "content-range": content_range,
            "content-type": BASIC_CONTENT,
        }
        transport.request.assert_called_once_with(
            "PUT",
            upload.resumable_url,
            data=payload,
            headers=expected_headers,
            timeout=12.6,
        )

    @pytest.mark.asyncio
    async def test_recover(self):
        upload = upload_mod.ResumableUpload(RESUMABLE_URL, ONE_MB)
        upload._invalid = True  # Make sure invalid.
        upload._stream = mock.Mock(spec=["seek"])
        upload._resumable_url = "http://test.invalid?upload_id=big-deal"

        end = 55555
        headers = {"range": "bytes=0-{:d}".format(end)}
        transport = self._chunk_mock(http.client.PERMANENT_REDIRECT, headers)

        ret_val = await upload.recover(transport)
        assert ret_val is transport.request.return_value
        # Check the state of ``upload`` after.
        assert upload.bytes_uploaded == end + 1
        assert not upload.invalid
        upload._stream.seek.assert_called_once_with(end + 1)
        expected_headers = {"content-range": "bytes */*"}
        transport.request.assert_called_once_with(
            "PUT",
            upload.resumable_url,
            data=None,
            headers=expected_headers,
            timeout=EXPECTED_TIMEOUT,
        )


def _make_response(status_code=200, headers=None):
    headers = headers or {}
    return mock.Mock(
        _headers=headers,
        headers=headers,
        status=status_code,
        spec=["_headers", "headers", "status_code"],
    )
