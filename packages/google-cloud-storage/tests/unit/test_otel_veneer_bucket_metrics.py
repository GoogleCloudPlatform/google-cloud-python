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

"""Unit tests for OpenTelemetry Client, Bucket, Batch, ACL, HMAC & Notification Veneer metrics."""

import http.client
import io
import json
from unittest import mock

import pytest
import requests
from google.api_core import retry
from google.auth import credentials as auth_credentials
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import InMemoryMetricReader

from google.cloud.storage import _opentelemetry_metrics
from google.cloud.storage.acl import (
    ACL,
    BucketACL,
    DefaultObjectACL,
    ObjectACL,
    _ACLEntity,
)
from google.cloud.storage.blob import Blob
from google.cloud.storage.bucket import Bucket
from google.cloud.storage.client import Client
from google.cloud.storage.hmac_key import HMACKeyMetadata
from google.cloud.storage.notification import BucketNotification


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


def test_client_get_bucket_retries_and_bucket_patch_error(metrics_env):
    client, session, reader = metrics_env
    session.request.side_effect = [
        _json_response({"error": {"message": "503-1"}}, status_code=503),
        requests.ConnectionError("transient reset"),
        _json_response({"id": "my-bucket", "name": "my-bucket"}, status_code=200),
    ]
    fast_retry = retry.Retry(initial=0.001, maximum=0.002, deadline=5.0)
    bucket = client.get_bucket("my-bucket", retry=fast_retry)
    assert bucket.name == "my-bucket"

    pts = _collect_metrics(reader)
    assert len(pts["gcp.storage.client.operations"]) == 1
    op = pts["gcp.storage.client.operations"][0]
    dur = pts["gcp.client.request.duration"][0]
    assert op.attributes["gcp.storage.operation"] == "GetBucket"
    assert op.attributes["gcp.client.method"] == "storage.Client.get_bucket"
    assert op.attributes["error.type"] == "OK"
    assert dur.attributes["rpc.method"] == "google.storage.v2.Storage/GetBucket"
    assert dur.attributes["error.type"] == "OK"
    assert sum(p.value for p in pts["gcp.storage.client.attempts"]) == 3
    assert sum(p.value for p in pts["gcp.storage.client.retries"]) == 2
    assert sum(p.value for p in pts["gcp.storage.client.errors"]) == 2

    # Terminal HTTP 400 BadRequest on Bucket.patch maps to INVALID_ARGUMENT
    session.request.side_effect = [
        _json_response(
            {"error": {"message": "Invalid bucket configuration"}},
            status_code=400,
        )
    ]
    b = client.bucket("my-bucket")
    with pytest.raises(Exception):
        b.patch(retry=None)
    pts_after = _collect_metrics(reader)
    patch_ops = [
        p
        for p in pts_after["gcp.storage.client.operations"]
        if p.attributes["gcp.client.method"] == "storage.Bucket.patch"
    ]
    assert len(patch_ops) == 1
    assert patch_ops[0].attributes["error.type"] == "INVALID_ARGUMENT"


def test_existence_and_lookup_404_semantics(metrics_env):
    client, session, reader = metrics_env
    session.request.side_effect = [
        _json_response({"error": {"message": "not found"}}, status_code=404),
        _json_response({"error": {"message": "not found"}}, status_code=404),
        _json_response({"error": {"message": "not found"}}, status_code=404),
        _json_response({"error": {"message": "not found"}}, status_code=404),
        _json_response({"error": {"message": "not found"}}, status_code=404),
    ]

    assert client.lookup_bucket("missing-b") is None
    bucket = client.bucket("missing-b")
    assert bucket.exists() is False
    assert bucket.get_blob("missing-obj") is None
    hmac_meta = HMACKeyMetadata(client, access_id="GOOG123")
    assert hmac_meta.exists() is False
    notif = BucketNotification(bucket, notification_id="n1")
    assert notif.exists() is False

    pts = _collect_metrics(reader)
    ops = pts["gcp.storage.client.operations"]
    assert sum(p.value for p in ops) == 5
    for op in ops:
        assert op.attributes["error.type"] == "OK"
    for dur in pts["gcp.client.request.duration"]:
        assert dur.attributes["error.type"] == "OK"

    attempts = pts["gcp.storage.client.attempts"]
    assert sum(p.value for p in attempts) == 5
    for att in attempts:
        assert att.attributes["error.type"] == "NOT_FOUND"
    for http_dur in pts["http.client.request.duration"]:
        assert http_dur.attributes["http.response.status_code"] == 404


def test_lazy_pagination_iterators_and_precedence(metrics_env):
    client, session, reader = metrics_env

    # Constructing iterators emits 0 metrics
    b_iter = client.bucket("my-bucket").list_blobs()
    c_iter = client.list_blobs("my-bucket")
    buckets_iter = client.list_buckets()
    hmac_iter = client.list_hmac_keys()
    notif_iter = client.bucket("my-bucket").list_notifications()
    assert _collect_metrics(reader) == {}

    # Iterating 2 pages on Bucket.list_blobs emits 2 ListObjects operations
    # attributed to storage.Bucket.list_blobs (outermost wins over Client.list_blobs)
    session.request.side_effect = [
        _json_response({"items": [{"name": "o1"}], "nextPageToken": "tok2"}),
        _json_response({"items": [{"name": "o2"}]}),
        _json_response({"items": [{"name": "o3"}]}),
        _json_response({"items": [{"name": "b1"}]}),
        _json_response({"items": [{"accessId": "k1"}]}),
        _json_response(
            {
                "items": [
                    {
                        "id": "n1",
                        "topic": "//pubsub.googleapis.com/projects/my-proj/topics/my-topic",
                    }
                ]
            }
        ),
    ]
    assert [b.name for b in b_iter] == ["o1", "o2"]
    assert [b.name for b in c_iter] == ["o3"]
    assert [b.name for b in buckets_iter] == ["b1"]
    assert [k.access_id for k in hmac_iter] == ["k1"]
    assert [n.notification_id for n in notif_iter] == ["n1"]

    pts = _collect_metrics(reader)
    by_method = {}
    for p in pts["gcp.storage.client.operations"]:
        key = (
            p.attributes["gcp.client.method"],
            p.attributes["gcp.storage.operation"],
        )
        by_method[key] = by_method.get(key, 0) + p.value

    assert by_method == {
        ("storage.Bucket.list_blobs", "ListObjects"): 2,
        ("storage.Client.list_blobs", "ListObjects"): 1,
        ("storage.Client.list_buckets", "ListBuckets"): 1,
        ("storage.Client.list_hmac_keys", "ListHMACKeys"): 1,
        ("storage.Bucket.list_notifications", "ListNotifications"): 1,
    }


def test_all_client_bucket_acl_hmac_and_notification_methods(metrics_env):
    client, session, reader = metrics_env

    # Client methods
    session.request.side_effect = [
        _json_response({"email_address": "sa@example.com"}),  # get_service_account
        _json_response({"name": "created-b"}),  # create_bucket
        _json_response({"name": "restored-b"}),  # restore_bucket
        _json_response(
            {"secret": "sec", "metadata": {"accessId": "GOOG1"}}
        ),  # create_hmac_key
        _json_response({"accessId": "GOOG1", "state": "ACTIVE"}),  # get_hmac_key_meta
    ]
    assert client.get_service_account_email() == "sa@example.com"
    assert client.create_bucket("created-b").name == "created-b"
    assert client.restore_bucket("restored-b", generation=123).name == "restored-b"
    meta, secret = client.create_hmac_key("sa@test.iam.gserviceaccount.com")
    assert secret == "sec"
    assert meta.access_id == "GOOG1"
    assert client.get_hmac_key_metadata("GOOG1").state == "ACTIVE"

    # Client.download_blob_to_file (mocking _prep_and_do_download to test Veneer wrapper)
    bucket = client.bucket("my-bucket")
    blob = bucket.blob("my-obj")
    with mock.patch.object(Blob, "_prep_and_do_download"):
        client.download_blob_to_file(blob, io.BytesIO())

    # Bucket methods
    iam_payload = {
        "version": 1,
        "etag": "CAE=",
        "bindings": [{"role": "roles/storage.objectViewer", "members": ["allUsers"]}],
    }
    session.request.side_effect = [
        _json_response({"name": "my-bucket"}),  # bucket.create
        _json_response({"name": "my-bucket"}),  # bucket.reload
        _json_response({"name": "my-bucket"}),  # bucket.update
        _json_response({"name": "my-bucket"}),  # bucket.patch
        _json_response(
            {
                "id": "n1",
                "topic": "//pubsub.googleapis.com/projects/my-proj/topics/my-topic",
            }
        ),  # bucket.get_notification
        _json_response(None, status_code=204),  # bucket.delete_blob
        _json_response({"resource": {"name": "copied"}}),  # bucket.copy_blob
        _json_response({"name": "moved"}),  # bucket.move_blob
        _json_response({"name": "restored"}),  # bucket.restore_blob
        _json_response(iam_payload),  # bucket.get_iam_policy
        _json_response(iam_payload),  # bucket.set_iam_policy
        _json_response({"permissions": ["storage.objects.get"]}),  # test_iam
        _json_response({"name": "my-bucket", "metageneration": "2"}),  # lock_retention
        _json_response(None, status_code=204),  # bucket.delete
    ]
    bucket.create()
    bucket.reload()
    bucket.update()
    bucket.patch()
    assert bucket.get_notification("n1").notification_id == "n1"
    bucket.delete_blob("old-obj")
    bucket.copy_blob(blob, bucket, new_name="copied")
    bucket.move_blob(blob, new_name="moved")
    bucket.restore_blob("restored", generation=1)
    pol = bucket.get_iam_policy()
    bucket.set_iam_policy(pol)
    assert bucket.test_iam_permissions(["storage.objects.get"]) == [
        "storage.objects.get"
    ]
    bucket._properties["metageneration"] = 1
    bucket._properties["retentionPolicy"] = {"retentionPeriod": 100}
    bucket.lock_retention_policy()
    bucket.delete()

    # Subclass of Bucket preserves canonical class name in gcp.client.method
    class _UserBucket(Bucket):
        pass

    session.request.side_effect = [_json_response({"name": "sub-b"})]
    ub = _UserBucket(client, "sub-b")
    ub.reload()

    # Multi-RPC Bucket methods: delete(force=True), delete_blobs(on_error=...),
    # rename_blob, make_public(recursive=True, future=True), make_private(recursive=True, future=True)
    session.request.side_effect = [
        _json_response({"items": [{"name": "o1"}]}),  # delete(force=True) list_blobs
        _json_response(None, status_code=204),  # delete(force=True) delete o1
        _json_response(None, status_code=204),  # delete(force=True) delete bucket
        _json_response(
            {"error": {"message": "404"}}, status_code=404
        ),  # delete_blobs 1
        _json_response(None, status_code=204),  # delete_blobs 2
        _json_response({"resource": {"name": "renamed"}}),  # rename_blob copy
        _json_response(None, status_code=204),  # rename_blob delete
        _json_response({"items": []}),  # make_public reload bucket acl
        _json_response({"acl": []}),  # make_public patch bucket acl
        _json_response({"items": []}),  # make_public reload default acl
        _json_response({"defaultObjectAcl": []}),  # make_public patch default acl
        _json_response({"items": [{"name": "o1", "acl": []}]}),  # make_public list
        _json_response({"acl": []}),  # make_public blob o1 patch
        _json_response({"acl": []}),  # make_private patch bucket acl (already loaded)
        _json_response({"defaultObjectAcl": []}),  # make_private patch default acl
        _json_response({"items": [{"name": "o1", "acl": []}]}),  # make_private list
        _json_response({"acl": []}),  # make_private blob o1 patch
    ]
    bucket.delete(force=True)
    errors = []
    bucket.delete_blobs(["missing", "present"], on_error=errors.append)
    assert len(errors) == 1
    bucket.rename_blob(blob, new_name="renamed")
    bucket.make_public(recursive=True, future=True)
    bucket.make_private(recursive=True, future=True)

    # ACL, DefaultObjectACL, ObjectACL
    for acl_obj in (BucketACL(bucket), DefaultObjectACL(bucket), ObjectACL(blob)):
        # save() when loaded=False is a local no-op -> 0 metrics
        acl_obj.loaded = False
        acl_obj.save()
        session.request.side_effect = [
            _json_response({"items": [{"entity": "allUsers", "role": "READER"}]}),
            _json_response({}),
            _json_response({}),
            _json_response({}),
        ]
        acl_obj.reload()
        acl_obj.save()
        acl_obj.save_predefined("publicRead")
        acl_obj.clear()
        assert isinstance(acl_obj, ACL)

    # HMACKeyMetadata
    hmac_meta = HMACKeyMetadata(client, access_id="GOOG999")
    hmac_meta.state = "INACTIVE"
    session.request.side_effect = [
        _json_response({"accessId": "GOOG999", "state": "ACTIVE"}),
        _json_response({"accessId": "GOOG999", "state": "ACTIVE"}),
        _json_response({"accessId": "GOOG999", "state": "INACTIVE"}),
        _json_response(None, status_code=204),
    ]
    assert hmac_meta.exists() is True
    hmac_meta.reload()
    hmac_meta.state = "INACTIVE"
    hmac_meta.update()
    hmac_meta.delete()

    # BucketNotification (including client validation error when notification_id is None)
    notif_missing_id = BucketNotification(bucket)
    for fn in (
        notif_missing_id.exists,
        notif_missing_id.reload,
        notif_missing_id.delete,
    ):
        with pytest.raises(ValueError):
            fn()

    notif = BucketNotification(bucket, topic_name="my-topic", topic_project="my-proj")
    session.request.side_effect = [
        _json_response(
            {
                "id": "notif-1",
                "topic": "//pubsub.googleapis.com/projects/my-proj/topics/my-topic",
            }
        ),
        _json_response({"id": "notif-1"}),
        _json_response(
            {
                "id": "notif-1",
                "topic": "//pubsub.googleapis.com/projects/my-proj/topics/my-topic",
            }
        ),
        _json_response(None, status_code=204),
    ]
    notif.create()
    assert notif.exists() is True
    notif.reload()
    notif.delete()

    pts = _collect_metrics(reader)
    methods_seen = {
        p.attributes["gcp.client.method"] for p in pts["gcp.storage.client.operations"]
    }
    expected_subset = {
        "storage.Client.get_service_account_email",
        "storage.Client.create_bucket",
        "storage.Client.restore_bucket",
        "storage.Client.create_hmac_key",
        "storage.Client.get_hmac_key_metadata",
        "storage.Client.download_blob_to_file",
        "storage.Bucket.create",
        "storage.Bucket.reload",
        "storage.Bucket.update",
        "storage.Bucket.patch",
        "storage.Bucket.get_notification",
        "storage.Bucket.delete_blob",
        "storage.Bucket.delete_blobs",
        "storage.Bucket.copy_blob",
        "storage.Bucket.rename_blob",
        "storage.Bucket.move_blob",
        "storage.Bucket.restore_blob",
        "storage.Bucket.get_iam_policy",
        "storage.Bucket.set_iam_policy",
        "storage.Bucket.test_iam_permissions",
        "storage.Bucket.make_public",
        "storage.Bucket.make_private",
        "storage.Bucket.lock_retention_policy",
        "storage.Bucket.delete",
        "storage.BucketACL.reload",
        "storage.BucketACL.save",
        "storage.BucketACL.save_predefined",
        "storage.BucketACL.clear",
        "storage.DefaultObjectACL.reload",
        "storage.DefaultObjectACL.save",
        "storage.DefaultObjectACL.save_predefined",
        "storage.DefaultObjectACL.clear",
        "storage.ObjectACL.reload",
        "storage.ObjectACL.save",
        "storage.ObjectACL.save_predefined",
        "storage.ObjectACL.clear",
        "storage.HMACKeyMetadata.exists",
        "storage.HMACKeyMetadata.reload",
        "storage.HMACKeyMetadata.update",
        "storage.HMACKeyMetadata.delete",
        "storage.BucketNotification.create",
        "storage.BucketNotification.exists",
        "storage.BucketNotification.reload",
        "storage.BucketNotification.delete",
    }
    assert expected_subset.issubset(methods_seen)
    assert not any("_UserBucket" in m for m in methods_seen)
    assert "gcp.storage.client.retries" not in pts


def test_batch_deferral_and_subresponse_semantics_on_bucket(metrics_env):
    client, session, reader = metrics_env
    bucket = client.bucket("my-bucket")

    # Empty batch finish -> CLIENT_VALIDATION_ERROR
    empty_batch = client.batch()
    with pytest.raises(ValueError):
        empty_batch.finish()
    pts_empty = _collect_metrics(reader)
    assert (
        pts_empty["gcp.storage.client.operations"][0].attributes["error.type"]
        == "CLIENT_VALIDATION_ERROR"
    )

    multipart_ok_and_403 = (
        b"--batch_boundary\r\n"
        b"Content-Type: application/http\r\n"
        b"Content-ID: <response-1>\r\n\r\n"
        b"HTTP/1.1 200 OK\r\n"
        b"Content-Type: application/json\r\n\r\n"
        b'{"name": "my-bucket"}\r\n'
        b"--batch_boundary\r\n"
        b"Content-Type: application/http\r\n"
        b"Content-ID: <response-2>\r\n\r\n"
        b"HTTP/1.1 403 Forbidden\r\n"
        b"Content-Type: application/json\r\n\r\n"
        b'{"error": {"message": "denied"}}\r\n'
        b"--batch_boundary--\r\n"
    )

    # 1. raise_exception=False: queuing emits 0 metrics; finish emits Batch OK
    session.request.return_value = _json_response(
        multipart_ok_and_403,
        status_code=200,
        headers={"Content-Type": "multipart/mixed; boundary=batch_boundary"},
    )
    with client.batch(raise_exception=False):
        bucket.patch()
        bucket.delete()
        pts_during = _collect_metrics(reader)
        assert len(pts_during["gcp.storage.client.operations"]) == 1

    pts_after_no_raise = _collect_metrics(reader)
    assert len(pts_after_no_raise["gcp.storage.client.operations"]) == 2

    # 2. raise_exception=True: subresponse 403 fails Batch with PERMISSION_DENIED
    session.request.return_value = _json_response(
        multipart_ok_and_403,
        status_code=200,
        headers={"Content-Type": "multipart/mixed; boundary=batch_boundary"},
    )
    with pytest.raises(Exception):
        with client.batch(raise_exception=True):
            bucket.patch()
            bucket.delete()

    pts_final = _collect_metrics(reader)
    batch_ops = pts_final["gcp.storage.client.operations"]
    err_map = [p.attributes.get("error.type", "OK") for p in batch_ops]
    assert "CLIENT_VALIDATION_ERROR" in err_map
    assert "OK" in err_map
    assert "PERMISSION_DENIED" in err_map

    http_att = pts_final["http.client.request.duration"][0]
    assert http_att.attributes["url.template"] == "/batch/storage/v1"
    assert http_att.attributes["http.request.method"] == "POST"


def test_lazy_acl_methods_attribution(metrics_env):
    client, session, reader = metrics_env
    bucket = client.bucket("my-bucket")

    acl_payload = {"items": [{"entity": "user-a@example.com", "role": "READER"}]}
    lazy_cases = [
        ("__iter__", lambda acl: list(acl)),
        (
            "entity_from_dict",
            lambda acl: acl.entity_from_dict(
                {"entity": "user-b@example.com", "role": "READER"}
            ),
        ),
        ("has_entity", lambda acl: acl.has_entity("user-a@example.com")),
        ("get_entity", lambda acl: acl.get_entity("user-a@example.com")),
        (
            "add_entity",
            lambda acl: acl.add_entity(_ACLEntity("user", "c@example.com")),
        ),
        ("entity", lambda acl: acl.entity("user", "a@example.com")),
        ("user", lambda acl: acl.user("a@example.com")),
        ("group", lambda acl: acl.group("g@example.com")),
        ("domain", lambda acl: acl.domain("example.com")),
        ("all", lambda acl: acl.all()),
        ("all_authenticated", lambda acl: acl.all_authenticated()),
        ("get_entities", lambda acl: acl.get_entities()),
    ]
    for _, fn in lazy_cases:
        session.request.return_value = _json_response(acl_payload)
        acl = BucketACL(bucket)
        fn(acl)
        fn(acl)  # loaded=True fast path -> 0 additional metrics

    pts_acl = _collect_metrics(reader)
    acl_ops = pts_acl["gcp.storage.client.operations"]
    assert len(acl_ops) == len(lazy_cases)
    assert {p.attributes["gcp.client.method"] for p in acl_ops} == {
        f"storage.BucketACL.{name}" for name, _ in lazy_cases
    }
    assert all(
        p.attributes["gcp.storage.operation"] == "ListBucketACLs" for p in acl_ops
    )
