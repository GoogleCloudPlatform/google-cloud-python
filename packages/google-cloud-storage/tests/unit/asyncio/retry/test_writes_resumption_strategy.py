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
from datetime import datetime

import google_crc32c
import pytest
from google.api_core import exceptions
from google.rpc import status_pb2

from google.cloud._storage_v2.types import storage as storage_type
from google.cloud._storage_v2.types.storage import BidiWriteObjectRedirectedError
from google.cloud.storage.asyncio.retry.writes_resumption_strategy import (
    _WriteResumptionStrategy,
    _WriteState,
)


@pytest.fixture
def strategy():
    """Fixture to provide a WriteResumptionStrategy instance."""
    return _WriteResumptionStrategy()


class TestWriteResumptionStrategy:
    """Test suite for WriteResumptionStrategy."""

    # -------------------------------------------------------------------------
    # Tests for generate_requests
    # -------------------------------------------------------------------------

    def test_generate_requests_initial_chunking(self, strategy):
        """Verify initial data generation starts at offset 0 and chunks correctly."""
        mock_buffer = io.BytesIO(b"abcdefghij")
        write_state = _WriteState(
            chunk_size=3, user_buffer=mock_buffer, flush_interval=10
        )
        state = {"write_state": write_state}

        requests = strategy.generate_requests(state)

        # Expected: 4 requests (3, 3, 3, 1)
        assert len(requests) == 4

        # Verify Request 1
        assert requests[0].write_offset == 0
        assert requests[0].checksummed_data.content == b"abc"

        # Verify Request 2
        assert requests[1].write_offset == 3
        assert requests[1].checksummed_data.content == b"def"

        # Verify Request 3
        assert requests[2].write_offset == 6
        assert requests[2].checksummed_data.content == b"ghi"

        # Verify Request 4
        assert requests[3].write_offset == 9
        assert requests[3].checksummed_data.content == b"j"

    def test_generate_requests_resumption(self, strategy):
        """
        Verify request generation when resuming.
        The strategy should generate chunks starting from the current 'bytes_sent'.
        """
        mock_buffer = io.BytesIO(b"0123456789")
        write_state = _WriteState(
            chunk_size=4, user_buffer=mock_buffer, flush_interval=10
        )

        # Simulate resumption state: 4 bytes already sent/persisted
        write_state.persisted_size = 4
        write_state.bytes_sent = 4
        # Buffer must be seeked to 4 before calling generate
        mock_buffer.seek(4)

        state = {"write_state": write_state}

        requests = strategy.generate_requests(state)

        # Since 4 bytes are done, we expect remaining 6 bytes: [4 bytes, 2 bytes]
        assert len(requests) == 2

        # Check first generated request starts at offset 4
        assert requests[0].write_offset == 4
        assert requests[0].checksummed_data.content == b"4567"

        # Check second generated request starts at offset 8
        assert requests[1].write_offset == 8
        assert requests[1].checksummed_data.content == b"89"

    def test_generate_requests_empty_file(self, strategy):
        """Verify request sequence for an empty file."""
        mock_buffer = io.BytesIO(b"")
        write_state = _WriteState(
            chunk_size=4, user_buffer=mock_buffer, flush_interval=10
        )
        state = {"write_state": write_state}

        requests = strategy.generate_requests(state)

        assert len(requests) == 0

    def test_generate_requests_checksum_verification(self, strategy):
        """Verify CRC32C is calculated correctly for each chunk."""
        chunk_data = b"test_data"
        mock_buffer = io.BytesIO(chunk_data)
        write_state = _WriteState(
            chunk_size=10, user_buffer=mock_buffer, flush_interval=10
        )
        state = {"write_state": write_state}

        requests = strategy.generate_requests(state)

        expected_int = google_crc32c.value(chunk_data)
        assert requests[0].checksummed_data.crc32c == expected_int

    def test_generate_requests_checksum_disabled(self, strategy):
        """Verify CRC32C is not calculated if enable_checksum is False."""
        chunk_data = b"test_data"
        mock_buffer = io.BytesIO(chunk_data)
        write_state = _WriteState(
            chunk_size=10,
            user_buffer=mock_buffer,
            flush_interval=10,
            enable_checksum=False,
        )
        state = {"write_state": write_state}

        requests = strategy.generate_requests(state)

        assert not requests[0].checksummed_data.crc32c

    def test_generate_requests_flush_logic_exact_interval(self, strategy):
        """Verify the flush bit is set exactly when the interval is reached."""
        mock_buffer = io.BytesIO(b"A" * 12)
        # 2 byte chunks, flush every 4 bytes
        write_state = _WriteState(
            chunk_size=2, user_buffer=mock_buffer, flush_interval=4
        )
        state = {"write_state": write_state}

        requests = strategy.generate_requests(state)

        # Request index 1 (4 bytes total) should have flush=True
        assert requests[0].flush is False
        assert requests[1].flush is True

        # Request index 2 (8 bytes total) should have flush=True
        assert requests[2].flush is False
        assert requests[3].flush is True

        # Request index 3 (12 bytes total) should have flush=True
        assert requests[4].flush is False
        assert requests[5].flush is True

        # Verify counter reset in state
        assert write_state.bytes_since_last_flush == 0

    def test_generate_requests_flush_logic_data_less_than_interval(self, strategy):
        """Verify flush is not set if data sent is less than interval."""
        mock_buffer = io.BytesIO(b"A" * 5)
        # Flush every 10 bytes
        write_state = _WriteState(
            chunk_size=2, user_buffer=mock_buffer, flush_interval=10
        )
        state = {"write_state": write_state}

        requests = strategy.generate_requests(state)

        # Total 5 bytes < 10 bytes interval
        for req in requests:
            assert req.flush is False

        assert write_state.bytes_since_last_flush == 5

    def test_generate_requests_honors_finalized_state(self, strategy):
        """If state is already finalized, no requests should be generated."""
        mock_buffer = io.BytesIO(b"data")
        write_state = _WriteState(
            chunk_size=4, user_buffer=mock_buffer, flush_interval=10
        )
        write_state.is_finalized = True
        state = {"write_state": write_state}

        requests = strategy.generate_requests(state)
        assert len(requests) == 0

    @pytest.mark.asyncio
    async def test_generate_requests_after_failure_and_recovery(self, strategy):
        """
        Verify recovery and resumption flow (Integration of recover + generate).
        """
        mock_buffer = io.BytesIO(b"0123456789abcdef")  # 16 bytes
        write_state = _WriteState(
            chunk_size=4, user_buffer=mock_buffer, flush_interval=10
        )
        state = {"write_state": write_state}

        # Simulate initial progress: sent 8 bytes
        write_state.bytes_sent = 8
        mock_buffer.seek(8)

        strategy.update_state_from_response(
            storage_type.BidiWriteObjectResponse(
                persisted_size=4,
                write_handle=storage_type.BidiWriteHandle(handle=b"handle-1"),
            ),
            state,
        )

        # Simulate Failure Triggering Recovery
        await strategy.recover_state_on_failure(Exception("network error"), state)

        # Assertions after recovery
        # 1. Buffer should rewind to persisted_size (4)
        assert mock_buffer.tell() == 4
        # 2. bytes_sent should track persisted_size (4)
        assert write_state.bytes_sent == 4

        requests = strategy.generate_requests(state)

        # Remaining data from offset 4 to 16 (12 bytes total)
        # Chunks: [4-8], [8-12], [12-16]
        assert len(requests) == 3

        # Verify resumption offset
        assert requests[0].write_offset == 4
        assert requests[0].checksummed_data.content == b"4567"

    # -------------------------------------------------------------------------
    # Tests for update_state_from_response
    # -------------------------------------------------------------------------

    def test_update_state_from_response_all_fields(self, strategy):
        """Verify all fields from a BidiWriteObjectResponse update the state."""
        write_state = _WriteState(
            chunk_size=4, user_buffer=io.BytesIO(), flush_interval=10
        )
        state = {"write_state": write_state}

        # 1. Update persisted_size
        strategy.update_state_from_response(
            storage_type.BidiWriteObjectResponse(persisted_size=123), state
        )
        assert write_state.persisted_size == 123

        # 2. Update write_handle
        handle = storage_type.BidiWriteHandle(handle=b"new-handle")
        strategy.update_state_from_response(
            storage_type.BidiWriteObjectResponse(write_handle=handle), state
        )
        assert write_state.write_handle == handle

        # 3. Update from Resource (finalization)
        resource = storage_type.Object(size=1000, finalize_time=datetime.now())
        strategy.update_state_from_response(
            storage_type.BidiWriteObjectResponse(resource=resource), state
        )
        assert write_state.persisted_size == 1000
        assert write_state.is_finalized

    def test_update_state_from_response_none(self, strategy):
        """Verify None response doesn't crash."""
        write_state = _WriteState(
            chunk_size=4, user_buffer=io.BytesIO(), flush_interval=10
        )
        state = {"write_state": write_state}
        strategy.update_state_from_response(None, state)
        assert write_state.persisted_size == 0

    # -------------------------------------------------------------------------
    # Tests for recover_state_on_failure
    # -------------------------------------------------------------------------

    @pytest.mark.asyncio
    async def test_recover_state_on_failure_rewind_logic(self, strategy):
        """Verify buffer seek and counter resets on generic failure (Non-redirect)."""
        mock_buffer = io.BytesIO(b"0123456789")
        write_state = _WriteState(
            chunk_size=2, user_buffer=mock_buffer, flush_interval=100
        )

        # Simulate progress: sent 8 bytes, but server only persisted 4
        write_state.bytes_sent = 8
        write_state.persisted_size = 4
        write_state.bytes_since_last_flush = 2
        mock_buffer.seek(8)

        # Simulate generic 503 error without trailers
        await strategy.recover_state_on_failure(
            exceptions.ServiceUnavailable("busy"), {"write_state": write_state}
        )

        # Buffer must be seeked back to 4
        assert mock_buffer.tell() == 4
        assert write_state.bytes_sent == 4
        # Flush counter must be reset to avoid incorrect firing after resume
        assert write_state.bytes_since_last_flush == 0

    @pytest.mark.asyncio
    async def test_recover_state_on_failure_direct_redirect(self, strategy):
        """Verify handling when the error is a BidiWriteObjectRedirectedError."""
        write_state = _WriteState(
            chunk_size=4, user_buffer=io.BytesIO(), flush_interval=100
        )
        state = {"write_state": write_state}

        redirect = BidiWriteObjectRedirectedError(
            routing_token="tok-1",
            write_handle=storage_type.BidiWriteHandle(handle=b"h-1"),
        )

        await strategy.recover_state_on_failure(redirect, state)

        assert write_state.routing_token == "tok-1"
        assert write_state.write_handle.handle == b"h-1"

    @pytest.mark.asyncio
    async def test_recover_state_on_failure_wrapped_redirect(self, strategy):
        """Verify handling when RedirectedError is inside Aborted.errors."""
        write_state = _WriteState(
            chunk_size=4, user_buffer=io.BytesIO(), flush_interval=10
        )

        redirect = BidiWriteObjectRedirectedError(routing_token="tok-wrapped")
        # google-api-core Aborted often wraps multiple errors
        error = exceptions.Aborted("conflict", errors=[redirect])

        await strategy.recover_state_on_failure(error, {"write_state": write_state})

        assert write_state.routing_token == "tok-wrapped"

    @pytest.mark.asyncio
    async def test_recover_state_on_failure_trailer_metadata_redirect(self, strategy):
        """Verify complex parsing from 'grpc-status-details-bin' in trailers."""
        write_state = _WriteState(
            chunk_size=4, user_buffer=io.BytesIO(), flush_interval=10
        )

        redirect_proto = BidiWriteObjectRedirectedError(routing_token="metadata-token")
        status = status_pb2.Status()
        detail = status.details.add()
        detail.type_url = (
            "type.googleapis.com/google.storage.v2.BidiWriteObjectRedirectedError"
        )
        detail.value = BidiWriteObjectRedirectedError.serialize(redirect_proto)

        # FIX: No spec= here, because Aborted doesn't have trailing_metadata in its base definition
        mock_error = mock.MagicMock()
        mock_error.errors = []
        mock_error.trailing_metadata.return_value = [
            ("grpc-status-details-bin", status.SerializeToString())
        ]

        with mock.patch(
            "google.cloud.storage.asyncio.retry.writes_resumption_strategy._extract_bidi_writes_redirect_proto",
            return_value=redirect_proto,
        ):
            await strategy.recover_state_on_failure(
                mock_error, {"write_state": write_state}
            )

        assert write_state.routing_token == "metadata-token"

    def test_write_state_initialization(self):
        """Verify WriteState starts with clean counters."""
        buffer = io.BytesIO(b"test")
        ws = _WriteState(chunk_size=10, user_buffer=buffer, flush_interval=100)

        assert ws.persisted_size == 0
        assert ws.bytes_sent == 0
        assert ws.bytes_since_last_flush == 0
        assert ws.flush_interval == 100
        assert not ws.is_finalized
