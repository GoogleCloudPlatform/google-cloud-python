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

"""Asynchronous Resumable Upload session and helpers."""

import asyncio
import datetime
import inspect
import io
import logging
import time
from typing import (
    Any,
    AsyncGenerator,
    AsyncIterable,
    AsyncIterator,
    Awaitable,
    BinaryIO,
    Callable,
    Dict,
    Generator,
    Generic,
    Iterable,
    List,
    Mapping,
    Optional,
    Tuple,
    TypeVar,
    Union,
    cast,
)

try:
    import aiohttp

    _HAS_AIOHTTP = True
except ImportError:  # pragma: NO COVER
    _HAS_AIOHTTP = False

try:
    from google.auth import exceptions as auth_exceptions
    from google.auth.aio.transport.sessions import AsyncAuthorizedSession

    _HAS_GOOGLE_AUTH_AIO = True
except ImportError:  # pragma: NO COVER
    _HAS_GOOGLE_AUTH_AIO = False

import google.api_core.retry
from google.api_core import exceptions
from google.api_core.resumable_transfer import common, upload_state
from google.api_core.resumable_transfer.common import (
    DEFAULT_START_TIMEOUT,
    ResumableUploadConfig,
    UploadProgress,
    _format_response_payload,
)

_LOGGER = logging.getLogger(__name__)
_monotonic_clock = time.monotonic


AsyncTransport = Union["aiohttp.ClientSession", "AsyncAuthorizedSession"]
"""Asynchronous HTTP transports accepted by :class:`AsyncResumableUploadSession`.

``google.auth.aio.transport.sessions.AsyncAuthorizedSession`` is the transport
used by generated asynchronous REST clients.
"""

# google-auth >= 2.49.0 accepts ``total_attempts`` to cap AsyncAuthorizedSession's
# own status-code retries; older releases forward unknown kwargs to aiohttp.
_HAS_TOTAL_ATTEMPTS = _HAS_GOOGLE_AUTH_AIO and (
    "total_attempts" in inspect.signature(AsyncAuthorizedSession.request).parameters
)


def _get_buffer_size(stream: object) -> Optional[int]:
    """Returns buffer size in bytes if stream exposes getbuffer(), else None."""
    getbuffer_fn = getattr(stream, "getbuffer", None)
    if callable(getbuffer_fn):
        return int(getbuffer_fn().nbytes)
    return None


ResponseType = TypeVar("ResponseType")


class AsyncUploadOperation(
    Generic[ResponseType],
    Awaitable[ResponseType],
    AsyncIterable[UploadProgress],
):
    """Handle representing an asynchronous upload operation.

    Implements Awaitable[ResponseType] and AsyncIterable[UploadProgress] so
    callers can either await the operation directly or iterate over progress
    snapshots.
    """

    def __init__(
        self,
        progress_stream: AsyncIterator[UploadProgress],
        session: "AsyncResumableUploadSession",
    ) -> None:
        """Initializes the upload operation handle.

        Args:
            progress_stream: Async iterator yielding progress snapshots during the upload.
            session: Underlying asynchronous resumable upload session.
        """
        self._progress_stream = progress_stream
        self._session = session
        self._consumed = False
        self._exception: Optional[BaseException] = None

    async def _consume(self) -> ResponseType:
        """Consumes the upload stream to completion and returns the response."""
        if not self._consumed:
            try:
                async for _ in self._progress_stream:
                    pass
            except BaseException as exc:
                self._exception = exc
                raise
            finally:
                self._consumed = True
        if self._exception is not None:
            raise self._exception
        return self._session.response  # type: ignore[return-value]

    def __await__(self) -> Generator[Any, None, ResponseType]:
        """Awaits completion of the upload and returns the server response."""
        return self._consume().__await__()

    def __aiter__(self) -> AsyncIterator[UploadProgress]:
        """Iterates over progress snapshots yielded during upload execution."""
        return self.progress()

    async def progress(self) -> AsyncIterator[UploadProgress]:
        """Yields UploadProgress snapshots as the transfer progresses.

        Yields:
            UploadProgress snapshots for each progress transition.
        """
        if not self._consumed:
            try:
                async for item in self._progress_stream:
                    yield item
            except BaseException as exc:
                self._exception = exc
                raise
            finally:
                self._consumed = True

    @property
    def response(self) -> Optional[ResponseType]:
        """The deserialized response message (or raw bytes), or None if in progress."""
        return self._session.response

    @property
    def upload_url(self) -> Optional[str]:
        """The session upload URL."""
        return self._session.upload_url

    @property
    def chunk_size(self) -> int:
        """The negotiated chunk size."""
        return self._session.chunk_size

    @property
    def bytes_uploaded(self) -> int:
        """Total confirmed bytes committed so far."""
        return self._session.bytes_uploaded


class AsyncResumableUploadSession:
    """Manages the full lifecycle of an asynchronous resumable upload session."""

    def __init__(
        self,
        upload_url: Optional[str] = None,
        config: Optional[ResumableUploadConfig] = None,
        transport: Optional[AsyncTransport] = None,
        content_type: Optional[str] = None,
        response_type: Optional[Any] = None,
        start_retry: Optional[google.api_core.retry.AsyncRetry] = None,
        start_timeout: float = DEFAULT_START_TIMEOUT,
        request_body: Optional[Union[str, bytes]] = None,
    ) -> None:
        """Initializes an AsyncResumableUploadSession.

        Args:
            upload_url: The initial URL for the start request when starting a
                new upload, or the pre-existing upload session URL when resuming.
            config: Optional upload configuration parameters. Defaults to
                ``ResumableUploadConfig()`` when ``None``.
            transport: Optional :data:`AsyncTransport`. When ``None``, a
                transport must be provided to ``upload()`` or ``resume()``.
            content_type: Optional MIME type of the stream payload. When
                ``None``, no content-type header is sent unless overridden.
            response_type: Optional message class, callable deserializer, or
                ``None``. When ``None``, raw response bytes are returned.
            start_retry: Optional retry configuration (``google.api_core.retry.AsyncRetry``)
                for the initial session creation request. When ``None``, the
                default transient retry policy is used. Use this to customize
                exponential backoff timing (such as ``AsyncRetry(initial=1.0, maximum=60.0)``)
                or to supply a custom ``predicate`` function for API-specific transient
                errors. A custom ``predicate`` replaces the default transient HTTP status
                check (HTTP 408, 429, 500, 502, 503, and 504). Transport errors
                (``aiohttp.ClientError``) are always retried. Terminal errors
                (``DeadlineExceeded``, ``TransferStalledError``,
                ``UploadCancelledError``, and ``UnseekableStreamError``) are never
                retried.
            start_timeout: Timeout in seconds for the start request. Defaults to
                ``60.0`` seconds.
            request_body: Optional default metadata payload sent with the start request.
                Used by ``upload()`` whenever it is called without an explicit
                ``request_body``. When ``None``, an empty payload is sent.
        """
        self._config = config or ResumableUploadConfig()
        self._transport = transport
        self._content_type = content_type
        self._response_type = response_type
        self._start_retry = start_retry
        self._start_timeout = start_timeout
        self._request_body: Union[str, bytes] = (
            request_body if request_body is not None else ""
        )
        self._response: Optional[Any] = None
        self._state = upload_state._ProtocolState(
            upload_url=upload_url,
            chunk_size=self._config.chunk_size,
        )

        # In-memory zero-copy buffer
        self._buffered_chunk: Optional[memoryview] = None
        self._buffered_chunk_offset: int = 0
        self._buffered_chunk_is_last: bool = False
        self._start_stream_offset: int = 0

        # Stall control tracking via monotonic clock
        self._aggregate_lag: float = 0.0
        self._needs_recovery: bool = False

    @property
    def upload_url(self) -> Optional[str]:
        """Optional[str]: The established upload session URL for this session.

        Once an upload is initiated, this is populated with the unique session
        URL returned by the server in the ``x-goog-upload-url`` header (or updated
        to the session URL passed to ``resume()``), and can be saved to resume an
        interrupted upload later.
        """
        return self._state.upload_url

    @property
    def chunk_size(self) -> int:
        """int: The negotiated chunk size."""
        return self._state.chunk_size

    @property
    def response(self) -> Optional[Any]:
        """Optional[Any]: The cached response message if finished."""
        return self._response

    @property
    def bytes_uploaded(self) -> int:
        """int: Confirmed number of bytes committed so far."""
        return self._state.bytes_uploaded

    @property
    def finished(self) -> bool:
        """bool: Whether the upload has completed successfully."""
        return self._state.finished

    def _reset_transfer_state(self) -> None:
        """Resets per-transfer buffer, recovery, and stall control state."""
        self._response = None
        self._buffered_chunk = None
        self._buffered_chunk_offset = 0
        self._buffered_chunk_is_last = False
        self._start_stream_offset = 0
        self._aggregate_lag = 0.0
        self._needs_recovery = False
        self._state._finished = False
        self._state._invalid = False

    def _ensure_aiohttp(self) -> None:
        """Validates that aiohttp is installed and accessible.

        Raises:
            ImportError: If aiohttp is not installed.
        """
        if not _HAS_AIOHTTP:
            raise ImportError(
                "The aiohttp library is required to use AsyncResumableUploadSession. "
                "Please install google-api-core[async_rest]."
            )

    def _get_transport(self, transport: Optional[AsyncTransport]) -> AsyncTransport:
        """Returns the transport to use, raising ValueError when none is set."""
        sess = transport or self._transport
        if sess is None:
            raise ValueError(
                "An aiohttp.ClientSession or AsyncAuthorizedSession transport "
                "must be provided."
            )
        return sess

    async def _send_request(
        self,
        transport: AsyncTransport,
        method: str,
        url: str,
        payload: bytes,
        headers: Mapping[str, str],
        timeout: float,
    ) -> Tuple[int, Mapping[str, str], bytes]:
        """Sends one request over ``transport`` and reads the whole response.

        Args:
            transport: The transport to dispatch the request over.
            method: HTTP method verb.
            url: Request URL.
            payload: Request body bytes.
            headers: Request headers.
            timeout: Total timeout in seconds for this attempt.

        Returns:
            Tuple of (status code, response headers, response body bytes).

        Raises:
            exceptions.GoogleAPICallError: If the status is not 200 or 201.
            asyncio.TimeoutError: If the attempt times out, whichever transport
                is used.
        """
        if _HAS_GOOGLE_AUTH_AIO and isinstance(transport, AsyncAuthorizedSession):
            # google-auth applies its own overall deadline (``max_allowed_time``,
            # 180s by default) on top of the per-request ``timeout``; use the
            # caller's timeout for both. Where supported, a single attempt also
            # disables google-auth's own status-code retries so that this module
            # is the only retry layer.
            retry_kwargs: Dict[str, Any] = (
                {"total_attempts": 1} if _HAS_TOTAL_ATTEMPTS else {}
            )
            try:
                response = await transport.request(
                    method,
                    url,
                    data=payload,
                    headers=headers,
                    timeout=timeout,
                    max_allowed_time=timeout,
                    **retry_kwargs,
                )
                try:
                    status_code = response.status_code
                    resp_headers: Mapping[str, str] = dict(response.headers)
                    body = await response.read()
                finally:
                    await response.close()
            except auth_exceptions.TimeoutError as exc:
                # google-auth raises its own TimeoutError (not an asyncio one, and
                # not reliably chained to one); re-raise it as asyncio.TimeoutError
                # so stall control sees the same type as with aiohttp.ClientSession.
                raise asyncio.TimeoutError(str(exc)) from exc
        else:
            # mypy cannot narrow the negative of the guarded check above.
            session = cast("aiohttp.ClientSession", transport)
            async with session.request(
                method,
                url,
                data=payload,
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=timeout),
            ) as resp:
                status_code = resp.status
                resp_headers = dict(resp.headers)
                body = await resp.read()

        if status_code not in (200, 201):
            raise exceptions.from_http_status(
                status_code, body.decode("utf-8", errors="replace")
            )
        return status_code, resp_headers, body

    def _enrich_exception(self, exc: BaseException) -> None:
        """Attaches session diagnostic metadata to an active exception.

        Args:
            exc: Exception instance to augment with upload_url and chunk_size.
        """
        setattr(exc, "upload_url", self.upload_url)
        setattr(exc, "chunk_size", self.chunk_size)

    def _notify_progress(
        self,
        state: common.ProgressState,
        queue: Optional[List[UploadProgress]] = None,
    ) -> None:
        """Appends current upload status to the optional progress queue.

        Args:
            state: ProgressState transition milestone.
            queue: Optional list to receive progress event.
        """
        if self.upload_url:
            progress = UploadProgress(
                upload_url=self.upload_url,
                chunk_size=self.chunk_size,
                bytes_uploaded=self._state.bytes_uploaded,
                total_bytes=self._state.total_bytes,
                state=state,
            )
            if queue is not None:
                queue.append(progress)

    def _get_deadline_remaining(self) -> Optional[float]:
        """Calculates remaining seconds until the configured upload deadline.

        Returns:
            Remaining seconds before deadline, or None if no deadline configured.

        Raises:
            exceptions.DeadlineExceeded: If deadline has already elapsed.
        """
        if self._config.deadline:
            now = datetime.datetime.now(datetime.timezone.utc)
            dl = self._config.deadline.astimezone(datetime.timezone.utc)
            remaining = (dl - now).total_seconds()
            if remaining <= 0:
                raise exceptions.DeadlineExceeded(
                    f"Resumable upload deadline {self._config.deadline} exceeded."
                )
            return remaining
        return None

    def _get_start_timeout(self, timeout_override: Optional[float] = None) -> float:
        """Computes timeout in seconds for start and control requests.

        Args:
            timeout_override: Explicit timeout override in seconds.

        Returns:
            Applicable timeout in seconds.
        """
        remaining = self._get_deadline_remaining()
        timeout = (
            timeout_override if timeout_override is not None else self._start_timeout
        )
        if remaining is not None:
            return min(timeout, remaining)
        return timeout

    def _get_retry_predicate(
        self,
        is_start: bool = False,
        custom_predicate: Optional[Callable[[Exception], bool]] = None,
    ) -> Callable[[Exception], bool]:
        """Returns a predicate function for determining if an exception is retryable.

        Args:
            is_start: If True, only transient status codes (RETRYABLE_STATUS_CODES)
                are retried. If False (transmitting and finalizing states), state
                consistency errors (RECOVERABLE_STATUS_CODES and
                MissingStatusHeaderError) are also retried via recovery.
            custom_predicate: Optional callable taking an exception and returning True
                if the error should be retried (from a user-supplied AsyncRetry instance).
                Custom predicates replace the default transient HTTP status check
                (``RETRYABLE_STATUS_CODES``: HTTP 408, 429, 500, 502, 503, and 504)
                and are evaluated after protocol-enforced rules:
                1. Terminal errors (``TERMINAL_ERRORS``: ``DeadlineExceeded``,
                   ``TransferStalledError``, ``UploadCancelledError``, and
                   ``UnseekableStreamError``) always return ``False``.
                2. Protocol-recoverable errors during chunk transfer
                   (``RECOVERABLE_STATUS_CODES`` and ``MissingStatusHeaderError``)
                   and transport errors (``aiohttp.ClientError``,
                   ``google.auth.exceptions.TransportError``,
                   ``google.auth.exceptions.ResponseError``, and
                   ``asyncio.TimeoutError``) always return ``True`` so the session
                   can query server state and recover.

        Returns:
            A callable accepting an exception and returning a boolean.
        """

        def should_retry(exc: Exception) -> bool:
            if isinstance(exc, common.TERMINAL_ERRORS):
                return False
            if not is_start and (
                isinstance(exc, exceptions.MissingStatusHeaderError)
                or (
                    isinstance(exc, exceptions.GoogleAPICallError)
                    and exc.code in common.RECOVERABLE_STATUS_CODES
                )
            ):
                return True
            if isinstance(exc, asyncio.TimeoutError) or (
                _HAS_AIOHTTP and isinstance(exc, aiohttp.ClientError)
            ):
                return True
            if _HAS_GOOGLE_AUTH_AIO and isinstance(
                exc, (auth_exceptions.TransportError, auth_exceptions.ResponseError)
            ):
                return True
            if (
                custom_predicate is not None
                and custom_predicate is not google.api_core.retry.if_transient_error
            ):
                return bool(custom_predicate(exc))
            if isinstance(exc, exceptions.GoogleAPICallError):
                return exc.code in common.RETRYABLE_STATUS_CODES
            return False

        return should_retry

    def _get_async_retry(
        self, retry_override: Optional[google.api_core.retry.AsyncRetry] = None
    ) -> google.api_core.retry.AsyncRetry:
        """Resolves unary AsyncRetry policy for start requests.

        Args:
            retry_override: Optional unary AsyncRetry policy override for the start
                request. Terminal errors (``DeadlineExceeded``,
                ``TransferStalledError``, ``UploadCancelledError``, and
                ``UnseekableStreamError``) are never retried.

        Returns:
            Configured or default unary AsyncRetry instance.
        """
        candidate = retry_override or self._start_retry
        if candidate is not None:
            return candidate.with_predicate(
                self._get_retry_predicate(
                    is_start=True, custom_predicate=candidate._predicate
                )
            )
        return google.api_core.retry.AsyncRetry(
            predicate=self._get_retry_predicate(is_start=True)
        )

    def _get_async_streaming_retry(
        self,
        retry_override: Optional[google.api_core.retry.AsyncStreamingRetry] = None,
    ) -> google.api_core.retry.AsyncStreamingRetry:
        """Resolves the AsyncStreamingRetry policy for the chunk upload generator.

        Args:
            retry_override: Optional AsyncStreamingRetry policy override for chunk
                transmission. Protocol recovery is preserved automatically, and
                terminal errors (``DeadlineExceeded``, ``TransferStalledError``,
                ``UploadCancelledError``, and ``UnseekableStreamError``) are never
                retried.

        Returns:
            Configured or default AsyncStreamingRetry instance.
        """
        if retry_override is not None:
            wrapped_pred = self._get_retry_predicate(
                is_start=False, custom_predicate=retry_override._predicate
            )
            return retry_override.with_predicate(wrapped_pred)
        return google.api_core.retry.AsyncStreamingRetry(
            predicate=self._get_retry_predicate(is_start=False),
            timeout=None,
        )

    async def _initiate(
        self,
        transport: AsyncTransport,
        request_body: Union[str, bytes] = "",
        size: Optional[int] = None,
        progress_queue: Optional[List[UploadProgress]] = None,
        content_type: Optional[str] = None,
    ) -> str:
        """Initiates the upload session asynchronously.

        Args:
            transport: The asynchronous transport to dispatch requests over.
            request_body: Initial metadata payload sent with start request.
            size: Total stream size in bytes, if known.
            progress_queue: Optional queue to receive progress event.
            content_type: Optional MIME type override of the payload.

        Returns:
            The negotiated upload session URL.
        """
        self._ensure_aiohttp()
        if content_type is not None:
            self._content_type = content_type

        method, url, headers, payload = self._state.build_start_request(
            body=request_body,
            headers=self._config.start_headers,
            content_type=self._content_type,
            size=size,
        )

        async def do_initiate() -> str:
            status_code, resp_headers, _ = await self._send_request(
                transport,
                method,
                url,
                payload,
                headers,
                timeout=self._get_start_timeout(),
            )
            return self._state.process_start_response(status_code, resp_headers)

        retry_policy = self._get_async_retry()
        retryable_initiate = retry_policy(do_initiate)
        session_url = await retryable_initiate()
        self._notify_progress(common.ProgressState.STARTED, progress_queue)
        return session_url

    async def _transmit_chunk(
        self,
        transport: AsyncTransport,
        reader_fn: Callable[[int], Awaitable[bytes]],
        size: Optional[int],
        progress_queue: Optional[List[UploadProgress]] = None,
        timeout: Optional[float] = None,
    ) -> Tuple[int, Mapping[str, str], bytes]:
        """Transmits the next data chunk asynchronously with stall control.

        Args:
            transport: The asynchronous transport to dispatch requests over.
            reader_fn: Async callable returning chunk bytes.
            size: Total stream size in bytes, if known.
            progress_queue: Optional queue to receive progress updates.
            timeout: Optional per-attempt timeout ceiling in seconds.

        Returns:
            Tuple of (status code, headers mapping, response body bytes).

        Raises:
            TransferStalledError: If chunk transfer throughput stalls.
            DeadlineExceeded: If upload deadline is reached.
            GoogleAPICallError: If chunk upload encounters an error.
        """
        chunk_size = self._state.chunk_size

        # Retain active chunk in zero-copy buffer if not present.
        # Ensure that EOF status (_buffered_chunk_is_last) is computed once
        # when reading from the stream and preserved across _recover() retries.
        # On partial server commit, _recover() slices _buffered_chunk in-place
        # to the uncommitted tail. Preserving _buffered_chunk_is_last ensures
        # that a sliced tail smaller than chunk_size is not prematurely
        # treated as the final chunk when unread bytes remain in the stream.
        if self._buffered_chunk is None:
            raw_bytes = await reader_fn(chunk_size)
            if not raw_bytes:
                raw_bytes = b""
            self._buffered_chunk = memoryview(raw_bytes)
            self._buffered_chunk_offset = self._state.bytes_uploaded
            is_eof = len(raw_bytes) < chunk_size
            if size is not None and self._state.bytes_uploaded + len(raw_bytes) >= size:
                is_eof = True
            self._buffered_chunk_is_last = is_eof

        data = self._buffered_chunk
        data_len = len(data)
        is_last = self._buffered_chunk_is_last

        method, url, headers, payload = self._state.build_chunk_request(
            data=data,
            is_last_chunk=is_last,
            content_type=self._content_type,
        )

        per_attempt_timeout = self._compute_chunk_timeout(
            data_len, timeout_override=timeout
        )
        t_start = _monotonic_clock()
        try:
            status_code, resp_headers, resp_body = await self._send_request(
                transport,
                method,
                url,
                payload,
                headers,
                timeout=per_attempt_timeout,
            )
            t_elapsed = _monotonic_clock() - t_start
        except Exception as exc:
            self._enrich_exception(exc)
            if isinstance(
                exc,
                (
                    asyncio.TimeoutError,
                    aiohttp.ServerTimeoutError,
                ),
            ):
                t_elapsed = _monotonic_clock() - t_start
                self._get_deadline_remaining()
                self._update_stall_control(0, t_elapsed)
            raise

        self._update_stall_control(data_len, t_elapsed)

        self._state.process_chunk_response(status_code, resp_headers, data_len)
        self._buffered_chunk = None
        self._notify_progress(
            common.ProgressState.FINALIZED
            if self._state.finished
            else common.ProgressState.UPLOADING,
            progress_queue,
        )
        return status_code, resp_headers, resp_body

    def _compute_chunk_timeout(
        self, data_len: int, timeout_override: Optional[float] = None
    ) -> float:
        """Computes the dynamic per-attempt chunk timeout based on stall control and deadlines.

        Args:
            data_len: Length of the current chunk in bytes.
            timeout_override: Optional per-attempt timeout ceiling in seconds.

        Returns:
            Timeout in seconds for chunk transmission attempt.
        """
        rate = self._config.stall_minimum_rate
        expected_sec = data_len / rate if rate > 0 else 60.0

        # Remaining time budget for this chunk across all retries before stalling.
        # If prior chunks accumulated high aggregate_lag (or if expected_sec is tiny
        # when stall_timeout is 0), expected_sec - _aggregate_lag + stall_timeout can
        # drop to <= 0. Enforce a 1.0s minimum so the HTTP transport always receives
        # a valid positive timeout instead of failing immediately with <= 0s.
        min_chunk_timeout = 1.0
        next_chunk_timeout = max(
            min_chunk_timeout,
            expected_sec - self._aggregate_lag + self._config.stall_timeout,
        )

        if timeout_override is not None:
            if rate > 0 and self._config.stall_timeout > 0:
                per_attempt_timeout = min(timeout_override, next_chunk_timeout)
            else:
                per_attempt_timeout = timeout_override
        else:
            # Give a single attempt up to 2x expected_sec (bounded by next_chunk_timeout)
            # so a hung socket fails fast enough to recover and retry before stalling.
            # For a tiny final chunk (e.g. a few hundred bytes), 2x expected_sec is only
            # a few milliseconds—shorter than an HTTP round-trip—so enforce a 5s minimum
            # per-attempt timeout (e.g. 0.01s -> 5.0s, while 256.0s stays 256.0s).
            min_attempt_timeout = 5.0
            per_attempt_timeout = max(
                min_attempt_timeout,
                min(next_chunk_timeout, 2.0 * expected_sec),
            )

        remaining = self._get_deadline_remaining()
        if remaining is not None:
            per_attempt_timeout = min(per_attempt_timeout, remaining)

        return per_attempt_timeout

    def _update_stall_control(self, data_len: int, t_elapsed: float) -> None:
        """Updates aggregate transfer rate lag and enforces stall timeout and deadlines.

        Args:
            data_len: Length of the transmitted chunk in bytes.
            t_elapsed: Elapsed duration in seconds for chunk transmission.

        Raises:
            exceptions.DeadlineExceeded: If upload deadline is exceeded.
            exceptions.TransferStalledError: If transfer throughput stalls past configured timeout.
        """
        if not (self._config.stall_minimum_rate and self._config.stall_timeout):
            return

        rate = self._config.stall_minimum_rate
        expected_sec = data_len / rate if rate > 0 else 0.0
        current_lag = t_elapsed - expected_sec
        self._aggregate_lag = max(0.0, self._aggregate_lag + current_lag)
        if self._aggregate_lag >= self._config.stall_timeout:
            self._get_deadline_remaining()
            raise exceptions.TransferStalledError(
                f"Upload stalled: transfer rate remained below {rate} bytes/s for longer than {self._config.stall_timeout}s.",
                upload_url=self.upload_url,
                chunk_size=self.chunk_size,
            )

    async def _recover(
        self,
        transport: AsyncTransport,
        stream_obj: Optional[object] = None,
        progress_queue: Optional[List[UploadProgress]] = None,
    ) -> Tuple[int, Mapping[str, str], bytes]:
        """Queries server for committed byte offset and adjusts buffer.

        Args:
            transport: The asynchronous transport to dispatch requests over.
            stream_obj: Underlying stream object to rewind if seekable.
            progress_queue: Optional queue to receive progress updates.

        Returns:
            Tuple of (status code, headers mapping, response body bytes).

        Raises:
            exceptions.UnseekableStreamError: If server offset precedes buffer and stream cannot be rewound.
            exceptions.GoogleAPICallError: If query request fails on the server.
        """
        method, url, headers, payload = self._state.build_query_request()
        status_code, resp_headers, body = await self._send_request(
            transport,
            method,
            url,
            payload,
            headers,
            timeout=self._get_start_timeout(),
        )

        received = self._state.process_query_response(status_code, resp_headers)
        self._notify_progress(common.ProgressState.OFFSET_RECEIVED, progress_queue)

        if self._buffered_chunk is not None:
            chunk_start = self._buffered_chunk_offset
            chunk_end = chunk_start + len(self._buffered_chunk)
            if chunk_start <= received <= chunk_end:
                discard_len = received - chunk_start
                self._buffered_chunk = self._buffered_chunk[discard_len:]
                self._buffered_chunk_offset = received
                # When the server confirms receipt of the entire buffered chunk
                # (received == chunk_end), slicing leaves a 0-length memoryview.
                # Reset _buffered_chunk to None so the next upload attempt reads
                # the next chunk from the stream instead of sending an empty buffer.
                if len(self._buffered_chunk) == 0:
                    self._buffered_chunk = None
                return status_code, resp_headers, body

        self._buffered_chunk = None
        seek_fn = getattr(stream_obj, "seek", None)
        if callable(seek_fn):
            seekable_fn = getattr(stream_obj, "seekable", None)
            if callable(seekable_fn) and not seekable_fn():
                raise exceptions.UnseekableStreamError(
                    f"Stream is not seekable. Cannot recover upload to offset {received}.",
                    upload_url=self.upload_url,
                    chunk_size=self.chunk_size,
                )
            try:
                seek_fn(self._start_stream_offset + received)
                return status_code, resp_headers, body
            except (OSError, AttributeError) as exc:
                raise exceptions.UnseekableStreamError(
                    f"Failed to seek stream to offset {received}: {exc}",
                    upload_url=self.upload_url,
                    chunk_size=self.chunk_size,
                ) from exc

        raise exceptions.UnseekableStreamError(
            f"Server offset {received} precedes active buffer. Stream cannot be rewound.",
            upload_url=self.upload_url,
            chunk_size=self.chunk_size,
        )

    async def cancel(self, transport: Optional[AsyncTransport] = None) -> None:
        """Cancels the resumable upload session asynchronously.

        Args:
            transport: Optional aiohttp.ClientSession or AsyncAuthorizedSession.

        Raises:
            ValueError: If transport is missing.
            exceptions.GoogleAPICallError: If cancellation request fails on the server.
        """
        self._ensure_aiohttp()
        sess = self._get_transport(transport)
        method, url, headers, payload = self._state.build_cancel_request()
        status_code, resp_headers, _ = await self._send_request(
            sess,
            method,
            url,
            payload,
            headers,
            timeout=self._get_start_timeout(),
        )
        self._state.process_cancel_response(status_code, resp_headers)

    async def _transmit_all_chunks(
        self,
        transport: AsyncTransport,
        reader_fn: Callable[[int], Awaitable[bytes]],
        computed_size: Optional[int],
        progress_queue: Optional[List[UploadProgress]] = None,
        stream_obj: Optional[object] = None,
        retry: Optional[google.api_core.retry.AsyncStreamingRetry] = None,
        timeout: Optional[float] = None,
    ) -> AsyncGenerator[UploadProgress, None]:
        """Transmits chunks until completion using a single outer AsyncStreamingRetry coordinator.

        Args:
            transport: The asynchronous transport to dispatch requests over.
            reader_fn: Async callable returning chunk bytes.
            computed_size: Total stream size in bytes, if known.
            progress_queue: Optional list receiving UploadProgress snapshots.
            stream_obj: Underlying stream object for recovery seeking.
            retry: Optional retry policy override for chunk transmission. Protocol
                recovery is preserved automatically, and terminal errors
                (``DeadlineExceeded``, ``TransferStalledError``,
                ``UploadCancelledError``, and ``UnseekableStreamError``) are never
                retried.
            timeout: Optional per-attempt timeout ceiling in seconds.

        Yields:
            UploadProgress snapshots for each chunk transmission milestone.
        """
        final_resp_tuple: Optional[Tuple[int, Mapping[str, str], bytes]] = None
        retry_policy = self._get_async_streaming_retry(retry_override=retry)

        async def attempt_stream() -> AsyncGenerator[UploadProgress, None]:
            nonlocal final_resp_tuple
            if self._needs_recovery:
                _LOGGER.info(
                    "Recoverable error during async chunk upload. Querying server offset."
                )
                self._notify_progress(common.ProgressState.RECOVERING, progress_queue)
                recover_tuple = await self._recover(
                    transport, stream_obj, progress_queue=progress_queue
                )
                if self._state.finished:
                    final_resp_tuple = recover_tuple
                self._needs_recovery = False
                while progress_queue:
                    yield progress_queue.pop(0)

            while not self._state.finished and not self._state.invalid:
                try:
                    final_resp_tuple = await self._transmit_chunk(
                        transport,
                        reader_fn,
                        computed_size,
                        progress_queue,
                        timeout=timeout,
                    )
                except Exception as exc:
                    if retry_policy._predicate(exc):
                        self._needs_recovery = True
                    raise
                while progress_queue:
                    yield progress_queue.pop(0)

        try:
            retryable_stream = retry_policy(attempt_stream)
            stream_gen = await retryable_stream()
            async for item in stream_gen:
                yield item
        except (
            asyncio.TimeoutError,
            aiohttp.ServerTimeoutError,
            exceptions.RetryError,
        ) as exc:
            timeout_exc = (
                exc.__cause__ if isinstance(exc, exceptions.RetryError) else exc
            )
            if not isinstance(
                timeout_exc, (asyncio.TimeoutError, aiohttp.ServerTimeoutError)
            ):
                raise
            self._enrich_exception(timeout_exc)
            self._get_deadline_remaining()
            raise exceptions.TransferStalledError(
                f"Upload stalled: chunk transfer timed out ({timeout_exc}).",
                upload_url=self.upload_url,
                chunk_size=self.chunk_size,
            ) from timeout_exc

        if final_resp_tuple is None:
            raise ValueError("Upload completed without receiving a final response.")

        _, _, body_bytes = final_resp_tuple
        self._response = _format_response_payload(body_bytes, self._response_type)

    def upload(
        self,
        stream: Union[AsyncIterable[bytes], BinaryIO, bytes, Iterable[bytes]],
        request_body: Optional[Union[str, bytes]] = None,
        size: Optional[int] = None,
        transport: Optional[AsyncTransport] = None,
        content_type: Optional[str] = None,
        retry: Optional[google.api_core.retry.AsyncStreamingRetry] = None,
        timeout: Optional[float] = None,
    ) -> AsyncUploadOperation:
        """Initiates and executes upload asynchronously, returning an AsyncUploadOperation.

        Args:
            stream: Data payload to upload (async iterable, binary stream, bytes, or iterable).
            request_body: Initial metadata payload sent with the start request.
                When ``None``, the ``request_body`` supplied to the session constructor
                (if any) is used.
            size: Total stream size in bytes, if known.
            transport: Optional aiohttp.ClientSession or AsyncAuthorizedSession.
            content_type: Optional MIME type of the stream payload.
            retry: Optional retry configuration (``AsyncStreamingRetry``) for
                chunk upload requests. Use this to customize exponential backoff timing between chunk retries or to
                supply a custom ``predicate`` for API-specific transient errors.
                A custom ``predicate`` replaces the default transient HTTP status
                check (HTTP 408, 429, 500, 502, 503, and 504). Transport errors and
                protocol recovery errors (HTTP 400, 412, 416, and
                ``MissingStatusHeaderError``) always initiate server offset
                recovery. Terminal errors (``DeadlineExceeded``,
                ``TransferStalledError``, ``UploadCancelledError``, and
                ``UnseekableStreamError``) are never retried.
            timeout: Optional per-attempt timeout ceiling in seconds.

        Returns:
            An AsyncUploadOperation handle representing the transfer.

        Raises:
            ValueError: If transport is missing.
        """
        self._ensure_aiohttp()
        sess = self._get_transport(transport)

        if content_type is not None:
            self._content_type = content_type
        if request_body is None:
            request_body = self._request_body

        self._reset_transfer_state()
        progress_queue: List[UploadProgress] = []
        reader_fn, computed_size, stream_obj = self._prepare_async_reader(stream, size)

        async def _run() -> AsyncGenerator[UploadProgress, None]:
            try:
                await self._initiate(
                    transport=sess,
                    request_body=request_body,
                    size=computed_size,
                    progress_queue=progress_queue,
                )
                while progress_queue:
                    yield progress_queue.pop(0)

                async for item in self._transmit_all_chunks(
                    sess,
                    reader_fn,
                    computed_size,
                    progress_queue=progress_queue,
                    stream_obj=stream_obj,
                    retry=retry,
                    timeout=timeout,
                ):
                    yield item
            except BaseException as exc:
                self._enrich_exception(exc)
                raise

        return AsyncUploadOperation(progress_stream=_run(), session=self)

    def resume(
        self,
        upload_url: str,
        stream: Union[AsyncIterable[bytes], BinaryIO, bytes, Iterable[bytes]],
        size: Optional[int] = None,
        chunk_size: Optional[int] = None,
        transport: Optional[AsyncTransport] = None,
        retry: Optional[google.api_core.retry.AsyncStreamingRetry] = None,
        timeout: Optional[float] = None,
    ) -> AsyncUploadOperation:
        """Resumes an existing upload asynchronously, returning an AsyncUploadOperation.

        Args:
            upload_url (str): Established upload session URL.
            stream (Union[AsyncIterable[bytes], BinaryIO, bytes, Iterable[bytes]]):
                Data payload to resume uploading.
            size (Optional[int]): Total stream size in bytes, if known.
            chunk_size (Optional[int]): Optional chunk size override in bytes.
            transport (Optional[AsyncTransport]): Optional transport override.
            retry (Optional[google.api_core.retry.AsyncStreamingRetry]): Optional
                retry configuration (``AsyncStreamingRetry``) for chunk upload
                requests. Use this to customize exponential backoff timing
                between chunk retries or to supply a custom ``predicate`` for
                API-specific transient errors. A custom ``predicate`` replaces
                the default transient HTTP status check (HTTP 408, 429, 500,
                502, 503, and 504). Transport errors and protocol recovery
                errors (HTTP 400, 412, 416, and ``MissingStatusHeaderError``)
                always initiate server offset recovery. Terminal errors
                (``DeadlineExceeded``, ``TransferStalledError``,
                ``UploadCancelledError``, and ``UnseekableStreamError``) are
                never retried.
            timeout (Optional[float]): Optional per-attempt timeout ceiling in
                seconds.

        Returns:
            An AsyncUploadOperation handle representing the resumed transfer.

        Raises:
            ValueError: If transport, upload_url, or stream is missing.
        """
        self._ensure_aiohttp()
        sess = self._get_transport(transport)
        actual_url = upload_url or self.upload_url
        if not actual_url:
            raise ValueError("An upload URL must be provided to resume.")
        if stream is None:
            raise ValueError("A data stream or payload must be provided to resume.")

        self._reset_transfer_state()
        if chunk_size is not None:
            self._state._chunk_size = chunk_size

        self._state._upload_url = actual_url
        progress_queue: List[UploadProgress] = []
        reader_fn, computed_size, stream_obj = self._prepare_async_reader(stream, size)

        async def _run() -> AsyncGenerator[UploadProgress, None]:
            try:
                await self._recover(sess, stream_obj, progress_queue=progress_queue)
                while progress_queue:
                    yield progress_queue.pop(0)

                async for item in self._transmit_all_chunks(
                    sess,
                    reader_fn,
                    computed_size,
                    progress_queue=progress_queue,
                    stream_obj=stream_obj,
                    retry=retry,
                    timeout=timeout,
                ):
                    yield item
            except BaseException as exc:
                self._enrich_exception(exc)
                raise

        return AsyncUploadOperation(progress_stream=_run(), session=self)

    def _prepare_async_reader(
        self,
        stream: Union[AsyncIterable[bytes], BinaryIO, bytes, Iterable[bytes]],
        size: Optional[int],
    ) -> Tuple[
        Callable[[int], Awaitable[bytes]],
        Optional[int],
        Optional[object],
    ]:
        """Creates an asynchronous byte reader and determines stream length.

        Args:
            stream: Input payload (async iterable, binary stream, bytes, or iterable).
            size: Explicit total size in bytes, if known.

        Returns:
            Tuple of (async reader function, computed total size, underlying stream object).

        Raises:
            TypeError: If the stream type is not supported.
        """
        computed_size = size

        if isinstance(stream, (str, dict)):
            raise TypeError(f"Unsupported stream type: {type(stream)}")

        if isinstance(stream, bytes):
            bytes_io = io.BytesIO(stream)
            if computed_size is None:
                computed_size = len(stream)

            async def reader(n: int) -> bytes:
                return bytes_io.read(n)

            return reader, computed_size, bytes_io

        read_fn = getattr(stream, "read", None)
        if callable(read_fn):
            if inspect.iscoroutinefunction(read_fn):
                # Native async reader (e.g. asyncio.StreamReader)
                async def reader(n: int) -> bytes:
                    return await read_fn(n)

                return reader, computed_size, stream

            # Synchronous binary stream (e.g. io.BytesIO or open file handle):
            # offload blocking reads to worker thread via asyncio.to_thread.
            if computed_size is None:
                computed_size = _get_buffer_size(stream)

            tell_fn = getattr(stream, "tell", None)
            if callable(tell_fn):
                try:
                    self._start_stream_offset = tell_fn()
                except (OSError, AttributeError):
                    self._start_stream_offset = 0

            async def reader(n: int) -> bytes:
                return await asyncio.to_thread(read_fn, n)

            return reader, computed_size, stream

        if hasattr(stream, "__aiter__"):
            # Native AsyncIterable[bytes]
            iterator = stream.__aiter__()
            buffer = bytearray()

            async def reader(n: int) -> bytes:
                while len(buffer) < n:
                    try:
                        chunk = await iterator.__anext__()
                        buffer.extend(chunk)
                    except StopAsyncIteration:
                        break
                result = bytes(buffer[:n])
                del buffer[:n]
                return result

            return reader, computed_size, None

        if isinstance(stream, Iterable):
            # Synchronous Iterable[bytes]: offload to worker thread
            iterator = iter(stream)
            buffer = bytearray()

            def _next_chunk():
                try:
                    return next(iterator)
                except StopIteration:
                    return None

            async def reader(n: int) -> bytes:
                while len(buffer) < n:
                    chunk = await asyncio.to_thread(_next_chunk)
                    if chunk is None:
                        break
                    buffer.extend(chunk)
                result = bytes(buffer[:n])
                del buffer[:n]
                return result

            return reader, computed_size, None

        raise TypeError(f"Unsupported stream type: {type(stream)}")
