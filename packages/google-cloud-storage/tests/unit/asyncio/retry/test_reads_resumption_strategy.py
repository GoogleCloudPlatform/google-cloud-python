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
import io
import unittest

import google_crc32c
from google.api_core import exceptions

from google.cloud import _storage_v2 as storage_v2
from google.cloud._storage_v2.types.storage import BidiReadObjectRedirectedError
from google.cloud.storage.asyncio.retry.reads_resumption_strategy import (
    _DownloadState,
    _ReadResumptionStrategy,
)
from google.cloud.storage.exceptions import DataCorruption

_READ_ID = 1
LOGGER_NAME = "google.cloud.storage.asyncio.retry.reads_resumption_strategy"


class TestDownloadState(unittest.TestCase):
    def test_initialization(self):
        """Test that _DownloadState initializes correctly."""
        initial_offset = 10
        initial_length = 100
        user_buffer = io.BytesIO()
        state = _DownloadState(initial_offset, initial_length, user_buffer)

        self.assertEqual(state.initial_offset, initial_offset)
        self.assertEqual(state.initial_length, initial_length)
        self.assertEqual(state.user_buffer, user_buffer)
        self.assertEqual(state.bytes_written, 0)
        self.assertEqual(state.next_expected_offset, initial_offset)
        self.assertFalse(state.is_complete)
        self.assertFalse(state.is_full_object_read)
        self.assertIsNone(state.rolling_checksum)

    def test_initialization_with_full_object_read(self):
        """Test that _DownloadState initializes correctly when is_full_object_read is True."""
        initial_offset = 10
        initial_length = 100
        user_buffer = io.BytesIO()
        state_full = _DownloadState(
            initial_offset, initial_length, user_buffer, is_full_object_read=True
        )

        self.assertEqual(state_full.initial_offset, initial_offset)
        self.assertEqual(state_full.initial_length, initial_length)
        self.assertEqual(state_full.user_buffer, user_buffer)
        self.assertEqual(state_full.bytes_written, 0)
        self.assertEqual(state_full.next_expected_offset, initial_offset)
        self.assertFalse(state_full.is_complete)
        self.assertTrue(state_full.is_full_object_read)
        self.assertIsNotNone(state_full.rolling_checksum)

    def test_initialization_with_full_object_read_and_checksum_disabled(self):
        """Test that _DownloadState does not initialize rolling_checksum when enable_checksum is False."""
        initial_offset = 10
        initial_length = 100
        user_buffer = io.BytesIO()
        state_full = _DownloadState(
            initial_offset,
            initial_length,
            user_buffer,
            is_full_object_read=True,
            enable_checksum=False,
        )

        self.assertEqual(state_full.initial_offset, initial_offset)
        self.assertEqual(state_full.initial_length, initial_length)
        self.assertEqual(state_full.user_buffer, user_buffer)
        self.assertEqual(state_full.bytes_written, 0)
        self.assertEqual(state_full.next_expected_offset, initial_offset)
        self.assertFalse(state_full.is_complete)
        self.assertTrue(state_full.is_full_object_read)
        self.assertIsNone(state_full.rolling_checksum)


class TestReadResumptionStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = _ReadResumptionStrategy()

        self.state = {"download_states": {}, "read_handle": None, "routing_token": None}

    def _add_download(
        self,
        read_id,
        offset=0,
        length=100,
        buffer=None,
        is_full_object_read=False,
        enable_checksum=True,
    ):
        """Helper to inject a download state into the correct nested location."""
        if buffer is None:
            buffer = io.BytesIO()
        state = _DownloadState(
            initial_offset=offset,
            initial_length=length,
            user_buffer=buffer,
            is_full_object_read=is_full_object_read,
            enable_checksum=enable_checksum,
        )
        self.state["download_states"][read_id] = state
        return state

    def _create_response(
        self,
        content,
        read_id,
        offset,
        crc=None,
        range_end=False,
        handle=None,
        has_read_range=True,
    ):
        """Helper to create a response object."""
        checksummed_data = None
        if content is not None:
            if crc is None:
                crc = google_crc32c.value(content)
            checksummed_data = storage_v2.ChecksummedData(content=content, crc32c=crc)

        read_range = None
        if has_read_range:
            read_range = storage_v2.ReadRange(read_id=read_id, read_offset=offset)

        read_handle_message = None
        if handle:
            read_handle_message = storage_v2.BidiReadHandle(handle=handle)
            self.state["read_handle"] = handle

        return storage_v2.BidiReadObjectResponse(
            object_data_ranges=[
                storage_v2.ObjectRangeData(
                    checksummed_data=checksummed_data,
                    read_range=read_range,
                    range_end=range_end,
                )
            ],
            read_handle=read_handle_message,
        )

    # --- Request Generation Tests ---

    def test_generate_requests_single_incomplete(self):
        """Test generating a request for a single incomplete download."""
        read_state = self._add_download(_READ_ID, offset=0, length=100)
        read_state.bytes_written = 20

        requests = self.strategy.generate_requests(self.state)

        self.assertEqual(len(requests), 1)
        self.assertEqual(requests[0].read_offset, 20)
        self.assertEqual(requests[0].read_length, 80)
        self.assertEqual(requests[0].read_id, _READ_ID)

    def test_generate_requests_multiple_incomplete(self):
        """Test generating requests for multiple incomplete downloads."""
        read_id2 = 2
        rs1 = self._add_download(_READ_ID, offset=0, length=100)
        rs1.bytes_written = 50

        self._add_download(read_id2, offset=200, length=100)

        requests = self.strategy.generate_requests(self.state)

        self.assertEqual(len(requests), 2)
        requests.sort(key=lambda r: r.read_id)

        req1 = requests[0]
        req2 = requests[1]

        self.assertEqual(req1.read_id, _READ_ID)
        self.assertEqual(req1.read_offset, 50)
        self.assertEqual(req1.read_length, 50)

        self.assertEqual(req2.read_id, read_id2)
        self.assertEqual(req2.read_offset, 200)
        self.assertEqual(req2.read_length, 100)

    def test_generate_requests_read_to_end_resumption(self):
        """Test resumption for 'read to end' (length=0) requests."""
        read_state = self._add_download(_READ_ID, offset=0, length=0)
        read_state.bytes_written = 500

        requests = self.strategy.generate_requests(self.state)

        self.assertEqual(len(requests), 1)
        self.assertEqual(requests[0].read_offset, 500)
        self.assertEqual(requests[0].read_length, 0)

    def test_generate_requests_with_complete(self):
        """Test that no request is generated for a completed download."""
        read_state = self._add_download(_READ_ID)
        read_state.is_complete = True

        requests = self.strategy.generate_requests(self.state)
        self.assertEqual(len(requests), 0)

    def test_generate_requests_multiple_mixed_states(self):
        """Test generating requests with mixed complete, partial, and fresh states."""
        s1 = self._add_download(1, length=100)
        s1.is_complete = True

        s2 = self._add_download(2, offset=0, length=100)
        s2.bytes_written = 50

        s3 = self._add_download(3, offset=200, length=100)
        s3.bytes_written = 0

        requests = self.strategy.generate_requests(self.state)

        self.assertEqual(len(requests), 2)
        requests.sort(key=lambda r: r.read_id)

        self.assertEqual(requests[0].read_id, 2)
        self.assertEqual(requests[1].read_id, 3)

    def test_generate_requests_empty_state(self):
        """Test generating requests with an empty state."""
        requests = self.strategy.generate_requests(self.state)
        self.assertEqual(len(requests), 0)

    # --- Update State and response processing Tests ---

    def test_update_state_processes_single_chunk_successfully(self):
        """Test updating state from a successful response."""
        read_state = self._add_download(_READ_ID, offset=0, length=100)
        data = b"test_data"

        response = self._create_response(data, _READ_ID, offset=0)

        self.strategy.update_state_from_response(response, self.state)

        self.assertEqual(read_state.bytes_written, len(data))
        self.assertEqual(read_state.next_expected_offset, len(data))
        self.assertFalse(read_state.is_complete)
        self.assertEqual(read_state.user_buffer.getvalue(), data)

    def test_update_state_accumulates_chunks(self):
        """Verify that state updates correctly over multiple chunks."""
        read_state = self._add_download(_READ_ID, offset=0, length=8)

        resp1 = self._create_response(b"test", _READ_ID, offset=0)
        self.strategy.update_state_from_response(resp1, self.state)

        self.assertEqual(read_state.bytes_written, 4)
        self.assertEqual(read_state.user_buffer.getvalue(), b"test")

        resp2 = self._create_response(b"data", _READ_ID, offset=4, range_end=True)
        self.strategy.update_state_from_response(resp2, self.state)

        self.assertEqual(read_state.bytes_written, 8)
        self.assertTrue(read_state.is_complete)
        self.assertEqual(read_state.user_buffer.getvalue(), b"testdata")

    def test_update_state_captures_read_handle(self):
        """Verify read_handle is extracted from the response."""
        self._add_download(_READ_ID)

        new_handle = b"optimized_handle"
        response = self._create_response(b"data", _READ_ID, 0, handle=new_handle)

        self.strategy.update_state_from_response(response, self.state)
        self.assertEqual(self.state["read_handle"].handle, new_handle)

    def test_update_state_unknown_id(self):
        """Verify we ignore data for IDs not in our tracking state."""
        self._add_download(_READ_ID)
        response = self._create_response(b"ghost", read_id=999, offset=0)

        self.strategy.update_state_from_response(response, self.state)
        self.assertEqual(self.state["download_states"][_READ_ID].bytes_written, 0)

    def test_update_state_missing_read_range(self):
        """Verify we ignore ranges without read_range metadata."""
        response = self._create_response(b"data", _READ_ID, 0, has_read_range=False)
        self.strategy.update_state_from_response(response, self.state)

    def test_update_state_offset_mismatch(self):
        """Test that an offset mismatch raises DataCorruption."""
        read_state = self._add_download(_READ_ID, offset=0)
        read_state.next_expected_offset = 10

        response = self._create_response(b"data", _READ_ID, offset=0)

        with self.assertRaisesRegex(DataCorruption, "Offset mismatch"):
            self.strategy.update_state_from_response(response, self.state)

    def test_update_state_checksum_mismatch(self):
        """Test that a CRC32C mismatch raises DataCorruption."""
        self._add_download(_READ_ID)
        response = self._create_response(b"data", _READ_ID, offset=0, crc=999999)

        with self.assertRaisesRegex(DataCorruption, "Checksum mismatch"):
            self.strategy.update_state_from_response(response, self.state)

    def test_update_state_final_byte_count_mismatch(self):
        """Test mismatch between expected length and actual bytes written on completion."""
        self._add_download(_READ_ID, length=100)

        data = b"data" * 30
        response = self._create_response(data, _READ_ID, offset=0, range_end=True)

        with self.assertRaisesRegex(DataCorruption, "Byte count mismatch"):
            self.strategy.update_state_from_response(response, self.state)

    def test_update_state_completes_download(self):
        """Test that the download is marked complete on range_end."""
        data = b"test_data"
        read_state = self._add_download(_READ_ID, length=len(data))

        response = self._create_response(data, _READ_ID, offset=0, range_end=True)

        self.strategy.update_state_from_response(response, self.state)

        self.assertTrue(read_state.is_complete)
        self.assertEqual(read_state.bytes_written, len(data))

    def test_update_state_completes_download_zero_length(self):
        """Test completion for a download with initial_length of 0."""
        read_state = self._add_download(_READ_ID, length=0)
        data = b"test_data"

        response = self._create_response(data, _READ_ID, offset=0, range_end=True)

        self.strategy.update_state_from_response(response, self.state)

        self.assertTrue(read_state.is_complete)
        self.assertEqual(read_state.bytes_written, len(data))

    def test_update_state_zero_byte_file(self):
        """Test downloading a completely empty file."""
        read_state = self._add_download(_READ_ID, length=0)

        response = self._create_response(b"", _READ_ID, offset=0, range_end=True)

        self.strategy.update_state_from_response(response, self.state)

        self.assertTrue(read_state.is_complete)
        self.assertEqual(read_state.bytes_written, 0)
        self.assertEqual(read_state.user_buffer.getvalue(), b"")

    def test_update_state_missing_read_range_logs_warning(self):
        """Verify we log a warning and continue when read_range is missing."""
        response = self._create_response(b"data", _READ_ID, 0, has_read_range=False)

        # assertLogs captures logs for the given logger name and minimum level
        with self.assertLogs(LOGGER_NAME, level="WARNING") as cm:
            self.strategy.update_state_from_response(response, self.state)

        self.assertTrue(
            any("missing read_range field" in output for output in cm.output)
        )

    def test_update_state_unknown_id_logs_warning(self):
        """Verify we log a warning and continue when read_id is unknown."""
        unknown_id = 999
        self._add_download(_READ_ID)
        response = self._create_response(b"ghost", read_id=unknown_id, offset=0)

        with self.assertLogs(LOGGER_NAME, level="WARNING") as cm:
            self.strategy.update_state_from_response(response, self.state)

        self.assertTrue(
            any(
                f"unknown or stale read_id {unknown_id}" in output
                for output in cm.output
            )
        )

    # --- Recovery Tests ---

    def test_recover_state_on_failure_handles_redirect(self):
        """Verify recover_state_on_failure correctly extracts routing_token."""
        token = "dummy-routing-token"
        redirect_error = BidiReadObjectRedirectedError(routing_token=token)
        final_error = exceptions.Aborted("Retry failed", errors=[redirect_error])

        async def run():
            await self.strategy.recover_state_on_failure(final_error, self.state)

        asyncio.new_event_loop().run_until_complete(run())

        self.assertEqual(self.state["routing_token"], token)

    def test_recover_state_ignores_standard_errors(self):
        """Verify that non-redirect errors do not corrupt the routing token."""
        self.state["routing_token"] = "existing-token"

        std_error = exceptions.ServiceUnavailable("Maintenance")
        final_error = exceptions.RetryError("Retry failed", cause=std_error)

        async def run():
            await self.strategy.recover_state_on_failure(final_error, self.state)

        asyncio.new_event_loop().run_until_complete(run())

        # Token should remain unchanged
        self.assertEqual(self.state["routing_token"], "existing-token")

    def test_update_state_full_object_checksum_success(self):
        """Test that full object checksum verification succeeds on range_end."""
        read_state = self._add_download(
            _READ_ID, offset=0, length=9, is_full_object_read=True
        )
        self.state["enable_checksum"] = True
        self.state["full_obj_server_crc32c"] = google_crc32c.value(b"testdata1")

        resp1 = self._create_response(b"test", _READ_ID, offset=0)
        self.strategy.update_state_from_response(resp1, self.state)

        resp2 = self._create_response(b"data1", _READ_ID, offset=4, range_end=True)
        self.strategy.update_state_from_response(resp2, self.state)

        self.assertTrue(read_state.is_complete)
        self.assertEqual(read_state.bytes_written, 9)

    def test_update_state_full_object_checksum_failure(self):
        """Test that full object checksum verification raises DataCorruption on mismatch at range_end."""
        self._add_download(_READ_ID, offset=0, length=9, is_full_object_read=True)
        self.state["enable_checksum"] = True
        self.state["full_obj_server_crc32c"] = 111111  # Wrong server checksum!

        resp1 = self._create_response(b"test", _READ_ID, offset=0)
        self.strategy.update_state_from_response(resp1, self.state)

        resp2 = self._create_response(b"data1", _READ_ID, offset=4, range_end=True)
        with self.assertRaisesRegex(DataCorruption, "Full object checksum mismatch"):
            self.strategy.update_state_from_response(resp2, self.state)

    def test_update_state_checksum_mismatch_ignored_when_disabled(self):
        """Test that a CRC32C mismatch is ignored when enable_checksum is False."""
        self._add_download(_READ_ID)
        self.state["enable_checksum"] = False
        response = self._create_response(b"data", _READ_ID, offset=0, crc=999999)

        # Should NOT raise DataCorruption!
        self.strategy.update_state_from_response(response, self.state)

    def test_update_state_full_object_checksum_mismatch_ignored_when_disabled(self):
        """Test that a full-object CRC32C mismatch is ignored when enable_checksum is False."""
        self._add_download(
            _READ_ID,
            offset=0,
            length=9,
            is_full_object_read=True,
            enable_checksum=False,
        )
        self.state["enable_checksum"] = False
        self.state["full_obj_server_crc32c"] = 111111  # Wrong server checksum!

        resp1 = self._create_response(b"test", _READ_ID, offset=0)
        self.strategy.update_state_from_response(resp1, self.state)

        resp2 = self._create_response(b"data1", _READ_ID, offset=4, range_end=True)
        # Should NOT raise DataCorruption!
        self.strategy.update_state_from_response(resp2, self.state)
