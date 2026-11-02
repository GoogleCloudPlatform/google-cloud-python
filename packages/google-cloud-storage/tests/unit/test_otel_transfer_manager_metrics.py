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

"""Unit tests for OpenTelemetry transfer_manager concurrent and multiprocessing metrics."""

import base64
import concurrent.futures
import http.client
import io
import json
from unittest import mock

import google_crc32c
import pytest
import requests
from google.auth import credentials as auth_credentials
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import InMemoryMetricReader

from google.cloud.storage import (
    _helpers,
    _opentelemetry_metrics,
    transfer_manager,
)
from google.cloud.storage._media.requests.upload import XMLMPUContainer, XMLMPUPart
from google.cloud.storage.client import Client
from google.cloud.storage.exceptions import DataCorruption, InvalidResponse


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


def test_transfer_manager_many_operations_thread_and_process(metrics_env, tmp_path):
    client, session, reader = metrics_env
    bucket = client.bucket("tm-bucket")

    f1 = tmp_path / "u1.txt"
    f1.write_bytes(b"file-1")
    f2 = tmp_path / "u2.txt"
    f2.write_bytes(b"file-2")

    # 1. upload_many (THREAD) with filename (multipart) + BytesIO (resumable)
    tm_res_uri = "https://storage.googleapis.com/upload/storage/v1/b/tm-bucket/o?uploadType=resumable&upload_id=tm1"

    def _tm_upload_transport(method, url, **kw):
        if method == "POST" and "uploadType=resumable" in url:
            return _media_response(
                b"", status_code=200, headers={"location": tm_res_uri}
            )
        if method == "PUT":
            return _json_response(
                {"name": "b2", "size": "5", "crc32c": _crc32c_b64(b"mem-2")}
            )
        return _json_response({"name": "b1", "size": "6"})

    session.request.side_effect = _tm_upload_transport
    res_up = transfer_manager.upload_many(
        [(str(f1), bucket.blob("b1")), (io.BytesIO(b"mem-2"), bucket.blob("b2"))],
        worker_type=transfer_manager.THREAD,
        max_workers=2,
        raise_exception=True,
    )
    assert res_up == [None, None]

    # 2. upload_many_from_filenames (THREAD) attributes gcp.client.method properly
    session.request.side_effect = lambda method, url, **kw: _json_response(
        {"name": "uploaded", "size": "6"}
    )
    transfer_manager.upload_many_from_filenames(
        bucket,
        ["u1.txt", "u2.txt"],
        source_directory=str(tmp_path),
        worker_type=transfer_manager.THREAD,
        max_workers=2,
        raise_exception=True,
    )

    # 3. download_many (THREAD) with filename, skipped existing file, and BytesIO
    existing_dest = tmp_path / "already_exists.txt"
    existing_dest.write_bytes(b"keep")
    new_dest = tmp_path / "d1.txt"
    payload = b"dl-bytes"
    crc_hdr = f"crc32c={_crc32c_b64(payload)}"
    session.request.side_effect = lambda method, url, **kw: _media_response(
        payload,
        status_code=200,
        headers={"x-goog-generation": "1", "x-goog-hash": crc_hdr},
        streaming=True,
    )
    mem_out = io.BytesIO()
    transfer_manager.download_many(
        [
            (bucket.blob("skip-me"), str(existing_dest)),
            (bucket.blob("d1"), str(new_dest)),
            (bucket.blob("d2"), mem_out),
        ],
        skip_if_exists=True,
        worker_type=transfer_manager.THREAD,
        max_workers=2,
        raise_exception=True,
    )
    assert new_dest.read_bytes() == payload
    assert mem_out.getvalue() == payload

    # 4. download_many_to_path (THREAD) attributes gcp.client.method properly
    dl_dir = tmp_path / "dl_dir"
    dl_dir.mkdir()
    session.request.side_effect = [
        _media_response(
            payload,
            status_code=200,
            headers={"x-goog-generation": "1", "x-goog-hash": crc_hdr},
            streaming=True,
        ),
    ]
    transfer_manager.download_many_to_path(
        bucket,
        ["p1.txt"],
        destination_directory=str(dl_dir),
        worker_type=transfer_manager.THREAD,
        max_workers=1,
        raise_exception=True,
    )
    assert (dl_dir / "p1.txt").read_bytes() == payload

    # 5. PROCESS worker_type pickling branches
    with pytest.raises(ValueError):
        transfer_manager.upload_many(
            [(io.BytesIO(b"bad"), bucket.blob("bad"))],
            worker_type=transfer_manager.PROCESS,
        )
    with pytest.raises(ValueError):
        transfer_manager.download_many(
            [(bucket.blob("bad"), io.BytesIO())],
            worker_type=transfer_manager.PROCESS,
        )

    proc_client = Client(
        project="test-project",
        credentials=_make_credentials(),
        enable_metrics=False,
    )
    proc_client._bucket_metadata_cache = None
    proc_bucket = proc_client.bucket("proc-b")
    proc_dest = tmp_path / "proc_dl.txt"
    with mock.patch(
        "google.cloud.storage.transfer_manager._get_pool_class_and_requirements",
        return_value=(concurrent.futures.ThreadPoolExecutor, True),
    ):
        with mock.patch.object(
            transfer_manager.Blob, "_handle_filename_and_upload", return_value=None
        ):
            transfer_manager.upload_many(
                [(str(f1), proc_bucket.blob("pb1"))],
                worker_type=transfer_manager.PROCESS,
                max_workers=1,
                raise_exception=True,
            )
        with mock.patch.object(
            transfer_manager.Blob, "_handle_filename_and_download", return_value=None
        ):
            transfer_manager.download_many(
                [(proc_bucket.blob("pb1"), str(proc_dest))],
                worker_type=transfer_manager.PROCESS,
                max_workers=1,
                raise_exception=True,
            )
    proc_client.close()

    pts = _collect_metrics(reader)
    by_method = {}
    for p in pts["gcp.storage.client.operations"]:
        key = (
            p.attributes["gcp.client.method"],
            p.attributes["gcp.storage.operation"],
        )
        by_method[key] = by_method.get(key, 0) + p.value

    assert by_method == {
        ("storage.transfer_manager.upload_many", "WriteObject"): 2,
        ("storage.transfer_manager.upload_many_from_filenames", "WriteObject"): 2,
        ("storage.transfer_manager.download_many", "ReadObject"): 2,
        ("storage.transfer_manager.download_many_to_path", "ReadObject"): 1,
    }


def test_transfer_manager_concurrent_chunked_operations(metrics_env, tmp_path):
    client, session, reader = metrics_env
    bucket = client.bucket("chunked-bucket")

    # 1. download_chunks_concurrently validation errors -> CLIENT_VALIDATION_ERROR
    v_blob = bucket.blob("val-blob")
    with pytest.raises(ValueError):
        transfer_manager.download_chunks_concurrently(
            v_blob, str(tmp_path / "v1"), download_kwargs={"start": 0}
        )
    with pytest.raises(ValueError):
        transfer_manager.download_chunks_concurrently(
            v_blob, str(tmp_path / "v2"), download_kwargs={"checksum": "md5"}
        )

    # 2. download_chunks_concurrently (THREAD): reload + 2 shards -> 1 ReadObject, 1 body size, 3 HTTP attempts
    full_data = b"0123456789"
    full_crc = _crc32c_b64(full_data)
    d_blob = bucket.blob("sharded-dl")

    def _sharded_get(method, url, **kwargs):
        if "/storage/v1/b/" in url and "/download/" not in url:
            return _json_response(
                {
                    "name": "sharded-dl",
                    "size": "10",
                    "generation": "42",
                    "crc32c": full_crc,
                }
            )
        rng = (kwargs.get("headers") or {}).get("range", "")
        if rng == "bytes=0-5":
            return _media_response(
                b"012345",
                status_code=http.client.PARTIAL_CONTENT,
                headers={"content-range": "bytes 0-5/10", "x-goog-generation": "42"},
                streaming=True,
            )
        return _media_response(
            b"6789",
            status_code=http.client.PARTIAL_CONTENT,
            headers={"content-range": "bytes 6-9/10", "x-goog-generation": "42"},
            streaming=True,
        )

    session.request.side_effect = _sharded_get
    dl_target = tmp_path / "sharded_out.bin"
    transfer_manager.download_chunks_concurrently(
        d_blob,
        str(dl_target),
        chunk_size=6,
        worker_type=transfer_manager.THREAD,
        max_workers=2,
        crc32c_checksum=True,
    )
    assert dl_target.read_bytes() == full_data

    # 3. download_chunks_concurrently CRC32C mismatch -> CHECKSUM_MISMATCH, no body size recorded
    bad_blob = bucket.blob("bad-crc")
    bad_blob._properties.update(
        {"size": 4, "generation": "9", "crc32c": _crc32c_b64(b"zzzz")}
    )
    session.request.side_effect = [
        _media_response(
            b"abcd",
            status_code=http.client.PARTIAL_CONTENT,
            headers={"content-range": "bytes 0-3/4", "x-goog-generation": "9"},
            streaming=True,
        )
    ]
    with pytest.raises(DataCorruption):
        transfer_manager.download_chunks_concurrently(
            bad_blob,
            str(tmp_path / "bad_crc.bin"),
            chunk_size=4,
            worker_type=transfer_manager.THREAD,
            max_workers=1,
            crc32c_checksum=True,
        )

    # 4. upload_chunks_concurrently (THREAD): initiate + 2 parts + finalize -> 1 WriteObject, 1 body size, 4 attempts
    up_src = tmp_path / "sharded_up.bin"
    up_src.write_bytes(b"abcdefghij")
    u_blob = bucket.blob("sharded-up")
    u_blob._bucket = bucket.__class__(client, "chunked-bucket", user_project="up-proj")
    u_blob.kms_key_name = "projects/p/locations/l/keyRings/r/cryptoKeys/k"

    xml_ns = 'xmlns="http://s3.amazonaws.com/doc/2006-03-01/"'

    def _mpu_transport(method, url, **kwargs):
        if method == "POST" and "uploads" in url:
            return _media_response(
                f"<InitiateMultipartUploadResult {xml_ns}><UploadId>mpu-1</UploadId></InitiateMultipartUploadResult>".encode(
                    "utf-8"
                ),
                status_code=200,
            )
        if method == "PUT":
            part_bytes = kwargs.get("data", b"")
            return _media_response(
                b"",
                status_code=200,
                headers={
                    "ETag": '"part-etag"',
                    "x-goog-hash": f"crc32c={_crc32c_b64(part_bytes)}",
                },
            )
        return _media_response(
            f'<CompleteMultipartUploadResult {xml_ns}><ETag>"done"</ETag></CompleteMultipartUploadResult>'.encode(
                "utf-8"
            ),
            status_code=200,
        )

    session.request.side_effect = _mpu_transport
    transfer_manager.upload_chunks_concurrently(
        str(up_src),
        u_blob,
        chunk_size=6,
        worker_type=transfer_manager.THREAD,
        max_workers=2,
    )

    # 5. upload_chunks_concurrently part failure triggers suppressed container.cancel()
    def _mpu_fail_transport(method, url, **kwargs):
        if method == "POST" and "uploads" in url:
            return _media_response(
                f"<InitiateMultipartUploadResult {xml_ns}><UploadId>mpu-fail</UploadId></InitiateMultipartUploadResult>".encode(
                    "utf-8"
                ),
                status_code=200,
            )
        if method == "PUT":
            return _json_response({"error": {"message": "503"}}, status_code=503)
        return _media_response(b"", status_code=204)

    session.request.side_effect = _mpu_fail_transport
    with pytest.raises(InvalidResponse):
        transfer_manager.upload_chunks_concurrently(
            str(up_src),
            bucket.blob("sharded-up-fail"),
            chunk_size=10,
            worker_type=transfer_manager.THREAD,
            max_workers=1,
            retry=None,
        )

    # 6. PROCESS pickling & suppressed / disabled metrics branches for chunked helpers
    with _helpers._suppress_body_size():
        session.request.side_effect = _mpu_transport
        transfer_manager.upload_chunks_concurrently(
            str(up_src),
            bucket.blob("suppressed-body-up"),
            chunk_size=10,
            worker_type=transfer_manager.THREAD,
            max_workers=1,
        )
        zero_sharded = bucket.blob("zero-sharded")
        zero_sharded._properties.update({"size": 4, "generation": "1"})
        session.request.side_effect = [
            _media_response(
                b"0123",
                status_code=http.client.PARTIAL_CONTENT,
                headers={"content-range": "bytes 0-3/4", "x-goog-generation": "1"},
                streaming=True,
            )
        ]
        transfer_manager.download_chunks_concurrently(
            zero_sharded,
            str(tmp_path / "sup_dl.bin"),
            chunk_size=4,
            worker_type=transfer_manager.THREAD,
            max_workers=1,
            crc32c_checksum=False,
        )

    proc_client = Client(
        project="test-project",
        credentials=_make_credentials(),
        enable_metrics=False,
    )
    proc_client._bucket_metadata_cache = None
    p_blob = proc_client.bucket("pb").blob("po")
    p_blob._properties.update({"size": 4, "generation": "1"})
    with mock.patch(
        "google.cloud.storage.transfer_manager._get_pool_class_and_requirements",
        return_value=(concurrent.futures.ThreadPoolExecutor, True),
    ):
        with mock.patch.object(
            transfer_manager.Blob, "_prep_and_do_download", return_value=None
        ):
            transfer_manager.download_chunks_concurrently(
                p_blob,
                str(tmp_path / "proc_sharded.bin"),
                chunk_size=4,
                worker_type=transfer_manager.PROCESS,
                max_workers=1,
                crc32c_checksum=False,
            )
        with mock.patch.object(XMLMPUContainer, "initiate"):
            with mock.patch.object(XMLMPUContainer, "finalize"):
                with mock.patch.object(XMLMPUPart, "upload"):
                    transfer_manager.upload_chunks_concurrently(
                        str(up_src),
                        p_blob,
                        chunk_size=10,
                        worker_type=transfer_manager.PROCESS,
                        max_workers=1,
                    )
    proc_client.close()

    pts = _collect_metrics(reader)
    dl_chunk_ops = [
        p
        for p in pts["gcp.storage.client.operations"]
        if p.attributes["gcp.client.method"]
        == "storage.transfer_manager.download_chunks_concurrently"
    ]
    assert sum(p.value for p in dl_chunk_ops) == 5
    assert any(p.attributes["error.type"] == "CHECKSUM_MISMATCH" for p in dl_chunk_ops)

    up_chunk_ops = [
        p
        for p in pts["gcp.storage.client.operations"]
        if p.attributes["gcp.client.method"]
        == "storage.transfer_manager.upload_chunks_concurrently"
    ]
    assert sum(p.value for p in up_chunk_ops) == 3

    assert not any(
        p.attributes.get("http.request.method") == "DELETE"
        for p in pts["http.client.request.duration"]
    )
    resp_body = pts["gcp.storage.client.response.body.size"]
    assert sum(p.count for p in resp_body) == 1
    assert resp_body[0].sum == 10
    req_body = pts["gcp.storage.client.request.body.size"]
    assert sum(p.count for p in req_body) == 1
    assert req_body[0].sum == 10


def test_transfer_manager_cleanup_chaining_multiprocessing_and_lazy_client(
    metrics_env, tmp_path, monkeypatch
):
    client, session, reader = metrics_env
    bucket = client.bucket("r1-bucket")
    xml_ns = 'xmlns="http://s3.amazonaws.com/doc/2006-03-01/"'

    # 1. upload_chunks_concurrently where part upload raises 403 InvalidResponse AND container.cancel raises ConnectionError
    up_src = tmp_path / "mpu_cleanup.bin"
    up_src.write_bytes(b"0123456789")
    session.request.side_effect = [
        _media_response(
            f"<InitiateMultipartUploadResult {xml_ns}><UploadId>u-clean</UploadId></InitiateMultipartUploadResult>".encode(
                "utf-8"
            ),
            status_code=200,
        ),
        _json_response({"error": {"message": "part forbidden"}}, status_code=403),
        requests.ConnectionError("cancel network down"),
    ]
    with pytest.raises(requests.ConnectionError, match="cancel network down"):
        transfer_manager.upload_chunks_concurrently(
            str(up_src),
            bucket.blob("mpu-cleanup-err"),
            chunk_size=10,
            worker_type=transfer_manager.THREAD,
            max_workers=1,
            retry=None,
        )

    # 2. download_chunks_concurrently honors download_kwargs["client"]
    disabled_client = Client(
        project="test-project",
        credentials=_make_credentials(),
        _http=mock.MagicMock(),
        enable_metrics=False,
    )
    disabled_client._bucket_metadata_cache = None
    foreign_blob = disabled_client.bucket("r1-bucket").blob("foreign-sharded")
    full_bytes = b"abcdefgh"
    session.request.side_effect = [
        _json_response(
            {
                "name": "foreign-sharded",
                "size": "8",
                "generation": "5",
                "crc32c": _crc32c_b64(full_bytes),
            }
        ),
        _media_response(
            b"abcd",
            status_code=http.client.PARTIAL_CONTENT,
            headers={"content-range": "bytes 0-3/8", "x-goog-generation": "5"},
            streaming=True,
        ),
        _media_response(
            b"efgh",
            status_code=http.client.PARTIAL_CONTENT,
            headers={"content-range": "bytes 4-7/8", "x-goog-generation": "5"},
            streaming=True,
        ),
    ]
    foreign_out = tmp_path / "foreign_out.bin"
    transfer_manager.download_chunks_concurrently(
        foreign_blob,
        str(foreign_out),
        chunk_size=4,
        download_kwargs={"client": client},
        worker_type=transfer_manager.THREAD,
        max_workers=1,
        crc32c_checksum=True,
    )
    assert foreign_out.read_bytes() == full_bytes
    disabled_client.close()

    # 3. upload_many_from_filenames & download_many_to_path with needs_pickling=True,
    #    plus _suppress_internal_metrics() propagation across needs_pickling=True
    src_dir = tmp_path / "proc_src"
    src_dir.mkdir()
    (src_dir / "f1.txt").write_bytes(b"hello")
    dst_dir = tmp_path / "proc_dst"
    dst_dir.mkdir()

    with monkeypatch.context() as mp_cache:
        mp_cache.setattr(transfer_manager, "_cached_clients", {id(client): client})
        with mock.patch(
            "google.cloud.storage.transfer_manager._get_pool_class_and_requirements",
            return_value=(concurrent.futures.ThreadPoolExecutor, True),
        ):
            session.request.side_effect = [
                _json_response({"name": "f1.txt", "size": "5"}),
                _media_response(
                    b"hello",
                    status_code=200,
                    headers={
                        "x-goog-generation": "1",
                        "x-goog-hash": f"crc32c={_crc32c_b64(b'hello')}",
                    },
                    streaming=True,
                ),
            ]
            transfer_manager.upload_many_from_filenames(
                bucket,
                ["f1.txt"],
                source_directory=str(src_dir),
                worker_type=transfer_manager.PROCESS,
                max_workers=1,
                raise_exception=True,
            )
            transfer_manager.download_many_to_path(
                bucket,
                ["f1.txt"],
                destination_directory=str(dst_dir),
                worker_type=transfer_manager.PROCESS,
                max_workers=1,
                raise_exception=True,
            )
            assert (dst_dir / "f1.txt").read_bytes() == b"hello"

            pts_pre_sup = _collect_metrics(reader)
            attempts_pre_sup = sum(
                p.value for p in pts_pre_sup["gcp.storage.client.attempts"]
            )
            ops_pre_sup = sum(
                p.value for p in pts_pre_sup["gcp.storage.client.operations"]
            )

            sup_blob = bucket.blob("sup-sharded")
            sup_blob._properties.update({"size": 4, "generation": "1"})
            session.request.side_effect = [
                _json_response({"name": "f1.txt", "size": "5"}),
                _media_response(
                    b"hello",
                    status_code=200,
                    headers={
                        "x-goog-generation": "1",
                        "x-goog-hash": f"crc32c={_crc32c_b64(b'hello')}",
                    },
                    streaming=True,
                ),
                _media_response(
                    b"0123",
                    status_code=http.client.PARTIAL_CONTENT,
                    headers={"content-range": "bytes 0-3/4", "x-goog-generation": "1"},
                    streaming=True,
                ),
                _media_response(
                    f"<InitiateMultipartUploadResult {xml_ns}><UploadId>u-sup</UploadId></InitiateMultipartUploadResult>".encode(
                        "utf-8"
                    ),
                    status_code=200,
                ),
                _media_response(
                    b"",
                    status_code=200,
                    headers={
                        "ETag": '"e1"',
                        "x-goog-hash": f"crc32c={_crc32c_b64(b'0123456789')}",
                    },
                ),
                _media_response(
                    f'<CompleteMultipartUploadResult {xml_ns}><ETag>"done"</ETag></CompleteMultipartUploadResult>'.encode(
                        "utf-8"
                    ),
                    status_code=200,
                ),
            ]
            with _helpers._suppress_internal_metrics():
                transfer_manager.upload_many(
                    [(str(src_dir / "f1.txt"), bucket.blob("sup-u"))],
                    worker_type=transfer_manager.PROCESS,
                    max_workers=1,
                    raise_exception=True,
                )
                transfer_manager.download_many(
                    [(bucket.blob("sup-d"), str(tmp_path / "sup_d.txt"))],
                    worker_type=transfer_manager.PROCESS,
                    max_workers=1,
                    raise_exception=True,
                )
                transfer_manager.download_chunks_concurrently(
                    sup_blob,
                    str(tmp_path / "sup_chunk_d.bin"),
                    chunk_size=4,
                    worker_type=transfer_manager.PROCESS,
                    max_workers=1,
                    crc32c_checksum=False,
                )
                transfer_manager.upload_chunks_concurrently(
                    str(up_src),
                    bucket.blob("sup-chunk-u"),
                    chunk_size=10,
                    worker_type=transfer_manager.PROCESS,
                    max_workers=1,
                )

            pts_post_sup = _collect_metrics(reader)
            assert (
                sum(p.value for p in pts_post_sup["gcp.storage.client.attempts"])
                == attempts_pre_sup
            )
            assert (
                sum(p.value for p in pts_post_sup["gcp.storage.client.operations"])
                == ops_pre_sup
            )

    # 4. Isolated _LazyClient & _cleanup_cached_clients branches, plus real subprocess smoke test
    with monkeypatch.context() as mp:
        fake_atexit = mock.MagicMock()
        fake_finalize = mock.MagicMock()
        mp.setattr(transfer_manager, "_cached_clients", {})
        mp.setattr(transfer_manager, "_cleanup_registered_pid", None)
        mp.setattr(transfer_manager.atexit, "register", fake_atexit)
        mp.setattr(transfer_manager.multiprocessing.util, "Finalize", fake_finalize)

        base_pos = ("proj", _make_credentials(), mock.MagicMock(), None, None)
        c5 = transfer_manager._LazyClient("id-5", *base_pos, {}, True, False)
        assert transfer_manager._LazyClient("id-5", *base_pos) is c5
        transfer_manager._LazyClient("id-5only", *base_pos, enable_metrics=False)
        transfer_manager._LazyClient(
            "id-6", *base_pos, {"X-Test": "1"}, enable_metrics=False
        )
        transfer_manager._LazyClient("id-7", *base_pos, {}, False)
        transfer_manager._LazyClient("id-8", *base_pos, {}, False, False)
        fake_atexit.assert_called_once_with(transfer_manager._cleanup_cached_clients)
        fake_finalize.assert_called_once_with(
            None, transfer_manager._cleanup_cached_clients, exitpriority=10
        )

        flush_provider = mock.Mock(spec=["force_flush"])
        with mock.patch.object(
            _opentelemetry_metrics.metrics,
            "get_meter_provider",
            return_value=flush_provider,
        ):
            transfer_manager._cleanup_cached_clients()
            transfer_manager._cleanup_cached_clients()
        flush_provider.force_flush.assert_called_once()
        assert transfer_manager._cached_clients == {}

        bad_close_cl = mock.Mock(
            metrics_enabled=False,
            debug_metrics_enabled=False,
            close=mock.Mock(side_effect=RuntimeError("close boom")),
        )
        ok_close_cl = mock.Mock(metrics_enabled=False, debug_metrics_enabled=False)
        transfer_manager._cached_clients.update({"b1": bad_close_cl, "b2": ok_close_cl})
        with mock.patch.object(
            _opentelemetry_metrics.metrics,
            "get_meter_provider",
            side_effect=AssertionError("must not flush when metrics disabled"),
        ):
            transfer_manager._cleanup_cached_clients()
        bad_close_cl.close.assert_called_once()
        ok_close_cl.close.assert_called_once()

        err_flush_provider = mock.Mock(
            spec=["force_flush"],
            force_flush=mock.Mock(side_effect=RuntimeError("flush boom")),
        )
        transfer_manager._cached_clients["dbg"] = mock.Mock(
            metrics_enabled=False, debug_metrics_enabled=True
        )
        with mock.patch.object(
            _opentelemetry_metrics.metrics,
            "get_meter_provider",
            return_value=err_flush_provider,
        ):
            transfer_manager._cleanup_cached_clients()
        err_flush_provider.force_flush.assert_called_once()

        transfer_manager._cached_clients["act-no-flush"] = mock.Mock(
            metrics_enabled=True, debug_metrics_enabled=False
        )
        with mock.patch.object(
            _opentelemetry_metrics.metrics,
            "get_meter_provider",
            return_value=object(),
        ):
            transfer_manager._cleanup_cached_clients()

        transfer_manager._cached_clients["act-no-otel"] = mock.Mock(
            metrics_enabled=True, debug_metrics_enabled=False
        )
        mp.setattr(_opentelemetry_metrics, "metrics", None)
        transfer_manager._cleanup_cached_clients()

    real_proc_client = Client(
        project="test-project",
        credentials=_make_credentials(),
        client_options={"api_endpoint": "http://127.0.0.1:1"},
        enable_metrics=True,
    )
    real_proc_client._bucket_metadata_cache = None
    real_results = transfer_manager.upload_many(
        [(str(src_dir / "f1.txt"), real_proc_client.bucket("b").blob("o"))],
        upload_kwargs={"retry": None, "timeout": 0.2},
        worker_type=transfer_manager.PROCESS,
        max_workers=1,
        raise_exception=False,
    )
    assert len(real_results) == 1
    assert isinstance(real_results[0], Exception)
    real_proc_client.close()

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
        "storage.transfer_manager.upload_chunks_concurrently",
        "WriteObject",
        "PERMISSION_DENIED",
    ) in by_method_err
    assert (
        "storage.transfer_manager.download_chunks_concurrently",
        "ReadObject",
        "OK",
    ) in by_method_err
    assert (
        "storage.transfer_manager.upload_many_from_filenames",
        "WriteObject",
        "OK",
    ) in by_method_err
    assert (
        "storage.transfer_manager.download_many_to_path",
        "ReadObject",
        "OK",
    ) in by_method_err
