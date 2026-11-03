# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""System tests for GAPIC Resumable Upload progress tracking and Golden Path workflows.

Covers both direct `ResumableUploadSession` usage and end-to-end client-level
execution (`ResumableUploadServiceClient` and `ResumableUploadServiceAsyncClient`)
across default `grpc`/`grpc_asyncio` and `rest`/`rest_asyncio` transports,
including the generated sample patterns:
- Option 1: Direct upload from start to completion
- Option 2: Upload while receiving progress updates
- Section 2.1 Golden Path Suite (multi-chunk known size, small upload default
  chunk size, standalone finalize on unseekable stream)
"""

import io
import os
from typing import List
import pytest

from google.auth import credentials as ga_credentials
from google.api_core.resumable_transfer import (
    DEFAULT_CHUNK_SIZE,
    ProgressState,
    ResumableUploadConfig,
    ResumableUploadSession,
    UploadProgress,
)
from google.showcase import (
    ResumableUploadServiceClient,
    UploadMediaRequest,
    UploadMediaResponse,
)

from conftest import (
    HAS_ASYNC_REST_RESUMABLE_UPLOAD_TRANSPORT,
    make_resumable_upload,
)

if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":
    from conftest import async_anonymous_credentials
    from google.showcase import ResumableUploadServiceAsyncClient

SHOWCASE_API_ENDPOINT = "http://localhost:7469"


class _UnknownSizeUnseekableStream:
    """Stream wrapper with unknown total size and non-seekable semantics."""

    def __init__(self, data: bytes) -> None:
        self._buf = io.BytesIO(data)

    def read(self, size: int = -1) -> bytes:
        return self._buf.read(size)

    def seekable(self) -> bool:
        return False


def test_make_resumable_upload_end_to_end(intercepted_resumable_upload_rest):
    client, _ = intercepted_resumable_upload_rest
    stream = io.BytesIO(b"0123456789" * 100)

    # Use make_resumable_upload from start to finish
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    request_body = '{"name": "full_e2e_upload.txt"}'

    response = make_resumable_upload(
        transport=client.transport._session,
        request_body=request_body,
        stream=stream,
        upload_url=initial_url,
        chunk_size=256,
    )
    assert isinstance(response, bytes)

    final_response = UploadMediaResponse.from_json(response)
    assert final_response.name == "full_e2e_upload.txt"
    assert final_response.size == len(stream.getvalue())


def test_resumable_upload_generator_progress_tracking(intercepted_resumable_upload_rest):
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    payload = b"0123456789" * 100
    stream = io.BytesIO(payload)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "chunk_granularity"),
        ("Content-Type", "application/json"),
    ]
    config = ResumableUploadConfig(
        chunk_size=256,
        headers=scenario_headers,
    )
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
    )

    progress_list = []
    # PEP 255 generator progress tracking
    for progress in session.iter_upload(stream, request_body='{"name": "generator_upload.txt"}'):
        progress_list.append(progress)
        assert isinstance(progress, UploadProgress)
        assert "sid=" in progress.upload_url
        assert progress.chunk_size == 256
        assert progress.total_bytes == len(payload)

    # Verify yielded snapshots
    assert len(progress_list) >= 3
    assert progress_list[0].state == ProgressState.STARTED
    assert progress_list[-1].state == ProgressState.FINALIZED
    assert progress_list[-1].bytes_uploaded == len(payload)

    # Verify response populated on session after generator exhaustion
    assert session.response is not None
    assert session.response.name == "generator_upload.txt"
    assert session.response.size == len(payload)


def test_resumable_upload_unseekable_stream_recovery(intercepted_resumable_upload_rest):
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    request_body = '{"name": "unseekable_stream_upload.txt"}'

    class UnseekableStream(io.BytesIO):
        def seekable(self):
            return False

        def seek(self, offset, whence=io.SEEK_SET):
            raise io.UnsupportedOperation("Stream is not seekable")

    data = b"B" * 1024
    stream = UnseekableStream(data)

    # Injects 503 error on first chunk attempt, which ResumableUploadSession recovers via in-memory buffer
    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
        ("X-Goog-Test-Scenario-Config", '{"error_code":503,"failure_count":1,"after_offset":0}'),
    ]

    response = make_resumable_upload(
        transport=client.transport._session,
        request_body=request_body,
        stream=stream,
        upload_url=initial_url,
        size=len(data),
        chunk_size=512,
        headers=scenario_headers,
    )
    assert isinstance(response, bytes)
    final_response = UploadMediaResponse.from_json(response)
    assert final_response.name == "unseekable_stream_upload.txt"
    assert final_response.size == len(data)


def test_multi_chunk_known_size(intercepted_resumable_upload_rest):
    """Golden Path Case 1: Multi-chunk upload with known size (1.5 MB, 512 KiB chunks)."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    total_size = 1_500_000
    chunk_size = 524_288  # 512 KiB
    payload = b"M" * total_size
    stream = io.BytesIO(payload)

    config = ResumableUploadConfig(
        chunk_size=chunk_size,
        headers={"Content-Type": "application/json"},
    )
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
    )

    progress_records = list(
        session.iter_upload(
            stream,
            request_body='{"name": "multi_chunk_known_size.mp4"}',
            size=total_size,
        )
    )

    assert isinstance(session.response, UploadMediaResponse)
    assert session.response.name == "multi_chunk_known_size.mp4"
    assert session.response.size == total_size

    phases = [p.state for p in progress_records]
    offsets = [p.bytes_uploaded for p in progress_records]
    assert phases == [
        ProgressState.STARTED,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.FINALIZED,
    ]
    assert offsets == [0, 524_288, 1_048_576, 1_500_000]
    assert all(p.total_bytes == total_size for p in progress_records)


def test_small_upload_default_chunk_size(intercepted_resumable_upload_rest):
    """Golden Path Case 2: Default chunk size on small upload (~100 KB)."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    total_size = 100_000
    payload = b"S" * total_size
    stream = io.BytesIO(payload)

    config = ResumableUploadConfig(headers={"Content-Type": "application/json"})
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
    )

    progress_records = list(
        session.iter_upload(
            stream,
            request_body='{"name": "small_default_chunk.bin"}',
            size=total_size,
        )
    )

    assert session.chunk_size <= DEFAULT_CHUNK_SIZE
    assert isinstance(session.response, UploadMediaResponse)
    assert session.response.name == "small_default_chunk.bin"
    assert session.response.size == total_size

    phases = [p.state for p in progress_records]
    offsets = [p.bytes_uploaded for p in progress_records]
    assert phases == [
        ProgressState.STARTED,
        ProgressState.FINALIZED,
    ]
    assert offsets == [0, 100_000]
    assert all(p.total_bytes == total_size for p in progress_records)


def test_standalone_finalize_unseekable_stream(intercepted_resumable_upload_rest):
    """Golden Path Case 3: Unseekable stream with unknown size and exact chunk multiple."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    chunk_size = 262_144  # 256 KiB
    total_size = 3 * chunk_size  # 786_432 bytes
    payload = b"U" * total_size
    stream = _UnknownSizeUnseekableStream(payload)

    config = ResumableUploadConfig(
        chunk_size=chunk_size,
        headers={"Content-Type": "application/json"},
    )
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
    )

    progress_records = list(
        session.iter_upload(
            stream,
            request_body='{"name": "unseekable_exact_multiple.bin"}',
            size=None,
        )
    )

    assert isinstance(session.response, UploadMediaResponse)
    assert session.response.name == "unseekable_exact_multiple.bin"
    assert session.response.size == total_size

    phases = [p.state for p in progress_records]
    offsets = [p.bytes_uploaded for p in progress_records]
    assert phases == [
        ProgressState.STARTED,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.FINALIZED,
    ]
    assert offsets == [0, 262_144, 524_288, 786_432, 786_432]
    assert all(p.total_bytes is None for p in progress_records)


def test_client_upload_media_passes_request_body(intercepted_resumable_upload_rest):
    """ Verify that invoking `client.upload_media(request=UploadMediaRequest(...))`
    and calling `session.upload(stream=...)` forwards the serialized request body
    on the initial upload session start request so the server echoes back the
    expected resource name in `UploadMediaResponse.name`."""
    client, _ = intercepted_resumable_upload_rest
    payload = b"0123456789" * 100
    stream = io.BytesIO(payload)

    session = client.upload_media(
        request=UploadMediaRequest(name="client_upload_media.txt"),
    )
    response = session.upload(stream=stream)

    assert isinstance(response, UploadMediaResponse)
    assert response.name == "client_upload_media.txt"
    assert response.size == len(payload)


def test_client_upload_media_with_custom_headers_sets_json_content_type(
    intercepted_resumable_upload_rest,
):
    """Verify that `client.upload_media` sets `Content-Type: application/json`
    on the start request and forwards both `metadata` and `config.headers`."""
    client, interceptor = intercepted_resumable_upload_rest
    payload = b"0123456789" * 100
    stream = io.BytesIO(payload)
    # Pass the scenario header via `metadata` so the server only replies with
    # `X-Goog-Upload-Chunk-Granularity: 256` (aligning chunk_size=300 -> 512
    # instead of the default 262,144) if `metadata` is sent on the start request.
    request_metadata = ("X-Goog-Test-Scenario", "chunk_granularity")

    session = client.upload_media(
        request=UploadMediaRequest(name="custom_headers_upload_media.txt"),
        config=ResumableUploadConfig(
            chunk_size=300,
            headers=[("x-custom-config-header", "config-value")],
        ),
        metadata=[request_metadata],
    )
    response = session.upload(stream=stream)

    assert request_metadata in interceptor.request_metadata
    assert session.chunk_size == 512
    assert isinstance(response, UploadMediaResponse)
    assert response.name == "custom_headers_upload_media.txt"
    assert response.size == len(payload)


if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":

    @pytest.mark.asyncio
    async def test_async_client_upload_media_end_to_end(
        intercepted_resumable_upload_rest_async,
    ):
        """Verify end-to-end async resumable upload via ResumableUploadServiceAsyncClient."""
        client, _ = intercepted_resumable_upload_rest_async
        payload = b"0123456789" * 100
        stream = io.BytesIO(payload)

        session = await client.upload_media(
            request=UploadMediaRequest(name="async_client_upload_media.txt"),
            config=ResumableUploadConfig(chunk_size=256),
        )
        response = await session.upload(stream=stream)

        assert isinstance(response, UploadMediaResponse)
        assert response.name == "async_client_upload_media.txt"
        assert response.size == len(payload)

    @pytest.mark.asyncio
    async def test_async_client_upload_media_with_custom_headers_sets_json_content_type(
        intercepted_resumable_upload_rest_async,
    ):
        """Verify that `async_client.upload_media` sets `Content-Type: application/json`
        on the start request and forwards both `metadata` and `config.headers`."""
        client, interceptor = intercepted_resumable_upload_rest_async
        payload = b"0123456789" * 100
        stream = io.BytesIO(payload)
        request_metadata = ("X-Goog-Test-Scenario", "chunk_granularity")

        session = await client.upload_media(
            request=UploadMediaRequest(name="async_custom_headers_upload_media.txt"),
            config=ResumableUploadConfig(
                chunk_size=300,
                headers=[("x-custom-config-header", "config-value")],
            ),
            metadata=[request_metadata],
        )
        response = await session.upload(stream=stream)

        assert request_metadata in interceptor.request_metadata
        assert session.chunk_size == 512
        assert isinstance(response, UploadMediaResponse)
        assert response.name == "async_custom_headers_upload_media.txt"
        assert response.size == len(payload)

    @pytest.mark.asyncio
    async def test_async_client_upload_media_progress_tracking(
        intercepted_resumable_upload_rest_async,
    ):
        """Verify async progress iteration over ResumableUploadServiceAsyncClient.upload_media."""
        client, _ = intercepted_resumable_upload_rest_async
        chunk_size = 262_144  # 256 KiB
        total_size = 600_000
        payload = b"A" * total_size
        stream = io.BytesIO(payload)

        session = await client.upload_media(
            request=UploadMediaRequest(name="async_multi_chunk.bin"),
            config=ResumableUploadConfig(chunk_size=chunk_size),
        )

        progress_records = [
            p async for p in session.upload(stream=stream, size=total_size)
        ]

        assert isinstance(session.response, UploadMediaResponse)
        assert session.response.name == "async_multi_chunk.bin"
        assert session.response.size == total_size

        phases = [p.state for p in progress_records]
        offsets = [p.bytes_uploaded for p in progress_records]
        assert phases == [
            ProgressState.STARTED,
            ProgressState.UPLOADING,
            ProgressState.UPLOADING,
            ProgressState.FINALIZED,
        ]
        assert offsets == [0, 262_144, 524_288, 600_000]
        assert all(p.total_bytes == total_size for p in progress_records)


# =============================================================================
# End-to-End Client Sample Patterns & 2.1 Golden Path Suite (gRPC & REST)
# =============================================================================


def _create_sync_client(transport, monkeypatch):
    monkeypatch.setenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
    return ResumableUploadServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options={"api_endpoint": SHOWCASE_API_ENDPOINT},
        transport=transport,
    )


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_sample_option_1_direct_upload(transport, monkeypatch):
    """Option 1: Direct upload from start to completion across gRPC and REST transports."""
    client = _create_sync_client(transport, monkeypatch)
    payload = b"0123456789" * 100
    stream = io.BytesIO(payload)

    request = UploadMediaRequest(name="sample_option_1_sync.txt")
    config = ResumableUploadConfig(chunk_size=262_144)

    upload_session = client.upload_media(request=request, config=config)
    response = upload_session.upload(stream)

    assert isinstance(response, UploadMediaResponse)
    assert response.name == "sample_option_1_sync.txt"
    assert response.size == len(payload)


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_sample_option_2_progress_tracking_upload(transport, monkeypatch):
    """Option 2: Upload while receiving progress updates across gRPC and REST transports."""
    client = _create_sync_client(transport, monkeypatch)
    chunk_size = 262_144  # 256 KiB
    total_size = 600_000
    payload = b"P" * total_size
    stream = io.BytesIO(payload)

    request = UploadMediaRequest(name="sample_option_2_sync.bin")
    config = ResumableUploadConfig(chunk_size=chunk_size)

    upload_session = client.upload_media(request=request, config=config)
    progress_snapshots: List[UploadProgress] = []
    for progress in upload_session.iter_upload(stream):
        progress_snapshots.append(progress)

    response = upload_session.response
    assert isinstance(response, UploadMediaResponse)
    assert response.name == "sample_option_2_sync.bin"
    assert response.size == total_size
    assert [p.state for p in progress_snapshots] == [
        ProgressState.STARTED,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.FINALIZED,
    ]
    assert [p.bytes_uploaded for p in progress_snapshots] == [
        0,
        262_144,
        524_288,
        total_size,
    ]


# -----------------------------------------------------------------------------
# 2.1 Golden Path Suite (End-to-End Client across gRPC & REST)
# -----------------------------------------------------------------------------


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_client_multi_chunk_known_size(transport, monkeypatch):
    """Golden Path Case 1: Multi-chunk upload with known size (1.5 MB, 512 KiB chunks)."""
    client = _create_sync_client(transport, monkeypatch)
    total_size = 1_500_000
    chunk_size = 524_288  # 512 KiB
    stream = io.BytesIO(b"M" * total_size)

    upload_session = client.upload_media(
        request=UploadMediaRequest(name="multi_chunk_known_size.mp4"),
        config=ResumableUploadConfig(chunk_size=chunk_size),
    )
    progress_records = list(
        upload_session.iter_upload(stream, size=total_size)
    )

    assert isinstance(upload_session.response, UploadMediaResponse)
    assert upload_session.response.name == "multi_chunk_known_size.mp4"
    assert upload_session.response.size == total_size
    assert [p.state for p in progress_records] == [
        ProgressState.STARTED,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.FINALIZED,
    ]
    assert [p.bytes_uploaded for p in progress_records] == [
        0,
        524_288,
        1_048_576,
        1_500_000,
    ]
    assert all(p.total_bytes == total_size for p in progress_records)


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_client_small_upload_default_chunk_size(transport, monkeypatch):
    """Golden Path Case 2: Default chunk size on small upload (~100 KB)."""
    client = _create_sync_client(transport, monkeypatch)
    total_size = 100_000
    stream = io.BytesIO(b"S" * total_size)

    upload_session = client.upload_media(
        request=UploadMediaRequest(name="small_default_chunk.bin"),
    )
    progress_records = list(
        upload_session.iter_upload(stream, size=total_size)
    )

    assert upload_session.chunk_size <= DEFAULT_CHUNK_SIZE
    assert isinstance(upload_session.response, UploadMediaResponse)
    assert upload_session.response.name == "small_default_chunk.bin"
    assert upload_session.response.size == total_size
    assert [p.state for p in progress_records] == [
        ProgressState.STARTED,
        ProgressState.FINALIZED,
    ]
    assert [p.bytes_uploaded for p in progress_records] == [0, 100_000]
    assert all(p.total_bytes == total_size for p in progress_records)


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_client_standalone_finalize_unseekable_stream(transport, monkeypatch):
    """Golden Path Case 3: Unseekable stream with unknown size and exact chunk multiple."""
    client = _create_sync_client(transport, monkeypatch)
    chunk_size = 262_144  # 256 KiB
    total_size = 3 * chunk_size  # 786_432 bytes
    stream = _UnknownSizeUnseekableStream(b"U" * total_size)

    upload_session = client.upload_media(
        request=UploadMediaRequest(name="unseekable_exact_multiple.bin"),
        config=ResumableUploadConfig(chunk_size=chunk_size),
    )
    progress_records = list(upload_session.iter_upload(stream, size=None))

    assert isinstance(upload_session.response, UploadMediaResponse)
    assert upload_session.response.name == "unseekable_exact_multiple.bin"
    assert upload_session.response.size == total_size
    assert [p.state for p in progress_records] == [
        ProgressState.STARTED,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.FINALIZED,
    ]
    assert [p.bytes_uploaded for p in progress_records] == [
        0,
        262_144,
        524_288,
        786_432,
        786_432,
    ]
    assert all(p.total_bytes is None for p in progress_records)


if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":

    def _create_async_client(transport, monkeypatch):
        monkeypatch.setenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
        if not HAS_ASYNC_REST_RESUMABLE_UPLOAD_TRANSPORT:
            pytest.skip("Async REST transport not available.")
        if (
            transport == "rest_asyncio"
            and "rest_asyncio"
            not in ResumableUploadServiceClient._transport_registry
        ):
            pytest.skip(
                "rest_asyncio transport is not registered when rest_async_io_enabled is False."
            )
        return ResumableUploadServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            client_options={"api_endpoint": SHOWCASE_API_ENDPOINT},
            transport=transport,
        )

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_sample_option_1_direct_upload(transport, monkeypatch):
        """Async Option 1: Direct upload from start to completion."""
        client = _create_async_client(transport, monkeypatch)
        payload = b"0123456789" * 100
        stream = io.BytesIO(payload)

        request = UploadMediaRequest(name="sample_option_1_async.txt")
        config = ResumableUploadConfig(chunk_size=262_144)

        upload_session = await client.upload_media(
            request=request, config=config
        )
        response = await upload_session.upload(stream)

        assert isinstance(response, UploadMediaResponse)
        assert response.name == "sample_option_1_async.txt"
        assert response.size == len(payload)

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_sample_option_2_progress_tracking_upload(
        transport, monkeypatch
    ):
        """Async Option 2: Upload while receiving progress updates."""
        client = _create_async_client(transport, monkeypatch)
        chunk_size = 262_144  # 256 KiB
        total_size = 600_000
        payload = b"P" * total_size
        stream = io.BytesIO(payload)

        request = UploadMediaRequest(name="sample_option_2_async.bin")
        config = ResumableUploadConfig(chunk_size=chunk_size)

        upload_session = await client.upload_media(
            request=request, config=config
        )
        progress_snapshots: List[UploadProgress] = []
        async for progress in upload_session.upload(stream):
            progress_snapshots.append(progress)

        response = upload_session.response
        assert isinstance(response, UploadMediaResponse)
        assert response.name == "sample_option_2_async.bin"
        assert response.size == total_size
        assert [p.state for p in progress_snapshots] == [
            ProgressState.STARTED,
            ProgressState.UPLOADING,
            ProgressState.UPLOADING,
            ProgressState.FINALIZED,
        ]
        assert [p.bytes_uploaded for p in progress_snapshots] == [
            0,
            262_144,
            524_288,
            total_size,
        ]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_multi_chunk_known_size(transport, monkeypatch):
        """Async Golden Path Case 1: Multi-chunk upload with known size."""
        client = _create_async_client(transport, monkeypatch)
        total_size = 1_500_000
        chunk_size = 524_288
        stream = io.BytesIO(b"M" * total_size)

        upload_session = await client.upload_media(
            request=UploadMediaRequest(name="async_multi_chunk_known_size.mp4"),
            config=ResumableUploadConfig(chunk_size=chunk_size),
        )
        progress_records = [
            p async for p in upload_session.upload(stream, size=total_size)
        ]

        assert isinstance(upload_session.response, UploadMediaResponse)
        assert upload_session.response.name == "async_multi_chunk_known_size.mp4"
        assert upload_session.response.size == total_size
        assert [p.state for p in progress_records] == [
            ProgressState.STARTED,
            ProgressState.UPLOADING,
            ProgressState.UPLOADING,
            ProgressState.FINALIZED,
        ]
        assert [p.bytes_uploaded for p in progress_records] == [
            0,
            524_288,
            1_048_576,
            1_500_000,
        ]
        assert all(p.total_bytes == total_size for p in progress_records)

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_small_upload_default_chunk_size(
        transport, monkeypatch
    ):
        """Async Golden Path Case 2: Default chunk size on small upload."""
        client = _create_async_client(transport, monkeypatch)
        total_size = 100_000
        stream = io.BytesIO(b"S" * total_size)

        upload_session = await client.upload_media(
            request=UploadMediaRequest(name="async_small_default_chunk.bin"),
        )
        progress_records = [
            p async for p in upload_session.upload(stream, size=total_size)
        ]

        assert upload_session.chunk_size <= DEFAULT_CHUNK_SIZE
        assert isinstance(upload_session.response, UploadMediaResponse)
        assert upload_session.response.name == "async_small_default_chunk.bin"
        assert upload_session.response.size == total_size
        assert [p.state for p in progress_records] == [
            ProgressState.STARTED,
            ProgressState.FINALIZED,
        ]
        assert [p.bytes_uploaded for p in progress_records] == [0, 100_000]
        assert all(p.total_bytes == total_size for p in progress_records)

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_standalone_finalize_unseekable_stream(
        transport, monkeypatch
    ):
        """Async Golden Path Case 3: Unseekable stream with unknown size and exact chunk multiple."""
        client = _create_async_client(transport, monkeypatch)
        chunk_size = 262_144
        total_size = 3 * chunk_size
        stream = _UnknownSizeUnseekableStream(b"U" * total_size)

        upload_session = await client.upload_media(
            request=UploadMediaRequest(
                name="async_unseekable_exact_multiple.bin"
            ),
            config=ResumableUploadConfig(chunk_size=chunk_size),
        )
        progress_records = [
            p async for p in upload_session.upload(stream, size=None)
        ]

        assert isinstance(upload_session.response, UploadMediaResponse)
        assert (
            upload_session.response.name
            == "async_unseekable_exact_multiple.bin"
        )
        assert upload_session.response.size == total_size
        assert [p.state for p in progress_records] == [
            ProgressState.STARTED,
            ProgressState.UPLOADING,
            ProgressState.UPLOADING,
            ProgressState.UPLOADING,
            ProgressState.FINALIZED,
        ]
        assert [p.bytes_uploaded for p in progress_records] == [
            0,
            262_144,
            524_288,
            786_432,
            786_432,
        ]
        assert all(p.total_bytes is None for p in progress_records)
