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

"""Sans-I/O Resumable Upload protocol implementation.

This module provides the pure state machine for Resumable Uploads.
"""

import logging
from typing import Dict, Optional, Sequence, Tuple

from google.api_core import exceptions
from google.api_core.resumable_media import _common

_LOGGER = logging.getLogger(__name__)


class ResumableUpload(object):
    """Sans-I/O state machine for a resumable upload.

    This class manages the initiation, chunk boundaries, offset calculation,
    and recovery states for a Google Resumable Upload. It emits logical
    requests (method, url, headers, data) and consumes logical responses
    (status_code, headers).

    Args:
        upload_url (str): The initial URL to start the resumable upload.
        chunk_size (Optional[int]): The base size of chunks in bytes. If not
            specified, defaults to 10MB (`_common.DEFAULT_CHUNK_SIZE`).
    """

    def __init__(self, upload_url: str, chunk_size: int = _common.DEFAULT_CHUNK_SIZE):
        self._initial_url = upload_url
        self._chunk_size = chunk_size
        self._resumable_url: Optional[str] = None
        self._chunk_granularity: Optional[int] = None
        self._bytes_uploaded = 0
        self._total_bytes: Optional[int] = None
        self._finished = False
        self._invalid = False

    @property
    def resumable_url(self) -> Optional[str]:
        """Optional[str]: The session URL returned by the initiate request."""
        return self._resumable_url

    @property
    def bytes_uploaded(self) -> int:
        """int: The number of bytes successfully uploaded so far."""
        return self._bytes_uploaded

    @property
    def finished(self) -> bool:
        """bool: Indicates if the upload has completed successfully."""
        return self._finished

    @property
    def invalid(self) -> bool:
        """bool: Indicates if the state machine encountered an unrecoverable state."""
        return self._invalid

    @property
    def chunk_size(self) -> int:
        """int: The block-aligned chunk size informed by server granularity.

        All chunks (except the last one) must have a size that is a multiple
        of the server's chunk granularity. We round the user's requested size
        up to the nearest granularity multiple to ensure all intermediate
        chunks conform to this protocol constraint.
        """
        if self._chunk_granularity:
            return (
                (self._chunk_size + self._chunk_granularity - 1)
                // self._chunk_granularity
            ) * self._chunk_granularity
        return self._chunk_size

    def build_initiate_request(
        self,
        stream_metadata: Optional[Sequence[Tuple[str, str]]] = None,
        content_type: Optional[str] = None,
        size: Optional[int] = None,
    ) -> Tuple[str, str, Dict[str, str], bytes]:
        """Constructs an upload initiation request.

        Args:
            stream_metadata (Optional[Sequence[Tuple[str, str]]]): Additional headers for
                the upload initiation request. These headers are ONLY applied to
                the initial request and will NOT be included in subsequent chunk
                upload requests. If not specified, no additional headers will be appended.
            content_type (Optional[str]): MIME type of the uploaded content.
                If not specified, the `X-Goog-Upload-Header-Content-Type` header
                will be omitted.
            size (Optional[int]): Total size of the payload in bytes if known.
                If not specified, the `X-Goog-Upload-Header-Content-Length` header
                will be omitted, indicating an unknown overall payload size.

        Returns:
            Tuple[str, str, Dict[str, str], bytes]: The method, url, headers, and body.
        """
        self._total_bytes = size
        headers = {}

        # Merge user metadata first
        if stream_metadata:
            for k, v in stream_metadata:
                headers[k] = v.decode("utf-8") if isinstance(v, bytes) else str(v)

        # Critical protocol headers overwrite user metadata
        headers[_common.UPLOAD_PROTOCOL_HEADER] = _common.UPLOAD_PROTOCOL_VALUE
        headers[_common.UPLOAD_COMMAND_HEADER] = _common.UploadCommand.START

        if content_type is not None:
            headers[_common.UPLOAD_CONTENT_TYPE_HEADER] = content_type
        if size is not None:
            headers[_common.UPLOAD_CONTENT_LENGTH_HEADER] = str(size)

        return "POST", self._initial_url, headers, b""

    def process_initiate_response(
        self, status_code: int, headers: Dict[str, str]
    ) -> None:
        """Processes the initiation response from the server.

        Args:
            status_code (int): HTTP status code of the response.
            headers (Dict[str, str]): HTTP headers of the response.
        """
        if status_code not in (200, 201):
            self._invalid = True
            return

        headers_lower = {k.lower(): v for k, v in headers.items()}
        resumable_url_target = _common.UPLOAD_URL_HEADER.lower()

        self._resumable_url = headers_lower.get(resumable_url_target)
        if not self._resumable_url:
            self._invalid = True
            raise ValueError(f"Server did not return {_common.UPLOAD_URL_HEADER}")

        granularity = headers_lower.get(_common.UPLOAD_CHUNK_GRANULARITY_HEADER.lower())
        if granularity:
            self._chunk_granularity = int(granularity)

    def process_initiate_error(self, exc: Exception) -> None:
        """Processes an error from the initiation request.

        Args:
            exc (Exception): The exception raised during initiation.
        """
        self._invalid = True

    def build_chunk_request(
        self, data: bytes, final: bool = False
    ) -> Tuple[str, str, Dict[str, str], bytes]:
        """Constructs a request to upload a chunk of data.

        Args:
            data (bytes): The chunk of data to upload.
            final (bool): Whether this is the final chunk. The I/O layer should
                set this to True when the stream is exhausted.

        Returns:
            Tuple[str, str, Dict[str, str], bytes]: The method, url, headers, and body.
        """
        if not self._resumable_url:
            raise ValueError("Upload not initiated.")

        data_len = len(data)
        is_last_chunk = final

        if self._total_bytes is not None:
            if self._bytes_uploaded + data_len >= self._total_bytes:
                is_last_chunk = True
        elif data_len < self.chunk_size:
            is_last_chunk = True

        command = _common.UploadCommand.UPLOAD
        if is_last_chunk:
            command = (
                f"{_common.UploadCommand.UPLOAD}, {_common.UploadCommand.FINALIZE}"
            )

        headers = {
            _common.UPLOAD_COMMAND_HEADER: command,
            _common.UPLOAD_OFFSET_HEADER: str(self._bytes_uploaded),
        }

        return "POST", self._resumable_url, headers, data

    def process_chunk_response(
        self, status_code: int, headers: Dict[str, str], expected_chunk_bytes: int
    ) -> None:
        """Processes the upload chunk response from the server.

        Args:
            status_code (int): HTTP status code of the response.
            headers (Dict[str, str]): HTTP headers of the response.
            expected_chunk_bytes (int): The number of bytes that were uploaded.
        """
        if status_code not in (200, 201):
            # We do not invalidate the upload here. A non-2xx response (like 503)
            # could be transient. The I/O layer can either retry the chunk
            # directly or execute a recovery query to sync the state.
            return

        headers_lower = {k.lower(): v for k, v in headers.items()}
        status = headers_lower.get(_common.UPLOAD_STATUS_HEADER.lower())

        if status == _common.UploadStatus.ACTIVE:
            self._bytes_uploaded += expected_chunk_bytes
        elif status == _common.UploadStatus.FINAL:
            self._finished = True
            self._bytes_uploaded += expected_chunk_bytes
        elif status == _common.UploadStatus.CANCELLED:
            self._invalid = True

    def process_chunk_error(self, exc: Exception) -> bool:
        """Processes an error from the chunk upload request.

        Args:
            exc (Exception): The exception raised during chunk upload.

        Returns:
            bool: True if the error is recoverable and requires a recovery query,
                  False otherwise.
        """
        if isinstance(exc, exceptions.GoogleAPICallError):
            if exc.code in _common.RECOVERABLE_STATUS_CODES:
                return True

        self._invalid = True
        return False

    def build_recovery_request(self) -> Tuple[str, str, Dict[str, str], bytes]:
        """Constructs a request to query the server's current upload state.

        Returns:
            Tuple[str, str, Dict[str, str], bytes]: The method, url, headers, and body.
        """
        if not self._resumable_url:
            raise ValueError("Upload not initiated.")

        headers = {_common.UPLOAD_COMMAND_HEADER: _common.UploadCommand.QUERY}
        return "POST", self._resumable_url, headers, b""

    def process_recovery_response(
        self, status_code: int, headers: Dict[str, str]
    ) -> int:
        """Processes the recovery query response from the server.

        Args:
            status_code (int): HTTP status code of the response.
            headers (Dict[str, str]): HTTP headers of the response.

        Returns:
            int: The confirmed number of bytes uploaded so far.
        """
        if status_code not in (200, 201):
            self._invalid = True
            raise ValueError(f"Recovery failed with status {status_code}")

        headers_lower = {k.lower(): v for k, v in headers.items()}
        status = headers_lower.get(_common.UPLOAD_STATUS_HEADER.lower())

        if status == _common.UploadStatus.ACTIVE:
            received = int(
                headers_lower.get(_common.UPLOAD_SIZE_RECEIVED_HEADER.lower(), "0")
            )
            self._bytes_uploaded = received
        elif status == _common.UploadStatus.FINAL:
            self._finished = True
        elif status == _common.UploadStatus.CANCELLED:
            self._invalid = True
            raise RuntimeError("Upload was cancelled by server")

        return self._bytes_uploaded

    def process_recovery_error(self, exc: Exception) -> None:
        """Processes an error from the recovery query request.

        Args:
            exc (Exception): The exception raised during recovery.
        """
        self._invalid = True
