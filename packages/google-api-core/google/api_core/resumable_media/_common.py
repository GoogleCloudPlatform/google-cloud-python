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

"""Common constants and utilities for Resumable Media."""

# The default size for individual upload chunks (10 MB).
# When a resumable upload is chunked, the size of each chunk (except the last)
# must be a multiple of the chunk granularity specified by the server in the
# `X-Goog-Upload-Chunk-Granularity` header during the initial `start` request.
# 10 MB is used as a default.
DEFAULT_CHUNK_SIZE = 10 * 1024 * 1024  # 10MB

# The header specifying the upload protocol.
# Sent by the client during upload initiation.
UPLOAD_PROTOCOL_HEADER = "X-Goog-Upload-Protocol"

# The header specifying the protocol command.
# Sent by the client on active requests (e.g. start, upload, finalize, query).
UPLOAD_COMMAND_HEADER = "X-Goog-Upload-Command"

# The header specifying the status of the upload.
# Received from the server.
UPLOAD_STATUS_HEADER = "X-Goog-Upload-Status"

# The header providing the dedicated upload URL.
# Received from the server in the start command response.
UPLOAD_URL_HEADER = "X-Goog-Upload-URL"

# The header specifying the byte offset of the current chunk.
# Sent by the client during chunk uploads.
UPLOAD_OFFSET_HEADER = "X-Goog-Upload-Offset"

# The header specifying the number of bytes successfully persisted so far.
# Received from the server, typically in query responses.
UPLOAD_SIZE_RECEIVED_HEADER = "X-Goog-Upload-Size-Received"

# The header specifying the content type of the uploaded content.
# Sent by the client during upload initiation.
UPLOAD_CONTENT_TYPE_HEADER = "X-Goog-Upload-Header-Content-Type"

# The header specifying the total content length of the uploaded content.
# Sent by the client during upload initiation when length is known.
UPLOAD_CONTENT_LENGTH_HEADER = "X-Goog-Upload-Header-Content-Length"

# The header specifying the required block alignment size for chunks.
# Received from the server in the start command response.
UPLOAD_CHUNK_GRANULARITY_HEADER = "X-Goog-Upload-Chunk-Granularity"

# The value indicating the resumable upload protocol.
# Sent by the client in the `UPLOAD_PROTOCOL_HEADER`.
UPLOAD_PROTOCOL_VALUE = "resumable"


class UploadCommand:
    """HTTP Header values for the Resumable Upload command header."""

    START = "start"
    UPLOAD = "upload"
    FINALIZE = "finalize"
    QUERY = "query"
    CANCEL = "cancel"


class UploadStatus:
    """HTTP Header values for the Resumable Upload status header."""

    ACTIVE = "active"
    FINAL = "final"
    CANCELLED = "cancelled"


# HTTP status codes that indicate a transient error and can be retried.
RETRYABLE_STATUS_CODES = (408, 429, 500, 502, 503, 504)

# HTTP status codes that indicate a state mismatch and require modification (recovery).
RECOVERABLE_STATUS_CODES = (400, 412, 416)
