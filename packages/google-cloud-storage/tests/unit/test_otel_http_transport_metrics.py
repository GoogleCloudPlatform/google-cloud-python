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

"""Unit tests for OpenTelemetry HTTP JSON transport, Client lifecycle, and core helpers."""

import functools
import http.client
import json
from unittest import mock

import pytest
import requests
from google.api_core import retry
from google.auth import credentials as auth_credentials
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import InMemoryMetricReader
from opentelemetry.sdk.trace import TracerProvider

from google.cloud.storage import _helpers, _opentelemetry_metrics
from google.cloud.storage._bucket_metadata_cache import BucketMetadataCache
from google.cloud.storage.client import Client


def _make_credentials():
    return auth_credentials.AnonymousCredentials()


def _json_response(payload, status_code=http.client.OK):
    response = requests.Response()
    response.status_code = status_code
    response.headers.update({"Content-Type": "application/json"})
    response._content = json.dumps(payload).encode("utf-8")
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
    # Disable async daemon cache fetches from consuming session.request.side_effect
    client._bucket_metadata_cache = None
    yield client, session, reader
    client.close()


def test_client_metrics_disabled_by_default_and_fast_paths(monkeypatch):
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", False)
    session = mock.MagicMock()
    session.request.return_value = _json_response({"items": []})
    client = Client(
        project="test-project",
        credentials=_make_credentials(),
        _http=session,
        enable_metrics=True,
    )
    assert client._metrics_recorder.enabled is False
    with _helpers._list_metrics_context("storage.Client.list_buckets", "ListBuckets"):
        iterator = client._list_resource("/b", lambda it, item: item)
    assert isinstance(iterator.api_request, functools.partial)
    assert list(iterator) == []
    resp = client._connection._make_request("GET", "/b")
    assert resp.status_code == http.client.OK
    client.close()


def test_client_custom_endpoint_and_owned_shutdown():
    session = mock.MagicMock()
    session.request.return_value = _json_response({"email_address": "sa@example.com"})
    reader = InMemoryMetricReader()
    provider = MeterProvider(metric_readers=[reader])
    client = Client(
        project="test-project",
        credentials=_make_credentials(),
        _http=session,
        client_options={"api_endpoint": "https://custom.storage.example.com:8443"},
        enable_metrics=True,
        meter_provider=provider,
    )
    with _helpers._start_storage_operation(
        client,
        "storage.Client.get_service_account_email",
        "GetServiceAccount",
    ):
        resp = client._get_resource("/projects/test-project/serviceAccount")
        assert resp["email_address"] == "sa@example.com"

    pts = _collect_metrics(reader)
    op_pt = pts["gcp.storage.client.operations"][0]
    dur_pt = pts["gcp.client.request.duration"][0]
    assert op_pt.attributes["server.address"] == "custom.storage.example.com"
    assert dur_pt.attributes["server.address"] == "custom.storage.example.com"
    assert op_pt.attributes["rpc.system.name"] == "http"

    att_pt = pts["gcp.storage.client.attempts"][0]
    http_dur_pt = pts["http.client.request.duration"][0]
    assert att_pt.attributes["server.address"] == "custom.storage.example.com"
    assert http_dur_pt.attributes["server.address"] == "custom.storage.example.com"
    assert att_pt.attributes["network.path"] == "cloudpath"

    with client:
        pass

    with mock.patch.object(client._metrics_recorder, "shutdown") as mock_shutdown:
        client.close()
    mock_shutdown.assert_called_once()

    # Immutable _http and missing _metrics_recorder on close() are safe no-ops
    ro_client = Client(
        project="test-project",
        credentials=_make_credentials(),
        _http=object(),
        enable_metrics=True,
    )
    assert ro_client._http is ro_client._http_internal
    assert ro_client.metrics_enabled is True
    assert ro_client.debug_metrics_enabled is False
    ro_client._metrics_recorder.shutdown()
    ro_client._metrics_recorder = None
    assert ro_client.metrics_enabled is False
    assert ro_client.debug_metrics_enabled is False
    assert ro_client._http is ro_client._http_internal
    ro_client.close()

    # Lazy _http session creation attaches _gcs_metrics_recorder on first access
    lazy_client = Client(
        project="test-project",
        credentials=_make_credentials(),
        _http=None,
        enable_metrics=True,
        meter_provider=provider,
    )
    lazy_client._bucket_metadata_cache = None
    lazy_session = mock.MagicMock()
    with mock.patch(
        "google.cloud.client.ClientWithProject._http",
        new_callable=mock.PropertyMock,
        return_value=lazy_session,
    ):
        assert lazy_client._http is lazy_session
        assert lazy_session._gcs_metrics_recorder is lazy_client._metrics_recorder
    lazy_client.close()


def test_list_resource_metrics_context_and_unannotated_passthrough(metrics_env):
    client, session, reader = metrics_env

    # Unannotated _list_resource leaves raw functools.partial untouched
    raw_iter = client._list_resource("/b", lambda it, item: item)
    assert isinstance(raw_iter.api_request, functools.partial)

    # Annotated _list_resource wraps api_request and emits one operation per page
    with _helpers._list_metrics_context("storage.Client.list_buckets", "ListBuckets"):
        paged_iter = client._list_resource("/b", lambda it, item: item["name"])
    assert not isinstance(paged_iter.api_request, functools.partial)
    assert _collect_metrics(reader) == {}

    session.request.side_effect = [
        _json_response({"items": [{"name": "b1"}], "nextPageToken": "p2"}),
        _json_response({"items": [{"name": "b2"}]}),
    ]
    assert list(paged_iter) == ["b1", "b2"]
    pts = _collect_metrics(reader)
    ops = pts["gcp.storage.client.operations"]
    assert sum(p.value for p in ops) == 2
    assert ops[0].attributes["gcp.client.method"] == "storage.Client.list_buckets"
    assert ops[0].attributes["gcp.storage.operation"] == "ListBuckets"


def test_helpers_context_managers_batch_deferral_and_property_mixin(metrics_env):
    client, session, reader = metrics_env

    class _BrokenClientObj:
        _client = "fallback-client"

        @property
        def client(self):
            raise RuntimeError("unbound")

    broken = _BrokenClientObj()
    assert _helpers._resolve_operation_client(broken, client="explicit") == "explicit"
    assert _helpers._resolve_operation_client(broken) == "fallback-client"

    with _helpers._suppress_body_size():
        assert _helpers._SUPPRESS_BODY_SIZE.get() is True
    assert _helpers._SUPPRESS_BODY_SIZE.get() is False

    with _helpers._list_metrics_context("outer.method", "ListObjects"):
        with _helpers._list_metrics_context("inner.method", "ListBuckets"):
            assert _helpers._LIST_METRICS_CONTEXT.get() == (
                "outer.method",
                "ListObjects",
            )
    assert _helpers._LIST_METRICS_CONTEXT.get() is None

    with _helpers._client_method_override("outer.override"):
        with _helpers._client_method_override("inner.override"):
            assert _helpers._CLIENT_METHOD_OVERRIDE.get() == "outer.override"
    assert _helpers._CLIENT_METHOD_OVERRIDE.get() is None

    # Disabled client yields None in _start_storage_operation
    disabled_client = Client(
        project="test-project",
        credentials=_make_credentials(),
        _http=mock.MagicMock(),
        enable_metrics=False,
    )
    disabled_client._bucket_metadata_cache = None
    with _helpers._start_storage_operation(
        disabled_client, "storage.Client.get_bucket", "GetBucket"
    ) as st_disabled:
        assert st_disabled is None
    disabled_client.close()

    # Batch deferral in Connection.api_request and _start_storage_operation skips
    # queued/batchable ops while keeping non-batchable ops
    batch = client.batch()
    batch.__enter__()
    try:
        bkt = client.bucket("b1")
        bkt.storage_class = "NEARLINE"
        bkt.patch()
        assert _collect_metrics(reader) == {}

        with _helpers._start_storage_operation(
            client, "storage.Bucket.patch", "UpdateBucket"
        ) as st_deferred:
            assert st_deferred is None
        with _helpers._client_method_override("storage.Blob.download_as_bytes"):
            with _helpers._start_storage_operation(
                client, "storage.Blob.download_to_file", "ReadObject"
            ) as st_non_batch:
                assert st_non_batch is not None
    finally:
        client._pop_batch()

    # Custom _PropertyMixin without _METRICS_GET_OP / _METRICS_UPDATE_OP executes uninstrumented branch
    class _CustomResource(_helpers._PropertyMixin):
        path = "/custom/1"
        user_project = None

        def __init__(self, cl):
            super().__init__(name="c1")
            self._client = cl

        @property
        def client(self):
            return self._client

    mock_client = mock.MagicMock()
    mock_client._get_resource.return_value = {"k": "v"}
    mock_client._patch_resource.return_value = {"k": "v2"}
    mock_client._put_resource.return_value = {"k": "v3"}
    res = _CustomResource(mock_client)
    res.reload()
    res.patch()
    res.update()
    assert res._properties == {"k": "v3"}

    # Instrumented _PropertyMixin records reload, patch, and update with canonical class name
    class _InstrumentedResource(_helpers._PropertyMixin):
        _METRICS_CLASS_NAME = "Bucket"
        _METRICS_GET_OP = "GetBucket"
        _METRICS_UPDATE_OP = "UpdateBucket"
        path = "/b/my-bucket"
        user_project = None

        def __init__(self, cl):
            super().__init__(name="my-bucket")
            self._client = cl

        @property
        def client(self):
            return self._client

    session.request.side_effect = [
        _json_response({"name": "my-bucket"}),
        _json_response({"name": "my-bucket"}),
        _json_response({"name": "my-bucket"}),
    ]
    inst_res = _InstrumentedResource(client)
    inst_res.reload()
    inst_res.patch()
    inst_res.update()

    pts = _collect_metrics(reader)
    methods_seen = {
        p.attributes["gcp.client.method"] for p in pts["gcp.storage.client.operations"]
    }
    assert methods_seen == {
        "storage.Blob.download_as_bytes",
        "storage.Bucket.reload",
        "storage.Bucket.patch",
        "storage.Bucket.update",
    }


def test_http_connection_direct_make_request_and_edge_branches(metrics_env):
    client, session, reader = metrics_env
    conn = client._connection

    # 1. Suppressed internal metrics bypasses recording
    session.request.return_value = _json_response({"ok": True})
    with _helpers._suppress_internal_metrics():
        with _helpers._start_storage_operation(
            client, "storage.Client.get_bucket", "GetBucket"
        ) as st:
            assert st is None
        conn._make_request("GET", "https://storage.googleapis.com/storage/v1/b/b1")
        conn.api_request(method="GET", path="/b/b1")
    assert _collect_metrics(reader) == {}

    # 2. Direct _make_request network exception -> CONNECTION_ERROR, no TTFB, no status_code
    session.request.side_effect = requests.ConnectionError("reset by peer")
    with _helpers._start_storage_operation(client, "storage.Batch.finish", "Batch"):
        with pytest.raises(requests.ConnectionError):
            conn._make_request(
                "POST", "https://storage.googleapis.com/batch/storage/v1"
            )
    pts = _collect_metrics(reader)
    assert "gcp.storage.client.ttfb" not in pts
    att = pts["gcp.storage.client.attempts"][-1]
    assert att.attributes["error.type"] == "CONNECTION_ERROR"
    assert "http.response.status_code" not in att.attributes

    # 3. Direct _make_request non-2xx with normal response AND broken response object
    session.request.side_effect = None
    session.request.return_value = _json_response(
        {"error": {"message": "unavailable"}}, status_code=503
    )
    resp_503 = conn._make_request(
        "POST", "https://storage.googleapis.com/batch/storage/v1"
    )
    assert resp_503.status_code == 503

    broken_resp = mock.Mock()
    broken_resp.status_code = 500
    session.request.return_value = broken_resp
    conn._make_request("POST", "https://storage.googleapis.com/batch/storage/v1")

    bool_sc_resp = mock.Mock()
    bool_sc_resp.status_code = True
    session.request.return_value = bool_sc_resp
    conn._make_request("POST", "https://storage.googleapis.com/batch/storage/v1")

    pts2 = _collect_metrics(reader)
    statuses = [
        p.attributes.get("http.response.status_code")
        for p in pts2["http.client.request.duration"]
    ]
    assert 503 in statuses
    assert 500 in statuses
    assert statuses[-1] is None
    assert sum(p.count for p in pts2["gcp.storage.client.ttfb"]) == 2

    # 4. api_request fallback branches when base_call bypasses _make_request or url is empty
    with mock.patch("google.cloud._http.JSONConnection.api_request", return_value={}):
        conn.api_request("GET", "/b/my-bucket")
    weird_resp = _json_response({"ok": True})
    weird_resp.status_code = True  # bool is excluded from int status_code
    with mock.patch.object(
        _helpers._opentelemetry_metrics,
        "normalize_url_template",
        wraps=_opentelemetry_metrics.normalize_url_template,
    ):
        session.request.return_value = _json_response({"ok": True})
        with mock.patch(
            "google.cloud._http.JSONConnection._make_request",
            return_value=weird_resp,
        ):
            with mock.patch(
                "google.cloud._http.JSONConnection.api_request",
                side_effect=lambda *a, **kw: (conn._make_request("GET", "") and {}),
            ):
                conn.api_request(method="GET", path="/b/my-bucket")

        with mock.patch(
            "google.cloud._http.JSONConnection._make_request",
            return_value=weird_resp,
        ):
            with mock.patch(
                "google.cloud._http.JSONConnection.api_request",
                side_effect=lambda *a, **kw: (
                    conn._make_request("GET", "")
                    and (_ for _ in ()).throw(RuntimeError("boom"))
                ),
            ):
                with pytest.raises(RuntimeError):
                    conn.api_request(method="GET", path="/b/my-bucket")


def test_retries_errors_and_ttfb_on_api_request(metrics_env):
    client, session, reader = metrics_env
    session.request.side_effect = [
        _json_response({"error": {"message": "503-1"}}, status_code=503),
        requests.ConnectionError("transient reset"),
        _json_response({"id": "my-bucket", "name": "my-bucket"}, status_code=200),
    ]
    fast_retry = retry.Retry(initial=0.001, maximum=0.002, deadline=5.0)
    with _helpers._start_storage_operation(
        client, "storage.Client.get_bucket", "GetBucket"
    ):
        resp = client._connection.api_request(
            method="GET", path="/b/my-bucket", retry=fast_retry
        )
    assert resp["name"] == "my-bucket"

    pts = _collect_metrics(reader)
    assert len(pts["gcp.storage.client.operations"]) == 1
    op = pts["gcp.storage.client.operations"][0]
    dur = pts["gcp.client.request.duration"][0]
    assert op.attributes["gcp.storage.operation"] == "GetBucket"
    assert op.attributes["gcp.client.method"] == "storage.Client.get_bucket"
    assert op.attributes["error.type"] == "OK"
    assert dur.attributes["rpc.method"] == "google.storage.v2.Storage/GetBucket"
    assert dur.attributes["error.type"] == "OK"

    attempts = pts["gcp.storage.client.attempts"]
    assert sum(p.value for p in attempts) == 3
    err_types = {p.attributes.get("error.type", "OK") for p in attempts}
    assert err_types == {"UNAVAILABLE", "CONNECTION_ERROR", "OK"}

    retries_pts = pts["gcp.storage.client.retries"]
    assert sum(p.value for p in retries_pts) == 2
    retry_errs = {p.attributes["error.type"] for p in retries_pts}
    assert retry_errs == {"UNAVAILABLE", "CONNECTION_ERROR"}

    errors_pts = pts["gcp.storage.client.errors"]
    assert sum(p.value for p in errors_pts) == 2

    # TTFB recorded only for the 503 response and the 200 response (NOT ConnectionError)
    ttfb_pts = pts["gcp.storage.client.ttfb"]
    assert sum(p.count for p in ttfb_pts) == 2

    # Terminal HTTP 400 BadRequest maps to INVALID_ARGUMENT
    session.request.side_effect = [
        _json_response(
            {"error": {"message": "Invalid bucket configuration"}},
            status_code=400,
        )
    ]
    with pytest.raises(Exception):
        with _helpers._start_storage_operation(
            client, "storage.Bucket.patch", "UpdateBucket"
        ):
            client._connection.api_request(
                method="PATCH", path="/b/my-bucket", retry=None
            )
    pts_after = _collect_metrics(reader)
    patch_ops = [
        p
        for p in pts_after["gcp.storage.client.operations"]
        if p.attributes["gcp.client.method"] == "storage.Bucket.patch"
    ]
    assert len(patch_ops) == 1
    assert patch_ops[0].attributes["error.type"] == "INVALID_ARGUMENT"


def test_bucket_metadata_cache_background_suppression(metrics_env):
    client, session, reader = metrics_env
    cache = BucketMetadataCache(client)

    session.request.side_effect = [
        _json_response({"id": "b1", "name": "b1", "location": "US"}),
        _json_response({"error": {"message": "404"}}, status_code=404),
    ]
    cache._fetch_background("b1")
    cache._verify_existence_background("b1")

    assert _collect_metrics(reader) == {}


def test_trace_exemplar_correlation_on_http_json_metrics(metrics_env):
    client, session, reader = metrics_env
    session.request.return_value = _json_response({"name": "my-bucket"})

    tracer_provider = TracerProvider()
    tracer = tracer_provider.get_tracer("test-tracer")
    with tracer.start_as_current_span("parent-span") as span:
        expected_trace_id = span.get_span_context().trace_id
        expected_span_id = span.get_span_context().span_id
        with _helpers._start_storage_operation(
            client, "storage.Client.get_bucket", "GetBucket"
        ):
            client._connection.api_request(method="GET", path="/b/my-bucket")

    pts = _collect_metrics(reader)
    op_exemplars = pts["gcp.client.request.duration"][0].exemplars
    http_exemplars = pts["http.client.request.duration"][0].exemplars
    assert len(op_exemplars) >= 1
    assert len(http_exemplars) >= 1
    assert op_exemplars[0].trace_id == expected_trace_id
    assert op_exemplars[0].span_id != 0
    assert http_exemplars[0].trace_id == expected_trace_id
    assert http_exemplars[0].span_id != 0
    assert expected_span_id != 0
