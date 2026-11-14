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


from google.api_core import exceptions
from google.api_core.resumable_media import _common
from google.api_core.resumable_media import _upload


class TestResumableUpload:
    def test_init(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        assert upload.resumable_url is None
        assert upload.bytes_uploaded == 0
        assert not upload.finished
        assert not upload.invalid
        assert upload.chunk_size == _common.DEFAULT_CHUNK_SIZE

    def test_chunk_size_granularity(self):
        upload = _upload.ResumableUpload("http://test.local/upload", chunk_size=3)
        # Manually set granularity to test the property
        upload._chunk_granularity = 2
        # chunk size 3 should be rounded to next multiple of 2, which is 4
        assert upload.chunk_size == 4

    def test_initiate_request(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        method, url, headers, body = upload.build_initiate_request(
            stream_metadata=[("x-custom-meta", "value")],
            content_type="text/plain",
            size=100,
        )
        assert method == "POST"
        assert url == "http://test.local/upload"
        assert headers[_common.UPLOAD_PROTOCOL_HEADER] == _common.UPLOAD_PROTOCOL_VALUE
        assert headers[_common.UPLOAD_COMMAND_HEADER] == _common.UploadCommand.START
        assert headers["X-Goog-Upload-Header-Content-Type"] == "text/plain"
        assert headers["X-Goog-Upload-Header-Content-Length"] == "100"
        assert headers["x-custom-meta"] == "value"
        assert body == b""

    def test_initiate_request_conflicting_metadata(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        method, url, headers, body = upload.build_initiate_request(
            stream_metadata=[
                ("x-custom-meta", "value"),
                (_common.UPLOAD_PROTOCOL_HEADER, "malicious-protocol"),
                (_common.UPLOAD_COMMAND_HEADER, "malicious-command"),
                (_common.UPLOAD_CONTENT_TYPE_HEADER, "malicious/type"),
            ],
            content_type="text/plain",
            size=100,
        )
        assert method == "POST"
        assert headers[_common.UPLOAD_PROTOCOL_HEADER] == _common.UPLOAD_PROTOCOL_VALUE
        assert headers[_common.UPLOAD_COMMAND_HEADER] == _common.UploadCommand.START
        assert headers[_common.UPLOAD_CONTENT_TYPE_HEADER] == "text/plain"
        assert headers["x-custom-meta"] == "value"

    def test_process_initiate_response_success(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        headers = {
            _common.UPLOAD_URL_HEADER: "http://test.local/resumable_session",
            _common.UPLOAD_CHUNK_GRANULARITY_HEADER: "1024",
        }
        upload.process_initiate_response(200, headers)

        assert not upload.invalid
        assert upload.resumable_url == "http://test.local/resumable_session"
        assert upload._chunk_granularity == 1024

    def test_process_initiate_response_failure(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        upload.process_initiate_response(500, {})
        assert upload.invalid

    def test_build_chunk_request(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        upload._resumable_url = "http://test.local/resumable_session"
        upload._total_bytes = 100
        upload._bytes_uploaded = 0

        # Upload a 50 byte chunk
        method, url, headers, body = upload.build_chunk_request(b"a" * 50)
        assert method == "POST"
        assert url == "http://test.local/resumable_session"
        assert headers[_common.UPLOAD_COMMAND_HEADER] == _common.UploadCommand.UPLOAD
        assert headers[_common.UPLOAD_OFFSET_HEADER] == "0"
        assert body == b"a" * 50

    def test_build_chunk_request_final_chunk(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        upload._resumable_url = "http://test.local/resumable_session"
        upload._total_bytes = 100
        upload._bytes_uploaded = 50

        # Upload final 50 bytes
        method, url, headers, body = upload.build_chunk_request(b"b" * 50)
        assert method == "POST"
        assert url == "http://test.local/resumable_session"
        assert (
            headers[_common.UPLOAD_COMMAND_HEADER]
            == f"{_common.UploadCommand.UPLOAD}, {_common.UploadCommand.FINALIZE}"
        )
        assert headers[_common.UPLOAD_OFFSET_HEADER] == "50"
        assert body == b"b" * 50

    def test_build_chunk_request_unknown_size_final(self):
        upload = _upload.ResumableUpload("http://test.local/upload", chunk_size=100)
        upload._resumable_url = "http://test.local/resumable_session"
        upload._total_bytes = None
        upload._bytes_uploaded = 0

        # Upload a chunk smaller than chunk_size, implying it's the final chunk
        method, url, headers, body = upload.build_chunk_request(b"c" * 50)
        assert method == "POST"
        assert (
            headers[_common.UPLOAD_COMMAND_HEADER]
            == f"{_common.UploadCommand.UPLOAD}, {_common.UploadCommand.FINALIZE}"
        )

    def test_build_chunk_request_explicit_final(self):
        upload = _upload.ResumableUpload("http://test.local/upload", chunk_size=100)
        upload._resumable_url = "http://test.local/resumable_session"
        upload._total_bytes = None
        upload._bytes_uploaded = 0

        # Upload an exact-size chunk but signal final explicitly
        method, url, headers, body = upload.build_chunk_request(b"d" * 100, final=True)
        assert method == "POST"
        assert (
            headers[_common.UPLOAD_COMMAND_HEADER]
            == f"{_common.UploadCommand.UPLOAD}, {_common.UploadCommand.FINALIZE}"
        )

    def test_process_chunk_response_active(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        upload._resumable_url = "http://test.local/resumable_session"

        headers = {_common.UPLOAD_STATUS_HEADER: _common.UploadStatus.ACTIVE}
        upload.process_chunk_response(200, headers, 50)

        assert not upload.invalid
        assert not upload.finished
        assert upload.bytes_uploaded == 50

    def test_process_chunk_response_final(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        upload._resumable_url = "http://test.local/resumable_session"

        headers = {_common.UPLOAD_STATUS_HEADER: _common.UploadStatus.FINAL}
        upload.process_chunk_response(200, headers, 50)

        assert not upload.invalid
        assert upload.finished
        assert upload.bytes_uploaded == 50

    def test_process_chunk_response_transient_error(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        upload._resumable_url = "http://test.local/resumable_session"

        upload.process_chunk_response(503, {}, 50)

        # Ensure that transient errors do not invalidate the upload state,
        # allowing the I/O layer to issue a recovery query.
        assert not upload.invalid
        assert not upload.finished
        assert upload.bytes_uploaded == 0

    def test_build_recovery_request(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        upload._resumable_url = "http://test.local/resumable_session"

        method, url, headers, body = upload.build_recovery_request()
        assert method == "POST"
        assert url == "http://test.local/resumable_session"
        assert headers[_common.UPLOAD_COMMAND_HEADER] == _common.UploadCommand.QUERY
        assert body == b""

    def test_process_recovery_response_active(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        upload._resumable_url = "http://test.local/resumable_session"

        headers = {
            _common.UPLOAD_STATUS_HEADER: _common.UploadStatus.ACTIVE,
            _common.UPLOAD_SIZE_RECEIVED_HEADER: "123",
        }
        bytes_uploaded = upload.process_recovery_response(200, headers)

        assert bytes_uploaded == 123
        assert upload.bytes_uploaded == 123
        assert not upload.finished

    def test_process_recovery_response_final(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        upload._resumable_url = "http://test.local/resumable_session"

        headers = {_common.UPLOAD_STATUS_HEADER: _common.UploadStatus.FINAL}
        upload.process_recovery_response(200, headers)

        assert upload.finished

    def test_process_initiate_error(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        upload.process_initiate_error(Exception("Test error"))
        assert upload.invalid

    def test_process_chunk_error_recoverable(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        exc = exceptions.GoogleAPICallError("Recoverable")
        exc.code = 400

        assert upload.process_chunk_error(exc)
        assert not upload.invalid

    def test_process_chunk_error_non_recoverable(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        exc = exceptions.GoogleAPICallError("Non-recoverable")
        exc.code = 500

        assert not upload.process_chunk_error(exc)
        assert upload.invalid

    def test_process_recovery_error(self):
        upload = _upload.ResumableUpload("http://test.local/upload")
        upload.process_recovery_error(Exception("Test error"))
        assert upload.invalid
