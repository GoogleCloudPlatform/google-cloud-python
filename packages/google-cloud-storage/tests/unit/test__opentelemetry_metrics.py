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

import asyncio
import concurrent.futures
import http.client
import importlib
import socket
import ssl
import sys
import types
from unittest import mock

import pytest
import requests.exceptions
import urllib3.exceptions
from google.api_core import exceptions as api_exceptions
from google.auth import exceptions as auth_exceptions

from google.cloud.storage import _opentelemetry_metrics
from google.cloud.storage import exceptions as storage_exceptions
from google.cloud.storage.version import __version__


@pytest.fixture(autouse=True)
def setup(monkeypatch):
    """Default HAS_OPENTELEMETRY_METRICS to True for gating logic tests."""
    monkeypatch.setattr(_opentelemetry_metrics, "HAS_OPENTELEMETRY_METRICS", True)


def test_opentelemetry_import_error_on_load(monkeypatch):
    """Verify module import gracefully handles missing opentelemetry package."""
    try:
        with monkeypatch.context() as m:
            m.setitem(sys.modules, "opentelemetry", None)
            importlib.reload(_opentelemetry_metrics)
            m.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)
            assert _opentelemetry_metrics.HAS_OPENTELEMETRY_METRICS is False
            assert (
                _opentelemetry_metrics.is_metrics_enabled(enable_metrics=True) is False
            )
            assert (
                _opentelemetry_metrics.is_debug_metrics_enabled(
                    enable_debug_metrics=True
                )
                is False
            )
            assert _opentelemetry_metrics.get_meter(enable_metrics=True) is None
            m.setattr(_opentelemetry_metrics, "HAS_OPENTELEMETRY_METRICS", True)
            assert _opentelemetry_metrics.get_meter(enable_metrics=True) is None
    finally:
        importlib.reload(_opentelemetry_metrics)


@pytest.mark.parametrize(
    "env_val,default,expected",
    [
        ("1", False, True),
        ("true", False, True),
        ("True", False, True),
        ("yes", False, True),
        ("on", False, True),
        ("0", True, False),
        ("false", True, False),
        ("no", True, False),
        ("off", True, False),
        ("", True, True),
        ("", False, False),
        ("   ", True, True),
        ("   ", False, False),
    ],
)
def test_parse_bool_env(monkeypatch, env_val, default, expected):
    monkeypatch.setenv("TEST_BOOL_ENV", env_val)
    assert _opentelemetry_metrics._parse_bool_env("TEST_BOOL_ENV", default) == expected


def test_parse_bool_env_unrecognized_logs_warning(monkeypatch, caplog):
    monkeypatch.setenv("TEST_BOOL_ENV", "enabled")
    with caplog.at_level("WARNING", logger=_opentelemetry_metrics.__name__):
        assert _opentelemetry_metrics._parse_bool_env("TEST_BOOL_ENV", False) is False
        assert _opentelemetry_metrics._parse_bool_env("TEST_BOOL_ENV", True) is True

    assert (
        "Unrecognized boolean value 'enabled' for environment variable TEST_BOOL_ENV"
        in caplog.text
    )


def test_parse_bool_env_default(monkeypatch):
    monkeypatch.delenv("TEST_BOOL_ENV_MISSING", raising=False)
    assert _opentelemetry_metrics._parse_bool_env("TEST_BOOL_ENV_MISSING", True) is True
    assert (
        _opentelemetry_metrics._parse_bool_env("TEST_BOOL_ENV_MISSING", False) is False
    )


def test_dev_gate_locked_disables_metrics(monkeypatch):
    """When _ENABLE_METRICS_DEV_GATE is False, metrics must remain disabled."""
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", False)
    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS", "true")
    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_DEBUG_METRICS", "true")

    assert _opentelemetry_metrics.is_metrics_enabled() is False
    assert _opentelemetry_metrics.is_metrics_enabled(enable_metrics=True) is False
    assert _opentelemetry_metrics.is_debug_metrics_enabled() is False
    assert (
        _opentelemetry_metrics.is_debug_metrics_enabled(enable_debug_metrics=True)
        is False
    )


def test_dev_gate_unlocked_respects_env_var(monkeypatch):
    """When dev gate is open, environment variable enables metrics."""
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)

    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS", "true")
    assert _opentelemetry_metrics.is_metrics_enabled() is True

    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS", "false")
    assert _opentelemetry_metrics.is_metrics_enabled() is False


def test_metrics_default_is_disabled_when_env_unset(monkeypatch):
    """When env var is unset, default value is False."""
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)
    monkeypatch.delenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS", raising=False)
    monkeypatch.delenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_DEBUG_METRICS", raising=False)

    assert _opentelemetry_metrics.is_metrics_enabled() is False
    assert _opentelemetry_metrics.is_debug_metrics_enabled() is False


def test_client_setting_overrides_env_var(monkeypatch):
    """Client constructor parameter must take precedence over env var."""
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)

    # Client disables while env var is True
    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS", "true")
    assert _opentelemetry_metrics.is_metrics_enabled(enable_metrics=False) is False

    # Client enables while env var is False
    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS", "false")
    assert _opentelemetry_metrics.is_metrics_enabled(enable_metrics=True) is True


def test_non_boolean_client_setting_raises_type_error():
    """Passing a non-boolean setting such as 'false' must raise TypeError."""
    with pytest.raises(TypeError, match="enable_metrics must be a boolean or None"):
        _opentelemetry_metrics.is_metrics_enabled(enable_metrics="false")  # type: ignore[arg-type]

    with pytest.raises(
        TypeError, match="enable_debug_metrics must be a boolean or None"
    ):
        _opentelemetry_metrics.is_debug_metrics_enabled(
            enable_debug_metrics="false"  # type: ignore[arg-type]
        )


def test_debug_metrics_independent_of_base_metrics(monkeypatch):
    """Debug metrics can be enabled independently when base metrics are disabled."""
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)
    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS", "false")
    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_DEBUG_METRICS", "true")

    assert _opentelemetry_metrics.is_metrics_enabled() is False
    assert _opentelemetry_metrics.is_debug_metrics_enabled() is True
    assert _opentelemetry_metrics.is_metrics_enabled(enable_metrics=False) is False
    assert (
        _opentelemetry_metrics.is_debug_metrics_enabled(enable_debug_metrics=True)
        is True
    )


def test_debug_metrics_enabled(monkeypatch):
    """Debug metrics is enabled when debug flag is True."""
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)
    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_DEBUG_METRICS", "true")

    assert _opentelemetry_metrics.is_debug_metrics_enabled() is True

    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_DEBUG_METRICS", "false")
    assert _opentelemetry_metrics.is_debug_metrics_enabled() is False


def test_debug_metrics_client_setting_overrides_env_var(monkeypatch):
    """Client setting overrides debug metrics env var in both directions."""
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)

    # Client enables while debug env var is False
    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_DEBUG_METRICS", "false")
    assert (
        _opentelemetry_metrics.is_debug_metrics_enabled(enable_debug_metrics=True)
        is True
    )

    # Client disables while debug env var is True
    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_DEBUG_METRICS", "true")
    assert (
        _opentelemetry_metrics.is_debug_metrics_enabled(enable_debug_metrics=False)
        is False
    )


def test_otel_missing_disables_metrics(monkeypatch):
    """If opentelemetry-api is not installed, metrics must gracefully disable."""
    monkeypatch.setattr(_opentelemetry_metrics, "HAS_OPENTELEMETRY_METRICS", False)
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)
    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS", "true")
    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_DEBUG_METRICS", "true")

    assert _opentelemetry_metrics.is_metrics_enabled() is False
    assert _opentelemetry_metrics.is_debug_metrics_enabled() is False
    assert _opentelemetry_metrics.get_meter() is None
    assert _opentelemetry_metrics.get_meter(enable_metrics=True) is None
    assert _opentelemetry_metrics.get_meter(enable_debug_metrics=True) is None


def test_get_common_attributes():
    """Verify common attributes conform to GCS OTel specification."""
    attrs = _opentelemetry_metrics.get_common_attributes()
    assert set(attrs.keys()) == {
        "gcp.client.service",
        "gcp.client.version",
        "gcp.client.artifact",
    }
    assert "gcp.client.repo" not in attrs
    assert attrs["gcp.client.service"] == "storage"
    assert attrs["gcp.client.version"] == __version__
    assert attrs["gcp.client.artifact"] == "google-cloud-storage"

    attrs["gcp.client.service"] = "mutated"
    assert (
        _opentelemetry_metrics.get_common_attributes()["gcp.client.service"]
        == "storage"
    )


def test_get_meter(monkeypatch):
    """Verify get_meter requires active metrics and forwards meter_provider."""
    monkeypatch.delenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS", raising=False)
    monkeypatch.delenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_DEBUG_METRICS", raising=False)

    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", False)
    assert _opentelemetry_metrics.get_meter(enable_metrics=True) is None

    mock_metrics = mock.Mock()
    monkeypatch.setattr(_opentelemetry_metrics, "metrics", mock_metrics, raising=False)
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)

    # Disabled when neither env var nor client setting enables metrics
    assert _opentelemetry_metrics.get_meter() is None
    assert (
        _opentelemetry_metrics.get_meter(
            enable_metrics=False, enable_debug_metrics=False
        )
        is None
    )

    # Enabled via client_setting (standard metrics)
    mock_provider = mock.Mock()
    meter = _opentelemetry_metrics.get_meter(
        enable_metrics=True, meter_provider=mock_provider
    )
    assert meter is not None
    mock_metrics.get_meter.assert_called_once_with(
        "google.cloud.storage",
        __version__,
        meter_provider=mock_provider,
    )

    # Enabled via client_setting (debug metrics only)
    mock_metrics.get_meter.reset_mock()
    meter_debug = _opentelemetry_metrics.get_meter(
        enable_metrics=False,
        enable_debug_metrics=True,
        meter_provider=mock_provider,
    )
    assert meter_debug is not None
    mock_metrics.get_meter.assert_called_once_with(
        "google.cloud.storage",
        __version__,
        meter_provider=mock_provider,
    )

    # Enabled via environment variable
    mock_metrics.get_meter.reset_mock()
    monkeypatch.setenv("GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS", "true")
    meter_env = _opentelemetry_metrics.get_meter(meter_provider=mock_provider)
    assert meter_env is not None
    mock_metrics.get_meter.assert_called_once_with(
        "google.cloud.storage",
        __version__,
        meter_provider=mock_provider,
    )


# ---------------------------------------------------------------------------
# Histogram Bucket Boundaries & Views Tests
# ---------------------------------------------------------------------------
def test_histogram_bucket_boundaries():
    """Verify custom latency and byte-size bucket boundaries match specification."""
    latency = _opentelemetry_metrics.LATENCY_HISTOGRAM_BOUNDARIES
    assert len(latency) == 165
    assert latency[0] == 0.0
    assert latency[1] == 0.002
    assert latency[49] == 0.098
    assert latency[50] == 0.1
    assert latency[60] == 0.2
    assert latency[-1] < 300.0
    assert list(latency) == sorted(latency)

    sizes = _opentelemetry_metrics.SIZE_HISTOGRAM_BOUNDARIES
    assert len(sizes) == 48
    assert sizes[0] == 0
    assert sizes[1] == 128 * 1024
    assert sizes[32] == 4 * 1024 * 1024
    assert sizes[33] == int(4.25 * 1024 * 1024)
    assert sizes[34] == int(4.75 * 1024 * 1024)
    assert sizes[-1] == 8593866752
    assert list(sizes) == sorted(sizes)


def test_get_histogram_views_with_and_without_sdk(monkeypatch):
    """Verify get_histogram_views builds 6 Views when SDK is installed and [] otherwise."""
    fake_view_mod = types.ModuleType("opentelemetry.sdk.metrics.view")

    class FakeAggregation:
        def __init__(self, boundaries):
            self.boundaries = boundaries

    class FakeView:
        def __init__(self, instrument_name, aggregation, meter_name=None):
            self.instrument_name = instrument_name
            self.aggregation = aggregation
            self.meter_name = meter_name

    fake_view_mod.ExplicitBucketHistogramAggregation = FakeAggregation
    fake_view_mod.View = FakeView

    with monkeypatch.context() as m:
        m.setitem(sys.modules, "opentelemetry", types.ModuleType("opentelemetry"))
        m.setitem(
            sys.modules, "opentelemetry.sdk", types.ModuleType("opentelemetry.sdk")
        )
        m.setitem(
            sys.modules,
            "opentelemetry.sdk.metrics",
            types.ModuleType("opentelemetry.sdk.metrics"),
        )
        m.setitem(sys.modules, "opentelemetry.sdk.metrics.view", fake_view_mod)

        views = _opentelemetry_metrics.get_histogram_views()
        assert len(views) == 6
        assert all(v.meter_name == "google.cloud.storage" for v in views)
        latency_views = [
            v
            for v in views
            if v.instrument_name in _opentelemetry_metrics._LATENCY_METRIC_NAMES
        ]
        size_views = [
            v
            for v in views
            if v.instrument_name in _opentelemetry_metrics._SIZE_METRIC_NAMES
        ]
        assert len(latency_views) == 4
        assert len(size_views) == 2
        assert (
            latency_views[0].aggregation.boundaries
            == _opentelemetry_metrics.LATENCY_HISTOGRAM_BOUNDARIES
        )
        assert (
            size_views[0].aggregation.boundaries
            == _opentelemetry_metrics.SIZE_HISTOGRAM_BOUNDARIES
        )

    # Without opentelemetry-sdk installed
    with monkeypatch.context() as m:
        m.setitem(sys.modules, "opentelemetry.sdk.metrics.view", None)
        assert _opentelemetry_metrics.get_histogram_views() == []


# ---------------------------------------------------------------------------
# Error Classification (`classify_error_type`) Tests
# ---------------------------------------------------------------------------
def test_classify_error_type_none_and_status_codes():
    assert _opentelemetry_metrics.classify_error_type() == "OK"
    assert _opentelemetry_metrics.classify_error_type(None, status_code=200) == "OK"
    assert _opentelemetry_metrics.classify_error_type(None, status_code=206) == "OK"
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=True) == "OK"  # type: ignore[arg-type]
    )
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=400)
        == "INVALID_ARGUMENT"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=401)
        == "UNAUTHENTICATED"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=403)
        == "PERMISSION_DENIED"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=404) == "NOT_FOUND"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=408)
        == "DEADLINE_EXCEEDED"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=409) == "ABORTED"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=412)
        == "FAILED_PRECONDITION"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=416)
        == "OUT_OF_RANGE"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=429)
        == "RESOURCE_EXHAUSTED"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=499) == "CANCELLED"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=500) == "INTERNAL"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=501)
        == "UNIMPLEMENTED"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=503)
        == "UNAVAILABLE"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(None, status_code=504)
        == "DEADLINE_EXCEEDED"
    )
    assert _opentelemetry_metrics.classify_error_type(None, status_code=502) == "502"
    assert _opentelemetry_metrics.classify_error_type(None, status_code=99999) == "OK"


def test_classify_error_type_exceptions():
    # 1. Checksum Mismatch (including subclasses of DataCorruption)
    resp_mock = mock.Mock(status_code=200)
    assert (
        _opentelemetry_metrics.classify_error_type(
            storage_exceptions.DataCorruption(resp_mock, "crc mismatch")
        )
        == "CHECKSUM_MISMATCH"
    )

    class CustomDataCorruption(storage_exceptions.DataCorruption):
        pass

    assert (
        _opentelemetry_metrics.classify_error_type(
            CustomDataCorruption(resp_mock, "subclass mismatch")
        )
        == "CHECKSUM_MISMATCH"
    )

    # 2. Authentication Errors
    assert (
        _opentelemetry_metrics.classify_error_type(
            auth_exceptions.RefreshError("token expired")
        )
        == "AUTHENTICATION_ERROR"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(
            auth_exceptions.TransportError("auth transport error")
        )
        == "AUTHENTICATION_ERROR"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(
            auth_exceptions.DefaultCredentialsError("missing adc")
        )
        == "AUTHENTICATION_ERROR"
    )

    # 3. Cancellation
    assert (
        _opentelemetry_metrics.classify_error_type(asyncio.CancelledError())
        == "CANCELLED"
    )

    # 4. HTTP Conflict (409) consistency with status_code=409
    conflict_exc = api_exceptions.Conflict("conflict")
    assert _opentelemetry_metrics.classify_error_type(conflict_exc) == "ABORTED"

    # 5. gRPC / GoogleAPICallError status codes
    not_found_exc = api_exceptions.NotFound("not found")
    assert _opentelemetry_metrics.classify_error_type(not_found_exc) == "NOT_FOUND"

    custom_api_exc = api_exceptions.GoogleAPICallError("custom")
    custom_api_exc.grpc_status_code = "RAW_GRPC_STATUS"  # type: ignore[assignment]
    assert (
        _opentelemetry_metrics.classify_error_type(custom_api_exc) == "RAW_GRPC_STATUS"
    )

    # Direct grpc.RpcError-like exception with .code() method
    class FakeStatusCode:
        name = "DEADLINE_EXCEEDED"

    class FakeRpcError(Exception):
        def code(self):
            return FakeStatusCode()

    assert (
        _opentelemetry_metrics.classify_error_type(FakeRpcError())
        == "DEADLINE_EXCEEDED"
    )

    class FakeRpcErrorNoName(Exception):
        def code(self):
            return object()

    assert _opentelemetry_metrics.classify_error_type(FakeRpcErrorNoName()) == "UNKNOWN"

    # 6. HTTP status code on exception
    http_api_exc = api_exceptions.GoogleAPICallError("bad gateway")
    http_api_exc.code = 502
    http_api_exc.grpc_status_code = None
    assert _opentelemetry_metrics.classify_error_type(http_api_exc) == "502"

    invalid_resp_with_code = storage_exceptions.InvalidResponse(
        mock.Mock(status_code=429), "rate limited"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(invalid_resp_with_code)
        == "RESOURCE_EXHAUSTED"
    )

    req_http_err = requests.exceptions.HTTPError(response=mock.Mock(status_code=503))
    assert _opentelemetry_metrics.classify_error_type(req_http_err) == "UNAVAILABLE"

    # 7. Timeouts
    assert (
        _opentelemetry_metrics.classify_error_type(
            requests.exceptions.ConnectTimeout("connect timeout")
        )
        == "TIMEOUT"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(
            requests.exceptions.ReadTimeout("read timeout")
        )
        == "TIMEOUT"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(socket.timeout("timed out"))
        == "TIMEOUT"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(
            urllib3.exceptions.ReadTimeoutError(None, "/", "read timed out")  # type: ignore[arg-type]
        )
        == "TIMEOUT"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(concurrent.futures.TimeoutError())
        == "TIMEOUT"
    )
    retry_err = api_exceptions.RetryError(
        "deadline exceeded", cause=socket.timeout("timed out")
    )
    assert _opentelemetry_metrics.classify_error_type(retry_err) == "TIMEOUT"

    # 8. TLS / SSL Failure
    assert (
        _opentelemetry_metrics.classify_error_type(
            requests.exceptions.SSLError("cert verify failed")
        )
        == "TLS_FAILURE"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(ssl.SSLError("ssl handshake error"))
        == "TLS_FAILURE"
    )

    # 9. DNS, Connection Refused, Connection Reset (direct and wrapped in requests/urllib3)
    gai_err = socket.gaierror(-2, "Name or service not known")
    new_conn_err = urllib3.exceptions.NewConnectionError(None, "dns failed")  # type: ignore[arg-type]
    new_conn_err.__cause__ = gai_err
    wrapped_dns = requests.exceptions.ConnectionError(
        urllib3.exceptions.MaxRetryError(
            None,  # type: ignore[arg-type]
            "/",
            reason=new_conn_err,
        )
    )
    assert _opentelemetry_metrics.classify_error_type(wrapped_dns) == "DNS_FAILURE"

    refused_err = ConnectionRefusedError(111, "Connection refused")
    wrapped_refused = requests.exceptions.ConnectionError(refused_err)
    assert (
        _opentelemetry_metrics.classify_error_type(wrapped_refused)
        == "CONNECTION_ERROR"
    )

    reset_err = ConnectionResetError(104, "Connection reset by peer")
    wrapped_reset = requests.exceptions.ConnectionError(reset_err)
    assert (
        _opentelemetry_metrics.classify_error_type(wrapped_reset) == "CONNECTION_ERROR"
    )

    # 10. Generic Connection Errors
    assert (
        _opentelemetry_metrics.classify_error_type(
            requests.exceptions.ConnectionError("connection aborted")
        )
        == "CONNECTION_ERROR"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(
            requests.exceptions.ChunkedEncodingError("incomplete read")
        )
        == "CONNECTION_ERROR"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(OSError("network unreachable"))
        == "CONNECTION_ERROR"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(
            http.client.IncompleteRead(b"partial", 10)
        )
        == "CONNECTION_ERROR"
    )

    # 11. Explicit status_code fallback when exception is generic
    assert (
        _opentelemetry_metrics.classify_error_type(
            RuntimeError("unexpected"), status_code=503
        )
        == "UNAVAILABLE"
    )

    # 12. Client Validation Errors
    assert (
        _opentelemetry_metrics.classify_error_type(ValueError("bad arg"))
        == "CLIENT_VALIDATION_ERROR"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(TypeError("bad type"))
        == "CLIENT_VALIDATION_ERROR"
    )
    invalid_resp_no_code = storage_exceptions.InvalidResponse(
        mock.Mock(status_code=None), "missing header"
    )
    assert (
        _opentelemetry_metrics.classify_error_type(invalid_resp_no_code)
        == "CLIENT_VALIDATION_ERROR"
    )

    # 13. Cyclic exception chain and unknown exception
    e1 = RuntimeError("cycle 1")
    e2 = RuntimeError("cycle 2", e1)
    e1.__cause__ = e2
    assert _opentelemetry_metrics.classify_error_type(e1) == "UNKNOWN"


# ---------------------------------------------------------------------------
# Route Normalization (`normalize_url_template`) Tests
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "raw_url,expected",
    [
        (None, "UNKNOWN"),
        ("", "UNKNOWN"),
        (123, "UNKNOWN"),
        ("https://storage.googleapis.com", "UNKNOWN"),
        ("/", "UNKNOWN"),
        ("///", "UNKNOWN"),
        (
            "https://storage.googleapis.com//storage/v1/b/my-bucket//",
            "/storage/v1/b/{bucket}",
        ),
        (
            "https://storage.googleapis.com/upload/storage/v1/b/my-bucket/o/my-obj?uploadType=resumable",
            "/upload/storage/v1/b/{bucket}/o",
        ),
        (
            "https://storage.googleapis.com/custom/path?tag=my_uploads",
            "UNKNOWN",
        ),
        (
            "https://storage.googleapis.com/custom/path?my_uploadId=123",
            "UNKNOWN",
        ),
        (
            "https://storage.googleapis.com/storage/v1/b?project=my-proj",
            "/storage/v1/b",
        ),
        ("/b?project=my-proj", "/storage/v1/b"),
        (
            "https://storage.googleapis.com/storage/v1/b/my-bucket?projection=full",
            "/storage/v1/b/{bucket}",
        ),
        ("/b/my-bucket/", "/storage/v1/b/{bucket}"),
        ("b/my-bucket", "/storage/v1/b/{bucket}"),
        (
            "https://storage.googleapis.com/storage/v1/b/my-bucket/o?prefix=foo",
            "/storage/v1/b/{bucket}/o",
        ),
        ("/b/my-bucket/o", "/storage/v1/b/{bucket}/o"),
        (
            "https://storage.googleapis.com/storage/v1/b/my-bucket/o/folder%2Ffile.txt?generation=1",
            "/storage/v1/b/{bucket}/o/{object}",
        ),
        ("/b/my-bucket/o/file.txt", "/storage/v1/b/{bucket}/o/{object}"),
        (
            "https://storage.googleapis.com/storage/v1/b/my-bucket/o/dest.txt/compose",
            "/storage/v1/b/{bucket}/o/{object}/compose",
        ),
        (
            "/b/my-bucket/o/dest.txt/compose",
            "/storage/v1/b/{bucket}/o/{object}/compose",
        ),
        (
            "https://storage.googleapis.com/storage/v1/b/src-b/o/src-o/rewriteTo/b/dst-b/o/dst-o",
            "/storage/v1/b/{bucket}/o/{object}/rewriteTo/b/{bucket}/o/{object}",
        ),
        (
            "/b/src-b/o/src-o/rewriteTo/b/dst-b/o/dst-o",
            "/storage/v1/b/{bucket}/o/{object}/rewriteTo/b/{bucket}/o/{object}",
        ),
        (
            "https://storage.googleapis.com/storage/v1/b/src-b/o/src-o/copyTo/b/dst-b/o/dst-o",
            "/storage/v1/b/{bucket}/o/{object}/copyTo/b/{bucket}/o/{object}",
        ),
        (
            "/b/src-b/o/src-o/copyTo/b/dst-b/o/dst-o",
            "/storage/v1/b/{bucket}/o/{object}/copyTo/b/{bucket}/o/{object}",
        ),
        (
            "https://storage.googleapis.com/storage/v1/b/my-bucket/o/src-o/moveTo/o/dst-o",
            "/storage/v1/b/{bucket}/o/{object}/moveTo/o/{object}",
        ),
        (
            "/b/my-bucket/o/src-o/moveTo/o/dst-o",
            "/storage/v1/b/{bucket}/o/{object}/moveTo/o/{object}",
        ),
        (
            "https://storage.googleapis.com/storage/v1/b/my-bucket/o/my-o/restore",
            "/storage/v1/b/{bucket}/o/{object}/restore",
        ),
        (
            "/b/my-bucket/o/my-o/restore",
            "/storage/v1/b/{bucket}/o/{object}/restore",
        ),
        (
            "/b/my-bucket/o/my-o/acl",
            "/storage/v1/b/{bucket}/o/{object}/acl",
        ),
        (
            "/b/my-bucket/o/my-o/acl/allUsers",
            "/storage/v1/b/{bucket}/o/{object}/acl/{entity}",
        ),
        (
            "/b/my-bucket/o/my-o/iam",
            "/storage/v1/b/{bucket}/o/{object}/iam",
        ),
        (
            "/b/my-bucket/o/my-o/iam/testPermissions",
            "/storage/v1/b/{bucket}/o/{object}/iam",
        ),
        (
            "/b/my-bucket/acl",
            "/storage/v1/b/{bucket}/acl",
        ),
        (
            "/b/my-bucket/acl/allUsers",
            "/storage/v1/b/{bucket}/acl/{entity}",
        ),
        (
            "/b/my-bucket/defaultObjectAcl",
            "/storage/v1/b/{bucket}/defaultObjectAcl",
        ),
        (
            "/b/my-bucket/defaultObjectAcl/allUsers",
            "/storage/v1/b/{bucket}/defaultObjectAcl/{entity}",
        ),
        (
            "/b/my-bucket/restore",
            "/storage/v1/b/{bucket}/restore",
        ),
        (
            "https://storage.googleapis.com/storage/v1/b/my-bucket/iam/testPermissions",
            "/storage/v1/b/{bucket}/iam",
        ),
        ("/b/my-bucket/iam", "/storage/v1/b/{bucket}/iam"),
        (
            "https://storage.googleapis.com/storage/v1/b/my-bucket/notificationConfigs",
            "/storage/v1/b/{bucket}/notificationConfigs",
        ),
        (
            "/b/my-bucket/notificationConfigs",
            "/storage/v1/b/{bucket}/notificationConfigs",
        ),
        (
            "https://storage.googleapis.com/storage/v1/b/my-bucket/notificationConfigs/42",
            "/storage/v1/b/{bucket}/notificationConfigs/{notification}",
        ),
        (
            "/b/my-bucket/notificationConfigs/42",
            "/storage/v1/b/{bucket}/notificationConfigs/{notification}",
        ),
        (
            "https://storage.googleapis.com/storage/v1/b/my-bucket/lockRetentionPolicy",
            "/storage/v1/b/{bucket}/lockRetentionPolicy",
        ),
        (
            "/b/my-bucket/lockRetentionPolicy",
            "/storage/v1/b/{bucket}/lockRetentionPolicy",
        ),
        (
            "/storage/v1/projects/my-proj/serviceAccount",
            "/storage/v1/projects/{project}/serviceAccount",
        ),
        (
            "/projects/my-proj/serviceAccount",
            "/storage/v1/projects/{project}/serviceAccount",
        ),
        (
            "/storage/v1/projects/my-proj/hmacKeys",
            "/storage/v1/projects/{project}/hmacKeys",
        ),
        ("/projects/my-proj/hmacKeys", "/storage/v1/projects/{project}/hmacKeys"),
        (
            "/storage/v1/projects/my-proj/hmacKeys/GOOG123",
            "/storage/v1/projects/{project}/hmacKeys/{access_id}",
        ),
        (
            "/projects/my-proj/hmacKeys/GOOG123",
            "/storage/v1/projects/{project}/hmacKeys/{access_id}",
        ),
        (
            "https://storage.googleapis.com/upload/storage/v1/b/my-bucket/o?uploadType=resumable",
            "/upload/storage/v1/b/{bucket}/o",
        ),
        (
            "https://storage.googleapis.com/download/storage/v1/b/my-bucket/o/my-obj?alt=media",
            "/download/storage/v1/b/{bucket}/o/{object}",
        ),
        ("https://storage.googleapis.com/batch/storage/v1", "/batch/storage/v1"),
        (
            "https://storage.googleapis.com/my-bucket/my-object?uploads",
            "/{bucket}/{object}",
        ),
        (
            "https://storage.googleapis.com/my-bucket/nested/dir/object.bin?uploadId=xyz&partNumber=2",
            "/{bucket}/{object}",
        ),
        (
            "https://storage.googleapis.com/unrecognized/two-segment",
            "UNKNOWN",
        ),
        ("https://storage.googleapis.com/storage/v2", "UNKNOWN"),
        ("https://storage.googleapis.com/storage/v2/other?uploadId=xyz", "UNKNOWN"),
        ("https://storage.googleapis.com/custom/unrecognized/path/here", "UNKNOWN"),
        ("https://[::1/storage/v1/b", "UNKNOWN"),
    ],
)
def test_normalize_url_template(raw_url, expected):
    assert _opentelemetry_metrics.normalize_url_template(raw_url) == expected


# ---------------------------------------------------------------------------
# Logical Operation Context (`start_operation`) Tests
# ---------------------------------------------------------------------------
def test_start_operation_disabled_and_nesting(monkeypatch):
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)
    mock_metrics = mock.Mock()
    mock_meter = mock.Mock()
    mock_meter.create_histogram.side_effect = lambda *a, **kw: mock.Mock()
    mock_meter.create_counter.side_effect = lambda *a, **kw: mock.Mock()
    mock_metrics.get_meter.return_value = mock_meter
    monkeypatch.setattr(_opentelemetry_metrics, "metrics", mock_metrics, raising=False)

    # Disabled recorder -> yields None and records nothing
    disabled_recorder = _opentelemetry_metrics._MetricsRecorder(enable_metrics=False)
    with _opentelemetry_metrics.start_operation(
        disabled_recorder, "storage.Blob.reload", "storage.objects.get"
    ) as op:
        assert op is None
        assert _opentelemetry_metrics.get_current_operation() is None

    # Enabled recorder -> outermost call records, nested call is suppressed
    enabled_recorder = _opentelemetry_metrics._MetricsRecorder(enable_metrics=True)
    with _opentelemetry_metrics.start_operation(
        enabled_recorder,
        "storage.Blob.download_to_filename",
        "storage.objects.get",
    ) as outer_op:
        assert outer_op is not None
        assert outer_op.client_method == "storage.Blob.download_to_filename"
        assert outer_op.rpc_method == "storage.objects.get"
        assert _opentelemetry_metrics.get_current_operation() == outer_op

        with _opentelemetry_metrics.start_operation(
            enabled_recorder,
            "storage.Blob.download_to_file",
            "storage.objects.get",
        ) as inner_op:
            assert inner_op is outer_op

    assert _opentelemetry_metrics.get_current_operation() is None
    enabled_recorder.client_request_duration.record.assert_called_once()
    enabled_recorder.operations_counter.add.assert_called_once()
    _, kwargs = enabled_recorder.operations_counter.add.call_args
    assert (
        kwargs["attributes"]["gcp.client.method"] == "storage.Blob.download_to_filename"
    )
    assert kwargs["attributes"]["gcp.storage.operation"] == "storage.objects.get"
    assert kwargs["attributes"]["error.type"] == "OK"


def test_start_operation_exception_and_suppression(monkeypatch):
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)
    mock_metrics = mock.Mock()
    mock_meter = mock.Mock()
    mock_meter.create_histogram.side_effect = lambda *a, **kw: mock.Mock()
    mock_meter.create_counter.side_effect = lambda *a, **kw: mock.Mock()
    mock_metrics.get_meter.return_value = mock_meter
    monkeypatch.setattr(_opentelemetry_metrics, "metrics", mock_metrics, raising=False)

    recorder = _opentelemetry_metrics._MetricsRecorder(enable_metrics=True)

    with pytest.raises(api_exceptions.NotFound):
        with _opentelemetry_metrics.start_operation(
            recorder, "storage.Bucket.get_blob", "storage.objects.get"
        ):
            raise api_exceptions.NotFound("missing")

    assert _opentelemetry_metrics.get_current_operation() is None
    _, kwargs = recorder.operations_counter.add.call_args
    assert kwargs["attributes"]["error.type"] == "NOT_FOUND"

    # Suppressed outer operation (e.g. transfer_manager worker) suppresses both
    # logical operation metrics and body size recording
    recorder.operations_counter.add.reset_mock()
    recorder.client_request_duration.record.reset_mock()
    with _opentelemetry_metrics.start_operation(
        None,
        "storage.transfer_manager.download_many_to_path",
        "storage.objects.get",
        suppress=True,
    ) as suppressed_op:
        assert suppressed_op is not None
        assert suppressed_op.suppressed is True
        with _opentelemetry_metrics.start_operation(
            recorder,
            "storage.Blob.download_to_filename",
            "storage.objects.get",
        ):
            recorder.record_request_body_size(2048)
            recorder.record_response_body_size(4096)

    assert _opentelemetry_metrics.get_current_operation() is None
    recorder.operations_counter.add.assert_not_called()
    recorder.client_request_duration.record.assert_not_called()
    recorder.request_body_size.record.assert_not_called()
    recorder.response_body_size.record.assert_not_called()

    # Nested suppress=True inside an active unsuppressed operation (e.g. BlobReader prefetch)
    with _opentelemetry_metrics.start_operation(
        recorder,
        "storage.Blob.open",
        "storage.objects.get",
    ) as active_op:
        assert active_op is not None and active_op.suppressed is False
        with _opentelemetry_metrics.start_operation(
            recorder,
            "storage.Blob.download_as_bytes",
            "storage.objects.get",
            suppress=True,
        ) as child_suppressed:
            assert child_suppressed is not None
            assert child_suppressed.suppressed is True
            assert child_suppressed.client_method == "storage.Blob.open"
            # Prefetch body size and TTFB are suppressed inside child_suppressed
            recorder.record_response_body_size(40 * 1024 * 1024)
            recorder.record_ttfb(0.05)
        # Outside the suppressed prefetch block, actual user bytes are recorded
        assert _opentelemetry_metrics.get_current_operation() == active_op
        recorder.record_response_body_size(1024)
        recorder.record_response_body_size(True)  # type: ignore[arg-type]
        recorder.record_request_body_size(False)  # type: ignore[arg-type]

    recorder.response_body_size.record.assert_called_once()
    assert recorder.response_body_size.record.call_args[0][0] == 1024
    recorder.operation_ttfb.record.assert_not_called()
    recorder.operations_counter.add.assert_called_once()


def test_start_operation_asyncio_concurrency_isolation(monkeypatch):
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)
    mock_metrics = mock.Mock()
    mock_meter = mock.Mock()
    mock_meter.create_histogram.side_effect = lambda *a, **kw: mock.Mock()
    mock_meter.create_counter.side_effect = lambda *a, **kw: mock.Mock()
    mock_metrics.get_meter.return_value = mock_meter
    monkeypatch.setattr(_opentelemetry_metrics, "metrics", mock_metrics, raising=False)

    recorder = _opentelemetry_metrics._MetricsRecorder(
        enable_metrics=True, rpc_system="grpc"
    )

    async def worker(method_name: str, rpc_name: str):
        with _opentelemetry_metrics.start_operation(recorder, method_name, rpc_name):
            await asyncio.sleep(0.005)
            current = _opentelemetry_metrics.get_current_operation()
            assert current is not None
            assert current.client_method == method_name
            assert current.rpc_method == rpc_name

    async def run_all():
        await asyncio.gather(
            worker(
                "storage.asyncio.AsyncMultiRangeDownloader.download_ranges",
                "google.storage.v2.Storage/BidiReadObject",
            ),
            worker(
                "storage.asyncio.AsyncAppendableObjectWriter.append",
                "google.storage.v2.Storage/BidiWriteObject",
            ),
        )

    asyncio.run(run_all())
    assert recorder.operations_counter.add.call_count == 2


# ---------------------------------------------------------------------------
# `_extract_server_address` & `_MetricsRecorder` Tests
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "endpoint,expected",
    [
        (None, "storage.googleapis.com"),
        ("", "storage.googleapis.com"),
        ("   ", "storage.googleapis.com"),
        ("https://storage.googleapis.com:443", "storage.googleapis.com"),
        ("storage.googleapis.com:443", "storage.googleapis.com"),
        ("//storage.googleapis.com:443", "storage.googleapis.com"),
        ("https://[::1]:8080", "::1"),
        ("http://localhost:9023/storage/v1", "localhost"),
        ("https://", "storage.googleapis.com"),
        ("https://[::1", "storage.googleapis.com"),
        ("[::1", "storage.googleapis.com"),
        ("dns://8.8.8.8/custom.endpoint.com:443", "custom.endpoint.com"),
        ("dns:custom.endpoint.com:443", "custom.endpoint.com"),
        ("dns://custom.endpoint.com:443", "custom.endpoint.com"),
        ("dns://8.8.8.8/", "storage.googleapis.com"),
        ("ipv4:127.0.0.1:443", "127.0.0.1"),
        ("ipv6:[::1]:443", "::1"),
    ],
)
def test_extract_server_address(endpoint, expected):
    assert _opentelemetry_metrics._extract_server_address(endpoint) == expected


def test_metrics_recorder_recording_and_shutdown(monkeypatch):
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)
    mock_metrics = mock.Mock()
    mock_meter = mock.Mock()
    mock_meter.create_histogram.side_effect = lambda *a, **kw: mock.Mock()
    mock_meter.create_counter.side_effect = lambda *a, **kw: mock.Mock()
    mock_metrics.get_meter.return_value = mock_meter
    monkeypatch.setattr(_opentelemetry_metrics, "metrics", mock_metrics, raising=False)

    mock_provider = mock.Mock()
    recorder = _opentelemetry_metrics._MetricsRecorder(
        enable_metrics=True,
        meter_provider=mock_provider,
        api_endpoint="https://custom.storage.googleapis.com:443",
        rpc_system="http",
    )
    assert recorder.standard_enabled is True
    assert recorder.enabled is True
    assert recorder.server_address == "custom.storage.googleapis.com"

    base_attrs = recorder.get_base_attributes()
    assert base_attrs["server.address"] == "custom.storage.googleapis.com"
    assert base_attrs["rpc.system.name"] == "http"

    # Verify exact instrument names, units, and descriptions
    histogram_specs = {
        call.args[0]: (call.kwargs["unit"], call.kwargs["description"])
        for call in mock_meter.create_histogram.call_args_list
    }
    assert histogram_specs == {
        "rpc.client.call.duration": (
            "s",
            "Duration of an individual gRPC attempt in seconds (excluding retries).",
        ),
        "http.client.request.duration": (
            "s",
            "Duration of an individual HTTP request attempt in seconds (excluding retries).",
        ),
        "gcp.client.request.duration": (
            "s",
            "End-to-end latency of a logical user-facing Veneer operation in seconds.",
        ),
        "gcp.storage.client.request.body.size": (
            "By",
            "Application payload bytes submitted by the caller for an upload or write operation.",
        ),
        "gcp.storage.client.response.body.size": (
            "By",
            "Application payload bytes delivered to the caller.",
        ),
        "gcp.storage.client.ttfb": (
            "s",
            "Time elapsed from attempt initiation to receipt of the first response byte.",
        ),
    }
    counter_specs = {
        call.args[0]: (call.kwargs["unit"], call.kwargs["description"])
        for call in mock_meter.create_counter.call_args_list
    }
    assert counter_specs == {
        "gcp.storage.client.operations": (
            "{operation}",
            "Number of logical GCS client operations.",
        ),
        "gcp.storage.client.attempts": (
            "{attempt}",
            "Number of physical network transport attempts executed.",
        ),
        "gcp.storage.client.retries": (
            "{retry}",
            "Number of transport retries executed after a failed attempt.",
        ),
        "gcp.storage.client.errors": (
            "{error}",
            "Number of physical network transport attempts terminating with a non-OK status.",
        ),
    }

    # Record within a logical operation context
    with _opentelemetry_metrics.start_operation(
        recorder,
        "storage.Blob.upload_from_string",
        "WriteObject",
        rpc_method="google.storage.v2.Storage/WriteObject",
    ):
        recorder.record_http_attempt(
            duration=0.05,
            http_method="post",
            url_template="/upload/storage/v1/b/{bucket}/o",
            status_code=503,
            error_type="UNAVAILABLE",
            network_path="cloudpath",
        )
        recorder.record_http_attempt(
            duration=0.04,
            http_method="POST",
            url_template="/upload/storage/v1/b/{bucket}/o",
            status_code=200,
            error_type="OK",
            network_path="cloudpath",
        )
        recorder.record_request_body_size(1024)
        recorder.record_response_body_size(512)
        recorder.record_ttfb(0.01, network_path="cloudpath")

    # Logical operation metrics: duration has rpc.method; operations counter does not
    recorder.client_request_duration.record.assert_called_once()
    _, req_dur_kwargs = recorder.client_request_duration.record.call_args
    assert req_dur_kwargs["attributes"]["gcp.storage.operation"] == "WriteObject"
    assert (
        req_dur_kwargs["attributes"]["rpc.method"]
        == "google.storage.v2.Storage/WriteObject"
    )
    assert (
        req_dur_kwargs["attributes"]["gcp.client.method"]
        == "storage.Blob.upload_from_string"
    )
    assert req_dur_kwargs["attributes"]["error.type"] == "OK"

    recorder.operations_counter.add.assert_called_once()
    _, op_cnt_kwargs = recorder.operations_counter.add.call_args
    assert op_cnt_kwargs["attributes"]["gcp.storage.operation"] == "WriteObject"
    assert "rpc.method" not in op_cnt_kwargs["attributes"]

    assert recorder.http_request_duration.record.call_count == 2
    _, http_dur_kwargs = recorder.http_request_duration.record.call_args_list[0]
    assert http_dur_kwargs["attributes"]["http.request.method"] == "POST"
    assert (
        http_dur_kwargs["attributes"]["url.template"]
        == "/upload/storage/v1/b/{bucket}/o"
    )
    assert http_dur_kwargs["attributes"]["http.response.status_code"] == 503
    assert http_dur_kwargs["attributes"]["error.type"] == "UNAVAILABLE"
    assert http_dur_kwargs["attributes"]["network.path"] == "cloudpath"
    assert "gcp.storage.operation" not in http_dur_kwargs["attributes"]
    assert "gcp.client.method" not in http_dur_kwargs["attributes"]

    assert recorder.attempts_counter.add.call_count == 2
    _, attempt_kwargs = recorder.attempts_counter.add.call_args_list[0]
    assert attempt_kwargs["attributes"]["gcp.storage.operation"] == "WriteObject"
    assert attempt_kwargs["attributes"]["http.response.status_code"] == 503
    assert attempt_kwargs["attributes"]["error.type"] == "UNAVAILABLE"
    assert attempt_kwargs["attributes"]["network.path"] == "cloudpath"
    assert "url.template" not in attempt_kwargs["attributes"]
    assert "http.request.method" not in attempt_kwargs["attributes"]
    assert "gcp.client.method" not in attempt_kwargs["attributes"]

    # Retry counter incremented once for the second attempt after 503 UNAVAILABLE
    recorder.retries_counter.add.assert_called_once()
    _, http_retry_kwargs = recorder.retries_counter.add.call_args
    assert http_retry_kwargs["attributes"]["gcp.storage.operation"] == "WriteObject"
    assert http_retry_kwargs["attributes"]["error.type"] == "UNAVAILABLE"
    assert http_retry_kwargs["attributes"]["network.path"] == "cloudpath"
    assert "gcp.client.method" not in http_retry_kwargs["attributes"]

    # Only the 503 attempt records an error (no gcp.client.method on errors)
    recorder.errors_counter.add.assert_called_once()
    _, err_kwargs = recorder.errors_counter.add.call_args
    assert err_kwargs["attributes"]["error.type"] == "UNAVAILABLE"
    assert err_kwargs["attributes"]["gcp.storage.operation"] == "WriteObject"
    assert err_kwargs["attributes"]["network.path"] == "cloudpath"
    assert "gcp.client.method" not in err_kwargs["attributes"]
    assert "url.template" not in err_kwargs["attributes"]
    assert "http.response.status_code" not in err_kwargs["attributes"]

    recorder.request_body_size.record.assert_called_once()
    recorder.response_body_size.record.assert_called_once()
    recorder.ttfb.record.assert_called_once()
    _, ttfb_kwargs = recorder.ttfb.record.call_args
    assert ttfb_kwargs["attributes"]["gcp.storage.operation"] == "WriteObject"
    assert ttfb_kwargs["attributes"]["network.path"] == "cloudpath"
    assert "gcp.client.method" not in ttfb_kwargs["attributes"]

    # gRPC attempt recording (UNAVAILABLE -> OK retry sequence)
    recorder.errors_counter.add.reset_mock()
    recorder.attempts_counter.add.reset_mock()
    recorder.retries_counter.add.reset_mock()
    with _opentelemetry_metrics.start_operation(
        recorder,
        "storage.asyncio.AsyncMultiRangeDownloader.download_ranges",
        "ReadObject",
        rpc_method="google.storage.v2.Storage/BidiReadObject",
    ):
        recorder.record_rpc_attempt(
            duration=0.03,
            operation="ReadObject",
            status_code="UNAVAILABLE",
            error_type="UNAVAILABLE",
            rpc_method="google.storage.v2.Storage/BidiReadObject",
            network_path="directpath",
        )
        recorder.record_rpc_attempt(
            duration=0.02,
            operation="ReadObject",
            status_code="OK",
            error_type="OK",
            rpc_method="google.storage.v2.Storage/BidiReadObject",
            network_path="directpath",
        )
    assert recorder.rpc_call_duration.record.call_count == 2
    _, rpc_dur_kwargs = recorder.rpc_call_duration.record.call_args_list[1]
    assert (
        rpc_dur_kwargs["attributes"]["rpc.method"]
        == "google.storage.v2.Storage/BidiReadObject"
    )
    assert rpc_dur_kwargs["attributes"]["rpc.response.status_code"] == "OK"
    assert rpc_dur_kwargs["attributes"]["error.type"] == "OK"
    assert rpc_dur_kwargs["attributes"]["network.path"] == "directpath"
    assert "gcp.storage.operation" not in rpc_dur_kwargs["attributes"]
    assert "gcp.client.method" not in rpc_dur_kwargs["attributes"]

    assert recorder.attempts_counter.add.call_count == 2
    _, rpc_attempt_kwargs = recorder.attempts_counter.add.call_args_list[1]
    assert rpc_attempt_kwargs["attributes"]["gcp.storage.operation"] == "ReadObject"
    assert rpc_attempt_kwargs["attributes"]["rpc.response.status_code"] == "OK"
    assert rpc_attempt_kwargs["attributes"]["error.type"] == "OK"
    assert rpc_attempt_kwargs["attributes"]["network.path"] == "directpath"
    assert "gcp.client.method" not in rpc_attempt_kwargs["attributes"]
    assert "rpc.method" not in rpc_attempt_kwargs["attributes"]

    recorder.errors_counter.add.assert_called_once()
    _, rpc_err_kwargs = recorder.errors_counter.add.call_args
    assert rpc_err_kwargs["attributes"]["gcp.storage.operation"] == "ReadObject"
    assert rpc_err_kwargs["attributes"]["error.type"] == "UNAVAILABLE"
    assert rpc_err_kwargs["attributes"]["network.path"] == "directpath"
    assert "gcp.client.method" not in rpc_err_kwargs["attributes"]
    assert "rpc.response.status_code" not in rpc_err_kwargs["attributes"]

    recorder.retries_counter.add.assert_called_once()
    _, rpc_retry_kwargs = recorder.retries_counter.add.call_args
    assert rpc_retry_kwargs["attributes"]["gcp.storage.operation"] == "ReadObject"
    assert rpc_retry_kwargs["attributes"]["error.type"] == "UNAVAILABLE"
    assert rpc_retry_kwargs["attributes"]["network.path"] == "directpath"

    # Record outside of start_operation with status_code=None and callable .code() returning None
    recorder.record_http_attempt(
        duration=0.01,
        http_method="GET",
        url_template="/storage/v1/b",
        status_code=None,
        error_type="UNKNOWN",
    )
    recorder.record_rpc_attempt(
        duration=0.01,
        operation="google.storage.v2.Storage/GetObject",
        status_code=None,
        error_type="UNKNOWN",
    )
    recorder.record_request_body_size(64)

    class _NoneCodeErr(Exception):
        def code(self):
            return None

    class _NonTupleArgsErr(Exception):
        args = 123  # type: ignore[assignment]

    assert _opentelemetry_metrics.classify_error_type(_NoneCodeErr()) == "UNKNOWN"
    assert _opentelemetry_metrics.classify_error_type(_NonTupleArgsErr()) == "UNKNOWN"
    assert (
        _opentelemetry_metrics.classify_error_type(concurrent.futures.CancelledError())
        == "CANCELLED"
    )
    assert (
        _opentelemetry_metrics._is_subclass_by_module(
            mock.MagicMock(__mro__=123), "google.cloud.storage", {"DataCorruption"}
        )
        is False
    )
    assert (
        _opentelemetry_metrics.classify_error_type(
            urllib3.exceptions.NewConnectionError(None, "conn err")
        )
        == "CONNECTION_ERROR"
    )

    # Shutdown flushes custom meter_provider and swallows force_flush errors gracefully
    recorder.shutdown()
    mock_provider.force_flush.assert_called_once()

    mock_provider.force_flush.side_effect = RuntimeError("flush failed")
    recorder.shutdown()  # Must not raise


def test_get_active_recorder_and_grpc_uri_schemes(monkeypatch):
    monkeypatch.setattr(_opentelemetry_metrics, "HAS_OPENTELEMETRY_METRICS", True)
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)

    assert (
        _opentelemetry_metrics._extract_server_address("dns:///custom.endpoint.com:443")
        == "custom.endpoint.com"
    )
    assert (
        _opentelemetry_metrics._extract_server_address(
            "google-c2p-experimental:///storage.googleapis.com"
        )
        == "storage.googleapis.com"
    )

    # Unconfigured MagicMock should not be treated as an active recorder
    unconfigured_mock = mock.MagicMock()
    assert _opentelemetry_metrics.get_active_recorder(unconfigured_mock) is None
    assert _opentelemetry_metrics.get_active_recorder(None) is None

    active_rec = _opentelemetry_metrics._MetricsRecorder(enable_metrics=True)
    holder = mock.MagicMock()
    holder._metrics_recorder = active_rec
    assert _opentelemetry_metrics.get_active_recorder(holder) is active_rec

    disabled_rec = _opentelemetry_metrics._MetricsRecorder(enable_metrics=False)
    holder._metrics_recorder = disabled_rec
    assert _opentelemetry_metrics.get_active_recorder(holder) is None


def test_metrics_recorder_disabled_no_ops(monkeypatch):
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", False)
    recorder = _opentelemetry_metrics._MetricsRecorder(enable_metrics=True)
    assert recorder.standard_enabled is False
    assert recorder.enabled is False

    # All recording methods are safe no-ops when disabled
    recorder.record_logical_operation(0.1, "m", "op")
    recorder.record_retry("ReadObject", "UNAVAILABLE", "cloudpath")
    recorder.record_http_attempt(0.1, "GET", "/storage/v1/b")
    recorder.record_rpc_attempt(0.1, "google.storage.v2.Storage/ReadObject")
    recorder.record_request_body_size(100)
    recorder.record_response_body_size(100)
    recorder.record_ttfb(0.01)
    recorder.shutdown()


def test_normalize_logical_operation_and_resolve_rpc_method():
    assert _opentelemetry_metrics.normalize_logical_operation(None) == "UNKNOWN"
    assert _opentelemetry_metrics.normalize_logical_operation("") == "UNKNOWN"
    assert _opentelemetry_metrics.normalize_logical_operation(123) == "UNKNOWN"  # type: ignore[arg-type]
    assert _opentelemetry_metrics.normalize_logical_operation("///") == "UNKNOWN"
    assert (
        _opentelemetry_metrics.normalize_logical_operation(
            "google.storage.v2.Storage/BidiReadObject"
        )
        == "ReadObject"
    )
    assert (
        _opentelemetry_metrics.normalize_logical_operation(
            "/google.storage.v2.Storage/BidiWriteObject"
        )
        == "WriteObject"
    )
    assert (
        _opentelemetry_metrics.normalize_logical_operation(
            "google.storage.v2.Storage/GetObject"
        )
        == "GetObject"
    )
    assert (
        _opentelemetry_metrics.normalize_logical_operation("GetNotificationConfig")
        == "GetNotificationConfig"
    )

    assert _opentelemetry_metrics.resolve_rpc_method(None, None) == "UNKNOWN"
    assert _opentelemetry_metrics.resolve_rpc_method("", "") == "UNKNOWN"
    assert _opentelemetry_metrics.resolve_rpc_method("///", None) == "UNKNOWN"
    assert _opentelemetry_metrics.resolve_rpc_method("UNKNOWN", None) == "UNKNOWN"
    assert (
        _opentelemetry_metrics.resolve_rpc_method(
            "ReadObject", "google.storage.v2.Storage/BidiReadObject"
        )
        == "google.storage.v2.Storage/BidiReadObject"
    )
    assert (
        _opentelemetry_metrics.resolve_rpc_method("ReadObject")
        == "google.storage.v2.Storage/ReadObject"
    )
    assert (
        _opentelemetry_metrics.resolve_rpc_method("GetNotificationConfig")
        == "google.storage.v1.Storage/GetNotificationConfig"
    )
    assert (
        _opentelemetry_metrics.resolve_rpc_method("storage.objects.get")
        == "storage.objects.get"
    )


def test_iter_exception_chain_traverses_errors_list():
    wrapped = api_exceptions.Aborted(
        "aborted",
        errors=[socket.timeout("nested timeout in errors")],
    )
    chain = list(_opentelemetry_metrics._iter_exception_chain(wrapped))
    assert any(isinstance(item, socket.timeout) for item in chain)

    class _NonSeqErrorsErr(Exception):
        errors = 123

    assert _opentelemetry_metrics.classify_error_type(_NonSeqErrorsErr()) == "UNKNOWN"


def test_operation_state_and_retry_helpers(monkeypatch):
    monkeypatch.setattr(_opentelemetry_metrics, "_ENABLE_METRICS_DEV_GATE", True)
    mock_metrics = mock.Mock()
    mock_meter = mock.Mock()
    mock_meter.create_histogram.side_effect = lambda *a, **kw: mock.Mock()
    mock_meter.create_counter.side_effect = lambda *a, **kw: mock.Mock()
    mock_metrics.get_meter.return_value = mock_meter
    monkeypatch.setattr(_opentelemetry_metrics, "metrics", mock_metrics, raising=False)

    recorder = _opentelemetry_metrics._MetricsRecorder(
        enable_metrics=True, rpc_system="grpc"
    )
    disabled_recorder = _opentelemetry_metrics._MetricsRecorder(enable_metrics=False)

    # No-ops when recorder is None, disabled, or no active operation
    _opentelemetry_metrics.record_pending_retry(None)
    _opentelemetry_metrics.record_pending_retry(disabled_recorder)
    _opentelemetry_metrics.record_pending_retry(recorder)
    _opentelemetry_metrics.handle_unrecorded_retryable_failure(
        None, RuntimeError("e"), attempts_before=0, will_retry=True
    )
    _opentelemetry_metrics.handle_unrecorded_retryable_failure(
        disabled_recorder, RuntimeError("e"), attempts_before=0, will_retry=True
    )
    _opentelemetry_metrics.handle_unrecorded_retryable_failure(
        recorder, RuntimeError("e"), attempts_before=0, will_retry=True
    )

    # Standalone record_retry and record_ttfb outside start_operation without optional attrs
    recorder.record_retry(operation=None, error_type="UNAVAILABLE", network_path=None)
    _, retry_no_op_kw = recorder.retries_counter.add.call_args
    assert "gcp.storage.operation" not in retry_no_op_kw["attributes"]
    assert "network.path" not in retry_no_op_kw["attributes"]

    recorder.record_ttfb(0.02, operation=None, network_path=None)
    _, ttfb_no_op_kw = recorder.ttfb.record.call_args
    assert "gcp.storage.operation" not in ttfb_no_op_kw["attributes"]
    assert "network.path" not in ttfb_no_op_kw["attributes"]

    recorder.retries_counter.add.reset_mock()
    with _opentelemetry_metrics.start_operation(
        recorder,
        "storage.asyncio.AsyncMultiRangeDownloader.open",
        "ReadObject",
        rpc_method="google.storage.v2.Storage/BidiReadObject",
    ) as op_state:
        assert op_state is not None
        op_state.mark_attempt_failed("OK")
        op_state.mark_attempt_failed("")
        assert op_state.last_failure_error_type is None

        # Pending retry when no failure occurred is a no-op
        _opentelemetry_metrics.record_pending_retry(recorder)
        recorder.retries_counter.add.assert_not_called()

        # When transport already recorded the attempt, handle_unrecorded_retryable_failure skips
        op_state.recorded_attempts = 1
        _opentelemetry_metrics.handle_unrecorded_retryable_failure(
            recorder,
            api_exceptions.ServiceUnavailable("503"),
            attempts_before=0,
            will_retry=True,
            network_path="directpath",
        )
        assert op_state.recorded_attempts == 1
        assert op_state.last_failure_error_type is None

        # Unrecorded failure 1 (will_retry=True) -> marks failure, no retry yet
        _opentelemetry_metrics.handle_unrecorded_retryable_failure(
            recorder,
            api_exceptions.ServiceUnavailable("503"),
            attempts_before=1,
            will_retry=True,
            network_path="unknown",
        )
        assert op_state.recorded_attempts == 2
        assert op_state.last_failure_error_type == "UNAVAILABLE"
        recorder.retries_counter.add.assert_not_called()

        # Consecutive unrecorded failure 2 (will_retry=True) -> emits retry for failure 1, marks failure 2
        _opentelemetry_metrics.handle_unrecorded_retryable_failure(
            recorder,
            api_exceptions.DeadlineExceeded("timeout"),
            attempts_before=2,
            will_retry=True,
            network_path="cloudpath",
        )
        assert op_state.recorded_attempts == 3
        assert op_state.last_failure_error_type == "DEADLINE_EXCEEDED"
        recorder.retries_counter.add.assert_called_once()
        assert (
            recorder.retries_counter.add.call_args.kwargs["attributes"]["error.type"]
            == "UNAVAILABLE"
        )

        # Unrecorded terminal failure 3 (will_retry=False) -> emits retry for failure 2, leaves error cleared
        _opentelemetry_metrics.handle_unrecorded_retryable_failure(
            recorder,
            api_exceptions.PermissionDenied("403"),
            attempts_before=3,
            will_retry=False,
            network_path="cloudpath",
        )
        assert op_state.recorded_attempts == 4
        assert op_state.last_failure_error_type is None
        assert recorder.retries_counter.add.call_count == 2
        assert (
            recorder.retries_counter.add.call_args.kwargs["attributes"]["error.type"]
            == "DEADLINE_EXCEEDED"
        )

        # Mark failure and consume via record_pending_retry
        op_state.mark_attempt_failed("ABORTED")
        _opentelemetry_metrics.record_pending_retry(recorder, network_path="directpath")
        assert recorder.retries_counter.add.call_count == 3
        _, pending_kw = recorder.retries_counter.add.call_args
        assert pending_kw["attributes"]["gcp.storage.operation"] == "ReadObject"
        assert pending_kw["attributes"]["error.type"] == "ABORTED"
        assert pending_kw["attributes"]["network.path"] == "directpath"

        import contextvars

        copied_ctx = contextvars.copy_context()

    # Once start_operation exits, state.finished is True even in copied contexts
    assert op_state.finished is True
    assert copied_ctx.run(_opentelemetry_metrics.get_current_operation) is None
