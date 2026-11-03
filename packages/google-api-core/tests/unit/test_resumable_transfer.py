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
from typing import Union
from unittest import mock

import pytest
import requests
from google.protobuf import empty_pb2

import google.api_core.retry
from google.api_core import exceptions
from google.api_core.resumable_transfer import (
    DEFAULT_CHUNK_SIZE,
    MissingStatusHeaderError,
    ProgressState,
    ResumableUploadConfig,
    ResumableUploadSession,
    TransferStalledError,
    UnseekableStreamError,
    UploadCancelledError,
    UploadProgress,
    common,
    upload,
    upload_state,
)
from tests.helpers import EchoResponse


class DummyResponse:
    """Mock response class representing a deserialized protobuf message."""

    def __init__(self, name: str, size: int) -> None:
        """Initializes a DummyResponse.

        Args:
            name: Resource name string.
            size: Resource size in bytes.
        """
        self.name = name
        self.size = size

    @classmethod
    def from_json(cls, data: Union[str, bytes]) -> "DummyResponse":
        """Deserializes JSON payload into a DummyResponse instance.

        Args:
            data: JSON byte string or text.

        Returns:
            A DummyResponse instance.
        """
        import json

        d = json.loads(data.decode("utf-8") if isinstance(data, bytes) else data)
        return cls(name=d.get("name", ""), size=d.get("size", 0))


# =====================================================================
# 1. Common Constants and Error Types
# =====================================================================


def test_common_constants():
    assert DEFAULT_CHUNK_SIZE == 10 * 1024 * 1024
    assert common.HEADER_PROTOCOL == "X-Goog-Upload-Protocol"
    assert common.HEADER_COMMAND == "X-Goog-Upload-Command"
    assert common.HEADER_STATUS == "X-Goog-Upload-Status"
    assert common.HEADER_URL == "X-Goog-Upload-URL"
    assert common.HEADER_OFFSET == "X-Goog-Upload-Offset"
    assert common.HEADER_SIZE_RECEIVED == "X-Goog-Upload-Size-Received"
    assert common.PROTOCOL_RESUMABLE == "resumable"

    assert common._Command.START == "start"
    assert common._Command.UPLOAD == "upload"
    assert common._Command.FINALIZE == "finalize"
    assert common._Command.QUERY == "query"
    assert common._Command.CANCEL == "cancel"

    assert common._Status.ACTIVE == "active"
    assert common._Status.FINAL == "final"
    assert common._Status.CANCELLED == "cancelled"

    assert ProgressState.STARTED == "started"
    assert ProgressState.UPLOADING == "uploading"
    assert ProgressState.RECOVERING == "recovering"
    assert ProgressState.OFFSET_RECEIVED == "offset received"
    assert ProgressState.FINALIZED == "finalized"


def test_upload_progress_dataclass():
    prog = UploadProgress(
        upload_url="https://upload.example.com/session123",
        chunk_size=1024,
        bytes_uploaded=512,
        total_bytes=2048,
        state=ProgressState.UPLOADING,
    )
    assert prog.upload_url == "https://upload.example.com/session123"
    assert prog.chunk_size == 1024
    assert prog.bytes_uploaded == 512
    assert prog.total_bytes == 2048
    assert prog.state == ProgressState.UPLOADING


def test_exception_hierarchy():
    assert issubclass(TransferStalledError, exceptions.GoogleAPICallError)
    assert issubclass(UnseekableStreamError, exceptions.GoogleAPICallError)
    assert issubclass(UploadCancelledError, exceptions.GoogleAPICallError)
    assert issubclass(MissingStatusHeaderError, exceptions.GoogleAPICallError)
    assert exceptions.TransferStalledError is TransferStalledError
    assert exceptions.UnseekableStreamError is UnseekableStreamError
    assert exceptions.UploadCancelledError is UploadCancelledError
    assert exceptions.MissingStatusHeaderError is MissingStatusHeaderError


# =====================================================================
# 2. Pure Sans-I/O State Machine (upload_state.py)
# =====================================================================


def test_protocol_state_start_request():
    state = upload_state._ProtocolState(upload_url="https://api.example.com/start")
    method, url, headers, payload = state.build_start_request(
        body='{"name": "test"}',
        headers=[("X-Custom", "val")],
        content_type="text/plain",
        size=1000,
    )

    assert method == "POST"
    assert url == "https://api.example.com/start"
    assert headers["X-Goog-Upload-Protocol"] == "resumable"
    assert headers["X-Goog-Upload-Command"] == "start"
    assert headers["X-Goog-Upload-Header-Content-Type"] == "text/plain"
    assert headers["X-Goog-Upload-Header-Content-Length"] == "1000"
    assert headers["X-Custom"] == "val"
    assert payload == b'{"name": "test"}'


def test_protocol_state_process_start_response():
    state = upload_state._ProtocolState(upload_url="https://api.example.com/start")
    headers = {
        "X-Goog-Upload-Status": "active",
        "X-Goog-Upload-URL": "https://upload.example.com/resumable-id",
        "X-Goog-Upload-Chunk-Granularity": "262144",
    }
    url = state.process_start_response(200, headers)
    assert url == "https://upload.example.com/resumable-id"
    assert state.upload_url == "https://upload.example.com/resumable-id"
    assert state._chunk_granularity == 262144


def test_protocol_state_start_response_missing_status():
    state = upload_state._ProtocolState(upload_url="https://api.example.com/start")
    headers = {"X-Goog-Upload-URL": "https://upload.example.com/resumable-id"}
    with pytest.raises(MissingStatusHeaderError):
        state.process_start_response(200, headers)


def test_protocol_state_start_response_missing_url():
    state = upload_state._ProtocolState(upload_url="https://api.example.com/start")
    headers = {"X-Goog-Upload-Status": "active"}
    with pytest.raises(ValueError, match="Server did not return"):
        state.process_start_response(200, headers)


def test_protocol_state_granularity_alignment():
    state = upload_state._ProtocolState(chunk_size=500)
    assert state.chunk_size == 500
    state._chunk_granularity = 256
    # 500 rounded up to multiple of 256 is 512
    assert state.chunk_size == 512


def test_protocol_state_chunk_request_and_response():
    state = upload_state._ProtocolState(upload_url="https://upload.example.com/session")

    # First chunk: not last
    method, url, headers, payload = state.build_chunk_request(
        data=b"0123456789", is_last_chunk=False
    )
    assert headers["X-Goog-Upload-Command"] == "upload"
    assert headers["X-Goog-Upload-Offset"] == "0"
    assert payload == b"0123456789"

    state.process_chunk_response(200, {"X-Goog-Upload-Status": "active"}, 10)
    assert state.bytes_uploaded == 10
    assert not state.finished

    # Second chunk: last chunk
    method, url, headers, payload = state.build_chunk_request(
        data=b"abcdef", is_last_chunk=True, content_type="text/plain"
    )
    assert headers["X-Goog-Upload-Command"] == "upload, finalize"
    assert headers["X-Goog-Upload-Offset"] == "10"
    assert headers["Content-Type"] == "text/plain"

    state.process_chunk_response(200, {"X-Goog-Upload-Status": "final"}, 6)
    assert state.bytes_uploaded == 16
    assert state.finished


def test_protocol_state_chunk_missing_status_header():
    state = upload_state._ProtocolState(upload_url="https://upload.example.com/session")
    with pytest.raises(MissingStatusHeaderError):
        state.process_chunk_response(200, {}, 10)


def test_protocol_state_chunk_cancelled_status():
    state = upload_state._ProtocolState(upload_url="https://upload.example.com/session")
    with pytest.raises(UploadCancelledError):
        state.process_chunk_response(200, {"X-Goog-Upload-Status": "cancelled"}, 10)
    assert state.invalid


def test_protocol_state_query_and_cancel():
    state = upload_state._ProtocolState(upload_url="https://upload.example.com/session")
    method, url, headers, payload = state.build_query_request()
    assert headers["X-Goog-Upload-Command"] == "query"

    received = state.process_query_response(
        200, {"X-Goog-Upload-Status": "active", "X-Goog-Upload-Size-Received": "1024"}
    )
    assert received == 1024
    assert state.bytes_uploaded == 1024

    # query with unknown status
    state2 = upload_state._ProtocolState(
        upload_url="https://upload.example.com/session"
    )
    received2 = state2.process_query_response(200, {"X-Goog-Upload-Status": "unknown"})
    assert received2 == 0

    method, url, headers, payload = state.build_cancel_request()
    assert headers["X-Goog-Upload-Command"] == "cancel"
    state.process_cancel_response(200, {})
    assert state.invalid


# =====================================================================
# 3. ResumableUploadConfig Sensible Defaults
# =====================================================================


def test_resumable_upload_config_defaults():
    config = ResumableUploadConfig()
    assert config.chunk_size == 10 * 1024 * 1024
    assert config.stall_minimum_rate == 64 * 1024
    assert config.stall_timeout == 120.0
    assert config.headers is None
    assert config.deadline is None


def test_resumable_upload_config_headers():
    config1 = ResumableUploadConfig(
        headers={"X-Test": "1"},
    )
    assert config1.start_headers == [("X-Test", "1")]

    config2 = ResumableUploadConfig(
        headers=[("X-Test", "2")],
    )
    assert config2.start_headers == [("X-Test", "2")]


# =====================================================================
# 4. Synchronous ResumableUploadSession (upload.py)
# =====================================================================


def test_sync_upload_direct_execution():
    session_transport = mock.create_autospec(requests.Session, instance=True)

    # 1. Start response
    start_resp = mock.Mock()
    start_resp.ok = True
    start_resp.status_code = 200
    start_resp.headers = {
        "X-Goog-Upload-Status": "active",
        "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
    }

    # 2. Chunk response
    chunk_resp = mock.Mock()
    chunk_resp.ok = True
    chunk_resp.status_code = 200
    chunk_resp.headers = {"X-Goog-Upload-Status": "final"}
    chunk_resp.content = b'{"name": "done.txt", "size": 11}'

    session_transport.request.side_effect = [start_resp, chunk_resp]

    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=session_transport,
        response_type=DummyResponse,
    )

    payload = b"Hello world"
    result = session.upload(stream=payload, request_body='{"name": "test"}')

    assert isinstance(result, DummyResponse)
    assert result.name == "done.txt"
    assert result.size == 11
    assert session.finished is True
    assert session.bytes_uploaded == 11
    assert session.upload_url == "https://upload.example.com/resumable-123"
    assert session.response == result


def test_sync_upload_iterative_progress():
    session_transport = mock.create_autospec(requests.Session, instance=True)

    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
        },
    )
    chunk1_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "active"},
    )
    chunk2_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b'{"name": "stream.txt", "size": 8}',
    )

    session_transport.request.side_effect = [start_resp, chunk1_resp, chunk2_resp]

    config = ResumableUploadConfig(chunk_size=4)
    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=session_transport,
        response_type=DummyResponse,
    )

    progress_events = list(session.iter_upload(stream=b"12345678"))
    assert len(progress_events) == 3
    assert progress_events[0].state == ProgressState.STARTED
    assert progress_events[1].state == ProgressState.UPLOADING
    assert progress_events[1].bytes_uploaded == 4
    assert progress_events[2].state == ProgressState.FINALIZED
    assert progress_events[2].bytes_uploaded == 8

    assert session.response.name == "stream.txt"
    assert session.response.size == 8


def _make_single_chunk_sync_transport() -> mock.Mock:
    """Builds a mock requests.Session returning a start response and a final chunk response."""
    session_transport = mock.create_autospec(requests.Session, instance=True)
    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
        },
    )
    chunk_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b"",
    )
    session_transport.request.side_effect = [start_resp, chunk_resp]
    return session_transport


def test_sync_upload_uses_session_request_body():
    # A request_body supplied to the constructor is sent with the start
    # request when upload() is called without an explicit request_body.
    session_transport = _make_single_chunk_sync_transport()
    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=session_transport,
        request_body='{"name": "from-init"}',
    )

    session.upload(stream=b"payload")

    start_call = session_transport.request.call_args_list[0]
    assert start_call.kwargs["data"] == b'{"name": "from-init"}'
    assert start_call.kwargs["headers"]["X-Goog-Upload-Command"] == "start"


def test_sync_iter_upload_uses_session_request_body():
    session_transport = _make_single_chunk_sync_transport()
    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=session_transport,
        request_body=b'{"name": "from-init-bytes"}',
    )

    list(session.iter_upload(stream=b"payload"))

    start_call = session_transport.request.call_args_list[0]
    assert start_call.kwargs["data"] == b'{"name": "from-init-bytes"}'


@pytest.mark.parametrize(
    "override, expected",
    [
        ('{"name": "override"}', b'{"name": "override"}'),
        (b'{"name": "override-bytes"}', b'{"name": "override-bytes"}'),
        ("", b""),
    ],
)
def test_sync_upload_request_body_argument_overrides_session_default(
    override, expected
):
    # An explicit per-call request_body (including an empty one) takes
    # precedence over the request_body supplied to the constructor.
    session_transport = _make_single_chunk_sync_transport()
    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=session_transport,
        request_body='{"name": "from-init"}',
    )

    session.upload(stream=b"payload", request_body=override)

    start_call = session_transport.request.call_args_list[0]
    assert start_call.kwargs["data"] == expected


def test_sync_upload_request_body_positional_override():
    # request_body stays the second positional parameter, so callers that
    # pass it positionally are not broken by the constructor default.
    session_transport = _make_single_chunk_sync_transport()
    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=session_transport,
        request_body='{"name": "from-init"}',
    )

    session.upload(b"payload", '{"name": "positional"}')

    start_call = session_transport.request.call_args_list[0]
    assert start_call.kwargs["data"] == b'{"name": "positional"}'


def test_sync_upload_request_body_defaults_to_empty():
    # Without a request_body on the constructor or the call, the start
    # request carries an empty payload.
    session_transport = _make_single_chunk_sync_transport()
    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=session_transport,
    )

    session.upload(stream=b"payload")

    start_call = session_transport.request.call_args_list[0]
    assert start_call.kwargs["data"] == b""


def test_sync_resume():
    session_transport = mock.create_autospec(requests.Session, instance=True)

    # 1. Query response returns offset 5
    query_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "5",
        },
    )
    # 2. Remaining chunk response
    chunk_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b'{"name": "resumed.txt", "size": 10}',
    )
    session_transport.request.side_effect = [query_resp, chunk_resp]

    session = ResumableUploadSession(response_type=DummyResponse)

    stream = io.BytesIO(b"0123456789")
    resp = session.resume(
        upload_url="https://upload.example.com/resumable-123",
        stream=stream,
        transport=session_transport,
    )

    assert isinstance(resp, DummyResponse)
    assert resp.name == "resumed.txt"
    assert session.bytes_uploaded == 10
    assert session.finished is True


def test_sync_iter_resume():
    """Verifies streaming progress during upload resumption."""
    session_transport = mock.create_autospec(requests.Session, instance=True)

    query_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "5",
        },
    )
    chunk_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b'{"name": "iter_resumed.txt", "size": 10}',
    )
    session_transport.request.side_effect = [query_resp, chunk_resp]

    session = ResumableUploadSession(response_type=DummyResponse)

    stream = io.BytesIO(b"0123456789")
    progress_list = list(
        session.iter_resume(
            upload_url="https://upload.example.com/resumable-123",
            stream=stream,
            transport=session_transport,
        )
    )

    assert session.response.name == "iter_resumed.txt"
    assert session.bytes_uploaded == 10
    assert session.finished is True
    assert len(progress_list) == 2
    assert progress_list[0].state == ProgressState.OFFSET_RECEIVED
    assert progress_list[1].state == ProgressState.FINALIZED


def test_sync_recoverable_status_code_triggers_offset_recovery():
    session_transport = mock.create_autospec(requests.Session, instance=True)

    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
        },
    )
    # First chunk upload fails with 400 (recoverable Category 2)
    err400_resp = mock.Mock(
        ok=False,
        status_code=400,
        headers={},
    )
    err400_resp.json.return_value = {"error": {"message": "Bad Request", "details": []}}
    err400_resp.text = '{"error": {"message": "Bad Request"}}'
    err400_resp.content = err400_resp.text.encode("utf-8")
    # Recovery query returns offset 0
    query_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "0",
        },
    )
    # Retry chunk upload succeeds
    success_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b'{"name": "recovered.txt", "size": 5}',
    )

    session_transport.request.side_effect = [
        start_resp,
        err400_resp,
        query_resp,
        success_resp,
    ]

    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=DummyResponse,
        transport=session_transport,
    )

    resp = session.upload(stream=b"12345")
    assert resp.name == "recovered.txt"
    assert session.bytes_uploaded == 5


def test_sync_exceptions_carry_upload_url_and_chunk_size():
    session_transport = mock.create_autospec(requests.Session, instance=True)

    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
        },
    )
    # Fatal 403 error on chunk upload
    err403_resp = mock.Mock(
        ok=False,
        status_code=403,
        headers={},
    )
    err403_resp.json.return_value = {"error": {"message": "Forbidden", "details": []}}
    err403_resp.text = '{"error": {"message": "Forbidden"}}'
    err403_resp.content = err403_resp.text.encode("utf-8")
    session_transport.request.side_effect = [start_resp, err403_resp]

    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=session_transport,
    )

    with pytest.raises(exceptions.GoogleAPICallError) as exc_info:
        session.upload(stream=b"data")

    err = exc_info.value
    assert err.upload_url == "https://upload.example.com/resumable-123"
    assert err.chunk_size == session.chunk_size


def test_sync_unseekable_stream_error_on_preceding_offset():
    session_transport = mock.create_autospec(requests.Session, instance=True)

    query_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "50",
        },
    )
    session_transport.request.side_effect = [query_resp]

    session = ResumableUploadSession(
        config=ResumableUploadConfig(),
        transport=session_transport,
    )

    # Mock an unseekable stream
    unseekable = mock.Mock(spec=io.RawIOBase)
    unseekable.seekable.return_value = False

    with pytest.raises(UnseekableStreamError) as exc_info:
        session.resume(
            upload_url="https://upload.example.com/resumable-123",
            stream=unseekable,
            transport=session_transport,
        )

    assert exc_info.value.upload_url == "https://upload.example.com/resumable-123"


def test_sync_stall_timeout(monkeypatch):
    session_transport = mock.create_autospec(requests.Session, instance=True)

    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
        },
    )
    session_transport.request.side_effect = [
        start_resp,
        requests.exceptions.Timeout("Read timed out"),
    ]

    # Configure stall control with 0.1s timeout
    config = ResumableUploadConfig(
        stall_minimum_rate=1024,
        stall_timeout=0.1,
    )
    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=session_transport,
    )

    clock_vals = iter([0.0, 0.5, 0.5])
    monkeypatch.setattr(upload, "_monotonic_clock", lambda: next(clock_vals))

    with pytest.raises(TransferStalledError) as exc_info:
        session.upload(stream=b"test data")

    assert exc_info.value.upload_url == "https://upload.example.com/resumable-123"


def test_sync_multi_chunk_small_lag_does_not_false_stall(monkeypatch):
    """Verifies that a small lag on chunk 1 does not cause chunk 2's normal transfer
    duration to count toward stall_timeout and falsely raise TransferStalledError."""
    session_transport = mock.create_autospec(requests.Session, instance=True)

    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
        },
    )
    chunk1_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "active"},
        content=b"",
    )
    chunk2_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b'{"name": "ok.txt", "size": 20480}',
    )
    responses = iter([start_resp, chunk1_resp, chunk2_resp])
    current_time = [0.0]

    def handle_request(*args, **kwargs):
        resp = next(responses)
        if resp is not start_resp:
            current_time[0] += 10.5
        return resp

    session_transport.request.side_effect = handle_request
    monkeypatch.setattr(upload, "_monotonic_clock", lambda: current_time[0])

    # Each 10240-byte chunk has expected_sec = 10240 / 1024 = 10.0s, and stall_timeout = 10.0s.
    # Chunk 1 takes 10.5s (t=0.0 -> 10.5, lag=0.5s).
    # Chunk 2 takes 10.5s (t=10.5 -> 21.0, lag=0.5s).
    # Cumulative lag is only 1.0s (< 10.0s stall_timeout), even though wall-clock time
    # elapsed since chunk 1 started lagging is 11.0s (>= 10.0s).
    config = ResumableUploadConfig(
        chunk_size=10240,
        stall_minimum_rate=1024,
        stall_timeout=10.0,
    )
    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=session_transport,
        response_type=DummyResponse,
    )

    result = session.upload(stream=b"x" * 20480)
    assert result.name == "ok.txt"
    assert session._aggregate_lag == pytest.approx(1.0)


def test_sync_cancel():
    session_transport = mock.create_autospec(requests.Session, instance=True)
    cancel_resp = mock.Mock(ok=True, status_code=200, headers={})
    session_transport.request.return_value = cancel_resp

    session = ResumableUploadSession(
        upload_url="https://upload.example.com/resumable-123",
        transport=session_transport,
    )
    session.cancel()
    assert session._state.invalid is True


def test_sync_response_type_proto_message():
    session_transport = mock.create_autospec(requests.Session, instance=True)
    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
        },
    )
    chunk_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b'{"content": "proto_payload"}',
    )
    session_transport.request.side_effect = [start_resp, chunk_resp]

    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=EchoResponse,
        transport=session_transport,
    )
    resp = session.upload(stream=b"payload")
    assert isinstance(resp, EchoResponse)
    assert resp.content == "proto_payload"


def test_sync_response_type_protobuf_message():
    session_transport = mock.create_autospec(requests.Session, instance=True)
    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
        },
    )
    chunk_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b"{}",
    )
    session_transport.request.side_effect = [start_resp, chunk_resp]

    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=empty_pb2.Empty,
        transport=session_transport,
    )
    resp = session.upload(stream=b"payload")
    assert isinstance(resp, empty_pb2.Empty)


def test_sync_response_type_callable():
    session_transport = mock.create_autospec(requests.Session, instance=True)
    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
        },
    )
    chunk_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b"custom_payload",
    )
    session_transport.request.side_effect = [start_resp, chunk_resp]

    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=lambda c: c.decode("utf-8").upper(),
        transport=session_transport,
    )
    resp = session.upload(stream=b"payload")
    assert resp == "CUSTOM_PAYLOAD"


def test_sync_response_type_raw_response():
    session_transport = mock.create_autospec(requests.Session, instance=True)
    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
        },
    )
    chunk_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b"raw_content",
    )
    session_transport.request.side_effect = [start_resp, chunk_resp]

    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        response_type=None,
        transport=session_transport,
    )
    resp = session.upload(stream=b"payload")
    assert resp == b"raw_content"


def test_sync_retry_predicate_allows_timeout_with_stall_control():
    config = ResumableUploadConfig(stall_minimum_rate=1024, stall_timeout=1.0)
    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
    )
    predicate = session._get_retry_predicate()
    assert predicate(requests.exceptions.Timeout("Read timed out")) is True


@pytest.mark.parametrize("invalid_stream", ["invalid_string", {"key": "value"}, 12345])
def test_sync_upload_rejects_invalid_stream_types(invalid_stream):
    session_transport = mock.create_autospec(requests.Session, instance=True)
    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        transport=session_transport,
    )
    with pytest.raises(TypeError, match="Unsupported stream type"):
        session.upload(stream=invalid_stream)


def test_upload_state_properties():
    state = upload_state._ProtocolState("https://api.example.com/init", chunk_size=500)
    assert state.initial_url == "https://api.example.com/init"
    assert state.upload_url == "https://api.example.com/init"
    assert state.bytes_uploaded == 0
    assert state.total_bytes is None
    assert state.finished is False
    assert state.invalid is False
    assert state.chunk_size == 500

    # With granularity alignment
    state._chunk_granularity = 256
    assert state.chunk_size == 512


def test_upload_state_start_errors():
    empty_state = upload_state._ProtocolState()
    with pytest.raises(
        ValueError, match="upload_url must be provided to start an upload"
    ):
        empty_state.build_start_request()

    state = upload_state._ProtocolState("https://api.example.com/init")
    with pytest.raises(ValueError, match="Start command failed with status 500"):
        state.process_start_response(500, {})
    assert state.invalid is True

    state2 = upload_state._ProtocolState("https://api.example.com/init")
    with pytest.raises(ValueError, match="Server did not return"):
        state2.process_start_response(200, {"X-Goog-Upload-Status": "active"})
    assert state2.invalid is True


def test_upload_state_chunk_and_query_errors():
    state = upload_state._ProtocolState()
    with pytest.raises(ValueError, match="Upload session URL not established"):
        state.build_chunk_request(b"data", is_last_chunk=True)

    with pytest.raises(ValueError, match="Upload session URL not established"):
        state.build_query_request()

    with pytest.raises(ValueError, match="Upload session URL not established"):
        state.build_cancel_request()

    # process_chunk_response with non-200/201 status code
    state.process_chunk_response(503, {}, 10)
    assert state.bytes_uploaded == 0

    # process_query_response with non-200/201 status code
    with pytest.raises(ValueError, match="Query recovery failed with status 500"):
        state.process_query_response(500, {})
    assert state.invalid is True

    # process_query_response with final status
    state3 = upload_state._ProtocolState("https://api.example.com/init")
    state3.process_query_response(200, {"X-Goog-Upload-Status": "final"})
    assert state3.finished is True

    # process_query_response with cancelled status
    state4 = upload_state._ProtocolState("https://api.example.com/init")
    with pytest.raises(UploadCancelledError):
        state4.process_query_response(200, {"X-Goog-Upload-Status": "cancelled"})
    assert state4.invalid is True


def test_sync_upload_session_properties_and_enrichment():
    session_transport = mock.create_autospec(requests.Session, instance=True)
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        transport=session_transport,
    )
    assert session._get_transport(None) is session_transport
    assert session._state.upload_url == "https://api.example.com/init"
    assert session.bytes_uploaded == 0
    assert session._state.total_bytes is None
    assert session.finished is False
    assert session._state.invalid is False

    # Exception without __dict__ does not fail _enrich_exception
    exc_no_dict = Exception()
    session._enrich_exception(exc_no_dict)


def test_sync_upload_session_transport_missing():
    session = ResumableUploadSession(upload_url="https://api.example.com/init")
    with pytest.raises(
        ValueError, match="A requests.Session transport must be provided"
    ):
        session.upload(stream=b"payload")

    with pytest.raises(
        ValueError, match="A requests.Session transport must be provided"
    ):
        session.cancel()


def test_sync_deadline_handling():
    past = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(seconds=10)
    config = ResumableUploadConfig(deadline=past)
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config,
    )
    with pytest.raises(exceptions.DeadlineExceeded):
        session._get_deadline_remaining()

    future_naive = datetime.datetime.now() + datetime.timedelta(hours=1)
    config2 = ResumableUploadConfig(deadline=future_naive)
    session2 = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config2,
    )
    rem = session2._get_deadline_remaining()
    assert rem is not None and rem > 0


def test_sync_retry_predicate_branches():
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
    )
    pred_transfer = session._get_retry_predicate(is_start=False)
    pred_start = session._get_retry_predicate(is_start=True)

    assert pred_transfer(exceptions.DeadlineExceeded("deadline")) is False
    assert pred_transfer(TransferStalledError("stalled")) is False
    assert pred_transfer(UploadCancelledError("cancelled")) is False
    assert pred_transfer(MissingStatusHeaderError("missing")) is True
    assert pred_start(MissingStatusHeaderError("missing")) is False
    assert pred_transfer(requests.exceptions.ConnectionError("conn")) is True
    assert pred_transfer(requests.exceptions.ChunkedEncodingError("chunked")) is True
    assert pred_transfer(exceptions.from_http_status(503, "503")) is True
    assert pred_transfer(exceptions.from_http_status(400, "400")) is True
    assert pred_transfer(exceptions.from_http_status(412, "412")) is True
    assert pred_transfer(exceptions.from_http_status(416, "416")) is True
    assert pred_start(exceptions.from_http_status(400, "400")) is False
    assert pred_start(exceptions.from_http_status(412, "412")) is False
    assert pred_start(exceptions.from_http_status(416, "416")) is False
    assert pred_transfer(exceptions.from_http_status(409, "409")) is False
    assert pred_start(exceptions.from_http_status(409, "409")) is False
    assert pred_transfer(exceptions.from_http_status(403, "403")) is False
    assert pred_transfer(TypeError("other")) is False


def test_sync_reposition_stream_errors():
    session_transport = mock.create_autospec(requests.Session, instance=True)
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        transport=session_transport,
    )

    unseekable = mock.Mock()
    unseekable.seekable.return_value = False
    with pytest.raises(UnseekableStreamError, match="Stream is not seekable"):
        session._reposition_stream_offset(unseekable, 100)

    failing_seek = mock.Mock()
    failing_seek.seekable.return_value = True
    failing_seek.seek.side_effect = OSError("Disk read failure")
    with pytest.raises(UnseekableStreamError, match="Failed to seek stream"):
        session._reposition_stream_offset(failing_seek, 100)


def test_sync_prepare_stream_seekable_and_iterable():
    session_transport = mock.create_autospec(requests.Session, instance=True)
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        transport=session_transport,
    )

    stream_obj, computed_size = session._prepare_stream([b"hello ", b"world"], None)
    assert stream_obj.seekable() is False
    assert stream_obj.read(4) == b"hell"
    assert stream_obj.read(4) == b"o wo"
    assert stream_obj.read(4) == b"rld"
    assert stream_obj.read(4) == b""
    assert computed_size is None

    stream_obj_all, _ = session._prepare_stream([b"hello ", b"world"], None)
    assert stream_obj_all.read() == b"hello world"

    class CustomSeekable:
        def __init__(self, data: bytes):
            self._bio = io.BytesIO(data)

        def read(self, n: int = -1) -> bytes:
            return self._bio.read(n)

        def seek(self, offset: int, whence: int = io.SEEK_SET) -> int:
            return self._bio.seek(offset, whence)

        def tell(self) -> int:
            return self._bio.tell()

        def seekable(self) -> bool:
            return True

    custom = CustomSeekable(b"0123456789")
    custom.seek(2)
    stream_obj2, computed_size2 = session._prepare_stream(custom, None)
    assert computed_size2 == 8
    assert custom.tell() == 2


def test_sync_config_headers():
    cfg_dict = ResumableUploadConfig(headers={"X-Key": "Val"})
    assert cfg_dict.start_headers == [("X-Key", "Val")]

    cfg_list = ResumableUploadConfig(headers=[("X-Key", "Val")])
    assert cfg_list.start_headers == [("X-Key", "Val")]

    cfg_none = ResumableUploadConfig(headers=None)
    assert cfg_none.start_headers is None


def test_sync_cancel_failure_raises():
    session_transport = mock.create_autospec(requests.Session, instance=True)
    err_resp = mock.create_autospec(requests.Response, instance=True)
    err_resp.ok = False
    err_resp.status_code = 500
    err_resp.headers = {}
    err_resp.request = mock.Mock(method="POST", url="https://upload.example.com")
    err_resp.json.return_value = {"error": {"message": "Server Error", "errors": []}}
    session_transport.request.return_value = err_resp

    session = ResumableUploadSession(
        upload_url="https://upload.example.com/resumable-123",
        transport=session_transport,
    )
    with pytest.raises(exceptions.GoogleAPICallError):
        session.cancel()


def test_sync_resume_chunk_size_override():
    session_transport = mock.create_autospec(requests.Session, instance=True)
    query_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "0",
        },
    )
    chunk_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b"done",
    )
    session_transport.request.side_effect = [query_resp, chunk_resp]

    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        transport=session_transport,
    )
    session.resume(
        upload_url="https://upload.example.com/resumable-123",
        stream=b"data",
        chunk_size=1024,
    )
    assert session.chunk_size == 1024


def test_sync_on_progress_and_capture():
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
    )
    session._state._upload_url = "https://api.example.com/init"
    progress_queue = []
    session._notify_progress(
        common.ProgressState.UPLOADING, progress_queue=progress_queue
    )
    assert len(progress_queue) == 1
    assert progress_queue[0].state == common.ProgressState.UPLOADING


def test_sync_naive_deadline_tz():
    naive = datetime.datetime.now() + datetime.timedelta(hours=1)
    config = ResumableUploadConfig(deadline=naive)
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config,
    )
    rem = session._get_deadline_remaining()
    assert rem is not None and rem > 0
    assert session._get_start_timeout() <= rem


def test_sync_get_retry_start_and_override():
    """Verifies how user-supplied Retry objects are resolved and wrapped."""

    class CustomApiError(Exception):
        """Example API-specific transient exception provided by a caller."""

    # -------------------------------------------------------------------------
    # Scenario 1: User provides a custom predicate to retry an API-specific error
    # -------------------------------------------------------------------------
    custom_start_retry = google.api_core.retry.Retry(
        initial=0.5,
        predicate=lambda exc: isinstance(exc, CustomApiError),
    )
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        start_retry=custom_start_retry,
    )
    resolved_start = session._get_retry()

    # Backoff settings (0.5s initial delay) are preserved
    assert resolved_start._initial == 0.5
    # The user's custom exception is retried, while unrelated errors are not
    assert resolved_start._predicate(CustomApiError("rate limit")) is True
    assert resolved_start._predicate(ValueError("invalid input")) is False

    # -------------------------------------------------------------------------
    # Scenario 2: Terminal errors are blocked even if custom predicate returns True
    # -------------------------------------------------------------------------
    overly_broad_retry = google.api_core.retry.Retry(
        initial=0.25,
        predicate=lambda exc: True,
    )
    resolved_override = session._get_retry(retry_override=overly_broad_retry)

    assert resolved_override._initial == 0.25
    # Terminal transfer errors must never be retried, preventing infinite loops
    assert (
        resolved_override._predicate(exceptions.DeadlineExceeded("deadline expired"))
        is False
    )
    assert (
        resolved_override._predicate(exceptions.TransferStalledError("upload stalled"))
        is False
    )

    # -------------------------------------------------------------------------
    # Scenario 3: Category 2 recovery (400, 412, 416, MissingStatusHeaderError)
    # is preserved during chunk transfer
    # -------------------------------------------------------------------------
    default_stream = session._get_streaming_retry()
    assert default_stream.timeout is None

    restrictive_chunk_retry = google.api_core.retry.StreamingRetry(
        initial=0.1,
        predicate=lambda exc: False,
    )
    resolved_chunk = session._get_streaming_retry(
        retry_override=restrictive_chunk_retry
    )

    assert resolved_chunk._initial == 0.1
    # Category 2 recovery triggers (400, 412, 416, and missing status header)
    # must still return True during chunk transfer so the client can query
    # server offset and synchronize state
    assert (
        resolved_chunk._predicate(exceptions.from_http_status(400, "Bad Request"))
        is True
    )
    assert (
        resolved_chunk._predicate(
            exceptions.from_http_status(412, "Precondition Failed")
        )
        is True
    )
    assert (
        resolved_chunk._predicate(
            exceptions.from_http_status(416, "Range Not Satisfiable")
        )
        is True
    )
    missing_header_error = MissingStatusHeaderError("Missing X-Goog-Upload-Status")
    assert resolved_chunk._predicate(missing_header_error) is True
    # Unretriable HTTP status codes (such as 409 Conflict) and non-protocol errors
    # follow the predicate and return False
    assert (
        resolved_chunk._predicate(exceptions.from_http_status(409, "Conflict")) is False
    )
    assert resolved_chunk._predicate(RuntimeError("unexpected crash")) is False


def test_sync_stall_control_with_deadline():
    config = ResumableUploadConfig(
        stall_minimum_rate=1024,
        stall_timeout=10.0,
    )
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config,
    )
    # 512 bytes / 1024 B/s -> expected_sec = 0.5s.
    # With aggregate_lag = 0.0 and stall_timeout = 10.0s:
    # next_chunk_timeout = 0.5 - 0.0 + 10.0 = 10.5s.
    # timeout_override=15.0 exceeds next_chunk_timeout, so it clamps to 10.5s.
    t1 = session._compute_chunk_timeout(512, timeout_override=15.0)
    assert t1 == pytest.approx(10.5)
    # timeout_override=8.0 is below next_chunk_timeout (10.5s), so 8.0s is used
    # directly instead of the default heuristic (max(5.0, 2 * 0.5) = 5.0s).
    assert session._compute_chunk_timeout(512, timeout_override=8.0) == pytest.approx(
        8.0
    )

    # When stall control is disabled, timeout_override is returned as-is.
    session_no_stall = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=ResumableUploadConfig(stall_minimum_rate=0, stall_timeout=0),
    )
    assert session_no_stall._compute_chunk_timeout(
        512, timeout_override=15.0
    ) == pytest.approx(15.0)

    # Overall upload deadline (5s left) caps the per-attempt timeout.
    config2 = ResumableUploadConfig(
        stall_minimum_rate=1024,
        stall_timeout=10.0,
        deadline=datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(seconds=5),
    )
    session2 = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config2,
    )
    t2 = session2._compute_chunk_timeout(512)
    assert t2 <= 5.0

    # If the upload stalls and the overall deadline has already passed,
    # DeadlineExceeded takes precedence over TransferStalledError.
    config3 = ResumableUploadConfig(
        stall_minimum_rate=1024,
        stall_timeout=10.0,
        deadline=datetime.datetime.now(datetime.timezone.utc)
        - datetime.timedelta(seconds=5),
    )
    session3 = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config3,
    )
    with pytest.raises(exceptions.DeadlineExceeded):
        session3._update_stall_control(512, 15.0)

    # 512 bytes / 1024 B/s -> expected_sec = 0.5s. Taking 15.0s yields
    # current_lag = 14.5s, which exceeds stall_timeout (10.0s).
    config4 = ResumableUploadConfig(
        stall_minimum_rate=1024,
        stall_timeout=10.0,
    )
    session4 = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config4,
    )
    session4._state._upload_url = "https://api.example.com/init"
    with pytest.raises(exceptions.TransferStalledError):
        session4._update_stall_control(512, 15.0)

    # 10240 bytes / 1024 B/s -> expected_sec = 10.0s.
    # Taking 10.5s gives current_lag = 10.5 - 10.0 = 0.5s.
    # Only the 0.5s lag counts toward stall_timeout (10.0s), not the full 10.5s,
    # so even across two such chunks (aggregate_lag = 1.0s < 10.0s) the transfer
    # does not stall.
    session5 = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config4,
    )
    session5._state._upload_url = "https://api.example.com/init"
    session5._update_stall_control(10240, 10.5)
    assert session5._aggregate_lag == pytest.approx(0.5)
    session5._update_stall_control(10240, 10.5)
    assert session5._aggregate_lag == pytest.approx(1.0)
    session5._buffered_chunk = memoryview(b"stale")
    session5._reset_transfer_state()
    assert session5._buffered_chunk is None
    assert session5._aggregate_lag == 0.0


def test_sync_update_stall_control_disabled():
    config = ResumableUploadConfig(stall_minimum_rate=0, stall_timeout=10.0)
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config,
    )
    session._update_stall_control(512, 5.0)
    assert session._aggregate_lag == 0.0

    # Ensure that _aggregate_lag resets to 0.0 when transfer rate exceeds minimum rate.
    active_config = ResumableUploadConfig(stall_minimum_rate=1024, stall_timeout=10.0)
    active_session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=active_config,
    )
    active_session._aggregate_lag = 0.5
    active_session._update_stall_control(1024, 0.1)
    assert active_session._aggregate_lag == 0.0


def test_sync_initiate_failure():
    transport = mock.create_autospec(requests.Session, instance=True)
    resp = mock.create_autospec(requests.Response, instance=True)
    resp.ok = False
    resp.status_code = 400
    resp.headers = {}
    resp.json.return_value = {"error": {"message": "Init Failed"}}
    resp.request = mock.Mock(method="POST", url="https://api.example.com/init")
    transport.request.return_value = resp

    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        transport=transport,
    )
    with pytest.raises(exceptions.GoogleAPICallError):
        session._initiate(transport=transport)


def test_sync_transmit_empty_stream():
    transport = mock.create_autospec(requests.Session, instance=True)
    resp = mock.create_autospec(requests.Response, instance=True)
    resp.ok = True
    resp.status_code = 200
    resp.headers = {"X-Goog-Upload-Status": "final"}
    resp.content = b"done"
    transport.request.return_value = resp

    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        transport=transport,
    )
    stream = io.BytesIO(b"")
    session._state._upload_url = "https://upload.example.com/resumable-123"
    result = session._transmit_chunk(transport, stream, size=0)
    assert result is resp


def test_sync_transmit_chunk_timeout_with_stall_control_active(monkeypatch):
    transport = mock.create_autospec(requests.Session, instance=True)
    transport.request.side_effect = requests.exceptions.Timeout("Read timeout")

    config = ResumableUploadConfig(
        stall_minimum_rate=1024,
        stall_timeout=10.0,
    )
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config,
        transport=transport,
    )
    session._state._upload_url = "https://upload.example.com/resumable-123"

    # Attempt 1 times out at 5.0s (< stall_timeout=10.0s): re-raises Timeout so retry/recovery can run
    clock_vals = iter([0.0, 5.0, 5.0, 10.0, 0.0, 5.0])
    monkeypatch.setattr(upload, "_monotonic_clock", lambda: next(clock_vals))
    with pytest.raises(requests.exceptions.Timeout):
        session._transmit_chunk(transport, io.BytesIO(b"data"), size=4)

    # Attempt 2 reaches elapsed stall duration of 10.0s (>= stall_timeout=10.0s): raises TransferStalledError
    with pytest.raises(exceptions.TransferStalledError):
        session._transmit_chunk(transport, io.BytesIO(b"data"), size=4)

    config_dl = ResumableUploadConfig(
        stall_minimum_rate=1024,
        stall_timeout=10.0,
        deadline=datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(seconds=5),
    )
    session_dl = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config_dl,
        transport=transport,
    )
    session_dl._state._upload_url = "https://upload.example.com/resumable-123"
    session_dl._get_deadline_remaining = mock.Mock(
        side_effect=[5.0, exceptions.DeadlineExceeded("Deadline exceeded")]
    )
    with pytest.raises(exceptions.DeadlineExceeded):
        session_dl._transmit_chunk(transport, io.BytesIO(b"data"), size=4)


def test_sync_per_attempt_timeout_retries_before_stall_timeout(monkeypatch):
    """Verifies that hitting per_attempt_timeout (5s) retries via recovery rather
    than prematurely raising TransferStalledError when stall_timeout (120s) has not elapsed."""
    transport = mock.create_autospec(requests.Session, instance=True)
    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
        },
    )
    query_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "0",
        },
    )
    final_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b'{"status": "completed"}',
    )
    transport.request.side_effect = [
        start_resp,
        requests.exceptions.Timeout("Per-attempt 5s timeout"),
        query_resp,
        final_resp,
    ]

    # Configure stall control with 120s stall_timeout; per_attempt_timeout is 5.0s
    config = ResumableUploadConfig(
        stall_minimum_rate=1024,
        stall_timeout=120.0,
    )
    session = ResumableUploadSession(
        upload_url="https://api.example.com/start",
        config=config,
        transport=transport,
    )

    # First attempt times out after 5.0s (< 120.0s stall_timeout); retry succeeds at 6.0s
    clock_vals = iter([0.0, 5.0, 5.0, 5.0, 6.0, 6.0])
    monkeypatch.setattr(upload, "_monotonic_clock", lambda: next(clock_vals))

    result = session.upload(
        stream=b"test data",
        retry=google.api_core.retry.StreamingRetry(initial=0.01, maximum=0.01),
    )
    assert result == b'{"status": "completed"}'
    assert transport.request.call_count == 4


def test_sync_transmit_chunk_timeout_outer_exception():
    transport = mock.create_autospec(requests.Session, instance=True)
    transport.request.side_effect = requests.exceptions.Timeout("Read timeout")

    config = ResumableUploadConfig(
        stall_minimum_rate=0,
    )
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config,
        transport=transport,
    )
    session._state._upload_url = "https://upload.example.com/resumable-123"
    no_retry = google.api_core.retry.StreamingRetry(
        predicate=lambda e: False, timeout=0
    )
    with pytest.raises(exceptions.TransferStalledError):
        list(
            session._transmit_all_chunks(
                transport, io.BytesIO(b"data"), 4, retry=no_retry
            )
        )

    # To hit outer exception handler in _transmit_all_chunks with elapsed deadline
    config_dl = ResumableUploadConfig(
        stall_minimum_rate=0,
        deadline=datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(seconds=5),
    )
    session_dl = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config_dl,
        transport=transport,
    )
    session_dl._state._upload_url = "https://upload.example.com/resumable-123"
    session_dl._get_deadline_remaining = mock.Mock(
        side_effect=[5.0, 5.0, exceptions.DeadlineExceeded("Deadline exceeded")]
    )
    with pytest.raises(exceptions.DeadlineExceeded):
        list(
            session_dl._transmit_all_chunks(
                transport, io.BytesIO(b"data"), 4, retry=no_retry
            )
        )

    # Non-timeout RetryError re-raises RetryError rather than TransferStalledError
    transport_conn = mock.create_autospec(requests.Session, instance=True)
    transport_conn.request.side_effect = requests.exceptions.ConnectionError(
        "Connection dropped"
    )
    session_conn = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config,
        transport=transport_conn,
    )
    session_conn._state._upload_url = "https://upload.example.com/resumable-123"
    with pytest.raises(exceptions.RetryError):
        list(
            session_conn._transmit_all_chunks(
                transport_conn, io.BytesIO(b"data"), 4, retry=no_retry
            )
        )


def test_sync_recover_failure():
    transport = mock.create_autospec(requests.Session, instance=True)
    resp = mock.create_autospec(requests.Response, instance=True)
    resp.ok = False
    resp.status_code = 400
    resp.headers = {}
    resp.json.return_value = {"error": {"message": "Recovery Failed"}}
    resp.request = mock.Mock(
        method="POST", url="https://upload.example.com/resumable-123"
    )
    transport.request.return_value = resp

    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        transport=transport,
    )
    session._state._upload_url = "https://upload.example.com/resumable-123"
    with pytest.raises(exceptions.GoogleAPICallError):
        session._recover(transport, io.BytesIO(b"data"))


def test_sync_transmit_all_chunks_completed_without_response():
    transport = mock.create_autospec(requests.Session, instance=True)
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        transport=transport,
    )
    session._state._finished = True
    with pytest.raises(
        ValueError, match="Upload completed without receiving a final response"
    ):
        list(session._transmit_all_chunks(transport, io.BytesIO(b"data"), 4))


def test_sync_iter_resume_errors():
    transport = mock.create_autospec(requests.Session, instance=True)
    session = ResumableUploadSession(transport=transport)
    with pytest.raises(ValueError, match="An upload URL must be provided to resume"):
        list(session.iter_resume(upload_url=None, stream=b"data"))

    with pytest.raises(
        ValueError, match="A data stream or payload must be provided to resume"
    ):
        list(
            session.iter_resume(upload_url="https://api.example.com/init", stream=None)
        )


def test_sync_prepare_stream_tell_error():
    class TellFailingStream(io.BytesIO):
        def tell(self) -> int:
            raise OSError("Tell failed")

    session = ResumableUploadSession()
    stream = TellFailingStream(b"data")
    stream_obj, computed_size = session._prepare_stream(stream, None)
    assert session._start_stream_offset == 0


def test_sync_format_response_payload_custom_inputs():
    from google.api_core.resumable_transfer.upload import _format_response_payload

    class CustomBytesConvertible:
        def __bytes__(self) -> bytes:
            return b"custom_bytes"

    res = _format_response_payload(CustomBytesConvertible(), response_type=None)
    assert res == b"custom_bytes"

    res_parsed = _format_response_payload(
        CustomBytesConvertible(), response_type=lambda x: x + b"_extra"
    )
    assert res_parsed == b"custom_bytes_extra"

    from google.protobuf import empty_pb2

    msg_instance = empty_pb2.Empty()
    res_msg = _format_response_payload(b"{}", response_type=msg_instance)
    assert isinstance(res_msg, empty_pb2.Empty)


class SlotException(Exception):
    __slots__ = ()


class NoTellStream:
    def read(self, n):
        return b""


class TellErrorStream:
    def read(self, n):
        return b""

    def tell(self):
        raise OSError("tell failed")


class CustomReadStream:
    def __init__(self, data):
        self.data = data

    def read(self, n):
        return self.data


def test_sync_enrich_exception():
    session = ResumableUploadSession(
        upload_url="https://upload.example.com/resumable-123",
        transport=mock.sentinel.transport,
    )
    exc = RuntimeError("test error")
    session._enrich_exception(exc)
    assert getattr(exc, "upload_url") == "https://upload.example.com/resumable-123"


def test_sync_notify_progress_no_upload_url():
    session = ResumableUploadSession(
        upload_url=None,
        transport=mock.sentinel.transport,
    )
    session._notify_progress(common.ProgressState.STARTED)


def test_sync_should_retry_request_exception_not_retryable():
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        transport=mock.sentinel.transport,
    )
    should_retry = session._get_retry_predicate()
    exc = requests.exceptions.HTTPError("Non-retryable HTTP Error")
    assert not should_retry(exc)


class NoSeekableButSeekStream:
    def read(self, n):
        return b""

    def seek(self, offset):
        pass


class UnseekableReadStream:
    def read(self, n):
        return b""

    def seekable(self):
        return False


class SeekableNoTellStream:
    def read(self, n):
        return b""

    def seekable(self):
        return True


def test_sync_rewind_stream_no_seekable_attr():
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        transport=mock.sentinel.transport,
    )
    stream = NoSeekableButSeekStream()
    session._reposition_stream_offset(stream, 0)


def test_sync_recover_buffered_chunk_out_of_bounds():
    session = ResumableUploadSession()
    session._buffered_chunk = memoryview(b"data")
    session._buffered_chunk_offset = 0

    unseekable = mock.Mock()
    unseekable.seekable.return_value = False

    with pytest.raises(UnseekableStreamError):
        session._reposition_stream_offset(unseekable, 10)

    assert session._buffered_chunk is None


def test_sync_prepare_stream_edge_cases():
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        transport=mock.sentinel.transport,
    )

    # 1. NoTellStream: Has read, but no tell
    stream1 = NoTellStream()
    s_obj1, size1 = session._prepare_stream(stream1, size=None)
    assert s_obj1 is stream1
    assert size1 is None
    assert session._start_stream_offset == 0

    # 2. TellErrorStream: Has read and tell, but tell raises OSError
    stream2 = TellErrorStream()
    s_obj2, size2 = session._prepare_stream(stream2, size=None)
    assert s_obj2 is stream2
    assert size2 is None
    assert session._start_stream_offset == 0

    # 3. CustomReadStream: Has read, no getbuffer, no seekable
    stream3 = CustomReadStream(b"hello")
    s_obj3, size3 = session._prepare_stream(stream3, size=None)
    assert s_obj3 is stream3
    assert size3 is None

    # 4. UnseekableReadStream: Has read, has seekable returning False
    stream4 = UnseekableReadStream()
    s_obj4, size4 = session._prepare_stream(stream4, size=None)
    assert s_obj4 is stream4
    assert size4 is None

    # 5. SeekableNoTellStream: Has read, has seekable returning True, no tell
    stream5 = SeekableNoTellStream()
    s_obj5, size5 = session._prepare_stream(stream5, size=None)
    assert s_obj5 is stream5
    assert size5 is None


def test_sync_transmit_all_chunks_captured_empty():
    session_transport = mock.create_autospec(requests.Session, instance=True)
    chunk_resp = mock.create_autospec(requests.Response, instance=True)
    chunk_resp.status_code = 200
    chunk_resp.content = b"{}"
    chunk_resp.headers = {"X-Goog-Upload-Status": "final"}
    session_transport.request.return_value = chunk_resp

    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
    )
    session._state._upload_url = "https://upload.example.com/resumable-123"

    stream_obj = io.BytesIO(b"data")

    # Consume the generator
    list(
        session._transmit_all_chunks(
            session_transport, stream_obj, 4, progress_queue=None
        )
    )


def test_sync_upload_multiple_chunks():
    session_transport = mock.create_autospec(requests.Session, instance=True)

    # Start response
    start_resp = mock.create_autospec(requests.Response, instance=True)
    start_resp.status_code = 200
    start_resp.content = b""
    start_resp.headers = {
        "X-Goog-Upload-Status": "active",
        "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
    }

    # 1st chunk response: active
    chunk1_resp = mock.create_autospec(requests.Response, instance=True)
    chunk1_resp.status_code = 200
    chunk1_resp.content = b""
    chunk1_resp.headers = {"X-Goog-Upload-Status": "active"}

    # 2nd chunk response: final
    chunk2_resp = mock.create_autospec(requests.Response, instance=True)
    chunk2_resp.status_code = 200
    chunk2_resp.content = b"{}"
    chunk2_resp.headers = {"X-Goog-Upload-Status": "final"}

    session_transport.request.side_effect = [start_resp, chunk1_resp, chunk2_resp]

    config = ResumableUploadConfig(chunk_size=5)
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config,
    )

    res = session.upload(stream=b"0123456789", transport=session_transport)
    assert res == chunk2_resp.content
    assert session.bytes_uploaded == 10
    assert session_transport.request.call_count == 3


def test_sync_format_response_payload_unsupported_type():
    from google.api_core.resumable_transfer.upload import _format_response_payload

    res = _format_response_payload(b"some content", "unsupported")
    assert res == b"some content"


def test_sync_prepare_stream_explicit_size():
    session = ResumableUploadSession(upload_url="https://api.example.com/init")

    # 1. bytes with explicit size
    _, computed_size = session._prepare_stream(b"abcd", size=4)
    assert computed_size == 4

    # 2. Iterable with explicit size
    _, computed_size = session._prepare_stream([b"ab", b"cd"], size=4)
    assert computed_size == 4

    # 3. BinaryIO with explicit size
    _, computed_size = session._prepare_stream(io.BytesIO(b"abcd"), size=4)
    assert computed_size == 4


def test_state_process_chunk_response_unknown_status():
    from google.api_core.resumable_transfer.upload_state import _ProtocolState

    state = _ProtocolState(upload_url="https://api.example.com/init")
    state.process_chunk_response(200, {"X-Goog-Upload-Status": "unknown"}, 100)
    assert state.bytes_uploaded == 0
    assert not state.finished


def test_sync_partial_chunk_recovery_does_not_prematurely_finalize():
    """Ensure that retrying a partially committed chunk (len < chunk_size) does not prematurely finalize.

    When a 4-byte chunk (b"0123") partially succeeds (server commits 2 bytes)
    and is retried, ensure that the remaining 2 bytes (b"23") are sent with
    "upload" rather than "upload, finalize" so the remaining payload (b"45")
    is not dropped.
    """
    server_received_bytes = bytearray()
    call_count = 0

    def handle_request(method, url, data=None, headers=None, **kwargs):
        nonlocal call_count
        call_count += 1
        cmd = headers.get("X-Goog-Upload-Command", "") if headers else ""

        resp = mock.create_autospec(requests.Response, instance=True)
        resp.request = mock.Mock(method=method, url=url)
        resp.content = b""

        # Request 1: start session
        if call_count == 1:
            assert cmd == "start"
            resp.status_code = 200
            resp.ok = True
            resp.headers = {
                "X-Goog-Upload-Status": "active",
                "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
            }
            return resp

        # Request 2: initial Chunk 1 (b"0123") -> server commits partial 2 bytes (b"01"), then fails 503
        if call_count == 2:
            assert cmd == "upload"
            assert bytes(data) == b"0123"
            server_received_bytes.extend(b"01")
            resp.status_code = 503
            resp.ok = False
            resp.headers = {}
            resp.json.return_value = {
                "error": {"code": 503, "message": "Service Unavailable"}
            }
            return resp

        # Request 3: recovery query -> server reports 2 committed bytes
        if call_count == 3:
            assert cmd == "query"
            resp.status_code = 200
            resp.ok = True
            resp.headers = {
                "X-Goog-Upload-Status": "active",
                "X-Goog-Upload-Size-Received": str(len(server_received_bytes)),
            }
            return resp

        # Subsequent upload requests (Request 4: remaining b"23", Request 5: final b"45")
        if data:
            server_received_bytes.extend(bytes(data))

        resp.status_code = 200
        resp.ok = True
        if "finalize" in cmd:
            resp.headers = {"X-Goog-Upload-Status": "final"}
            resp.content = b"{}"
        else:
            resp.headers = {"X-Goog-Upload-Status": "active"}
        return resp

    session_transport = mock.create_autospec(requests.Session, instance=True)
    session_transport.request.side_effect = handle_request

    # Ensure that the unified outer StreamingRetry coordinates backoff and
    # triggers protocol-level _recover() on retryable errors before retransmitting.
    retry_cfg = google.api_core.retry.StreamingRetry(
        predicate=ResumableUploadSession()._get_retry_predicate(),
        initial=0.001,
    )
    config = ResumableUploadConfig(chunk_size=4)
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        config=config,
    )

    session.upload(stream=b"012345", transport=session_transport, retry=retry_cfg)

    # Verify no data loss occurred: server must receive all 6 bytes (b"012345"), not truncated b"0123"
    assert bytes(server_received_bytes) == b"012345"


def test_sync_streaming_retry_and_recovery_final():
    """Ensure that StreamingRetry configuration and recovery returning 'final' status are handled properly."""
    session_transport = mock.create_autospec(requests.Session, instance=True)

    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/resumable-123",
        },
    )
    err503_resp = mock.Mock(
        ok=False,
        status_code=503,
        headers={},
    )
    err503_resp.json.return_value = {"error": {"code": 503, "message": "Unavailable"}}
    err503_resp.text = '{"error": {"code": 503, "message": "Unavailable"}}'
    err503_resp.content = err503_resp.text.encode("utf-8")

    # Recovery query reports that the upload already reached 'final' status on the server
    query_final_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b'{"name": "already_done.txt", "size": 4}',
    )

    session_transport.request.side_effect = [
        start_resp,
        err503_resp,
        query_final_resp,
    ]

    streaming_retry = google.api_core.retry.StreamingRetry(
        predicate=ResumableUploadSession()._get_retry_predicate(),
        initial=0.001,
    )
    session = ResumableUploadSession(
        upload_url="https://api.example.com/init",
        response_type=DummyResponse,
    )
    resolved_streaming = session._get_streaming_retry(retry_override=streaming_retry)
    assert resolved_streaming._initial == 0.001

    result = session.upload(
        stream=b"data", transport=session_transport, retry=streaming_retry
    )
    assert isinstance(result, DummyResponse)
    assert result.name == "already_done.txt"
    assert session.finished is True


def test_sync_method_override_arguments() -> None:
    """Verifies content_type and on_progress overrides on initiate, upload, and resume."""
    # 1. initiate with content_type override
    start_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-URL": "https://upload.example.com/123",
        },
        content=b"",
    )
    transport1 = mock.Mock(spec=requests.Session)
    transport1.request.return_value = start_resp
    session1 = ResumableUploadSession(upload_url="https://api.example.com/start")
    session1._initiate(transport=transport1, content_type="text/plain")
    assert session1._content_type == "text/plain"

    # 2. upload with content_type override
    chunk_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={"X-Goog-Upload-Status": "final"},
        content=b"{}",
    )
    transport2 = mock.Mock(spec=requests.Session)
    transport2.request.side_effect = [start_resp, chunk_resp]
    session2 = ResumableUploadSession(upload_url="https://api.example.com/start")
    session2.upload(
        stream=b"data",
        transport=transport2,
        content_type="text/csv",
    )
    assert session2._content_type == "text/csv"

    # 3. resume with chunk_size override
    query_resp = mock.Mock(
        ok=True,
        status_code=200,
        headers={
            "X-Goog-Upload-Status": "active",
            "X-Goog-Upload-Size-Received": "0",
        },
        content=b"",
    )
    transport3 = mock.Mock(spec=requests.Session)
    transport3.request.side_effect = [query_resp, chunk_resp]
    session3 = ResumableUploadSession()
    session3.resume(
        upload_url="https://upload.example.com/123",
        stream=b"data",
        transport=transport3,
    )
