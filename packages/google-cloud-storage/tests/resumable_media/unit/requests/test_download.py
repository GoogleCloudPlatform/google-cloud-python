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

from google.cloud.storage._media import _helpers
from google.cloud.storage._media.requests import _request_helpers
from google.cloud.storage._media.requests import download as download_mod
from google.cloud.storage.exceptions import DataCorruption

URL_PREFIX = "https://www.googleapis.com/download/storage/v1/b/{BUCKET}/o/"
EXAMPLE_URL = URL_PREFIX + "{OBJECT}?alt=media"
EXPECTED_TIMEOUT = (61, 60)


class TestDownload(object):
    def test__write_to_stream_no_hash_check(self):
        stream = io.BytesIO()
        download = download_mod.Download(EXAMPLE_URL, stream=stream)

        chunk1 = b"right now, "
        chunk2 = b"but a little later"
        response = _mock_response(chunks=[chunk1, chunk2], headers={})

        ret_val = download._write_to_stream(response)
        assert ret_val is None

        assert stream.getvalue() == chunk1 + chunk2
        assert download._bytes_downloaded == len(chunk1 + chunk2)

        # Check mocks.
        response.__enter__.assert_called_once_with()
        response.__exit__.assert_called_once_with(None, None, None)
        response.iter_content.assert_called_once_with(
            chunk_size=_request_helpers._SINGLE_GET_CHUNK_SIZE, decode_unicode=False
        )

    def test__write_to_stream_empty_chunks(self):
        stream = io.BytesIO()
        download = download_mod.Download(EXAMPLE_URL, stream=stream)

        response = _mock_response(chunks=[], headers={})

        ret_val = download._write_to_stream(response)
        assert ret_val is None

        assert stream.getvalue() == b""
        assert download._bytes_downloaded == 0

        # Check mocks.
        response.__enter__.assert_called_once_with()
        response.__exit__.assert_called_once_with(None, None, None)
        response.iter_content.assert_called_once_with(
            chunk_size=_request_helpers._SINGLE_GET_CHUNK_SIZE, decode_unicode=False
        )

    @pytest.mark.parametrize("checksum", ["auto", "md5", "crc32c", None])
    def test__write_to_stream_with_hash_check_success(self, checksum):
        stream = io.BytesIO()
        download = download_mod.Download(EXAMPLE_URL, stream=stream, checksum=checksum)

        chunk1 = b"first chunk, count starting at 0. "
        chunk2 = b"second chunk, or chunk 1, which is better? "
        chunk3 = b"ordinals and numerals and stuff."
        header_value = "crc32c=qmNCyg==,md5=fPAJHnnoi/+NadyNxT2c2w=="
        headers = {_helpers._HASH_HEADER: header_value}
        response = _mock_response(chunks=[chunk1, chunk2, chunk3], headers=headers)

        ret_val = download._write_to_stream(response)
        assert ret_val is None

        assert stream.getvalue() == chunk1 + chunk2 + chunk3
        assert download._bytes_downloaded == len(chunk1 + chunk2 + chunk3)
        assert download._checksum_object is not None

        # Check mocks.
        response.__enter__.assert_called_once_with()
        response.__exit__.assert_called_once_with(None, None, None)
        response.iter_content.assert_called_once_with(
            chunk_size=_request_helpers._SINGLE_GET_CHUNK_SIZE, decode_unicode=False
        )

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test__write_to_stream_with_hash_check_fail(self, checksum):
        stream = io.BytesIO()
        download = download_mod.Download(EXAMPLE_URL, stream=stream, checksum=checksum)

        chunk1 = b"first chunk, count starting at 0. "
        chunk2 = b"second chunk, or chunk 1, which is better? "
        chunk3 = b"ordinals and numerals and stuff."
        bad_checksum = "d3JvbmcgbiBtYWRlIHVwIQ=="
        header_value = "crc32c={bad},md5={bad}".format(bad=bad_checksum)
        headers = {_helpers._HASH_HEADER: header_value}
        response = _mock_response(chunks=[chunk1, chunk2, chunk3], headers=headers)

        with pytest.raises(DataCorruption) as exc_info:
            download._write_to_stream(response)

        assert not download.finished

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 1
        if checksum == "md5":
            good_checksum = "fPAJHnnoi/+NadyNxT2c2w=="
        else:
            good_checksum = "qmNCyg=="
        msg = download_mod._CHECKSUM_MISMATCH.format(
            EXAMPLE_URL, bad_checksum, good_checksum, checksum_type=checksum.upper()
        )
        assert msg in error.args[0]
        assert (
            f"The download request read {download._bytes_downloaded} bytes of data."
            in error.args[0]
        )

        # Check mocks.
        response.__enter__.assert_called_once_with()
        response.__exit__.assert_called_once_with(None, None, None)
        response.iter_content.assert_called_once_with(
            chunk_size=_request_helpers._SINGLE_GET_CHUNK_SIZE, decode_unicode=False
        )

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test__write_to_stream_no_checksum_validation_for_partial_response(
        self, checksum
    ):
        stream = io.BytesIO()
        download = download_mod.Download(EXAMPLE_URL, stream=stream, checksum=checksum)

        chunk1 = b"first chunk"
        response = _mock_response(
            status_code=http.client.PARTIAL_CONTENT, chunks=[chunk1]
        )

        # Make sure that the checksum is not validated.
        with mock.patch(
            "google.cloud.storage._media._helpers.prepare_checksum_digest",
            return_value=None,
        ) as prepare_checksum_digest:
            download._write_to_stream(response)
            assert not prepare_checksum_digest.called

        assert not download.finished

        # Check mocks.
        response.__enter__.assert_called_once_with()
        response.__exit__.assert_called_once_with(None, None, None)
        response.iter_content.assert_called_once_with(
            chunk_size=_request_helpers._SINGLE_GET_CHUNK_SIZE, decode_unicode=False
        )

    def test__write_to_stream_with_invalid_checksum_type(self):
        BAD_CHECKSUM_TYPE = "badsum"

        stream = io.BytesIO()
        download = download_mod.Download(
            EXAMPLE_URL, stream=stream, checksum=BAD_CHECKSUM_TYPE
        )

        chunk1 = b"first chunk, count starting at 0. "
        chunk2 = b"second chunk, or chunk 1, which is better? "
        chunk3 = b"ordinals and numerals and stuff."
        bad_checksum = "d3JvbmcgbiBtYWRlIHVwIQ=="
        header_value = "crc32c={bad},md5={bad}".format(bad=bad_checksum)
        headers = {_helpers._HASH_HEADER: header_value}
        response = _mock_response(chunks=[chunk1, chunk2, chunk3], headers=headers)

        with pytest.raises(ValueError) as exc_info:
            download._write_to_stream(response)

        assert not download.finished

        error = exc_info.value
        assert error.args[0] == "checksum must be ``'md5'``, ``'crc32c'`` or ``None``"

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test__write_to_stream_incomplete_read(self, checksum):
        stream = io.BytesIO()
        download = download_mod.Download(EXAMPLE_URL, stream=stream, checksum=checksum)

        chunk1 = b"first chunk"
        mock_full_content_length = len(chunk1) + 123
        headers = {"x-goog-stored-content-length": mock_full_content_length}
        bad_checksum = "d3JvbmcgbiBtYWRlIHVwIQ=="
        header_value = "crc32c={bad},md5={bad}".format(bad=bad_checksum)
        headers[_helpers._HASH_HEADER] = header_value
        response = _mock_response(chunks=[chunk1], headers=headers)

        with pytest.raises(ConnectionError) as exc_info:
            download._write_to_stream(response)

        assert not download.finished
        error = exc_info.value
        assert (
            f"The download request read {download._bytes_downloaded} bytes of data."
            in error.args[0]
        )

    @pytest.mark.parametrize("checksum", ["auto", "md5", "crc32c", None])
    def test__write_to_stream_single_shot_download(self, checksum):
        stream = io.BytesIO()
        download = download_mod.Download(
            EXAMPLE_URL, stream=stream, checksum=checksum, single_shot_download=True
        )

        chunk1 = b"all at once!"
        response = _mock_response(chunks=[chunk1], headers={})
        ret_val = download._write_to_stream(response)

        assert ret_val is None
        assert stream.getvalue() == chunk1
        assert download._bytes_downloaded == len(chunk1)

        response.__enter__.assert_called_once_with()
        response.__exit__.assert_called_once_with(None, None, None)
        response.raw.read.assert_called_once_with(decode_content=True)

    def _consume_helper(
        self,
        stream=None,
        end=65536,
        headers=None,
        chunks=(),
        response_headers=None,
        checksum="md5",
        timeout=None,
    ):
        download = download_mod.Download(
            EXAMPLE_URL, stream=stream, end=end, headers=headers, checksum=checksum
        )
        transport = mock.Mock(spec=["request"])
        transport.request.return_value = _mock_response(
            chunks=chunks, headers=response_headers
        )

        assert not download.finished

        if timeout is not None:
            ret_val = download.consume(transport, timeout=timeout)
        else:
            ret_val = download.consume(transport)

        assert ret_val is transport.request.return_value

        called_kwargs = {
            "data": None,
            "headers": download._headers,
            "timeout": EXPECTED_TIMEOUT if timeout is None else timeout,
        }
        if chunks:
            assert stream is not None
            called_kwargs["stream"] = True

        transport.request.assert_called_once_with("GET", EXAMPLE_URL, **called_kwargs)

        range_bytes = "bytes={:d}-{:d}".format(0, end)
        assert download._headers["range"] == range_bytes
        assert download.finished

        return transport

    def test_consume(self):
        self._consume_helper()

    def test_consume_with_custom_timeout(self):
        self._consume_helper(timeout=14.7)

    @pytest.mark.parametrize("checksum", ["auto", "md5", "crc32c", None])
    def test_consume_with_stream(self, checksum):
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")
        transport = self._consume_helper(
            stream=stream, chunks=chunks, checksum=checksum
        )

        assert stream.getvalue() == b"".join(chunks)

        # Check mocks.
        response = transport.request.return_value
        response.__enter__.assert_called_once_with()
        response.__exit__.assert_called_once_with(None, None, None)
        response.iter_content.assert_called_once_with(
            chunk_size=_request_helpers._SINGLE_GET_CHUNK_SIZE, decode_unicode=False
        )

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test_consume_with_stream_hash_check_success(self, checksum):
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")
        header_value = "crc32c=UNIQxg==,md5=JvS1wjMvfbCXgEGeaJJLDQ=="
        headers = {_helpers._HASH_HEADER: header_value}
        transport = self._consume_helper(
            stream=stream, chunks=chunks, response_headers=headers, checksum=checksum
        )

        assert stream.getvalue() == b"".join(chunks)

        # Check mocks.
        response = transport.request.return_value
        response.__enter__.assert_called_once_with()
        response.__exit__.assert_called_once_with(None, None, None)
        response.iter_content.assert_called_once_with(
            chunk_size=_request_helpers._SINGLE_GET_CHUNK_SIZE, decode_unicode=False
        )

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test_consume_with_stream_hash_check_fail(self, checksum):
        stream = io.BytesIO()
        download = download_mod.Download(EXAMPLE_URL, stream=stream, checksum=checksum)

        chunks = (b"zero zero", b"niner tango")
        bad_checksum = "anVzdCBub3QgdGhpcyAxLA=="
        header_value = "crc32c={bad},md5={bad}".format(bad=bad_checksum)
        headers = {_helpers._HASH_HEADER: header_value}
        transport = mock.Mock(spec=["request"])
        transport.request.return_value = _mock_response(chunks=chunks, headers=headers)

        assert not download.finished
        with pytest.raises(DataCorruption) as exc_info:
            download.consume(transport)

        assert stream.getvalue() == b"".join(chunks)
        assert download.finished
        assert download._headers == {}

        error = exc_info.value
        assert error.response is transport.request.return_value
        assert len(error.args) == 1
        if checksum == "md5":
            good_checksum = "1A/dxEpys717C6FH7FIWDw=="
        else:
            good_checksum = "GvNZlg=="
        msg = download_mod._CHECKSUM_MISMATCH.format(
            EXAMPLE_URL, bad_checksum, good_checksum, checksum_type=checksum.upper()
        )
        assert msg in error.args[0]
        assert (
            f"The download request read {download._bytes_downloaded} bytes of data."
            in error.args[0]
        )

        # Check mocks.
        transport.request.assert_called_once_with(
            "GET",
            EXAMPLE_URL,
            data=None,
            headers={},
            stream=True,
            timeout=EXPECTED_TIMEOUT,
        )

    def test_consume_with_headers(self):
        headers = {}  # Empty headers
        end = 16383
        self._consume_helper(end=end, headers=headers)
        range_bytes = "bytes={:d}-{:d}".format(0, end)
        # Make sure the headers have been modified.
        assert headers == {"range": range_bytes}

    def test_consume_gets_generation_from_url(self):
        GENERATION_VALUE = 1641590104888641
        url = EXAMPLE_URL + f"&generation={GENERATION_VALUE}"
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")

        download = download_mod.Download(
            url, stream=stream, end=65536, headers=None, checksum="md5"
        )
        transport = mock.Mock(spec=["request"])
        transport.request.return_value = _mock_response(chunks=chunks, headers=None)

        assert not download.finished
        assert download._object_generation is None

        ret_val = download.consume(transport)

        assert download._object_generation == GENERATION_VALUE
        assert ret_val is transport.request.return_value
        assert stream.getvalue() == b"".join(chunks)

        called_kwargs = {
            "data": None,
            "headers": download._headers,
            "timeout": EXPECTED_TIMEOUT,
            "stream": True,
        }
        transport.request.assert_called_once_with("GET", url, **called_kwargs)

    def test_consume_gets_generation_from_headers(self):
        GENERATION_VALUE = 1641590104888641
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")

        download = download_mod.Download(
            EXAMPLE_URL, stream=stream, end=65536, headers=None, checksum="md5"
        )
        transport = mock.Mock(spec=["request"])
        headers = {_helpers._GENERATION_HEADER: GENERATION_VALUE}
        transport.request.return_value = _mock_response(chunks=chunks, headers=headers)

        assert not download.finished
        assert download._object_generation is None

        ret_val = download.consume(transport)

        assert download._object_generation == GENERATION_VALUE
        assert ret_val is transport.request.return_value
        assert stream.getvalue() == b"".join(chunks)

        called_kwargs = {
            "data": None,
            "headers": download._headers,
            "timeout": EXPECTED_TIMEOUT,
            "stream": True,
        }
        transport.request.assert_called_once_with("GET", EXAMPLE_URL, **called_kwargs)

    def test_consume_w_object_generation(self):
        GENERATION_VALUE = 1641590104888641
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")
        end = 65536

        download = download_mod.Download(
            EXAMPLE_URL, stream=stream, end=end, headers=None, checksum="md5"
        )
        transport = mock.Mock(spec=["request"])
        transport.request.return_value = _mock_response(chunks=chunks, headers=None)

        assert download._object_generation is None

        # Mock a retry operation with object generation retrieved and bytes already downloaded in the stream
        download._object_generation = GENERATION_VALUE
        offset = 256
        download._bytes_downloaded = offset
        download.consume(transport)

        expected_url = EXAMPLE_URL + f"&generation={GENERATION_VALUE}"
        called_kwargs = {
            "data": None,
            "headers": download._headers,
            "timeout": EXPECTED_TIMEOUT,
            "stream": True,
        }
        transport.request.assert_called_once_with("GET", expected_url, **called_kwargs)
        range_bytes = "bytes={:d}-{:d}".format(offset, end)
        assert download._headers["range"] == range_bytes

    def test_consume_w_bytes_downloaded(self):
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")
        end = 65536

        download = download_mod.Download(
            EXAMPLE_URL, stream=stream, end=end, headers=None, checksum="md5"
        )
        transport = mock.Mock(spec=["request"])
        transport.request.return_value = _mock_response(chunks=chunks, headers=None)

        assert download._bytes_downloaded == 0

        # Mock a retry operation with bytes already downloaded in the stream and checksum stored
        offset = 256
        download._bytes_downloaded = offset
        download._expected_checksum = None
        download._checksum_object = _helpers._DoNothingHash()
        download.consume(transport)

        called_kwargs = {
            "data": None,
            "headers": download._headers,
            "timeout": EXPECTED_TIMEOUT,
            "stream": True,
        }
        transport.request.assert_called_once_with("GET", EXAMPLE_URL, **called_kwargs)
        range_bytes = "bytes={:d}-{:d}".format(offset, end)
        assert download._headers["range"] == range_bytes

    def test_consume_w_bytes_downloaded_range_read(self):
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")
        start = 1024
        end = 65536

        download = download_mod.Download(
            EXAMPLE_URL,
            stream=stream,
            start=start,
            end=end,
            headers=None,
            checksum="md5",
        )
        transport = mock.Mock(spec=["request"])
        transport.request.return_value = _mock_response(chunks=chunks, headers=None)

        assert download._bytes_downloaded == 0

        # Mock a retry operation with bytes already downloaded in the stream and checksum stored
        offset = 256
        download._bytes_downloaded = offset
        download._expected_checksum = None
        download._checksum_object = _helpers._DoNothingHash()
        download.consume(transport)

        called_kwargs = {
            "data": None,
            "headers": download._headers,
            "timeout": EXPECTED_TIMEOUT,
            "stream": True,
        }
        transport.request.assert_called_once_with("GET", EXAMPLE_URL, **called_kwargs)
        range_bytes = "bytes={:d}-{:d}".format(offset + start, end)
        assert download._headers["range"] == range_bytes

    def test_consume_gzip_reset_stream_w_bytes_downloaded(self):
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")
        end = 65536

        download = download_mod.Download(
            EXAMPLE_URL, stream=stream, end=end, headers=None, checksum="md5"
        )
        transport = mock.Mock(spec=["request"])

        # Mock a decompressive transcoding retry operation with bytes already downloaded in the stream
        headers = {_helpers._STORED_CONTENT_ENCODING_HEADER: "gzip"}
        transport.request.return_value = _mock_response(chunks=chunks, headers=headers)
        offset = 16
        download._bytes_downloaded = offset
        download.consume(transport)

        assert stream.getvalue() == b"".join(chunks)
        assert download._bytes_downloaded == len(b"".join(chunks))

    def test_consume_gzip_reset_stream_error(self):
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")
        end = 65536

        download = download_mod.Download(
            EXAMPLE_URL, stream=stream, end=end, headers=None, checksum="md5"
        )
        transport = mock.Mock(spec=["request"])

        # Mock a stream seek error while resuming a decompressive transcoding download
        stream.seek = mock.Mock(side_effect=OSError("mock stream seek error"))
        headers = {_helpers._STORED_CONTENT_ENCODING_HEADER: "gzip"}
        transport.request.return_value = _mock_response(chunks=chunks, headers=headers)
        offset = 16
        download._bytes_downloaded = offset
        with pytest.raises(Exception):
            download.consume(transport)


class TestRawDownload(object):
    def test__write_to_stream_no_hash_check(self):
        stream = io.BytesIO()
        download = download_mod.RawDownload(EXAMPLE_URL, stream=stream)

        chunk1 = b"right now, "
        chunk2 = b"but a little later"
        response = _mock_raw_response(chunks=[chunk1, chunk2], headers={})

        ret_val = download._write_to_stream(response)
        assert ret_val is None

        assert stream.getvalue() == chunk1 + chunk2
        assert download._bytes_downloaded == len(chunk1 + chunk2)

        # Check mocks.
        response.__enter__.assert_called_once_with()
        response.__exit__.assert_called_once_with(None, None, None)
        response.raw.stream.assert_called_once_with(
            _request_helpers._SINGLE_GET_CHUNK_SIZE, decode_content=False
        )

    @pytest.mark.parametrize("checksum", ["auto", "md5", "crc32c", None])
    def test__write_to_stream_with_hash_check_success(self, checksum):
        stream = io.BytesIO()
        download = download_mod.RawDownload(
            EXAMPLE_URL, stream=stream, checksum=checksum
        )

        chunk1 = b"first chunk, count starting at 0. "
        chunk2 = b"second chunk, or chunk 1, which is better? "
        chunk3 = b"ordinals and numerals and stuff."
        header_value = "crc32c=qmNCyg==,md5=fPAJHnnoi/+NadyNxT2c2w=="
        headers = {_helpers._HASH_HEADER: header_value}
        response = _mock_raw_response(chunks=[chunk1, chunk2, chunk3], headers=headers)

        ret_val = download._write_to_stream(response)
        assert ret_val is None

        assert stream.getvalue() == chunk1 + chunk2 + chunk3
        assert download._bytes_downloaded == len(chunk1 + chunk2 + chunk3)
        assert download._checksum_object is not None

        # Check mocks.
        response.__enter__.assert_called_once_with()
        response.__exit__.assert_called_once_with(None, None, None)
        response.raw.stream.assert_called_once_with(
            _request_helpers._SINGLE_GET_CHUNK_SIZE, decode_content=False
        )

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test__write_to_stream_with_hash_check_fail(self, checksum):
        stream = io.BytesIO()
        download = download_mod.RawDownload(
            EXAMPLE_URL, stream=stream, checksum=checksum
        )

        chunk1 = b"first chunk, count starting at 0. "
        chunk2 = b"second chunk, or chunk 1, which is better? "
        chunk3 = b"ordinals and numerals and stuff."
        bad_checksum = "d3JvbmcgbiBtYWRlIHVwIQ=="
        header_value = "crc32c={bad},md5={bad}".format(bad=bad_checksum)
        headers = {_helpers._HASH_HEADER: header_value}
        response = _mock_raw_response(chunks=[chunk1, chunk2, chunk3], headers=headers)

        with pytest.raises(DataCorruption) as exc_info:
            download._write_to_stream(response)

        assert not download.finished

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 1
        if checksum == "md5":
            good_checksum = "fPAJHnnoi/+NadyNxT2c2w=="
        else:
            good_checksum = "qmNCyg=="
        msg = download_mod._CHECKSUM_MISMATCH.format(
            EXAMPLE_URL, bad_checksum, good_checksum, checksum_type=checksum.upper()
        )
        assert msg in error.args[0]
        assert (
            f"The download request read {download._bytes_downloaded} bytes of data."
            in error.args[0]
        )

        # Check mocks.
        response.__enter__.assert_called_once_with()
        response.__exit__.assert_called_once_with(None, None, None)
        response.raw.stream.assert_called_once_with(
            _request_helpers._SINGLE_GET_CHUNK_SIZE, decode_content=False
        )

    def test__write_to_stream_with_invalid_checksum_type(self):
        BAD_CHECKSUM_TYPE = "badsum"

        stream = io.BytesIO()
        download = download_mod.RawDownload(
            EXAMPLE_URL, stream=stream, checksum=BAD_CHECKSUM_TYPE
        )

        chunk1 = b"first chunk, count starting at 0. "
        chunk2 = b"second chunk, or chunk 1, which is better? "
        chunk3 = b"ordinals and numerals and stuff."
        bad_checksum = "d3JvbmcgbiBtYWRlIHVwIQ=="
        header_value = "crc32c={bad},md5={bad}".format(bad=bad_checksum)
        headers = {_helpers._HASH_HEADER: header_value}
        response = _mock_response(chunks=[chunk1, chunk2, chunk3], headers=headers)

        with pytest.raises(ValueError) as exc_info:
            download._write_to_stream(response)

        assert not download.finished

        error = exc_info.value
        assert error.args[0] == "checksum must be ``'md5'``, ``'crc32c'`` or ``None``"

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test__write_to_stream_incomplete_read(self, checksum):
        stream = io.BytesIO()
        download = download_mod.RawDownload(
            EXAMPLE_URL, stream=stream, checksum=checksum
        )

        chunk1 = b"first chunk"
        mock_full_content_length = len(chunk1) + 123
        headers = {"x-goog-stored-content-length": mock_full_content_length}
        bad_checksum = "d3JvbmcgbiBtYWRlIHVwIQ=="
        header_value = "crc32c={bad},md5={bad}".format(bad=bad_checksum)
        headers[_helpers._HASH_HEADER] = header_value
        response = _mock_raw_response(chunks=[chunk1], headers=headers)

        with pytest.raises(ConnectionError) as exc_info:
            download._write_to_stream(response)

        assert not download.finished
        error = exc_info.value
        assert (
            f"The download request read {download._bytes_downloaded} bytes of data."
            in error.args[0]
        )

    def test__write_to_stream_single_shot_download(self):
        stream = io.BytesIO()
        download = download_mod.RawDownload(
            EXAMPLE_URL, stream=stream, single_shot_download=True
        )

        chunk1 = b"all at once, raw!"
        response = _mock_raw_response(chunks=[chunk1], headers={})
        ret_val = download._write_to_stream(response)

        assert ret_val is None
        assert stream.getvalue() == chunk1
        assert download._bytes_downloaded == len(chunk1)

        response.__enter__.assert_called_once_with()
        response.__exit__.assert_called_once_with(None, None, None)
        response.raw.read.assert_called_once_with()

    def _consume_helper(
        self,
        stream=None,
        end=65536,
        headers=None,
        chunks=(),
        response_headers=None,
        checksum=None,
        timeout=None,
    ):
        download = download_mod.RawDownload(
            EXAMPLE_URL, stream=stream, end=end, headers=headers, checksum=checksum
        )
        transport = mock.Mock(spec=["request"])
        transport.request.return_value = _mock_raw_response(
            chunks=chunks, headers=response_headers
        )

        assert not download.finished

        if timeout is not None:
            ret_val = download.consume(transport, timeout=timeout)
        else:
            ret_val = download.consume(transport)

        assert ret_val is transport.request.return_value

        if chunks:
            assert stream is not None
        transport.request.assert_called_once_with(
            "GET",
            EXAMPLE_URL,
            data=None,
            headers=download._headers,
            stream=True,
            timeout=EXPECTED_TIMEOUT if timeout is None else timeout,
        )

        range_bytes = "bytes={:d}-{:d}".format(0, end)
        assert download._headers["range"] == range_bytes
        assert download.finished

        return transport

    def test_consume(self):
        self._consume_helper()

    def test_consume_with_custom_timeout(self):
        self._consume_helper(timeout=14.7)

    @pytest.mark.parametrize("checksum", ["auto", "md5", "crc32c", None])
    def test_consume_with_stream(self, checksum):
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")
        transport = self._consume_helper(
            stream=stream, chunks=chunks, checksum=checksum
        )

        assert stream.getvalue() == b"".join(chunks)

        # Check mocks.
        response = transport.request.return_value
        response.__enter__.assert_called_once_with()
        response.__exit__.assert_called_once_with(None, None, None)
        response.raw.stream.assert_called_once_with(
            _request_helpers._SINGLE_GET_CHUNK_SIZE, decode_content=False
        )

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test_consume_with_stream_hash_check_success(self, checksum):
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")
        header_value = "crc32c=UNIQxg==,md5=JvS1wjMvfbCXgEGeaJJLDQ=="
        headers = {_helpers._HASH_HEADER: header_value}
        transport = self._consume_helper(
            stream=stream, chunks=chunks, response_headers=headers, checksum=checksum
        )

        assert stream.getvalue() == b"".join(chunks)

        # Check mocks.
        response = transport.request.return_value
        response.__enter__.assert_called_once_with()
        response.__exit__.assert_called_once_with(None, None, None)
        response.raw.stream.assert_called_once_with(
            _request_helpers._SINGLE_GET_CHUNK_SIZE, decode_content=False
        )

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test_consume_with_stream_hash_check_fail(self, checksum):
        stream = io.BytesIO()
        download = download_mod.RawDownload(
            EXAMPLE_URL, stream=stream, checksum=checksum
        )

        chunks = (b"zero zero", b"niner tango")
        bad_checksum = "anVzdCBub3QgdGhpcyAxLA=="
        header_value = "crc32c={bad},md5={bad}".format(bad=bad_checksum)
        headers = {_helpers._HASH_HEADER: header_value}
        transport = mock.Mock(spec=["request"])
        transport.request.return_value = _mock_raw_response(
            chunks=chunks, headers=headers
        )

        assert not download.finished
        with pytest.raises(DataCorruption) as exc_info:
            download.consume(transport)

        assert stream.getvalue() == b"".join(chunks)
        assert download.finished
        assert download._headers == {}

        error = exc_info.value
        assert error.response is transport.request.return_value
        assert len(error.args) == 1
        if checksum == "md5":
            good_checksum = "1A/dxEpys717C6FH7FIWDw=="
        else:
            good_checksum = "GvNZlg=="
        msg = download_mod._CHECKSUM_MISMATCH.format(
            EXAMPLE_URL, bad_checksum, good_checksum, checksum_type=checksum.upper()
        )
        assert msg in error.args[0]
        assert (
            f"The download request read {download._bytes_downloaded} bytes of data."
            in error.args[0]
        )

        # Check mocks.
        transport.request.assert_called_once_with(
            "GET",
            EXAMPLE_URL,
            data=None,
            headers={},
            stream=True,
            timeout=EXPECTED_TIMEOUT,
        )

    def test_consume_with_headers(self):
        headers = {}  # Empty headers
        end = 16383
        self._consume_helper(end=end, headers=headers)
        range_bytes = "bytes={:d}-{:d}".format(0, end)
        # Make sure the headers have been modified.
        assert headers == {"range": range_bytes}

    def test_consume_gets_generation_from_url(self):
        GENERATION_VALUE = 1641590104888641
        url = EXAMPLE_URL + f"&generation={GENERATION_VALUE}"
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")

        download = download_mod.RawDownload(
            url, stream=stream, end=65536, headers=None, checksum="md5"
        )
        transport = mock.Mock(spec=["request"])
        transport.request.return_value = _mock_raw_response(chunks=chunks, headers=None)

        assert not download.finished
        assert download._object_generation is None

        ret_val = download.consume(transport)

        assert download._object_generation == GENERATION_VALUE
        assert ret_val is transport.request.return_value
        assert stream.getvalue() == b"".join(chunks)

        called_kwargs = {
            "data": None,
            "headers": download._headers,
            "timeout": EXPECTED_TIMEOUT,
            "stream": True,
        }
        transport.request.assert_called_once_with("GET", url, **called_kwargs)

    def test_consume_gets_generation_from_headers(self):
        GENERATION_VALUE = 1641590104888641
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")

        download = download_mod.RawDownload(
            EXAMPLE_URL, stream=stream, end=65536, headers=None, checksum="md5"
        )
        transport = mock.Mock(spec=["request"])
        headers = {_helpers._GENERATION_HEADER: GENERATION_VALUE}
        transport.request.return_value = _mock_raw_response(
            chunks=chunks, headers=headers
        )

        assert not download.finished
        assert download._object_generation is None

        ret_val = download.consume(transport)

        assert download._object_generation == GENERATION_VALUE
        assert ret_val is transport.request.return_value
        assert stream.getvalue() == b"".join(chunks)

        called_kwargs = {
            "data": None,
            "headers": download._headers,
            "timeout": EXPECTED_TIMEOUT,
            "stream": True,
        }
        transport.request.assert_called_once_with("GET", EXAMPLE_URL, **called_kwargs)

    def test_consume_w_object_generation(self):
        GENERATION_VALUE = 1641590104888641
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")
        end = 65536

        download = download_mod.RawDownload(
            EXAMPLE_URL, stream=stream, end=end, headers=None, checksum="md5"
        )
        transport = mock.Mock(spec=["request"])
        transport.request.return_value = _mock_raw_response(chunks=chunks, headers=None)

        assert download._object_generation is None

        # Mock a retry operation with object generation retrieved and bytes already downloaded in the stream
        download._object_generation = GENERATION_VALUE
        offset = 256
        download._bytes_downloaded = offset
        download.consume(transport)

        expected_url = EXAMPLE_URL + f"&generation={GENERATION_VALUE}"
        called_kwargs = {
            "data": None,
            "headers": download._headers,
            "timeout": EXPECTED_TIMEOUT,
            "stream": True,
        }
        transport.request.assert_called_once_with("GET", expected_url, **called_kwargs)
        range_bytes = "bytes={:d}-{:d}".format(offset, end)
        assert download._headers["range"] == range_bytes

    def test_consume_w_bytes_downloaded(self):
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")
        end = 65536

        download = download_mod.RawDownload(
            EXAMPLE_URL, stream=stream, end=end, headers=None, checksum="md5"
        )
        transport = mock.Mock(spec=["request"])
        transport.request.return_value = _mock_raw_response(chunks=chunks, headers=None)

        assert download._bytes_downloaded == 0

        # Mock a retry operation with bytes already downloaded in the stream and checksum stored
        offset = 256
        download._bytes_downloaded = offset
        download._expected_checksum = None
        download._checksum_object = _helpers._DoNothingHash()
        download.consume(transport)

        called_kwargs = {
            "data": None,
            "headers": download._headers,
            "timeout": EXPECTED_TIMEOUT,
            "stream": True,
        }
        transport.request.assert_called_once_with("GET", EXAMPLE_URL, **called_kwargs)
        range_bytes = "bytes={:d}-{:d}".format(offset, end)
        assert download._headers["range"] == range_bytes

    def test_consume_w_bytes_downloaded_range_read(self):
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")
        start = 1024
        end = 65536

        download = download_mod.RawDownload(
            EXAMPLE_URL,
            stream=stream,
            start=start,
            end=end,
            headers=None,
            checksum="md5",
        )
        transport = mock.Mock(spec=["request"])
        transport.request.return_value = _mock_raw_response(chunks=chunks, headers=None)

        assert download._bytes_downloaded == 0

        # Mock a retry operation with bytes already downloaded in the stream and checksum stored
        offset = 256
        download._bytes_downloaded = offset
        download._expected_checksum = None
        download._checksum_object = _helpers._DoNothingHash()
        download.consume(transport)

        called_kwargs = {
            "data": None,
            "headers": download._headers,
            "timeout": EXPECTED_TIMEOUT,
            "stream": True,
        }
        transport.request.assert_called_once_with("GET", EXAMPLE_URL, **called_kwargs)
        range_bytes = "bytes={:d}-{:d}".format(start + offset, end)
        assert download._headers["range"] == range_bytes

    def test_consume_gzip_reset_stream_w_bytes_downloaded(self):
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")
        end = 65536

        download = download_mod.RawDownload(
            EXAMPLE_URL, stream=stream, end=end, headers=None, checksum="md5"
        )
        transport = mock.Mock(spec=["request"])

        # Mock a decompressive transcoding retry operation with bytes already downloaded in the stream
        headers = {_helpers._STORED_CONTENT_ENCODING_HEADER: "gzip"}
        transport.request.return_value = _mock_raw_response(
            chunks=chunks, headers=headers
        )
        offset = 16
        download._bytes_downloaded = offset
        download.consume(transport)

        assert stream.getvalue() == b"".join(chunks)
        assert download._bytes_downloaded == len(b"".join(chunks))

    def test_consume_gzip_reset_stream_error(self):
        stream = io.BytesIO()
        chunks = (b"up down ", b"charlie ", b"brown")
        end = 65536

        download = download_mod.RawDownload(
            EXAMPLE_URL, stream=stream, end=end, headers=None, checksum="md5"
        )
        transport = mock.Mock(spec=["request"])

        # Mock a stream seek error while resuming a decompressive transcoding download
        stream.seek = mock.Mock(side_effect=OSError("mock stream seek error"))
        headers = {_helpers._STORED_CONTENT_ENCODING_HEADER: "gzip"}
        transport.request.return_value = _mock_raw_response(
            chunks=chunks, headers=headers
        )
        offset = 16
        download._bytes_downloaded = offset
        with pytest.raises(Exception):
            download.consume(transport)


class TestChunkedDownload(object):
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

    def test_consume_next_chunk_already_finished(self):
        download = download_mod.ChunkedDownload(EXAMPLE_URL, 512, None)
        download._finished = True
        with pytest.raises(ValueError):
            download.consume_next_chunk(None)

    def _mock_transport(self, start, chunk_size, total_bytes, content=b""):
        transport = mock.Mock(spec=["request"])
        assert len(content) == chunk_size
        transport.request.return_value = self._mock_response(
            start,
            start + chunk_size - 1,
            total_bytes,
            content=content,
            status_code=int(http.client.OK),
        )

        return transport

    def test_consume_next_chunk(self):
        start = 1536
        stream = io.BytesIO()
        data = b"Just one chunk."
        chunk_size = len(data)
        download = download_mod.ChunkedDownload(
            EXAMPLE_URL, chunk_size, stream, start=start
        )
        total_bytes = 16384
        transport = self._mock_transport(start, chunk_size, total_bytes, content=data)

        # Verify the internal state before consuming a chunk.
        assert not download.finished
        assert download.bytes_downloaded == 0
        assert download.total_bytes is None
        # Actually consume the chunk and check the output.
        ret_val = download.consume_next_chunk(transport)
        assert ret_val is transport.request.return_value
        range_bytes = "bytes={:d}-{:d}".format(start, start + chunk_size - 1)
        download_headers = {"range": range_bytes}
        transport.request.assert_called_once_with(
            "GET",
            EXAMPLE_URL,
            data=None,
            headers=download_headers,
            timeout=EXPECTED_TIMEOUT,
        )
        assert stream.getvalue() == data
        # Go back and check the internal state after consuming the chunk.
        assert not download.finished
        assert download.bytes_downloaded == chunk_size
        assert download.total_bytes == total_bytes

    def test_consume_next_chunk_with_custom_timeout(self):
        start = 1536
        stream = io.BytesIO()
        data = b"Just one chunk."
        chunk_size = len(data)
        download = download_mod.ChunkedDownload(
            EXAMPLE_URL, chunk_size, stream, start=start
        )
        total_bytes = 16384
        transport = self._mock_transport(start, chunk_size, total_bytes, content=data)

        # Actually consume the chunk and check the output.
        download.consume_next_chunk(transport, timeout=14.7)

        range_bytes = "bytes={:d}-{:d}".format(start, start + chunk_size - 1)
        download_headers = {"range": range_bytes}
        transport.request.assert_called_once_with(
            "GET",
            EXAMPLE_URL,
            data=None,
            headers=download_headers,
            timeout=14.7,
        )


class TestRawChunkedDownload(object):
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
            _content=content,
            headers=response_headers,
            status_code=status_code,
            spec=["_content", "headers", "status_code"],
        )

    def test_consume_next_chunk_already_finished(self):
        download = download_mod.RawChunkedDownload(EXAMPLE_URL, 512, None)
        download._finished = True
        with pytest.raises(ValueError):
            download.consume_next_chunk(None)

    def _mock_transport(self, start, chunk_size, total_bytes, content=b""):
        transport = mock.Mock(spec=["request"])
        assert len(content) == chunk_size
        transport.request.return_value = self._mock_response(
            start,
            start + chunk_size - 1,
            total_bytes,
            content=content,
            status_code=int(http.client.OK),
        )

        return transport

    def test_consume_next_chunk(self):
        start = 1536
        stream = io.BytesIO()
        data = b"Just one chunk."
        chunk_size = len(data)
        download = download_mod.RawChunkedDownload(
            EXAMPLE_URL, chunk_size, stream, start=start
        )
        total_bytes = 16384
        transport = self._mock_transport(start, chunk_size, total_bytes, content=data)

        # Verify the internal state before consuming a chunk.
        assert not download.finished
        assert download.bytes_downloaded == 0
        assert download.total_bytes is None
        # Actually consume the chunk and check the output.
        ret_val = download.consume_next_chunk(transport)
        assert ret_val is transport.request.return_value
        range_bytes = "bytes={:d}-{:d}".format(start, start + chunk_size - 1)
        download_headers = {"range": range_bytes}
        transport.request.assert_called_once_with(
            "GET",
            EXAMPLE_URL,
            data=None,
            headers=download_headers,
            stream=True,
            timeout=EXPECTED_TIMEOUT,
        )
        assert stream.getvalue() == data
        # Go back and check the internal state after consuming the chunk.
        assert not download.finished
        assert download.bytes_downloaded == chunk_size
        assert download.total_bytes == total_bytes

    def test_consume_next_chunk_with_custom_timeout(self):
        start = 1536
        stream = io.BytesIO()
        data = b"Just one chunk."
        chunk_size = len(data)
        download = download_mod.RawChunkedDownload(
            EXAMPLE_URL, chunk_size, stream, start=start
        )
        total_bytes = 16384
        transport = self._mock_transport(start, chunk_size, total_bytes, content=data)

        # Actually consume the chunk and check the output.
        download.consume_next_chunk(transport, timeout=14.7)

        range_bytes = "bytes={:d}-{:d}".format(start, start + chunk_size - 1)
        download_headers = {"range": range_bytes}
        transport.request.assert_called_once_with(
            "GET",
            EXAMPLE_URL,
            data=None,
            headers=download_headers,
            stream=True,
            timeout=14.7,
        )
        assert stream.getvalue() == data
        # Go back and check the internal state after consuming the chunk.
        assert not download.finished
        assert download.bytes_downloaded == chunk_size
        assert download.total_bytes == total_bytes


class Test__add_decoder(object):
    def test_non_gzipped(self):
        response_raw = mock.Mock(headers={}, spec=["headers"])
        md5_hash = download_mod._add_decoder(response_raw, mock.sentinel.md5_hash)

        assert md5_hash is mock.sentinel.md5_hash

    def test_gzipped(self):
        headers = {"content-encoding": "gzip"}
        response_raw = mock.Mock(headers=headers, spec=["headers", "_decoder"])
        md5_hash = download_mod._add_decoder(response_raw, mock.sentinel.md5_hash)

        assert md5_hash is not mock.sentinel.md5_hash
        assert isinstance(md5_hash, _helpers._DoNothingHash)
        assert isinstance(response_raw._decoder, download_mod._GzipDecoder)
        assert response_raw._decoder._checksum is mock.sentinel.md5_hash

    def test_brotli(self):
        headers = {"content-encoding": "br"}
        response_raw = mock.Mock(headers=headers, spec=["headers", "_decoder"])
        md5_hash = download_mod._add_decoder(response_raw, mock.sentinel.md5_hash)

        assert md5_hash is not mock.sentinel.md5_hash
        assert isinstance(md5_hash, _helpers._DoNothingHash)
        assert isinstance(response_raw._decoder, download_mod._BrotliDecoder)
        assert response_raw._decoder._checksum is mock.sentinel.md5_hash
        # Go ahead and exercise the flush method, added only for completion
        response_raw._decoder.flush()


class Test_GzipDecoder(object):
    def test_constructor(self):
        decoder = download_mod._GzipDecoder(mock.sentinel.md5_hash)
        assert decoder._checksum is mock.sentinel.md5_hash

    def test_decompress(self):
        md5_hash = mock.Mock(spec=["update"])
        decoder = download_mod._GzipDecoder(md5_hash)

        data = b"\x1f\x8b\x08\x08"
        result = decoder.decompress(data)

        assert result == b""
        md5_hash.update.assert_called_once_with(data)


class Test_BrotliDecoder(object):
    def test_constructor(self):
        decoder = download_mod._BrotliDecoder(mock.sentinel.md5_hash)
        assert decoder._checksum is mock.sentinel.md5_hash

    def test_decompress(self):
        md5_hash = mock.Mock(spec=["update"])
        decoder = download_mod._BrotliDecoder(md5_hash)

        data = b"\xc1\xf8I\xc0/\x83\xf3\xfa"
        result = decoder.decompress(data)

        assert result == b""
        md5_hash.update.assert_called_once_with(data)


def _mock_response(status_code=http.client.OK, chunks=None, headers=None):
    if headers is None:
        headers = {}

    if chunks is not None:
        mock_raw = mock.Mock(headers=headers, spec=["headers"])
        response = mock.MagicMock(
            headers=headers,
            status_code=int(status_code),
            raw=mock_raw,
            spec=[
                "__enter__",
                "__exit__",
                "iter_content",
                "status_code",
                "headers",
                "raw",
            ],
        )
        # i.e. context manager returns ``self``.
        response.__enter__.return_value = response
        response.__exit__.return_value = None
        response.iter_content.return_value = iter(chunks)
        response.raw.read = mock.Mock(
            side_effect=lambda *args, **kwargs: b"".join(chunks)
        )
        return response
    else:
        return mock.Mock(
            headers=headers,
            status_code=int(status_code),
            spec=["status_code", "headers"],
        )


def _mock_raw_response(status_code=http.client.OK, chunks=(), headers=None):
    if headers is None:
        headers = {}

    mock_raw = mock.Mock(headers=headers, spec=["stream"])
    mock_raw.stream.return_value = iter(chunks)
    mock_raw.read = mock.Mock(return_value=b"".join(chunks))
    response = mock.MagicMock(
        headers=headers,
        status_code=int(status_code),
        raw=mock_raw,
        spec=[
            "__enter__",
            "__exit__",
            "iter_content",
            "status_code",
            "headers",
            "raw",
        ],
    )
    # i.e. context manager returns ``self``.
    response.__enter__.return_value = response
    response.__exit__.return_value = None
    return response
