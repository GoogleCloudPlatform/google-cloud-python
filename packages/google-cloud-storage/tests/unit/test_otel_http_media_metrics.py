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

"""Unit tests for OpenTelemetry HTTP media downloads, uploads, and XML MPU metrics."""

import base64
import datetime
import http.client
import io
import json
from unittest import mock

import google_crc32c
import pytest
import requests
from google.api_core import retry
from google.auth import credentials as auth_credentials
from google.cloud.exceptions import Forbidden, NotFound
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import InMemoryMetricReader

from google.cloud.storage import _helpers, _opentelemetry_metrics
from google.cloud.storage._media.requests import _request_helpers
from google.cloud.storage._media.requests.download import (
    ChunkedDownload,
    Download,
    RawChunkedDownload,
    RawDownload,
)
from google.cloud.storage._media.requests.upload import (
    MultipartUpload,
    ResumableUpload,
    SimpleUpload,
    XMLMPUContainer,
    XMLMPUPart,
)
from google.cloud.storage.client import Client
from google.cloud.storage.exceptions import DataCorruption, InvalidResponse
from google.cloud.storage.retry import DEFAULT_RETRY_IF_GENERATION_SPECIFIED


def _make_credentials():
    return auth_credentials.AnonymousCredentials()


def _crc32c_b64(data: bytes) -> str:
    checksum = google_crc32c.Checksum(data)
    return base64.b64encode(checksum.digest()).decode("ascii")


class _FakeRawStream:
    """Minimal urllib3-like raw response backing streaming and single-shot reads."""

    def __init__(self, chunks, error_after=None):
        self._chunks = list(chunks)
        self._buf = b"".join(self._chunks)
        self._error_after = error_after
        self.headers = {}

    def read(self, amt=None, decode_content=None):
        if amt is None:
            data, self._buf = self._buf, b""
            self._chunks = []
            return data
        data, self._buf = self._buf[:amt], self._buf[amt:]
        if not self._buf:
            self._chunks = []
        return data

    def stream(self, amt=8192, decode_content=None):
        for idx, chunk in enumerate(self._chunks):
            if self._error_after is not None and idx >= self._error_after:
                raise requests.ReadTimeout("mid-stream timeout")
            yield chunk

    def close(self):
        pass


def _media_response(
    body=b"",
    status_code=http.client.OK,
    headers=None,
    chunks=None,
    streaming=False,
    error_after=None,
):
    response = requests.Response()
    response.status_code = status_code
    if headers:
        response.headers.update(headers)
    chunk_list = list(chunks) if chunks is not None else ([body] if body else [])
    response.raw = _FakeRawStream(chunk_list, error_after=error_after)
    if streaming:
        response._content = False
    else:
        response._content = body
    response.request = requests.Request(
        "GET", "https://storage.googleapis.com/download/storage/v1/b/b1/o/o1"
    ).prepare()
    return response


def _json_response(payload=None, status_code=http.client.OK):
    hdrs = {"Content-Type": "application/json"}
    body = b"" if payload is None else json.dumps(payload).encode("utf-8")
    return _media_response(body=body, status_code=status_code, headers=hdrs)


def _collect_metrics(reader):
    data = reader.get_metrics_data()
    collected = {}
    if data is None:  # pragma: NO COVER
        return collected
    for resource_metric in data.resource_metrics:
        for scope_metric in resource_metric.scope_metrics:
            for metric in scope_metric.metrics:
                collected.setdefault(metric.name, []).extend(metric.data.data_points)
    return collected


@pytest.fixture(autouse=True)
def _enable_dev_gate(monkeypatch):
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)
    monkeypatch.setattr(_opentelemetry_metrics, "HAS_OPENTELEMETRY_METRICS", True)


@pytest.fixture
def metrics_env():
    reader = InMemoryMetricReader()
    provider = MeterProvider(metric_readers=[reader])
    session = mock.MagicMock()
    client = Client(
        project="test-project",
        credentials=_make_credentials(),
        _http=session,
        enable_metrics=True,
        meter_provider=provider,
    )
    client._bucket_metadata_cache = None
    yield client, session, reader
    client.close()


def test_request_helpers_branches(metrics_env):
    client, session, reader = metrics_env
    recorder = client._metrics_recorder

    # 1. resolve_transport_recorder suppressed, disabled, ContextVar, and transport attribute
    with _helpers._suppress_internal_metrics():
        assert _request_helpers.resolve_transport_recorder(session) is None

    disabled_client = Client(
        project="test-project",
        credentials=_make_credentials(),
        _http=mock.MagicMock(),
        enable_metrics=False,
    )
    disabled_client._bucket_metadata_cache = None
    assert _request_helpers.resolve_transport_recorder(disabled_client._http) is None
    disabled_client.close()

    plain_transport = mock.MagicMock(spec=["request"])
    assert _request_helpers.resolve_transport_recorder(plain_transport) is None
    with _helpers._start_storage_operation(
        client, "storage.Blob.download_to_file", "ReadObject"
    ):
        assert _request_helpers.resolve_transport_recorder(plain_transport) is recorder
    assert _request_helpers.resolve_transport_recorder(session) is recorder

    # Inactive recorder in _ACTIVE_METRICS_RECORDER falls through to transport
    inactive_rec = mock.Mock(standard_enabled=False)
    tok = _helpers._ACTIVE_METRICS_RECORDER.set(inactive_rec)
    try:
        assert _request_helpers.resolve_transport_recorder(session) is recorder
    finally:
        _helpers._ACTIVE_METRICS_RECORDER.reset(tok)

    # 2. Direct helper edge cases outside wait_and_retry
    _request_helpers.record_streaming_ttfb()  # No-op when state is None
    plain_transport.request.return_value = _json_response({"ok": True})
    direct_resp = _request_helpers.transport_request(
        plain_transport, "GET", "https://storage.googleapis.com/b1/o1"
    )
    assert direct_resp.status_code == 200
    assert _request_helpers._extract_status_code(direct_resp) == 200
    assert _request_helpers._extract_status_code(mock.Mock(status_code=True)) is None
    assert _request_helpers._extract_status_code(None) is None

    # 3. transport_request when ttfb_recorded is already True vs streaming=False
    manual_state = _request_helpers._MediaAttemptState(
        recorder=recorder,
        method="GET",
        fallback_url="https://storage.googleapis.com/b1/o1",
        streaming=False,
    )
    manual_state.ttfb_recorded = True
    st_tok = _request_helpers._MEDIA_ATTEMPT_STATE.set(manual_state)
    try:
        _request_helpers.transport_request(
            plain_transport, "GET", "https://storage.googleapis.com/b1/o1"
        )
    finally:
        _request_helpers._MEDIA_ATTEMPT_STATE.reset(st_tok)

    # 4. RequestsMixin & RawRequestsMixin._get_body branches: multi-chunk, 0-chunk, and pre-populated _content
    req_mixin = _request_helpers.RequestsMixin()
    req_chunks = _media_response(chunks=[b"ab", b"cd"], streaming=True)
    assert req_mixin._get_body(req_chunks) == b"abcd"
    assert req_mixin._get_body(req_chunks) == b"abcd"
    req_empty = _media_response(chunks=[], streaming=True)
    assert req_mixin._get_body(req_empty) == b""

    raw_mixin = _request_helpers.RawRequestsMixin()
    resp_chunks = _media_response(chunks=[b"ab", b"cd"], streaming=True)
    assert raw_mixin._get_body(resp_chunks) == b"abcd"
    assert raw_mixin._get_body(resp_chunks) == b"abcd"
    resp_empty_stream = _media_response(chunks=[], streaming=True)
    assert raw_mixin._get_body(resp_empty_stream) == b""

    # 5. wait_and_retry edge branches:
    fast_retry = retry.Retry(
        predicate=retry.if_exception_type(RuntimeError),
        initial=0.001,
        maximum=0.002,
        deadline=1.0,
    )
    calls = {"n": 0}

    def _flaky_uninstrumented():
        calls["n"] += 1
        if calls["n"] == 1:
            raise RuntimeError("retry me")
        return "done"

    assert (
        _request_helpers.wait_and_retry(
            _flaky_uninstrumented, fast_retry, transport=plain_transport
        )
        == "done"
    )
    assert (
        _request_helpers.wait_and_retry(
            lambda: "no-retry", None, transport=plain_transport
        )
        == "no-retry"
    )

    assert (
        _request_helpers.wait_and_retry(
            lambda: None,
            None,
            transport=session,
            method="GET",
            url="https://storage.googleapis.com/download/storage/v1/b/b1/o/o1",
        )
        is None
    )
    assert (
        _request_helpers.wait_and_retry(
            lambda: _json_response({"ok": True}),
            None,
            transport=session,
            method="GET",
            url="https://storage.googleapis.com/download/storage/v1/b/b1/o/o1",
        ).status_code
        == 200
    )

    err_with_resp = requests.HTTPError("502 Bad Gateway")
    err_with_resp.response = _json_response({"err": "bad gateway"}, status_code=502)
    with pytest.raises(requests.HTTPError):
        _request_helpers.wait_and_retry(
            lambda: (_ for _ in ()).throw(err_with_resp),
            None,
            transport=session,
            method="GET",
            url="https://storage.googleapis.com/download/storage/v1/b/b1/o/o1",
        )

    session.request.return_value = _json_response({"ok": True})
    assert (
        _request_helpers.wait_and_retry(
            lambda: _request_helpers.transport_request(
                session,
                "GET",
                "https://storage.googleapis.com/download/storage/v1/b/b1/o/o1",
            ),
            None,
            transport=session,
            method="GET",
            url="https://storage.googleapis.com/download/storage/v1/b/b1/o/o1",
            streaming=True,
        ).status_code
        == 200
    )

    # 6. Missing status_code (None) must NOT record TTFB
    pts_before_nosc = _collect_metrics(reader)
    ttfb_before_nosc = sum(p.count for p in pts_before_nosc["gcp.storage.client.ttfb"])

    resp_no_sc = mock.Mock(status_code=None, headers={})
    session.request.return_value = resp_no_sc
    _request_helpers.wait_and_retry(
        lambda: _request_helpers.transport_request(
            session,
            "GET",
            "https://storage.googleapis.com/download/storage/v1/b/b1/o/o1",
        ),
        None,
        transport=session,
        method="GET",
        url="https://storage.googleapis.com/download/storage/v1/b/b1/o/o1",
        streaming=False,
    )

    def _streaming_no_sc_invalid():
        r = _request_helpers.transport_request(
            session,
            "GET",
            "https://storage.googleapis.com/download/storage/v1/b/b1/o/o1",
        )
        _request_helpers.record_streaming_ttfb()
        raise InvalidResponse(r, "missing status code")

    with pytest.raises(InvalidResponse):
        _request_helpers.wait_and_retry(
            _streaming_no_sc_invalid,
            None,
            transport=session,
            method="GET",
            url="https://storage.googleapis.com/download/storage/v1/b/b1/o/o1",
            streaming=True,
        )

    pts_after_nosc = _collect_metrics(reader)
    ttfb_after_nosc = sum(p.count for p in pts_after_nosc["gcp.storage.client.ttfb"])
    assert ttfb_after_nosc == ttfb_before_nosc


def test_media_downloads_ttfb_retries_and_416_zero_byte(metrics_env):
    client, session, reader = metrics_env
    media_url = "https://storage.googleapis.com/download/storage/v1/b/b1/o/o1?alt=media"
    fast_retry = retry.Retry(
        predicate=retry.if_exception_type(
            InvalidResponse, requests.ConnectionError, requests.Timeout
        ),
        initial=0.001,
        maximum=0.002,
        deadline=5.0,
    )

    payload = b"hello world!"
    crc_hdr = f"crc32c={_crc32c_b64(payload)}"
    session.request.side_effect = [
        requests.ConnectTimeout("connect timed out"),
        requests.ConnectionError("connection reset"),
        _media_response(b"unavailable", status_code=503, streaming=True),
        _media_response(
            chunks=[b"hello ", b"world!"],
            status_code=200,
            streaming=True,
            error_after=0,
        ),
        _media_response(
            chunks=[b"hello ", b"world!"],
            status_code=200,
            streaming=True,
            error_after=1,
        ),
        _media_response(
            chunks=[b"hello ", b"world!"],
            status_code=200,
            headers={"x-goog-generation": "1", "x-goog-hash": crc_hdr},
            streaming=True,
        ),
    ]
    out = io.BytesIO()
    with _helpers._start_storage_operation(
        client, "storage.Blob.download_to_file", "ReadObject"
    ):
        dl = Download(media_url, stream=out, checksum="crc32c")
        dl._retry_strategy = fast_retry
        dl.consume(session)

    assert out.getvalue().endswith(payload)
    pts = _collect_metrics(reader)
    assert sum(p.value for p in pts["gcp.storage.client.operations"]) == 1
    assert sum(p.value for p in pts["gcp.storage.client.attempts"]) == 6
    assert sum(p.value for p in pts["gcp.storage.client.retries"]) == 5
    assert sum(p.value for p in pts["gcp.storage.client.errors"]) == 5
    err_by_type = {}
    for p in pts["gcp.storage.client.errors"]:
        et = p.attributes["error.type"]
        err_by_type[et] = err_by_type.get(et, 0) + p.value
    assert err_by_type == {
        "TIMEOUT": 3,
        "CONNECTION_ERROR": 1,
        "UNAVAILABLE": 1,
    }
    assert sum(p.count for p in pts["gcp.storage.client.ttfb"]) == 3
    for h_pt in pts["http.client.request.duration"]:
        assert (
            h_pt.attributes["url.template"]
            == "/download/storage/v1/b/{bucket}/o/{object}"
        )

    large_oneshot = b"x" * 9000
    delayed_dl_resp = _media_response(b"", status_code=200, streaming=True)
    delayed_dl_resp.raw.read = mock.Mock(side_effect=[b"", b"delayed-gzip-dl"])
    session.request.side_effect = [
        _media_response(large_oneshot, status_code=200, streaming=True),
        delayed_dl_resp,
        _media_response(b"", status_code=200, streaming=True),
        _media_response(chunks=[], status_code=200, streaming=True),
        _media_response(b"nostream", status_code=200, streaming=False),
    ]
    dl_single_buf = io.BytesIO()
    dl_single = Download(media_url, stream=dl_single_buf, single_shot_download=True)
    dl_single.consume(session)
    assert dl_single_buf.getvalue() == large_oneshot
    dl_delayed_buf = io.BytesIO()
    Download(
        media_url, stream=dl_delayed_buf, single_shot_download=True, checksum=None
    ).consume(session)
    assert dl_delayed_buf.getvalue() == b"delayed-gzip-dl"
    Download(media_url, stream=io.BytesIO(), single_shot_download=True).consume(session)
    dl_empty = Download(media_url, stream=io.BytesIO(), single_shot_download=False)
    dl_empty.consume(session)
    dl_nostream = Download(media_url, stream=None)
    dl_nostream.consume(session)

    plain_transport = mock.MagicMock(spec=["request"])
    plain_transport.request.side_effect = [
        _media_response(b"plain-dl", status_code=200, streaming=True),
        _media_response(b"plain-raw", status_code=200, streaming=True),
    ]
    plain_dl_buf = io.BytesIO()
    Download(media_url, stream=plain_dl_buf, single_shot_download=True).consume(
        plain_transport
    )
    assert plain_dl_buf.getvalue() == b"plain-dl"
    plain_raw_buf = io.BytesIO()
    RawDownload(media_url, stream=plain_raw_buf, single_shot_download=True).consume(
        plain_transport
    )
    assert plain_raw_buf.getvalue() == b"plain-raw"

    delayed_raw_resp = _media_response(b"", status_code=200, streaming=True)
    delayed_raw_resp.raw.read = mock.Mock(side_effect=[b"", b"delayed-raw-body"])
    session.request.side_effect = [
        _media_response(large_oneshot, status_code=200, streaming=True),
        delayed_raw_resp,
        _media_response(b"", status_code=200, streaming=True),
        _media_response(chunks=[b"raw-", b"multi"], status_code=200, streaming=True),
        _media_response(chunks=[], status_code=200, streaming=True),
        _media_response(chunks=[b"raw-nostream"], status_code=200, streaming=True),
    ]
    raw_single_buf = io.BytesIO()
    RawDownload(media_url, stream=raw_single_buf, single_shot_download=True).consume(
        session
    )
    assert raw_single_buf.getvalue() == large_oneshot
    raw_delayed_buf = io.BytesIO()
    RawDownload(
        media_url, stream=raw_delayed_buf, single_shot_download=True, checksum=None
    ).consume(session)
    assert raw_delayed_buf.getvalue() == b"delayed-raw-body"
    RawDownload(media_url, stream=io.BytesIO(), single_shot_download=True).consume(
        session
    )
    RawDownload(media_url, stream=io.BytesIO(), single_shot_download=False).consume(
        session
    )
    RawDownload(media_url, stream=io.BytesIO(), single_shot_download=False).consume(
        session
    )
    RawDownload(media_url, stream=None).consume(session)

    err_cd_active = _media_response(b"err", status_code=500, streaming=True)
    err_cd_active.close = mock.MagicMock(wraps=err_cd_active.close)
    err_cd_plain = _media_response(b"err", status_code=500, streaming=False)
    err_cd_plain.close = mock.MagicMock(wraps=err_cd_plain.close)

    session.request.side_effect = [
        _media_response(
            chunks=[b"ab", b"cd"],
            status_code=http.client.PARTIAL_CONTENT,
            headers={"content-range": "bytes 0-3/4", "content-length": "4"},
            streaming=True,
        ),
        err_cd_active,
        _media_response(
            chunks=[b"ab", b"cd"],
            status_code=http.client.PARTIAL_CONTENT,
            headers={"content-range": "bytes 0-3/4", "content-length": "4"},
            streaming=True,
        ),
        _media_response(
            b"",
            status_code=http.client.REQUESTED_RANGE_NOT_SATISFIABLE,
            headers={"content-range": "bytes */0"},
            streaming=True,
        ),
    ]
    cd_buf = io.BytesIO()
    cd = ChunkedDownload(media_url, chunk_size=4, stream=cd_buf)
    cd.consume_next_chunk(session)
    assert cd.finished
    assert cd_buf.getvalue() == b"abcd"

    cd_fail_active = ChunkedDownload(
        media_url, chunk_size=4, stream=io.BytesIO(), retry=None
    )
    with pytest.raises(InvalidResponse):
        cd_fail_active.consume_next_chunk(session)
    err_cd_active.close.assert_called_once()

    plain_transport.request.side_effect = [err_cd_plain]
    cd_fail_plain = ChunkedDownload(
        media_url, chunk_size=4, stream=io.BytesIO(), retry=None
    )
    with pytest.raises(InvalidResponse):
        cd_fail_plain.consume_next_chunk(plain_transport)
    err_cd_plain.close.assert_not_called()

    rcd = RawChunkedDownload(media_url, chunk_size=4, stream=io.BytesIO())
    rcd.consume_next_chunk(session)
    assert rcd.finished

    bucket = client.bucket("b1")
    zero_blob = bucket.blob("empty-obj", chunk_size=262144)
    zero_buf = io.BytesIO()
    zero_blob.download_to_file(zero_buf)
    assert zero_buf.getvalue() == b""

    pts_after = _collect_metrics(reader)
    dl_ops = [
        p
        for p in pts_after["gcp.storage.client.operations"]
        if p.attributes["gcp.client.method"] == "storage.Blob.download_to_file"
    ]
    assert sum(p.value for p in dl_ops) == 2
    assert all(p.attributes["error.type"] == "OK" for p in dl_ops)
    body_pts = pts_after["gcp.storage.client.response.body.size"]
    assert any(p.sum == 0 for p in body_pts)


def test_all_media_upload_classes_and_xml_mpu(metrics_env, tmp_path):
    client, session, reader = metrics_env
    upload_url = "https://storage.googleapis.com/upload/storage/v1/b/b1/o?uploadType=media&name=o1"
    mp_url = (
        "https://storage.googleapis.com/upload/storage/v1/b/b1/o?uploadType=multipart"
    )
    res_url = (
        "https://storage.googleapis.com/upload/storage/v1/b/b1/o?uploadType=resumable"
    )
    session_uri = "https://storage.googleapis.com/upload/storage/v1/b/b1/o?uploadType=resumable&upload_id=abc"
    xml_url = "https://storage.googleapis.com/b1/o1"

    session.request.side_effect = [
        _json_response({"name": "o1", "size": "3"}),
        _json_response({"name": "o1", "size": "5"}),
    ]
    su = SimpleUpload(upload_url)
    su.transmit(session, b"abc", "text/plain")
    mu = MultipartUpload(mp_url)
    mu.transmit(session, b"hello", {"name": "o1"}, "text/plain")

    chunk_size = 256 * 1024
    ru_bytes = b"x" * chunk_size + b"y" * 10
    stream = io.BytesIO(ru_bytes)
    ru = ResumableUpload(res_url, chunk_size)
    session.request.side_effect = [
        _media_response(
            b"",
            status_code=http.client.OK,
            headers={"location": session_uri},
        ),
        _media_response(
            b"",
            status_code=http.client.PERMANENT_REDIRECT,
            headers={"range": f"bytes=0-{chunk_size - 1}"},
        ),
        _media_response(
            b"",
            status_code=http.client.PERMANENT_REDIRECT,
            headers={"range": f"bytes=0-{chunk_size - 1}"},
        ),
        _json_response(
            {
                "name": "o1",
                "size": str(chunk_size + 10),
                "crc32c": _crc32c_b64(ru_bytes),
            }
        ),
    ]
    ru.initiate(session, stream, {"name": "o1"}, "application/octet-stream")
    ru.transmit_next_chunk(session)
    ru._invalid = True
    ru.recover(session)
    assert not ru.invalid
    ru.transmit_next_chunk(session)
    assert ru.finished

    sample_file = tmp_path / "mpu.bin"
    sample_file.write_bytes(b"0123456789")
    xml_ns = 'xmlns="http://s3.amazonaws.com/doc/2006-03-01/"'
    session.request.side_effect = [
        _media_response(
            f"<InitiateMultipartUploadResult {xml_ns}><UploadId>u-123</UploadId></InitiateMultipartUploadResult>".encode(
                "utf-8"
            ),
            status_code=200,
        ),
        _media_response(
            b"",
            status_code=200,
            headers={
                "ETag": '"etag-1"',
                "x-goog-hash": f"crc32c={_crc32c_b64(b'0123456789')}",
            },
        ),
        _media_response(
            f'<CompleteMultipartUploadResult {xml_ns}><ETag>"final"</ETag></CompleteMultipartUploadResult>'.encode(
                "utf-8"
            ),
            status_code=200,
        ),
        _media_response(b"", status_code=204),
    ]
    container = XMLMPUContainer(xml_url, str(sample_file))
    container.initiate(session, content_type="application/octet-stream")
    assert container.upload_id == "u-123"
    part = XMLMPUPart(
        xml_url,
        "u-123",
        str(sample_file),
        start=0,
        end=10,
        part_number=1,
        checksum="crc32c",
    )
    part.upload(session)
    container.register_part(1, part.etag)
    container.finalize(session)
    container.cancel(session)

    pts = _collect_metrics(reader)
    templates = {
        p.attributes["url.template"] for p in pts["http.client.request.duration"]
    }
    assert "/upload/storage/v1/b/{bucket}/o" in templates
    assert "/{bucket}/{object}" in templates
    assert sum(p.value for p in pts["gcp.storage.client.attempts"]) == 10


def test_blob_media_methods_body_size_and_corruption_cleanup(metrics_env, tmp_path):
    client, session, reader = metrics_env
    bucket = client.bucket("b1")
    blob = bucket.blob("o1")
    payload = b"storage-payload"
    crc_hdr = f"crc32c={_crc32c_b64(payload)}"

    dl_file = tmp_path / "downloaded.bin"
    tm_dl_file = tmp_path / "tm_downloaded.bin"
    blob._properties["updated"] = "2026-01-02T03:04:05.000Z"
    session.request.side_effect = [
        _media_response(
            payload,
            status_code=200,
            headers={"x-goog-generation": "7", "x-goog-hash": crc_hdr},
            streaming=True,
        ),
        _media_response(
            payload,
            status_code=200,
            headers={"x-goog-generation": "7", "x-goog-hash": crc_hdr},
            streaming=True,
        ),
        _media_response(
            payload,
            status_code=200,
            headers={"x-goog-generation": "7", "x-goog-hash": crc_hdr},
            streaming=True,
        ),
        _media_response(
            payload,
            status_code=200,
            headers={"x-goog-generation": "7", "x-goog-hash": crc_hdr},
            streaming=True,
        ),
        _media_response(
            payload,
            status_code=200,
            headers={"x-goog-generation": "7", "x-goog-hash": crc_hdr},
            streaming=True,
        ),
        _media_response(
            payload,
            status_code=200,
            headers={"x-goog-generation": "7", "x-goog-hash": crc_hdr},
            streaming=True,
        ),
    ]
    blob.download_to_file(
        io.BytesIO(),
        if_generation_match=7,
        retry=DEFAULT_RETRY_IF_GENERATION_SPECIFIED,
    )
    assert blob.download_as_bytes() == payload
    with pytest.warns(PendingDeprecationWarning):
        assert blob.download_as_string() == payload
    blob.download_to_filename(str(dl_file))
    assert dl_file.read_bytes() == payload
    assert isinstance(blob.updated, datetime.datetime)
    # Exercise internal transfer_manager default_method branches on Blob helpers
    blob._handle_filename_and_download(str(tm_dl_file), command="tm.download_many")
    blob._prep_and_do_download(io.BytesIO(), command="tm.download_many")

    missing_dest = tmp_path / "missing.bin"
    corrupt_dest = tmp_path / "corrupt.bin"
    session.request.side_effect = [
        _json_response({"error": {"message": "not found"}}, status_code=404),
        _media_response(
            b"tampered",
            status_code=200,
            headers={"x-goog-generation": "7", "x-goog-hash": crc_hdr},
            streaming=True,
        ),
    ]
    with pytest.raises(NotFound):
        blob.download_to_filename(str(missing_dest), retry=None)
    assert not missing_dest.exists()

    with pytest.raises(DataCorruption):
        blob.download_to_filename(str(corrupt_dest), retry=None)
    assert not corrupt_dest.exists()

    up_file = tmp_path / "upload.txt"
    up_file.write_bytes(b"from-disk")
    session.request.side_effect = [
        _json_response({"name": "o1", "size": "9"}),
        _json_response({"name": "o1", "size": "9"}),
        _json_response({"name": "o1", "size": "9"}),
        _json_response({"name": "o1", "size": "9"}),
        _json_response({"error": {"message": "forbidden"}}, status_code=403),
    ]
    blob.upload_from_string(b"123456789")
    blob.upload_from_filename(str(up_file))
    blob._handle_filename_and_upload(str(up_file), command="tm.upload_many")
    blob._prep_and_do_upload(io.BytesIO(b"123456789"), size=9, command="tm.upload_many")
    with pytest.raises(Forbidden):
        blob.upload_from_file(io.BytesIO(b"denied"), size=6, retry=None)

    res_blob = bucket.blob("resumable-obj", chunk_size=256 * 1024)
    res_data = b"a" * (256 * 1024) + b"b" * 100
    session_uri = "https://storage.googleapis.com/upload/storage/v1/b/b1/o?uploadType=resumable&upload_id=r1"
    session.request.side_effect = [
        _media_response(b"", status_code=200, headers={"location": session_uri}),
        _media_response(
            b"",
            status_code=http.client.PERMANENT_REDIRECT,
            headers={"range": f"bytes=0-{256 * 1024 - 1}"},
        ),
        _json_response(
            {
                "name": "resumable-obj",
                "size": str(len(res_data)),
                "crc32c": _crc32c_b64(res_data),
            }
        ),
    ]
    res_blob.upload_from_file(io.BytesIO(res_data))

    # Resumable DataCorruption triggers self.delete() which MUST be suppressed!
    session.request.side_effect = [
        _media_response(b"", status_code=200, headers={"location": session_uri}),
        _json_response(None, status_code=204),  # suppressed self.delete()
    ]
    with mock.patch.object(
        ResumableUpload,
        "transmit_next_chunk",
        side_effect=DataCorruption(mock.Mock(), "hash mismatch"),
    ):
        with pytest.raises(DataCorruption):
            res_blob.upload_from_file(io.BytesIO(b"corrupt"), retry=None)

    disabled_session = mock.MagicMock()
    disabled_client = Client(
        project="test-project",
        credentials=_make_credentials(),
        _http=disabled_session,
        enable_metrics=False,
    )
    disabled_client._bucket_metadata_cache = None
    d_blob = disabled_client.bucket("b1").blob("o1")
    disabled_session.request.side_effect = [
        _media_response(b"ok", status_code=200, streaming=True),
        _json_response({"name": "o1", "size": "2"}),
        _media_response(b"", status_code=200, headers={"location": session_uri}),
        _json_response({"name": "o1", "size": "2", "crc32c": _crc32c_b64(b"ok")}),
    ]
    d_blob.download_to_file(io.BytesIO())
    d_blob.upload_from_string(b"ok")
    d_res_blob = disabled_client.bucket("b1").blob("o2", chunk_size=256 * 1024)
    d_res_blob.upload_from_file(io.BytesIO(b"ok"))
    disabled_client.close()

    with mock.patch.object(
        Download,
        "consume",
        autospec=True,
        side_effect=lambda self_dl, *a, **kw: (
            setattr(self_dl, "_bytes_downloaded", True) or _media_response(b"")
        ),
    ):
        blob._do_download(
            session,
            io.BytesIO(),
            "https://storage.googleapis.com/download/storage/v1/b/b1/o/o1?alt=media",
            {},
        )
    mock_up = mock.MagicMock()
    mock_up.finished = False
    mock_up.resumable_url = session_uri

    def _finish_bool(*a, **kw):
        mock_up.finished = True
        mock_up.bytes_uploaded = True
        return _json_response({"name": "o1"})

    mock_up.transmit_next_chunk.side_effect = _finish_bool
    with mock.patch.object(
        res_blob,
        "_initiate_resumable_upload",
        return_value=(mock_up, session),
    ):
        res_blob.upload_from_file(io.BytesIO(b"x"))

    with _helpers._suppress_body_size():
        session.request.side_effect = [
            _media_response(
                b"sup",
                status_code=200,
                headers={
                    "x-goog-generation": "7",
                    "x-goog-hash": f"crc32c={_crc32c_b64(b'sup')}",
                },
                streaming=True,
            ),
            _json_response({"name": "o1", "size": "3"}),
            _media_response(b"", status_code=200, headers={"location": session_uri}),
            _json_response({"name": "o1", "size": "3", "crc32c": _crc32c_b64(b"sup")}),
        ]
        blob.download_to_file(io.BytesIO())
        blob.upload_from_string(b"sup")
        res_blob.upload_from_file(io.BytesIO(b"sup"))

    pts = _collect_metrics(reader)
    ops = pts["gcp.storage.client.operations"]
    assert not any(p.attributes["gcp.storage.operation"] == "DeleteObject" for p in ops)
    op_err_pairs = {
        (p.attributes["gcp.storage.operation"], p.attributes["error.type"]) for p in ops
    }
    assert ("ReadObject", "NOT_FOUND") in op_err_pairs
    assert ("ReadObject", "CHECKSUM_MISMATCH") in op_err_pairs
    assert ("WriteObject", "CHECKSUM_MISMATCH") in op_err_pairs
    resp_pts = pts["gcp.storage.client.response.body.size"]
    assert sum(p.sum for p in resp_pts) == 6 * len(payload)
    assert sum(p.count for p in resp_pts) == 6
    req_pts = pts["gcp.storage.client.request.body.size"]
    assert sum(p.sum for p in req_pts) == len(res_data) + 4 * 9
    assert sum(p.count for p in req_pts) == 5


def test_primary_exception_pinning_and_resumable_cleanup_chaining(metrics_env):
    client, session, reader = metrics_env
    bucket = client.bucket("r1-bucket")
    session_uri = "https://storage.googleapis.com/upload/storage/v1/b/r1-bucket/o?uploadType=resumable&upload_id=r1"

    _helpers._record_primary_exception(
        RuntimeError("outside-op"), RuntimeError("outside-cleanup")
    )
    c1 = RuntimeError("cleanup-1")
    c2 = RuntimeError("cleanup-2")
    c2.__context__ = c1
    with pytest.raises(RuntimeError, match="cleanup-2"):
        with _helpers._start_storage_operation(client, "outer.chained", "WriteObject"):
            _helpers._record_primary_exception(ValueError("first-pin"), c1)
            _helpers._record_primary_exception(KeyError("second-ignored"), c2)
            with pytest.raises(RuntimeError, match="nested-boom"):
                with _helpers._start_storage_operation(
                    client, "inner.method", "DeleteObject"
                ):
                    raise RuntimeError("nested-boom")
            raise c2

    with pytest.raises(ValueError, match="unrelated-after-caught"):
        with _helpers._start_storage_operation(client, "outer.caught", "WriteObject"):
            _helpers._record_primary_exception(
                DataCorruption(mock.Mock(), "stale"), RuntimeError("caught-cleanup")
            )
            raise ValueError("unrelated-after-caught")

    c_second = RuntimeError("independent-cleanup")
    with pytest.raises(RuntimeError, match="independent-cleanup"):
        with _helpers._start_storage_operation(client, "outer.repinned", "WriteObject"):
            _helpers._record_primary_exception(
                ValueError("caught-pin"), RuntimeError("caught-cleanup")
            )
            _helpers._record_primary_exception(KeyError("fresh-pin"), c_second)
            raise c_second

    res_blob = bucket.blob("corrupt-cleanup-err", chunk_size=256 * 1024)
    session.request.side_effect = [
        _media_response(b"", status_code=200, headers={"location": session_uri}),
    ]
    corrupt_exc = DataCorruption(mock.Mock(), "bad crc")
    mid_conn_exc = requests.ConnectionError("delete retry transport failure")
    top_cleanup_exc = Forbidden("delete denied after retry")

    def _chained_delete(*args, **kwargs):
        try:
            raise mid_conn_exc
        except requests.ConnectionError:
            raise top_cleanup_exc

    with (
        mock.patch.object(
            ResumableUpload,
            "transmit_next_chunk",
            side_effect=corrupt_exc,
        ),
        mock.patch.object(res_blob, "delete", side_effect=_chained_delete),
    ):
        with pytest.raises(Forbidden) as exc_info:
            res_blob.upload_from_file(io.BytesIO(b"bad"), retry=None)
    assert exc_info.value is top_cleanup_exc
    assert exc_info.value.__context__ is mid_conn_exc
    assert exc_info.value.__context__.__context__ is corrupt_exc

    pts = _collect_metrics(reader)
    by_method_err = {
        (
            p.attributes["gcp.client.method"],
            p.attributes["gcp.storage.operation"],
            p.attributes["error.type"],
        ): p.value
        for p in pts["gcp.storage.client.operations"]
    }
    assert (
        "outer.chained",
        "WriteObject",
        "CLIENT_VALIDATION_ERROR",
    ) in by_method_err
    assert (
        "outer.caught",
        "WriteObject",
        "CLIENT_VALIDATION_ERROR",
    ) in by_method_err
    assert (
        "outer.repinned",
        "WriteObject",
        "UNKNOWN",
    ) in by_method_err
    assert (
        "storage.Blob.upload_from_file",
        "WriteObject",
        "CHECKSUM_MISMATCH",
    ) in by_method_err
