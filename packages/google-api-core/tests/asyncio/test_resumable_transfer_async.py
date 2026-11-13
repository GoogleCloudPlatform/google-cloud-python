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

"""Asynchronous tests for Resumable Upload protocol implementation."""

# mypy: disable-error-code="arg-type"

import asyncio
import datetime
import inspect
import io
import json
from typing import (
    Any,
    AsyncIterable,
    AsyncIterator,
    Dict,
    List,
    Mapping,
    Optional,
    Tuple,
    Union,
)
from unittest import mock

import pytest
from google.auth import exceptions as auth_exceptions
from google.protobuf import empty_pb2

from google.api_core import exceptions
from google.api_core.resumable_transfer import (
    AsyncResumableUploadSession,
    AsyncUploadOperation,
    ProgressState,
    ResumableUploadConfig,
    TransferStalledError,
    UnseekableStreamError,
    UploadCancelledError,
    UploadProgress,
    common,
    upload_async,
)
from tests.helpers import EchoResponse

try:
    import aiohttp  # noqa: F401
    import google.auth.aio.transport  # noqa: F401
    from google.auth.aio import credentials as aio_credentials
    from google.auth.aio.transport import sessions as aio_sessions

    GOOGLE_AUTH_AIO_INSTALLED = True
except ImportError:
    GOOGLE_AUTH_AIO_INSTALLED = False


@pytest.fixture(autouse=True)
def check_async_rest_installed(request: pytest.FixtureRequest) -> None:
    if request.node.name == "test_async_ensure_aiohttp_missing":
        return
    if not GOOGLE_AUTH_AIO_INSTALLED:
        pytest.skip("Skipped because google-api-core[async_rest] is not installed")


class DummyResponse:
    """Mock response class representing a deserialized protobuf message."""

    def __init__(self, name: str, size: int) -> None:
        """Initializes a DummyResponse.

        Args:
            name: Resource name string.
            size: Resource size in bytes.
        """
        self.name = name
        self.size = size

    @classmethod
    def from_json(cls, data: Union[str, bytes]) -> "DummyResponse":
        """Deserializes JSON payload into a DummyResponse instance.

        Args:
            data: JSON byte string or text.

        Returns:
            A DummyResponse instance.
        """
        d = json.loads(data.decode("utf-8") if isinstance(data, bytes) else data)
        return cls(name=d.get("name", ""), size=d.get("size", 0))


class DummyAsyncResponse:
    """Mock HTTP response conforming to aiohttp.ClientResponse interface."""

    def __init__(
        self,
        status: int = 200,
        headers: Optional[Mapping[str, str]] = None,
        body: bytes = b"",
    ) -> None:
        """Initializes a DummyAsyncResponse.

        Args:
            status: HTTP status code.
            headers: HTTP response headers mapping.
            body: Response payload bytes.
        """
        self.status = status
        self.headers = headers or {}
        self._body = body

    async def read(self) -> bytes:
        """Reads and returns response payload bytes.

        Returns:
            Raw response payload bytes.
        """
        return self._body

    async def __aenter__(self) -> "DummyAsyncResponse":
        """Enters the asynchronous context manager.

        Returns:
            The DummyAsyncResponse instance.
        """
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Exits the asynchronous context manager.

        Args:
            exc_type: Exception type if raised.
            exc_val: Exception value if raised.
            exc_tb: Exception traceback if raised.
        """
        pass


class DummyAsyncSession:
    """Mock asynchronous HTTP client session conforming to aiohttp.ClientSession interface."""

    def __init__(self, responses: Optional[List[DummyAsyncResponse]] = None) -> None:
        """Initializes a DummyAsyncSession.

        Args:
            responses: Sequence of canned DummyAsyncResponse objects.
        """
        self._responses: List[DummyAsyncResponse] = list(responses or [])
        self.requests: List[Tuple[str, str, Dict[str, Any]]] = []

    def request(self, method: str, url: str, **kwargs: Any) -> DummyAsyncResponse:
        """Records the request and yields the next canned response.

        Args:
            method: HTTP method verb.
            url: Destination endpoint URL.
            **kwargs: Additional request parameters.

        Returns:
            Next canned DummyAsyncResponse.
        """
        self.requests.append((method, url, kwargs))
        if not self._responses:
            return DummyAsyncResponse(status=200, headers={}, body=b"")
        return self._responses.pop(0)


class NonSeekableBytesIO(io.BytesIO):
    """BytesIO stream simulation with seekable returning False."""

    def seekable(self) -> bool:
        """Reports whether the stream supports random access.

        Returns:
            False unconditionally.
        """
        return False


# =====================================================================
# 1. Initialization and Configuration Tests
# =====================================================================


def test_async_session_initialization_defaults() -> None:
    """Validates default attribute values of an uninitiated async session."""
    session = AsyncResumableUploadSession(upload_url="https://api.example.com/start")
    assert session.upload_url == "https://api.example.com/start"
    assert session.chunk_size == common.DEFAULT_CHUNK_SIZE
    assert session.response is None
    assert session.bytes_uploaded == 0
    assert session.finished is False


def test_async_missing_transport_raises() -> None:
    """Verifies that invoking session operations without a transport raises ValueError."""
    session = AsyncResumableUploadSession()

    with pytest.raises(ValueError, match="aiohttp.ClientSession"):
        session.upload(stream=b"data")

    with pytest.raises(ValueError, match="aiohttp.ClientSession"):
        session.resume(upload_url="https://upload.example.com", stream=b"data")


@pytest.mark.asyncio
async def test_async_cancel_missing_transport_raises() -> None:
    """Verifies that cancel without a transport raises ValueError."""
    session = AsyncResumableUploadSession()
    with pytest.raises(ValueError, match="aiohttp.ClientSession"):
        await session.cancel()


def test_async_ensure_aiohttp_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    """Verifies that _ensure_aiohttp raises ImportError when aiohttp is unavailable."""
    monkeypatch.setattr(upload_async, "_HAS_AIOHTTP", False)
    session = AsyncResumableUploadSession()
    with pytest.raises(ImportError, match="google-api-core\\[async_rest\\]"):
        session._ensure_aiohttp()


# =====================================================================
# 2. Upload Execution and Operation Handle Tests
# =====================================================================


@pytest.mark.asyncio
async def test_async_upload_direct_execution() -> None:
    """Verifies single-chunk upload execution with protobuf deserialization."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"name": "async_file.txt", "size": 10}',
    )

    async_transport = DummyAsyncSession([start_resp, chunk_resp])
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=DummyResponse,
        transport=async_transport,
    )

    result = await session.upload(stream=b"0123456789", request_body='{"name": "test"}')

    assert isinstance(result, DummyResponse)
    assert result.name == "async_file.txt"
    assert result.size == 10
    assert session.finished is True
    assert session.bytes_uploaded == 10
    assert session.upload_url == "https://upload.example.com/resumable-async"


def _make_single_chunk_async_transport() -> DummyAsyncSession:
    """Builds a DummyAsyncSession returning a start response and a final chunk response."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b"",
    )
    return DummyAsyncSession([start_resp, chunk_resp])


@pytest.mark.asyncio
async def test_async_upload_uses_session_request_body() -> None:
    """Verifies the constructor request_body is sent with the start request by default."""
    async_transport = _make_single_chunk_async_transport()
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=async_transport,
        request_body='{"name": "from-init"}',
    )

    await session.upload(stream=b"payload")

    _, _, start_kwargs = async_transport.requests[0]
    assert start_kwargs["data"] == b'{"name": "from-init"}'
    assert start_kwargs["headers"]["X-Goog-Upload-Command"] == "start"


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "override, expected",
    [
        ('{"name": "override"}', b'{"name": "override"}'),
        (b'{"name": "override-bytes"}', b'{"name": "override-bytes"}'),
        ("", b""),
    ],
)
async def test_async_upload_request_body_argument_overrides_session_default(
    override: Union[str, bytes], expected: bytes
) -> None:
    """Verifies an explicit per-call request_body (even empty) overrides the constructor default."""
    async_transport = _make_single_chunk_async_transport()
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=async_transport,
        request_body='{"name": "from-init"}',
    )

    await session.upload(stream=b"payload", request_body=override)

    _, _, start_kwargs = async_transport.requests[0]
    assert start_kwargs["data"] == expected


@pytest.mark.asyncio
async def test_async_upload_request_body_positional_override() -> None:
    """Verifies request_body remains the second positional parameter of upload()."""
    async_transport = _make_single_chunk_async_transport()
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=async_transport,
        request_body='{"name": "from-init"}',
    )

    await session.upload(b"payload", '{"name": "positional"}')

    _, _, start_kwargs = async_transport.requests[0]
    assert start_kwargs["data"] == b'{"name": "positional"}'


@pytest.mark.asyncio
async def test_async_upload_request_body_defaults_to_empty() -> None:
    """Verifies the start request carries an empty payload when no request_body is configured."""
    async_transport = _make_single_chunk_async_transport()
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=async_transport,
    )

    await session.upload(stream=b"payload")

    _, _, start_kwargs = async_transport.requests[0]
    assert start_kwargs["data"] == b""


@pytest.mark.asyncio
async def test_async_upload_multi_chunk_operation_handle() -> None:
    """Verifies multi-chunk upload dispatching and AsyncUploadOperation property handles."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk1_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "active"},
        body=b"",
    )
    chunk2_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"name": "multi.txt", "size": 8}',
    )

    async_transport = DummyAsyncSession([start_resp, chunk1_resp, chunk2_resp])
    config = ResumableUploadConfig(chunk_size=4)
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        response_type=DummyResponse,
        transport=async_transport,
    )

    upload_op = session.upload(stream=b"12345678")
    assert isinstance(upload_op, AsyncUploadOperation)
    assert upload_op.chunk_size == 4

    result = await upload_op
    assert isinstance(result, DummyResponse)
    assert result.name == "multi.txt"
    assert upload_op.response == result
    assert upload_op.bytes_uploaded == 8
    assert upload_op.upload_url == "https://upload.example.com/resumable-async"

    # Validate commands dispatched in request history
    assert len(async_transport.requests) == 3
    # Start request
    assert async_transport.requests[0][2]["headers"]["X-Goog-Upload-Command"] == "start"
    # Chunk 1 request
    assert (
        async_transport.requests[1][2]["headers"]["X-Goog-Upload-Command"] == "upload"
    )
    assert async_transport.requests[1][2]["headers"]["X-Goog-Upload-Offset"] == "0"
    # Chunk 2 request (last chunk concludes transfer)
    assert (
        async_transport.requests[2][2]["headers"]["X-Goog-Upload-Command"]
        == "upload, finalize"
    )
    assert async_transport.requests[2][2]["headers"]["X-Goog-Upload-Offset"] == "4"


@pytest.mark.asyncio
async def test_async_upload_progress_tracking() -> None:
    """Verifies that progress stream yields snapshots matching transmission milestones."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk1_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "active"},
        body=b"",
    )
    chunk2_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"name": "progress.txt", "size": 8}',
    )

    async_transport = DummyAsyncSession([start_resp, chunk1_resp, chunk2_resp])
    config = ResumableUploadConfig(chunk_size=4)
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        response_type=DummyResponse,
        transport=async_transport,
    )

    upload_op = session.upload(stream=b"12345678")
    progress_list: List[UploadProgress] = []
    async for p in upload_op.progress():
        progress_list.append(p)

    final_resp = await upload_op
    assert isinstance(final_resp, DummyResponse)
    assert len(progress_list) == 3
    assert progress_list[0].state == ProgressState.STARTED
    assert progress_list[1].state == ProgressState.UPLOADING
    assert progress_list[1].bytes_uploaded == 4
    assert progress_list[2].state == ProgressState.FINALIZED
    assert progress_list[2].bytes_uploaded == 8


# =====================================================================
# 3. Stream Input Types Tests
# =====================================================================


@pytest.mark.asyncio
async def test_async_stream_types_async_iterable() -> None:
    """Verifies upload compatibility with an asynchronous generator stream."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"name": "async_gen.txt", "size": 6}',
    )

    async_transport = DummyAsyncSession([start_resp, chunk_resp])

    async def async_generator() -> AsyncIterator[bytes]:
        yield b"abc"
        yield b"def"

    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=DummyResponse,
        transport=async_transport,
    )

    resp = await session.upload(stream=async_generator())
    assert resp.name == "async_gen.txt"
    assert session.bytes_uploaded == 6


@pytest.mark.asyncio
async def test_async_stream_types_binary_io() -> None:
    """Verifies upload compatibility with a seekable BinaryIO stream."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"name": "bytes_io.txt", "size": 5}',
    )

    async_transport = DummyAsyncSession([start_resp, chunk_resp])
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=DummyResponse,
        transport=async_transport,
    )

    stream = io.BytesIO(b"hello")
    resp = await session.upload(stream=stream)
    assert resp.name == "bytes_io.txt"
    assert session.bytes_uploaded == 5


@pytest.mark.asyncio
async def test_async_stream_types_sync_iterable() -> None:
    """Verifies upload compatibility with a synchronous iterable of byte chunks."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"name": "iterable.txt", "size": 6}',
    )

    async_transport = DummyAsyncSession([start_resp, chunk_resp])
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=DummyResponse,
        transport=async_transport,
    )

    resp = await session.upload(stream=[b"foo", b"bar"])
    assert resp.name == "iterable.txt"
    assert session.bytes_uploaded == 6


def test_async_stream_types_unsupported_raises() -> None:
    """Verifies that passing an unsupported stream type raises TypeError."""
    session = AsyncResumableUploadSession(transport=DummyAsyncSession())
    prepare_reader = getattr(session, "_prepare_async_reader")
    with pytest.raises(TypeError, match="Unsupported stream type"):
        prepare_reader(stream=12345, size=10)


# =====================================================================
# 4. Resume and Offset Recovery Tests
# =====================================================================


@pytest.mark.asyncio
async def test_async_resume_success() -> None:
    """Verifies resuming an existing upload by querying server offset."""
    query_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "5",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"name": "resumed_async.txt", "size": 10}',
    )

    async_transport = DummyAsyncSession([query_resp, chunk_resp])
    session = AsyncResumableUploadSession(
        response_type=DummyResponse,
        transport=async_transport,
    )

    upload_op = session.resume(
        upload_url="https://upload.example.com/resumable-async",
        stream=b"0123456789",
    )
    resp = await upload_op
    assert resp.name == "resumed_async.txt"
    assert session.bytes_uploaded == 10
    assert session.finished is True

    # First request was query
    assert async_transport.requests[0][2]["headers"]["X-Goog-Upload-Command"] == "query"
    # Second request was remaining chunk starting from offset 5
    assert async_transport.requests[1][2]["headers"]["X-Goog-Upload-Offset"] == "5"


def test_async_resume_missing_arguments_raises() -> None:
    """Verifies that resume raises ValueError when upload_url or stream is missing."""
    session = AsyncResumableUploadSession(transport=DummyAsyncSession())
    with pytest.raises(ValueError, match="An upload URL must be provided to resume"):
        session.resume(upload_url="", stream=b"data")

    with pytest.raises(
        ValueError, match="A data stream or payload must be provided to resume"
    ):
        session.resume(
            upload_url="https://upload.example.com/resumable-async",
            stream=None,  # type: ignore[arg-type]
        )


@pytest.mark.asyncio
async def test_async_resume_recovery_unseekable_stream_raises() -> None:
    """Verifies that UnseekableStreamError is raised if server offset cannot be rewound."""
    query_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "100",
        },
        body=b"",
    )

    async_transport = DummyAsyncSession([query_resp])
    session = AsyncResumableUploadSession(
        response_type=DummyResponse,
        transport=async_transport,
    )

    stream = NonSeekableBytesIO(b"some content")
    upload_op = session.resume(
        upload_url="https://upload.example.com/resumable-async",
        stream=stream,
    )

    with pytest.raises(UnseekableStreamError) as exc_info:
        await upload_op

    assert exc_info.value.upload_url == "https://upload.example.com/resumable-async"


@pytest.mark.asyncio
async def test_async_resume_recovery_seekable_stream() -> None:
    """Verifies that seekable streams are rewound to committed server offset."""
    query_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "3",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"name": "seekable.txt", "size": 6}',
    )

    async_transport = DummyAsyncSession([query_resp, chunk_resp])
    session = AsyncResumableUploadSession(
        response_type=DummyResponse,
        transport=async_transport,
    )

    stream = io.BytesIO(b"abcdef")
    upload_op = session.resume(
        upload_url="https://upload.example.com/resumable-async",
        stream=stream,
    )
    resp = await upload_op
    assert resp.name == "seekable.txt"
    assert session.bytes_uploaded == 6


# =====================================================================
# 5. Cancellation Tests
# =====================================================================


@pytest.mark.asyncio
async def test_async_cancel_success() -> None:
    """Verifies client-initiated cancellation marks session state invalid."""
    cancel_resp = DummyAsyncResponse(status=200, headers={}, body=b"")
    async_transport = DummyAsyncSession([cancel_resp])

    session = AsyncResumableUploadSession(
        upload_url="https://upload.example.com/resumable-async",
        transport=async_transport,
    )
    await session.cancel()
    assert session._state.invalid is True
    assert (
        async_transport.requests[0][2]["headers"]["X-Goog-Upload-Command"] == "cancel"
    )


@pytest.mark.asyncio
async def test_async_server_cancelled_raises_error() -> None:
    """Verifies that server returning cancelled status raises UploadCancelledError."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "cancelled"},
        body=b"",
    )

    async_transport = DummyAsyncSession([start_resp, chunk_resp])
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=async_transport,
    )

    with pytest.raises(UploadCancelledError, match="cancelled by server"):
        await session.upload(stream=b"12345")


# =====================================================================
# 6. Retry and Error Handling Tests
# =====================================================================


@pytest.mark.asyncio
async def test_async_retry_transient_http_errors() -> None:
    """Verifies transparent retries on transient HTTP status codes (503 Service Unavailable)."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_503 = DummyAsyncResponse(status=503, headers={}, body=b"Service Unavailable")
    chunk_success = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"name": "retried.txt", "size": 5}',
    )

    async_transport = DummyAsyncSession([start_resp, chunk_503, chunk_success])
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=DummyResponse,
        transport=async_transport,
    )

    with mock.patch("asyncio.sleep", new_callable=mock.AsyncMock):
        resp = await session.upload(stream=b"hello")

    assert resp.name == "retried.txt"
    assert session.finished is True


@pytest.mark.asyncio
async def test_async_non_retryable_error_raises() -> None:
    """Verifies that non-retryable errors (e.g. 404 Not Found) terminate immediately."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_404 = DummyAsyncResponse(status=404, headers={}, body=b"Not Found")

    async_transport = DummyAsyncSession([start_resp, chunk_404])
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=async_transport,
    )

    with pytest.raises(exceptions.NotFound):
        await session.upload(stream=b"test")


@pytest.mark.asyncio
async def test_async_recoverable_status_code_triggers_recovery() -> None:
    """Verifies that recoverable error status codes trigger query and offset reconciliation."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    # Chunk 1 returns Category 2 recoverable error (412 Precondition Failed)
    chunk_precondition_failed = DummyAsyncResponse(
        status=412, headers={}, body=b"Precondition Failed"
    )
    # Recovery query returns confirmed committed offset 0
    query_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "0",
        },
        body=b"",
    )
    # Retransmission succeeds
    chunk_success = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"name": "recovered.txt", "size": 5}',
    )

    async_transport = DummyAsyncSession(
        [start_resp, chunk_precondition_failed, query_resp, chunk_success]
    )
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=DummyResponse,
        transport=async_transport,
    )

    with mock.patch("asyncio.sleep", new_callable=mock.AsyncMock):
        resp = await session.upload(stream=b"hello")

    assert resp.name == "recovered.txt"
    assert session.bytes_uploaded == 5


@pytest.mark.asyncio
async def test_async_missing_status_header_triggers_recovery() -> None:
    """Verifies that missing status header triggers query recovery."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    # Successful HTTP status but missing X-Goog-Upload-Status header
    chunk_missing_hdr = DummyAsyncResponse(status=200, headers={}, body=b"")
    # Recovery query
    query_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "0",
        },
        body=b"",
    )
    chunk_success = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"name": "header_recovered.txt", "size": 5}',
    )

    async_transport = DummyAsyncSession(
        [start_resp, chunk_missing_hdr, query_resp, chunk_success]
    )
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=DummyResponse,
        transport=async_transport,
    )

    with mock.patch("asyncio.sleep", new_callable=mock.AsyncMock):
        resp = await session.upload(stream=b"hello")

    assert resp.name == "header_recovered.txt"


# =====================================================================
# 7. Stall Control and Deadline Tests
# =====================================================================


@pytest.mark.asyncio
async def test_async_stall_timeout_raises_transfer_stalled_error(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Verifies that transfer stalling beyond timeout threshold raises TransferStalledError."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"name": "slow.txt", "size": 10}',
    )

    async_transport = DummyAsyncSession([start_resp, chunk_resp])
    # Expect 100 bytes/sec, timeout 1 second
    config = ResumableUploadConfig(stall_minimum_rate=100, stall_timeout=1.0)
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=async_transport,
    )

    # Simulate elapsed time 10.0 seconds during 10-byte upload (rate = 1 byte/s < 100)
    clock_vals = iter([0.0, 10.0, 10.0])
    monkeypatch.setattr(upload_async, "_monotonic_clock", lambda: next(clock_vals))

    with pytest.raises(TransferStalledError, match="Upload stalled"):
        await session.upload(stream=b"0123456789")

    # config has stall_minimum_rate=100 B/s, stall_timeout=1.0s.
    # 100 bytes / 100 B/s -> expected_sec = 1.0s.
    # Taking 1.2s gives current_lag = 1.2 - 1.0 = 0.2s.
    # Two such chunks accumulate aggregate_lag = 0.4s (< 1.0s stall_timeout),
    # so the transfer does not stall prematurely.
    session3 = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
    )
    session3._update_stall_control(100, 1.2)
    assert session3._aggregate_lag == pytest.approx(0.2)
    session3._update_stall_control(100, 1.2)
    assert session3._aggregate_lag == pytest.approx(0.4)

    # With aggregate_lag = 0.4s (0.2s + 0.2s), next_chunk_timeout is
    # 1.0 - 0.4 + 1.0 = 1.6s. timeout_override=0.5s is smaller, so 0.5s wins.
    assert session3._compute_chunk_timeout(100, timeout_override=0.5) == pytest.approx(
        0.5
    )

    # A third chunk taking 1.6s adds current_lag = 0.6s -> aggregate_lag = 1.0s >= stall_timeout (1.0s),
    # raising TransferStalledError.
    with pytest.raises(TransferStalledError, match="Upload stalled"):
        session3._update_stall_control(100, 1.6)
    session_no_stall = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=ResumableUploadConfig(stall_minimum_rate=0, stall_timeout=0),
    )
    assert session_no_stall._compute_chunk_timeout(
        100, timeout_override=15.0
    ) == pytest.approx(15.0)


@pytest.mark.asyncio
async def test_async_multi_chunk_small_lag_does_not_false_stall(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Verifies that a small lag on chunk 1 does not cause chunk 2's normal transfer
    duration to count toward stall_timeout and falsely raise TransferStalledError."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk1_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "active"},
        body=b"",
    )
    chunk2_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"name": "ok_async.txt", "size": 20480}',
    )
    responses = iter([start_resp, chunk1_resp, chunk2_resp])
    current_time = [0.0]

    class AdvancingClockAsyncSession:
        def request(self, *args: Any, **kwargs: Any) -> DummyAsyncResponse:
            resp = next(responses)
            if resp is not start_resp:
                current_time[0] += 10.5
            return resp

    monkeypatch.setattr(upload_async, "_monotonic_clock", lambda: current_time[0])

    config = ResumableUploadConfig(
        chunk_size=10240,
        stall_minimum_rate=1024,
        stall_timeout=10.0,
    )
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=AdvancingClockAsyncSession(),
        response_type=DummyResponse,
    )

    result = await session.upload(stream=b"x" * 20480)
    assert result.name == "ok_async.txt"
    assert session._aggregate_lag == pytest.approx(1.0)


@pytest.mark.asyncio
async def test_async_deadline_exceeded() -> None:
    """Verifies that exceeding the configured upload deadline raises DeadlineExceeded."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    async_transport = DummyAsyncSession([start_resp])
    past_deadline = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(
        seconds=10
    )
    config = ResumableUploadConfig(deadline=past_deadline)
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=async_transport,
    )

    with pytest.raises(exceptions.DeadlineExceeded):
        await session.upload(stream=b"data")


# =====================================================================
# 8. Response Deserialization Types Tests
# =====================================================================


@pytest.mark.asyncio
async def test_async_response_type_proto_message() -> None:
    """Verifies that a proto.Message type parses final response bytes."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"content": "proto_async_payload"}',
    )

    async_transport = DummyAsyncSession([start_resp, chunk_resp])
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=EchoResponse,
        transport=async_transport,
    )

    result = await session.upload(stream=b"data")
    assert isinstance(result, EchoResponse)
    assert result.content == "proto_async_payload"


@pytest.mark.asyncio
async def test_async_response_type_protobuf_message() -> None:
    """Verifies that a google.protobuf.message.Message type parses final response bytes."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b"{}",
    )

    async_transport = DummyAsyncSession([start_resp, chunk_resp])
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=empty_pb2.Empty,
        transport=async_transport,
    )

    result = await session.upload(stream=b"data")
    assert isinstance(result, empty_pb2.Empty)


@pytest.mark.asyncio
async def test_async_response_type_callable() -> None:
    """Verifies that a custom callable deserializer parses final response body bytes."""
    if not GOOGLE_AUTH_AIO_INSTALLED:
        pytest.skip("Skipped because google-api-core[async_rest] is not installed")

    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b"parsed:hello",
    )

    async_transport = DummyAsyncSession([start_resp, chunk_resp])

    def custom_parser(raw: bytes) -> str:
        return raw.decode("utf-8").upper()

    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=custom_parser,
        transport=async_transport,
    )

    result = await session.upload(stream=b"data")
    assert result == "PARSED:HELLO"


@pytest.mark.asyncio
async def test_async_response_type_raw_bytes() -> None:
    """Verifies that raw bytes are returned when response_type is not configured."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b"raw-bytes-output",
    )

    async_transport = DummyAsyncSession([start_resp, chunk_resp])
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=async_transport,
    )

    result = await session.upload(stream=b"data")
    assert result == b"raw-bytes-output"


@pytest.mark.asyncio
async def test_async_operation_error_propagation_in_progress() -> None:
    """Verifies that background task errors propagate through progress queue iteration."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=403,
        headers={},
        body=b"Permission Denied",
    )

    async_transport = DummyAsyncSession([start_resp, chunk_resp])
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=async_transport,
    )

    upload_op = session.upload(stream=b"data")
    with pytest.raises(exceptions.Forbidden):
        async for _ in upload_op.progress():
            pass

    with pytest.raises(exceptions.Forbidden):
        await upload_op


@pytest.mark.parametrize("invalid_stream", ["invalid_string", {"key": "value"}, 12345])
def test_async_upload_rejects_invalid_stream_types(invalid_stream: Any) -> None:
    """Verifies that str, dict, and non-stream objects raise TypeError synchronously on upload()."""
    async_transport = DummyAsyncSession([])
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=async_transport,
    )
    with pytest.raises(TypeError, match="Unsupported stream type"):
        session.upload(stream=invalid_stream)


@pytest.mark.parametrize("invalid_stream", ["invalid_string", {"key": "value"}, 12345])
def test_async_resume_rejects_invalid_stream_types(invalid_stream: Any) -> None:
    """Verifies that str, dict, and non-stream objects raise TypeError synchronously on resume()."""
    async_transport = DummyAsyncSession([])
    session = AsyncResumableUploadSession(
        transport=async_transport,
    )
    with pytest.raises(TypeError, match="Unsupported stream type"):
        session.resume(
            upload_url="https://upload.example.com/resumable-async",
            stream=invalid_stream,
        )


def test_async_enrich_exception() -> None:
    """Verifies that _enrich_exception attaches upload_url and chunk_size."""
    session = AsyncResumableUploadSession(
        upload_url="https://upload.example.com/resumable-async",
    )
    exc = RuntimeError("test error")
    session._enrich_exception(exc)
    assert getattr(exc, "upload_url") == "https://upload.example.com/resumable-async"


def test_async_notify_progress_branches() -> None:
    """Verifies progress notification queue capture."""
    session = AsyncResumableUploadSession(
        upload_url=None,
    )
    # When upload_url is None
    session._notify_progress(common.ProgressState.UPLOADING)

    # When upload_url is established on state
    session._state._upload_url = "https://upload.example.com/resumable-async"
    # Call with queue=None
    session._notify_progress(common.ProgressState.UPLOADING, queue=None)

    q: List[UploadProgress] = []
    session._notify_progress(common.ProgressState.UPLOADING, queue=q)
    assert len(q) == 1


def test_async_deadline_handling_and_start_timeout() -> None:
    """Verifies deadline remaining calculations and start timeout calculation."""
    # Past deadline raises DeadlineExceeded
    past = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(seconds=10)
    config = ResumableUploadConfig(deadline=past)
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
    )
    with pytest.raises(exceptions.DeadlineExceeded):
        session._get_deadline_remaining()

    # Naive future deadline is localized to UTC
    future_naive = datetime.datetime.now() + datetime.timedelta(hours=1)
    config2 = ResumableUploadConfig(deadline=future_naive)
    session2 = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config2,
    )
    rem = session2._get_deadline_remaining()
    assert rem is not None and rem > 0
    t = session2._get_start_timeout()
    assert t > 0


@pytest.mark.asyncio
async def test_async_retry_branches() -> None:
    """Verifies retry predicate and policy resolution branches in upload_async."""
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
    )

    pred_start = session._get_retry_predicate(is_start=True)
    pred_transfer = session._get_retry_predicate(is_start=False)

    assert pred_start(exceptions.DeadlineExceeded("deadline")) is False
    assert pred_start(exceptions.TransferStalledError("stalled")) is False
    assert pred_start(exceptions.UploadCancelledError("cancelled")) is False
    assert pred_start(exceptions.UnseekableStreamError("unseekable")) is False
    assert pred_start(exceptions.MissingStatusHeaderError("missing")) is False
    assert pred_transfer(exceptions.MissingStatusHeaderError("missing")) is True
    assert pred_start(aiohttp.ClientError("network error")) is True
    assert pred_start(exceptions.from_http_status(503, "Service Unavailable")) is True
    assert pred_start(exceptions.from_http_status(400, "Bad Request")) is False
    assert pred_start(exceptions.from_http_status(412, "Precondition Failed")) is False
    assert (
        pred_start(exceptions.from_http_status(416, "Range Not Satisfiable")) is False
    )
    assert pred_start(exceptions.from_http_status(409, "Conflict")) is False
    assert pred_start(RuntimeError("runtime")) is False

    # Category 1 and Category 2 status codes are retryable during transfer
    assert pred_transfer(exceptions.from_http_status(500, "Internal Error")) is True
    assert pred_transfer(exceptions.from_http_status(400, "Bad Request")) is True
    assert (
        pred_transfer(exceptions.from_http_status(412, "Precondition Failed")) is True
    )
    assert (
        pred_transfer(exceptions.from_http_status(416, "Range Not Satisfiable")) is True
    )
    assert pred_transfer(exceptions.from_http_status(409, "Conflict")) is False

    # Default retry resolution
    default_unary = session._get_async_retry()
    assert isinstance(default_unary, google.api_core.retry.AsyncRetry)

    default_stream = session._get_async_streaming_retry()
    assert isinstance(default_stream, google.api_core.retry.AsyncStreamingRetry)
    assert default_stream.timeout is None

    class CustomApiError(Exception):
        """Example API-specific transient exception provided by a caller."""

    # -------------------------------------------------------------------------
    # Scenario 1: User provides a custom predicate to retry an API-specific error
    # -------------------------------------------------------------------------
    custom_unary = google.api_core.retry.AsyncRetry(
        initial=0.5,
        predicate=lambda exc: isinstance(exc, CustomApiError),
    )
    session_unary = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        start_retry=custom_unary,
    )
    resolved_unary = session_unary._get_async_retry()

    assert isinstance(resolved_unary, google.api_core.retry.AsyncRetry)
    assert resolved_unary._initial == 0.5
    # User's custom exception is retried, while unrelated errors are not
    assert resolved_unary._predicate(CustomApiError("rate limit")) is True
    assert resolved_unary._predicate(ValueError("invalid input")) is False
    # Terminal errors must always return False regardless of custom predicate
    assert (
        resolved_unary._predicate(exceptions.DeadlineExceeded("deadline expired"))
        is False
    )

    # -------------------------------------------------------------------------
    # Scenario 2: Custom AsyncStreamingRetry preserves Category 2 recovery
    # -------------------------------------------------------------------------
    custom_stream = google.api_core.retry.AsyncStreamingRetry(
        initial=0.5,
        predicate=google.api_core.retry.if_exception_type(CustomApiError),
    )
    converted_stream = session_unary._get_async_streaming_retry(
        retry_override=custom_stream
    )
    assert isinstance(converted_stream, google.api_core.retry.AsyncStreamingRetry)
    assert converted_stream._initial == 0.5
    assert converted_stream._predicate(CustomApiError("rate limit")) is True
    # Category 2 recovery (400, 412, 416, MissingStatusHeaderError) is preserved during chunk transfer
    missing_header_error = exceptions.MissingStatusHeaderError(
        "Missing X-Goog-Upload-Status"
    )
    assert converted_stream._predicate(missing_header_error) is True
    assert (
        converted_stream._predicate(
            exceptions.from_http_status(412, "Precondition Failed")
        )
        is True
    )

    # -------------------------------------------------------------------------
    # Scenario 3: Restrictive custom predicate still preserves Category 2 recovery
    # -------------------------------------------------------------------------
    restrictive_stream = google.api_core.retry.AsyncStreamingRetry(
        initial=0.25,
        predicate=lambda exc: False,
    )
    resolved_stream = session._get_async_streaming_retry(
        retry_override=restrictive_stream
    )
    assert isinstance(resolved_stream, google.api_core.retry.AsyncStreamingRetry)
    assert resolved_stream._initial == 0.25
    # Category 2 errors (400, 412, 416, MissingStatusHeaderError) return True so
    # server offset synchronization is preserved
    assert (
        resolved_stream._predicate(exceptions.from_http_status(400, "Bad Request"))
        is True
    )
    assert (
        resolved_stream._predicate(
            exceptions.from_http_status(412, "Precondition Failed")
        )
        is True
    )
    assert (
        resolved_stream._predicate(
            exceptions.from_http_status(416, "Range Not Satisfiable")
        )
        is True
    )
    assert resolved_stream._predicate(missing_header_error) is True
    # Unretriable HTTP status codes (such as 409 Conflict) and non-protocol errors
    # follow the predicate and return False
    assert (
        resolved_stream._predicate(exceptions.from_http_status(409, "Conflict"))
        is False
    )
    bad_gateway_error = exceptions.from_http_status(502, "Bad Gateway")
    assert resolved_stream._predicate(bad_gateway_error) is False
    assert resolved_stream._predicate(RuntimeError("unexpected crash")) is False


def test_async_transport_missing_errors() -> None:
    """Verifies ValueError when transport is missing from upload, resume, and cancel."""
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
    )
    with pytest.raises(
        ValueError, match="or AsyncAuthorizedSession transport must be provided"
    ):
        session.upload(stream=b"data")

    with pytest.raises(
        ValueError, match="or AsyncAuthorizedSession transport must be provided"
    ):
        session.resume(upload_url="https://upload.example.com/123", stream=b"data")


@pytest.mark.asyncio
async def test_async_cancel_missing_transport_and_error() -> None:
    """Verifies cancel method with missing transport and server error."""
    session = AsyncResumableUploadSession(
        upload_url="https://upload.example.com/123",
    )
    with pytest.raises(
        ValueError, match="or AsyncAuthorizedSession transport must be provided"
    ):
        await session.cancel()

    err_resp = DummyAsyncResponse(status=500, headers={}, body=b"Cancel Error")
    sess_transport = DummyAsyncSession([err_resp])
    session2 = AsyncResumableUploadSession(
        upload_url="https://upload.example.com/123",
        transport=sess_transport,
    )
    with pytest.raises(exceptions.GoogleAPICallError):
        await session2.cancel()


@pytest.mark.asyncio
async def test_async_prepare_async_reader_types() -> None:
    """Verifies async reader preparation for native async reader, tell error, and iterables."""
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
    )

    class AsyncReader(AsyncIterable[bytes]):  # Inherit to satisfy mypy
        async def read(self, n: int) -> bytes:
            return b"chunk"

        async def __aiter__(self) -> AsyncIterator[bytes]:
            yield b"chunk"

    reader_fn, size, obj = session._prepare_async_reader(AsyncReader(), None)
    chunk = await reader_fn(5)
    assert chunk == b"chunk"

    # Sync stream whose tell() raises OSError
    class TellFailingStream(io.BytesIO):
        def tell(self) -> int:
            raise OSError("tell error")

    stream = TellFailingStream(b"data")
    reader_fn2, size2, obj2 = session._prepare_async_reader(stream, None)
    chunk2 = await reader_fn2(4)
    assert chunk2 == b"data"
    assert session._start_stream_offset == 0

    # Sync Iterable[bytes]
    reader_fn3, size3, obj3 = session._prepare_async_reader([b"part1", b"part2"], None)
    chunk3 = await reader_fn3(10)
    assert chunk3 == b"part1part2"


@pytest.mark.asyncio
async def test_async_initiate_and_recover_failures() -> None:
    """Verifies initiate and recover error handling when server returns error codes."""
    err_resp = DummyAsyncResponse(status=400, headers={}, body=b"Bad Request")
    sess_transport = DummyAsyncSession([err_resp])
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=sess_transport,
    )
    with pytest.raises(exceptions.BadRequest):
        await session._initiate(transport=sess_transport)

    err_resp2 = DummyAsyncResponse(status=400, headers={}, body=b"Query Failed")
    sess_transport2 = DummyAsyncSession([err_resp2])
    session2 = AsyncResumableUploadSession(
        transport=sess_transport2,
    )
    session2._state._upload_url = "https://upload.example.com/123"
    with pytest.raises(exceptions.BadRequest):
        await session2._recover(sess_transport2)


@pytest.mark.asyncio
async def test_async_recover_stream_errors() -> None:
    """Verifies UnseekableStreamError during async recovery."""
    query_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "active", "X-Goog-Upload-Size-Received": "10"},
        body=b"",
    )
    sess_transport = DummyAsyncSession([query_resp])
    session = AsyncResumableUploadSession(
        transport=sess_transport,
    )
    session._state._upload_url = "https://upload.example.com/123"

    # Stream whose seekable() returns False
    unseekable = mock.Mock()
    unseekable.seekable.return_value = False
    with pytest.raises(UnseekableStreamError, match="Stream is not seekable"):
        await session._recover(sess_transport, stream_obj=unseekable)

    # Stream whose seek() raises OSError
    sess_transport2 = DummyAsyncSession([query_resp])
    session2 = AsyncResumableUploadSession(
        transport=sess_transport2,
    )
    session2._state._upload_url = "https://upload.example.com/123"
    failing_seek = mock.Mock()
    failing_seek.seekable.return_value = True
    failing_seek.seek.side_effect = OSError("Seek error")
    with pytest.raises(UnseekableStreamError, match="Failed to seek stream"):
        await session2._recover(sess_transport2, stream_obj=failing_seek)


@pytest.mark.asyncio
async def test_async_upload_with_timeout_and_deadline() -> None:
    future_deadline = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        seconds=60
    )
    config = ResumableUploadConfig(deadline=future_deadline)

    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    resp = DummyAsyncResponse(
        status=200, headers={"X-Goog-Upload-Status": "final"}, body=b"{}"
    )
    sess_transport = DummyAsyncSession([start_resp, resp])

    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=sess_transport,
    )
    session._state._upload_url = "https://upload.example.com/resumable-async"

    # Run the upload
    res = await session.upload(stream=b"data", timeout=30.0)
    assert res == b"{}"


@pytest.mark.asyncio
async def test_async_transmit_chunk_timeout_errors() -> None:
    # 1. TimeoutError raises TransferStalledError when remaining is > 0
    future_deadline = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        seconds=60
    )
    config = ResumableUploadConfig(deadline=future_deadline)

    class TimeoutAsyncSession:
        def __init__(self):
            self.calls = 0

        def request(self, *args, **kwargs):
            self.calls += 1
            if self.calls == 1:

                class StartContext:
                    async def __aenter__(self):
                        class Resp:
                            status = 200
                            headers = {
                                "X-Goog-Upload-Status": "active",
                                "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
                            }

                            async def read(self):
                                return b""

                        return Resp()

                    async def __aexit__(self, exc_type, exc, tb):
                        pass

                return StartContext()
            else:

                class TimeoutContext:
                    async def __aenter__(self):
                        raise asyncio.TimeoutError("timeout")

                    async def __aexit__(self, exc_type, exc, tb):
                        pass

                return TimeoutContext()

    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=TimeoutAsyncSession(),
    )
    session._state._upload_url = "https://upload.example.com/resumable-async"
    no_retry = google.api_core.retry.AsyncStreamingRetry(
        predicate=lambda e: False, timeout=0.001
    )

    with pytest.raises(exceptions.TransferStalledError):
        await session.upload(stream=b"data", retry=no_retry)

    # 2. TimeoutError raises DeadlineExceeded when deadline expires
    config2 = ResumableUploadConfig(deadline=future_deadline)

    session2 = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config2,
        transport=TimeoutAsyncSession(),
    )
    session2._state._upload_url = "https://upload.example.com/resumable-async"

    with mock.patch.object(
        session2,
        "_get_deadline_remaining",
        side_effect=[5.0, 5.0, exceptions.DeadlineExceeded("Deadline exceeded")],
    ):
        with pytest.raises(exceptions.DeadlineExceeded):
            await session2.upload(stream=b"data", retry=no_retry)

    # 3. Non-timeout RetryError re-raises RetryError rather than TransferStalledError
    class ConnectionErrorAsyncSession:
        def __init__(self):
            self.calls = 0

        def request(self, *args, **kwargs):
            self.calls += 1
            if self.calls == 1:

                class StartContext:
                    async def __aenter__(self):
                        class Resp:
                            status = 200
                            headers = {
                                "X-Goog-Upload-Status": "active",
                                "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
                            }

                            async def read(self):
                                return b""

                        return Resp()

                    async def __aexit__(self, exc_type, exc, tb):
                        pass

                return StartContext()
            else:

                class ErrorContext:
                    async def __aenter__(self):
                        raise aiohttp.ClientConnectionError("Connection dropped")

                    async def __aexit__(self, exc_type, exc, tb):
                        pass

                return ErrorContext()

    session3 = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=ConnectionErrorAsyncSession(),
    )
    session3._state._upload_url = "https://upload.example.com/resumable-async"

    with pytest.raises(exceptions.RetryError):
        await session3.upload(stream=b"data", retry=no_retry)


@pytest.mark.asyncio
async def test_async_upload_multiple_chunks_async_iterable() -> None:
    # chunk_size = 3, payload = b"012345" (6 bytes)
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk1_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "active"},
        body=b"",
    )
    chunk2_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b"{}",
    )
    sess_transport = DummyAsyncSession([start_resp, chunk1_resp, chunk2_resp])

    async def async_gen():
        yield b"012"
        yield b"345"

    config = ResumableUploadConfig(chunk_size=3)
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=sess_transport,
    )
    session._state._upload_url = "https://upload.example.com/resumable-async"

    res = await session.upload(stream=async_gen())
    assert res == b"{}"


@pytest.mark.asyncio
async def test_async_prepare_async_reader_additional_branches() -> None:
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
    )

    # Inherit from concrete io.BytesIO so mypy recognizes these test streams as
    # valid BinaryIO instances natively.
    class LocalNoTellStream(io.BytesIO):
        """Simulates a stream that has read() but lacks getbuffer() and tell().

        Overrides __getattribute__ to raise AttributeError for "tell" and
        "getbuffer" so that hasattr(stream, "tell") and hasattr(stream, "getbuffer")
        evaluate to False at runtime while remaining mypy-compliant.
        """

        def __getattribute__(self, name: str) -> Any:
            if name in ("tell", "getbuffer"):
                raise AttributeError(f"no {name}")
            return super().__getattribute__(name)

    class LocalCustomReadStream(io.BytesIO):
        """Simulates a stream that lacks getbuffer() and where tell() raises OSError.

        Used to verify that _prepare_async_reader gracefully catches OSError
        when attempting to record the starting stream offset via tell().
        """

        def __getattribute__(self, name: str) -> Any:
            if name == "getbuffer":
                raise AttributeError("no getbuffer")
            return super().__getattribute__(name)

        def tell(self) -> int:
            raise OSError("tell failed")

    # 1. bytes stream with explicit size
    reader_fn1, size1, obj1 = session._prepare_async_reader(b"data", size=4)
    assert size1 == 4

    # 2. NoTellStream: read but no tell
    stream2 = LocalNoTellStream(b"")
    reader_fn2, size2, obj2 = session._prepare_async_reader(stream2, size=None)
    assert size2 is None

    # 3. CustomReadStream: read, but no getbuffer and tell raises OSError
    stream3 = LocalCustomReadStream(b"hello")
    reader_fn3, size3, obj3 = session._prepare_async_reader(stream3, size=None)
    assert size3 is None

    # 4. BinaryIO stream with explicit size (covers computed_size is not None branch)
    reader_fn4, size4, obj4 = session._prepare_async_reader(
        io.BytesIO(b"hello"), size=5
    )
    assert size4 == 5


@pytest.mark.asyncio
async def test_async_upload_empty_stream() -> None:
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b"{}",
    )
    async_transport = DummyAsyncSession([start_resp, chunk_resp])
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=async_transport,
    )
    res = await session.upload(stream=b"")
    assert res == b"{}"


@pytest.mark.asyncio
async def test_async_upload_no_stall_config() -> None:
    config = ResumableUploadConfig(stall_minimum_rate=0, stall_timeout=0)

    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    resp = DummyAsyncResponse(
        status=200, headers={"X-Goog-Upload-Status": "final"}, body=b"{}"
    )
    sess_transport = DummyAsyncSession([start_resp, resp])

    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=sess_transport,
    )
    res = await session.upload(stream=b"data")
    assert res == b"{}"


@pytest.mark.asyncio
async def test_async_transmit_chunk_timeout_errors_no_stall() -> None:
    # 1. TimeoutError raises TransferStalledError when remaining is > 0 and no stall control
    future_deadline = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        seconds=60
    )
    config = ResumableUploadConfig(
        deadline=future_deadline, stall_minimum_rate=0, stall_timeout=0
    )

    class TimeoutAsyncSession:
        def __init__(self):
            self.calls = 0

        def request(self, *args, **kwargs):
            self.calls += 1
            if self.calls == 1:

                class StartContext:
                    async def __aenter__(self):
                        class Resp:
                            status = 200
                            headers = {
                                "X-Goog-Upload-Status": "active",
                                "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
                            }

                            async def read(self):
                                return b""

                        return Resp()

                    async def __aexit__(self, exc_type, exc, tb):
                        pass

                return StartContext()
            else:

                class TimeoutContext:
                    async def __aenter__(self):
                        raise asyncio.TimeoutError("timeout")

                    async def __aexit__(self, exc_type, exc, tb):
                        pass

                return TimeoutContext()

    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=TimeoutAsyncSession(),
    )
    session._state._upload_url = "https://upload.example.com/resumable-async"
    no_retry = google.api_core.retry.AsyncStreamingRetry(
        predicate=lambda e: False, timeout=0.001
    )

    with pytest.raises(exceptions.TransferStalledError):
        await session.upload(stream=b"data", retry=no_retry)

    # 2. TimeoutError raises DeadlineExceeded when deadline expires and no stall control
    config2 = ResumableUploadConfig(
        deadline=future_deadline, stall_minimum_rate=0, stall_timeout=0
    )

    session2 = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config2,
        transport=TimeoutAsyncSession(),
    )
    session2._state._upload_url = "https://upload.example.com/resumable-async"

    with mock.patch.object(
        session2,
        "_get_deadline_remaining",
        side_effect=[5.0, 5.0, exceptions.DeadlineExceeded("Deadline exceeded")],
    ):
        with pytest.raises(exceptions.DeadlineExceeded):
            await session2.upload(stream=b"data", retry=no_retry)


@pytest.mark.asyncio
async def test_async_per_attempt_timeout_retries_before_stall_timeout(
    monkeypatch,
) -> None:
    """Verifies that hitting per_attempt_timeout (5s) in async uploads retries via recovery rather
    than prematurely raising TransferStalledError when stall_timeout (120s) has not elapsed."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    query_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "0",
        },
        body=b"",
    )
    final_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"status": "completed"}',
    )

    class RecoverAfterTimeoutSession:
        def __init__(self):
            self.calls = 0

        def request(self, *args, **kwargs):
            self.calls += 1
            if self.calls == 1:
                return start_resp
            if self.calls == 2:

                class TimeoutContext:
                    async def __aenter__(self):
                        raise aiohttp.ServerTimeoutError("Per-attempt 5s timeout")

                    async def __aexit__(self, exc_type, exc, tb):
                        pass

                return TimeoutContext()
            if self.calls == 3:
                return query_resp
            return final_resp

    transport = RecoverAfterTimeoutSession()
    config = ResumableUploadConfig(
        stall_minimum_rate=1024,
        stall_timeout=120.0,
    )
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=transport,
    )

    clock_vals = iter([0.0, 5.0, 5.0, 5.0, 6.0, 6.0])
    monkeypatch.setattr(upload_async, "_monotonic_clock", lambda: next(clock_vals))

    result = await session.upload(
        stream=b"test data",
        retry=google.api_core.retry.AsyncStreamingRetry(initial=0.01, maximum=0.01),
    )
    assert result == b'{"status": "completed"}'
    assert transport.calls == 4


@pytest.mark.asyncio
async def test_async_recover_buffered_chunk_out_of_bounds() -> None:
    session = AsyncResumableUploadSession()
    session._state._upload_url = "https://upload.example.com/resumable-async"
    session._buffered_chunk = memoryview(b"data")
    session._buffered_chunk_offset = 0

    query_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "active", "X-Goog-Upload-Size-Received": "10"},
        body=b"",
    )
    sess_transport = DummyAsyncSession([query_resp])

    unseekable = mock.Mock()
    unseekable.seekable.return_value = False

    with pytest.raises(UnseekableStreamError):
        await session._recover(sess_transport, stream_obj=unseekable)

    assert session._buffered_chunk is None


@pytest.mark.asyncio
async def test_async_recover_stream_obj_none() -> None:
    session = AsyncResumableUploadSession()
    session._state._upload_url = "https://upload.example.com/resumable-async"
    session._buffered_chunk = None

    query_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "active", "X-Goog-Upload-Size-Received": "10"},
        body=b"",
    )
    sess_transport = DummyAsyncSession([query_resp])

    with pytest.raises(UnseekableStreamError, match="precedes active buffer"):
        await session._recover(sess_transport, stream_obj=None)


@pytest.mark.asyncio
async def test_async_upload_already_finished_raises_value_error() -> None:
    session = AsyncResumableUploadSession()
    session._state._upload_url = "https://upload.example.com/resumable-async"

    async def mark_finished(*args, **kwargs):
        session._state._finished = True

    with mock.patch.object(
        session, "_initiate", new_callable=mock.AsyncMock, side_effect=mark_finished
    ):
        sess_transport = DummyAsyncSession([])
        with pytest.raises(
            ValueError, match="Upload completed without receiving a final response"
        ):
            await session.upload(stream=b"data", transport=sess_transport)


@pytest.mark.asyncio
async def test_async_resume_already_finished_raises_value_error() -> None:
    session = AsyncResumableUploadSession()
    session._state._upload_url = "https://upload.example.com/resumable-async"

    async def mark_finished(*args, **kwargs):
        session._state._finished = True

    sess_transport = DummyAsyncSession([])
    with mock.patch.object(
        session, "_recover", new_callable=mock.AsyncMock, side_effect=mark_finished
    ):
        op = session.resume(
            upload_url="https://upload.example.com/resumable-async",
            stream=b"data",
            chunk_size=1024,
            transport=sess_transport,
        )
        with pytest.raises(
            ValueError,
            match="Upload completed without receiving a final response",
        ):
            await op


@pytest.mark.asyncio
async def test_async_partial_chunk_recovery_does_not_prematurely_finalize() -> None:
    """Ensure that retrying a partially committed chunk (len < chunk_size) does not prematurely finalize.

    When a 4-byte chunk (b"0123") partially succeeds (server commits 2 bytes)
    and is retried, ensure that the remaining 2 bytes (b"23") are sent with
    "upload" rather than "upload, finalize" so the remaining payload (b"45")
    is not dropped.
    """
    server_received_bytes = bytearray()

    class StatefulAsyncTransport:
        def __init__(self) -> None:
            self.call_count = 0

        def request(
            self,
            method: str,
            url: str,
            data: Any = None,
            headers: Optional[Mapping[str, str]] = None,
            **kwargs: Any,
        ) -> DummyAsyncResponse:
            self.call_count += 1
            cmd = headers.get("X-Goog-Upload-Command", "") if headers else ""

            # Request 1: start session
            if self.call_count == 1:
                assert cmd == "start"
                return DummyAsyncResponse(
                    status=200,
                    headers={
                        "X-Goog-Upload-Status": "active",
                        "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
                    },
                    body=b"",
                )

            # Request 2: initial Chunk 1 (b"0123") -> server commits partial 2 bytes (b"01"), then fails 503
            if self.call_count == 2:
                assert cmd == "upload"
                assert bytes(data) == b"0123"
                server_received_bytes.extend(b"01")
                return DummyAsyncResponse(
                    status=503,
                    headers={},
                    body=b"Service Unavailable",
                )

            # Request 3: recovery query -> server reports 2 committed bytes
            if self.call_count == 3:
                assert cmd == "query"
                return DummyAsyncResponse(
                    status=200,
                    headers={
                        "X-Goog-Upload-Status": "active",
                        "X-Goog-Upload-Size-Received": str(len(server_received_bytes)),
                    },
                    body=b"",
                )

            # Subsequent upload requests (Request 4: remaining b"23", Request 5: final b"45")
            if data:
                server_received_bytes.extend(bytes(data))

            if "finalize" in cmd:
                return DummyAsyncResponse(
                    status=200,
                    headers={"X-Goog-Upload-Status": "final"},
                    body=b"{}",
                )
            return DummyAsyncResponse(
                status=200,
                headers={"X-Goog-Upload-Status": "active"},
                body=b"",
            )

    transport = StatefulAsyncTransport()
    config = ResumableUploadConfig(
        chunk_size=4,
    )
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=transport,
    )

    await session.upload(
        stream=b"012345",
        retry=google.api_core.retry.AsyncStreamingRetry(
            predicate=lambda exc: True, initial=0.001
        ),
    )

    # Verify no data loss occurred: server must receive all 6 bytes (b"012345"), not truncated b"0123"
    assert bytes(server_received_bytes) == b"012345"


@pytest.mark.asyncio
async def test_async_upload_progress_cancellation() -> None:
    """Verifies that cancelling a task iterating over progress() propagates CancelledError cleanly."""
    slow_event = asyncio.Event()

    class HangingTransport:
        def request(self, *args: Any, **kwargs: Any) -> Any:
            class HangingCtx:
                async def __aenter__(self) -> Any:
                    # Block indefinitely to simulate an in-flight HTTP request.
                    await slow_event.wait()
                    return DummyAsyncResponse(status=200, headers={}, body=b"")

                async def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
                    pass

            return HangingCtx()

    session_cancel = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=HangingTransport(),
    )
    op_cancel = session_cancel.upload(stream=b"data")

    async def consume_progress() -> None:
        async for _ in op_cancel.progress():
            pass

    # Start iterating over progress() in a background task, allow it to reach
    # the blocking request, and then cancel the task.
    progress_task = asyncio.create_task(consume_progress())
    await asyncio.sleep(0.01)
    progress_task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await progress_task


@pytest.mark.asyncio
async def test_async_upload_progress_base_exception() -> None:
    """Verifies that a BaseException raised during progress() is captured and propagated."""

    class CustomBaseException(BaseException):
        pass

    class BaseExceptionTransport:
        def request(self, *args: Any, **kwargs: Any) -> Any:
            class BaseExceptionCtx:
                async def __aenter__(self) -> Any:
                    # Raise a direct BaseException subclass to verify non-Exception
                    # errors mark the operation as consumed and propagate out of progress().
                    raise CustomBaseException("fatal error")

                async def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
                    pass

            return BaseExceptionCtx()

    session_base_exc = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=BaseExceptionTransport(),
    )
    op_base_exc = session_base_exc.upload(stream=b"data")
    with pytest.raises(CustomBaseException, match="fatal error"):
        async for _ in op_base_exc.progress():
            pass
    assert op_base_exc._consumed is True
    assert isinstance(op_base_exc._exception, CustomBaseException)


@pytest.mark.asyncio
async def test_async_upload_progress_repeated_iteration_after_completion() -> None:
    """Verifies that iterating over progress() again after stream completion yields no items."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-async",
        },
        body=b"",
    )
    final_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b"{}",
    )
    session_ok = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=DummyAsyncSession([start_resp, final_resp]),
    )
    op_ok = session_ok.upload(stream=b"data")

    # First pass drains the entire progress stream (STARTED and FINALIZED).
    first_pass = [p async for p in op_ok]
    assert len(first_pass) == 2
    assert op_ok._consumed is True

    # Subsequent iteration over progress() sees _consumed=True and returns immediately.
    second_pass = [p async for p in op_ok.progress()]
    assert second_pass == []


@pytest.mark.asyncio
async def test_async_upload_partial_progress_iteration_then_await() -> None:
    """Verifies that breaking out of progress iteration early allows awaiting the remaining upload."""
    start_partial = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-partial",
        },
        body=b"",
    )
    chunk1_partial = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "active"},
        body=b"",
    )
    chunk2_partial = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b'{"name": "partial_then_await.txt", "size": 8}',
    )
    # Configure a 2-chunk upload (8 bytes total with 4-byte chunk_size), which yields
    # 3 progress notifications in total: STARTED, UPLOADING (after chunk 1), and FINALIZED (after chunk 2).
    session_partial = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=ResumableUploadConfig(chunk_size=4),
        response_type=DummyResponse,
        transport=DummyAsyncSession([start_partial, chunk1_partial, chunk2_partial]),
    )
    op_partial = session_partial.upload(stream=b"01234567")

    # Consume only the first two progress events (STARTED and first UPLOADING) and break early.
    seen_states = []
    async for p in op_partial:
        seen_states.append(p.state)
        if len(seen_states) == 2:
            break

    # The stream has not reached the end yet, so _consumed remains False.
    assert op_partial._consumed is False

    # Awaiting the operation handle resumes draining the remaining chunks from _progress_stream
    # until completion, marks _consumed=True, and returns the deserialized response.
    final_result = await op_partial
    assert op_partial._consumed is True
    assert isinstance(final_result, DummyResponse)
    assert final_result.name == "partial_then_await.txt"
    assert final_result.size == 8


@pytest.mark.asyncio
async def test_async_method_override_arguments() -> None:
    """Verifies content_type and on_progress overrides on initiate, upload, and resume."""
    start_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/123",
        },
        body=b"",
    )
    chunk_resp = DummyAsyncResponse(
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body=b"{}",
    )

    # 1. initiate with content_type override
    session1 = AsyncResumableUploadSession(upload_url="https://api.example.com/start")
    await session1._initiate(
        transport=DummyAsyncSession([start_resp]), content_type="text/plain"
    )
    assert session1._content_type == "text/plain"

    # 2. upload with content_type override
    session2 = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=DummyAsyncSession([start_resp, chunk_resp]),
    )
    await session2.upload(
        stream=b"data",
        content_type="text/csv",
    )
    assert session2._content_type == "text/csv"

    # 3. resume with chunk_size override
    query_resp = DummyAsyncResponse(
        status=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "0",
        },
        body=b"",
    )
    session3 = AsyncResumableUploadSession(
        transport=DummyAsyncSession([query_resp, chunk_resp])
    )
    await session3.resume(
        upload_url="https://upload.example.com/123",
        stream=b"data",
    )


def test_async_retry_predicate_includes_asyncio_timeout_error() -> None:
    """Verifies that asyncio.TimeoutError is treated as retryable by _get_retry_predicate."""
    session = AsyncResumableUploadSession(upload_url="https://api.example.com/start")
    predicate = session._get_retry_predicate()
    assert predicate(asyncio.TimeoutError()) is True


# =====================================================================
# 11. google.auth AsyncAuthorizedSession Transport Tests
# =====================================================================


START_HEADERS = {
    "X-Goog-Upload-Status": "active",
    "X-Goog-Upload-URL": "https://upload.example.com/123",
}


def _auth_response(
    status_code: int = 200,
    headers: Optional[Mapping[str, str]] = None,
    body: bytes = b"",
) -> mock.Mock:
    """Builds a ``google.auth.aio.transport.Response`` double."""
    return mock.Mock(
        status_code=status_code,
        headers=dict(headers or {}),
        read=mock.AsyncMock(return_value=body),
        close=mock.AsyncMock(),
    )


def _authorized_session(
    *outcomes: Union[mock.Mock, BaseException],
) -> Tuple["aio_sessions.AsyncAuthorizedSession", mock.AsyncMock]:
    """Builds a real AsyncAuthorizedSession whose HTTP adapter replays ``outcomes``.

    google-auth invokes the adapter positionally as
    ``(url, method, body, headers, timeout, **kwargs)``.
    """
    auth_request = mock.AsyncMock(side_effect=list(outcomes))
    transport = aio_sessions.AsyncAuthorizedSession(
        aio_credentials.AnonymousCredentials(), auth_request=auth_request
    )
    return transport, auth_request


def _adapter_commands(auth_request: mock.AsyncMock) -> List[str]:
    return [c.args[3]["X-Goog-Upload-Command"] for c in auth_request.call_args_list]


def _supports_total_attempts() -> bool:
    """Returns True if google-auth (>= 2.49.0) accepts ``total_attempts``."""
    params = inspect.signature(aio_sessions.AsyncAuthorizedSession.request).parameters
    return "total_attempts" in params


@pytest.mark.asyncio
async def test_async_authorized_session_upload() -> None:
    """Uploads through a real AsyncAuthorizedSession (the generated REST client transport).

    Unlike aiohttp.ClientSession, its ``request()`` is a coroutine returning a
    ``google.auth.aio.transport.Response`` (``status_code``, explicit ``close()``).
    """
    responses = [
        _auth_response(200, START_HEADERS),
        _auth_response(200, {"X-Goog-Upload-Status": "active"}),
        _auth_response(
            200, {"X-Goog-Upload-Status": "final"}, b'{"name": "auth.txt", "size": 6}'
        ),
    ]
    transport, auth_request = _authorized_session(*responses)
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=ResumableUploadConfig(chunk_size=4),
        transport=transport,
        response_type=DummyResponse,
        start_timeout=7.5,
    )

    with mock.patch.object(transport, "request", wraps=transport.request) as spy:
        result = await session.upload(stream=b"012345")

    assert isinstance(result, DummyResponse)
    assert (result.name, result.size) == ("auth.txt", 6)
    assert session.bytes_uploaded == 6
    assert _adapter_commands(auth_request) == ["start", "upload", "upload, finalize"]
    assert [c.args[2] for c in auth_request.call_args_list] == [b"", b"0123", b"45"]
    assert [c.args[0] for c in auth_request.call_args_list] == [
        "https://api.example.com/start",
        "https://upload.example.com/123",
        "https://upload.example.com/123",
    ]
    for response in responses:
        response.close.assert_awaited_once()
    # api_core owns the timeout: google-auth's wall-clock guard is bounded by the
    # same per-attempt timeout, and nothing extra leaks through to the adapter.
    assert spy.call_args_list[0].kwargs["timeout"] == 7.5
    expected_total_attempts = 1 if _supports_total_attempts() else None
    for call in spy.call_args_list:
        assert call.kwargs["max_allowed_time"] == call.kwargs["timeout"]
        assert call.kwargs.get("total_attempts") == expected_total_attempts
    assert all(c.kwargs == {} for c in auth_request.call_args_list)


@pytest.mark.asyncio
async def test_async_authorized_session_server_error_not_retried_internally() -> None:
    """Verifies a 5xx reaches api_core's retry layer instead of google-auth's.

    AsyncAuthorizedSession retries retryable status codes itself by default;
    api_core passes ``total_attempts=1`` (google-auth >= 2.49.0) so that its
    protocol-aware retry and offset recovery is the single retry layer.
    """
    if not _supports_total_attempts():
        pytest.skip("google-auth < 2.49.0 retries 5xx responses internally")
    response = _auth_response(503, body=b"Service Unavailable")
    transport, auth_request = _authorized_session(response)
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=transport,
        start_retry=google.api_core.retry.AsyncRetry(predicate=lambda exc: False),
    )

    with pytest.raises(exceptions.ServiceUnavailable, match="Service Unavailable"):
        await session.upload(stream=b"data")

    assert auth_request.await_count == 1
    response.close.assert_awaited_once()


@pytest.mark.asyncio
@pytest.mark.parametrize("on_read", [False, True], ids=["request", "read"])
async def test_async_authorized_session_timeout_raises_transfer_stalled(
    on_read: bool,
) -> None:
    """Verifies google.auth.exceptions.TimeoutError feeds stall control.

    It is not a subclass of asyncio.TimeoutError, so it is normalized to one
    (keeping the original as the cause) to surface as TransferStalledError.
    """
    read_resp = _auth_response(200, {"X-Goog-Upload-Status": "final"})
    read_resp.read.side_effect = auth_exceptions.TimeoutError("read timed out")
    chunk_outcome: Any = (
        read_resp if on_read else auth_exceptions.TimeoutError("timed out")
    )
    transport, auth_request = _authorized_session(
        _auth_response(200, START_HEADERS), chunk_outcome
    )
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start", transport=transport
    )
    no_retry = google.api_core.retry.AsyncStreamingRetry(
        predicate=lambda e: False, timeout=0.001
    )

    with pytest.raises(TransferStalledError) as exc_info:
        await session.upload(stream=b"data", retry=no_retry)

    cause = exc_info.value.__cause__
    assert isinstance(cause, asyncio.TimeoutError)
    assert isinstance(cause.__cause__, auth_exceptions.TimeoutError)
    assert _adapter_commands(auth_request) == ["start", "upload, finalize"]
    if on_read:
        read_resp.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_async_authorized_session_transport_error_recovers() -> None:
    """Verifies google.auth.exceptions.TransportError triggers offset recovery."""
    transport, auth_request = _authorized_session(
        _auth_response(200, START_HEADERS),
        auth_exceptions.TransportError("connection reset"),
        _auth_response(
            200, {"X-Goog-Upload-Status": "active", "X-Goog-Upload-Size-Received": "0"}
        ),
        _auth_response(200, {"X-Goog-Upload-Status": "final"}, b'{"name": "f"}'),
    )
    session = AsyncResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=transport,
        response_type=DummyResponse,
    )

    result = await session.upload(
        stream=b"data",
        retry=google.api_core.retry.AsyncStreamingRetry(initial=0.01, maximum=0.01),
    )

    assert isinstance(result, DummyResponse)
    assert result.name == "f"
    assert _adapter_commands(auth_request) == [
        "start",
        "upload, finalize",
        "query",
        "upload, finalize",
    ]


def test_async_retry_predicate_includes_google_auth_errors() -> None:
    """Verifies google-auth transport errors are retryable, unlike its other errors."""
    session = AsyncResumableUploadSession(upload_url="https://api.example.com/start")
    for is_start in (True, False):
        predicate = session._get_retry_predicate(is_start=is_start)
        assert predicate(auth_exceptions.TransportError()) is True
        assert predicate(auth_exceptions.ResponseError()) is True
        assert predicate(auth_exceptions.RefreshError()) is False
