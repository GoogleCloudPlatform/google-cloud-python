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
import collections
import concurrent.futures
import logging
import os
from typing import IO, Any, Dict, List, NamedTuple, Optional

import google_crc32c

from google.cloud import _storage_v2 as storage_v2
from google.cloud.storage.asyncio.retry._helpers import (
    _handle_redirect,
)
from google.cloud.storage.asyncio.retry.base_strategy import (
    _BaseResumptionStrategy,
)
from google.cloud.storage.exceptions import DataCorruption

_BIDI_READ_REDIRECTED_TYPE_URL = (
    "type.googleapis.com/google.storage.v2.BidiReadObjectRedirectedError"
)
logger = logging.getLogger(__name__)


def _int_from_env(name: str, default: int) -> int:
    """Reads an integer tuning knob from the environment; bad values are ignored."""
    try:
        return int(os.environ.get(name, default))
    except ValueError:
        return default


# Chunks at least this large are checksummed on a worker thread instead of the
# event-loop thread; smaller chunks are hashed inline, and 0 (or any value
# below 1) hashes every chunk inline. The 1 MiB default matches google_crc32c's
# GIL-release threshold, so offloaded hashes over ``bytes``-backed chunks
# (received chunks are) always run with the GIL released.
_CRC32C_OFFLOAD_MIN_BYTES = _int_from_env(
    "GCS_PYTHON_CLIENT_CRC32C_OFFLOAD_MIN_BYTES",
    getattr(google_crc32c, "GIL_RELEASE_THRESHOLD", 1024 * 1024),
)
# Upper bound on chunks held for verification per download_ranges() call.
# Chunks are written only once their checksum matches, so this keeps a slow
# worker from pinning an unbounded number of received messages.
_CRC32C_MAX_PENDING = 32


def _new_crc32c_executor() -> concurrent.futures.ThreadPoolExecutor:
    return concurrent.futures.ThreadPoolExecutor(
        max_workers=2, thread_name_prefix="gcs-crc32c"
    )


# Process-wide pool shared by all clients; its threads start on the first submit().
_crc32c_executor = _new_crc32c_executor()


def _reset_crc32c_executor() -> None:
    """Replaces the parent's pool in a forked child, where it has no threads."""
    global _crc32c_executor
    _crc32c_executor = _new_crc32c_executor()


if hasattr(os, "register_at_fork"):  # pragma: no branch - not on Windows
    os.register_at_fork(after_in_child=_reset_crc32c_executor)


def _submit_crc32c(data: Any) -> Optional[concurrent.futures.Future]:
    """Starts hashing ``data`` on the pool; None if the pool refuses work."""
    try:
        return _crc32c_executor.submit(google_crc32c.value, data)
    except RuntimeError:
        # Raised once interpreter shutdown has begun; hash inline instead.
        return None


class _PendingChunk(NamedTuple):
    """A received chunk that is not written to its buffer yet."""

    read_id: int
    data: Any
    range_end: bool
    response: Any
    server_checksum: Optional[int]
    # Worker-side CRC32C of ``data``; None if it was verified (or needs no
    # verification) on receipt and only waits for the chunks ahead of it.
    checksum_future: Optional[concurrent.futures.Future]


class _DownloadState:
    """A helper class to track the state of a single range download."""

    def __init__(
        self,
        initial_offset: int,
        initial_length: int,
        user_buffer: IO[bytes],
        is_full_object_read: bool = False,
        enable_checksum: bool = True,
    ):
        self.initial_offset = initial_offset
        self.initial_length = initial_length
        self.user_buffer = user_buffer
        self.bytes_written = 0
        # Offset of the next chunk to accept. Runs ahead of
        # initial_offset + bytes_written while received chunks are held for
        # checksum verification.
        self.next_expected_offset = initial_offset
        self.is_complete = False
        self.is_full_object_read = is_full_object_read
        self.rolling_checksum = (
            google_crc32c.Checksum()
            if (is_full_object_read and enable_checksum)
            else None
        )


class _ReadResumptionStrategy(_BaseResumptionStrategy):
    """The concrete resumption strategy for bidi reads."""

    def generate_requests(self, state: Dict[str, Any]) -> List[storage_v2.ReadRange]:
        """Generates new ReadRange requests for all incomplete downloads.

        :type state: dict
        :param state: A dictionary mapping a read_id to its corresponding
                  _DownloadState object.
        """
        pending_requests = []
        download_states: Dict[int, _DownloadState] = state["download_states"]

        for read_id, read_state in download_states.items():
            if not read_state.is_complete:
                new_offset = read_state.initial_offset + read_state.bytes_written

                # Calculate remaining length. If initial_length is 0 (read to end),
                # it stays 0. Otherwise, subtract bytes_written.
                new_length = 0
                if read_state.initial_length > 0:
                    new_length = read_state.initial_length - read_state.bytes_written

                new_request = storage_v2.ReadRange(
                    read_offset=new_offset,
                    read_length=new_length,
                    read_id=read_id,
                )
                pending_requests.append(new_request)
        return pending_requests

    def update_state_from_response(
        self, response: storage_v2.BidiReadObjectResponse, state: Dict[str, Any]
    ) -> None:
        """Processes a server response, performs integrity checks, and updates state."""
        proto = getattr(response, "_pb", response)

        # Capture read_handle if provided.
        if proto.HasField("read_handle"):
            state["read_handle"] = storage_v2.BidiReadHandle(
                handle=proto.read_handle.handle
            )

        download_states = state["download_states"]
        checksum_enabled = state.get("enable_checksum", True)

        for object_data_range in proto.object_data_ranges:
            # Ignore empty ranges or ranges for IDs not in our state
            # (e.g., from a previously cancelled request on the same stream).
            if not object_data_range.HasField("read_range"):
                logger.warning(
                    "Received response with missing read_range field; ignoring."
                )
                continue

            read_range_pb = object_data_range.read_range
            read_id = read_range_pb.read_id

            if read_id not in download_states:
                logger.warning(
                    f"Received data for unknown or stale read_id {read_id}; ignoring."
                )
                continue

            read_state = download_states[read_id]

            # Offset Verification
            # We must validate data before updating state or writing to buffer.
            chunk_offset = read_range_pb.read_offset
            if chunk_offset != read_state.next_expected_offset:
                raise DataCorruption(
                    response,
                    f"Offset mismatch for read_id {read_id}. "
                    f"Expected {read_state.next_expected_offset}, got {chunk_offset}",
                )

            # Checksum Verification
            checksummed_data = object_data_range.checksummed_data
            data = checksummed_data.content
            server_checksum = None
            checksum_future = None

            if checksum_enabled and checksummed_data.HasField("crc32c"):
                server_checksum = checksummed_data.crc32c
                if (
                    _CRC32C_OFFLOAD_MIN_BYTES > 0
                    and len(data) >= _CRC32C_OFFLOAD_MIN_BYTES
                    and read_state.rolling_checksum is None
                ):
                    # Hash off the loop thread; the chunk is written by
                    # verify_pending_checksums() once the checksum matches.
                    # Full-object reads are excluded: they already fold every
                    # chunk into rolling_checksum on this thread, so a second
                    # hash on a worker would only add CPU work.
                    checksum_future = _submit_crc32c(data)
                if checksum_future is None:
                    client_checksum = google_crc32c.value(data)
                    if server_checksum != client_checksum:
                        raise DataCorruption(
                            response,
                            f"Checksum mismatch for read_id {read_id}. "
                            f"Server sent {server_checksum}, client calculated {client_checksum}.",
                        )

            read_state.next_expected_offset += len(data)
            chunk = _PendingChunk(
                read_id,
                data,
                object_data_range.range_end,
                response,
                server_checksum,
                checksum_future,
            )
            pending = state.get("pending_checksums")
            if checksum_future is None and not pending:
                self._write_chunk(state, chunk)
            else:
                # Hold the chunk; chunks are written in arrival order.
                if pending is None:
                    pending = state["pending_checksums"] = collections.deque()
                pending.append(chunk)

    def _write_chunk(self, state: Dict[str, Any], chunk: _PendingChunk) -> None:
        """Writes a verified chunk to its buffer and runs the end-of-range checks."""
        read_state = state["download_states"][chunk.read_id]
        data = chunk.data
        try:
            # Update State & Write Data
            read_state.user_buffer.write(data)

            # Commit updates only after the write succeeds
            if (
                state.get("enable_checksum", True)
                and read_state.rolling_checksum is not None
            ):
                read_state.rolling_checksum.update(data)
            read_state.bytes_written += len(data)
        except BaseException:
            # Keep every read resumable right after its written bytes.
            self.discard_pending_checksums(state)
            raise

        # Final Byte Count & Full Object Checksum Verification
        if chunk.range_end:
            read_state.is_complete = True
            if (
                read_state.initial_length != 0
                and read_state.bytes_written > read_state.initial_length
            ):
                raise DataCorruption(
                    chunk.response,
                    f"Byte count mismatch for read_id {chunk.read_id}. "
                    f"Expected {read_state.initial_length}, got {read_state.bytes_written}",
                )

            # Perform full-object checksum verification once the stream finishes.
            if (
                read_state.is_full_object_read
                and state.get("enable_checksum", True)
                and read_state.rolling_checksum is not None
            ):
                full_obj_server_crc32c = state.get("full_obj_server_crc32c")
                if full_obj_server_crc32c is not None:
                    # Use standard big-endian byte conversion to retrieve the rolling checksum value.
                    client_checksum = int.from_bytes(
                        read_state.rolling_checksum.digest(),
                        byteorder="big",
                    )
                    if client_checksum != full_obj_server_crc32c:
                        raise DataCorruption(
                            chunk.response,
                            f"Full object checksum mismatch for read_id {chunk.read_id}. "
                            f"Server authoritative crc32c: {full_obj_server_crc32c}, client calculated rolling: {client_checksum}.",
                        )

    async def verify_pending_checksums(
        self, state: Dict[str, Any], max_pending: int = 0
    ) -> None:
        """Writes held chunks, in arrival order, once their checksums match.

        Returns when at most ``max_pending`` chunks are still held; only an
        unfinished checksum at the head of the queue is waited for. On a chunk
        checksum mismatch, raises DataCorruption after discarding every held
        chunk (see discard_pending_checksums()), so nothing from the corrupt
        chunk on is written and a retry requests it again; a checksum that
        failed on the worker is re-raised the same way.
        """
        pending = state.get("pending_checksums")
        while pending:
            chunk = pending[0]
            if chunk.checksum_future is not None:
                try:
                    if not chunk.checksum_future.done():
                        if len(pending) <= max_pending:
                            return
                        await asyncio.wrap_future(chunk.checksum_future)
                    client_checksum = chunk.checksum_future.result()
                except BaseException:
                    self.discard_pending_checksums(state)
                    raise
                if client_checksum != chunk.server_checksum:
                    self.discard_pending_checksums(state)
                    raise DataCorruption(
                        chunk.response,
                        f"Checksum mismatch for read_id {chunk.read_id}. "
                        f"Server sent {chunk.server_checksum}, client calculated {client_checksum}.",
                    )
            pending.popleft()
            self._write_chunk(state, chunk)

    def discard_pending_checksums(self, state: Dict[str, Any]) -> None:
        """Drops held chunks unwritten and rewinds each read to its written end.

        Checksums not yet started on the pool are cancelled. A retry requests
        the dropped bytes again.
        """
        pending = state.get("pending_checksums")
        if pending:
            for chunk in pending:
                if chunk.checksum_future is not None:
                    chunk.checksum_future.cancel()
            pending.clear()
        for read_state in state["download_states"].values():
            read_state.next_expected_offset = (
                read_state.initial_offset + read_state.bytes_written
            )

    async def recover_state_on_failure(self, error: Exception, state: Any) -> None:
        """Handles BidiReadObjectRedirectedError, then writes held chunks.

        A retry resumes each read right after its written bytes, so held
        chunks are verified and written first; a corrupt one raises
        DataCorruption instead.
        """
        routing_token, read_handle = _handle_redirect(error)
        if routing_token:
            state["routing_token"] = routing_token
        if read_handle:
            state["read_handle"] = read_handle
        await self.verify_pending_checksums(state)
