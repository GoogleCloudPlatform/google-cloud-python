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

"""Common constants, headers, and shared configuration for Resumable Upload protocol."""

import dataclasses
import datetime
import enum
from typing import Any, Mapping, Optional, Sequence, Tuple, Union

import google.protobuf.message
import proto
from google.protobuf import json_format

from google.api_core import exceptions

# Default chunk size: 10 MiB
DEFAULT_CHUNK_SIZE = 10 * 1024 * 1024

# Default timeout in seconds for the initial start request
DEFAULT_START_TIMEOUT = 60.0

# Protocol Headers
HEADER_PROTOCOL = "X-Goog-Upload-Protocol"
HEADER_COMMAND = "X-Goog-Upload-Command"
HEADER_STATUS = "X-Goog-Upload-Status"
HEADER_URL = "X-Goog-Upload-URL"
HEADER_OFFSET = "X-Goog-Upload-Offset"
HEADER_SIZE_RECEIVED = "X-Goog-Upload-Size-Received"
HEADER_CONTENT_TYPE = "X-Goog-Upload-Header-Content-Type"
HEADER_CONTENT_LENGTH = "X-Goog-Upload-Header-Content-Length"
HEADER_CHUNK_GRANULARITY = "X-Goog-Upload-Chunk-Granularity"

PROTOCOL_RESUMABLE = "resumable"


class _Command(str, enum.Enum):
    """Protocol commands."""

    START = "start"
    UPLOAD = "upload"
    FINALIZE = "finalize"
    QUERY = "query"
    CANCEL = "cancel"


class _Status(str, enum.Enum):
    """Server upload status values."""

    ACTIVE = "active"
    FINAL = "final"
    CANCELLED = "cancelled"


class ProgressState(str, enum.Enum):
    """Progress notification state values."""

    STARTED = "started"
    UPLOADING = "uploading"
    RECOVERING = "recovering"
    OFFSET_RECEIVED = "offset received"
    FINALIZED = "finalized"


@dataclasses.dataclass(frozen=True)
class UploadProgress:
    """Upload progress notification payload.

    Attributes:
        upload_url: The unique session URL for this upload.
        chunk_size: The actual negotiated chunk size.
        bytes_uploaded: The total confirmed bytes committed so far.
        total_bytes: The total size of the stream in bytes, if known.
        state: The current progress state.
    """

    upload_url: str
    chunk_size: int
    bytes_uploaded: int
    total_bytes: Optional[int]
    state: ProgressState


# HTTP status codes indicating transient retryable errors (Category 1)
RETRYABLE_STATUS_CODES = (408, 429, 500, 502, 503, 504)

# HTTP status codes indicating state consistency errors requiring recovery (Category 2)
RECOVERABLE_STATUS_CODES = (400, 412, 416)

# Exception types indicating unrecoverable terminal conditions (Category 3)
TERMINAL_ERRORS = (
    exceptions.DeadlineExceeded,
    exceptions.TransferStalledError,
    exceptions.UploadCancelledError,
    exceptions.UnseekableStreamError,
)


@dataclasses.dataclass
class ResumableUploadConfig:
    """Configuration options for a resumable upload.

    Attributes:
        chunk_size: Size in bytes for each uploaded data chunk. Defaults to 10 MiB.
        stall_minimum_rate: Minimum transfer rate in bytes per second. Defaults to 64 KiB/s.
        stall_timeout: Stall duration threshold in seconds. Defaults to 120s.
        headers: Additional HTTP headers dispatched exclusively with start request.
        deadline: Optional overall wall-clock deadline for the entire upload process.
            When set, each HTTP request timeout is trimmed to the remaining time before
            the deadline, and DeadlineExceeded is raised immediately when the deadline
            elapses (even on healthy streams). Timezone-aware datetimes (e.g.,
            ``datetime.now(timezone.utc) + timedelta(...)``) are recommended;
            timezone-naive datetimes are assumed to be in local system time. When
            None (default), transfer duration is governed by stall control
            (stall_minimum_rate and stall_timeout), allowing healthy streams
            transferring above the minimum rate to continue indefinitely.
    """

    chunk_size: int = DEFAULT_CHUNK_SIZE
    stall_minimum_rate: int = 64 * 1024
    stall_timeout: float = 120.0
    headers: Optional[Union[Mapping[str, str], Sequence[Tuple[str, str]]]] = None
    deadline: Optional[datetime.datetime] = None

    def __post_init__(self) -> None:
        if self.deadline is not None:
            self.deadline = self.deadline.astimezone(datetime.timezone.utc)

    @property
    def start_headers(self) -> Optional[Sequence[Tuple[str, str]]]:
        """Returns normalized additional headers for the start request."""
        if self.headers is None:
            return None
        if isinstance(self.headers, Mapping):
            return list(self.headers.items())
        return list(self.headers)


def _format_response_payload(
    response: Union[Any, bytes],
    response_type: Optional[Any],
) -> Any:
    """Formats raw response or bytes into protobuf or proto-plus message type if configured.

    Args:
        response: Raw HTTP response object or response body bytes.
        response_type: Deserializer callable, proto.Message class, or
            google.protobuf.message.Message class or instance.

    Returns:
        Deserialized protobuf message, or raw response bytes if
        ``response_type`` is ``None``.
    """
    content: bytes
    if isinstance(response, bytes):
        content = response
    elif hasattr(response, "content"):
        content = response.content
    else:
        content = bytes(response)

    if response_type is None:
        return content

    from_json_fn = getattr(response_type, "from_json", None)
    if callable(from_json_fn):
        if isinstance(response_type, type) and issubclass(response_type, proto.Message):
            return from_json_fn(content, ignore_unknown_fields=True)
        return from_json_fn(content)
    if isinstance(response_type, type) and issubclass(
        response_type, google.protobuf.message.Message
    ):
        instance = response_type()
        return json_format.Parse(content, instance, ignore_unknown_fields=True)
    if isinstance(response_type, google.protobuf.message.Message):
        return json_format.Parse(content, response_type, ignore_unknown_fields=True)
    if callable(response_type):
        return response_type(content)

    return content
