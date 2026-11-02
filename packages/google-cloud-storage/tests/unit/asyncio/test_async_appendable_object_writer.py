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

import io
import unittest.mock as mock
from unittest.mock import AsyncMock, MagicMock

import pytest
from google.api_core import exceptions
from google.rpc import status_pb2

from google.cloud._storage_v2.types import storage as storage_type
from google.cloud._storage_v2.types.storage import BidiWriteObjectRedirectedError
from google.cloud.storage import Blob
from google.cloud.storage.asyncio.async_appendable_object_writer import (
    _DEFAULT_FLUSH_INTERVAL_BYTES,
    _MAX_CHUNK_SIZE_BYTES,
    AsyncAppendableObjectWriter,
    _is_write_retryable,
)

# Constants
BUCKET = "test-bucket"
OBJECT = "test-object"
GENERATION = 123
WRITE_HANDLE = b"test-write-handle"
PERSISTED_SIZE = 456
EIGHT_MIB = 8 * 1024 * 1024
DATA_LESS_THAN_FLUSH_INTERVAL = (
    b"test-data"  # 9 bytes, less than default flush interval
)


class TestIsWriteRetryable:
    """Exhaustive tests for retry predicate logic."""

    # TODO: remove `mock_appendable_writer` param.
    def test_standard_transient_errors(self, mock_appendable_writer):
        for exc in [
            exceptions.InternalServerError("500"),
            exceptions.ServiceUnavailable("503"),
            exceptions.DeadlineExceeded("timeout"),
            exceptions.TooManyRequests("429"),
        ]:
            assert _is_write_retryable(exc)

    def test_aborted_with_redirect_proto(self, mock_appendable_writer):
        # Direct redirect error wrapped in Aborted
        redirect = BidiWriteObjectRedirectedError(routing_token="token")
        exc = exceptions.Aborted("aborted", errors=[redirect])
        assert _is_write_retryable(exc)

    def test_aborted_with_trailers(self, mock_appendable_writer):
        # Setup Status with Redirect Detail
        status = status_pb2.Status()
        detail = status.details.add()
        detail.type_url = (
            "type.googleapis.com/google.storage.v2.BidiWriteObjectRedirectedError"
        )

        # Mock error with trailing_metadata method
        mock_grpc_error = MagicMock()
        mock_grpc_error.trailing_metadata.return_value = [
            ("grpc-status-details-bin", status.SerializeToString())
        ]

        # Aborted wraps the grpc error
        exc = exceptions.Aborted("aborted", errors=[mock_grpc_error])
        assert _is_write_retryable(exc)

    def test_aborted_without_metadata(self, mock_appendable_writer):
        mock_grpc_error = MagicMock()
        mock_grpc_error.trailing_metadata.return_value = []
        exc = exceptions.Aborted("bare aborted", errors=[mock_grpc_error])
        assert not _is_write_retryable(exc)

    def test_non_retryable_errors(self, mock_appendable_writer):
        assert not _is_write_retryable(exceptions.BadRequest("400"))
        assert not _is_write_retryable(exceptions.NotFound("404"))


@pytest.fixture
def mock_appendable_writer():
    """Fixture to provide a mock AsyncAppendableObjectWriter setup."""
    mock_client = mock.MagicMock()
    mock_client.grpc_client = mock.AsyncMock()
    # Internal stream class patch
    stream_patcher = mock.patch(
        "google.cloud.storage.asyncio.async_appendable_object_writer._AsyncWriteObjectStream"
    )
    mock_stream_cls = stream_patcher.start()
    mock_stream = mock_stream_cls.return_value

    # Configure all async methods explicitly
    mock_stream.open = AsyncMock()
    mock_stream.close = AsyncMock()
    mock_stream.send = AsyncMock()
    mock_stream.recv = AsyncMock()

    # Default mock properties
    mock_stream.is_stream_open = False
    mock_stream.persisted_size = 0
    mock_stream.generation_number = GENERATION
    mock_stream.write_handle = WRITE_HANDLE
    mock_stream.storage_class = None

    def _create_stream(*args, **kwargs):
        mock_stream.storage_class = kwargs.get("storage_class")
        return mock_stream

    mock_stream_cls.side_effect = _create_stream

    yield {
        "mock_client": mock_client,
        "mock_stream": mock_stream,
        "mock_stream_cls": mock_stream_cls,
    }

    stream_patcher.stop()


class TestAsyncAppendableObjectWriter:
    def _make_one(self, mock_client, **kwargs):
        return AsyncAppendableObjectWriter(mock_client, BUCKET, OBJECT, **kwargs)

    # -------------------------------------------------------------------------
    # Initialization & Configuration Tests
    # -------------------------------------------------------------------------

    def test_init_defaults(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        assert writer.bucket_name == BUCKET
        assert writer.object_name == OBJECT
        assert writer.persisted_size is None
        assert writer.bytes_appended_since_last_flush == 0
        assert writer.flush_interval == _DEFAULT_FLUSH_INTERVAL_BYTES
        assert writer.storage_class is None

    @pytest.mark.asyncio
    @pytest.mark.parametrize("storage_class", ["STANDARD", "RAPID"])
    async def test_init_with_storage_class(self, mock_appendable_writer, storage_class):
        writer = self._make_one(
            mock_appendable_writer["mock_client"],
            storage_class=storage_class,
        )
        assert writer.storage_class == storage_class

        mock_appendable_writer["mock_stream"].generation_number = 456
        mock_appendable_writer["mock_stream"].write_handle = b"new-h"
        mock_appendable_writer["mock_stream"].persisted_size = 0

        await writer.open()

        assert writer._is_stream_open
        mock_stream_cls = mock_appendable_writer["mock_stream_cls"]
        mock_stream_cls.assert_called_once_with(
            client=mock_appendable_writer["mock_client"].grpc_client,
            bucket_name=BUCKET,
            object_name=OBJECT,
            blob=None,
            generation_number=None,
            write_handle=None,
            routing_token=None,
            storage_class=storage_class,
        )
        assert writer.write_obj_stream.storage_class == storage_class

    def test_init_with_writer_options(self, mock_appendable_writer):
        writer = self._make_one(
            mock_appendable_writer["mock_client"],
            writer_options={"FLUSH_INTERVAL_BYTES": EIGHT_MIB},
        )
        assert writer.flush_interval == EIGHT_MIB

    def test_init_validation_chunk_size_raises(self, mock_appendable_writer):
        with pytest.raises(exceptions.OutOfRange):
            self._make_one(
                mock_appendable_writer["mock_client"],
                writer_options={"FLUSH_INTERVAL_BYTES": _MAX_CHUNK_SIZE_BYTES - 1},
            )

    def test_init_validation_multiple_raises(self, mock_appendable_writer):
        with pytest.raises(exceptions.OutOfRange):
            self._make_one(
                mock_appendable_writer["mock_client"],
                writer_options={"FLUSH_INTERVAL_BYTES": _MAX_CHUNK_SIZE_BYTES + 1},
            )

    def test_init_raises_if_crc32c_missing(self, mock_appendable_writer):
        with mock.patch(
            "google.cloud.storage.asyncio._utils.google_crc32c"
        ) as mock_crc:
            mock_crc.implementation = "python"
            with pytest.raises(exceptions.FailedPrecondition):
                self._make_one(mock_appendable_writer["mock_client"])

    def test_from_blob(self, mock_appendable_writer):
        mock_blob = mock.Mock(spec=Blob)
        mock_blob.name = OBJECT
        mock_blob.bucket.name = BUCKET
        mock_blob.generation = GENERATION
        mock_blob.storage_class = "RAPID"

        writer = AsyncAppendableObjectWriter.from_blob(
            mock_appendable_writer["mock_client"],
            mock_blob,
            writer_options={"FLUSH_INTERVAL_BYTES": EIGHT_MIB},
        )

        assert writer.bucket_name == BUCKET
        assert writer.object_name == OBJECT
        assert writer.generation == GENERATION
        assert writer.flush_interval == EIGHT_MIB
        assert writer.blob == mock_blob
        assert writer.storage_class == "RAPID"

    @pytest.mark.parametrize("storage_class", ["STANDARD", "RAPID", None])
    def test_from_blob_storage_class(self, mock_appendable_writer, storage_class):
        mock_blob = mock.Mock(spec=Blob)
        mock_blob.name = OBJECT
        mock_blob.bucket.name = BUCKET
        mock_blob.generation = GENERATION
        mock_blob.storage_class = storage_class

        writer = AsyncAppendableObjectWriter.from_blob(
            mock_appendable_writer["mock_client"],
            mock_blob,
        )

        assert writer.storage_class == storage_class

    @pytest.mark.asyncio
    @pytest.mark.parametrize("storage_class", ["STANDARD", "RAPID"])
    async def test_from_blob_open_passes_storage_class(
        self, mock_appendable_writer, storage_class
    ):
        mock_blob = mock.Mock(spec=Blob)
        mock_blob.name = OBJECT
        mock_blob.bucket.name = BUCKET
        mock_blob.generation = GENERATION
        mock_blob.storage_class = storage_class

        writer = AsyncAppendableObjectWriter.from_blob(
            mock_appendable_writer["mock_client"],
            mock_blob,
        )
        mock_appendable_writer["mock_stream"].generation_number = 456
        mock_appendable_writer["mock_stream"].write_handle = b"new-h"
        mock_appendable_writer["mock_stream"].persisted_size = 0

        await writer.open()

        assert writer._is_stream_open
        mock_stream_cls = mock_appendable_writer["mock_stream_cls"]
        mock_stream_cls.assert_called_once_with(
            client=mock_appendable_writer["mock_client"].grpc_client,
            bucket_name=BUCKET,
            object_name=OBJECT,
            blob=mock_blob,
            generation_number=GENERATION,
            write_handle=None,
            routing_token=None,
            storage_class=storage_class,
        )
        assert writer.write_obj_stream.storage_class == storage_class

    # -------------------------------------------------------------------------
    # Stream Lifecycle Tests
    # -------------------------------------------------------------------------

    @pytest.mark.asyncio
    async def test_state_lookup(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]

        mock_appendable_writer[
            "mock_stream"
        ].recv.return_value = storage_type.BidiWriteObjectResponse(persisted_size=100)

        size = await writer.state_lookup()

        mock_appendable_writer["mock_stream"].send.assert_awaited_once()
        assert size == 100
        assert writer.persisted_size == 100

    @pytest.mark.asyncio
    async def test_open_success(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        mock_appendable_writer["mock_stream"].generation_number = 456
        mock_appendable_writer["mock_stream"].write_handle = b"new-h"
        mock_appendable_writer["mock_stream"].persisted_size = 0

        await writer.open()

        assert writer._is_stream_open
        assert writer.generation == 456
        assert writer.write_handle == b"new-h"
        mock_appendable_writer["mock_stream"].open.assert_awaited_once()
        mock_stream_cls = mock_appendable_writer["mock_stream_cls"]
        assert mock_stream_cls.call_args.kwargs["storage_class"] is None
        assert writer.write_obj_stream.storage_class is None

    def test_on_open_error_redirection(self, mock_appendable_writer):
        """Verify redirect info is extracted from helper."""
        writer = self._make_one(mock_appendable_writer["mock_client"])
        redirect = BidiWriteObjectRedirectedError(
            routing_token="rt1",
            write_handle=storage_type.BidiWriteHandle(handle=b"h1"),
            generation=777,
        )

        with mock.patch(
            "google.cloud.storage.asyncio.async_appendable_object_writer._extract_bidi_writes_redirect_proto",
            return_value=redirect,
        ):
            writer._on_open_error(exceptions.Aborted("redirect"))

        assert writer._routing_token == "rt1"
        assert writer.write_handle.handle == b"h1"
        assert writer.generation == 777

    @pytest.mark.asyncio
    async def test_open_closes_existing_stream(self, mock_appendable_writer):
        """Verify proper cleanup of existing stream on re-open."""
        writer = self._make_one(mock_appendable_writer["mock_client"])
        # We simulate a state where write_obj_stream exists but we are opening (e.g. retry or stale)
        writer._is_stream_open = False
        # Set an existing stream
        old_stream = mock.AsyncMock()
        old_stream.is_stream_open = True
        writer.write_obj_stream = old_stream

        # Mock the creation of NEW stream to avoid overwriting our old_stream reference too early if we needed it,
        # but here we just want to verify old_stream.close() is called.

        # Act
        await writer.open()

        # Assert
        old_stream.close.assert_awaited_once()
        assert writer.write_obj_stream != old_stream
        assert writer._is_stream_open

    @pytest.mark.asyncio
    async def test_open_logs_warning_on_close_error(self, mock_appendable_writer):
        """Verify logging when closing existing stream fails."""
        writer = self._make_one(mock_appendable_writer["mock_client"])
        old_stream = mock.AsyncMock()
        old_stream.is_stream_open = True
        old_stream.close.side_effect = ValueError("close failed")
        writer.write_obj_stream = old_stream
        writer._is_stream_open = False

        with mock.patch(
            "google.cloud.storage.asyncio.async_appendable_object_writer.logger"
        ) as mock_logger:
            await writer.open()

            mock_logger.warning.assert_called_once()
            args, _ = mock_logger.warning.call_args
            assert "Error closing previous write stream" in args[0]
            assert "close failed" in args[0]

    # -------------------------------------------------------------------------
    # Append Tests
    # -------------------------------------------------------------------------

    @pytest.mark.asyncio
    async def test_append_data_less_than_flush_interval(self, mock_appendable_writer):
        """Verify append orchestrates manager and drives the internal generator."""
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.persisted_size = 0
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]
        writer.write_obj_stream.send = AsyncMock()

        data_len = len(DATA_LESS_THAN_FLUSH_INTERVAL)
        await writer.append(DATA_LESS_THAN_FLUSH_INTERVAL)

        assert writer.offset == data_len
        assert writer.bytes_appended_since_last_flush == data_len

    @pytest.mark.asyncio
    async def test_append_with_checksum_disabled(self, mock_appendable_writer):
        """Verify append propagates enable_checksum=False to the _WriteState."""
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.persisted_size = 0
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]
        writer.write_obj_stream.send = AsyncMock()

        with mock.patch(
            "google.cloud.storage.asyncio.async_appendable_object_writer._BidiStreamRetryManager"
        ) as MockManager:
            mock_execute = AsyncMock()
            MockManager.return_value.execute = mock_execute

            await writer.append(DATA_LESS_THAN_FLUSH_INTERVAL, enable_checksum=False)

            # Check that execute was called with a state dictionary containing write_state having enable_checksum=False
            mock_execute.assert_called_once()
            state_arg = mock_execute.call_args[0][0]
            assert "write_state" in state_arg
            assert state_arg["write_state"].enable_checksum is False

    @pytest.mark.parametrize(
        "data_len",
        [
            _DEFAULT_FLUSH_INTERVAL_BYTES - 1,
            _DEFAULT_FLUSH_INTERVAL_BYTES,
            _DEFAULT_FLUSH_INTERVAL_BYTES + 1,
        ],
    )
    @pytest.mark.asyncio
    async def test_append(self, data_len, mock_appendable_writer):
        """Verify append orchestrates manager and drives the internal generator."""
        # Arrange
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.persisted_size = 0
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]
        writer.write_obj_stream.send = AsyncMock()

        # if data > flush interval then we expect 1 flush & 1 state_lookup going through
        # which means we will do 1 recv() call.
        writer.write_obj_stream.recv = AsyncMock(
            return_value=storage_type.BidiWriteObjectResponse(
                persisted_size=_DEFAULT_FLUSH_INTERVAL_BYTES
            )
        )
        data = b"a" * data_len

        # Act
        await writer.append(data)

        # Assert
        expected_recv_count = data_len // _DEFAULT_FLUSH_INTERVAL_BYTES
        assert writer.offset == data_len
        assert (
            writer.bytes_appended_since_last_flush
            == data_len % _DEFAULT_FLUSH_INTERVAL_BYTES
        )
        assert (
            writer.persisted_size == expected_recv_count * _DEFAULT_FLUSH_INTERVAL_BYTES
        )
        assert writer.write_obj_stream.send.await_count == -(
            -data_len // _MAX_CHUNK_SIZE_BYTES
        )  # Ceiling division for number of chunks
        assert (
            writer.write_obj_stream.recv.await_count == expected_recv_count
        )  # Expect 1 recv per flush interval

    @pytest.mark.asyncio
    async def test_append_recovery_reopens_stream(self, mock_appendable_writer):
        """Verifies re-opening logic on retry."""
        writer = self._make_one(
            mock_appendable_writer["mock_client"], write_handle=b"h1"
        )
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]
        # Setup mock to allow close() call
        mock_appendable_writer["mock_stream"].is_stream_open = True

        async def mock_open(metadata=None):
            writer.write_obj_stream = mock_appendable_writer["mock_stream"]
            writer._is_stream_open = True
            writer.persisted_size = 5
            writer.write_handle = b"h_recovered"

        with mock.patch.object(
            writer, "open", side_effect=mock_open
        ) as mock_writer_open:
            with mock.patch(
                "google.cloud.storage.asyncio.async_appendable_object_writer._BidiStreamRetryManager"
            ) as MockManager:

                async def mock_execute(state, policy):
                    factory = MockManager.call_args[0][1]
                    # Simulate Attempt 1 fail
                    gen1 = factory([], state)
                    try:
                        await gen1.__anext__()
                    except Exception:
                        pass
                    # Simulate Attempt 2
                    gen2 = factory([], state)
                    mock_appendable_writer["mock_stream"].recv.return_value = None
                    async for _ in gen2:
                        pass

                MockManager.return_value.execute.side_effect = mock_execute
                await writer.append(b"0123456789")

                # mock_appendable_writer["mock_stream"].close.assert_awaited() # Removed because open() is mocked
                mock_writer_open.assert_awaited()
                assert writer.persisted_size == 5

    @pytest.mark.asyncio
    async def test_append_unimplemented_string_raises(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        with pytest.raises(NotImplementedError):
            await writer.append_from_string("test")

    # -------------------------------------------------------------------------
    # Flush, Close, Finalize
    # -------------------------------------------------------------------------

    @pytest.mark.asyncio
    async def test_flush_resets_counters(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]
        writer.bytes_appended_since_last_flush = 100

        mock_appendable_writer[
            "mock_stream"
        ].recv.return_value = storage_type.BidiWriteObjectResponse(persisted_size=200)

        await writer.flush()

        assert writer.bytes_appended_since_last_flush == 0
        assert writer.persisted_size == 200

    @pytest.mark.asyncio
    async def test_simple_flush(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]
        writer.bytes_appended_since_last_flush = 50

        await writer.simple_flush()

        mock_appendable_writer["mock_stream"].send.assert_awaited_with(
            storage_type.BidiWriteObjectRequest(flush=True)
        )
        assert writer.bytes_appended_since_last_flush == 0

    @pytest.mark.asyncio
    async def test_close_without_finalize(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]
        writer.persisted_size = 50

        size = await writer.close()

        mock_appendable_writer["mock_stream"].close.assert_awaited()
        assert not writer._is_stream_open
        assert size == 50

    @pytest.mark.asyncio
    async def test_finalize_lifecycle(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]

        resource = storage_type.Object(size=999)
        mock_appendable_writer[
            "mock_stream"
        ].recv.return_value = storage_type.BidiWriteObjectResponse(resource=resource)

        res = await writer.finalize()

        assert res == resource
        assert writer.persisted_size == 999
        mock_appendable_writer["mock_stream"].send.assert_awaited_with(
            storage_type.BidiWriteObjectRequest(finish_write=True)
        )
        mock_appendable_writer["mock_stream"].close.assert_awaited()
        assert not writer._is_stream_open

    @pytest.mark.asyncio
    async def test_close_with_finalize_on_close(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.finalize = AsyncMock()

        await writer.close(finalize_on_close=True)
        writer.finalize.assert_awaited_once()

    # -------------------------------------------------------------------------
    # Helper Tests
    # -------------------------------------------------------------------------

    @pytest.mark.asyncio
    async def test_append_from_file(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.append = AsyncMock()

        fp = io.BytesIO(b"a" * 12)
        await writer.append_from_file(fp, block_size=4)

        assert writer.append.await_count == 3

    @pytest.mark.asyncio
    async def test_methods_require_open_stream_raises(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        methods = [
            writer.append(b"data"),
            writer.flush(),
            writer.simple_flush(),
            writer.close(),
            writer.finalize(),
            writer.state_lookup(),
        ]
        for coro in methods:
            with pytest.raises(ValueError, match="Stream is not open"):
                await coro

    @pytest.mark.asyncio
    async def test_finalize_with_checksum(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]

        resource = storage_type.Object(size=999)
        mock_appendable_writer[
            "mock_stream"
        ].recv.return_value = storage_type.BidiWriteObjectResponse(resource=resource)

        checksum = 12345678
        res = await writer.finalize(full_object_checksum=checksum)

        assert res == resource
        assert writer.persisted_size == 999
        mock_appendable_writer["mock_stream"].send.assert_awaited_with(
            storage_type.BidiWriteObjectRequest(
                finish_write=True,
                object_checksums=storage_type.ObjectChecksums(crc32c=checksum),
            )
        )
        mock_appendable_writer["mock_stream"].close.assert_awaited()
        assert not writer._is_stream_open

    @pytest.mark.asyncio
    async def test_close_with_checksum_and_finalize(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.finalize = AsyncMock()

        checksum = 12345678
        await writer.close(finalize_on_close=True, full_object_checksum=checksum)
        writer.finalize.assert_awaited_once_with(
            full_object_checksum=checksum, retry_policy=None
        )

    @pytest.mark.asyncio
    async def test_close_with_checksum_without_finalize_raises(
        self, mock_appendable_writer
    ):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True

        checksum = 12345678
        with pytest.raises(
            ValueError,
            match="full_object_checksum can only be provided when finalize_on_close is True",
        ):
            await writer.close(finalize_on_close=False, full_object_checksum=checksum)

    @pytest.mark.asyncio
    async def test_finalize_invalid_checksum_type(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]

        with pytest.raises(TypeError, match="full_object_checksum must be an integer"):
            await writer.finalize(full_object_checksum="not-an-int")

        with pytest.raises(TypeError, match="full_object_checksum must be an integer"):
            await writer.finalize(full_object_checksum=True)

    @pytest.mark.asyncio
    async def test_finalize_invalid_checksum_range(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]

        # negative
        with pytest.raises(
            ValueError, match="full_object_checksum must be a 32-bit unsigned integer"
        ):
            await writer.finalize(full_object_checksum=-1)

        # overflow
        with pytest.raises(
            ValueError, match="full_object_checksum must be a 32-bit unsigned integer"
        ):
            await writer.finalize(full_object_checksum=0x100000000)

    @pytest.mark.asyncio
    async def test_finalize_mismatch_closes_stream(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]

        # Mock recv to raise an exception (like server rejecting checksum mismatch)
        from google.api_core.exceptions import InvalidArgument

        mock_appendable_writer["mock_stream"].recv.side_effect = InvalidArgument(
            "checksum mismatch"
        )

        with pytest.raises(InvalidArgument):
            await writer.finalize(full_object_checksum=12345)

        # Assert stream was closed and local state reset despite exception
        mock_appendable_writer["mock_stream"].close.assert_awaited()
        assert not writer._is_stream_open

    @pytest.mark.asyncio
    async def test_finalize_retry_on_transient_error(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]

        resource = storage_type.Object(size=999)
        mock_appendable_writer["mock_stream"].recv.side_effect = [
            exceptions.InternalServerError("500 Transient Error"),
            storage_type.BidiWriteObjectResponse(resource=resource),
        ]

        res = await writer.finalize()

        assert res == resource
        assert writer.persisted_size == 999
        assert mock_appendable_writer["mock_stream"].send.await_count == 2
        assert mock_appendable_writer["mock_stream"].recv.await_count == 2
        assert not writer._is_stream_open

    @pytest.mark.asyncio
    async def test_finalize_custom_retry_policy(self, mock_appendable_writer):
        from google.api_core.retry_async import AsyncRetry

        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]

        custom_policy = AsyncRetry(
            predicate=lambda exc: isinstance(exc, exceptions.InternalServerError)
        )
        resource = storage_type.Object(size=999)
        mock_appendable_writer[
            "mock_stream"
        ].recv.return_value = storage_type.BidiWriteObjectResponse(resource=resource)

        res = await writer.finalize(retry_policy=custom_policy)

        assert res == resource
        assert writer.persisted_size == 999
        assert mock_appendable_writer["mock_stream"].send.await_count == 1
        assert mock_appendable_writer["mock_stream"].recv.await_count == 1
        assert not writer._is_stream_open

    @pytest.mark.asyncio
    async def test_close_with_finalize_and_custom_retry_policy(
        self, mock_appendable_writer
    ):
        from google.api_core.retry_async import AsyncRetry

        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]

        custom_policy = AsyncRetry(
            predicate=lambda exc: isinstance(exc, exceptions.InternalServerError)
        )
        resource = storage_type.Object(size=999)
        mock_appendable_writer[
            "mock_stream"
        ].recv.return_value = storage_type.BidiWriteObjectResponse(resource=resource)

        res = await writer.close(finalize_on_close=True, retry_policy=custom_policy)

        assert res == resource
        assert writer.persisted_size == 999
        assert mock_appendable_writer["mock_stream"].send.await_count == 1
        assert mock_appendable_writer["mock_stream"].recv.await_count == 1
        assert not writer._is_stream_open

    @pytest.mark.asyncio
    async def test_close_retry_on_transient_error(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]

        resource = storage_type.Object(size=999)
        mock_appendable_writer["mock_stream"].recv.side_effect = [
            exceptions.InternalServerError("500 Transient Error"),
            storage_type.BidiWriteObjectResponse(resource=resource),
        ]

        res = await writer.close(finalize_on_close=True)

        assert res == resource
        assert writer.persisted_size == 999
        assert mock_appendable_writer["mock_stream"].send.await_count == 2
        assert mock_appendable_writer["mock_stream"].recv.await_count == 2
        assert not writer._is_stream_open

    @pytest.mark.asyncio
    async def test_finalize_retry_on_redirect_error(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]

        redirect = BidiWriteObjectRedirectedError(
            routing_token="rt1",
            write_handle=storage_type.BidiWriteHandle(handle=b"h1"),
        )
        exc = exceptions.Aborted("aborted", errors=[redirect])

        resource = storage_type.Object(size=999)
        mock_appendable_writer["mock_stream"].recv.side_effect = [
            exc,
            storage_type.BidiWriteObjectResponse(resource=resource),
        ]

        writer.open = mock.AsyncMock()

        res = await writer.finalize()

        assert res == resource
        assert writer.persisted_size == 999
        assert mock_appendable_writer["mock_stream"].send.await_count == 2
        assert mock_appendable_writer["mock_stream"].recv.await_count == 2
        assert writer._routing_token == "rt1"
        assert writer.write_handle.handle == b"h1"
        writer.open.assert_awaited_once()
        assert not writer._is_stream_open

    @pytest.mark.asyncio
    async def test_close_retry_on_redirect_error(self, mock_appendable_writer):
        writer = self._make_one(mock_appendable_writer["mock_client"])
        writer._is_stream_open = True
        writer.write_obj_stream = mock_appendable_writer["mock_stream"]

        redirect = BidiWriteObjectRedirectedError(
            routing_token="rt2",
            write_handle=storage_type.BidiWriteHandle(handle=b"h2"),
        )
        exc = exceptions.Aborted("aborted", errors=[redirect])

        mock_appendable_writer["mock_stream"].close.side_effect = [
            exc,
            None,
        ]

        writer.open = mock.AsyncMock()
        writer.persisted_size = 999

        res = await writer.close()

        assert res == 999
        assert mock_appendable_writer["mock_stream"].close.await_count == 2
        assert writer._routing_token == "rt2"
        assert writer.write_handle.handle == b"h2"
        writer.open.assert_awaited_once()
        assert not writer._is_stream_open
