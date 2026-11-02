# Copyright 2026 Google LLC
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

"""Test suite covering edge cases, stream boundaries, retry interactions, and sync/async parity.

These tests evaluate:
1. Stream continuity and subsequent chunk delivery following full/partial chunk recovery.
2. Parity in return types, retry configuration, and exception handling between sync and async.
3. Memory efficiency when consuming streaming iterables.
4. Coordination of retry policies, backoffs, and timeout handling during transport interruptions.
"""

import asyncio
import datetime
from unittest import mock

import pytest
import requests

import google.api_core.retry
from google.api_core.resumable_transfer.upload import (
    ResumableUploadConfig,
    ResumableUploadSession,
)
from google.api_core.resumable_transfer.upload_async import (
    AsyncResumableUploadSession,
)

try:
    import aiohttp  # noqa: F401
    import google.auth.aio.transport  # noqa: F401

    GOOGLE_AUTH_AIO_INSTALLED = True
except ImportError:
    GOOGLE_AUTH_AIO_INSTALLED = False


class _MockAiohttpResp:
    """Mock for aiohttp response context manager."""

    def __init__(self, status: int, headers: dict, body: bytes):
        self.status = status
        self.headers = headers
        self._body = body

    async def read(self) -> bytes:
        return self._body

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass


# ==============================================================================
# 1. Stream Recovery & Chunk Continuity
# ==============================================================================


def test_full_chunk_recovery_transmits_subsequent_chunks_sync():
    """Verifies that sync upload continues transmitting subsequent chunks after full chunk recovery.

    Why this test is needed:
        When chunk 1 (bytes 0..100) fails with a recoverable error (e.g. 412 Precondition Failed)
        after the server has actually committed all 100 bytes, the status query returns
        ``X-Goog-Upload-Size-Received: 100``. Slicing the active in-memory buffer by the
        committed byte count (`_buffered_chunk[100:]`) yields a 0-length ``memoryview``.
        If `_reposition_stream_offset` leaves a non-``None`` 0-length buffer in place instead
        of resetting `_buffered_chunk = None`, the next transmission attempt treats that empty
        buffer as the active chunk rather than reading chunk 2 (bytes 100..200) from the stream.
    """
    transport = mock.Mock()
    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/session1",
        },
    )
    resp_412 = mock.Mock(
        ok=False,
        status_code=412,
        text="Precondition Failed",
        content=b"Precondition Failed",
        headers={},
        json=lambda: {},
    )
    # Status query confirms the entire first chunk (100 bytes) was committed on the server.
    query_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "100",
        },
    )
    final_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b"done",
    )
    transport.request.side_effect = [start_resp, resp_412, query_resp, final_resp]

    # Total payload: 200 bytes across two 100-byte chunks.
    payload = b"A" * 100 + b"B" * 100
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(chunk_size=100),
        transport=transport,
    )
    session.upload(stream=payload)

    transmitted_chunks = [
        request_call.kwargs.get("data")
        for request_call in transport.request.call_args_list
        if request_call.kwargs.get("headers", {}).get("X-Goog-Upload-Command")
        in ("upload", "upload, finalize")
    ]
    total_bytes_sent = sum(
        len(chunk) for chunk in transmitted_chunks if chunk is not None
    )
    assert total_bytes_sent == 200, (
        f"Expected 200 bytes uploaded across all chunks, but received {total_bytes_sent} "
        f"bytes. Transmitted chunks: {transmitted_chunks}"
    )


@pytest.mark.skipif(
    not GOOGLE_AUTH_AIO_INSTALLED,
    reason="Skipped because google-api-core[async_rest] is not installed",
)
@pytest.mark.asyncio
async def test_full_chunk_recovery_transmits_subsequent_chunks_async():
    """Async counterpart verifying subsequent chunks continue transmitting after full chunk recovery.

    Why this test is needed:
        Ensures ``AsyncResumableUploadSession._recover`` clears ``_buffered_chunk = None``
        when a status query confirms all bytes of the active chunk were committed, so the
        next iteration reads the next chunk from the stream instead of sending an empty slice.
    """
    transport = mock.Mock()
    start_resp = _MockAiohttpResp(
        200,
        {
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/session1",
        },
        b"",
    )
    resp_412 = _MockAiohttpResp(412, {}, b"Precondition Failed")
    query_resp = _MockAiohttpResp(
        200,
        {"X-Goog-Upload-Status": "active", "X-Goog-Upload-Size-Received": "100"},
        b"",
    )
    final_resp = _MockAiohttpResp(200, {"X-Goog-Upload-Status": "final"}, b"done")
    transport.request.side_effect = [start_resp, resp_412, query_resp, final_resp]

    payload = b"A" * 100 + b"B" * 100
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(chunk_size=100),
        transport=transport,
    )
    await session.upload(stream=payload)

    transmitted_chunks = [
        request_call.kwargs.get("data")
        for request_call in transport.request.call_args_list
        if request_call.kwargs.get("headers", {}).get("X-Goog-Upload-Command")
        in ("upload", "upload, finalize")
    ]
    total_bytes_sent = sum(
        len(chunk) for chunk in transmitted_chunks if chunk is not None
    )
    assert total_bytes_sent == 200, (
        f"Expected 200 bytes uploaded across all chunks, but received {total_bytes_sent} "
        f"bytes. Transmitted chunks: {transmitted_chunks}"
    )


def test_partial_chunk_recovery_does_not_finalize_prematurely_sync():
    """Verifies that retransmitting a partial chunk does not prematurely finalize the upload.

    Why this test is needed:
        When chunk 1 (100 bytes out of a 200-byte stream) partially commits 50 bytes before
        failing, `_reposition_stream_offset` slices the active buffer to the remaining 50 bytes.
        If EOF detection checks `len(data) < chunk_size` on the sliced buffer instead of
        preserving `_buffered_chunk_is_last` computed when reading from the stream, the 50-byte
        partial retransmission would be misclassified as the final chunk (`upload, finalize`),
        truncating the upload before chunk 2 is ever sent.
    """
    transport = mock.Mock()
    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/session1",
        },
    )
    resp_412 = mock.Mock(
        ok=False,
        status_code=412,
        text="Precondition Failed",
        content=b"Precondition Failed",
        headers={},
        json=lambda: {},
    )
    # Server confirms 50 of the 100 bytes in chunk 1 were committed.
    query_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "50",
        },
    )
    final_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b"done",
    )
    transport.request.side_effect = [start_resp, resp_412, query_resp, final_resp]

    # Total payload: 200 bytes across two 100-byte chunks.
    payload = b"A" * 100 + b"B" * 100
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(chunk_size=100),
        transport=transport,
    )
    session.upload(stream=payload)

    # Request sequence: [0] start -> [1] initial chunk 1 -> [2] query -> [3] partial chunk 1 retransmit.
    request_calls = transport.request.call_args_list
    partial_retransmit_call = request_calls[3]
    partial_retransmit_command = partial_retransmit_call.kwargs.get("headers", {}).get(
        "X-Goog-Upload-Command"
    )
    assert partial_retransmit_command == "upload", (
        f"Partial retransmit request used command '{partial_retransmit_command}' instead of 'upload'. "
        "A partial retransmit should not mark finalize when subsequent chunks remain."
    )


@pytest.mark.skipif(
    not GOOGLE_AUTH_AIO_INSTALLED,
    reason="Skipped because google-api-core[async_rest] is not installed",
)
@pytest.mark.asyncio
async def test_partial_chunk_recovery_does_not_finalize_prematurely_async():
    """Async counterpart verifying partial chunk retransmission does not prematurely finalize.

    Why this test is needed:
        Ensures ``AsyncResumableUploadSession`` preserves ``_buffered_chunk_is_last`` across
        partial recovery so a sliced tail smaller than ``chunk_size`` is sent with
        ``X-Goog-Upload-Command: upload`` rather than ``upload, finalize``.
    """
    transport = mock.Mock()
    start_resp = _MockAiohttpResp(
        200,
        {
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/session1",
        },
        b"",
    )
    resp_412 = _MockAiohttpResp(412, {}, b"Precondition Failed")
    query_resp = _MockAiohttpResp(
        200,
        {"X-Goog-Upload-Status": "active", "X-Goog-Upload-Size-Received": "50"},
        b"",
    )
    final_resp = _MockAiohttpResp(200, {"X-Goog-Upload-Status": "final"}, b"done")
    transport.request.side_effect = [start_resp, resp_412, query_resp, final_resp]

    payload = b"A" * 100 + b"B" * 100
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(chunk_size=100),
        transport=transport,
    )
    await session.upload(stream=payload)

    # Request sequence: [0] start -> [1] initial chunk 1 -> [2] query -> [3] partial chunk 1 retransmit.
    request_calls = transport.request.call_args_list
    partial_retransmit_call = request_calls[3]
    partial_retransmit_command = partial_retransmit_call.kwargs.get("headers", {}).get(
        "X-Goog-Upload-Command"
    )
    assert partial_retransmit_command == "upload", (
        f"Async partial retransmit request used command '{partial_retransmit_command}' instead of 'upload'. "
        "A partial retransmit should not mark finalize when subsequent chunks remain."
    )


# ==============================================================================
# 2. Sync vs Async Consistency & Parity
# ==============================================================================


@pytest.mark.skipif(
    not GOOGLE_AUTH_AIO_INSTALLED,
    reason="Skipped because google-api-core[async_rest] is not installed",
)
@pytest.mark.asyncio
async def test_sync_async_return_type_parity():
    """Verifies consistent return types between sync and async when response_type is set.

    Why this test is needed:
        Sync sessions receive a ``requests.Response`` object while async sessions read raw
        body bytes inside the ``aiohttp`` context manager. Both must pass the final payload
        through ``_format_response_payload`` so callers configuring ``response_type``
        receive identical deserialized types from ``upload()``.
    """
    # Sync session
    transport_sync = mock.Mock()
    start_sync = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/s1",
        },
    )
    chunk_sync = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b'{"status": "ok"}',
    )
    transport_sync.request.side_effect = [start_sync, chunk_sync]
    sync_session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(),
        response_type=bytes,
        transport=transport_sync,
    )
    sync_result = sync_session.upload(stream=b"data")

    # Async session
    transport_async = mock.Mock()
    start_async = _MockAiohttpResp(
        200,
        {
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/s1",
        },
        b"",
    )
    chunk_async = _MockAiohttpResp(
        200,
        {"X-Goog-Upload-Status": "final"},
        b'{"status": "ok"}',
    )
    transport_async.request.side_effect = [start_async, chunk_async]
    async_session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(),
        response_type=bytes,
        transport=transport_async,
    )
    async_result = await async_session.upload(stream=b"data")

    assert type(sync_result) is type(async_result), (
        f"Expected consistent return types: sync returned {type(sync_result).__name__}, "
        f"while async returned {type(async_result).__name__}."
    )


@pytest.mark.skipif(
    not GOOGLE_AUTH_AIO_INSTALLED,
    reason="Skipped because google-api-core[async_rest] is not installed",
)
@pytest.mark.asyncio
async def test_sync_async_custom_retry_parity():
    """Verifies that user-configured retry policies are applied in both sync and async sessions.

    Why this test is needed:
        Callers may pass a ``StreamingRetry`` / ``AsyncStreamingRetry`` override to
        ``upload(retry=...)`` to customize backoff timing (e.g. ``initial`` delay).
        Both sync and async sessions must apply the caller's configured backoff
        parameters while wrapping the predicate with protocol recovery rules.
    """
    sync_retry = google.api_core.retry.StreamingRetry(initial=0.25)
    async_retry = google.api_core.retry.AsyncStreamingRetry(initial=0.25)

    # Sync
    transport_sync = mock.Mock()
    start_sync = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/s1",
        },
    )
    chunk_sync = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b"ok",
    )
    transport_sync.request.side_effect = [start_sync, chunk_sync]
    sync_session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(),
        transport=transport_sync,
    )
    resolved_sync = sync_session._get_streaming_retry(retry_override=sync_retry)
    sync_session.upload(stream=b"data", retry=sync_retry)

    # Async
    transport_async = mock.Mock()
    start_async = _MockAiohttpResp(
        200,
        {
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/s1",
        },
        b"",
    )
    chunk_async = _MockAiohttpResp(200, {"X-Goog-Upload-Status": "final"}, b"ok")
    transport_async.request.side_effect = [start_async, chunk_async]
    async_session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(),
        transport=transport_async,
    )
    resolved_async = async_session._get_async_streaming_retry(
        retry_override=async_retry
    )
    await async_session.upload(stream=b"data", retry=async_retry)

    assert resolved_sync._initial == resolved_async._initial == 0.25


@pytest.mark.skipif(
    not GOOGLE_AUTH_AIO_INSTALLED,
    reason="Skipped because google-api-core[async_rest] is not installed",
)
@pytest.mark.asyncio
async def test_sync_async_error_retry_parity():
    """Verifies that non-retriable exceptions (e.g. ValueError) fail fast without retries in both.

    Why this test is needed:
        Programming and configuration errors (such as ``ValueError`` or ``TypeError``) are
        not transient transport failures. Both sync and async retry predicates must reject
        non-retriable exceptions immediately on the first attempt without entering backoff loops.
    """
    # Sync: transport raises ValueError
    transport_sync = mock.Mock()
    transport_sync.request.side_effect = ValueError("fatal configuration issue")
    sync_session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(),
        transport=transport_sync,
    )
    with pytest.raises(ValueError):
        sync_session.upload(stream=b"data")
    sync_attempts = transport_sync.request.call_count

    # Async: transport raises ValueError
    transport_async = mock.Mock()
    transport_async.request.side_effect = ValueError("fatal configuration issue")
    async_session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(),
        transport=transport_async,
    )
    with pytest.raises(ValueError):
        await async_session.upload(stream=b"data")
    async_attempts = transport_async.request.call_count

    assert sync_attempts == async_attempts == 1, (
        f"Expected non-retriable error to fail after 1 attempt in both implementations: "
        f"sync attempts={sync_attempts}, async attempts={async_attempts}."
    )


def test_iterable_stream_incremental_consumption_sync():
    """Verifies that iterable streams are consumed incrementally rather than loaded upfront.

    Why this test is needed:
        Resumable uploads often stream multi-gigabyte payloads from generators or chunk
        iterators. If ``_prepare_stream`` eagerly materialized the iterable into memory
        (e.g. via ``b"".join(stream)``) to inspect its size, large uploads would exhaust
        process memory before transmitting the first chunk.
    """
    chunks_generated = 0

    def data_generator():
        nonlocal chunks_generated
        for _ in range(10):
            chunks_generated += 1
            yield b"X" * 1024

    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(chunk_size=1024),
    )
    # Stream preparation must wrap the generator lazily without advancing it.
    stream_obj, size = session._prepare_stream(data_generator(), size=10 * 1024)

    assert chunks_generated == 0, (
        f"Expected iterable stream to be consumed lazily during upload, but all "
        f"{chunks_generated} chunks were buffered into memory during preparation."
    )


def test_timezone_naive_deadline_handling():
    """Verifies that naive future datetimes are compared accurately against current time.

    Why this test is needed:
        Callers frequently construct upload deadlines using ``datetime.datetime.now()``
        (timezone-naive) rather than ``datetime.datetime.now(datetime.timezone.utc)``.
        Comparing a naive ``deadline`` against a timezone-aware clock raises ``TypeError``,
        and misinterpreting local time as UTC skews the remaining deadline budget.
    """
    future_naive = datetime.datetime.now() + datetime.timedelta(hours=1)
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(deadline=future_naive),
    )
    remaining = session._get_deadline_remaining()
    assert remaining is not None and remaining > 0, (
        f"Expected positive remaining deadline duration for future naive timestamp, got {remaining}s."
    )


# ==============================================================================
# 3. Retry Coordination & Multi-Layer Interactions
# ==============================================================================


def test_single_layer_backoff_coordination():
    """Verifies that retry backoff delays are coordinated through a single layer during chunk recovery.

    Why this test is needed:
        When a chunk upload fails with a transient 503 error, recovery involves querying
        the server offset before retransmitting. If inner helper methods wrapped their own
        independent retry loops around chunk transmission and recovery, a single transient
        failure would trigger compounded backoff sleeps across multiple layers. Only the
        outer streaming retry loop should schedule backoff delays.
    """
    transport = mock.Mock()
    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/s1",
        },
    )
    resp_503 = mock.Mock(
        ok=False,
        status_code=503,
        text="Service Unavailable",
        content=b"503",
        headers={},
        json=lambda: {},
    )
    query_200 = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "0",
        },
    )
    final_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b"done",
    )

    transport.request.side_effect = [
        start_resp,
        resp_503,
        query_200,
        final_resp,
    ]

    sleep_durations = []
    with mock.patch(
        "time.sleep", side_effect=lambda duration: sleep_durations.append(duration)
    ):
        session = ResumableUploadSession(
            upload_url="https://api.example.com/init",
            config=ResumableUploadConfig(chunk_size=100),
            transport=transport,
        )
        session.upload(stream=b"A" * 100)

    # For a single transient failure, exactly 1 coordinated retry backoff sleep should occur.
    assert len(sleep_durations) == 1, (
        f"Expected exactly 1 coordinated retry backoff delay for a single failed chunk attempt, "
        f"but observed {len(sleep_durations)} sleeps ({sleep_durations}) compounding across nested layers."
    )


def test_connection_recovery_with_custom_retry_predicate():
    """Verifies that network connection drops initiate an offset query when a custom retry is set.

    Why this test is needed:
        Callers often supply a narrow custom retry predicate (such as retrying only
        ``ServiceUnavailable``) to control transient HTTP status retries. When a TCP
        connection resets mid-chunk, the client cannot tell how many bytes the server
        persisted and must issue an ``X-Goog-Upload-Command: query`` offset check.
        Transport connection drops must remain recoverable even when a custom predicate is set.
    """
    transport = mock.Mock()
    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/s1",
        },
    )
    query_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "0",
        },
    )
    final_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b"done",
    )

    transport.request.side_effect = [
        start_resp,
        requests.exceptions.ConnectionError("TCP connection reset by peer"),
        query_resp,
        final_resp,
    ]

    user_retry = google.api_core.retry.StreamingRetry(
        predicate=google.api_core.retry.if_exception_type(
            google.api_core.exceptions.ServiceUnavailable
        )
    )
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(chunk_size=100),
        transport=transport,
    )

    session.upload(stream=b"A" * 100, retry=user_retry)

    request_calls = transport.request.call_args_list
    query_calls = [
        request_call
        for request_call in request_calls
        if request_call.kwargs.get("headers", {}).get("X-Goog-Upload-Command")
        == "query"
    ]
    assert len(query_calls) >= 1, (
        "Expected transport connection drop to initiate an offset query to reconcile server state."
    )


def test_precondition_failed_response_triggers_offset_query():
    """Verifies that a 412 Precondition Failed status initiates an offset query rather than immediate resend.

    Why this test is needed:
        Under the Resumable Upload protocol, a ``412 Precondition Failed`` response during
        chunk upload indicates a state/offset mismatch between client and server. Blindly
        retransmitting the chunk at the old offset without first issuing an
        ``X-Goog-Upload-Command: query`` request would repeatedly fail with 412. The session
        must set ``_needs_recovery = True`` so the immediate next request queries server state.
    """
    transport = mock.Mock()
    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/s1",
        },
    )
    resp_412 = mock.Mock(
        ok=False,
        status_code=412,
        text="Precondition Failed",
        content=b"Precondition Failed",
        headers={},
        json=lambda: {},
    )
    query_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "0",
        },
    )
    final_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b"done",
    )

    transport.request.side_effect = [
        start_resp,
        resp_412,
        query_resp,
        final_resp,
    ]

    user_retry = google.api_core.retry.StreamingRetry(
        maximum=0.01,
        deadline=0.05,
    )
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(chunk_size=100),
        transport=transport,
    )

    session.upload(stream=b"A" * 100, retry=user_retry)

    # Request sequence: [0] start -> [1] failed chunk upload (412) -> [2] recovery query.
    request_calls = transport.request.call_args_list
    recovery_request_call = request_calls[2]
    recovery_request_command = recovery_request_call.kwargs.get("headers", {}).get(
        "X-Goog-Upload-Command"
    )
    assert recovery_request_command == "query", (
        f"Expected command 'query' to reconcile server offset after 412 Precondition Failed, "
        f"but received '{recovery_request_command}'."
    )


def test_socket_timeout_initiates_recovery():
    """Verifies that a transient socket read timeout triggers recovery when stall termination is disabled.

    Why this test is needed:
        A socket read timeout (``requests.exceptions.Timeout``) during chunk upload means
        the client cannot determine how many bytes the server persisted before the connection
        stalled. When stall termination is disabled (``stall_minimum_rate=0``), the session
        must treat the timeout as a recoverable transport interruption, query the server
        offset via ``X-Goog-Upload-Command: query``, and resume uploading from that offset.
    """
    transport = mock.Mock()
    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/s1",
        },
    )
    query_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "0",
        },
    )
    final_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b"done",
    )
    transport.request.side_effect = [
        start_resp,
        requests.exceptions.Timeout("Read timed out on socket"),
        query_resp,
        final_resp,
    ]

    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(
            chunk_size=100, stall_minimum_rate=0, stall_timeout=0.0
        ),
        transport=transport,
    )

    session.upload(stream=b"A" * 100)

    request_calls = transport.request.call_args_list
    assert len(request_calls) > 2, (
        f"Expected socket read timeout to attempt recovery rather than terminating after {len(request_calls)} call(s)."
    )


@pytest.mark.skipif(
    not GOOGLE_AUTH_AIO_INSTALLED,
    reason="Skipped because google-api-core[async_rest] is not installed",
)
@pytest.mark.asyncio
async def test_async_upload_cancellation_does_not_deadlock():
    """Verifies that cancelling an in-flight async upload terminates cleanly without queue deadlock.

    Why this test is needed:
        ``AsyncUploadOperation`` runs the upload in a background ``asyncio.Task`` and feeds
        progress snapshots to callers iterating over ``op.progress()`` via an internal
        ``asyncio.Queue``. In Python 3.8+, ``asyncio.CancelledError`` inherits from
        ``BaseException`` rather than ``Exception``. If the background task catches only
        ``Exception`` when pushing error sentinels into ``_progress_queue``, cancelling
        the task leaves ``op.progress()`` consumers awaiting ``_progress_queue.get()``
        forever. This test ensures task cancellation propagates cleanly to consumers.
    """

    class HangingTransport:
        def __init__(self):
            self.started = asyncio.Event()

        def request(self, method, url, **kwargs):
            return self._HangingRequestContext(self)

        class _HangingRequestContext:
            def __init__(self, parent):
                self.parent = parent

            async def __aenter__(self):
                self.parent.started.set()
                await asyncio.sleep(60)

            async def __aexit__(self, *args):
                pass

    transport = HangingTransport()
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/init",
        transport=transport,
    )

    upload_operation = session.upload(stream=b"payload")
    progress_iterator = upload_operation.progress()
    consume_task = asyncio.create_task(progress_iterator.__anext__())
    await transport.started.wait()
    consume_task.cancel()
    with pytest.raises((asyncio.CancelledError, StopAsyncIteration)):
        await asyncio.wait_for(consume_task, timeout=5)
