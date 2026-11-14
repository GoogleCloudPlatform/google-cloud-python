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

import datetime
import logging
from typing import Any, BinaryIO, Callable, Dict, Optional, Sequence, Tuple

import requests
import google.api_core.retry
from google.api_core import exceptions

from google.api_core.resumable_media import _common
from google.api_core.resumable_media import _upload

_LOGGER = logging.getLogger(__name__)
_DEFAULT_TIMEOUT = 60.0  # seconds


class _RecoveryRetransmit(Exception):
    """Internal exception to trigger retransmission after a state resync."""

    pass


class ResumableUploadStatus:
    """Status of a resumable upload.

    Attributes:
        upload_url (str): The session URL for the resumable upload.
        total_bytes (Optional[int]): The total number of bytes to be uploaded.
        bytes_uploaded (int): The number of bytes successfully uploaded so far.
        finished (bool): Whether the upload has completed.
    """

    def __init__(
        self,
        upload_url: str,
        total_bytes: Optional[int],
        bytes_uploaded: int,
        finished: bool,
    ):
        self.upload_url = upload_url
        self.total_bytes = total_bytes
        self.bytes_uploaded = bytes_uploaded
        self.finished = finished


class RequestsResumableUpload:
    """Synchronous I/O wrapper for resumable uploads using requests.

    This class adapts the Sans-I/O `ResumableUpload` state machine to perform
    actual network requests using the `requests` library.
    """

    def __init__(
        self,
        upload_url: str,
        stream: BinaryIO,
        size: Optional[int] = None,
        content_type: Optional[str] = None,
        chunk_size: Optional[int] = None,
        deadline: Optional[datetime.datetime] = None,
        headers: Optional[Sequence[Tuple[str, str]]] = None,
        on_progress: Optional[Callable[[ResumableUploadStatus], None]] = None,
    ):
        """Initializes the RequestsResumableUpload.

        Args:
            upload_url: The initial URL to start the resumable upload.
            stream: A stream of bytes to be uploaded.
            size: Total number of bytes to be uploaded.
            content_type: MIME type of the content.
            chunk_size: Block-aligned chunk size in bytes.
            deadline: The deadline for the entire upload process.
            headers: Extra headers for the initiation request.
            on_progress: Callback invoked after each chunk.
        """
        # Note: we let the state machine handle the default chunk size
        kwargs = {}
        if chunk_size is not None:
            kwargs["chunk_size"] = chunk_size
        self._machine = _upload.ResumableUpload(upload_url, **kwargs)

        self.stream = stream
        self.size = size
        self.content_type = content_type
        self.deadline = deadline
        self.extra_headers = headers
        self.on_progress = on_progress

        if hasattr(stream, "tell"):
            try:
                self._start_offset = stream.tell()
            except (OSError, AttributeError):
                self._start_offset = 0
        else:
            self._start_offset = 0

    @property
    def finished(self) -> bool:
        """bool: Indicates if the upload has completed successfully."""
        return self._machine.finished

    @property
    def invalid(self) -> bool:
        """bool: Indicates if the upload has entered an unrecoverable state."""
        return self._machine.invalid

    def _check_deadline(self) -> Optional[float]:
        if self.deadline:
            now = datetime.datetime.now(datetime.timezone.utc)
            deadline = self.deadline
            if deadline.tzinfo is None:
                deadline = deadline.replace(tzinfo=datetime.timezone.utc)
            timeout = (deadline - now).total_seconds()
            if timeout <= 0:
                raise exceptions.DeadlineExceeded(
                    f"Upload deadline {self.deadline} was exceeded."
                )
            return timeout
        return None

    def _get_retry_predicate(self):
        def should_retry(exc):
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
            if isinstance(exc, exceptions.GoogleAPICallError):
                return exc.code in _common.RETRYABLE_STATUS_CODES
            return False

        return should_retry

    def _check_and_raise_error(self, response: requests.Response):
        """Raises a Google API Core exception if status code is not success."""
        if not response.ok:
            # The API core from_http_response returns an exception instance
            raise exceptions.from_http_response(response)

    def _log_request(
        self, method: str, url: str, headers: Dict[str, str], data: Any = None
    ):
        if not _LOGGER.isEnabledFor(logging.DEBUG):
            return

        safe_headers = {
            k: ("REDACTED" if k.lower() == "authorization" else v)
            for k, v in headers.items()
        }

        display_data = data
        if isinstance(data, (bytes, str)):
            if len(data) > 64:
                display_data = f"{data[:64]!r}... ({len(data)} bytes)"
            else:
                display_data = data
        else:
            display_data = "<stream>" if data else None

        _LOGGER.debug(
            "HTTP Request: %s %s\nHeaders: %s\nBody: %s",
            method,
            url,
            safe_headers,
            display_data,
        )

    def _log_response(self, response: requests.Response):
        if not _LOGGER.isEnabledFor(logging.DEBUG):
            return
        try:
            body = response.text
        except (ValueError, AttributeError):
            body = "<unavailable or closed>"
        _LOGGER.debug(
            "HTTP Response: %s %s\nHeaders: %s\nBody: %s",
            response.status_code,
            response.reason,
            response.headers,
            body,
        )

    def initiate(
        self,
        transport: requests.Session,
        request_body: str = "",
        request_retry: Optional[google.api_core.retry.Retry] = None,
    ):
        """Initiates the resumable upload session.

        Args:
            transport: The requests session.
            request_body: JSON payload for the start request.
            request_retry: Policy for retrying the initial request.
        """
        _LOGGER.info("Initiating resumable upload to %s", self._machine._initial_url)
        method, url, headers, _ = self._machine.build_initiate_request(
            stream_metadata=self.extra_headers,
            content_type=self.content_type,
            size=self.size,
        )

        def do_initiate():
            timeout = self._check_deadline() or _DEFAULT_TIMEOUT
            self._log_request(method, url, headers, request_body)

            response = transport.request(
                method, url, data=request_body, headers=headers, timeout=timeout
            )
            self._log_response(response)
            self._check_and_raise_error(response)
            return response

        if request_retry:
            retry = request_retry
        else:
            retry = google.api_core.retry.Retry(
                predicate=self._get_retry_predicate(), deadline=self._check_deadline()
            )

        try:
            response = retry(do_initiate)()
            self._machine.process_initiate_response(
                response.status_code, response.headers
            )
        except Exception as e:
            self._machine.process_initiate_error(e)
            raise

        # The state machine processes the response to extract session URL etc.
        if self.on_progress:
            assert self._machine.resumable_url is not None
            self.on_progress(
                ResumableUploadStatus(
                    upload_url=self._machine.resumable_url,
                    total_bytes=self.size,
                    bytes_uploaded=0,
                    finished=False,
                )
            )

    def transmit_next_chunk(self, transport: requests.Session) -> requests.Response:
        """Uploads the next chunk of data from the stream.

        Args:
            transport: The requests session.

        Returns:
            The final response for this chunk.
        """
        self._check_deadline()

        def do_transmit():
            # Read a chunk from the stream
            chunk_size = self._machine.chunk_size
            data = self.stream.read(chunk_size)
            data_len = len(data)

            need_recovery, response = self._attempt_transmit_chunk(
                transport, data, data_len
            )
            if need_recovery:
                _LOGGER.info("Transparent recovery triggered for chunk transmission.")
                self._recover(transport)
                # Raise to signal the outer Retry loop to resubmit
                raise _RecoveryRetransmit()
            return response

        # Use Retry to drive the retransmission loop after recovery
        recovery_retransmit = google.api_core.retry.Retry(
            predicate=lambda e: isinstance(e, _RecoveryRetransmit),
            deadline=self._check_deadline(),
        )

        response = recovery_retransmit(do_transmit)()

        if self.on_progress:
            assert self._machine.resumable_url is not None
            self.on_progress(
                ResumableUploadStatus(
                    upload_url=self._machine.resumable_url,
                    total_bytes=self.size,
                    bytes_uploaded=self._machine.bytes_uploaded,
                    finished=self._machine.finished,
                )
            )

        return response

    def _attempt_transmit_chunk(
        self, transport: requests.Session, data: bytes, data_len: int
    ) -> Tuple[bool, Optional[requests.Response]]:
        """Attempts to transmit a single chunk of data using the `do_X` subfunction paradigm.

        This method encapsulates the request serialization, transient retry logic
        (google.api_core.retry.Retry), and HTTP response scrutiny. It classifies
        errors into categories defined in `retry_architecture.md`:

        - **Category 1 (Transient):** Retried automatically within the subfunction.
        - **Category 2 (State Consistency):** Pierces the retry block, intercepted by the outer `try/except`, and triggers signaling for `self._recover()`.
        - **Category 3 (Fatal) / Exhausted Category 1:** Pierces the retry block and raises immediately.

        Args:
            transport: The requests session.
            data: The byte payload to transmit.
            data_len: Length of the data payload.

        Returns:
            A tuple of (need_recovery: bool, response: Optional[requests.Response]).
            - `need_recovery` is True if a Category 2 error occurred, signaling `transmit_next_chunk` to synchronize state via `_recover`.
            - `response` is the successful response object if `need_recovery` is False.
        """
        chunk_size = self._machine.chunk_size
        is_last_chunk = data_len < chunk_size
        if self.size is not None:
            if self._machine.bytes_uploaded + data_len >= self.size:
                is_last_chunk = True

        method, url, headers, payload = self._machine.build_chunk_request(
            data, final=is_last_chunk
        )

        retry = google.api_core.retry.Retry(
            predicate=self._get_retry_predicate(), deadline=self._check_deadline()
        )

        def do_upload():
            _LOGGER.info(
                "Uploading chunk at offset %d, size %d",
                self._machine.bytes_uploaded,
                data_len,
            )
            timeout = self._check_deadline() or _DEFAULT_TIMEOUT
            self._log_request(method, url, headers, payload)

            response = transport.request(
                method, url, data=payload, headers=headers, timeout=timeout
            )
            self._log_response(response)
            if not response.ok:
                raise exceptions.from_http_response(response)
            return response

        try:
            response = retry(do_upload)()
            self._machine.process_chunk_response(
                response.status_code, response.headers, data_len
            )
            return False, response
        except Exception as e:
            if self._machine.process_chunk_error(e):
                _LOGGER.info(
                    "Recoverable error encountered during chunk upload: %s. Triggering state resync.",
                    e,
                )
                return True, None
            raise

    def _recover(self, transport: requests.Session):
        """Attempts to recover from a Category 2 (State Consistency) error by resynchronizing with the server.

        Issues a `QUERY` command via a `do_query` closure to discover the true `offset` of the upload
        and rewinds the local stream.

        Follows the standard architectural patterns (transient retries, deadline enforcement).
        Crucially, for a `QUERY` command, there are no Category 2 errors. If the query throws a 4xx error,
        it is treated as a Category 3 (Fatal) error and raises immediately, permanently halting the upload.

        Args:
            transport: The requests session.
            retry: The retry configuration to use for the query command.

        Raises:
            exceptions.GoogleAPICallError: If the query fails with an unretriable error or maximum attempts are exhausted.
            ValueError: If the stream is not seekable and cannot be rewound.
        """
        _LOGGER.info("Attempting recovery via query command")
        method, url, headers, payload = self._machine.build_recovery_request()

        def do_query():
            timeout = self._check_deadline() or _DEFAULT_TIMEOUT
            self._log_request(method, url, headers, payload)

            response = transport.request(
                method, url, data=payload, headers=headers, timeout=timeout
            )
            self._log_response(response)
            if not response.ok:
                raise exceptions.from_http_response(response)
            return response

        retry_for_recovery = google.api_core.retry.Retry(
            predicate=self._get_retry_predicate(),
            deadline=self._check_deadline(),
        )

        try:
            response = retry_for_recovery(do_query)()
            received = self._machine.process_recovery_response(
                response.status_code, response.headers
            )
        except Exception as e:
            self._machine.process_recovery_error(e)
            raise

        # Seek stream to correct position
        _LOGGER.info("Server reported %d bytes received. Seeking stream.", received)

        if hasattr(self.stream, "seekable") and not self.stream.seekable():
            raise ValueError(
                f"Stream is not seekable. Cannot recover upload to offset {received}."
            )
        try:
            target_offset = self._start_offset + received
            self.stream.seek(target_offset)

        except (OSError, AttributeError) as exc:
            raise ValueError(
                f"There was an error when seeking the stream. Cannot recover upload to offset {received}."
            ) from exc


def make_resumable_upload(
    transport: requests.Session,
    request_body: str,
    stream: BinaryIO,
    upload_url: str,
    size: Optional[int] = None,
    content_type: Optional[str] = None,
    chunk_size: Optional[int] = None,
    request_retry: Optional[google.api_core.retry.Retry] = None,
    deadline: Optional[datetime.datetime] = None,
    headers: Optional[Sequence[Tuple[str, str]]] = None,
    on_progress: Optional[Callable[[ResumableUploadStatus], None]] = None,
) -> requests.Response:
    """Makes a resumable upload using synchronous I/O.

    Args:
        transport: The requests session.
        request_body: JSON payload for the start request.
        stream: A stream of bytes to upload.
        upload_url: Initial URL.
        size: Total size of the upload.
        content_type: Content-type of the stream.
        chunk_size: Explicit chunk size to use.
        request_retry: Retry logic for the initiate request.
        deadline: Overall deadline constraint.
        headers: Extra headers.
        on_progress: Progress callback.

    Returns:
        The final requests.Response object.
    """

    upload = RequestsResumableUpload(
        upload_url=upload_url,
        stream=stream,
        size=size,
        content_type=content_type,
        chunk_size=chunk_size,
        deadline=deadline,
        headers=headers,
        on_progress=on_progress,
    )
    upload.initiate(
        transport=transport, request_body=request_body, request_retry=request_retry
    )

    final_response = None
    while not upload.finished and not upload.invalid:
        final_response = upload.transmit_next_chunk(transport=transport)
    assert final_response is not None
    return final_response
