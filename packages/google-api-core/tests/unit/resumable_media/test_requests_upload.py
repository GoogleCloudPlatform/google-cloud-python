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
import io
import pytest
import requests
import responses


from google.api_core import exceptions
from google.api_core.resumable_media import requests_upload


def test_resumable_upload_status():
    status = requests_upload.ResumableUploadStatus("http://example.com", 100, 50, False)
    assert status.upload_url == "http://example.com"
    assert status.total_bytes == 100
    assert status.bytes_uploaded == 50
    assert status.finished is False


def test_deadline_exceeded():
    deadline = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(
        seconds=1
    )
    upload = requests_upload.RequestsResumableUpload(
        "http://example.com", io.BytesIO(b"data"), deadline=deadline
    )
    with pytest.raises(exceptions.DeadlineExceeded):
        upload._check_deadline()


@responses.activate
def test_happy_path_upload(caplog):
    import logging

    caplog.set_level(
        logging.DEBUG, logger="google.api_core.resumable_media.requests_upload"
    )

    initial_url = "http://example.com/start"
    session_url = "http://example.com/session/123"
    data = b"hello world"
    stream = io.BytesIO(data)

    # Mock Start
    responses.add(
        responses.POST,
        initial_url,
        status=200,
        headers={"X-Goog-Upload-Status": "active", "X-Goog-Upload-URL": session_url},
        body="",
    )

    # Mock Upload & Finalize
    responses.add(
        responses.POST,
        session_url,
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body="Success",
    )

    session = requests.Session()
    response = requests_upload.make_resumable_upload(
        transport=session,
        request_body="test-initiate-metadata",
        stream=stream,
        upload_url=initial_url,
        size=len(data),
        content_type="text/plain",
        chunk_size=1024,
    )

    assert response is not None
    assert response.status_code == 200
    assert response.text == "Success"
    assert len(responses.calls) == 2
    assert (
        responses.calls[0].request.headers["X-Goog-Upload-Command"].lower() == "start"
    )
    assert (
        responses.calls[1].request.headers["X-Goog-Upload-Command"].lower()
        == "upload, finalize"
    )

    # Check that the initiation and chunk response logs are successfully written without raising exceptions
    assert f"HTTP Request: POST {initial_url}" in caplog.text
    assert "Body: test-initiate-metadata" in caplog.text
    assert f"HTTP Request: POST {session_url}" in caplog.text
    assert "HTTP Response: 200" in caplog.text
    assert "Body: Success" in caplog.text


@responses.activate
def test_upload_with_retry():
    initial_url = "http://example.com/start"
    session_url = "http://example.com/session/123"
    data = b"part1"
    stream = io.BytesIO(data)

    responses.add(
        responses.POST,
        initial_url,
        status=200,
        headers={"X-Goog-Upload-Status": "active", "X-Goog-Upload-URL": session_url},
        body="",
    )

    # Mock 503 then 200 for the same request
    responses.add(responses.POST, session_url, status=503, body="")
    responses.add(
        responses.POST,
        session_url,
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body="Done",
    )

    session = requests.Session()
    response = requests_upload.make_resumable_upload(
        transport=session,
        request_body="",
        stream=stream,
        upload_url=initial_url,
        size=len(data),
        chunk_size=10,
    )

    assert response is not None
    assert response.status_code == 200
    assert response.text == "Done"
    assert len(responses.calls) == 3


@responses.activate
def test_upload_with_recovery_query():
    initial_url = "http://example.com/start"
    session_url = "http://example.com/session/123"
    data = b"0123456789"
    stream = io.BytesIO(data)

    responses.add(
        responses.POST,
        initial_url,
        status=200,
        headers={"X-Goog-Upload-Status": "active", "X-Goog-Upload-URL": session_url},
        body="",
    )

    # Fatal error
    responses.add(
        responses.POST,
        session_url,
        status=400,
        headers={},
        body="",
    )

    # Recovery Query
    responses.add(
        responses.POST,
        session_url,
        status=200,
        headers={"X-Goog-Upload-Status": "active", "X-Goog-Upload-Size-Received": "0"},
        body="",
    )

    # Final Upload
    responses.add(
        responses.POST,
        session_url,
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body="Success",
    )

    session = requests.Session()
    response = requests_upload.make_resumable_upload(
        transport=session,
        request_body="",
        stream=stream,
        upload_url=initial_url,
        size=len(data),
        chunk_size=10,
    )

    assert response is not None
    assert response.status_code == 200
    assert response.text == "Success"
    assert len(responses.calls) == 4
    assert (
        responses.calls[2].request.headers["X-Goog-Upload-Command"].lower() == "query"
    )


@responses.activate
def test_interruption_and_query_recovery_mid_stream():
    initial_url = "http://example.com/start"
    session_url = "http://example.com/session/123"
    data = b"0123456789"
    stream = io.BytesIO(data)

    responses.add(
        responses.POST,
        initial_url,
        status=200,
        headers={"X-Goog-Upload-Status": "active", "X-Goog-Upload-URL": session_url},
        body="",
    )

    # 1. First chunk (0-4) succeeds. Note: The chunk boundary is 5
    responses.add(
        responses.POST,
        session_url,
        status=200,
        headers={"X-Goog-Upload-Status": "active"},
        body="",
    )

    # 2. Second chunk (5-9) fails fatally
    responses.add(
        responses.POST,
        session_url,
        status=400,
        body="",
    )

    # 3. Query reports 5 bytes received
    responses.add(
        responses.POST,
        session_url,
        status=200,
        headers={"X-Goog-Upload-Status": "active", "X-Goog-Upload-Size-Received": "5"},
        body="",
    )

    # 4. Resume from 5 succeeds
    responses.add(
        responses.POST,
        session_url,
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body="Final Success",
    )

    session = requests.Session()
    response = requests_upload.make_resumable_upload(
        transport=session,
        request_body="",
        stream=stream,
        upload_url=initial_url,
        size=len(data),
        chunk_size=5,
    )

    assert response is not None
    assert response.status_code == 200
    assert response.text == "Final Success"
    assert stream.tell() == 10


@responses.activate
def test_logging_success_path(caplog):
    caplog.set_level("DEBUG")
    initial_url = "http://example.com/start"
    session_url = "http://example.com/session/123"
    data = b"test data"
    stream = io.BytesIO(data)

    responses.add(
        responses.POST,
        initial_url,
        status=200,
        headers={"X-Goog-Upload-Status": "active", "X-Goog-Upload-URL": session_url},
        body="",
    )
    responses.add(
        responses.POST,
        session_url,
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body="Final Success",
    )

    session = requests.Session()
    requests_upload.make_resumable_upload(
        transport=session,
        request_body="metadata",
        stream=stream,
        upload_url=initial_url,
        size=len(data),
        chunk_size=1024,
    )

    # Check for initiation request logs
    assert f"HTTP Request: POST {initial_url}" in caplog.text
    assert "'start'" in caplog.text or "'X-Goog-Upload-Command': 'start'" in caplog.text
    assert "Body: metadata" in caplog.text

    # Check for initiate response logs
    assert "HTTP Response: 200" in caplog.text
    assert "http://example.com/session/123" in caplog.text

    # Check for upload/finalize request logs
    assert f"HTTP Request: POST {session_url}" in caplog.text

    # Check for final response logs
    assert "'final'" in caplog.text.lower() or "final" in caplog.text.lower()
    assert "Body: Final Success" in caplog.text


@responses.activate
def test_make_resumable_upload_with_custom_headers(caplog):
    caplog.set_level("DEBUG")
    initial_url = "http://example.com/start"
    session_url = "http://example.com/session/123"
    data = b"test data"
    stream = io.BytesIO(data)
    custom_headers = [("X-Custom-Header", "CustomValue")]

    responses.add(
        responses.POST,
        initial_url,
        status=200,
        headers={"X-Goog-Upload-Status": "active", "X-Goog-Upload-URL": session_url},
        body="",
    )
    responses.add(
        responses.POST,
        session_url,
        status=200,
        headers={"X-Goog-Upload-Status": "final"},
        body="Final Success",
    )

    session = requests.Session()
    requests_upload.make_resumable_upload(
        transport=session,
        request_body="metadata",
        stream=stream,
        upload_url=initial_url,
        size=len(data),
        chunk_size=1024,
        headers=custom_headers,
    )

    # Check for initiation request logs containing the custom header
    assert f"HTTP Request: POST {initial_url}" in caplog.text
    assert "'X-Custom-Header': 'CustomValue'" in caplog.text

    # Check for upload/finalize request logs NOT containing the custom header
    assert f"HTTP Request: POST {session_url}" in caplog.text
    assert caplog.text.count("'X-Custom-Header': 'CustomValue'") == 1
