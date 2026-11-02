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

"""Synchronous Resumable Upload session and helpers using requests."""

import datetime
import io
import logging
import time
from typing import (
    Any,
    BinaryIO,
    Callable,
    Generator,
    Iterable,
    List,
    Optional,
    Tuple,
    Union,
)

import requests

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


def _get_buffer_size(stream: object) -> Optional[int]:
    """Returns buffer size in bytes if stream exposes getbuffer(), else None."""
    getbuffer_fn = getattr(stream, "getbuffer", None)
    if callable(getbuffer_fn):
        return int(getbuffer_fn().nbytes)
    return None


class _IterableReader(io.BytesIO):
    """Wraps an Iterable[bytes] as a non-seekable binary stream.

    Ensure that chunks are pulled lazily from the underlying iterator
    on each read() call rather than buffering the entire iterable into memory.
    Inherits from io.BytesIO so static type checkers recognize instances as
    BinaryIO natively.
    """

    def __init__(self, iterable: Iterable[bytes]) -> None:
        super().__init__()
        self._iterator = iter(iterable)
        self._buffer = bytearray()

    def seekable(self) -> bool:
        return False

    def tell(self) -> int:
        raise OSError("Stream is not seekable")

    def read(self, size: Optional[int] = -1) -> bytes:
        if size is None or size < 0:
            for chunk in self._iterator:
                self._buffer.extend(chunk)
            result = bytes(self._buffer)
            self._buffer.clear()
            return result

        while len(self._buffer) < size:
            try:
                chunk = next(self._iterator)
                self._buffer.extend(chunk)
            except StopIteration:
                break
        result = bytes(self._buffer[:size])
        del self._buffer[:size]
        return result


class ResumableUploadSession:
    """Manages the full lifecycle of a resumable upload session."""

    def __init__(
        self,
        upload_url: Optional[str] = None,
        config: Optional[ResumableUploadConfig] = None,
        transport: Optional[requests.Session] = None,
        content_type: Optional[str] = None,
        response_type: Optional[Any] = None,
        start_retry: Optional[google.api_core.retry.Retry] = None,
        start_timeout: float = DEFAULT_START_TIMEOUT,
        request_body: Optional[Union[str, bytes]] = None,
    ) -> None:
        """Initializes a ResumableUploadSession.

        Args:
            upload_url: The initial URL for the start request when starting a
                new upload, or the pre-existing upload session URL when resuming.
            config: Optional upload configuration parameters. Defaults to
                ``ResumableUploadConfig()`` when ``None``.
            transport: Optional requests session. When ``None``, a transport
                must be provided to ``upload()`` or ``resume()``.
            content_type: Optional MIME type of the stream payload. When
                ``None``, no content-type header is sent unless overridden.
            response_type: Optional message class, callable deserializer, or
                ``None``. When ``None``, raw response bytes are returned.
            start_retry: Optional retry configuration (``google.api_core.retry.Retry``)
                for the initial session creation request. When ``None``, the
                default transient retry policy is used. Use this to customize
                exponential backoff timing (such as ``Retry(initial=1.0, maximum=60.0)``)
                or to supply a custom ``predicate`` function for API-specific transient
                errors. A custom ``predicate`` replaces the default transient HTTP status
                check (HTTP 408, 429, 500, 502, 503, and 504). Transport errors
                (``ConnectionError``, ``ChunkedEncodingError``, and ``Timeout``) are
                always retried. Terminal errors (``DeadlineExceeded``,
                ``TransferStalledError``, ``UploadCancelledError``, and
                ``UnseekableStreamError``) are never retried.
            start_timeout: Timeout in seconds for the start request. Defaults to
                ``60.0`` seconds.
            request_body: Optional default metadata payload sent with the start request.
                Used by ``upload()`` and ``iter_upload()`` whenever they are called
                without an explicit ``request_body``. When ``None``, an empty payload is sent.
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

        # In-memory zero-copy buffer (never discard chunk until confirmed)
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

    def _get_transport(self, transport: Optional[requests.Session]) -> requests.Session:
        """Resolves the requests.Session transport.

        Args:
            transport: Explicit requests session if provided.

        Returns:
            The resolved requests session.

        Raises:
            ValueError: If no requests session is available.
        """
        sess = transport or self._transport
        if sess is None:
            raise ValueError("A requests.Session transport must be provided.")
        return sess

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
        progress_queue: Optional[List[UploadProgress]] = None,
    ) -> None:
        """Appends current upload status to the optional progress queue.

        Args:
            state: ProgressState transition milestone.
            progress_queue: Optional list buffering UploadProgress snapshots for generator consumers.
        """
        if self.upload_url:
            progress = UploadProgress(
                upload_url=self.upload_url,
                chunk_size=self.chunk_size,
                bytes_uploaded=self._state.bytes_uploaded,
                total_bytes=self._state.total_bytes,
                state=state,
            )
            if progress_queue is not None:
                progress_queue.append(progress)

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
                if the error should be retried (from a user-supplied Retry instance).
                Custom predicates replace the default transient HTTP status check
                (``RETRYABLE_STATUS_CODES``: HTTP 408, 429, 500, 502, 503, and 504)
                and are evaluated after protocol-enforced rules:
                1. Terminal errors (``TERMINAL_ERRORS``: ``DeadlineExceeded``,
                   ``TransferStalledError``, ``UploadCancelledError``, and
                   ``UnseekableStreamError``) always return ``False``.
                2. Protocol-recoverable errors during chunk transfer
                   (``RECOVERABLE_STATUS_CODES`` and ``MissingStatusHeaderError``)
                   and transport errors (``ConnectionError``,
                   ``ChunkedEncodingError``, ``Timeout``) always return ``True`` so
                   the session can query server state and recover.

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
            if isinstance(exc, requests.exceptions.RequestException):
                if isinstance(
                    exc,
                    (
                        requests.exceptions.ConnectionError,
                        requests.exceptions.ChunkedEncodingError,
                        requests.exceptions.Timeout,
                    ),
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

    def _get_retry(
        self, retry_override: Optional[google.api_core.retry.Retry] = None
    ) -> google.api_core.retry.Retry:
        """Resolves unary Retry policy for start requests.

        Args:
            retry_override: Optional unary Retry policy override for the start
                request. Terminal errors (``DeadlineExceeded``,
                ``TransferStalledError``, ``UploadCancelledError``, and
                ``UnseekableStreamError``) are never retried.

        Returns:
            Configured or default unary Retry instance.
        """
        candidate = retry_override or self._start_retry
        if candidate is not None:
            return candidate.with_predicate(
                self._get_retry_predicate(
                    is_start=True, custom_predicate=candidate._predicate
                )
            )
        return google.api_core.retry.Retry(
            predicate=self._get_retry_predicate(is_start=True)
        )

    def _get_streaming_retry(
        self,
        retry_override: Optional[google.api_core.retry.StreamingRetry] = None,
    ) -> google.api_core.retry.StreamingRetry:
        """Resolves the StreamingRetry policy for the chunk upload generator.

        Args:
            retry_override: Optional StreamingRetry policy override for chunk
                transmission. Protocol recovery is preserved automatically, and
                terminal errors (``DeadlineExceeded``, ``TransferStalledError``,
                ``UploadCancelledError``, and ``UnseekableStreamError``) are never
                retried.

        Returns:
            Configured or default StreamingRetry instance.
        """
        if retry_override is not None:
            wrapped_pred = self._get_retry_predicate(
                is_start=False, custom_predicate=retry_override._predicate
            )
            return retry_override.with_predicate(wrapped_pred)
        return google.api_core.retry.StreamingRetry(
            predicate=self._get_retry_predicate(is_start=False),
            timeout=None,
        )

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
                f"Upload stalled: transfer rate remained below {rate} bytes/s "
                f"for longer than {self._config.stall_timeout}s.",
                upload_url=self.upload_url,
                chunk_size=self.chunk_size,
            )

    def _reposition_stream_offset(
        self, stream: Union[BinaryIO, Iterable[bytes]], received: int
    ) -> int:
        """Adjusts in-memory chunk buffer or seeks input stream to server offset.

        Args:
            stream: The input data stream.
            received: Confirmed byte offset committed on the server.

        Returns:
            The confirmed server byte offset.

        Raises:
            exceptions.UnseekableStreamError: If server offset precedes buffer and stream cannot be rewound.
        """
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
                return received

        self._buffered_chunk = None
        seekable_fn = getattr(stream, "seekable", None)
        if callable(seekable_fn) and not seekable_fn():
            raise exceptions.UnseekableStreamError(
                f"Stream is not seekable. Cannot recover upload to offset {received}.",
                upload_url=self.upload_url,
                chunk_size=self.chunk_size,
            )
        try:
            seek_fn = getattr(stream, "seek")
            seek_fn(self._start_stream_offset + received)
        except (OSError, AttributeError) as exc:
            raise exceptions.UnseekableStreamError(
                f"Failed to seek stream to offset {received}: {exc}",
                upload_url=self.upload_url,
                chunk_size=self.chunk_size,
            ) from exc

        return received

    def _initiate(
        self,
        transport: requests.Session,
        request_body: Union[str, bytes] = "",
        size: Optional[int] = None,
        progress_queue: Optional[List[UploadProgress]] = None,
        content_type: Optional[str] = None,
    ) -> str:
        """Initiates the upload session by sending the start command.

        Args:
            transport: The requests session.
            request_body: JSON payload for initial start request.
            size: Total size of payload in bytes, if known.
            progress_queue: Optional list buffering UploadProgress snapshots.
            content_type: Optional MIME type override of the payload.

        Returns:
            The upload session URL.
        """
        if content_type is not None:
            self._content_type = content_type

        method, url, headers, payload = self._state.build_start_request(
            body=request_body,
            headers=self._config.start_headers,
            content_type=self._content_type,
            size=size,
        )

        def do_initiate() -> str:
            req_timeout = self._get_start_timeout()
            response = transport.request(
                method, url, data=payload, headers=headers, timeout=req_timeout
            )
            if not response.ok:
                raise exceptions.from_http_response(response)
            session_url = self._state.process_start_response(
                response.status_code, response.headers
            )
            return session_url

        retry_policy = self._get_retry()
        retryable_initiate = retry_policy(do_initiate)
        session_url = retryable_initiate()
        self._notify_progress(
            common.ProgressState.STARTED, progress_queue=progress_queue
        )
        return session_url

    def _transmit_chunk(
        self,
        transport: requests.Session,
        stream: Union[BinaryIO, Iterable[bytes]],
        size: Optional[int],
        progress_queue: Optional[List[UploadProgress]] = None,
        timeout: Optional[float] = None,
    ) -> requests.Response:
        """Transmits a single data chunk attempt with stall control.

        Args:
            transport: The requests session.
            stream: The input data stream.
            size: Total size of the stream in bytes, if known.
            progress_queue: Optional list buffering UploadProgress snapshots.
            timeout: Optional per-attempt timeout ceiling in seconds.

        Returns:
            The HTTP response for the transmitted chunk.
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
            read_fn = getattr(stream, "read")
            raw_bytes = read_fn(chunk_size)
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
        try:
            t_start = _monotonic_clock()
            resp = transport.request(
                method,
                url,
                data=payload,
                headers=headers,
                timeout=per_attempt_timeout,
            )
            t_elapsed = _monotonic_clock() - t_start
            if not resp.ok:
                raise exceptions.from_http_response(resp)
        except requests.exceptions.Timeout as exc:
            t_elapsed = _monotonic_clock() - t_start
            self._enrich_exception(exc)
            self._get_deadline_remaining()
            self._update_stall_control(0, t_elapsed)
            raise
        except Exception as exc:
            self._enrich_exception(exc)
            raise

        self._update_stall_control(data_len, t_elapsed)
        self._state.process_chunk_response(resp.status_code, resp.headers, data_len)
        self._buffered_chunk = None
        self._notify_progress(
            common.ProgressState.FINALIZED
            if self._state.finished
            else common.ProgressState.UPLOADING,
            progress_queue=progress_queue,
        )
        return resp

    def _recover(
        self,
        transport: requests.Session,
        stream: Union[BinaryIO, Iterable[bytes]],
        progress_queue: Optional[List[UploadProgress]] = None,
    ) -> requests.Response:
        """Queries server for committed byte offset and adjusts buffer / stream.

        Args:
            transport: The requests session.
            stream: The input data stream.
            progress_queue: Optional list buffering UploadProgress snapshots.

        Returns:
            The HTTP response for the status query.

        Raises:
            exceptions.UnseekableStreamError: If server offset precedes buffer and stream cannot be rewound.
            exceptions.GoogleAPICallError: If query request fails on the server.
        """
        method, url, headers, payload = self._state.build_query_request()
        timeout = self._get_start_timeout()
        resp = transport.request(
            method, url, data=payload, headers=headers, timeout=timeout
        )
        if not resp.ok:
            raise exceptions.from_http_response(resp)
        received = self._state.process_query_response(resp.status_code, resp.headers)
        self._notify_progress(
            common.ProgressState.OFFSET_RECEIVED, progress_queue=progress_queue
        )
        self._reposition_stream_offset(stream, received)
        return resp

    def cancel(self, transport: Optional[requests.Session] = None) -> None:
        """Cancels the resumable upload session.

        Args:
            transport: Optional requests session to use for dispatching cancellation.

        Raises:
            ValueError: If no requests session is available.
            GoogleAPICallError: If the cancellation request fails on the server.
        """
        sess = self._get_transport(transport)
        method, url, headers, payload = self._state.build_cancel_request()
        timeout = self._get_start_timeout()
        resp = sess.request(method, url, data=payload, headers=headers, timeout=timeout)
        if not resp.ok:
            raise exceptions.from_http_response(resp)
        self._state.process_cancel_response(resp.status_code, resp.headers)

    def _transmit_all_chunks(
        self,
        transport: requests.Session,
        stream_obj: Union[BinaryIO, Iterable[bytes]],
        computed_size: Optional[int],
        progress_queue: Optional[List[UploadProgress]] = None,
        retry: Optional[google.api_core.retry.StreamingRetry] = None,
        timeout: Optional[float] = None,
    ) -> Generator[UploadProgress, None, None]:
        """Transmits chunks until transfer completes, yielding buffered progress updates.

        Args:
            transport: The requests session.
            stream_obj: Binary stream yielding upload chunks.
            computed_size: Total payload size in bytes if known.
            progress_queue: Optional list buffering UploadProgress snapshots.
            retry: Optional retry policy override for chunk transmission. Protocol
                recovery is preserved automatically, and terminal errors
                (``DeadlineExceeded``, ``TransferStalledError``,
                ``UploadCancelledError``, and ``UnseekableStreamError``) are never
                retried.
            timeout: Optional per-attempt timeout ceiling in seconds.

        Yields:
            UploadProgress snapshots for each transmission milestone.

        Raises:
            ValueError: If upload concludes without a server response.
        """
        if progress_queue is None:
            progress_queue = []

        while progress_queue:
            yield progress_queue.pop(0)

        final_resp: Optional[requests.Response] = None
        retry_policy = self._get_streaming_retry(retry_override=retry)

        def attempt_stream() -> Generator[UploadProgress, None, None]:
            nonlocal final_resp
            if self._needs_recovery:
                _LOGGER.info(
                    "Recoverable error during chunk upload. Querying server offset."
                )
                self._notify_progress(
                    common.ProgressState.RECOVERING,
                    progress_queue=progress_queue,
                )
                recover_resp = self._recover(
                    transport, stream_obj, progress_queue=progress_queue
                )
                if self._state.finished:
                    final_resp = recover_resp
                self._needs_recovery = False
                while progress_queue:
                    yield progress_queue.pop(0)

            while not self._state.finished and not self._state.invalid:
                try:
                    final_resp = self._transmit_chunk(
                        transport,
                        stream_obj,
                        computed_size,
                        progress_queue=progress_queue,
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
            yield from retryable_stream()
        except (requests.exceptions.Timeout, exceptions.RetryError) as exc:
            timeout_exc = (
                exc.__cause__ if isinstance(exc, exceptions.RetryError) else exc
            )
            if not isinstance(timeout_exc, requests.exceptions.Timeout):
                raise
            self._enrich_exception(timeout_exc)
            self._get_deadline_remaining()
            raise exceptions.TransferStalledError(
                f"Upload stalled: chunk transfer timed out ({timeout_exc}).",
                upload_url=self.upload_url,
                chunk_size=self.chunk_size,
            ) from timeout_exc

        if final_resp is None:
            raise ValueError("Upload completed without receiving a final response.")

        self._response = _format_response_payload(final_resp, self._response_type)

    def upload(
        self,
        stream: Union[BinaryIO, bytes, Iterable[bytes]],
        request_body: Optional[Union[str, bytes]] = None,
        size: Optional[int] = None,
        transport: Optional[requests.Session] = None,
        content_type: Optional[str] = None,
        retry: Optional[google.api_core.retry.StreamingRetry] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Executes the resumable upload from start to completion.

        Args:
            stream: Data payload to upload (file-like stream, bytes, or iterable of bytes).
            request_body: Initial metadata payload sent with the start request.
                When ``None``, the ``request_body`` supplied to the session constructor
                (if any) is used.
            size: Total stream size in bytes, if known.
            transport: Optional requests session.
            content_type: Optional MIME type of the stream payload.
            retry: Optional retry configuration (``StreamingRetry``) for
                chunk upload requests. Use this to customize exponential backoff
                timing between chunk retries or to supply a custom ``predicate`` for
                API-specific transient errors. A custom ``predicate`` replaces the
                default transient HTTP status check (HTTP 408, 429, 500, 502, 503,
                and 504). Transport errors and protocol recovery errors (HTTP 400,
                412, 416, and ``MissingStatusHeaderError``) always initiate server
                offset recovery. Terminal errors (``DeadlineExceeded``,
                ``TransferStalledError``, ``UploadCancelledError``, and
                ``UnseekableStreamError``) are never retried.
            timeout: Optional per-attempt timeout ceiling in seconds.

        Returns:
            The final server response payload or deserialized response message.

        Raises:
            ValueError: If transport is missing or upload completes without a response.
            GoogleAPICallError: If an unrecoverable API error occurs.
        """
        for _ in self.iter_upload(
            stream=stream,
            request_body=request_body,
            size=size,
            transport=transport,
            content_type=content_type,
            retry=retry,
            timeout=timeout,
        ):
            pass
        return self._response

    def iter_upload(
        self,
        stream: Union[BinaryIO, bytes, Iterable[bytes]],
        request_body: Optional[Union[str, bytes]] = None,
        size: Optional[int] = None,
        transport: Optional[requests.Session] = None,
        content_type: Optional[str] = None,
        retry: Optional[google.api_core.retry.StreamingRetry] = None,
        timeout: Optional[float] = None,
    ) -> Generator[UploadProgress, None, None]:
        """Streams upload execution, yielding UploadProgress snapshots (PEP 255).

        Args:
            stream: Data payload to upload (file-like stream, bytes, or iterable of bytes).
            request_body: Initial metadata payload sent with the start request.
                When ``None``, the ``request_body`` supplied to the session constructor
                (if any) is used.
            size: Total stream size in bytes, if known.
            transport: Optional requests session.
            content_type: Optional MIME type of the stream payload.
            retry: Optional retry configuration (``StreamingRetry``) for
                chunk upload requests. Use this to customize exponential backoff
                timing between chunk retries or to supply a custom ``predicate`` for
                API-specific transient errors. A custom ``predicate`` replaces the
                default transient HTTP status check (HTTP 408, 429, 500, 502, 503,
                and 504). Transport errors and protocol recovery errors (HTTP 400,
                412, 416, and ``MissingStatusHeaderError``) always initiate server
                offset recovery. Terminal errors (``DeadlineExceeded``,
                ``TransferStalledError``, ``UploadCancelledError``, and
                ``UnseekableStreamError``) are never retried.
            timeout: Optional per-attempt timeout ceiling in seconds.

        Yields:
            UploadProgress snapshots for each chunk transmission milestone.

        Raises:
            ValueError: If transport is missing or upload completes without a response.
            GoogleAPICallError: If an unrecoverable API error occurs.
        """
        sess = self._get_transport(transport)
        if content_type is not None:
            self._content_type = content_type
        if request_body is None:
            request_body = self._request_body
        self._reset_transfer_state()
        progress_queue: List[UploadProgress] = []
        try:
            stream_obj, computed_size = self._prepare_stream(stream, size)
            self._initiate(
                transport=sess,
                request_body=request_body,
                size=computed_size,
                progress_queue=progress_queue,
            )
            yield from self._transmit_all_chunks(
                sess,
                stream_obj,
                computed_size,
                progress_queue=progress_queue,
                retry=retry,
                timeout=timeout,
            )
        except Exception as exc:
            self._enrich_exception(exc)
            raise

    def resume(
        self,
        upload_url: str,
        stream: Union[BinaryIO, bytes, Iterable[bytes]],
        size: Optional[int] = None,
        chunk_size: Optional[int] = None,
        transport: Optional[requests.Session] = None,
        retry: Optional[google.api_core.retry.StreamingRetry] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Resumes an existing upload from a saved upload URL.

        Args:
            upload_url (str): The pre-existing upload session URL.
            stream (Union[BinaryIO, bytes, Iterable[bytes]]): The data payload
                to resume uploading from.
            size (Optional[int]): Total size of the payload in bytes, if known.
            chunk_size (Optional[int]): Optional chunk size override in bytes.
            transport (Optional[requests.Session]): Optional requests session.
            retry (Optional[google.api_core.retry.StreamingRetry]): Optional
                retry configuration (``StreamingRetry``) for chunk upload
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
            The final server response payload or deserialized response message.

        Raises:
            ValueError: If required arguments are missing or response not received.
            GoogleAPICallError: If an unrecoverable API error occurs.
        """
        for _ in self.iter_resume(
            upload_url=upload_url,
            stream=stream,
            size=size,
            chunk_size=chunk_size,
            transport=transport,
            retry=retry,
            timeout=timeout,
        ):
            pass
        return self._response

    def iter_resume(
        self,
        upload_url: str,
        stream: Union[BinaryIO, bytes, Iterable[bytes]],
        size: Optional[int] = None,
        chunk_size: Optional[int] = None,
        transport: Optional[requests.Session] = None,
        retry: Optional[google.api_core.retry.StreamingRetry] = None,
        timeout: Optional[float] = None,
    ) -> Generator[UploadProgress, None, None]:
        """Streams resumption of an upload, yielding UploadProgress snapshots.

        Args:
            upload_url (str): The pre-existing upload session URL.
            stream (Union[BinaryIO, bytes, Iterable[bytes]]): The data payload
                to resume uploading from.
            size (Optional[int]): Total size of the payload in bytes, if known.
            chunk_size (Optional[int]): Optional chunk size override in bytes.
            transport (Optional[requests.Session]): Optional requests session.
            retry (Optional[google.api_core.retry.StreamingRetry]): Optional
                retry configuration (``StreamingRetry``) for chunk upload
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

        Yields:
            UploadProgress snapshots for each chunk transmission milestone.

        Raises:
            ValueError: If required arguments are missing or response not received.
            GoogleAPICallError: If an unrecoverable API error occurs.
        """
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
        try:
            stream_obj, computed_size = self._prepare_stream(stream, size)
            self._recover(sess, stream_obj, progress_queue=progress_queue)
            yield from self._transmit_all_chunks(
                sess,
                stream_obj,
                computed_size,
                progress_queue=progress_queue,
                retry=retry,
                timeout=timeout,
            )
        except Exception as exc:
            self._enrich_exception(exc)
            raise

    def _prepare_stream(
        self, stream: Union[BinaryIO, bytes, Iterable[bytes]], size: Optional[int]
    ) -> Tuple[Union[BinaryIO, Iterable[bytes]], Optional[int]]:
        """Normalizes stream input into a readable stream object and determines stream length.

        Args:
            stream: Input stream, bytes, or iterable of bytes.
            size: Explicit total size in bytes, if known.

        Returns:
            Tuple of (prepared stream object, computed total size).
        """
        computed_size = size
        if isinstance(stream, (str, dict)):
            raise TypeError(f"Unsupported stream type: {type(stream)}")
        if isinstance(stream, bytes):
            stream_obj: Union[BinaryIO, Iterable[bytes]] = io.BytesIO(stream)
            if computed_size is None:
                computed_size = len(stream)
        elif not hasattr(stream, "read") and isinstance(stream, Iterable):
            stream_obj = _IterableReader(stream)
        elif hasattr(stream, "read"):
            stream_obj = stream
            if computed_size is None:
                computed_size = _get_buffer_size(stream_obj)
            seekable_fn = getattr(stream_obj, "seekable", None)
            tell_fn = getattr(stream_obj, "tell", None)
            seek_fn = getattr(stream_obj, "seek", None)
            if (
                computed_size is None
                and callable(seekable_fn)
                and seekable_fn()
                and callable(tell_fn)
                and callable(seek_fn)
            ):
                cur = tell_fn()
                seek_fn(0, io.SEEK_END)
                computed_size = tell_fn() - cur
                seek_fn(cur)
        else:
            raise TypeError(f"Unsupported stream type: {type(stream)}")

        tell_fn = getattr(stream_obj, "tell", None)
        if callable(tell_fn):
            try:
                self._start_stream_offset = tell_fn()
            except (OSError, AttributeError):
                self._start_stream_offset = 0

        return stream_obj, computed_size
