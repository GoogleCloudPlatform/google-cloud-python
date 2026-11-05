# Copyright 2025 Google LLC
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

import asyncio
import concurrent.futures
from io import BytesIO
from unittest import mock
from unittest.mock import AsyncMock

import google_crc32c
import pytest
from google.api_core import exceptions
from google.rpc import error_details_pb2, status_pb2

from google.cloud import _storage_v2
from google.cloud.storage.asyncio import _zero_copy_bidi_read, async_read_object_stream
from google.cloud.storage.asyncio.async_multi_range_downloader import (
    AsyncMultiRangeDownloader,
)
from google.cloud.storage.asyncio.retry import reads_resumption_strategy
from google.cloud.storage.exceptions import DataCorruption

_TEST_BUCKET_NAME = "test-bucket"
_TEST_OBJECT_NAME = "test-object"
_TEST_OBJECT_SIZE = 1024 * 1024  # 1 MiB
_TEST_GENERATION_NUMBER = 123456789
_TEST_READ_HANDLE = b"test-handle"


def _accept_memoryview_in_crc32c(monkeypatch):
    # Let the installed google-crc32c hash the zero-copy parser's views even if
    # it predates memoryview support, so that is_supported() holds.
    value, update = google_crc32c.value, google_crc32c.Checksum.update
    monkeypatch.setattr(google_crc32c, "value", lambda data: value(bytes(data)))
    monkeypatch.setattr(
        google_crc32c.Checksum, "update", lambda self, data: update(self, bytes(data))
    )


def _zero_copy_response(content, offset, read_id, range_end, crc32c=None):
    return _zero_copy_bidi_read.deserialize(
        _storage_v2.BidiReadObjectResponse.serialize(
            _storage_v2.BidiReadObjectResponse(
                object_data_ranges=[
                    _storage_v2.ObjectRangeData(
                        checksummed_data=_storage_v2.ChecksummedData(
                            content=content,
                            crc32c=google_crc32c.value(content)
                            if crc32c is None
                            else crc32c,
                        ),
                        range_end=range_end,
                        read_range=_storage_v2.ReadRange(
                            read_offset=offset,
                            read_length=len(content),
                            read_id=read_id,
                        ),
                    )
                ]
            )
        )
    )


@pytest.fixture(autouse=True)
def _reprobe_crc32c_memoryview_support(monkeypatch):
    # is_supported() caches its google_crc32c probe; tests below patch
    # google_crc32c.value, so each test must probe afresh.
    monkeypatch.setattr(_zero_copy_bidi_read, "_memoryview_supported", None)


class TestAsyncMultiRangeDownloader:
    @staticmethod
    def _make_mock_client():
        mock_client = mock.MagicMock()
        mock_client.grpc_client = mock.AsyncMock()
        return mock_client

    @staticmethod
    def _make_mock_stream(
        generation=_TEST_GENERATION_NUMBER,
        persisted_size=_TEST_OBJECT_SIZE,
        read_handle=_TEST_READ_HANDLE,
        is_finalized=True,
        open_side_effect=None,
    ):
        s = mock.MagicMock()
        s.open = AsyncMock(side_effect=open_side_effect)
        s.close = AsyncMock()
        s.generation_number = generation
        s.persisted_size = persisted_size
        s.read_handle = read_handle
        s.is_finalized = is_finalized
        s.full_obj_server_crc32c = 12345 if is_finalized else None
        s.object_metadata = mock.Mock()
        return s

    @staticmethod
    def _make_dummy_pooled_stream():
        from google.cloud.storage.asyncio._stream_pool import (
            _PooledStream,
        )

        return _PooledStream(
            mock.MagicMock(close=AsyncMock()),
            mock.MagicMock(close=AsyncMock()),
        )

    def create_read_ranges(self, num_ranges):
        ranges = []
        for i in range(num_ranges):
            ranges.append((i, 1, BytesIO()))
        return ranges

    # helper method
    @pytest.mark.asyncio
    async def _make_mock_mrd(
        self,
        mock_cls_async_read_object_stream,
        bucket_name=_TEST_BUCKET_NAME,
        object_name=_TEST_OBJECT_NAME,
        generation=_TEST_GENERATION_NUMBER,
        read_handle=_TEST_READ_HANDLE,
    ):
        mock_client = mock.MagicMock()
        mock_client.grpc_client = mock.AsyncMock()

        mock_stream = mock_cls_async_read_object_stream.return_value
        mock_stream.open = AsyncMock()
        mock_stream.generation_number = _TEST_GENERATION_NUMBER
        mock_stream.persisted_size = _TEST_OBJECT_SIZE
        mock_stream.read_handle = _TEST_READ_HANDLE
        mock_stream.object_metadata = mock.Mock()

        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client, bucket_name, object_name, generation, read_handle
        )

        return mrd, mock_client

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_create_mrd(self, mock_cls_async_read_object_stream):
        # Arrange & Act
        mrd, mock_client = await self._make_mock_mrd(mock_cls_async_read_object_stream)

        # Assert
        mock_cls_async_read_object_stream.assert_called_once_with(
            client=mock_client.grpc_client,
            bucket_name=_TEST_BUCKET_NAME,
            object_name=_TEST_OBJECT_NAME,
            generation_number=_TEST_GENERATION_NUMBER,
            read_handle=_TEST_READ_HANDLE,
            metrics_recorder=None,
        )

        mrd.read_obj_str.open.assert_called_once()

        assert mrd.client == mock_client
        assert mrd.bucket_name == _TEST_BUCKET_NAME
        assert mrd.object_name == _TEST_OBJECT_NAME
        assert mrd.generation == _TEST_GENERATION_NUMBER
        assert mrd.read_handle == _TEST_READ_HANDLE
        assert mrd.persisted_size == _TEST_OBJECT_SIZE
        assert mrd.is_stream_open
        assert mrd.object_metadata == mrd.read_obj_str.object_metadata
        assert mrd._open_retries == 0

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "zero_copy, accepts_memoryview, expected_type",
        [
            # A write() sink sees a memoryview only when the zero-copy parser
            # is enabled (GCS_PYTHON_CLIENT_ZERO_COPY_BIDI_READ=1) AND the
            # caller opted in; the generated parser always yields bytes.
            (True, True, memoryview),
            (True, False, bytes),
            (False, True, bytes),
            (False, False, bytes),
        ],
    )
    async def test_download_ranges_write_destination_chunk_type(
        self,
        mock_cls_async_read_object_stream,
        mock_random_int,
        monkeypatch,
        zero_copy,
        accepts_memoryview,
        expected_type,
    ):
        _accept_memoryview_in_crc32c(monkeypatch)
        data = b"these_are_18_chars"
        crc32c_int = google_crc32c.value(data)

        mock_mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)
        mock_random_int.side_effect = [456]

        wire = _storage_v2.BidiReadObjectResponse.serialize(
            _storage_v2.BidiReadObjectResponse(
                object_data_ranges=[
                    _storage_v2.ObjectRangeData(
                        checksummed_data=_storage_v2.ChecksummedData(
                            content=data, crc32c=crc32c_int
                        ),
                        range_end=True,
                        read_range=_storage_v2.ReadRange(
                            read_offset=0, read_length=18, read_id=456
                        ),
                    )
                ]
            )
        )
        if zero_copy:
            resp = _zero_copy_bidi_read.deserialize(wire)
            assert isinstance(
                resp.object_data_ranges[0].checksummed_data.content, memoryview
            )
        else:
            resp = _storage_v2.BidiReadObjectResponse.deserialize(wire)

        mock_mrd.read_obj_str.send = AsyncMock()
        mock_mrd.read_obj_str.recv = AsyncMock(side_effect=[resp, None])

        seen_types = []

        class RecordingSink:
            def __init__(self):
                self.chunks = []

            def write(self, chunk):
                seen_types.append(type(chunk))
                self.chunks.append(chunk)
                return len(chunk)

        sink = RecordingSink()
        await mock_mrd.download_ranges(
            [(0, 18, sink)], accepts_memoryview=accepts_memoryview
        )

        assert seen_types == [expected_type]
        assert b"".join(sink.chunks) == data

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_ranges_writes_into_writable_buffer(
        self, mock_cls_async_read_object_stream, mock_random_int, monkeypatch
    ):
        from google.cloud.storage.asyncio import _zero_copy_bidi_read

        _accept_memoryview_in_crc32c(monkeypatch)
        data = b"these_are_18_chars"
        crc1 = google_crc32c.value(data[:10])
        crc2 = google_crc32c.value(data[10:])

        mock_mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)
        mock_random_int.side_effect = [456, 789]

        resp = _zero_copy_bidi_read.deserialize(
            _storage_v2.BidiReadObjectResponse.serialize(
                _storage_v2.BidiReadObjectResponse(
                    object_data_ranges=[
                        _storage_v2.ObjectRangeData(
                            checksummed_data=_storage_v2.ChecksummedData(
                                content=data[:10], crc32c=crc1
                            ),
                            range_end=False,
                            read_range=_storage_v2.ReadRange(
                                read_offset=0, read_length=10, read_id=456
                            ),
                        ),
                        _storage_v2.ObjectRangeData(
                            checksummed_data=_storage_v2.ChecksummedData(
                                content=data[10:], crc32c=crc2
                            ),
                            range_end=True,
                            read_range=_storage_v2.ReadRange(
                                read_offset=10, read_length=8, read_id=456
                            ),
                        ),
                        _storage_v2.ObjectRangeData(
                            checksummed_data=_storage_v2.ChecksummedData(
                                content=data[10:], crc32c=crc2
                            ),
                            range_end=True,
                            read_range=_storage_v2.ReadRange(
                                read_offset=10, read_length=8, read_id=789
                            ),
                        ),
                    ]
                )
            )
        )
        mock_mrd.read_obj_str.send = AsyncMock()
        mock_mrd.read_obj_str.recv = AsyncMock(side_effect=[resp, None])

        raw = bytearray(18)
        backing = bytearray(b"." * 12)
        slice_view = memoryview(backing)[2:10]

        await mock_mrd.download_ranges([(0, 18, raw), (10, 8, slice_view)])

        assert bytes(raw) == data
        assert bytes(backing) == b".." + data[10:] + b".."

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "length, buf, match",
        [
            (0, bytearray(10), "requires bytes_to_read > 0"),
            (4, memoryview(b"abcd"), "writable, C-contiguous"),
            (4, memoryview(bytearray(8))[::2], "writable, C-contiguous"),
            (10, bytearray(4), "smaller than bytes_to_read"),
        ],
    )
    async def test_download_ranges_rejects_invalid_writable_buffer(
        self, mock_cls_async_read_object_stream, length, buf, match
    ):
        mock_mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)
        with pytest.raises(ValueError, match=match):
            await mock_mrd.download_ranges([(0, length, buf)])

    def test_buffer_destination_rejects_chunk_past_bytes_to_read(self):
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            _BufferWriter,
        )

        # A buffer may be larger than bytes_to_read; bytes past the range are
        # never written, even if a chunk runs past it.
        buffer = bytearray(b"." * 8)
        writer = _BufferWriter(buffer, 4)
        writer.write(b"ab")
        with pytest.raises(ValueError):
            writer.write(b"cde")
        assert bytes(buffer) == b"ab......"

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    @pytest.mark.parametrize("initial", [b"\0" * 10, b"B" * 20])
    async def test_download_ranges_rejects_chunk_past_bytes_to_read(
        self,
        mock_cls_async_read_object_stream,
        mock_random_int,
        monkeypatch,
        initial,
    ):
        # The server sends 12 bytes for a 10-byte range, in a message that is
        # not the range's last one.
        _accept_memoryview_in_crc32c(monkeypatch)
        mock_mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)
        mock_random_int.side_effect = [456]
        response = _zero_copy_response(b"A" * 12, 0, 456, False)
        assert isinstance(
            response.object_data_ranges[0].checksummed_data.content, memoryview
        )
        mock_mrd.read_obj_str.send = AsyncMock()
        mock_mrd.read_obj_str.close = AsyncMock()
        mock_mrd.read_obj_str.recv = AsyncMock(side_effect=[response, None])
        buffer = bytearray(initial)

        with pytest.raises(DataCorruption, match="Byte count mismatch"):
            await mock_mrd.download_ranges([(0, 10, buffer)])

        assert bytes(buffer) == initial
        assert not mock_mrd.is_stream_open

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_ranges_raises_on_short_read_into_buffer(
        self, mock_cls_async_read_object_stream, mock_random_int, monkeypatch
    ):
        # GCS clamps reads extending past EOF and closes the range after the
        # remaining bytes; a fixed buffer destination has no cursor or return
        # count, so unwritten tail bytes must not be left unnoticed.
        _accept_memoryview_in_crc32c(monkeypatch)
        mock_mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)
        mock_random_int.side_effect = [456]
        response = _zero_copy_response(b"6789", 6, 456, True)
        assert isinstance(
            response.object_data_ranges[0].checksummed_data.content, memoryview
        )
        mock_mrd.read_obj_str.send = AsyncMock()
        mock_mrd.read_obj_str.close = AsyncMock()
        mock_mrd.read_obj_str.recv = AsyncMock(side_effect=[response, None])
        buffer = bytearray(b"STALE_TAIL")

        with pytest.raises(
            BufferError, match="expected 10 bytes at offset 6, got 4"
        ) as exc_info:
            await mock_mrd.download_ranges([(6, 10, buffer)])

        assert mock_mrd.is_stream_open
        mock_mrd.read_obj_str.close.assert_not_awaited()
        # exc_info.tb still references download_ranges' frame here.
        assert exc_info.tb is not None
        buffer.clear()

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_ranges_allows_short_read_into_write_destination(
        self, mock_cls_async_read_object_stream, mock_random_int, monkeypatch
    ):
        _accept_memoryview_in_crc32c(monkeypatch)
        mock_mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)
        mock_random_int.side_effect = [456]
        response = _zero_copy_response(b"6789", 6, 456, True)
        mock_mrd.read_obj_str.send = AsyncMock()
        mock_mrd.read_obj_str.recv = AsyncMock(side_effect=[response, None])
        chunks = []

        class RecordingSink:
            def write(self, chunk):
                chunks.append((type(chunk), bytes(chunk)))
                return len(chunk)

        await mock_mrd.download_ranges(
            [(6, 10, RecordingSink())], accepts_memoryview=True
        )

        assert chunks == [(memoryview, b"6789")]

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_ranges_releases_buffer_when_a_later_range_is_invalid(
        self, mock_cls_async_read_object_stream
    ):
        mock_mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)
        buffer = bytearray(4)

        with pytest.raises(ValueError) as exc_info:
            await mock_mrd.download_ranges([(0, 4, buffer), (0, 0, bytearray(4))])
        # exc_info.tb still references download_ranges' frame here.
        assert exc_info.tb is not None
        buffer.clear()

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_ranges_checksum_mismatch_into_buffer(
        self, mock_cls_async_read_object_stream, mock_random_int, monkeypatch
    ):
        _accept_memoryview_in_crc32c(monkeypatch)
        mock_mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)
        mock_random_int.side_effect = [456]
        response = _zero_copy_response(b"x" * 18, 0, 456, True, crc32c=12345)
        assert isinstance(
            response.object_data_ranges[0].checksummed_data.content, memoryview
        )
        mock_mrd.read_obj_str.send = AsyncMock()
        mock_mrd.read_obj_str.close = AsyncMock()
        mock_mrd.read_obj_str.recv = AsyncMock(side_effect=[response, None])
        buffer = bytearray(18)

        with pytest.raises(DataCorruption) as exc_info:
            await mock_mrd.download_ranges([(0, 18, buffer)])
        assert bytes(buffer) == bytes(18)
        assert not mock_mrd.is_stream_open
        # exc_info.tb still references download_ranges' frame here.
        assert exc_info.tb is not None
        buffer.clear()

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_ranges_resumes_into_buffer_after_retry(
        self, mock_cls_async_read_object_stream, mock_random_int, monkeypatch
    ):
        _accept_memoryview_in_crc32c(monkeypatch)
        data = b"these_are_18_chars"
        mock_mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)
        mock_random_int.return_value = 456

        first_chunk = _zero_copy_response(data[:10], 0, 456, False)
        second_chunk = _zero_copy_response(data[10:], 10, 456, True)
        assert isinstance(
            first_chunk.object_data_ranges[0].checksummed_data.content, memoryview
        )
        assert isinstance(
            second_chunk.object_data_ranges[0].checksummed_data.content, memoryview
        )

        first_stream = mock_mrd.read_obj_str
        first_stream.send = AsyncMock()
        first_stream.close = AsyncMock()
        first_stream.is_stream_open = True
        first_stream.recv = AsyncMock(
            side_effect=[
                first_chunk,
                exceptions.Aborted("Idle stream has been closed."),
            ]
        )
        second_stream = mock.MagicMock()
        second_stream.open = AsyncMock()
        second_stream.send = AsyncMock()
        second_stream.close = AsyncMock()
        second_stream.recv = AsyncMock(side_effect=[second_chunk])
        mock_cls_async_read_object_stream.side_effect = [second_stream]
        buffer = bytearray(18)

        await mock_mrd.download_ranges([(0, 18, buffer)])

        assert bytes(buffer) == data
        second_stream.open.assert_awaited_once()
        second_stream.send.assert_awaited_once_with(
            _storage_v2.BidiReadObjectRequest(
                read_ranges=[
                    _storage_v2.ReadRange(read_offset=10, read_length=8, read_id=456)
                ]
            )
        )

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "length, make_destination",
        [(0, BytesIO), (18, lambda: bytearray(18))],
    )
    async def test_download_ranges_full_object_read_of_zero_copy_chunks(
        self,
        mock_cls_async_read_object_stream,
        mock_random_int,
        monkeypatch,
        length,
        make_destination,
    ):
        # Full-object reads also feed every chunk to Checksum.update.
        _accept_memoryview_in_crc32c(monkeypatch)
        destination = make_destination()
        data = b"these_are_18_chars"
        mock_mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)
        mock_mrd.persisted_size = len(data)
        mock_mrd.full_obj_server_crc32c = google_crc32c.value(data)
        mock_random_int.side_effect = [456]
        response = _zero_copy_response(data, 0, 456, True)
        assert isinstance(
            response.object_data_ranges[0].checksummed_data.content, memoryview
        )
        mock_mrd.read_obj_str.send = AsyncMock()
        mock_mrd.read_obj_str.recv = AsyncMock(side_effect=[response, None])

        await mock_mrd.download_ranges([(0, length, destination)], enable_checksum=True)

        written = (
            destination.getvalue()
            if isinstance(destination, BytesIO)
            else bytes(destination)
        )
        assert written == data

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_ranges_verifies_parser_output_with_installed_crc32c(
        self, mock_cls_async_read_object_stream, mock_random_int
    ):
        # Deliberately no monkeypatch of google_crc32c or is_supported: the
        # chunks the parser hands out (memoryview or bytes, depending on the
        # installed google-crc32c) must verify as-is, including the content-less
        # final message of a range that ends on a chunk boundary.
        from google.cloud.storage.asyncio import _zero_copy_bidi_read

        data = b"these_are_18_chars"
        mock_mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)
        mock_random_int.side_effect = [456, 789]

        def response(content, offset, range_end):
            return _zero_copy_bidi_read.deserialize(
                _storage_v2.BidiReadObjectResponse.serialize(
                    _storage_v2.BidiReadObjectResponse(
                        object_data_ranges=[
                            _storage_v2.ObjectRangeData(
                                checksummed_data=_storage_v2.ChecksummedData(
                                    content=content,
                                    crc32c=google_crc32c.value(content),
                                ),
                                range_end=range_end,
                                read_range=_storage_v2.ReadRange(
                                    read_offset=offset,
                                    read_length=len(content),
                                    read_id=read_id,
                                ),
                            )
                            for read_id in (456, 789)
                        ]
                    )
                )
            )

        mock_mrd.read_obj_str.send = AsyncMock()
        mock_mrd.read_obj_str.recv = AsyncMock(
            side_effect=[response(data, 0, False), response(b"", 18, True), None]
        )

        sink = BytesIO()
        raw = bytearray(18)
        await mock_mrd.download_ranges([(0, 18, sink), (0, 18, raw)])

        assert sink.getvalue() == data
        assert bytes(raw) == data

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_ranges_via_async_gather(
        self, mock_cls_async_read_object_stream, mock_random_int
    ):
        data = b"these_are_18_chars"
        crc32c_int = google_crc32c.value(data)
        crc32c_checksum_for_data_slice = google_crc32c.value(data[10:16])

        mock_mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)
        mock_random_int.side_effect = [456, 91011]

        send_count = 0
        both_sent = asyncio.Event()

        async def counting_send(request):
            nonlocal send_count
            send_count += 1
            if send_count >= 2:
                both_sent.set()

        mock_mrd.read_obj_str.send = AsyncMock(side_effect=counting_send)

        recv_call_count = 0

        async def controlled_recv():
            nonlocal recv_call_count
            recv_call_count += 1
            if recv_call_count == 1:
                await both_sent.wait()
                return _storage_v2.BidiReadObjectResponse(
                    object_data_ranges=[
                        _storage_v2.ObjectRangeData(
                            checksummed_data=_storage_v2.ChecksummedData(
                                content=data, crc32c=crc32c_int
                            ),
                            range_end=True,
                            read_range=_storage_v2.ReadRange(
                                read_offset=0, read_length=18, read_id=456
                            ),
                        )
                    ]
                )
            elif recv_call_count == 2:
                return _storage_v2.BidiReadObjectResponse(
                    object_data_ranges=[
                        _storage_v2.ObjectRangeData(
                            checksummed_data=_storage_v2.ChecksummedData(
                                content=data[10:16],
                                crc32c=crc32c_checksum_for_data_slice,
                            ),
                            range_end=True,
                            read_range=_storage_v2.ReadRange(
                                read_offset=10, read_length=6, read_id=91011
                            ),
                        )
                    ],
                )
            return None

        mock_mrd.read_obj_str.recv = AsyncMock(side_effect=controlled_recv)

        buffer = BytesIO()
        second_buffer = BytesIO()

        task1 = asyncio.create_task(mock_mrd.download_ranges([(0, 18, buffer)]))
        task2 = asyncio.create_task(mock_mrd.download_ranges([(10, 6, second_buffer)]))
        await asyncio.gather(task1, task2)

        assert buffer.getvalue() == data
        assert second_buffer.getvalue() == data[10:16]

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_ranges(
        self, mock_cls_async_read_object_stream, mock_random_int
    ):
        # Arrange
        data = b"these_are_18_chars"
        crc32c_int = google_crc32c.value(data)

        mock_mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)
        mock_random_int.side_effect = [456]

        mock_mrd.read_obj_str.send = AsyncMock()
        mock_mrd.read_obj_str.recv = AsyncMock()
        mock_mrd.read_obj_str.recv.side_effect = [
            _storage_v2.BidiReadObjectResponse(
                object_data_ranges=[
                    _storage_v2.ObjectRangeData(
                        checksummed_data=_storage_v2.ChecksummedData(
                            content=data, crc32c=crc32c_int
                        ),
                        range_end=True,
                        read_range=_storage_v2.ReadRange(
                            read_offset=0, read_length=18, read_id=456
                        ),
                    )
                ],
            ),
            None,
        ]
        # Act
        buffer = BytesIO()

        await mock_mrd.download_ranges([(0, 18, buffer)])

        # Assert
        mock_mrd.read_obj_str.send.assert_called_once_with(
            _storage_v2.BidiReadObjectRequest(
                read_ranges=[
                    _storage_v2.ReadRange(read_offset=0, read_length=18, read_id=456)
                ]
            )
        )
        assert buffer.getvalue() == data

    @pytest.mark.asyncio
    async def test_downloading_ranges_with_more_than_1000_should_throw_error(self):
        # Arrange
        mock_client = mock.MagicMock()
        mrd = AsyncMultiRangeDownloader(
            mock_client, _TEST_BUCKET_NAME, _TEST_OBJECT_NAME
        )

        # Act + Assert
        with pytest.raises(ValueError) as exc:
            await mrd.download_ranges(self.create_read_ranges(1001))

        # Assert
        assert (
            str(exc.value)
            == "Invalid input - length of read_ranges cannot be more than 1000"
        )

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_opening_mrd_more_than_once_should_throw_error(
        self, mock_cls_async_read_object_stream
    ):
        # Arrange
        mrd, _ = await self._make_mock_mrd(
            mock_cls_async_read_object_stream
        )  # mock mrd is already opened

        # Act + Assert
        with pytest.raises(ValueError) as exc:
            await mrd.open()

        # Assert
        assert str(exc.value) == "Underlying bidi-gRPC stream is already open"

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_close_mrd(self, mock_cls_async_read_object_stream):
        # Arrange
        mrd, _ = await self._make_mock_mrd(
            mock_cls_async_read_object_stream
        )  # mock mrd is already opened
        mrd.read_obj_str.close = AsyncMock()

        # Act
        await mrd.close()

        # Assert
        assert not mrd.is_stream_open
        assert mrd.object_metadata is None

    @pytest.mark.asyncio
    async def test_close_mrd_not_opened_should_throw_error(self):
        # Arrange
        mock_client = mock.MagicMock()
        mrd = AsyncMultiRangeDownloader(
            mock_client, _TEST_BUCKET_NAME, _TEST_OBJECT_NAME
        )
        # Act + Assert
        with pytest.raises(ValueError) as exc:
            await mrd.close()

        # Assert
        assert str(exc.value) == "Underlying bidi-gRPC stream is not open"
        assert not mrd.is_stream_open

    @pytest.mark.asyncio
    async def test_downloading_without_opening_should_throw_error(self):
        # Arrange
        mock_client = mock.MagicMock()
        mrd = AsyncMultiRangeDownloader(
            mock_client, _TEST_BUCKET_NAME, _TEST_OBJECT_NAME
        )

        # Act + Assert
        with pytest.raises(ValueError) as exc:
            await mrd.download_ranges([(0, 18, BytesIO())])

        # Assert
        assert str(exc.value) == "Underlying bidi-gRPC stream is not open"
        assert not mrd.is_stream_open

    @mock.patch("google.cloud.storage.asyncio._utils.google_crc32c")
    @pytest.mark.asyncio
    async def test_download_ranges_raises_if_crc32c_c_extension_is_missing(
        self, mock_google_crc32c
    ):
        mock_google_crc32c.implementation = "python"
        mock_client = mock.MagicMock()
        mrd = AsyncMultiRangeDownloader(mock_client, "bucket", "object")

        with pytest.raises(exceptions.FailedPrecondition) as exc_info:
            await mrd.download_ranges([(0, 10, BytesIO())])

        assert "The google-crc32c package is not installed with C support" in str(
            exc_info.value
        )

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "test_data",
        [
            pytest.param(b"some-data", id="inline"),
            pytest.param(
                b"x" * reads_resumption_strategy._CRC32C_OFFLOAD_MIN_BYTES,
                id="offloaded",
            ),
        ],
    )
    @mock.patch(
        "google.cloud.storage.asyncio.retry.reads_resumption_strategy.google_crc32c.value"
    )
    async def test_download_ranges_raises_on_checksum_mismatch(
        self, mock_crc32c_value, test_data
    ):
        from google.cloud.storage.asyncio._stream_multiplexer import _StreamMultiplexer
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            AsyncMultiRangeDownloader,
        )

        mock_client = mock.MagicMock()
        mock_stream = mock.AsyncMock(
            spec=async_read_object_stream._AsyncReadObjectStream
        )

        server_checksum = 12345
        mock_crc32c_value.return_value = 54321

        mock_response = _storage_v2.BidiReadObjectResponse(
            object_data_ranges=[
                _storage_v2.ObjectRangeData(
                    checksummed_data=_storage_v2.ChecksummedData(
                        content=test_data, crc32c=server_checksum
                    ),
                    read_range=_storage_v2.ReadRange(
                        read_id=0, read_offset=0, read_length=len(test_data)
                    ),
                    range_end=True,
                )
            ]
        )

        mock_stream.recv.side_effect = [mock_response, None]

        mrd = AsyncMultiRangeDownloader(mock_client, "bucket", "object")
        mrd.read_obj_str = mock_stream
        mrd._is_stream_open = True
        mrd._multiplexer = _StreamMultiplexer(mock_stream)

        buffer = BytesIO()
        with pytest.raises(DataCorruption) as exc_info:
            with mock.patch(
                "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer",
                return_value=0,
            ):
                await mrd.download_ranges([(0, len(test_data), buffer)])

        assert "Checksum mismatch" in str(exc_info.value)
        mock_crc32c_value.assert_called_once_with(test_data)
        assert buffer.getvalue() == b""

    def _mrd_with_held_chunk(self, content, recv_after_chunk):
        """An MRD whose stream sends one offloaded chunk of ``content`` (whose
        checksum future is returned) and then awaits ``recv_after_chunk()``."""
        from google.cloud.storage.asyncio._stream_multiplexer import _StreamMultiplexer

        future = concurrent.futures.Future()
        submitted = asyncio.Event()

        def submit(fn, data):
            submitted.set()
            return future

        executor = mock.Mock()
        executor.submit.side_effect = submit
        patcher = mock.patch.object(
            reads_resumption_strategy, "_crc32c_executor", executor
        )
        response = _storage_v2.BidiReadObjectResponse(
            object_data_ranges=[
                _storage_v2.ObjectRangeData(
                    checksummed_data=_storage_v2.ChecksummedData(
                        content=content, crc32c=google_crc32c.value(content)
                    ),
                    read_range=_storage_v2.ReadRange(
                        read_id=0, read_offset=0, read_length=len(content)
                    ),
                )
            ]
        )
        responses = iter([response])

        async def recv():
            item = next(responses, None)
            if item is not None:
                return item
            return await recv_after_chunk(submitted, future)

        mock_stream = mock.AsyncMock(
            spec=async_read_object_stream._AsyncReadObjectStream
        )
        mock_stream.recv.side_effect = recv
        mrd = AsyncMultiRangeDownloader(mock.MagicMock(), "bucket", "object")
        mrd.read_obj_str = mock_stream
        mrd._is_stream_open = True
        mrd._multiplexer = _StreamMultiplexer(mock_stream)
        return mrd, future, patcher

    @pytest.mark.asyncio
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer",
        return_value=0,
    )
    async def test_download_ranges_reports_held_corrupt_chunk_before_other_errors(
        self, _
    ):
        """A corrupt offloaded chunk is reported, and not written, even when a
        non-retryable error arrives before its checksum is known."""
        content = b"x" * reads_resumption_strategy._CRC32C_OFFLOAD_MIN_BYTES

        async def fail_after_chunk(submitted, future):
            await submitted.wait()  # the chunk is held, its check still running
            future.set_result(0)  # ...and the worker finds a mismatch
            raise exceptions.NotFound("object deleted")

        mrd, _, patcher = self._mrd_with_held_chunk(content, fail_after_chunk)
        buffer = BytesIO()
        with patcher, pytest.raises(DataCorruption) as exc_info:
            await mrd.download_ranges([(0, 2 * len(content), buffer)])

        assert "Checksum mismatch" in str(exc_info.value)
        assert isinstance(exc_info.value.__context__, exceptions.NotFound)
        assert buffer.getvalue() == b""

    @pytest.mark.asyncio
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer",
        return_value=0,
    )
    async def test_download_ranges_writes_held_chunks_before_other_errors(self, _):
        """Chunks received before a non-retryable error are written, as they
        are when checked inline, and the error is raised."""
        content = b"x" * reads_resumption_strategy._CRC32C_OFFLOAD_MIN_BYTES

        async def fail_after_chunk(submitted, future):
            await submitted.wait()
            future.set_result(google_crc32c.value(content))
            raise exceptions.NotFound("object deleted")

        mrd, _, patcher = self._mrd_with_held_chunk(content, fail_after_chunk)
        buffer = BytesIO()
        with patcher, pytest.raises(exceptions.NotFound):
            await mrd.download_ranges([(0, 2 * len(content), buffer)])

        assert buffer.getvalue() == content

    @pytest.mark.asyncio
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer",
        return_value=0,
    )
    async def test_download_ranges_cancellation_discards_held_chunks(self, _):
        content = b"x" * reads_resumption_strategy._CRC32C_OFFLOAD_MIN_BYTES

        async def hang(submitted, future):
            await asyncio.Event().wait()

        mrd, future, patcher = self._mrd_with_held_chunk(content, hang)
        buffer = BytesIO()
        with patcher:
            task = asyncio.create_task(
                mrd.download_ranges([(0, 2 * len(content), buffer)])
            )
            while not reads_resumption_strategy._crc32c_executor.submit.called:
                await asyncio.sleep(0)
            await asyncio.sleep(0)
            task.cancel()
            with pytest.raises(asyncio.CancelledError):
                await task

        assert future.cancelled()
        assert buffer.getvalue() == b""
        await mrd.close()

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.AsyncMultiRangeDownloader.open",
        new_callable=AsyncMock,
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.AsyncMultiRangeDownloader.close",
        new_callable=AsyncMock,
    )
    @pytest.mark.asyncio
    async def test_async_context_manager_calls_open_and_close(
        self, mock_close, mock_open
    ):
        # Arrange
        mock_client = mock.MagicMock()
        mrd = AsyncMultiRangeDownloader(
            mock_client, _TEST_BUCKET_NAME, _TEST_OBJECT_NAME
        )

        # To simulate the behavior of open and close changing the stream state
        async def open_side_effect():
            mrd._is_stream_open = True

        async def close_side_effect():
            mrd._is_stream_open = False

        mock_open.side_effect = open_side_effect
        mock_close.side_effect = close_side_effect
        mrd._is_stream_open = False

        # Act
        async with mrd as downloader:
            # Assert
            mock_open.assert_called_once()
            assert downloader == mrd
            assert mrd.is_stream_open

        mock_close.assert_called_once()
        assert not mrd.is_stream_open

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_create_mrd_with_generation_number(
        self, mock_cls_async_read_object_stream, caplog
    ):
        # Arrange
        mock_client = mock.MagicMock()
        mock_client.grpc_client = mock.AsyncMock()

        mock_stream = mock_cls_async_read_object_stream.return_value
        mock_stream.open = AsyncMock()
        mock_stream.generation_number = _TEST_GENERATION_NUMBER
        mock_stream.persisted_size = _TEST_OBJECT_SIZE
        mock_stream.read_handle = _TEST_READ_HANDLE

        # Act
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client,
            _TEST_BUCKET_NAME,
            _TEST_OBJECT_NAME,
            generation_number=_TEST_GENERATION_NUMBER,
            read_handle=_TEST_READ_HANDLE,
        )

        # Assert
        assert mrd.generation == _TEST_GENERATION_NUMBER
        assert mrd.read_handle == _TEST_READ_HANDLE
        assert mrd.persisted_size == _TEST_OBJECT_SIZE
        assert "'generation_number' is deprecated" in caplog.text

    @pytest.mark.asyncio
    async def test_create_mrd_with_both_generation_and_generation_number(self):
        # Arrange
        mock_client = mock.MagicMock()

        # Act & Assert
        with pytest.raises(TypeError):
            await AsyncMultiRangeDownloader.create_mrd(
                mock_client,
                _TEST_BUCKET_NAME,
                _TEST_OBJECT_NAME,
                generation=_TEST_GENERATION_NUMBER,
                generation_number=_TEST_GENERATION_NUMBER,
            )

    @mock.patch("google.cloud.storage.asyncio.async_multi_range_downloader.AsyncRetry")
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_open_retries_increment(
        self, mock_cls_async_read_object_stream, mock_async_retry
    ):
        # Arrange
        # Configure AsyncRetry mock to return a pass-through decorator so we can await the result
        mock_policy = mock.MagicMock()
        mock_policy.side_effect = lambda f: f
        mock_async_retry.return_value = mock_policy

        mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)
        # _make_mock_mrd calls create_mrd -> open.
        # We need to test logic where retry happens.

        # Create fresh MRD
        mock_client = mock.MagicMock()
        mock_client.grpc_client = mock.AsyncMock()
        mrd = AsyncMultiRangeDownloader(
            mock_client, _TEST_BUCKET_NAME, _TEST_OBJECT_NAME
        )
        # Mock stream
        mock_stream = mock_cls_async_read_object_stream.return_value
        mock_stream.open = AsyncMock()

        # Action: We want to capture the on_error passed to AsyncRetry
        await mrd.open()

        # Assert
        # Check that AsyncRetry was initialized with a wrapper
        call_args = mock_async_retry.call_args
        assert call_args is not None
        _, kwargs = call_args
        on_error = kwargs.get("on_error")
        assert on_error is not None

        # Simulate error to trigger increment
        assert mrd._open_retries == 0
        on_error(ValueError("test"))
        assert mrd._open_retries == 1

    @mock.patch("google.cloud.storage.asyncio.async_multi_range_downloader.AsyncRetry")
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_open_uses_redirect_aware_retry_predicate(
        self, mock_cls_async_read_object_stream, mock_async_retry
    ):
        mock_policy = mock.MagicMock()
        mock_policy.side_effect = lambda f: f
        mock_async_retry.return_value = mock_policy

        mock_client = mock.MagicMock()
        mock_client.grpc_client = mock.AsyncMock()
        mock_stream = mock_cls_async_read_object_stream.return_value
        mock_stream.open = AsyncMock()

        mrd = AsyncMultiRangeDownloader(
            mock_client, _TEST_BUCKET_NAME, _TEST_OBJECT_NAME
        )
        await mrd.open()

        predicate = mock_async_retry.call_args.kwargs["predicate"]
        redirect = _storage_v2.BidiReadObjectRedirectedError(
            routing_token="redirect-token"
        )
        status = status_pb2.Status()
        detail = status.details.add()
        detail.type_url = (
            "type.googleapis.com/google.storage.v2.BidiReadObjectRedirectedError"
        )
        detail.value = _storage_v2.BidiReadObjectRedirectedError.serialize(redirect)
        grpc_error = mock.MagicMock()
        grpc_error.trailing_metadata.return_value = [
            ("grpc-status-details-bin", status.SerializeToString())
        ]

        assert predicate(exceptions.ServiceUnavailable("unavailable")) is True
        assert predicate(exceptions.Aborted("redirect", errors=[grpc_error])) is True
        assert predicate(exceptions.Aborted("bare aborted")) is False
        assert predicate(ConnectionResetError("connection reset")) is False

    @mock.patch("google.cloud.storage.asyncio.async_multi_range_downloader.logger")
    @pytest.mark.asyncio
    async def test_on_open_error_logs_warning(self, mock_logger):
        # Arrange
        mock_client = mock.MagicMock()
        mrd = AsyncMultiRangeDownloader(
            mock_client, _TEST_BUCKET_NAME, _TEST_OBJECT_NAME
        )
        exc = ValueError("test error")

        # Act
        mrd._on_open_error(exc)

        # Assert
        mock_logger.warning.assert_called_once_with(
            f"Error occurred while opening MRD: {exc}"
        )

    @mock.patch("google.cloud.storage.asyncio.async_multi_range_downloader.logger")
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_ranges_resumption_logging(
        self, mock_cls_async_read_object_stream, mock_random_int, mock_logger
    ):
        # Arrange
        mock_mrd, _ = await self._make_mock_mrd(mock_cls_async_read_object_stream)

        from google.api_core import exceptions as core_exceptions

        retryable_exc = core_exceptions.ServiceUnavailable("Retry me")

        mock_mrd.read_obj_str.send = AsyncMock(
            side_effect=[
                retryable_exc,
                None,
            ]
        )

        recv_call_count = 0

        async def staged_recv():
            nonlocal recv_call_count
            recv_call_count += 1
            if recv_call_count == 1:
                return _storage_v2.BidiReadObjectResponse(
                    object_data_ranges=[
                        _storage_v2.ObjectRangeData(
                            checksummed_data=_storage_v2.ChecksummedData(
                                content=b"data", crc32c=123
                            ),
                            range_end=True,
                            read_range=_storage_v2.ReadRange(
                                read_offset=0, read_length=4, read_id=123
                            ),
                        )
                    ]
                )
            return None

        mock_mrd.read_obj_str.recv = AsyncMock(side_effect=staged_recv)

        mock_random_int.return_value = 123

        # Act
        buffer = BytesIO()

        # Patch google_crc32c.value where it is used in reads_resumption_strategy
        with mock.patch(
            "google.cloud.storage.asyncio.retry.reads_resumption_strategy.google_crc32c.value"
        ) as mock_crc_value:
            mock_crc_value.return_value = 123
            await mock_mrd.download_ranges([(0, 4, buffer)])

        # Assert
        mock_logger.info.assert_any_call("Resuming download (attempt 2) for 1 ranges.")

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_open_populates_checksum_properties(
        self, mock_cls_async_read_object_stream
    ):
        # Arrange
        mock_client = mock.MagicMock()
        mock_client.grpc_client = mock.AsyncMock()
        mock_stream = mock_cls_async_read_object_stream.return_value
        mock_stream.open = AsyncMock()
        mock_stream.generation_number = 123
        mock_stream.persisted_size = 100
        mock_stream.read_handle = b"h"
        mock_stream.is_finalized = True
        mock_stream.full_obj_server_crc32c = 999

        mrd = AsyncMultiRangeDownloader(mock_client, "bucket", "object")
        assert mrd.is_finalized is False
        assert mrd.full_obj_server_crc32c is None

        # Act
        await mrd.open()

        # Assert
        assert mrd.is_finalized is True
        assert mrd.full_obj_server_crc32c == 999

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._ReadResumptionStrategy"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._BidiStreamRetryManager"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_ranges_configures_full_object_read_state(
        self,
        mock_cls_async_read_object_stream,
        mock_retry_manager_cls,
        mock_strategy_cls,
    ):
        # Arrange
        mock_client = mock.MagicMock()
        mock_client.grpc_client = mock.AsyncMock()
        mock_stream = mock_cls_async_read_object_stream.return_value
        mock_stream.open = AsyncMock()
        mock_stream.persisted_size = 100
        mock_stream.is_finalized = True
        mock_stream.full_obj_server_crc32c = 999

        mrd = await AsyncMultiRangeDownloader.create_mrd(mock_client, "b", "o")

        mock_retry_manager = mock_retry_manager_cls.return_value
        mock_retry_manager.execute = AsyncMock()
        mock_strategy_cls.return_value.verify_pending_checksums = AsyncMock()

        # Act
        # Implicit full read (0, 0) and explicit full read (0, persisted_size=100)
        ranges = [(0, 0, BytesIO()), (0, 100, BytesIO()), (10, 20, BytesIO())]
        await mrd.download_ranges(ranges, enable_checksum=True)

        # Assert
        mock_retry_manager.execute.assert_called_once()
        initial_state = mock_retry_manager.execute.call_args[0][0]

        download_states = initial_state["download_states"]
        assert len(download_states) == 3

        states_list = list(download_states.values())
        # First state: (0, 0) -> is_full_object_read is True
        assert states_list[0].is_full_object_read is True
        assert states_list[0].rolling_checksum is not None

        # Second state: (0, 100) -> is_full_object_read is True
        assert states_list[1].is_full_object_read is True
        assert states_list[1].rolling_checksum is not None

        # Third state: (10, 20) -> is_full_object_read is False
        assert states_list[2].is_full_object_read is False
        assert states_list[2].rolling_checksum is None

        # State values for enable_checksum and crc32c
        assert initial_state["enable_checksum"] is True
        assert initial_state["full_obj_server_crc32c"] == 999

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._ReadResumptionStrategy"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._BidiStreamRetryManager"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_ranges_closes_on_datacorruption(
        self,
        mock_cls_async_read_object_stream,
        mock_retry_manager_cls,
        mock_strategy_cls,
    ):
        # Arrange
        mock_client = mock.MagicMock()
        mock_client.grpc_client = mock.AsyncMock()
        mock_stream = mock_cls_async_read_object_stream.return_value
        mock_stream.open = AsyncMock()

        mrd = await AsyncMultiRangeDownloader.create_mrd(mock_client, "b", "o")
        mrd.close = AsyncMock()

        mock_retry_manager = mock_retry_manager_cls.return_value
        mock_retry_manager.execute = AsyncMock(
            side_effect=DataCorruption(None, "corrupted")
        )

        # Act & Assert
        with pytest.raises(DataCorruption):
            await mrd.download_ranges([(0, 0, BytesIO())])

        mrd.close.assert_called_once()

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_ranges_retries_on_aborted_idle_stream_from_recv(
        self, mock_cls_async_read_object_stream, mock_random_int
    ):
        mock_client = mock.MagicMock()
        mock_client.grpc_client = mock.AsyncMock()

        initial_stream = mock.MagicMock()
        initial_stream.open = AsyncMock()
        initial_stream.close = AsyncMock()
        initial_stream.send = AsyncMock()
        initial_stream.generation_number = _TEST_GENERATION_NUMBER
        initial_stream.persisted_size = _TEST_OBJECT_SIZE
        initial_stream.read_handle = _TEST_READ_HANDLE
        initial_stream.is_finalized = True
        initial_stream.full_obj_server_crc32c = None
        initial_stream.is_stream_open = True

        replacement_stream = mock.MagicMock()
        replacement_stream.open = AsyncMock()
        replacement_stream.close = AsyncMock()
        replacement_stream.send = AsyncMock()
        replacement_stream.generation_number = _TEST_GENERATION_NUMBER
        replacement_stream.persisted_size = _TEST_OBJECT_SIZE
        replacement_stream.read_handle = _TEST_READ_HANDLE
        replacement_stream.is_finalized = True
        replacement_stream.full_obj_server_crc32c = None
        replacement_stream.is_stream_open = True

        mock_cls_async_read_object_stream.side_effect = [
            initial_stream,
            replacement_stream,
        ]

        error_info = error_details_pb2.ErrorInfo(
            reason="GRPC_REQUEST_TIMEOUT",
            domain="storage.googleapis.com",
        )
        initial_stream.recv = AsyncMock(
            side_effect=exceptions.Aborted(
                "Idle stream has been closed.",
                details=[error_info],
                error_info=error_info,
            )
        )

        response = _storage_v2.BidiReadObjectResponse(
            object_data_ranges=[
                _storage_v2.ObjectRangeData(
                    checksummed_data=_storage_v2.ChecksummedData(
                        content=b"data", crc32c=google_crc32c.value(b"data")
                    ),
                    range_end=True,
                    read_range=_storage_v2.ReadRange(
                        read_offset=0, read_length=4, read_id=123
                    ),
                )
            ]
        )
        replacement_stream.recv = AsyncMock(side_effect=[response])
        mock_random_int.return_value = 123

        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client,
            _TEST_BUCKET_NAME,
            _TEST_OBJECT_NAME,
            _TEST_GENERATION_NUMBER,
            _TEST_READ_HANDLE,
        )

        buffer = BytesIO()
        await mrd.download_ranges([(0, 4, buffer)])

        assert buffer.getvalue() == b"data"
        assert mock_cls_async_read_object_stream.call_count == 2
        initial_stream.close.assert_awaited_once()
        replacement_stream.open.assert_awaited_once()
        replacement_stream.send.assert_awaited_once_with(
            _storage_v2.BidiReadObjectRequest(
                read_ranges=[
                    _storage_v2.ReadRange(read_offset=0, read_length=4, read_id=123)
                ]
            )
        )

    def test_is_read_retryable_predicate(self):
        """Tests that _is_read_retryable correctly classifies retryable read errors."""
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            _is_read_retryable,
        )

        # Retryable exceptions
        assert _is_read_retryable(exceptions.Aborted("Idle stream closed")) is True
        assert _is_read_retryable(exceptions.ServiceUnavailable("unavailable")) is True
        assert _is_read_retryable(exceptions.InternalServerError("internal")) is True
        assert _is_read_retryable(exceptions.DeadlineExceeded("timeout")) is True
        assert _is_read_retryable(exceptions.TooManyRequests("quota")) is True
        assert _is_read_retryable(ConnectionResetError("connection reset")) is False
        assert _is_read_retryable(BrokenPipeError("broken pipe")) is False

        # Non-retryable exceptions
        assert _is_read_retryable(ValueError("invalid")) is False
        assert _is_read_retryable(exceptions.NotFound("not found")) is False
        assert _is_read_retryable(exceptions.PermissionDenied("denied")) is False
        assert _is_read_retryable(exceptions.InvalidArgument("invalid")) is False

    def test_pooled_stream_load(self):
        stream = self._make_dummy_pooled_stream()

        # Initially zero load
        assert stream.calculate_load(target_io_depth=10, target_bytes=1000) == 0.0

        # Add 5 ranges and 500 bytes -> 5/10 = 0.5, 500/1000 = 0.5 -> load = 0.5*0.5 + 0.5*0.5 = 0.5
        stream.record_request(5, 500)
        assert stream.pending_ranges == 5
        assert stream.pending_bytes == 500
        assert stream.calculate_load(target_io_depth=10, target_bytes=1000) == 0.5

        # Release
        stream.record_completion(3, 300)
        assert stream.pending_ranges == 2
        assert stream.pending_bytes == 200
        assert stream.calculate_load(target_io_depth=10, target_bytes=1000) == 0.2

    @mock.patch("google.cloud.storage.asyncio._stream_pool.logger")
    @pytest.mark.asyncio
    async def test_pooled_stream_close_logs_warnings_on_error(self, mock_logger):
        from google.cloud.storage.asyncio._stream_pool import (
            _PooledStream,
        )

        mock_stream = mock.MagicMock(
            close=AsyncMock(side_effect=RuntimeError("stream close error"))
        )
        mock_mux = mock.MagicMock(
            close=AsyncMock(side_effect=RuntimeError("mux close error"))
        )
        pooled = _PooledStream(mock_stream, mock_mux)

        await pooled.close()

        assert mock_logger.warning.call_count == 2

    @pytest.mark.asyncio
    async def test_stream_pool_scale_up_and_dispatch(self):
        from google.cloud.storage.asyncio._stream_pool import (
            MultiStreamConfig,
            _StreamPool,
        )

        async def stream_factory():
            return self._make_dummy_pooled_stream()

        pool = _StreamPool(
            stream_factory=stream_factory,
            multi_stream_config=MultiStreamConfig(
                min_streams=1,
                max_streams=2,
                target_io_depth=2,
                target_bytes=100,
            ),
        )
        initial_stream = await stream_factory()
        await pool.add_stream(initial_stream)

        # 1. Distribute with small load (1 range, 10 bytes) -> load < 1.0, stays on initial stream
        assignments, overflow, scale_tasks = await pool.distribute_ranges(
            [(0, 10, BytesIO())]
        )
        assert list(assignments.keys()) == [initial_stream]
        assert overflow == []
        assert scale_tasks == []
        assert len(pool.streams) == 1

        # 2. Add enough load to exceed target load > 1.0 -> triggers background scale up
        assignments2, _, _ = await pool.distribute_ranges([(10, 100, BytesIO())])
        assert list(assignments2.keys()) == [initial_stream]

        # Allow event loop to run background scale-up task
        await asyncio.sleep(0.01)
        assert len(pool.streams) == 2
        s2 = pool.streams[1]
        assert s2 != initial_stream

        # 3. Next distribute selects idle stream s2
        assignments3, _, _ = await pool.distribute_ranges([(110, 10, BytesIO())])
        assert list(assignments3.keys()) == [s2]

        # 4. Release stream capacity and close
        pool.release_stream(initial_stream, 2, 110)
        pool.release_stream(s2, 1, 10)
        await pool.close()
        assert len(pool.streams) == 0

    @pytest.mark.asyncio
    async def test_stream_pool_proportional_scale_up(self):
        from google.cloud.storage.asyncio._stream_pool import (
            MultiStreamConfig,
            _StreamPool,
        )

        async def stream_factory():
            return self._make_dummy_pooled_stream()

        pool = _StreamPool(
            stream_factory=stream_factory,
            multi_stream_config=MultiStreamConfig(
                min_streams=1,
                max_streams=5,
                target_io_depth=2,
                target_bytes=100,
            ),
        )
        initial_stream = await stream_factory()
        await pool.add_stream(initial_stream)

        # Huge burst: 6 ranges of 50 bytes each (total load = 3.0) -> triggers 2 concurrent background scale-ups
        ranges = [(i * 50, 50, BytesIO()) for i in range(6)]
        assignments, overflow, scale_tasks = await pool.distribute_ranges(ranges)
        assert list(assignments.keys()) == [initial_stream]
        assert len(assignments[initial_stream]) == 2
        assert len(overflow) == 4
        assert len(scale_tasks) == 2
        assert pool._pending_scale_ups == 2
        assert len(pool._background_tasks) == 2

        # Allow background scale-up tasks to finish
        await asyncio.gather(*scale_tasks)
        assert len(pool.streams) == 3
        assert pool._pending_scale_ups == 0

        # Burst exceeding max_streams -> capped by remaining headroom (5 - 3 = 2)
        more_ranges = [(i * 50, 50, BytesIO()) for i in range(10)]
        _, _, scale_tasks2 = await pool.distribute_ranges(more_ranges)
        assert len(scale_tasks2) == 2
        assert pool._pending_scale_ups == 2

        await asyncio.gather(*scale_tasks2)
        assert len(pool.streams) == 5
        assert pool._pending_scale_ups == 0

        await pool.close()
        assert len(pool.streams) == 0

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_create_mrd_with_multi_stream_config(self, mock_cls_stream):
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            MultiStreamConfig,
        )

        mock_client = self._make_mock_client()
        mock_cls_stream.side_effect = [
            self._make_mock_stream(read_handle=b"h1"),
            self._make_mock_stream(read_handle=b"h2"),
        ]

        config = MultiStreamConfig(
            min_streams=2,
            max_streams=4,
            target_io_depth=8,
            target_bytes=2 * 1024 * 1024,
        )

        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client, "b", "o", multi_stream_config=config
        )

        assert mrd.multi_stream_config.min_streams == 2
        assert mrd.multi_stream_config.max_streams == 4
        assert mrd.multi_stream_config.target_io_depth == 8
        assert mrd.multi_stream_config.target_bytes == 2 * 1024 * 1024
        # Verified that 2 streams were opened concurrently for min_streams=2
        assert len(mrd._pool.streams) == 2
        await mrd.close()

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_mrd_open_min_streams_failure_cleanup(self, mock_cls_stream):
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            MultiStreamConfig,
        )

        # Arrange: primary and 2nd stream succeed, 3rd stream fails during open()
        mock_client = self._make_mock_client()
        primary_stream = self._make_mock_stream()
        second_stream = self._make_mock_stream()
        failing_stream = self._make_mock_stream(
            open_side_effect=exceptions.PermissionDenied("Stream failed")
        )
        mock_cls_stream.side_effect = [
            primary_stream,
            second_stream,
            failing_stream,
        ]

        config = MultiStreamConfig(min_streams=3, max_streams=4)
        mrd = AsyncMultiRangeDownloader(
            mock_client, "b", "o", multi_stream_config=config
        )

        # Act & Assert
        with pytest.raises(exceptions.PermissionDenied, match="Stream failed"):
            await mrd.open()

        assert mrd._is_stream_open is False
        assert mrd._pool is None
        assert mrd.read_obj_str is None
        assert mrd._multiplexer is None
        assert mrd._primary_stream is None
        primary_stream.close.assert_awaited_once()
        second_stream.close.assert_awaited_once()

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_mrd_download_ranges_triggers_pool_scaling(self, mock_cls_stream):
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            MultiStreamConfig,
        )

        mock_client = self._make_mock_client()
        mock_cls_stream.side_effect = [
            self._make_mock_stream(),
            self._make_mock_stream(),
        ]

        config = MultiStreamConfig(
            min_streams=1,
            max_streams=3,
            target_io_depth=1,
            target_bytes=50,
        )
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client, "b", "o", multi_stream_config=config
        )
        assert len(mrd._pool.streams) == 1

        with mock.patch.object(mrd, "_download_ranges_on_stream", new=AsyncMock()):
            # Download ranges with load > 1.0 (2 ranges, 100 bytes)
            await mrd.download_ranges([(0, 50, BytesIO()), (50, 50, BytesIO())])
            await asyncio.sleep(0.01)
            # Pool dynamically scaled up to 2 streams
            assert len(mrd._pool.streams) == 2

        await mrd.close()

    @pytest.mark.parametrize(
        "config_kwargs",
        [
            pytest.param(None, id="default-no-config"),
            pytest.param(
                {"min_streams": 1, "max_streams": 1}, id="explicit-max-streams-one"
            ),
        ],
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_create_mrd_single_stream_bypass(
        self, mock_cls_stream, config_kwargs
    ):
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            MultiStreamConfig,
        )

        # Arrange
        mock_client = self._make_mock_client()
        mock_cls_stream.return_value = self._make_mock_stream()
        config = MultiStreamConfig(**config_kwargs) if config_kwargs else None

        # Act
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client, "b", "o", multi_stream_config=config
        )

        # Assert
        assert mrd._pool is None
        with mock.patch.object(
            mrd, "_download_ranges_on_stream", new=AsyncMock()
        ) as mock_dl:
            await mrd.download_ranges([(0, 50, BytesIO())])
            assert mock_dl.call_count == 1
            assert mock_dl.call_args[0][0] == mrd._primary_stream

        await mrd.close()

    @pytest.mark.asyncio
    async def test_stream_pool_closed_and_cancellation(self):
        from google.cloud.storage.asyncio._stream_pool import (
            MultiStreamConfig,
            _StreamPool,
        )

        scale_up_started = asyncio.Event()
        scale_up_finish = asyncio.Event()

        async def slow_factory():
            scale_up_started.set()
            await scale_up_finish.wait()
            return self._make_dummy_pooled_stream()

        pool = _StreamPool(
            stream_factory=slow_factory,
            multi_stream_config=MultiStreamConfig(
                min_streams=1,
                max_streams=2,
                target_io_depth=1,
                target_bytes=10,
            ),
        )
        initial_s = self._make_dummy_pooled_stream()
        await pool.add_stream(initial_s)

        # Trigger scale up
        await pool.distribute_ranges([(0, 20, BytesIO())])
        await scale_up_started.wait()
        assert len(pool._background_tasks) == 1
        task = next(iter(pool._background_tasks))

        # Close pool while scale up task is pending
        await pool.close()
        assert pool._closed is True
        assert len(pool.streams) == 0

        # Background task should be cancelled and awaited by close()
        with pytest.raises(asyncio.CancelledError):
            await task
        assert task.cancelled()

        # distribute_ranges on closed pool must raise ValueError
        with pytest.raises(ValueError, match="Pool is closed"):
            await pool.distribute_ranges([(0, 10, BytesIO())])

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_routing_token_preservation_and_propagation(
        self, mock_cls_async_read_object_stream
    ):
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            MultiStreamConfig,
        )

        def make_redirect_error(token: str, handle: bytes):
            redirect = _storage_v2.BidiReadObjectRedirectedError(
                routing_token=token,
                read_handle=_storage_v2.BidiReadHandle(handle=handle),
            )
            status = status_pb2.Status()
            detail = status.details.add()
            detail.type_url = (
                "type.googleapis.com/google.storage.v2.BidiReadObjectRedirectedError"
            )
            detail.value = _storage_v2.BidiReadObjectRedirectedError.serialize(redirect)
            grpc_error = mock.MagicMock()
            grpc_error.trailing_metadata.return_value = [
                ("grpc-status-details-bin", status.SerializeToString())
            ]
            return exceptions.Aborted("redirect", errors=[grpc_error])

        mock_client = self._make_mock_client()

        # 1. Primary stream fails on first open with redirect ("token-abc"), succeeds on retry
        s1_failed = self._make_mock_stream(
            open_side_effect=make_redirect_error("token-abc", b"h1")
        )
        s1_ok = self._make_mock_stream(read_handle=b"h1")
        # 2. Second stream opened via min_streams=2 receives "token-abc", fails once with redirect ("token-xyz"), succeeds on retry
        s2_failed = self._make_mock_stream(
            open_side_effect=make_redirect_error("token-xyz", b"h2")
        )
        s2_ok = self._make_mock_stream(read_handle=b"h2")

        mock_cls_async_read_object_stream.side_effect = [
            s1_failed,
            s1_ok,
            s2_failed,
            s2_ok,
        ]

        from google.api_core.retry_async import AsyncRetry

        on_err_mock = mock.MagicMock()
        custom_retry = AsyncRetry(initial=0.01, on_error=on_err_mock)
        config = MultiStreamConfig(min_streams=2, max_streams=4)
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client,
            "b",
            "o",
            retry_policy=custom_retry,
            multi_stream_config=config,
        )

        # Verify custom on_error was invoked for both primary and pooled stream redirects
        assert on_err_mock.call_count == 2

        # Verify s1_ok received routing_token=token-abc on retry and cleared mrd._routing_token
        assert ("x-goog-request-params", "routing_token=token-abc") in (
            s1_ok.open.call_args.kwargs["metadata"]
        )
        assert mrd._routing_token is None

        # Verify s2_failed started without a stale routing_token, then s2_ok retried with routing_token=token-xyz
        assert s2_failed.open.call_args.kwargs["metadata"] is None
        assert ("x-goog-request-params", "routing_token=token-xyz") in (
            s2_ok.open.call_args.kwargs["metadata"]
        )
        assert mrd.read_handle == b"h2"
        assert mrd._routing_token is None

        await mrd.close()

    @pytest.mark.asyncio
    async def test_stream_pool_selection_min_streams_and_further(self):
        from google.cloud.storage.asyncio._stream_pool import (
            MultiStreamConfig,
            _StreamPool,
        )

        pool = _StreamPool(
            stream_factory=lambda: self._make_dummy_pooled_stream(),
            multi_stream_config=MultiStreamConfig(
                min_streams=2,
                max_streams=4,
                target_io_depth=2,
                target_bytes=100,
            ),
        )

        s1 = self._make_dummy_pooled_stream()
        s2 = self._make_dummy_pooled_stream()
        await pool.add_stream(s1)
        await pool.add_stream(s2)

        # s1 has some load, s2 has 0 load -> selects least loaded among min_streams (s2)
        s1.record_request(1, 10)
        assert s1.calculate_load(2, 100) == 0.3
        assert s2.calculate_load(2, 100) == 0.0

        assignments, _, _ = await pool.distribute_ranges(
            [(0, 10, BytesIO())], allow_scale_up=False
        )
        assert list(assignments.keys()) == [s2]

        # Fully load both s1 and s2 (load >= 1.0)
        s1.record_request(2, 100)
        s2.record_request(3, 100)
        assert s1.is_fully_loaded(2, 100)
        assert s2.is_fully_loaded(2, 100)

        # Add further streams s3 and s4 (beyond min_streams=2)
        s3 = self._make_dummy_pooled_stream()
        s4 = self._make_dummy_pooled_stream()
        await pool.add_stream(s3)
        await pool.add_stream(s4)

        # Give s3 some load (0.35), s4 has 0.0 load
        s3.record_request(1, 20)
        assert s3.calculate_load(2, 100) == 0.35
        assert s4.calculate_load(2, 100) == 0.0

        # Since base streams are fully loaded, selects FIRST not fully loaded further stream (s3, not s4!)
        assignments_further, _, _ = await pool.distribute_ranges(
            [(0, 10, BytesIO())], allow_scale_up=False
        )
        assert list(assignments_further.keys()) == [s3]

        # Now fully load s3
        s3.record_request(3, 100)
        assert s3.is_fully_loaded(2, 100)

        # Next distribute chooses s4 (the first not fully loaded further stream now)
        assignments_s4, _, _ = await pool.distribute_ranges(
            [(0, 10, BytesIO())], allow_scale_up=False
        )
        assert list(assignments_s4.keys()) == [s4]

        # Now fully load s4
        s4.record_request(3, 100)
        assert s4.is_fully_loaded(2, 100)

        # When all streams are fully loaded, fallback selects the least loaded overall
        # Let s3 have load 2.0 and s1, s2, s4 have load 3.0
        s3.pending_ranges = 4
        s3.pending_bytes = 200
        s1.pending_ranges = 6
        s1.pending_bytes = 300
        s2.pending_ranges = 6
        s2.pending_bytes = 300
        s4.pending_ranges = 6
        s4.pending_bytes = 300

        fallback_assignments, _, _ = await pool.distribute_ranges(
            [(0, 10, BytesIO())], allow_scale_up=False
        )
        assert list(fallback_assignments.keys()) == [s3]

        await pool.close()

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_mrd_download_ranges_sharding_across_streams(self, mock_cls_stream):
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            MultiStreamConfig,
        )

        mock_client = self._make_mock_client()
        s1 = self._make_mock_stream(read_handle=b"h1")
        s2 = self._make_mock_stream(read_handle=b"h2")
        s3 = self._make_mock_stream(read_handle=b"h3")

        open_stream_started = asyncio.Event()

        async def s3_open_after_s1_starts(*args, **kwargs):
            # Prove s1/s2 start downloading before s3 finishes opening
            await asyncio.wait_for(open_stream_started.wait(), timeout=1.0)

        s3.open = AsyncMock(side_effect=s3_open_after_s1_starts)
        mock_cls_stream.side_effect = [s1, s2, s3]

        # Each range of 50 bytes with target_io_depth=2, target_bytes=100 has load = 0.5.
        # So 2 ranges (100 bytes) saturate a stream (load = 1.0).
        config = MultiStreamConfig(
            min_streams=2,
            max_streams=3,
            target_io_depth=2,
            target_bytes=100,
        )
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client, "b", "o", multi_stream_config=config
        )
        assert len(mrd._pool.streams) == 2

        dispatched_shards = []

        async def record_shard(pooled_stream, sub_ranges, *args, **kwargs):
            open_stream_started.set()
            dispatched_shards.append((pooled_stream, list(sub_ranges)))

        with mock.patch.object(
            mrd, "_download_ranges_on_stream", side_effect=record_shard
        ):
            # Pass 6 ranges of 50 bytes each (total load = 3.0 across max_streams=3).
            # Open streams (s1, s2) start immediately while s3 opens in parallel for overflow.
            ranges = [(i * 50, 50, BytesIO()) for i in range(6)]
            await mrd.download_ranges(ranges)

            assert len(mrd._pool.streams) == 3
            assert len(dispatched_shards) == 3
            assert [len(sub_ranges) for _, sub_ranges in dispatched_shards] == [2, 2, 2]

        # Verify all counters were released back to 0 after completion
        for ps in mrd._pool.streams:
            assert ps.pending_ranges == 0
            assert ps.pending_bytes == 0

        await mrd.close()

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_mrd_download_ranges_fills_current_stream_until_fully_loaded(
        self, mock_cls_stream
    ):
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            MultiStreamConfig,
        )

        mock_client = self._make_mock_client()
        s1 = self._make_mock_stream(read_handle=b"h1")
        s2 = self._make_mock_stream(read_handle=b"h2")
        mock_cls_stream.side_effect = [s1, s2]

        # Each 25-byte range has load = 0.5*(1/4) + 0.5*(25/100) = 0.25.
        # So 4 ranges (100 bytes) saturate a stream (load = 1.0).
        config = MultiStreamConfig(
            min_streams=2,
            max_streams=4,
            target_io_depth=4,
            target_bytes=100,
        )
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client, "b", "o", multi_stream_config=config
        )
        assert len(mrd._pool.streams) == 2

        dispatched_shards = []

        async def record_shard(pooled_stream, sub_ranges, *args, **kwargs):
            dispatched_shards.append((pooled_stream, list(sub_ranges)))

        with mock.patch.object(
            mrd, "_download_ranges_on_stream", side_effect=record_shard
        ):
            # 1. Small batch (2 ranges, total load = 0.5 < 1.0): stays together on stream 0
            r_small = [(0, 25, BytesIO()), (25, 25, BytesIO())]
            await mrd.download_ranges(r_small)
            assert len(dispatched_shards) == 1
            assert dispatched_shards[0] == (mrd._pool.streams[0], r_small)

            dispatched_shards.clear()

            # 2. Larger batch (6 ranges, total load = 1.5):
            # First 4 ranges fill stream 0 to load 1.0; next 2 ranges go contiguously to stream 1
            r_large = [(i * 25, 25, BytesIO()) for i in range(6)]
            await mrd.download_ranges(r_large)
            assert len(dispatched_shards) == 2
            assert dispatched_shards[0] == (mrd._pool.streams[0], r_large[:4])
            assert dispatched_shards[1] == (mrd._pool.streams[1], r_large[4:])

        await mrd.close()

    @pytest.mark.asyncio
    async def test_download_ranges_uninitialized_stream_or_multiplexer_raises(self):
        mock_client = self._make_mock_client()
        mrd = AsyncMultiRangeDownloader(mock_client, "b", "o")
        mrd._is_stream_open = True
        mrd.read_obj_str = None
        mrd._multiplexer = None

        with pytest.raises(
            ValueError,
            match="Underlying bidi-gRPC stream or multiplexer is not initialized",
        ):
            await mrd.download_ranges([(0, 10, BytesIO())])

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_reopen_non_primary_stream_preserves_primary_stream_and_metadata(
        self, mock_cls_stream
    ):
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            MultiStreamConfig,
        )

        mock_client = self._make_mock_client()
        primary_stream = self._make_mock_stream(read_handle=b"h1", is_finalized=True)
        non_primary_initial = self._make_mock_stream(
            read_handle=b"h2", is_finalized=False
        )
        non_primary_initial.object_metadata = None
        non_primary_initial.full_obj_server_crc32c = None

        replacement_stream = self._make_mock_stream(
            read_handle=b"h3", is_finalized=False
        )
        # Reopening with a read_handle may not return response.metadata
        replacement_stream.object_metadata = None
        replacement_stream.full_obj_server_crc32c = None

        mock_cls_stream.side_effect = [
            primary_stream,
            non_primary_initial,
            replacement_stream,
        ]

        config = MultiStreamConfig(min_streams=2, max_streams=4)
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client, "b", "o", multi_stream_config=config
        )
        assert mrd.read_obj_str is primary_stream
        assert mrd._primary_stream.stream is primary_stream
        assert mrd.is_finalized is True
        assert mrd.full_obj_server_crc32c == 12345

        non_primary_pooled = mrd._pool.streams[1]
        assert non_primary_pooled is not mrd._primary_stream
        assert non_primary_pooled.stream is non_primary_initial

        # Reopen the non-primary stream via _create_stream_factory
        factory = mrd._create_stream_factory(
            state={"read_handle": b"h2", "routing_token": "tok"},
            metadata=None,
            pooled_stream=non_primary_pooled,
        )
        reopened = await factory()

        assert reopened is replacement_stream
        assert non_primary_pooled.stream is replacement_stream
        assert mrd.read_obj_str is mrd._primary_stream.stream
        assert mrd.read_obj_str is primary_stream
        assert mrd.is_finalized is True
        assert mrd.full_obj_server_crc32c == 12345

        await mrd.close()

    @pytest.mark.parametrize(
        ("kwargs", "expected_msg"),
        [
            pytest.param(
                {"min_streams": 0},
                "min_streams must be >= 1",
                id="min-streams-below-one",
            ),
            pytest.param(
                {"min_streams": 4, "max_streams": 2},
                "max_streams must be >= min_streams",
                id="max-below-min-streams",
            ),
            pytest.param(
                {"target_io_depth": 0},
                "target_io_depth must be > 0",
                id="non-positive-target-io-depth",
            ),
            pytest.param(
                {"target_bytes": -1},
                "target_bytes must be > 0",
                id="non-positive-target-bytes",
            ),
        ],
    )
    def test_multi_stream_config_validation(self, kwargs, expected_msg):
        from google.cloud.storage.asyncio._stream_pool import MultiStreamConfig

        with pytest.raises(ValueError, match=expected_msg):
            MultiStreamConfig(**kwargs)

    @pytest.mark.asyncio
    async def test_stream_pool_empty_raises_and_scale_up_error_logged(self):
        from google.cloud.storage.asyncio._stream_pool import (
            MultiStreamConfig,
            _StreamPool,
        )

        async def failing_factory():
            raise RuntimeError("open failed")

        pool = _StreamPool(
            stream_factory=failing_factory,
            multi_stream_config=MultiStreamConfig(
                min_streams=1, max_streams=2, target_io_depth=1, target_bytes=10
            ),
        )

        with pytest.raises(ValueError, match="No streams available in stream pool"):
            await pool.distribute_ranges([(0, 10, BytesIO())])

        await pool.add_stream(self._make_dummy_pooled_stream())
        await pool.distribute_ranges([(0, 20, BytesIO())])
        await asyncio.sleep(0.01)

        assert pool._pending_scale_ups == 0
        assert len(pool.streams) == 1
        await pool.close()

    @pytest.mark.asyncio
    async def test_stream_pool_scale_up_cancellation_closes_new_stream(self):
        from google.cloud.storage.asyncio._stream_pool import (
            MultiStreamConfig,
            _StreamPool,
        )

        # Arrange
        factory_returning = asyncio.Event()
        new_pooled_stream = self._make_dummy_pooled_stream()
        new_pooled_stream.close = AsyncMock()

        async def factory():
            factory_returning.set()
            await asyncio.sleep(0)
            return new_pooled_stream

        pool = _StreamPool(
            stream_factory=factory,
            multi_stream_config=MultiStreamConfig(
                min_streams=1,
                max_streams=2,
                target_io_depth=1,
                target_bytes=10,
            ),
        )
        await pool.add_stream(self._make_dummy_pooled_stream())

        # Act: hold pool._lock while factory() finishes, then cancel the pending scale-up task
        await pool.distribute_ranges([(0, 20, BytesIO())])
        await factory_returning.wait()
        async with pool._lock:
            await asyncio.sleep(0)
            scale_task = next(iter(pool._background_tasks))
            scale_task.cancel()

        await pool.close()

        # Assert
        new_pooled_stream.close.assert_awaited_once()
        assert pool._pending_scale_ups == 0

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_ranges_cancels_siblings_on_failure_and_data_corruption(
        self, mock_cls_stream
    ):
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            MultiStreamConfig,
        )

        # Arrange: s1 (base), s2 (fast scale-up), s3 (slow scale-up)
        mock_client = self._make_mock_client()
        s1 = self._make_mock_stream(read_handle=b"h1")
        s2 = self._make_mock_stream(read_handle=b"h2")
        s3 = self._make_mock_stream(read_handle=b"h3")

        s2_overflow_started = asyncio.Event()
        scale_up_gate = asyncio.Event()

        async def slow_s3_open(*args, **kwargs):
            await scale_up_gate.wait()

        s3.open = AsyncMock(side_effect=slow_s3_open)
        mock_cls_stream.side_effect = [s1, s2, s3]

        config = MultiStreamConfig(
            min_streams=1,
            max_streams=3,
            target_io_depth=1,
            target_bytes=50,
        )
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client, "b", "o", multi_stream_config=config
        )

        overflow_batch_cancelled = asyncio.Event()

        async def side_effect_dl(pooled_stream, batch, *args, **kwargs):
            if pooled_stream.stream is s1:
                await s2_overflow_started.wait()
                await mrd.close()
                raise DataCorruption(None, "checksum mismatch")
            else:
                s2_overflow_started.set()
                try:
                    await asyncio.sleep(10)
                except asyncio.CancelledError:
                    overflow_batch_cancelled.set()
                    raise

        # Act & Assert
        with mock.patch.object(
            mrd, "_download_ranges_on_stream", side_effect=side_effect_dl
        ):
            ranges = [(i * 50, 50, BytesIO()) for i in range(3)]
            with pytest.raises(DataCorruption, match="checksum mismatch"):
                await mrd.download_ranges(ranges)

        assert overflow_batch_cancelled.is_set()
        assert mrd.is_stream_open is False
        assert mrd._pool is None

    @pytest.mark.asyncio
    async def test_stream_pool_contiguous_distribution_when_saturated(self):
        from google.cloud.storage.asyncio._stream_pool import (
            MultiStreamConfig,
            _StreamPool,
        )

        # Arrange
        pool = _StreamPool(
            stream_factory=lambda: self._make_dummy_pooled_stream(),
            multi_stream_config=MultiStreamConfig(
                min_streams=2,
                max_streams=2,
                target_io_depth=2,
                target_bytes=100,
            ),
        )
        s1 = self._make_dummy_pooled_stream()
        s2 = self._make_dummy_pooled_stream()
        await pool.add_stream(s1)
        await pool.add_stream(s2)
        ranges = [(i * 50, 50, BytesIO()) for i in range(8)]

        # Act
        assignments, overflow, scale_tasks = await pool.distribute_ranges(ranges)

        # Assert: contiguous slices without range-by-range interleaving
        assert overflow == []
        assert scale_tasks == []
        assert assignments[s1] == ranges[:4]
        assert assignments[s2] == ranges[4:]

        await pool.close()

    @pytest.mark.parametrize(
        ("persisted_size", "offset", "expected_effective_bytes"),
        [
            pytest.param(1000, 200, 800, id="known-persisted-size"),
            pytest.param(None, 0, 500, id="unknown-persisted-size-fallback"),
        ],
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_zero_length_range_load_accounting_and_release(
        self, mock_cls_stream, persisted_size, offset, expected_effective_bytes
    ):
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            MultiStreamConfig,
        )

        # Arrange
        mock_client = self._make_mock_client()
        s1 = self._make_mock_stream(read_handle=b"h1", persisted_size=persisted_size)
        s2 = self._make_mock_stream(read_handle=b"h2", persisted_size=persisted_size)
        mock_cls_stream.side_effect = [s1, s2]

        config = MultiStreamConfig(
            min_streams=1,
            max_streams=2,
            target_io_depth=2,
            target_bytes=500,
        )
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client, "b", "o", multi_stream_config=config
        )
        recorded_loads = []

        async def inspect_load(pooled_stream, batch, *args, **kwargs):
            recorded_loads.append(
                (pooled_stream.pending_ranges, pooled_stream.pending_bytes)
            )

        # Act
        with mock.patch.object(
            mrd, "_download_ranges_on_stream", side_effect=inspect_load
        ):
            await mrd.download_ranges([(offset, 0, BytesIO())])

        # Assert
        assert recorded_loads == [(1, expected_effective_bytes)]
        for ps in mrd._pool.streams:
            assert ps.pending_ranges == 0
            assert ps.pending_bytes == 0

        await mrd.close()

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_download_overflow_incremental_dispatch_and_inflight_reuse(
        self, mock_cls_stream
    ):
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            MultiStreamConfig,
        )

        mock_client = self._make_mock_client()
        s1 = self._make_mock_stream(read_handle=b"h1")
        s2 = self._make_mock_stream(read_handle=b"h2")
        s3 = self._make_mock_stream(read_handle=b"h3")

        s2_dispatched = asyncio.Event()

        async def s3_waits_for_s2_dispatch(*args, **kwargs):
            # Prove s2 receives and starts downloading overflow BEFORE s3 finishes opening!
            await asyncio.wait_for(s2_dispatched.wait(), timeout=1.0)

        s3.open = AsyncMock(side_effect=s3_waits_for_s2_dispatch)
        mock_cls_stream.side_effect = [s1, s2, s3]

        config = MultiStreamConfig(
            min_streams=1,
            max_streams=3,
            target_io_depth=2,
            target_bytes=100,
        )
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client, "b", "o", multi_stream_config=config
        )

        dispatched = []

        async def record_dl(pooled_stream, batch, *args, **kwargs):
            dispatched.append((pooled_stream, list(batch)))
            if pooled_stream.stream is s2:
                s2_dispatched.set()

        with mock.patch.object(
            mrd, "_download_ranges_on_stream", side_effect=record_dl
        ):
            # 6 ranges (2 per stream across s1, s2, s3).
            # s2 opens immediately, so overflow ranges r2..r3 are dispatched to s2
            # without head-of-line blocking on s3.open!
            ranges = [(i * 50, 50, BytesIO()) for i in range(6)]
            await mrd.download_ranges(ranges)

        assert len(mrd._pool.streams) == 3
        assert len(dispatched) == 3
        for ps in mrd._pool.streams:
            assert ps.pending_ranges == 0
            assert ps.pending_bytes == 0

        await mrd.close()

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_concurrent_multi_stream_stress_reliability(self, mock_cls_stream):
        from google.cloud.storage.asyncio.async_multi_range_downloader import (
            MultiStreamConfig,
        )

        mock_client = self._make_mock_client()

        def make_stream(*args, **kwargs):
            s = self._make_mock_stream(persisted_size=10_000)

            async def delayed_open(*a, **kw):
                await asyncio.sleep(0.002)

            s.open = AsyncMock(side_effect=delayed_open)
            return s

        mock_cls_stream.side_effect = make_stream

        config = MultiStreamConfig(
            min_streams=2,
            max_streams=6,
            target_io_depth=4,
            target_bytes=200,
        )
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client, "b", "o", multi_stream_config=config
        )

        completed_ranges = 0

        async def simulated_dl(pooled_stream, batch, *args, **kwargs):
            nonlocal completed_ranges
            await asyncio.sleep(0.001)
            for offset, length, buf in batch:
                size = length if length > 0 else (10_000 - offset)
                buf.write(b"x" * min(size, 16))
            completed_ranges += len(batch)

        with mock.patch.object(
            mrd, "_download_ranges_on_stream", side_effect=simulated_dl
        ):
            # Run 12 concurrent download_ranges calls with varying batch sizes and zero-length ranges
            concurrent_calls = []
            expected_ranges = 0
            for call_idx in range(12):
                batch = [
                    (i * 50, 50 if (i + call_idx) % 7 != 0 else 0, BytesIO())
                    for i in range(1, (call_idx % 8) + 2)
                ]
                expected_ranges += len(batch)
                concurrent_calls.append(mrd.download_ranges(batch))

            await asyncio.gather(*concurrent_calls)

        assert completed_ranges == expected_ranges
        assert 2 < len(mrd._pool.streams) <= 6
        for ps in mrd._pool.streams:
            assert ps.pending_ranges == 0
            assert ps.pending_bytes == 0

        await mrd.close()

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_mrd_metrics_recording(
        self, mock_cls_async_read_object_stream, mock_random_int
    ):
        mock_recorder = mock.MagicMock()
        mock_recorder.standard_enabled = True
        mock_client = mock.MagicMock()
        mock_client._metrics_recorder = mock_recorder
        mock_client.grpc_client = mock.AsyncMock()

        stream = mock.MagicMock()
        stream.open = AsyncMock()
        stream.close = AsyncMock()
        stream.send = AsyncMock()
        stream._mark_closing_cleanly = mock.MagicMock()
        stream.generation_number = _TEST_GENERATION_NUMBER
        stream.persisted_size = _TEST_OBJECT_SIZE
        stream.read_handle = _TEST_READ_HANDLE
        stream.is_finalized = True
        stream.full_obj_server_crc32c = None
        stream.is_stream_open = True
        mock_cls_async_read_object_stream.return_value = stream

        response = _storage_v2.BidiReadObjectResponse(
            object_data_ranges=[
                _storage_v2.ObjectRangeData(
                    checksummed_data=_storage_v2.ChecksummedData(
                        content=b"data", crc32c=google_crc32c.value(b"data")
                    ),
                    range_end=True,
                    read_range=_storage_v2.ReadRange(
                        read_offset=0, read_length=4, read_id=123
                    ),
                )
            ]
        )
        stream.recv = AsyncMock(side_effect=[response])
        mock_random_int.return_value = 123

        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client,
            _TEST_BUCKET_NAME,
            _TEST_OBJECT_NAME,
        )
        assert (
            mock_cls_async_read_object_stream.call_args.kwargs["metrics_recorder"]
            is mock_recorder
        )
        # create_mrd suppresses nested open() so only 1 logical operation is recorded
        mock_recorder.record_logical_operation.assert_called_once()
        assert (
            mock_recorder.record_logical_operation.call_args.kwargs["client_method"]
            == "storage.asyncio.AsyncMultiRangeDownloader.create_mrd"
        )

        mock_recorder.record_logical_operation.reset_mock()
        buf = BytesIO()
        await mrd.download_ranges([(0, 4, buf)])
        mock_recorder.record_response_body_size.assert_called_once_with(
            4, operation="ReadObject"
        )
        mock_recorder.record_logical_operation.assert_called_once()
        assert (
            mock_recorder.record_logical_operation.call_args.kwargs["client_method"]
            == "storage.asyncio.AsyncMultiRangeDownloader.download_ranges"
        )
        assert (
            mock_recorder.record_logical_operation.call_args.kwargs["operation"]
            == "ReadObject"
        )
        assert (
            mock_recorder.record_logical_operation.call_args.kwargs["rpc_method"]
            == "google.storage.v2.Storage/BidiReadObject"
        )

        # Verify download_ranges with custom metadata marks stream clean before reopen
        chunk1 = _storage_v2.BidiReadObjectResponse(
            object_data_ranges=[
                _storage_v2.ObjectRangeData(
                    checksummed_data=_storage_v2.ChecksummedData(
                        content=b"ab", crc32c=google_crc32c.value(b"ab")
                    ),
                    range_end=False,
                    read_range=_storage_v2.ReadRange(
                        read_offset=0, read_length=2, read_id=123
                    ),
                )
            ]
        )
        chunk2 = _storage_v2.BidiReadObjectResponse(
            object_data_ranges=[
                _storage_v2.ObjectRangeData(
                    checksummed_data=_storage_v2.ChecksummedData(
                        content=b"cd", crc32c=google_crc32c.value(b"cd")
                    ),
                    range_end=True,
                    read_range=_storage_v2.ReadRange(
                        read_offset=2, read_length=2, read_id=123
                    ),
                )
            ]
        )
        stream.recv = AsyncMock(side_effect=[chunk1, chunk2])
        mock_recorder.record_response_body_size.reset_mock()
        stream._mark_closing_cleanly.reset_mock()
        buf2 = BytesIO()
        await mrd.download_ranges([(0, 4, buf2)], metadata=[("x-custom", "val")])
        stream._mark_closing_cleanly.assert_called()
        assert (
            mock_cls_async_read_object_stream.call_args.kwargs["metrics_recorder"]
            is mock_recorder
        )
        mock_recorder.record_response_body_size.assert_called_once_with(
            4, operation="ReadObject"
        )

        # Verify DataCorruption on a mocked stream records CHECKSUM_MISMATCH before close
        corrupt_resp = _storage_v2.BidiReadObjectResponse(
            object_data_ranges=[
                _storage_v2.ObjectRangeData(
                    checksummed_data=_storage_v2.ChecksummedData(
                        content=b"data", crc32c=google_crc32c.value(b"data") + 1
                    ),
                    range_end=True,
                    read_range=_storage_v2.ReadRange(
                        read_offset=0, read_length=4, read_id=123
                    ),
                )
            ]
        )
        stream.recv = AsyncMock(side_effect=[corrupt_resp])
        mock_recorder.record_rpc_attempt.reset_mock()
        with pytest.raises(DataCorruption):
            await mrd.download_ranges([(0, 4, BytesIO())])
        mock_recorder.record_rpc_attempt.assert_called_once()
        assert (
            mock_recorder.record_rpc_attempt.call_args.kwargs["error_type"]
            == "CHECKSUM_MISMATCH"
        )
        assert mrd.is_stream_open is False

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader._AsyncReadObjectStream"
    )
    @pytest.mark.asyncio
    async def test_mrd_retry_metrics_accounting(
        self, mock_cls_async_read_object_stream, mock_random_int, monkeypatch
    ):
        from google.api_core.retry_async import AsyncRetry

        from google.cloud.storage import _opentelemetry_metrics

        monkeypatch.setattr(_opentelemetry_metrics, "HAS_OPENTELEMETRY_METRICS", True)
        monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)
        mock_metrics = mock.Mock()
        mock_meter = mock.Mock()
        mock_meter.create_histogram.side_effect = lambda *a, **kw: mock.Mock()
        mock_meter.create_counter.side_effect = lambda *a, **kw: mock.Mock()
        mock_metrics.get_meter.return_value = mock_meter
        monkeypatch.setattr(
            _opentelemetry_metrics, "metrics", mock_metrics, raising=False
        )

        recorder = _opentelemetry_metrics._MetricsRecorder(
            enable_metrics=True, rpc_system="grpc"
        )
        mock_client = mock.MagicMock()
        mock_client._metrics_recorder = recorder
        mock_client.grpc_client = mock.AsyncMock()

        # 1. MRD.open() retry (attempt 1 fails with 503, attempt 2 succeeds)
        failed_open_stream = mock.MagicMock()
        failed_open_stream.open = AsyncMock(
            side_effect=exceptions.ServiceUnavailable("503 open failed")
        )
        failed_open_stream.is_stream_open = False

        open_stream = mock.MagicMock()
        open_stream.open = AsyncMock()
        open_stream.close = AsyncMock()
        open_stream.send = AsyncMock()
        open_stream.generation_number = _TEST_GENERATION_NUMBER
        open_stream.persisted_size = _TEST_OBJECT_SIZE
        open_stream.read_handle = _TEST_READ_HANDLE
        open_stream.is_finalized = True
        open_stream.full_obj_server_crc32c = None
        open_stream.is_stream_open = True

        # 2. MRD.download_ranges() mid-stream retry (attempt 1 Aborted, attempt 2 succeeds)
        open_stream.recv = AsyncMock(
            side_effect=exceptions.Aborted("Idle stream closed")
        )
        recovered_stream = mock.MagicMock()
        recovered_stream.open = AsyncMock()
        recovered_stream.close = AsyncMock()
        recovered_stream.send = AsyncMock()
        recovered_stream.generation_number = _TEST_GENERATION_NUMBER
        recovered_stream.persisted_size = _TEST_OBJECT_SIZE
        recovered_stream.read_handle = _TEST_READ_HANDLE
        recovered_stream.is_finalized = True
        recovered_stream.full_obj_server_crc32c = None
        recovered_stream.is_stream_open = True
        recovered_stream.recv = AsyncMock(
            side_effect=[
                _storage_v2.BidiReadObjectResponse(
                    object_data_ranges=[
                        _storage_v2.ObjectRangeData(
                            checksummed_data=_storage_v2.ChecksummedData(
                                content=b"data", crc32c=google_crc32c.value(b"data")
                            ),
                            range_end=True,
                            read_range=_storage_v2.ReadRange(
                                read_offset=0, read_length=4, read_id=123
                            ),
                        )
                    ]
                )
            ]
        )

        mock_cls_async_read_object_stream.side_effect = [
            failed_open_stream,
            open_stream,
            recovered_stream,
        ]
        mock_random_int.return_value = 123

        user_on_error = mock.Mock()
        fast_retry = AsyncRetry(initial=0.001, maximum=0.001, on_error=user_on_error)
        mrd = AsyncMultiRangeDownloader(
            mock_client, _TEST_BUCKET_NAME, _TEST_OBJECT_NAME
        )
        await mrd.open(retry_policy=fast_retry)

        user_on_error.assert_called_once()
        recorder.retries_counter.add.assert_called_once()
        _, open_retry_kw = recorder.retries_counter.add.call_args
        assert open_retry_kw["attributes"]["gcp.storage.operation"] == "ReadObject"
        assert open_retry_kw["attributes"]["error.type"] == "UNAVAILABLE"

        recorder.retries_counter.add.reset_mock()
        buf = BytesIO()
        await mrd.download_ranges(
            [(0, 4, buf)],
            retry_policy=AsyncRetry(
                predicate=lambda e: True, initial=0.001, maximum=0.001
            ),
        )
        assert buf.getvalue() == b"data"
        recorder.retries_counter.add.assert_called_once()
        _, dl_retry_kw = recorder.retries_counter.add.call_args
        assert dl_retry_kw["attributes"]["gcp.storage.operation"] == "ReadObject"
        assert dl_retry_kw["attributes"]["error.type"] == "ABORTED"

        # 3. MRD.open() failure when metrics are disabled (recorder is None)
        disabled_client = mock.MagicMock()
        disabled_client._metrics_recorder = None
        disabled_client.grpc_client = mock.AsyncMock()
        fail_stream = mock.MagicMock()
        fail_stream.open = AsyncMock(side_effect=exceptions.NotFound("404"))
        mock_cls_async_read_object_stream.side_effect = [fail_stream]
        mrd_disabled = AsyncMultiRangeDownloader(
            disabled_client, _TEST_BUCKET_NAME, _TEST_OBJECT_NAME
        )
        with pytest.raises(exceptions.NotFound):
            await mrd_disabled.open()

    @mock.patch(
        "google.cloud.storage.asyncio.async_multi_range_downloader.generate_random_56_bit_integer"
    )
    @pytest.mark.asyncio
    async def test_mrd_bidi_stream_interceptor_ttfb_duration_and_reopen_metrics(
        self, mock_random_int, monkeypatch
    ):
        import grpc
        from google.api_core.retry_async import AsyncRetry

        from google.cloud.storage import _opentelemetry_metrics
        from google.cloud.storage.asyncio import async_grpc_client

        monkeypatch.setattr(_opentelemetry_metrics, "HAS_OPENTELEMETRY_METRICS", True)
        monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)
        mock_metrics = mock.Mock()
        mock_meter = mock.Mock()
        mock_meter.create_histogram.side_effect = lambda *a, **kw: mock.Mock()
        mock_meter.create_counter.side_effect = lambda *a, **kw: mock.Mock()
        mock_metrics.get_meter.return_value = mock_meter
        monkeypatch.setattr(
            _opentelemetry_metrics, "metrics", mock_metrics, raising=False
        )

        recorder = _opentelemetry_metrics._MetricsRecorder(
            enable_metrics=True, rpc_system="grpc"
        )
        _, _, _, s_s = async_grpc_client._create_metrics_interceptors(
            recorder, direct_path_attempted=False
        )
        details = mock.MagicMock(method="/google.storage.v2.Storage/BidiReadObject")

        class _FakeBidiCall:
            def __init__(self, corrupt_crc=False):
                self._queue = asyncio.Queue()
                self._done = False
                self._pump_task = None
                self._corrupt_crc = corrupt_crc

            def done(self):
                return self._done

            def add_done_callback(self, callback):
                pass

            def cancel(self):
                self._done = True
                self._pump_task.cancel()
                self._queue.put_nowait(grpc.aio.EOF)
                return True

            async def write(self, request):
                if request.read_object_spec.bucket:
                    self._queue.put_nowait(
                        _storage_v2.BidiReadObjectResponse(
                            metadata=_storage_v2.Object(
                                generation=_TEST_GENERATION_NUMBER,
                                size=_TEST_OBJECT_SIZE,
                            ),
                            read_handle=_storage_v2.BidiReadHandle(
                                handle=_TEST_READ_HANDLE
                            ),
                        )
                    )
                if request.read_ranges:
                    crc = google_crc32c.value(b"data") + (1 if self._corrupt_crc else 0)
                    for r in request.read_ranges:
                        self._queue.put_nowait(
                            _storage_v2.BidiReadObjectResponse(
                                object_data_ranges=[
                                    _storage_v2.ObjectRangeData(
                                        checksummed_data=_storage_v2.ChecksummedData(
                                            content=b"data",
                                            crc32c=crc,
                                        ),
                                        range_end=True,
                                        read_range=_storage_v2.ReadRange(
                                            read_offset=r.read_offset,
                                            read_length=4,
                                            read_id=r.read_id,
                                        ),
                                    )
                                ]
                            )
                        )

            async def done_writing(self):
                self._queue.put_nowait(grpc.aio.EOF)

            async def read(self):
                return await self._queue.get()

        created_tracked_calls = []
        raw_calls = [
            _FakeBidiCall(),
            _FakeBidiCall(),
            _FakeBidiCall(),
            _FakeBidiCall(corrupt_crc=True),
        ]

        async def start_bidi_rpc(request_iterator=None, metadata=None):
            raw = raw_calls.pop(0)
            tracked = await s_s.intercept_stream_stream(
                mock.AsyncMock(return_value=raw), details, request_iterator
            )

            async def _pump_requests():
                async for req in request_iterator:
                    await tracked.write(req)
                await tracked.done_writing()

            raw._pump_task = asyncio.create_task(_pump_requests())
            created_tracked_calls.append(tracked)
            return tracked

        mock_client = mock.MagicMock()
        mock_client._metrics_recorder = recorder
        bidi_key = object()
        mock_client.grpc_client._client._transport.bidi_read_object = bidi_key
        mock_client.grpc_client._client._transport._wrapped_methods = {
            bidi_key: start_bidi_rpc
        }
        mock_random_int.side_effect = [101, 102, 201, 202, 301]

        # Scenario A: Healthy MRD lifecycle across 2 download_ranges() calls + close()
        mrd = await AsyncMultiRangeDownloader.create_mrd(
            mock_client, _TEST_BUCKET_NAME, _TEST_OBJECT_NAME
        )
        created_tracked_calls[0]._start_time -= 50.0
        assert recorder.ttfb.record.call_count == 1

        b1, b2 = BytesIO(), BytesIO()
        await mrd.download_ranges([(0, 4, b1)])
        await mrd.download_ranges([(0, 4, b2)])
        # Same physical stream: TTFB is still recorded only once
        assert recorder.ttfb.record.call_count == 1
        assert b1.getvalue() == b"data"
        assert b2.getvalue() == b"data"

        await mrd.close()
        assert recorder.attempts_counter.add.call_count == 1
        assert (
            recorder.attempts_counter.add.call_args.kwargs["attributes"]["error.type"]
            == "OK"
        )
        assert recorder.rpc_call_duration.record.call_args.args[0] >= 50.0

        # Scenario B: Broken stream during download_ranges() triggers reopen_stream()
        recorder.ttfb.record.reset_mock()
        recorder.attempts_counter.add.reset_mock()
        recorder.retries_counter.add.reset_mock()
        recorder.rpc_call_duration.record.reset_mock()

        mrd2 = await AsyncMultiRangeDownloader.create_mrd(
            mock_client, _TEST_BUCKET_NAME, _TEST_OBJECT_NAME
        )
        assert recorder.ttfb.record.call_count == 1
        mrd2.read_obj_str.send = AsyncMock(
            side_effect=exceptions.ServiceUnavailable("send broke")
        )

        b3 = BytesIO()
        await mrd2.download_ranges(
            [(0, 4, b3)],
            retry_policy=AsyncRetry(
                predicate=lambda e: True, initial=0.001, maximum=0.001
            ),
        )
        assert b3.getvalue() == b"data"
        # Stream 1 + reopened Stream 2 => 2 TTFB points and 1 retry
        assert recorder.ttfb.record.call_count == 2
        assert recorder.retries_counter.add.call_count == 1
        # Broken stream 1 was NOT falsely marked OK by reopen_stream()
        stream1_err = recorder.attempts_counter.add.call_args_list[0].kwargs[
            "attributes"
        ]["error.type"]
        assert stream1_err == "CANCELLED"

        await mrd2.close()
        assert recorder.attempts_counter.add.call_count == 2
        stream2_err = recorder.attempts_counter.add.call_args_list[1].kwargs[
            "attributes"
        ]["error.type"]
        assert stream2_err == "OK"

        # Scenario C: DataCorruption records CHECKSUM_MISMATCH on tracked stream before close()
        recorder.attempts_counter.add.reset_mock()
        recorder.errors_counter.add.reset_mock()
        mrd3 = await AsyncMultiRangeDownloader.create_mrd(
            mock_client, _TEST_BUCKET_NAME, _TEST_OBJECT_NAME
        )
        with pytest.raises(DataCorruption):
            await mrd3.download_ranges([(0, 4, BytesIO())])
        assert mrd3.is_stream_open is False
        assert recorder.attempts_counter.add.call_count == 1
        assert (
            recorder.attempts_counter.add.call_args.kwargs["attributes"]["error.type"]
            == "CHECKSUM_MISMATCH"
        )
        assert recorder.errors_counter.add.call_count == 1
        assert (
            recorder.errors_counter.add.call_args.kwargs["attributes"]["error.type"]
            == "CHECKSUM_MISMATCH"
        )
