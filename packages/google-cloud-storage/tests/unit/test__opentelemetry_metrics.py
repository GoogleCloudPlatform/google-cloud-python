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

import importlib
import sys
from unittest import mock

import pytest

from google.cloud.storage import _opentelemetry_metrics
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
    # Argument validation executes before the _ENABLE_METRICS_DEV_GATE check.
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
    assert attrs["gcp.client.service"] == "storage"
    assert attrs["gcp.client.version"] == __version__
    assert attrs["gcp.client.repo"] == "googleapis/google-cloud-python"
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
