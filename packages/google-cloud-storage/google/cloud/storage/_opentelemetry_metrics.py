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

import asyncio
import concurrent.futures
import contextlib
import http.client
import logging
import os
import re
import socket
import ssl
import time
from collections import deque
from contextvars import ContextVar
from dataclasses import dataclass, field
from typing import (
    Any,
    Deque,
    Dict,
    FrozenSet,
    Iterator,
    List,
    Optional,
    Set,
    Tuple,
)
from urllib.parse import urlsplit

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

DEFAULT_SERVER_ADDRESS = "storage.googleapis.com"

# ---------------------------------------------------------------------------
# 3. Standard Metric Instrument Names
# ---------------------------------------------------------------------------
METRIC_RPC_CLIENT_CALL_DURATION = "rpc.client.call.duration"
METRIC_HTTP_CLIENT_REQUEST_DURATION = "http.client.request.duration"
METRIC_GCP_CLIENT_REQUEST_DURATION = "gcp.client.request.duration"
METRIC_STORAGE_CLIENT_OPERATIONS = "gcp.storage.client.operations"
METRIC_STORAGE_CLIENT_ATTEMPTS = "gcp.storage.client.attempts"
METRIC_STORAGE_CLIENT_RETRIES = "gcp.storage.client.retries"
METRIC_STORAGE_REQUEST_BODY_SIZE = "gcp.storage.client.request.body.size"
METRIC_STORAGE_RESPONSE_BODY_SIZE = "gcp.storage.client.response.body.size"
METRIC_STORAGE_CLIENT_TTFB = "gcp.storage.client.ttfb"
METRIC_STORAGE_CLIENT_ERRORS = "gcp.storage.client.errors"

_LATENCY_METRIC_NAMES = (
    METRIC_RPC_CLIENT_CALL_DURATION,
    METRIC_HTTP_CLIENT_REQUEST_DURATION,
    METRIC_GCP_CLIENT_REQUEST_DURATION,
    METRIC_STORAGE_CLIENT_TTFB,
)

_SIZE_METRIC_NAMES = (
    METRIC_STORAGE_REQUEST_BODY_SIZE,
    METRIC_STORAGE_RESPONSE_BODY_SIZE,
)

# ---------------------------------------------------------------------------
# 4. Optional OpenTelemetry Dependency Check
# ---------------------------------------------------------------------------
try:
    from opentelemetry import metrics

    HAS_OPENTELEMETRY_METRICS = True
except ImportError:
    metrics = None  # type: ignore[assignment]
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
# 5. Standard Common Attributes & Meter Provider
# ---------------------------------------------------------------------------
_METER_NAME = "google.cloud.storage"

_COMMON_ATTRIBUTES: Dict[str, Any] = {
    "gcp.client.service": "storage",
    "gcp.client.version": __version__,
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
    if (
        not (
            is_metrics_enabled(enable_metrics)
            or is_debug_metrics_enabled(enable_debug_metrics)
        )
        or metrics is None
    ):
        return None
    return metrics.get_meter(
        _METER_NAME,
        __version__,
        meter_provider=meter_provider,
    )


# ---------------------------------------------------------------------------
# 6. Custom Histogram Bucket Boundaries & Views
# ---------------------------------------------------------------------------
def _build_latency_buckets() -> Tuple[float, ...]:
    """Builds the custom latency histogram bucket boundaries in seconds.

    Uses 2ms resolution for the first 50 buckets (0.000s to 0.098s), then starts
    at 0.100s with 10ms resolution and doubles the increment every 10 buckets
    while boundary < 300.0s.
    """
    boundaries: List[float] = []
    boundary = 0.0
    increment = 0.002

    for _ in range(50):
        boundaries.append(round(boundary, 6))
        boundary += increment

    increment = 0.010
    i = 0
    while boundary < 300.0:
        if i != 0 and i % 10 == 0:
            increment *= 2
        boundaries.append(round(boundary, 6))
        boundary += increment
        i += 1

    return tuple(boundaries)


def _build_size_buckets() -> Tuple[int, ...]:
    """Builds the custom byte-size histogram bucket boundaries in bytes.

    Uses 128 KiB increments up to 4 MiB, then doubles the increment on each
    subsequent bucket while ``boundary <= 16 GiB`` (48 total buckets, matching
    Go and Java SDKs).
    """
    kb = 1024
    mb = 1024 * kb
    gb = 1024 * mb

    boundaries: List[int] = []
    boundary = 0
    increment = 128 * kb

    while boundary <= 16 * gb:
        boundaries.append(boundary)
        boundary += increment
        if boundary >= 4 * mb:
            increment *= 2

    return tuple(boundaries)


LATENCY_HISTOGRAM_BOUNDARIES: Tuple[float, ...] = _build_latency_buckets()
SIZE_HISTOGRAM_BOUNDARIES: Tuple[int, ...] = _build_size_buckets()


def get_histogram_views() -> List[Any]:
    """Returns OpenTelemetry SDK Views for custom latency and size histograms.

    If ``opentelemetry-sdk`` is not installed, returns an empty list.
    """
    try:
        from opentelemetry.sdk.metrics.view import (
            ExplicitBucketHistogramAggregation,
            View,
        )
    except ImportError:
        return []

    views: List[Any] = []
    for name in _LATENCY_METRIC_NAMES:
        views.append(
            View(
                instrument_name=name,
                meter_name=_METER_NAME,
                aggregation=ExplicitBucketHistogramAggregation(
                    boundaries=LATENCY_HISTOGRAM_BOUNDARIES
                ),
            )
        )
    for name in _SIZE_METRIC_NAMES:
        views.append(
            View(
                instrument_name=name,
                meter_name=_METER_NAME,
                aggregation=ExplicitBucketHistogramAggregation(
                    boundaries=SIZE_HISTOGRAM_BOUNDARIES
                ),
            )
        )
    return views


# ---------------------------------------------------------------------------
# 7. Canonical Error Classification (`error.type`)
# ---------------------------------------------------------------------------
_HTTP_STATUS_TO_ERROR_TYPE: Dict[int, str] = {
    400: "INVALID_ARGUMENT",
    401: "UNAUTHENTICATED",
    403: "PERMISSION_DENIED",
    404: "NOT_FOUND",
    408: "DEADLINE_EXCEEDED",
    409: "ABORTED",
    412: "FAILED_PRECONDITION",
    416: "OUT_OF_RANGE",
    429: "RESOURCE_EXHAUSTED",
    499: "CANCELLED",
    500: "INTERNAL",
    501: "UNIMPLEMENTED",
    503: "UNAVAILABLE",
    504: "DEADLINE_EXCEEDED",
}


def _is_valid_status_code(val: Any) -> bool:
    """Returns True if ``val`` is a valid HTTP error status code (int in 400..599)."""
    return isinstance(val, int) and not isinstance(val, bool) and 400 <= val < 600


def _iter_exception_chain(exc: BaseException) -> Iterator[BaseException]:
    """Yields ``exc`` and any nested causes, contexts, reasons, or exception args."""
    visited: Set[int] = {id(exc)}
    queue: Deque[BaseException] = deque([exc])
    while queue:
        current = queue.popleft()
        yield current

        for attr_name in (
            "__cause__",
            "__context__",
            "cause",
            "reason",
            "original_exception",
        ):
            nested = getattr(current, attr_name, None)
            if isinstance(nested, BaseException) and id(nested) not in visited:
                visited.add(id(nested))
                queue.append(nested)

        for seq_attr in ("args", "errors"):
            seq = getattr(current, seq_attr, ())
            if isinstance(seq, (tuple, list)):
                for item in seq:
                    if isinstance(item, BaseException) and id(item) not in visited:
                        visited.add(id(item))
                        queue.append(item)


def _is_subclass_by_module(
    cls: type, module_prefix: str, class_names: Set[str]
) -> bool:
    """Checks whether ``cls`` or any of its base classes match module/name criteria."""
    mro = getattr(cls, "__mro__", None)
    if isinstance(mro, tuple):
        for base in mro:
            mod = getattr(base, "__module__", "") or ""
            if mod == module_prefix or mod.startswith(module_prefix + "."):
                if getattr(base, "__name__", None) in class_names:
                    return True
    return False


def classify_error_type(
    exc: Optional[BaseException] = None,
    status_code: Optional[int] = None,
) -> str:
    """Maps an exception or HTTP status code to a low-cardinality ``error.type``.

    Args:
        exc: Optional exception raised during an operation or transport attempt.
        status_code: Optional HTTP status code from the response.

    Returns:
        str: Canonical low-cardinality error classification string.
    """
    valid_status = _is_valid_status_code(status_code)
    if exc is None:
        if not valid_status or status_code is None:
            return "OK"
        return _HTTP_STATUS_TO_ERROR_TYPE.get(status_code, str(status_code))

    chain = list(_iter_exception_chain(exc))

    # 1. Checksum Mismatch (DataCorruption)
    for item in chain:
        if _is_subclass_by_module(
            item.__class__, "google.cloud.storage", {"DataCorruption"}
        ) or _is_subclass_by_module(
            item.__class__, "google.resumable_media", {"DataCorruption"}
        ):
            return "CHECKSUM_MISMATCH"

    # 2. Authentication / Credentials Failure (google.auth.exceptions)
    for item in chain:
        if _is_subclass_by_module(
            item.__class__,
            "google.auth.exceptions",
            {
                "RefreshError",
                "TransportError",
                "DefaultCredentialsError",
                "GoogleAuthError",
            },
        ):
            return "AUTHENTICATION_ERROR"

    # 3. Cancellation
    for item in chain:
        if isinstance(
            item, (asyncio.CancelledError, concurrent.futures.CancelledError)
        ):
            return "CANCELLED"

    # 4. HTTP response status code on exception (checked before grpc_status_code so
    # HTTP 409 Conflict consistently maps to ABORTED across HTTP and Veneer metrics)
    for item in chain:
        resp = getattr(item, "response", None)
        resp_status = getattr(resp, "status_code", None)
        if _is_valid_status_code(resp_status):
            return _HTTP_STATUS_TO_ERROR_TYPE.get(resp_status, str(resp_status))

        if item.__class__.__name__ == "Conflict" and _is_subclass_by_module(
            item.__class__, "google.api_core.exceptions", {"Conflict"}
        ):
            return _HTTP_STATUS_TO_ERROR_TYPE[409]

    # 5. gRPC / GoogleAPICallError status code
    for item in chain:
        grpc_code = getattr(item, "grpc_status_code", None)
        if grpc_code is not None:
            name = getattr(grpc_code, "name", None)
            if name:
                return str(name)
            return str(grpc_code)

        # Direct grpc.RpcError (has callable .code())
        code_attr = getattr(item, "code", None)
        if callable(code_attr):
            try:
                rpc_status = code_attr()
                name = getattr(rpc_status, "name", None)
                if isinstance(name, str) and name:
                    return name
            except Exception:  # pragma: NO COVER
                pass

        if _is_valid_status_code(code_attr):
            return _HTTP_STATUS_TO_ERROR_TYPE.get(code_attr, str(code_attr))

    # 6. TLS / SSL Failure
    for item in chain:
        if (
            isinstance(item, ssl.SSLError)
            or _is_subclass_by_module(
                item.__class__,
                "requests.exceptions",
                {"SSLError"},
            )
            or _is_subclass_by_module(
                item.__class__,
                "urllib3.exceptions",
                {"SSLError"},
            )
        ):
            return "TLS_FAILURE"

    # 7. Specific Socket / Network Failures (DNS, Connection Refused, Connection Reset)
    for item in chain:
        if isinstance(item, socket.gaierror) or _is_subclass_by_module(
            item.__class__,
            "urllib3.exceptions",
            {"NameResolutionError"},
        ):
            return "DNS_FAILURE"
        if isinstance(item, (ConnectionRefusedError, ConnectionResetError)):
            return "CONNECTION_ERROR"

    # 8. Timeouts (Note: urllib3.exceptions.NewConnectionError subclasses ConnectTimeoutError
    # even for non-timeout connection failures, so exclude NewConnectionError here.)
    for item in chain:
        if item.__class__.__name__ != "NewConnectionError":
            if isinstance(
                item,
                (
                    socket.timeout,
                    TimeoutError,
                    asyncio.TimeoutError,
                    concurrent.futures.TimeoutError,
                ),
            ):
                return "TIMEOUT"
            if _is_subclass_by_module(
                item.__class__,
                "requests.exceptions",
                {"Timeout", "ConnectTimeout", "ReadTimeout"},
            ) or _is_subclass_by_module(
                item.__class__,
                "urllib3.exceptions",
                {"TimeoutError", "ReadTimeoutError", "ConnectTimeoutError"},
            ):
                return "TIMEOUT"

    # 9. Generic Connection / Network Transport Failure
    for item in chain:
        if (
            _is_subclass_by_module(
                item.__class__,
                "requests.exceptions",
                {"ConnectionError", "ChunkedEncodingError", "RequestException"},
            )
            or _is_subclass_by_module(
                item.__class__,
                "urllib3.exceptions",
                {"HTTPError"},
            )
            or isinstance(item, (OSError, http.client.HTTPException))
        ):
            return "CONNECTION_ERROR"

    # 10. Explicit HTTP status_code fallback
    if valid_status and status_code is not None:
        return _HTTP_STATUS_TO_ERROR_TYPE.get(status_code, str(status_code))

    # 11. Client Validation Errors
    for item in chain:
        if (
            isinstance(item, (ValueError, TypeError))
            or _is_subclass_by_module(
                item.__class__, "google.cloud.storage", {"InvalidResponse"}
            )
            or _is_subclass_by_module(
                item.__class__, "google.resumable_media", {"InvalidResponse"}
            )
        ):
            return "CLIENT_VALIDATION_ERROR"

    return "UNKNOWN"


# ---------------------------------------------------------------------------
# 8. HTTP `url.template` Route Normalization
# ---------------------------------------------------------------------------
_URL_TEMPLATE_PATTERNS: Tuple[Tuple[re.Pattern[str], str], ...] = (
    (
        re.compile(r"^/storage/v1/b/[^/]+/o/[^/]+/rewriteTo/b/[^/]+/o/.+$"),
        "/storage/v1/b/{bucket}/o/{object}/rewriteTo/b/{bucket}/o/{object}",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/o/[^/]+/copyTo/b/[^/]+/o/.+$"),
        "/storage/v1/b/{bucket}/o/{object}/copyTo/b/{bucket}/o/{object}",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/o/[^/]+/moveTo/o/.+$"),
        "/storage/v1/b/{bucket}/o/{object}/moveTo/o/{object}",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/o/[^/]+/compose$"),
        "/storage/v1/b/{bucket}/o/{object}/compose",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/o/[^/]+/restore$"),
        "/storage/v1/b/{bucket}/o/{object}/restore",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/o/[^/]+/acl/[^/]+$"),
        "/storage/v1/b/{bucket}/o/{object}/acl/{entity}",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/o/[^/]+/acl$"),
        "/storage/v1/b/{bucket}/o/{object}/acl",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/o/[^/]+/iam(?:/.*)?$"),
        "/storage/v1/b/{bucket}/o/{object}/iam",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/o/.+$"),
        "/storage/v1/b/{bucket}/o/{object}",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/o$"),
        "/storage/v1/b/{bucket}/o",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/acl/[^/]+$"),
        "/storage/v1/b/{bucket}/acl/{entity}",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/acl$"),
        "/storage/v1/b/{bucket}/acl",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/defaultObjectAcl/[^/]+$"),
        "/storage/v1/b/{bucket}/defaultObjectAcl/{entity}",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/defaultObjectAcl$"),
        "/storage/v1/b/{bucket}/defaultObjectAcl",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/iam(?:/.*)?$"),
        "/storage/v1/b/{bucket}/iam",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/notificationConfigs/[^/]+$"),
        "/storage/v1/b/{bucket}/notificationConfigs/{notification}",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/notificationConfigs$"),
        "/storage/v1/b/{bucket}/notificationConfigs",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/lockRetentionPolicy$"),
        "/storage/v1/b/{bucket}/lockRetentionPolicy",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+/restore$"),
        "/storage/v1/b/{bucket}/restore",
    ),
    (
        re.compile(r"^/storage/v1/b/[^/]+$"),
        "/storage/v1/b/{bucket}",
    ),
    (
        re.compile(r"^/storage/v1/b$"),
        "/storage/v1/b",
    ),
    (
        re.compile(r"^/storage/v1/projects/[^/]+/serviceAccount$"),
        "/storage/v1/projects/{project}/serviceAccount",
    ),
    (
        re.compile(r"^/storage/v1/projects/[^/]+/hmacKeys/[^/]+$"),
        "/storage/v1/projects/{project}/hmacKeys/{access_id}",
    ),
    (
        re.compile(r"^/storage/v1/projects/[^/]+/hmacKeys$"),
        "/storage/v1/projects/{project}/hmacKeys",
    ),
    (
        re.compile(r"^/upload/storage/v1/b/[^/]+/o(?:/[^/]+)?$"),
        "/upload/storage/v1/b/{bucket}/o",
    ),
    (
        re.compile(r"^/download/storage/v1/b/[^/]+/o/.+$"),
        "/download/storage/v1/b/{bucket}/o/{object}",
    ),
    (
        re.compile(r"^/batch/storage/v1$"),
        "/batch/storage/v1",
    ),
)

_XML_MPU_RESERVED_PREFIXES = {"storage", "upload", "download", "batch", "b", "projects"}
_XML_MPU_QUERY_KEYS = {"uploads", "uploadId", "partNumber"}
_XML_MULTI_SEGMENT_RE = re.compile(r"^/([^/]+)/(.+)$")


def normalize_url_template(url_or_path: Optional[str]) -> str:
    """Normalizes a raw HTTP URL or path into a bounded ``url.template`` string.

    Bucket names, object keys, project IDs, and query strings are stripped to
    prevent cardinality explosion. Unrecognized paths fall back to ``"UNKNOWN"``.

    Args:
        url_or_path: Full request URL or path string.

    Returns:
        str: Low-cardinality ``url.template`` value.
    """
    if not url_or_path or not isinstance(url_or_path, str):
        return "UNKNOWN"

    try:
        parsed = urlsplit(url_or_path)
    except ValueError:
        return "UNKNOWN"
    path = parsed.path or ""
    query = parsed.query or ""

    path = "/" + path.strip("/")
    if path == "/":
        return "UNKNOWN"

    # Normalize relative paths passed to Connection.api_request before /storage/v1 prefixing
    if path == "/b" or path.startswith(("/b/", "/projects/")):
        path = "/storage/v1" + path

    for pattern, template in _URL_TEMPLATE_PATTERNS:
        if pattern.match(path):
            return template

    # XML API Multipart Upload routes: /{bucket}/{object} with XML MPU query params
    if query:
        query_keys = {param.partition("=")[0] for param in query.split("&") if param}
        if query_keys & _XML_MPU_QUERY_KEYS:
            match_multi = _XML_MULTI_SEGMENT_RE.match(path)
            if match_multi and match_multi.group(1) not in _XML_MPU_RESERVED_PREFIXES:
                return "/{bucket}/{object}"

    return "UNKNOWN"


# ---------------------------------------------------------------------------
# 9. Logical Operation Normalization, Context & Suppression (`ContextVar`)
# ---------------------------------------------------------------------------
_GRPC_LOGICAL_OPERATION_OVERRIDES: Dict[str, str] = {
    "BidiReadObject": "ReadObject",
    "BidiWriteObject": "WriteObject",
}

_RPC_V2_METHODS: FrozenSet[str] = frozenset(
    {
        "BidiReadObject",
        "BidiWriteObject",
        "CancelResumableWrite",
        "ComposeObject",
        "CreateBucket",
        "DeleteBucket",
        "DeleteObject",
        "GetBucket",
        "GetIamPolicy",
        "GetObject",
        "ListBuckets",
        "ListObjects",
        "LockBucketRetentionPolicy",
        "MoveObject",
        "QueryWriteStatus",
        "ReadObject",
        "RestoreObject",
        "RewriteObject",
        "SetIamPolicy",
        "StartResumableWrite",
        "TestIamPermissions",
        "UpdateBucket",
        "UpdateObject",
        "WriteObject",
    }
)


def normalize_logical_operation(operation: Optional[str]) -> str:
    """Normalizes an RPC path or method name into a short logical ``gcp.storage.operation``."""
    if not operation or not isinstance(operation, str):
        return "UNKNOWN"
    cleaned = operation.strip().strip("/")
    if not cleaned:
        return "UNKNOWN"
    short_name = cleaned.rsplit("/", 1)[-1] if "/" in cleaned else cleaned
    return _GRPC_LOGICAL_OPERATION_OVERRIDES.get(short_name, short_name)


def resolve_rpc_method(
    operation: Optional[str], rpc_method: Optional[str] = None
) -> str:
    """Resolves the full RPC path (e.g. ``google.storage.v2.Storage/ReadObject``) for ``rpc.method``."""
    raw = rpc_method if (rpc_method and isinstance(rpc_method, str)) else operation
    if not raw or not isinstance(raw, str):
        return "UNKNOWN"
    cleaned = raw.strip().strip("/")
    if not cleaned or cleaned == "UNKNOWN":
        return "UNKNOWN"
    if "/" in cleaned:
        return cleaned
    if cleaned in _RPC_V2_METHODS:
        return f"google.storage.v2.Storage/{cleaned}"
    if "." in cleaned:
        return cleaned
    return f"google.storage.v1.Storage/{cleaned}"


@dataclass
class _OperationState:
    """Represents the active logical GCS Veneer operation in the current context."""

    client_method: str
    operation: str
    rpc_method: str
    suppressed: bool = False
    start_time: float = field(default_factory=time.perf_counter)
    finished: bool = False
    last_failure_error_type: Optional[str] = None
    recorded_attempts: int = 0

    def mark_attempt_failed(self, error_type: str) -> None:
        """Records the error type of a failed attempt for a subsequent retry."""
        if error_type and error_type != "OK":
            self.last_failure_error_type = error_type

    def consume_retry_error(self) -> Optional[str]:
        """Consumes and returns the prior failed attempt's error type, if any."""
        prior = self.last_failure_error_type
        self.last_failure_error_type = None
        return prior


_OP_STATE: ContextVar[Optional[_OperationState]] = ContextVar(
    "_gcs_otel_op_state", default=None
)


def get_current_operation() -> Optional[_OperationState]:
    """Returns the current logical `_OperationState` in this execution context, if any."""
    op = _OP_STATE.get()
    if op is not None and op.finished:
        return None
    return op


@contextlib.contextmanager
def start_operation(
    recorder: Optional["_MetricsRecorder"],
    client_method: str,
    operation: str,
    suppress: bool = False,
    rpc_method: Optional[str] = None,
) -> Iterator[Optional[_OperationState]]:
    """Context manager tracking a logical user-facing GCS operation.

    If a parent logical operation is already active in the current context,
    nested calls become a no-op so only the outermost user-invoked method
    emits ``gcp.client.request.duration`` and ``gcp.storage.client.operations``.

    Args:
        recorder: Optional `_MetricsRecorder` configured on the client.
        client_method: Fully qualified Python method name
            (e.g. ``"storage.Blob.download_to_filename"``).
        operation: Short logical GCS operation name
            (e.g. ``"ReadObject"``, ``"GetObject"``).
        suppress: If True, suppresses logical operation and payload size
            emission for this context and any nested calls (used by
            ``transfer_manager`` workers and ``BlobReader`` prefetches).
        rpc_method: Optional full RPC path
            (e.g. ``"google.storage.v2.Storage/BidiReadObject"``). If omitted,
            inferred from ``operation``.
    """
    existing = get_current_operation()
    if existing is not None:
        if suppress and not existing.suppressed:
            suppressed_child = _OperationState(
                client_method=existing.client_method,
                operation=existing.operation,
                rpc_method=existing.rpc_method,
                suppressed=True,
                start_time=existing.start_time,
            )
            child_token = _OP_STATE.set(suppressed_child)
            try:
                yield suppressed_child
            finally:
                suppressed_child.finished = True
                _OP_STATE.reset(child_token)
        else:
            yield existing
        return

    recorder_active = (
        recorder is not None and getattr(recorder, "standard_enabled", False) is True
    )
    if not recorder_active and not suppress:
        yield None
        return

    resolved_operation = normalize_logical_operation(operation)
    resolved_rpc_method = resolve_rpc_method(
        resolved_operation, rpc_method=rpc_method or operation
    )
    start_time = time.perf_counter()
    state = _OperationState(
        client_method=client_method,
        operation=resolved_operation,
        rpc_method=resolved_rpc_method,
        suppressed=suppress,
        start_time=start_time,
    )
    token = _OP_STATE.set(state)
    error_type = "OK"
    try:
        yield state
    except BaseException as exc:
        error_type = classify_error_type(exc)
        raise
    finally:
        state.finished = True
        duration = max(0.0, time.perf_counter() - start_time)
        _OP_STATE.reset(token)
        if recorder_active and not suppress and recorder is not None:
            recorder.record_logical_operation(
                duration=duration,
                client_method=client_method,
                operation=resolved_operation,
                error_type=error_type,
                rpc_method=resolved_rpc_method,
            )


def record_pending_retry(
    recorder: Optional["_MetricsRecorder"],
    operation: Optional[str] = None,
    network_path: Optional[str] = None,
) -> None:
    """Emits a pending ``gcp.storage.client.retries`` increment if a prior attempt failed."""
    if recorder is None or not getattr(recorder, "standard_enabled", False):
        return
    current_op = get_current_operation()
    if current_op is None:
        return
    prior_error = current_op.consume_retry_error()
    if prior_error is not None:
        recorder.record_retry(
            operation=operation or current_op.operation,
            error_type=prior_error,
            network_path=network_path,
        )


def handle_unrecorded_retryable_failure(
    recorder: Optional["_MetricsRecorder"],
    exc: BaseException,
    attempts_before: int,
    will_retry: bool,
    network_path: Optional[str] = None,
) -> None:
    """Tracks retry state when a failed attempt bypassed transport-level attempt recording."""
    if recorder is None or not getattr(recorder, "standard_enabled", False):
        return
    current_op = get_current_operation()
    if current_op is None:
        return
    if current_op.recorded_attempts > attempts_before:
        return
    current_op.recorded_attempts += 1
    prior_error = current_op.consume_retry_error()
    if prior_error is not None:
        recorder.record_retry(
            operation=current_op.operation,
            error_type=prior_error,
            network_path=network_path,
        )
    if will_retry:
        current_op.mark_attempt_failed(classify_error_type(exc))


def get_active_recorder(obj: Any) -> Optional["_MetricsRecorder"]:
    """Returns ``obj._metrics_recorder`` if it is an active ``_MetricsRecorder``."""
    recorder = getattr(obj, "_metrics_recorder", None)
    if recorder is not None and getattr(recorder, "standard_enabled", False) is True:
        return recorder
    return None


# ---------------------------------------------------------------------------
# 10. Server Address Parsing & `_MetricsRecorder`
# ---------------------------------------------------------------------------
def _extract_server_address(api_endpoint: Optional[str]) -> str:
    """Extracts the low-cardinality hostname from ``api_endpoint``."""
    if not api_endpoint or not isinstance(api_endpoint, str):
        return DEFAULT_SERVER_ADDRESS
    endpoint = api_endpoint.strip()
    if not endpoint:
        return DEFAULT_SERVER_ADDRESS
    for grpc_prefix in (
        "dns:",
        "google-c2p:",
        "google-c2p-experimental:",
        "xds:",
        "ipv4:",
        "ipv6:",
    ):
        if endpoint.startswith(grpc_prefix):
            remainder = endpoint[len(grpc_prefix) :]
            if remainder.startswith("//"):
                remainder = remainder[2:]
                remainder = (
                    remainder.split("/", 1)[1] if "/" in remainder else remainder
                )
            endpoint = remainder.lstrip("/")
            break
    if "://" not in endpoint:
        endpoint = "https://" + endpoint.lstrip("/")
    try:
        parsed = urlsplit(endpoint)
        return parsed.hostname or DEFAULT_SERVER_ADDRESS
    except ValueError:
        return DEFAULT_SERVER_ADDRESS


class _MetricsRecorder:
    """Holds OpenTelemetry metric instruments and records standard GCS metrics."""

    def __init__(
        self,
        enable_metrics: Optional[bool] = None,
        enable_debug_metrics: Optional[bool] = None,
        meter_provider: Optional[Any] = None,
        api_endpoint: Optional[str] = None,
        rpc_system: str = "http",
    ) -> None:
        self.standard_enabled: bool = is_metrics_enabled(enable_metrics)
        self.debug_enabled: bool = is_debug_metrics_enabled(enable_debug_metrics)
        self.enabled: bool = self.standard_enabled or self.debug_enabled
        self._meter_provider: Optional[Any] = meter_provider
        self.rpc_system: str = rpc_system
        self.server_address: str = _extract_server_address(api_endpoint)
        self.meter: Optional[Any] = get_meter(
            enable_metrics=enable_metrics,
            enable_debug_metrics=enable_debug_metrics,
            meter_provider=meter_provider,
        )

        self._base_attributes: Dict[str, Any] = {
            **_COMMON_ATTRIBUTES,
            "server.address": self.server_address,
            "rpc.system.name": self.rpc_system,
        }

        if self.standard_enabled and self.meter is not None:
            self.rpc_call_duration = self.meter.create_histogram(
                METRIC_RPC_CLIENT_CALL_DURATION,
                unit="s",
                description="Duration of an individual gRPC attempt in seconds (excluding retries).",
            )
            self.http_request_duration = self.meter.create_histogram(
                METRIC_HTTP_CLIENT_REQUEST_DURATION,
                unit="s",
                description="Duration of an individual HTTP request attempt in seconds (excluding retries).",
            )
            self.client_request_duration = self.meter.create_histogram(
                METRIC_GCP_CLIENT_REQUEST_DURATION,
                unit="s",
                description="End-to-end latency of a logical user-facing Veneer operation in seconds.",
            )
            self.operations_counter = self.meter.create_counter(
                METRIC_STORAGE_CLIENT_OPERATIONS,
                unit="{operation}",
                description="Number of logical GCS client operations.",
            )
            self.attempts_counter = self.meter.create_counter(
                METRIC_STORAGE_CLIENT_ATTEMPTS,
                unit="{attempt}",
                description="Number of physical network transport attempts executed.",
            )
            self.retries_counter = self.meter.create_counter(
                METRIC_STORAGE_CLIENT_RETRIES,
                unit="{retry}",
                description="Number of transport retries executed after a failed attempt.",
            )
            self.request_body_size = self.meter.create_histogram(
                METRIC_STORAGE_REQUEST_BODY_SIZE,
                unit="By",
                description="Application payload bytes submitted by the caller for an upload or write operation.",
            )
            self.response_body_size = self.meter.create_histogram(
                METRIC_STORAGE_RESPONSE_BODY_SIZE,
                unit="By",
                description="Application payload bytes delivered to the caller.",
            )
            self.ttfb = self.meter.create_histogram(
                METRIC_STORAGE_CLIENT_TTFB,
                unit="s",
                description="Time elapsed from attempt initiation to receipt of the first response byte.",
            )
            self.operation_ttfb = self.ttfb
            self.errors_counter = self.meter.create_counter(
                METRIC_STORAGE_CLIENT_ERRORS,
                unit="{error}",
                description="Number of physical network transport attempts terminating with a non-OK status.",
            )
        else:
            self.rpc_call_duration = None
            self.http_request_duration = None
            self.client_request_duration = None
            self.operations_counter = None
            self.attempts_counter = None
            self.retries_counter = None
            self.request_body_size = None
            self.response_body_size = None
            self.ttfb = None
            self.operation_ttfb = None
            self.errors_counter = None

    def get_base_attributes(self) -> Dict[str, Any]:
        """Returns a copy of the base attributes for this recorder instance."""
        return self._base_attributes.copy()

    def _build_operation_attributes(
        self,
        operation: Optional[str] = None,
        client_method: Optional[str] = None,
        current_op: Optional[_OperationState] = None,
    ) -> Dict[str, Any]:
        """Builds base attributes enriched with current or explicit operation metadata."""
        attrs = self._base_attributes.copy()
        if current_op is None:
            current_op = get_current_operation()
        raw_op = operation or (current_op.operation if current_op else None)
        resolved_method = client_method or (
            current_op.client_method if current_op else None
        )
        if raw_op is not None:
            attrs["gcp.storage.operation"] = normalize_logical_operation(raw_op)
        if resolved_method is not None:
            attrs["gcp.client.method"] = resolved_method
        return attrs

    def record_logical_operation(
        self,
        duration: float,
        client_method: str,
        operation: str,
        error_type: str = "OK",
        rpc_method: Optional[str] = None,
    ) -> None:
        """Records end-to-end logical operation duration and count."""
        if not self.standard_enabled or self.meter is None:
            return
        logical_op = normalize_logical_operation(operation)
        full_rpc_method = resolve_rpc_method(
            logical_op, rpc_method=rpc_method or operation
        )
        op_attrs = {
            **self._base_attributes,
            "gcp.storage.operation": logical_op,
            "gcp.client.method": client_method,
            "error.type": error_type,
        }
        duration_attrs = {
            **op_attrs,
            "rpc.method": full_rpc_method,
        }
        self.client_request_duration.record(
            max(0.0, duration), attributes=duration_attrs
        )
        self.operations_counter.add(1, attributes=op_attrs)

    def record_retry(
        self,
        operation: Optional[str] = None,
        error_type: str = "UNKNOWN",
        network_path: Optional[str] = None,
    ) -> None:
        """Records a transport retry attempt with the prior failed attempt's error type."""
        if not self.standard_enabled or self.meter is None:
            return
        current_op = get_current_operation()
        raw_op = operation or (current_op.operation if current_op else None)
        retry_attrs: Dict[str, Any] = {
            **self._base_attributes,
            "error.type": error_type,
        }
        if raw_op is not None:
            retry_attrs["gcp.storage.operation"] = normalize_logical_operation(raw_op)
        if network_path is not None:
            retry_attrs["network.path"] = network_path
        self.retries_counter.add(1, attributes=retry_attrs)

    def record_http_attempt(
        self,
        duration: float,
        http_method: str,
        url_template: str,
        status_code: Optional[int] = None,
        error_type: str = "OK",
        operation: Optional[str] = None,
        client_method: Optional[str] = None,
        network_path: Optional[str] = None,
    ) -> None:
        """Records a single physical HTTP request attempt."""
        if not self.standard_enabled or self.meter is None:
            return
        del client_method
        current_op = get_current_operation()
        raw_op = operation or (current_op.operation if current_op else None)
        resolved_op = (
            normalize_logical_operation(raw_op) if raw_op is not None else None
        )
        if current_op is not None:
            current_op.recorded_attempts += 1
            prior_error = current_op.consume_retry_error()
            if prior_error is not None:
                self.record_retry(
                    operation=resolved_op,
                    error_type=prior_error,
                    network_path=network_path,
                )
            if error_type != "OK":
                current_op.mark_attempt_failed(error_type)

        valid_code = (
            isinstance(status_code, int)
            and not isinstance(status_code, bool)
            and 100 <= status_code < 600
        )

        # 1. http.client.request.duration attributes
        http_attrs: Dict[str, Any] = {
            **self._base_attributes,
            "http.request.method": http_method.upper() if http_method else "UNKNOWN",
            "url.template": url_template,
            "error.type": error_type,
        }
        if valid_code:
            http_attrs["http.response.status_code"] = status_code
        if network_path is not None:
            http_attrs["network.path"] = network_path

        # 2. gcp.storage.client.attempts attributes
        attempt_attrs: Dict[str, Any] = {
            **self._base_attributes,
            "error.type": error_type,
        }
        if resolved_op is not None:
            attempt_attrs["gcp.storage.operation"] = resolved_op
        if valid_code:
            attempt_attrs["http.response.status_code"] = status_code
        if network_path is not None:
            attempt_attrs["network.path"] = network_path

        self.http_request_duration.record(max(0.0, duration), attributes=http_attrs)
        self.attempts_counter.add(1, attributes=attempt_attrs)

        # 3. gcp.storage.client.errors attributes
        if error_type != "OK":
            error_attrs: Dict[str, Any] = {
                **self._base_attributes,
                "error.type": error_type,
            }
            if resolved_op is not None:
                error_attrs["gcp.storage.operation"] = resolved_op
            if network_path is not None:
                error_attrs["network.path"] = network_path
            self.errors_counter.add(1, attributes=error_attrs)

    def record_rpc_attempt(
        self,
        duration: float,
        operation: Optional[str] = None,
        status_code: Optional[str] = None,
        error_type: str = "OK",
        rpc_method: Optional[str] = None,
        network_path: Optional[str] = None,
        op_state: Optional[_OperationState] = None,
    ) -> None:
        """Records a single physical gRPC call attempt."""
        if not self.standard_enabled or self.meter is None:
            return
        active_op = op_state if op_state is not None else get_current_operation()
        raw_rpc = (
            rpc_method or operation or (active_op.rpc_method if active_op else None)
        )
        resolved_rpc_method = resolve_rpc_method(operation, rpc_method=raw_rpc)
        raw_op = operation or rpc_method or (active_op.operation if active_op else None)
        resolved_op = normalize_logical_operation(raw_op)

        if active_op is not None:
            active_op.recorded_attempts += 1
            prior_error = active_op.consume_retry_error()
            if prior_error is not None:
                self.record_retry(
                    operation=resolved_op,
                    error_type=prior_error,
                    network_path=network_path,
                )
            if error_type != "OK":
                active_op.mark_attempt_failed(error_type)

        # 1. rpc.client.call.duration attributes
        rpc_attrs: Dict[str, Any] = {
            **self._base_attributes,
            "rpc.method": resolved_rpc_method,
            "error.type": error_type,
        }
        if status_code is not None:
            rpc_attrs["rpc.response.status_code"] = status_code
        if network_path is not None:
            rpc_attrs["network.path"] = network_path

        # 2. gcp.storage.client.attempts attributes
        attempt_attrs: Dict[str, Any] = {
            **self._base_attributes,
            "gcp.storage.operation": resolved_op,
            "error.type": error_type,
        }
        if status_code is not None:
            attempt_attrs["rpc.response.status_code"] = status_code
        if network_path is not None:
            attempt_attrs["network.path"] = network_path

        self.rpc_call_duration.record(max(0.0, duration), attributes=rpc_attrs)
        self.attempts_counter.add(1, attributes=attempt_attrs)

        # 3. gcp.storage.client.errors attributes
        if error_type != "OK":
            error_attrs: Dict[str, Any] = {
                **self._base_attributes,
                "gcp.storage.operation": resolved_op,
                "error.type": error_type,
            }
            if network_path is not None:
                error_attrs["network.path"] = network_path
            self.errors_counter.add(1, attributes=error_attrs)

    def record_request_body_size(
        self,
        size: int,
        operation: Optional[str] = None,
        client_method: Optional[str] = None,
    ) -> None:
        """Records the payload byte size of an upload or write operation."""
        if not self.standard_enabled or self.meter is None:
            return
        if not isinstance(size, int) or isinstance(size, bool):
            return
        current_op = get_current_operation()
        if current_op is not None and current_op.suppressed:
            return
        attrs = self._build_operation_attributes(
            operation=operation, client_method=client_method, current_op=current_op
        )
        self.request_body_size.record(max(0, size), attributes=attrs)

    def record_response_body_size(
        self,
        size: int,
        operation: Optional[str] = None,
        client_method: Optional[str] = None,
    ) -> None:
        """Records the payload byte size of a download or read operation."""
        if not self.standard_enabled or self.meter is None:
            return
        if not isinstance(size, int) or isinstance(size, bool):
            return
        current_op = get_current_operation()
        if current_op is not None and current_op.suppressed:
            return
        attrs = self._build_operation_attributes(
            operation=operation, client_method=client_method, current_op=current_op
        )
        self.response_body_size.record(max(0, size), attributes=attrs)

    def record_ttfb(
        self,
        duration: float,
        operation: Optional[str] = None,
        network_path: Optional[str] = None,
    ) -> None:
        """Records time to first response byte (TTFB) in seconds."""
        if not self.standard_enabled or self.meter is None:
            return
        current_op = get_current_operation()
        if current_op is not None and current_op.suppressed:
            return
        raw_op = operation or (current_op.operation if current_op else None)
        attrs: Dict[str, Any] = self._base_attributes.copy()
        if raw_op is not None:
            attrs["gcp.storage.operation"] = normalize_logical_operation(raw_op)
        if network_path is not None:
            attrs["network.path"] = network_path
        self.ttfb.record(max(0.0, duration), attributes=attrs)

    def shutdown(self) -> None:
        """Flushes pending metrics on a custom MeterProvider if configured."""
        if self._meter_provider is not None and hasattr(
            self._meter_provider, "force_flush"
        ):
            try:
                self._meter_provider.force_flush()
            except Exception as exc:
                logger.debug(
                    "Failed to force_flush custom MeterProvider during client shutdown: %s",
                    exc,
                )
