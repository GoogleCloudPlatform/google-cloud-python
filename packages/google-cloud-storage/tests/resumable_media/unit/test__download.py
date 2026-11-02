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
from unittest import mock

import pytest  # type: ignore

from google.cloud.storage._media import _download
from google.cloud.storage.exceptions import InvalidResponse
from google.cloud.storage.retry import DEFAULT_RETRY

EXAMPLE_URL = (
    "https://www.googleapis.com/download/storage/v1/b/{BUCKET}/o/{OBJECT}?alt=media"
)


class TestDownloadBase(object):
    def test_constructor_defaults(self):
        download = _download.DownloadBase(EXAMPLE_URL)
        assert download.media_url == EXAMPLE_URL
        assert download._stream is None
        assert download.start is None
        assert download.end is None
        assert download._headers == {}
        assert not download._finished
        _check_retry_strategy(download)

    def test_constructor_explicit(self):
        start = 11
        end = 10001
        headers = {"foof": "barf"}
        download = _download.DownloadBase(
            EXAMPLE_URL,
            stream=mock.sentinel.stream,
            start=start,
            end=end,
            headers=headers,
        )
        assert download.media_url == EXAMPLE_URL
        assert download._stream is mock.sentinel.stream
        assert download.start == start
        assert download.end == end
        assert download._headers is headers
        assert not download._finished
        _check_retry_strategy(download)

    def test_finished_property(self):
        download = _download.DownloadBase(EXAMPLE_URL)
        # Default value of @property.
        assert not download.finished

        # Make sure we cannot set it on public @property.
        with pytest.raises(AttributeError):
            download.finished = False

        # Set it privately and then check the @property.
        download._finished = True
        assert download.finished

    def test__get_status_code(self):
        with pytest.raises(NotImplementedError) as exc_info:
            _download.DownloadBase._get_status_code(None)

        exc_info.match("virtual")

    def test__get_headers(self):
        with pytest.raises(NotImplementedError) as exc_info:
            _download.DownloadBase._get_headers(None)

        exc_info.match("virtual")

    def test__get_body(self):
        with pytest.raises(NotImplementedError) as exc_info:
            _download.DownloadBase._get_body(None)

        exc_info.match("virtual")


class TestDownload(object):
    def test__prepare_request_already_finished(self):
        download = _download.Download(EXAMPLE_URL)
        download._finished = True
        with pytest.raises(ValueError):
            download._prepare_request()

    def test__prepare_request(self):
        download1 = _download.Download(EXAMPLE_URL)
        method1, url1, payload1, headers1 = download1._prepare_request()
        assert method1 == "GET"
        assert url1 == EXAMPLE_URL
        assert payload1 is None
        assert headers1 == {}

        download2 = _download.Download(EXAMPLE_URL, start=53)
        method2, url2, payload2, headers2 = download2._prepare_request()
        assert method2 == "GET"
        assert url2 == EXAMPLE_URL
        assert payload2 is None
        assert headers2 == {"range": "bytes=53-"}

    def test__prepare_request_with_headers(self):
        headers = {"spoonge": "borb"}
        download = _download.Download(EXAMPLE_URL, start=11, end=111, headers=headers)
        method, url, payload, new_headers = download._prepare_request()
        assert method == "GET"
        assert url == EXAMPLE_URL
        assert payload is None
        assert new_headers is headers
        assert headers == {"range": "bytes=11-111", "spoonge": "borb"}

    def test__process_response(self):
        download = _download.Download(EXAMPLE_URL)
        _fix_up_virtual(download)

        # Make sure **not finished** before.
        assert not download.finished
        response = mock.Mock(status_code=int(http.client.OK), spec=["status_code"])
        ret_val = download._process_response(response)
        assert ret_val is None
        # Make sure **finished** after.
        assert download.finished

    def test__process_response_bad_status(self):
        download = _download.Download(EXAMPLE_URL)
        _fix_up_virtual(download)

        # Make sure **not finished** before.
        assert not download.finished
        response = mock.Mock(
            status_code=int(http.client.NOT_FOUND), spec=["status_code"]
        )
        with pytest.raises(InvalidResponse) as exc_info:
            download._process_response(response)

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 5
        assert error.args[1] == response.status_code
        assert error.args[3] == http.client.OK
        assert error.args[4] == http.client.PARTIAL_CONTENT
        # Make sure **finished** even after a failure.
        assert download.finished

    def test_consume(self):
        download = _download.Download(EXAMPLE_URL)
        with pytest.raises(NotImplementedError) as exc_info:
            download.consume(None)

        exc_info.match("virtual")


class TestChunkedDownload(object):
    def test_constructor_defaults(self):
        chunk_size = 256
        stream = mock.sentinel.stream
        download = _download.ChunkedDownload(EXAMPLE_URL, chunk_size, stream)
        assert download.media_url == EXAMPLE_URL
        assert download.chunk_size == chunk_size
        assert download.start == 0
        assert download.end is None
        assert download._headers == {}
        assert not download._finished
        _check_retry_strategy(download)
        assert download._stream is stream
        assert download._bytes_downloaded == 0
        assert download._total_bytes is None
        assert not download._invalid

    def test_constructor_bad_start(self):
        with pytest.raises(ValueError):
            _download.ChunkedDownload(EXAMPLE_URL, 256, None, start=-11)

    def test_bytes_downloaded_property(self):
        download = _download.ChunkedDownload(EXAMPLE_URL, 256, None)
        # Default value of @property.
        assert download.bytes_downloaded == 0

        # Make sure we cannot set it on public @property.
        with pytest.raises(AttributeError):
            download.bytes_downloaded = 1024

        # Set it privately and then check the @property.
        download._bytes_downloaded = 128
        assert download.bytes_downloaded == 128

    def test_total_bytes_property(self):
        download = _download.ChunkedDownload(EXAMPLE_URL, 256, None)
        # Default value of @property.
        assert download.total_bytes is None

        # Make sure we cannot set it on public @property.
        with pytest.raises(AttributeError):
            download.total_bytes = 65536

        # Set it privately and then check the @property.
        download._total_bytes = 8192
        assert download.total_bytes == 8192

    def test__get_byte_range(self):
        chunk_size = 512
        download = _download.ChunkedDownload(EXAMPLE_URL, chunk_size, None)
        curr_start, curr_end = download._get_byte_range()
        assert curr_start == 0
        assert curr_end == chunk_size - 1

    def test__get_byte_range_with_end(self):
        chunk_size = 512
        start = 1024
        end = 1151
        download = _download.ChunkedDownload(
            EXAMPLE_URL, chunk_size, None, start=start, end=end
        )
        curr_start, curr_end = download._get_byte_range()
        assert curr_start == start
        assert curr_end == end
        # Make sure this is less than the chunk size.
        actual_size = curr_end - curr_start + 1
        assert actual_size < chunk_size

    def test__get_byte_range_with_total_bytes(self):
        chunk_size = 512
        download = _download.ChunkedDownload(EXAMPLE_URL, chunk_size, None)
        total_bytes = 207
        download._total_bytes = total_bytes
        curr_start, curr_end = download._get_byte_range()
        assert curr_start == 0
        assert curr_end == total_bytes - 1
        # Make sure this is less than the chunk size.
        actual_size = curr_end - curr_start + 1
        assert actual_size < chunk_size

    @staticmethod
    def _response_content_range(start_byte, end_byte, total_bytes):
        return "bytes {:d}-{:d}/{:d}".format(start_byte, end_byte, total_bytes)

    def _response_headers(self, start_byte, end_byte, total_bytes):
        content_length = end_byte - start_byte + 1
        resp_range = self._response_content_range(start_byte, end_byte, total_bytes)
        return {
            "content-length": "{:d}".format(content_length),
            "content-range": resp_range,
        }

    def _mock_response(
        self, start_byte, end_byte, total_bytes, content=None, status_code=None
    ):
        response_headers = self._response_headers(start_byte, end_byte, total_bytes)
        return mock.Mock(
            content=content,
            headers=response_headers,
            status_code=status_code,
            spec=["content", "headers", "status_code"],
        )

    def test__prepare_request_already_finished(self):
        download = _download.ChunkedDownload(EXAMPLE_URL, 64, None)
        download._finished = True
        with pytest.raises(ValueError) as exc_info:
            download._prepare_request()

        assert exc_info.match("Download has finished.")

    def test__prepare_request_invalid(self):
        download = _download.ChunkedDownload(EXAMPLE_URL, 64, None)
        download._invalid = True
        with pytest.raises(ValueError) as exc_info:
            download._prepare_request()

        assert exc_info.match("Download is invalid and cannot be re-used.")

    def test__prepare_request(self):
        chunk_size = 2048
        download1 = _download.ChunkedDownload(EXAMPLE_URL, chunk_size, None)
        method1, url1, payload1, headers1 = download1._prepare_request()
        assert method1 == "GET"
        assert url1 == EXAMPLE_URL
        assert payload1 is None
        assert headers1 == {"range": "bytes=0-2047"}

        download2 = _download.ChunkedDownload(
            EXAMPLE_URL, chunk_size, None, start=19991
        )
        download2._total_bytes = 20101
        method2, url2, payload2, headers2 = download2._prepare_request()
        assert method2 == "GET"
        assert url2 == EXAMPLE_URL
        assert payload2 is None
        assert headers2 == {"range": "bytes=19991-20100"}

    def test__prepare_request_with_headers(self):
        chunk_size = 2048
        headers = {"patrizio": "Starf-ish"}
        download = _download.ChunkedDownload(
            EXAMPLE_URL, chunk_size, None, headers=headers
        )
        method, url, payload, new_headers = download._prepare_request()
        assert method == "GET"
        assert url == EXAMPLE_URL
        assert payload is None
        assert new_headers is headers
        expected = {"patrizio": "Starf-ish", "range": "bytes=0-2047"}
        assert headers == expected

    def test__make_invalid(self):
        download = _download.ChunkedDownload(EXAMPLE_URL, 512, None)
        assert not download.invalid
        download._make_invalid()
        assert download.invalid

    def test__process_response(self):
        data = b"1234xyztL" * 37  # 9 * 37 == 33
        chunk_size = len(data)
        stream = io.BytesIO()
        download = _download.ChunkedDownload(EXAMPLE_URL, chunk_size, stream)
        _fix_up_virtual(download)

        already = 22
        download._bytes_downloaded = already
        total_bytes = 4444

        # Check internal state before.
        assert not download.finished
        assert download.bytes_downloaded == already
        assert download.total_bytes is None
        # Actually call the method to update.
        response = self._mock_response(
            already,
            already + chunk_size - 1,
            total_bytes,
            content=data,
            status_code=int(http.client.PARTIAL_CONTENT),
        )
        download._process_response(response)
        # Check internal state after.
        assert not download.finished
        assert download.bytes_downloaded == already + chunk_size
        assert download.total_bytes == total_bytes
        assert stream.getvalue() == data

    def test__process_response_transfer_encoding(self):
        data = b"1234xyztL" * 37
        chunk_size = len(data)
        stream = io.BytesIO()
        download = _download.ChunkedDownload(EXAMPLE_URL, chunk_size, stream)
        _fix_up_virtual(download)

        already = 22
        download._bytes_downloaded = already
        total_bytes = 4444

        # Check internal state before.
        assert not download.finished
        assert download.bytes_downloaded == already
        assert download.total_bytes is None
        assert not download.invalid
        # Actually call the method to update.
        response = self._mock_response(
            already,
            already + chunk_size - 1,
            total_bytes,
            content=data,
            status_code=int(http.client.PARTIAL_CONTENT),
        )
        response.headers["transfer-encoding"] = "chunked"
        del response.headers["content-length"]
        download._process_response(response)
        # Check internal state after.
        assert not download.finished
        assert download.bytes_downloaded == already + chunk_size
        assert download.total_bytes == total_bytes
        assert stream.getvalue() == data

    def test__process_response_bad_status(self):
        chunk_size = 384
        stream = mock.Mock(spec=["write"])
        download = _download.ChunkedDownload(EXAMPLE_URL, chunk_size, stream)
        _fix_up_virtual(download)

        total_bytes = 300

        # Check internal state before.
        assert not download.finished
        assert download.bytes_downloaded == 0
        assert download.total_bytes is None
        # Actually call the method to update.
        response = self._mock_response(
            0, total_bytes - 1, total_bytes, status_code=int(http.client.NOT_FOUND)
        )
        with pytest.raises(InvalidResponse) as exc_info:
            download._process_response(response)

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 5
        assert error.args[1] == response.status_code
        assert error.args[3] == http.client.OK
        assert error.args[4] == http.client.PARTIAL_CONTENT
        # Check internal state after.
        assert not download.finished
        assert download.bytes_downloaded == 0
        assert download.total_bytes is None
        assert download.invalid
        stream.write.assert_not_called()

    def test__process_response_missing_content_length(self):
        download = _download.ChunkedDownload(EXAMPLE_URL, 256, None)
        _fix_up_virtual(download)

        # Check internal state before.
        assert not download.finished
        assert download.bytes_downloaded == 0
        assert download.total_bytes is None
        assert not download.invalid
        # Actually call the method to update.
        response = mock.Mock(
            headers={"content-range": "bytes 0-99/99"},
            status_code=int(http.client.PARTIAL_CONTENT),
            content=b"DEADBEEF",
            spec=["headers", "status_code", "content"],
        )
        with pytest.raises(InvalidResponse) as exc_info:
            download._process_response(response)

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 2
        assert error.args[1] == "content-length"
        # Check internal state after.
        assert not download.finished
        assert download.bytes_downloaded == 0
        assert download.total_bytes is None
        assert download.invalid

    def test__process_response_bad_content_range(self):
        download = _download.ChunkedDownload(EXAMPLE_URL, 256, None)
        _fix_up_virtual(download)

        # Check internal state before.
        assert not download.finished
        assert download.bytes_downloaded == 0
        assert download.total_bytes is None
        assert not download.invalid
        # Actually call the method to update.
        data = b"stuff"
        headers = {
            "content-length": "{:d}".format(len(data)),
            "content-range": "kites x-y/58",
        }
        response = mock.Mock(
            content=data,
            headers=headers,
            status_code=int(http.client.PARTIAL_CONTENT),
            spec=["content", "headers", "status_code"],
        )
        with pytest.raises(InvalidResponse) as exc_info:
            download._process_response(response)

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 3
        assert error.args[1] == headers["content-range"]
        # Check internal state after.
        assert not download.finished
        assert download.bytes_downloaded == 0
        assert download.total_bytes is None
        assert download.invalid

    def test__process_response_body_wrong_length(self):
        chunk_size = 10
        stream = mock.Mock(spec=["write"])
        download = _download.ChunkedDownload(EXAMPLE_URL, chunk_size, stream)
        _fix_up_virtual(download)

        total_bytes = 100

        # Check internal state before.
        assert not download.finished
        assert download.bytes_downloaded == 0
        assert download.total_bytes is None
        # Actually call the method to update.
        data = b"not 10"
        response = self._mock_response(
            0,
            chunk_size - 1,
            total_bytes,
            content=data,
            status_code=int(http.client.PARTIAL_CONTENT),
        )
        with pytest.raises(InvalidResponse) as exc_info:
            download._process_response(response)

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 5
        assert error.args[2] == chunk_size
        assert error.args[4] == len(data)
        # Check internal state after.
        assert not download.finished
        assert download.bytes_downloaded == 0
        assert download.total_bytes is None
        assert download.invalid
        stream.write.assert_not_called()

    def test__process_response_when_finished(self):
        chunk_size = 256
        stream = io.BytesIO()
        download = _download.ChunkedDownload(EXAMPLE_URL, chunk_size, stream)
        _fix_up_virtual(download)

        total_bytes = 200

        # Check internal state before.
        assert not download.finished
        assert download.bytes_downloaded == 0
        assert download.total_bytes is None
        # Actually call the method to update.
        data = b"abcd" * 50  # 4 * 50 == 200
        response = self._mock_response(
            0,
            total_bytes - 1,
            total_bytes,
            content=data,
            status_code=int(http.client.OK),
        )
        download._process_response(response)
        # Check internal state after.
        assert download.finished
        assert download.bytes_downloaded == total_bytes
        assert total_bytes < chunk_size
        assert download.total_bytes == total_bytes
        assert stream.getvalue() == data

    def test__process_response_when_reaching_end(self):
        chunk_size = 8192
        end = 65000
        stream = io.BytesIO()
        download = _download.ChunkedDownload(EXAMPLE_URL, chunk_size, stream, end=end)
        _fix_up_virtual(download)

        download._bytes_downloaded = 7 * chunk_size
        download._total_bytes = 8 * chunk_size

        # Check internal state before.
        assert not download.finished
        assert download.bytes_downloaded == 7 * chunk_size
        assert download.total_bytes == 8 * chunk_size
        # Actually call the method to update.
        expected_size = end - 7 * chunk_size + 1
        data = b"B" * expected_size
        response = self._mock_response(
            7 * chunk_size,
            end,
            8 * chunk_size,
            content=data,
            status_code=int(http.client.PARTIAL_CONTENT),
        )
        download._process_response(response)
        # Check internal state after.
        assert download.finished
        assert download.bytes_downloaded == end + 1
        assert download.bytes_downloaded < download.total_bytes
        assert download.total_bytes == 8 * chunk_size
        assert stream.getvalue() == data

    def test__process_response_when_content_range_is_zero(self):
        chunk_size = 10
        stream = mock.Mock(spec=["write"])
        download = _download.ChunkedDownload(EXAMPLE_URL, chunk_size, stream)
        _fix_up_virtual(download)

        content_range = _download._ZERO_CONTENT_RANGE_HEADER
        headers = {"content-range": content_range}
        status_code = http.client.REQUESTED_RANGE_NOT_SATISFIABLE
        response = mock.Mock(
            headers=headers, status_code=status_code, spec=["headers", "status_code"]
        )
        download._process_response(response)
        stream.write.assert_not_called()
        assert download.finished
        assert download.bytes_downloaded == 0
        assert download.total_bytes is None

    def test_consume_next_chunk(self):
        download = _download.ChunkedDownload(EXAMPLE_URL, 256, None)
        with pytest.raises(NotImplementedError) as exc_info:
            download.consume_next_chunk(None)

        exc_info.match("virtual")


class Test__add_bytes_range(object):
    def test_do_nothing(self):
        headers = {}
        ret_val = _download.add_bytes_range(None, None, headers)
        assert ret_val is None
        assert headers == {}

    def test_both_vals(self):
        headers = {}
        ret_val = _download.add_bytes_range(17, 1997, headers)
        assert ret_val is None
        assert headers == {"range": "bytes=17-1997"}

    def test_end_only(self):
        headers = {}
        ret_val = _download.add_bytes_range(None, 909, headers)
        assert ret_val is None
        assert headers == {"range": "bytes=0-909"}

    def test_start_only(self):
        headers = {}
        ret_val = _download.add_bytes_range(3735928559, None, headers)
        assert ret_val is None
        assert headers == {"range": "bytes=3735928559-"}

    def test_start_as_offset(self):
        headers = {}
        ret_val = _download.add_bytes_range(-123454321, None, headers)
        assert ret_val is None
        assert headers == {"range": "bytes=-123454321"}


class Test_get_range_info(object):
    @staticmethod
    def _make_response(content_range):
        headers = {"content-range": content_range}
        return mock.Mock(headers=headers, spec=["headers"])

    def _success_helper(self, **kwargs):
        content_range = "Bytes 7-11/42"
        response = self._make_response(content_range)
        start_byte, end_byte, total_bytes = _download.get_range_info(
            response, _get_headers, **kwargs
        )
        assert start_byte == 7
        assert end_byte == 11
        assert total_bytes == 42

    def test_success(self):
        self._success_helper()

    def test_success_with_callback(self):
        callback = mock.Mock(spec=[])
        self._success_helper(callback=callback)
        callback.assert_not_called()

    def _failure_helper(self, **kwargs):
        content_range = "nope x-6/y"
        response = self._make_response(content_range)
        with pytest.raises(InvalidResponse) as exc_info:
            _download.get_range_info(response, _get_headers, **kwargs)

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 3
        assert error.args[1] == content_range

    def test_failure(self):
        self._failure_helper()

    def test_failure_with_callback(self):
        callback = mock.Mock(spec=[])
        self._failure_helper(callback=callback)
        callback.assert_called_once_with()

    def _missing_header_helper(self, **kwargs):
        response = mock.Mock(headers={}, spec=["headers"])
        with pytest.raises(InvalidResponse) as exc_info:
            _download.get_range_info(response, _get_headers, **kwargs)

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 2
        assert error.args[1] == "content-range"

    def test_missing_header(self):
        self._missing_header_helper()

    def test_missing_header_with_callback(self):
        callback = mock.Mock(spec=[])
        self._missing_header_helper(callback=callback)
        callback.assert_called_once_with()


class Test__check_for_zero_content_range(object):
    @staticmethod
    def _make_response(content_range, status_code):
        headers = {"content-range": content_range}
        return mock.Mock(
            headers=headers, status_code=status_code, spec=["headers", "status_code"]
        )

    def test_status_code_416_and_test_content_range_zero_both(self):
        content_range = _download._ZERO_CONTENT_RANGE_HEADER
        status_code = http.client.REQUESTED_RANGE_NOT_SATISFIABLE
        response = self._make_response(content_range, status_code)
        assert _download._check_for_zero_content_range(
            response, _get_status_code, _get_headers
        )

    def test_status_code_416_only(self):
        content_range = "bytes 2-5/3"
        status_code = http.client.REQUESTED_RANGE_NOT_SATISFIABLE
        response = self._make_response(content_range, status_code)
        assert not _download._check_for_zero_content_range(
            response, _get_status_code, _get_headers
        )

    def test_content_range_zero_only(self):
        content_range = _download._ZERO_CONTENT_RANGE_HEADER
        status_code = http.client.OK
        response = self._make_response(content_range, status_code)
        assert not _download._check_for_zero_content_range(
            response, _get_status_code, _get_headers
        )


def _get_status_code(response):
    return response.status_code


def _get_headers(response):
    return response.headers


def _get_body(response):
    return response.content


def _fix_up_virtual(download):
    download._get_status_code = _get_status_code
    download._get_headers = _get_headers
    download._get_body = _get_body


def _check_retry_strategy(download):
    assert download._retry_strategy == DEFAULT_RETRY
