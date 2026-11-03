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

"""Manages OpenTelemetry metrics instruments and gating for GCS client."""

import logging
import os
from typing import Any, Dict, Optional

from google.cloud.storage.version import __version__

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# 1. Hidden Development Gate
# ---------------------------------------------------------------------------
# Must remain False in production branches.
# Only enabled during active development and test runs.
_ENABLE_METRICS_DEV_GATE = False

# ---------------------------------------------------------------------------
# 2. Standardized Configuration and Environment Variable Names
# ---------------------------------------------------------------------------
ENABLE_OTEL_METRICS_ENV_VAR = "GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS"
ENABLE_OTEL_DEBUG_METRICS_ENV_VAR = "GCP_STORAGE_PYTHON_ENABLE_OTEL_DEBUG_METRICS"

_DEFAULT_ENABLE_METRICS = False
_DEFAULT_ENABLE_DEBUG_METRICS = False

# ---------------------------------------------------------------------------
# 3. Optional OpenTelemetry Dependency Check
# ---------------------------------------------------------------------------
try:
    from opentelemetry import metrics

    HAS_OPENTELEMETRY_METRICS = True
except ImportError:
    HAS_OPENTELEMETRY_METRICS = False
    logger.debug(
        "OpenTelemetry metrics package (opentelemetry-api >= 1.12.0) is not "
        "installed. GCS client metrics are disabled."
    )


_TRUTHY_ENV_VALUES = {"1", "true", "yes", "on"}
_FALSY_ENV_VALUES = {"0", "false", "no", "off"}


def _parse_bool_env(name: str, default: bool = False) -> bool:
    """Parses a boolean from an environment variable."""
    val = os.environ.get(name)
    if val is None:
        return default
    normalized = val.strip().lower()
    if not normalized:
        return default
    if normalized in _TRUTHY_ENV_VALUES:
        return True
    if normalized in _FALSY_ENV_VALUES:
        return False
    logger.warning(
        "Unrecognized boolean value %r for environment variable %s; using default %s.",
        val,
        name,
        default,
    )
    return default


def is_metrics_enabled(enable_metrics: Optional[bool] = None) -> bool:
    """Evaluates whether standard GCS metrics should be recorded.

    Args:
        enable_metrics: Optional boolean configured on the client instance.
            Takes precedence over the environment variable if specified.

    Returns:
        bool: True if metrics recording is enabled, False otherwise.
    """
    if enable_metrics is not None and not isinstance(enable_metrics, bool):
        raise TypeError("enable_metrics must be a boolean or None.")

    if not HAS_OPENTELEMETRY_METRICS:
        return False

    if not _ENABLE_METRICS_DEV_GATE:
        return False

    if enable_metrics is not None:
        return enable_metrics

    return _parse_bool_env(ENABLE_OTEL_METRICS_ENV_VAR, _DEFAULT_ENABLE_METRICS)


def is_debug_metrics_enabled(
    enable_debug_metrics: Optional[bool] = None,
) -> bool:
    """Evaluates whether high-frequency debug metrics should be recorded.

    Args:
        enable_debug_metrics: Optional boolean configured on the client
            instance. Takes precedence over the environment variable if
            specified.

    Returns:
        bool: True if debug metrics recording is enabled, False otherwise.
    """
    if enable_debug_metrics is not None and not isinstance(enable_debug_metrics, bool):
        raise TypeError("enable_debug_metrics must be a boolean or None.")

    if not HAS_OPENTELEMETRY_METRICS:
        return False

    if not _ENABLE_METRICS_DEV_GATE:
        return False

    if enable_debug_metrics is not None:
        return enable_debug_metrics

    return _parse_bool_env(
        ENABLE_OTEL_DEBUG_METRICS_ENV_VAR, _DEFAULT_ENABLE_DEBUG_METRICS
    )


# ---------------------------------------------------------------------------
# 4. Standard Common Attributes & Meter Provider
# ---------------------------------------------------------------------------
_COMMON_ATTRIBUTES: Dict[str, Any] = {
    "gcp.client.service": "storage",
    "gcp.client.version": __version__,
    "gcp.client.repo": "googleapis/google-cloud-python",
    "gcp.client.artifact": "google-cloud-storage",
}


def get_common_attributes() -> Dict[str, Any]:
    """Returns a copy of standard GCS client attributes for metrics."""
    return _COMMON_ATTRIBUTES.copy()


def get_meter(
    enable_metrics: Optional[bool] = None,
    enable_debug_metrics: Optional[bool] = None,
    meter_provider: Optional[Any] = None,
) -> Optional[Any]:
    """Returns the OpenTelemetry Meter for Google Cloud Storage.

    Args:
        enable_metrics: Optional boolean configured on the client instance for
            standard metrics.
        enable_debug_metrics: Optional boolean configured on the client
            instance for debug metrics.
        meter_provider: Optional custom OpenTelemetry MeterProvider instance.
            Defaults to the global MeterProvider if None.

    Returns:
        Optional[Any]: The OpenTelemetry Meter instance if standard or debug
            metrics are enabled, or None otherwise.
    """
    if not (
        is_metrics_enabled(enable_metrics)
        or is_debug_metrics_enabled(enable_debug_metrics)
    ):
        return None
    return metrics.get_meter(
        "google.cloud.storage",
        __version__,
        meter_provider=meter_provider,
    )
