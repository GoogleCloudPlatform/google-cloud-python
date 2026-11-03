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
