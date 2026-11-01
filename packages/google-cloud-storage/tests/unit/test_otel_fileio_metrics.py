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

"""Unit tests for OpenTelemetry streaming file I/O (BlobReader, BlobWriter, Blob.open) metrics."""

import base64
import gc
import http.client
import io
import json
from unittest import mock

import google_crc32c
import pytest
import requests
from google.auth import credentials as auth_credentials
from google.cloud.exceptions import NotFound
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import InMemoryMetricReader

from google.cloud.storage import _helpers, _opentelemetry_metrics, fileio
from google.cloud.storage._media.requests import _request_helpers
from google.cloud.storage.client import Client
from google.cloud.storage.exceptions import InvalidResponse


def _make_credentials():
    return auth_credentials.AnonymousCredentials()


def _crc32c_b64(data: bytes) -> str:
    checksum = google_crc32c.Checksum(data)
    return base64.b64encode(checksum.digest()).decode("ascii")


class _FakeRawStream:
    """Minimal urllib3-like raw response backing streaming chunk reads."""

    def __init__(self, chunks):
        self._chunks = list(chunks)
        self.headers = {}

    def stream(self, amt=8192, decode_content=None):
        for chunk in self._chunks:
            yield chunk


def _media_response(
    body=b"",
    status_code=http.client.OK,
    headers=None,
    streaming=False,
):
    response = requests.Response()
    response.status_code = status_code
    response.headers.update(headers or {})
    chunk_list = [body] if body else []
    response.raw = _FakeRawStream(chunk_list)
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


def test_bind_suboperation_context_branches(metrics_env):
    client, session, _ = metrics_env
    recorder = client._metrics_recorder

    with _helpers._suppress_internal_metrics():
        with _helpers._bind_suboperation_context(
            client, "storage.fileio.BlobReader", "ReadObject"
        ) as st:
            assert st is None

    disabled_client = Client(
        project="test-project",
        credentials=_make_credentials(),
        _http=mock.MagicMock(),
        enable_metrics=False,
    )
    disabled_client._bucket_metadata_cache = None
    with _helpers._bind_suboperation_context(
        disabled_client, "storage.fileio.BlobReader", "ReadObject"
    ) as st:
        assert st is None
    disabled_client.close()

    plain_transport = mock.MagicMock(spec=["request"])
    with _helpers._bind_suboperation_context(
        client, "storage.fileio.BlobReader", "ReadObject"
    ) as st:
        assert st is not None
        assert _helpers._SUPPRESS_BODY_SIZE.get() is True
        assert _request_helpers.resolve_transport_recorder(plain_transport) is recorder
    assert _helpers._SUPPRESS_BODY_SIZE.get() is False
    assert st.finished is True


def test_blob_open_and_fileio_stream_lifetime_metrics(metrics_env):
    client, session, reader = metrics_env
    bucket = client.bucket("b1")

    # 1. Blob.open validation errors before stream construction
    b_open = bucket.blob("open-validate")
    invalid_open_calls = [
        (
            {"mode": "rb", "encoding": "utf-8"},
            ValueError,
            "ReadObject",
            "CLIENT_VALIDATION_ERROR",
        ),
        (
            {"mode": "rb", "ignore_flush": True},
            ValueError,
            "ReadObject",
            "CLIENT_VALIDATION_ERROR",
        ),
        (
            {"mode": "wb", "encoding": "utf-8"},
            ValueError,
            "WriteObject",
            "CLIENT_VALIDATION_ERROR",
        ),
        (
            {"mode": "rt", "ignore_flush": True},
            ValueError,
            "ReadObject",
            "CLIENT_VALIDATION_ERROR",
        ),
        (
            {"mode": "wt", "ignore_flush": False},
            ValueError,
            "WriteObject",
            "CLIENT_VALIDATION_ERROR",
        ),
        ({"mode": "rw"}, NotImplementedError, "ReadObject", "UNKNOWN"),
        ({"mode": "wx"}, NotImplementedError, "WriteObject", "UNKNOWN"),
        ({"mode": "ab"}, NotImplementedError, "UNKNOWN", "UNKNOWN"),
    ]
    for kwargs, exc_cls, expected_op, expected_err in invalid_open_calls:
        with pytest.raises(exc_cls):
            b_open.open(**kwargs)
    pts_val = _collect_metrics(reader)
    assert sum(p.value for p in pts_val["gcp.storage.client.operations"]) == len(
        invalid_open_calls
    )
    seen_pairs = [
        (p.attributes["gcp.storage.operation"], p.attributes["error.type"])
        for p in pts_val["gcp.storage.client.operations"]
    ]
    for _, _, expected_op, expected_err in invalid_open_calls:
        assert (expected_op, expected_err) in seen_pairs

    # 2. Blob.open TextIOWrapper construction failure cleans up raw_reader / raw_writer
    with pytest.raises(ValueError):
        b_open.open("rt", newline="invalid-newline")
    with pytest.raises(ValueError):
        b_open.open("wt", newline="invalid-newline")

    # 3. Blob.open("rb"), ("rt"), ("wb"), ("wt") attribute stream lifetime to storage.Blob.open
    #    and record exact caller-consumed / caller-written bytes (not prefetched bytes!)
    read_blob = bucket.blob("stream-read")
    session.request.side_effect = [
        _media_response(
            b"01234567",
            status_code=http.client.PARTIAL_CONTENT,
            headers={"x-goog-generation": "1", "content-range": "bytes 0-7/16"},
            streaming=True,
        ),
        _media_response(
            b"hello",
            status_code=http.client.PARTIAL_CONTENT,
            headers={"x-goog-generation": "1", "content-range": "bytes 0-4/5"},
            streaming=True,
        ),
        _json_response(
            {"error": {"message": "range not satisfiable"}}, status_code=416
        ),
    ]
    with read_blob.open("rb", chunk_size=8) as r_bin:
        assert r_bin.read1(3) == b"012"
    r_bin.close()  # Idempotent second close emits nothing

    with read_blob.open("rt", chunk_size=8, encoding="utf-8") as r_txt:
        assert r_txt.read() == "hello"

    write_blob = bucket.blob("stream-write")
    session_uri = "https://storage.googleapis.com/upload/storage/v1/b/b1/o?uploadType=resumable&upload_id=w1"
    chunk_sz = 256 * 1024
    wb_payload = b"x" * chunk_sz + b"12345"
    session.request.side_effect = [
        _media_response(b"", status_code=200, headers={"location": session_uri}),
        _media_response(
            b"",
            status_code=http.client.PERMANENT_REDIRECT,
            headers={"range": f"bytes=0-{chunk_sz - 1}"},
        ),
        _json_response(
            {
                "name": "stream-write",
                "size": str(chunk_sz + 5),
                "crc32c": _crc32c_b64(wb_payload),
            }
        ),
        _media_response(b"", status_code=200, headers={"location": session_uri}),
        _json_response(
            {
                "name": "stream-write",
                "size": "4",
                "crc32c": _crc32c_b64(b"text"),
            }
        ),
    ]
    with write_blob.open("wb", chunk_size=chunk_sz) as w_bin:
        w_bin.write(b"x" * chunk_sz + b"12345")
    w_bin.close()  # Idempotent second close

    with write_blob.open("wt", encoding="utf-8") as w_txt:
        w_txt.write("text")

    pts_streams = _collect_metrics(reader)
    resp_pts = [
        p
        for p in pts_streams["gcp.storage.client.response.body.size"]
        if p.attributes["gcp.client.method"] == "storage.Blob.open"
    ]
    assert sum(p.sum for p in resp_pts) == 8
    assert sum(p.count for p in resp_pts) == 2

    req_pts = [
        p
        for p in pts_streams["gcp.storage.client.request.body.size"]
        if p.attributes["gcp.client.method"] == "storage.Blob.open"
    ]
    assert sum(p.sum for p in req_pts) == (chunk_sz + 5) + 4
    assert sum(p.count for p in req_pts) == 2


def test_direct_blob_reader_and_writer_edge_cases_and_errors(metrics_env):
    client, session, reader = metrics_env
    bucket = client.bucket("b1")
    blob = bucket.blob("direct-fileio")

    # 1. Suppressed / disabled BlobReader & BlobWriter construction (with valid kwargs)
    with _helpers._suppress_internal_metrics():
        sup_r = fileio.BlobReader(blob, raw_download=True)
        sup_r.close()
        sup_w = fileio.BlobWriter(blob, content_type="text/plain")
        sup_w.terminate()

    # 2. Invalid constructor arguments on direct BlobReader & BlobWriter
    with pytest.raises(ValueError):
        fileio.BlobReader(blob, unsupported_kwarg=123)
    with pytest.raises(ValueError):
        fileio.BlobWriter(blob, unsupported_kwarg=123)
    with pytest.raises(ValueError):
        fileio.BlobWriter(blob, chunk_size=100)  # Not a multiple of 256 KiB

    # 3. BlobReader seek(whence=2) triggering blob.reload() (success & failure) + invalid whence
    seek_blob = bucket.blob("seek-blob")
    session.request.side_effect = [
        _json_response({"name": "seek-blob", "size": "10", "generation": "1"}),
    ]
    sr = fileio.BlobReader(seek_blob, chunk_size=4)
    assert sr.seek(-2, 2) == 8
    with pytest.raises(ValueError):
        sr.seek(0, 99)
    sr.close()

    seek_fail_blob = bucket.blob("seek-fail")
    session.request.side_effect = [
        _json_response({"error": {"message": "missing"}}, status_code=404),
    ]
    sr_fail = fileio.BlobReader(seek_fail_blob, retry=None)
    with pytest.raises(NotFound):
        sr_fail.seek(0, 2)
    sr_fail.close()

    # 4. BlobReader mid-stream read error (with 0 bytes read vs >0 bytes read)
    err_blob = bucket.blob("read-err")
    session.request.side_effect = [
        _json_response({"error": {"message": "missing"}}, status_code=404),
        _media_response(
            b"abcd",
            status_code=http.client.PARTIAL_CONTENT,
            headers={"x-goog-generation": "1", "content-range": "bytes 0-3/8"},
            streaming=True,
        ),
        _json_response({"error": {"message": "gone"}}, status_code=404),
    ]
    r_zero = fileio.BlobReader(err_blob, chunk_size=4, retry=None)
    with pytest.raises(NotFound):
        r_zero.read(4)
    r_zero.close()

    r_partial = fileio.BlobReader(err_blob, chunk_size=4, retry=None)
    assert r_partial.read(4) == b"abcd"
    with pytest.raises(NotFound):
        r_partial.read(4)
    r_partial.close()

    # 5. BlobWriter terminate, write error, and close error
    session_uri = "https://storage.googleapis.com/upload/storage/v1/b/b1/o?uploadType=resumable&upload_id=term1"
    chunk_sz = 256 * 1024

    w_cancel_early = fileio.BlobWriter(blob, chunk_size=chunk_sz)
    w_cancel_early.terminate()

    session.request.side_effect = [
        _media_response(b"", status_code=200, headers={"location": session_uri}),
        _media_response(
            b"",
            status_code=http.client.PERMANENT_REDIRECT,
            headers={"range": f"bytes=0-{chunk_sz - 1}"},
        ),
    ]
    session.delete.return_value = _json_response(None, status_code=499)
    w_cancel_active = fileio.BlobWriter(blob, chunk_size=chunk_sz)
    w_cancel_active.write(b"a" * chunk_sz)
    w_cancel_active.terminate()
    session.delete.assert_called_once()

    session.request.side_effect = [
        _json_response({"error": {"message": "denied"}}, status_code=403),
    ]
    with pytest.raises(InvalidResponse):
        with fileio.BlobWriter(blob, chunk_size=chunk_sz, retry=None) as w_err:
            w_err.write(b"a" * chunk_sz)

    session.request.side_effect = [
        _json_response({"error": {"message": "unavailable"}}, status_code=503),
    ]
    w_close_err = fileio.BlobWriter(blob, chunk_size=chunk_sz, retry=None)
    w_close_err.write(b"small")
    with pytest.raises(InvalidResponse):
        w_close_err.close()

    pts = _collect_metrics(reader)
    reader_ops = [
        p
        for p in pts["gcp.storage.client.operations"]
        if p.attributes["gcp.client.method"] == "storage.fileio.BlobReader"
    ]
    writer_ops = [
        p
        for p in pts["gcp.storage.client.operations"]
        if p.attributes["gcp.client.method"] == "storage.fileio.BlobWriter"
    ]
    assert sum(p.value for p in reader_ops) == 5
    assert sum(p.value for p in writer_ops) == 6
    cancelled_pts = [p for p in writer_ops if p.attributes["error.type"] == "CANCELLED"]
    assert sum(p.value for p in cancelled_pts) == 2
    assert not any(
        p.attributes["gcp.storage.operation"] == "GetObject"
        for p in pts["gcp.storage.client.operations"]
    )


def test_text_io_wrapper_gc_safety_and_error_recovery(metrics_env):
    client, session, reader = metrics_env
    bucket = client.bucket("b1")
    session_uri = "https://storage.googleapis.com/upload/storage/v1/b/b1/o?uploadType=resumable&upload_id=txt1"

    # 1. Disabled client preserves exact stdlib io.TextIOWrapper; enabled uses _MetricsTextIOWrapper
    disabled_client = Client(
        project="test-project",
        credentials=_make_credentials(),
        _http=mock.MagicMock(),
        enable_metrics=False,
    )
    disabled_client._bucket_metadata_cache = None
    d_blob = disabled_client.bucket("b1").blob("plain-txt")
    t_read = d_blob.open("rt")
    t_write = d_blob.open("wt")
    assert type(t_read) is io.TextIOWrapper
    assert type(t_write) is io.TextIOWrapper
    t_read.close()
    t_write.buffer.terminate()
    disabled_client.close()

    # 2. _MetricsTextIOWrapper read, readline, seek(0), __next__, UnsupportedOperation, detached
    txt_blob = bucket.blob("txt-read")
    txt_blob._properties["size"] = 12
    session.request.side_effect = [
        _media_response(
            b"line1\nline2\n",
            status_code=http.client.PARTIAL_CONTENT,
            headers={"x-goog-generation": "1", "content-range": "bytes 0-11/12"},
            streaming=True,
        ),
        _json_response({"error": {"message": "eof"}}, status_code=416),
        _media_response(
            b"\xff\xfe",
            status_code=http.client.PARTIAL_CONTENT,
            headers={"x-goog-generation": "1", "content-range": "bytes 0-1/2"},
            streaming=True,
        ),
        _media_response(
            b"ok\n\xff\xfe",
            status_code=http.client.PARTIAL_CONTENT,
            headers={"x-goog-generation": "1", "content-range": "bytes 0-4/5"},
            streaming=True,
        ),
    ]
    with txt_blob.open("rt", chunk_size=16, encoding="utf-8") as f_ok:
        assert type(f_ok) is fileio._MetricsTextIOWrapper
        assert f_ok.seek(0) == 0
        assert f_ok.readline() == "line1\n"
        assert list(f_ok) == ["line2\n"]

    with pytest.raises(UnicodeDecodeError):
        with txt_blob.open("rt", chunk_size=16, encoding="utf-8") as f_bad_read:
            f_bad_read.read()

    with pytest.raises(UnicodeDecodeError):
        with txt_blob.open("rt", chunk_size=16, encoding="utf-8") as f_bad_iter:
            list(f_bad_iter)

    with pytest.raises(io.UnsupportedOperation):
        with txt_blob.open("rt", chunk_size=16, encoding="utf-8") as f_bad_seek:
            f_bad_seek.seek(1, io.SEEK_CUR)

    with pytest.raises(io.UnsupportedOperation):
        with txt_blob.open("rt", chunk_size=16, encoding="utf-8") as f_bad_trunc:
            f_bad_trunc.truncate()

    f_detached = txt_blob.open("rt", chunk_size=16, encoding="utf-8")
    raw_detached = f_detached.detach()
    with pytest.raises(ValueError, match="detached"):
        f_detached.read()
    with pytest.raises(ValueError, match="detached"):
        next(f_detached)
    del f_detached
    gc.collect()
    raw_detached.close()

    # 3. _MetricsTextIOWrapper write, writelines, UnicodeEncodeError abort, context-exit abort,
    #    closed exit, and BlobWriter.close() primary error preservation
    chunk_sz = 256 * 1024
    w_txt_blob = bucket.blob("txt-write")
    session.request.side_effect = [
        _media_response(b"", status_code=200, headers={"location": session_uri}),
        _json_response(
            {"name": "txt-write", "size": "6", "crc32c": _crc32c_b64(b"a\nb\nc\n")}
        ),
        _media_response(b"", status_code=200, headers={"location": session_uri}),
        _json_response(
            {"name": "txt-write", "size": "2", "crc32c": _crc32c_b64(b"hi")}
        ),
    ]
    with w_txt_blob.open("wt", encoding="ascii") as fw_ok:
        fw_ok.writelines(["a\n", "b\n"])
        fw_ok.write("c\n")

    session.request.reset_mock()
    session.request.side_effect = None
    with pytest.raises(UnicodeEncodeError):
        with w_txt_blob.open("wt", encoding="ascii") as fw_enc_err:
            fw_enc_err.write("\u2603")
    assert session.request.call_count == 0
    assert fw_enc_err.closed

    with pytest.raises(RuntimeError, match="caller-boom"):
        with w_txt_blob.open("wt", encoding="utf-8") as fw_abort:
            fw_abort.write("buffered-data-never-flushed")
            raise RuntimeError("caller-boom")
    assert session.request.call_count == 0
    assert fw_abort.closed

    session.request.side_effect = [
        _media_response(b"", status_code=200, headers={"location": session_uri}),
        _json_response(
            {"name": "txt-write", "size": "2", "crc32c": _crc32c_b64(b"hi")}
        ),
    ]
    with pytest.raises(RuntimeError, match="after-explicit-close"):
        with w_txt_blob.open("wt", encoding="utf-8") as fw_already_closed:
            fw_already_closed.write("hi")
            fw_already_closed.close()
            raise RuntimeError("after-explicit-close")

    session.request.side_effect = [
        _media_response(b"", status_code=200, headers={"location": session_uri}),
        _json_response({"error": {"message": "forbidden"}}, status_code=403),
    ]
    fw_flush_403 = w_txt_blob.open(
        "wt", encoding="ascii", chunk_size=chunk_sz, retry=None
    )
    fw_flush_403.buffer.write(b"a" * (chunk_sz - 2))
    fw_flush_403.write("bc")
    with pytest.raises(ValueError, match="invalid state"):
        fw_flush_403.close()

    session.request.side_effect = [
        _json_response({"error": {"message": "unavailable"}}, status_code=503),
    ]
    fw_close_503 = w_txt_blob.open(
        "wt", encoding="ascii", chunk_size=chunk_sz, retry=None
    )
    fw_close_503.write("ok")
    with pytest.raises(UnicodeEncodeError):
        fw_close_503.write("\u2603")
    with pytest.raises(InvalidResponse):
        fw_close_503.close()

    # 4. GC safety (__del__) on unclosed streams
    pts_before_gc = _collect_metrics(reader)
    ops_before_gc = sum(p.value for p in pts_before_gc["gcp.storage.client.operations"])
    session.request.reset_mock()
    session.request.side_effect = AssertionError("GC must never trigger network I/O")

    unclosed_r = fileio.BlobReader(bucket.blob("gc-r"))
    unclosed_w = fileio.BlobWriter(bucket.blob("gc-w"))
    unclosed_w.write(b"unflushed")
    uninit_r = fileio.BlobReader.__new__(fileio.BlobReader)
    unclosed_tw = bucket.blob("gc-tw").open("wt")
    unclosed_tw.write("unflushed-text")
    del unclosed_r, unclosed_w, uninit_r, unclosed_tw
    gc.collect()

    assert session.request.call_count == 0
    pts_after_gc = _collect_metrics(reader)
    ops_after_gc = sum(p.value for p in pts_after_gc["gcp.storage.client.operations"])
    assert ops_after_gc == ops_before_gc

    # 5. BlobWriter.terminate() finalizes CANCELLED metric and closes buffer even if transport.delete raises
    session.request.side_effect = [
        _media_response(b"", status_code=200, headers={"location": session_uri}),
        _media_response(
            b"",
            status_code=http.client.PERMANENT_REDIRECT,
            headers={"range": f"bytes=0-{chunk_sz - 1}"},
        ),
    ]
    session.delete.side_effect = requests.ConnectionError("abort transport down")
    w_term_err = fileio.BlobWriter(bucket.blob("term-err"), chunk_size=chunk_sz)
    w_term_err.write(b"x" * chunk_sz)
    with pytest.raises(requests.ConnectionError, match="abort transport down"):
        w_term_err.terminate()
    assert w_term_err.closed
    session.delete.side_effect = None

    # 6. Transient error recovery on BlobReader & BlobWriter
    rec_r_blob = bucket.blob("recover-read")
    rec_r_blob._properties["size"] = 4
    session.request.side_effect = [
        _json_response({"error": {"message": "transient"}}, status_code=404),
        _media_response(
            b"good",
            status_code=http.client.PARTIAL_CONTENT,
            headers={"x-goog-generation": "1", "content-range": "bytes 0-3/4"},
            streaming=True,
        ),
    ]
    rec_r = fileio.BlobReader(rec_r_blob, chunk_size=4, retry=None)
    with pytest.raises(ValueError):
        rec_r.seek(0, 99)
    with pytest.raises(NotFound):
        rec_r.read(4)
    assert rec_r.read(4) == b"good"
    rec_r.close()

    rec_w_blob = bucket.blob("recover-write")
    w_data = b"a" * chunk_sz + b"b" * chunk_sz
    session.request.side_effect = [
        _json_response({"error": {"message": "transient"}}, status_code=503),
        _media_response(b"", status_code=200, headers={"location": session_uri}),
        _media_response(
            b"",
            status_code=http.client.PERMANENT_REDIRECT,
            headers={"range": f"bytes=0-{chunk_sz - 1}"},
        ),
        _media_response(
            b"",
            status_code=http.client.PERMANENT_REDIRECT,
            headers={"range": f"bytes=0-{2 * chunk_sz - 1}"},
        ),
        _json_response(
            {
                "name": "recover-write",
                "size": str(2 * chunk_sz),
                "crc32c": _crc32c_b64(w_data),
            }
        ),
    ]
    rec_w = fileio.BlobWriter(rec_w_blob, chunk_size=chunk_sz, retry=None)
    with pytest.raises(InvalidResponse):
        rec_w.write(b"a" * chunk_sz)
    rec_w.write(b"b" * chunk_sz)
    rec_w.close()

    pts_final = _collect_metrics(reader)
    r_ok = [
        p
        for p in pts_final["gcp.storage.client.operations"]
        if p.attributes["gcp.client.method"] == "storage.fileio.BlobReader"
        and p.attributes["error.type"] == "OK"
    ]
    assert sum(p.value for p in r_ok) == 1
    w_ops = [
        p
        for p in pts_final["gcp.storage.client.operations"]
        if p.attributes["gcp.client.method"] == "storage.fileio.BlobWriter"
    ]
    assert {(p.attributes["error.type"], p.value) for p in w_ops} == {
        ("CANCELLED", 1),
        ("OK", 1),
    }
    open_ops = [
        p
        for p in pts_final["gcp.storage.client.operations"]
        if p.attributes["gcp.client.method"] == "storage.Blob.open"
    ]
    open_by_pair = {}
    for p in open_ops:
        k = (p.attributes["gcp.storage.operation"], p.attributes["error.type"])
        open_by_pair[k] = open_by_pair.get(k, 0) + p.value
    assert open_by_pair == {
        ("ReadObject", "OK"): 2,
        ("ReadObject", "CLIENT_VALIDATION_ERROR"): 2,
        ("ReadObject", "CONNECTION_ERROR"): 2,
        ("WriteObject", "OK"): 2,
        ("WriteObject", "CLIENT_VALIDATION_ERROR"): 1,
        ("WriteObject", "CANCELLED"): 1,
        ("WriteObject", "PERMISSION_DENIED"): 1,
        ("WriteObject", "UNAVAILABLE"): 1,
    }
