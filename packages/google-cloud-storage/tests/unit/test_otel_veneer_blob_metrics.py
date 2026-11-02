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

"""Unit tests for OpenTelemetry Blob control-plane and Veneer metrics."""

import http.client
import io
import json
from unittest import mock

import pytest
import requests
from google.api_core import iam
from google.auth import credentials as auth_credentials
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import InMemoryMetricReader

from google.cloud.storage import _opentelemetry_metrics
from google.cloud.storage.blob import Blob
from google.cloud.storage.client import Client


def _make_credentials():
    return auth_credentials.AnonymousCredentials()


def _json_response(payload=None, status_code=http.client.OK, headers=None):
    response = requests.Response()
    response.status_code = status_code
    response.headers.update({"Content-Type": "application/json"})
    if headers:
        response.headers.update(headers)
    if payload is not None:
        response._content = (
            payload
            if isinstance(payload, bytes)
            else json.dumps(payload).encode("utf-8")
        )
    else:
        response._content = b""
    response.request = requests.Request(
        "GET", "https://storage.googleapis.com/storage/v1/b"
    ).prepare()
    return response


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


def test_blob_exists_404_and_subclass_reload(metrics_env):
    client, session, reader = metrics_env
    bucket = client.bucket("my-bucket")
    blob = bucket.blob("missing-obj")

    session.request.side_effect = [
        _json_response({"error": {"message": "not found"}}, status_code=404),
        _json_response({"name": "sub-o"}),
    ]
    assert blob.exists() is False

    class _UserBlob(Blob):
        pass

    uo = _UserBlob("sub-o", bucket)
    uo.reload()

    pts = _collect_metrics(reader)
    ops = pts["gcp.storage.client.operations"]
    assert sum(p.value for p in ops) == 2
    assert {p.attributes["gcp.client.method"] for p in ops} == {
        "storage.Blob.exists",
        "storage.Blob.reload",
    }
    assert all(p.attributes["error.type"] == "OK" for p in ops)

    att_404 = [
        p
        for p in pts["gcp.storage.client.attempts"]
        if p.attributes["error.type"] == "NOT_FOUND"
    ]
    assert len(att_404) == 1
    assert att_404[0].attributes["gcp.storage.operation"] == "GetObject"


def test_all_blob_veneer_control_plane_and_entrypoint_methods(metrics_env):
    client, session, reader = metrics_env
    bucket = client.bucket("my-bucket")
    blob = bucket.blob("my-obj")

    iam_payload = {
        "version": 1,
        "etag": "CAE=",
        "bindings": [{"role": "roles/storage.objectViewer", "members": ["allUsers"]}],
    }
    session.request.side_effect = [
        _json_response({"name": "my-obj"}),  # blob.update
        _json_response({"name": "my-obj"}),  # blob.patch
        _json_response(iam_payload),  # blob.get_iam_policy
        _json_response(iam_payload),  # blob.set_iam_policy
        _json_response({"permissions": ["storage.objects.get"]}),  # blob.test_iam
        _json_response({"items": []}),  # blob.make_public reload acl
        _json_response({"acl": []}),  # blob.make_public save acl
        _json_response({"acl": []}),  # blob.make_private save acl (loaded)
        _json_response({"name": "my-obj"}),  # blob.compose
        _json_response(
            {
                "done": False,
                "rewriteToken": "tok1",
                "totalBytesRewritten": "10",
                "objectSize": "20",
            }
        ),  # blob.rewrite step 1
        _json_response(
            {
                "done": False,
                "rewriteToken": "tok2",
                "totalBytesRewritten": "10",
                "objectSize": "20",
            }
        ),  # blob.update_storage_class step 1
        _json_response(
            {
                "done": True,
                "totalBytesRewritten": "20",
                "objectSize": "20",
                "resource": {"name": "my-obj", "storageClass": "NEARLINE"},
            }
        ),  # blob.update_storage_class step 2
        _json_response(None, status_code=204),  # blob.delete
    ]
    blob.update()
    blob.patch()
    b_pol = iam.Policy()
    assert blob.get_iam_policy().version == 1
    blob.set_iam_policy(b_pol)
    assert blob.test_iam_permissions(["storage.objects.get"]) == ["storage.objects.get"]
    blob.make_public()
    blob.make_private()
    src1 = bucket.blob("s1")
    src2 = bucket.blob("s2")
    blob.compose([src1, src2])
    token, _, _ = blob.rewrite(src1)
    assert token == "tok1"
    blob._encryption_key = b"0" * 32
    blob.update_storage_class("NEARLINE")
    blob._encryption_key = None
    blob.delete()

    with mock.patch.object(Blob, "_prep_and_do_download", return_value=None):
        blob.download_to_file(io.BytesIO())
        with mock.patch("builtins.open", mock.mock_open()):
            blob.download_to_filename("/tmp/fake-download-unused")
    with mock.patch.object(
        Blob,
        "_prep_and_do_download",
        side_effect=lambda buf, **kw: buf.write(b"hello"),
    ):
        assert blob.download_as_bytes() == b"hello"
        with pytest.warns(PendingDeprecationWarning):
            assert blob.download_as_string() == b"hello"
        assert blob.download_as_text() == "hello"

    with mock.patch.object(Blob, "_do_upload", return_value={"name": "my-obj"}):
        blob.upload_from_file(io.BytesIO(b"abc"))
        blob.upload_from_string("abc")
        with mock.patch("builtins.open", mock.mock_open(read_data=b"abc")):
            with mock.patch("os.path.getsize", return_value=3):
                blob.upload_from_filename("/tmp/fake-upload-unused")

    with mock.patch.object(
        Blob,
        "_initiate_resumable_upload",
        return_value=(mock.Mock(resumable_url="https://u"), None),
    ):
        assert blob.create_resumable_upload_session() == "https://u"

    pts = _collect_metrics(reader)
    methods_seen = {
        p.attributes["gcp.client.method"] for p in pts["gcp.storage.client.operations"]
    }
    expected_methods = {
        "storage.Blob.update",
        "storage.Blob.patch",
        "storage.Blob.delete",
        "storage.Blob.get_iam_policy",
        "storage.Blob.set_iam_policy",
        "storage.Blob.test_iam_permissions",
        "storage.Blob.make_public",
        "storage.Blob.make_private",
        "storage.Blob.compose",
        "storage.Blob.rewrite",
        "storage.Blob.update_storage_class",
        "storage.Blob.download_to_file",
        "storage.Blob.download_to_filename",
        "storage.Blob.download_as_bytes",
        "storage.Blob.download_as_string",
        "storage.Blob.download_as_text",
        "storage.Blob.upload_from_file",
        "storage.Blob.upload_from_filename",
        "storage.Blob.upload_from_string",
        "storage.Blob.create_resumable_upload_session",
    }
    assert expected_methods == methods_seen


def test_blob_batch_deferral_non_batchable_ops_and_client_override(metrics_env):
    client, session, reader = metrics_env
    bucket = client.bucket("my-bucket")

    # 1. Batchable Blob ops defer to Batch.finish; non-batchable Blob ops record immediately
    multipart_ok_and_403 = (
        b"--b\r\n"
        b"Content-Type: application/http\r\n"
        b"Content-ID: <response-1>\r\n\r\n"
        b"HTTP/1.1 200 OK\r\n"
        b"Content-Type: application/json\r\n\r\n"
        b'{"name": "o1"}\r\n'
        b"--b\r\n"
        b"Content-Type: application/http\r\n"
        b"Content-ID: <response-2>\r\n\r\n"
        b"HTTP/1.1 403 Forbidden\r\n"
        b"Content-Type: application/json\r\n\r\n"
        b'{"error": {"message": "denied"}}\r\n'
        b"--b--\r\n"
    )
    session.request.return_value = _json_response(
        multipart_ok_and_403,
        status_code=200,
        headers={"Content-Type": "multipart/mixed; boundary=b"},
    )
    blob = bucket.blob("media-in-batch")
    with (
        mock.patch.object(blob, "_do_download"),
        mock.patch.object(blob, "_do_upload", return_value={"name": "media-in-batch"}),
        mock.patch(
            "google.cloud.storage.blob.ResumableUpload.initiate",
            return_value=_json_response(
                {}, headers={"location": "https://upload.example/1"}
            ),
        ),
    ):
        with client.batch(raise_exception=False):
            bucket.blob("o1").patch()  # Batchable JSON -> deferred to Batch.finish
            bucket.blob("o2").delete()  # Batchable JSON -> deferred to Batch.finish
            blob.download_as_bytes()
            blob.upload_from_string(b"abc")
            blob.create_resumable_upload_session()

    pts_batch = _collect_metrics(reader)
    batch_methods = {
        p.attributes["gcp.client.method"]
        for p in pts_batch["gcp.storage.client.operations"]
    }
    assert batch_methods == {
        "storage.Batch.finish",
        "storage.Blob.download_as_bytes",
        "storage.Blob.upload_from_string",
        "storage.Blob.create_resumable_upload_session",
    }
    assert "storage.Blob.patch" not in batch_methods
    assert "storage.Blob.delete" not in batch_methods

    # 2. Blob.update_storage_class(..., client=other_client) routes both logical and HTTP metrics to other_client
    uninstrumented_session = mock.MagicMock()
    uninstrumented_client = Client(
        project="test-project",
        credentials=_make_credentials(),
        _http=uninstrumented_session,
        enable_metrics=False,
    )
    uninstrumented_client._bucket_metadata_cache = None
    other_reader = InMemoryMetricReader()
    other_provider = MeterProvider(metric_readers=[other_reader])
    other_session = mock.MagicMock()
    other_session.request.side_effect = [
        _json_response(
            {
                "done": False,
                "rewriteToken": "tok-1",
                "totalBytesRewritten": "5",
                "objectSize": "10",
            }
        ),
        _json_response(
            {
                "done": True,
                "totalBytesRewritten": "10",
                "objectSize": "10",
                "resource": {"name": "obj", "storageClass": "NEARLINE"},
            }
        ),
    ]
    other_client = Client(
        project="test-project",
        credentials=_make_credentials(),
        _http=other_session,
        enable_metrics=True,
        meter_provider=other_provider,
    )
    other_client._bucket_metadata_cache = None
    ublob = uninstrumented_client.bucket("my-bucket").blob("obj")
    ublob.update_storage_class("NEARLINE", client=other_client)

    assert uninstrumented_session.request.call_count == 0
    assert other_session.request.call_count == 2
    other_pts = _collect_metrics(other_reader)
    assert len(other_pts["gcp.storage.client.operations"]) == 1
    assert (
        other_pts["gcp.storage.client.operations"][0].attributes["gcp.client.method"]
        == "storage.Blob.update_storage_class"
    )
    assert sum(p.value for p in other_pts["gcp.storage.client.attempts"]) == 2
    uninstrumented_client.close()
    other_client.close()
