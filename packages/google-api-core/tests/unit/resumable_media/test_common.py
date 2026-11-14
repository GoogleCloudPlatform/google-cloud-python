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


from google.api_core.resumable_media import _common


def test_constants():
    assert _common.UPLOAD_PROTOCOL_HEADER == "X-Goog-Upload-Protocol"
    assert _common.UPLOAD_COMMAND_HEADER == "X-Goog-Upload-Command"
    assert _common.UPLOAD_STATUS_HEADER == "X-Goog-Upload-Status"
    assert _common.UPLOAD_URL_HEADER == "X-Goog-Upload-URL"
    assert _common.UPLOAD_OFFSET_HEADER == "X-Goog-Upload-Offset"
    assert _common.UPLOAD_SIZE_RECEIVED_HEADER == "X-Goog-Upload-Size-Received"
    assert _common.UPLOAD_CHUNK_GRANULARITY_HEADER == "X-Goog-Upload-Chunk-Granularity"
    assert _common.UPLOAD_PROTOCOL_VALUE == "resumable"
    assert _common.DEFAULT_CHUNK_SIZE == 10 * 1024 * 1024


def test_upload_command():
    assert _common.UploadCommand.START == "start"
    assert _common.UploadCommand.UPLOAD == "upload"
    assert _common.UploadCommand.FINALIZE == "finalize"
    assert _common.UploadCommand.QUERY == "query"
    assert _common.UploadCommand.CANCEL == "cancel"


def test_upload_status():
    assert _common.UploadStatus.ACTIVE == "active"
    assert _common.UploadStatus.FINAL == "final"
    assert _common.UploadStatus.CANCELLED == "cancelled"
