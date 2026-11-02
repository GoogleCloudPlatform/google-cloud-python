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

"""Sans-I/O Resumable Upload protocol state machine."""

import logging
from typing import Dict, Mapping, Optional, Sequence, Tuple, Union

from google.api_core import exceptions
from google.api_core.resumable_transfer import common

_LOGGER = logging.getLogger(__name__)


class _ProtocolState(object):
    """Encapsulates the state and command formatting for Resumable Upload protocol."""

    def __init__(
        self,
        upload_url: Optional[str] = None,
        chunk_size: int = common.DEFAULT_CHUNK_SIZE,
    ) -> None:
        """Initializes the protocol state machine.

        Args:
            upload_url: The initial service endpoint URL for starting a new
                upload (stored statically as ``initial_url``), or an existing
                session URL when resuming.
            chunk_size: Desired chunk size in bytes.
        """
        self._initial_url = upload_url or ""
        self._chunk_size = chunk_size
        self._upload_url: Optional[str] = upload_url
        self._chunk_granularity: Optional[int] = None
        self._bytes_uploaded = 0
        self._total_bytes: Optional[int] = None
        self._finished = False
        self._invalid = False

    @property
    def initial_url(self) -> str:
        """str: The static service endpoint URL used to initiate a new upload session.

        Unlike ``upload_url``, this value remains unchanged throughout the
        lifecycle of the state machine and is used by ``build_start_request()``
        as the target endpoint for the ``start`` command.
        """
        return self._initial_url

    @property
    def upload_url(self) -> Optional[str]:
        """Optional[str]: The established upload session URL, or ``None`` if not established.

        Unlike ``initial_url`` (which remains static as the start endpoint),
        ``upload_url`` is populated with the unique session URL returned by the
        server in the ``x-goog-upload-url`` header once the upload is initiated
        (or updated via ``set_session_url()`` when resuming). It is used for
        subsequent chunk transfer, query, and cancel requests, and can be saved
        to resume an interrupted upload later.
        """
        return self._upload_url

    @property
    def bytes_uploaded(self) -> int:
        """The confirmed number of bytes committed to the server."""
        return self._bytes_uploaded

    @property
    def total_bytes(self) -> Optional[int]:
        """The total payload size in bytes, or None if unknown."""
        return self._total_bytes

    @property
    def finished(self) -> bool:
        """Whether the upload has completed successfully."""
        return self._finished

    @property
    def invalid(self) -> bool:
        """Whether the upload session has encountered a terminal failure."""
        return self._invalid

    @property
    def chunk_size(self) -> int:
        """Block-aligned chunk size informed by server granularity."""
        if self._chunk_granularity:
            return (
                (self._chunk_size + self._chunk_granularity - 1)
                // self._chunk_granularity
            ) * self._chunk_granularity
        return self._chunk_size

    def build_start_request(
        self,
        body: Union[str, bytes] = "",
        headers: Optional[Sequence[Tuple[str, str]]] = None,
        content_type: Optional[str] = None,
        size: Optional[int] = None,
    ) -> Tuple[str, str, Dict[str, str], bytes]:
        """Formats the HTTP start request.

        Args:
            body: Initial metadata payload.
            headers: Optional sequence of header tuples to include.
            content_type: MIME type of the stream payload.
            size: Total size of the stream in bytes, if known.

        Returns:
            A tuple of (HTTP method, URL, headers dict, payload bytes).

        Raises:
            ValueError: If the initial upload URL was not provided.
        """
        if not self._initial_url:
            raise ValueError("upload_url must be provided to start an upload.")
        self._upload_url = None
        self._chunk_granularity = None
        self._bytes_uploaded = 0
        self._total_bytes = size
        self._finished = False
        self._invalid = False
        req_headers: Dict[str, str] = {}

        if headers:
            for k, v in headers:
                key = k.decode("utf-8") if isinstance(k, bytes) else str(k)
                val = v.decode("utf-8") if isinstance(v, bytes) else str(v)
                req_headers[key] = val

        req_headers[common.HEADER_PROTOCOL] = common.PROTOCOL_RESUMABLE
        req_headers[common.HEADER_COMMAND] = common._Command.START.value

        if content_type is not None:
            req_headers[common.HEADER_CONTENT_TYPE] = content_type
        if size is not None:
            req_headers[common.HEADER_CONTENT_LENGTH] = str(size)

        payload = body.encode("utf-8") if isinstance(body, str) else body
        return "POST", self._initial_url, req_headers, payload

    def process_start_response(
        self, status_code: int, headers: Mapping[str, str]
    ) -> str:
        """Processes start response and extracts upload session URL.

        Args:
            status_code: HTTP response status code.
            headers: HTTP response headers.

        Returns:
            The established resumable upload session URL.

        Raises:
            exceptions.MissingStatusHeaderError: If status header is missing.
            ValueError: If start response indicates failure or URL is missing.
        """
        if status_code not in (200, 201):
            self._invalid = True
            raise ValueError(f"Start command failed with status {status_code}")

        headers_lower = {k.lower(): v for k, v in headers.items()}
        status = headers_lower.get(common.HEADER_STATUS.lower())
        if not status:
            raise exceptions.MissingStatusHeaderError(
                f"Missing {common.HEADER_STATUS} header in start response"
            )

        upload_url = headers_lower.get(common.HEADER_URL.lower())
        if not upload_url:
            self._invalid = True
            raise ValueError(f"Server did not return {common.HEADER_URL} header")

        self._upload_url = upload_url
        granularity = headers_lower.get(common.HEADER_CHUNK_GRANULARITY.lower())
        if granularity:
            self._chunk_granularity = int(granularity)

        return self._upload_url

    def build_chunk_request(
        self,
        data: Union[bytes, memoryview],
        is_last_chunk: bool,
        content_type: Optional[str] = None,
    ) -> Tuple[str, str, Dict[str, str], bytes]:
        """Formats an upload chunk request.

        Args:
            data: Chunk byte data or memoryview slice.
            is_last_chunk: True if this chunk concludes the upload payload.
            content_type: MIME type of the uploaded chunk data.

        Returns:
            A tuple of (HTTP method, URL, headers dict, payload bytes).

        Raises:
            ValueError: If upload session URL is not established.
        """
        if not self._upload_url:
            raise ValueError("Upload session URL not established.")

        command = (
            f"{common._Command.UPLOAD.value}, {common._Command.FINALIZE.value}"
            if is_last_chunk
            else common._Command.UPLOAD.value
        )

        headers = {
            common.HEADER_COMMAND: command,
            common.HEADER_OFFSET: str(self._bytes_uploaded),
        }
        if content_type:
            headers["Content-Type"] = content_type

        payload = bytes(data) if isinstance(data, memoryview) else data
        return "POST", self._upload_url, headers, payload

    def process_chunk_response(
        self, status_code: int, headers: Mapping[str, str], chunk_bytes_sent: int
    ) -> None:
        """Processes upload chunk response and updates committed bytes.

        Args:
            status_code: HTTP response status code.
            headers: HTTP response headers.
            chunk_bytes_sent: Byte length of the chunk sent in the request.

        Raises:
            exceptions.MissingStatusHeaderError: If status header is missing from successful response.
            exceptions.UploadCancelledError: If server indicates session was cancelled.
        """
        if status_code not in (200, 201):
            return

        headers_lower = {k.lower(): v for k, v in headers.items()}
        status = headers_lower.get(common.HEADER_STATUS.lower())
        if not status:
            raise exceptions.MissingStatusHeaderError(
                f"Missing {common.HEADER_STATUS} header in chunk upload response"
            )

        if status == common._Status.ACTIVE.value:
            self._bytes_uploaded += chunk_bytes_sent
        elif status == common._Status.FINAL.value:
            self._finished = True
            self._bytes_uploaded += chunk_bytes_sent
        elif status == common._Status.CANCELLED.value:
            self._invalid = True
            raise exceptions.UploadCancelledError(
                "Upload session was cancelled by server"
            )

    def build_query_request(self) -> Tuple[str, str, Dict[str, str], bytes]:
        """Formats the query request to discover server offset during recovery.

        Returns:
            A tuple of (HTTP method, URL, headers dict, payload bytes).

        Raises:
            ValueError: If upload session URL is not established.
        """
        if not self._upload_url:
            raise ValueError("Upload session URL not established.")

        headers = {common.HEADER_COMMAND: common._Command.QUERY.value}
        return "POST", self._upload_url, headers, b""

    def process_query_response(
        self, status_code: int, headers: Mapping[str, str]
    ) -> int:
        """Processes query response and returns current server byte offset.

        Args:
            status_code: HTTP response status code.
            headers: HTTP response headers.

        Returns:
            The current server byte offset.

        Raises:
            ValueError: If query recovery indicates failure.
            exceptions.UploadCancelledError: If server indicates session was cancelled.
        """
        if status_code not in (200, 201):
            self._invalid = True
            raise ValueError(f"Query recovery failed with status {status_code}")

        headers_lower = {k.lower(): v for k, v in headers.items()}
        status = headers_lower.get(common.HEADER_STATUS.lower())

        if status == common._Status.ACTIVE.value:
            received = int(headers_lower.get(common.HEADER_SIZE_RECEIVED.lower(), "0"))
            self._bytes_uploaded = received
        elif status == common._Status.FINAL.value:
            self._finished = True
        elif status == common._Status.CANCELLED.value:
            self._invalid = True
            raise exceptions.UploadCancelledError(
                "Upload session was cancelled by server"
            )

        return self._bytes_uploaded

    def build_cancel_request(self) -> Tuple[str, str, Dict[str, str], bytes]:
        """Formats the cancel request.

        Returns:
            A tuple of (HTTP method, URL, headers dict, payload bytes).

        Raises:
            ValueError: If upload session URL is not established.
        """
        if not self._upload_url:
            raise ValueError("Upload session URL not established.")

        headers = {common.HEADER_COMMAND: common._Command.CANCEL.value}
        return "POST", self._upload_url, headers, b""

    def process_cancel_response(
        self, status_code: int, headers: Mapping[str, str]
    ) -> None:
        """Processes cancel response and marks session invalid.

        Args:
            status_code: HTTP response status code.
            headers: HTTP response headers.
        """
        self._invalid = True
