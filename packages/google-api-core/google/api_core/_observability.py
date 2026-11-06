# -*- coding: utf-8 -*-
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
#

"""OpenTelemetry helpers for resolving and instantiating interceptors."""

from __future__ import annotations

import contextlib
import enum
import functools
import logging
import traceback
import urllib.parse
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Callable, Sequence

from google.api_core import _feature_gating_helpers, client_logging, exceptions
from google.api_core.client_options import ClientOptions

try:
    from opentelemetry.instrumentation.utils import (
        suppress_instrumentation as _suppress_instrumentation,
    )
except ImportError:
    _suppress_instrumentation = contextlib.nullcontext

if TYPE_CHECKING:
    # flake8: grpc and opentelemetry.trace are imported only for static analysis and type annotations
    # The 'noqa: F401' comment avoids flake8 "imported but not used" errors.
    import grpc  # noqa: F401
    import opentelemetry.trace  # noqa: F401

_LOGGER = logging.getLogger(__name__)
_TRACER_PROVIDER = "tracer_provider"
_TRACE_CONTEXT_PROPAGATOR: Any = None
_CHANNEL_INTERCEPTOR_MAPPING = (
    ("intercept_unary_unary", "_unary_unary_interceptors"),
    ("intercept_unary_stream", "_unary_stream_interceptors"),
    ("intercept_stream_unary", "_stream_unary_interceptors"),
    ("intercept_stream_stream", "_stream_stream_interceptors"),
)
_STANDARD_INTERCEPTOR_METHODS = tuple(
    method for method, _ in _CHANNEL_INTERCEPTOR_MAPPING
)


@functools.cache
def has_opentelemetry() -> bool:
    """Checks once per process if opentelemetry-api is installed."""
    try:
        # Ignored by mypy: Optional dependency only checked at runtime
        # flake8: Imported only to verify package installation
        import opentelemetry.trace  # type: ignore[import-not-found] # noqa: F401

        return True
    except ImportError:
        return False


def is_otel_capabilities_enabled(
    client_options: ClientOptions | dict[str, Any] | None = None,
    env_var: str = "GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED",
) -> bool:
    """Checks if OTel capabilities are enabled and installed.

    Args:
        client_options (ClientOptions | dict[str, Any] | None): The client options
            object or dictionary.
        env_var (str): The environment variable to check for enablement.

    Returns:
        bool: True if enabled and installed, False otherwise.
    """
    is_tracing_enabled = _feature_gating_helpers.resolve_feature_flags(
        env_var=env_var,
        feature_key=_TRACER_PROVIDER,
        configuration=client_options,
    )

    if is_tracing_enabled:
        try:
            import opentelemetry.instrumentation.grpc as otel_grpc  # type: ignore[import-not-found] # noqa: F401

            return True
        except ImportError:
            pass

    return False


def extract_trace_context(span: Any = None) -> dict[str, Any]:
    """Extracts trace_id, span_id, and Cloud Logging trace correlation fields.

    If `span` is None, falls back to `opentelemetry.trace.get_current_span()`
    when OpenTelemetry is installed. Returns an empty dict if no valid recording
    span context exists or if OpenTelemetry is not installed.

    Args:
        span (Any | None): The active OpenTelemetry span, if any.

    Returns:
        dict[str, Any]: Trace and span correlation attributes.
    """
    try:
        if span is None:
            if not has_opentelemetry():
                return {}
            # Ignored by mypy: Optional dependency only loaded after
            # has_opentelemetry() check
            from opentelemetry import trace  # type: ignore[import-not-found]

            span = trace.get_current_span()

        ctx = span.get_span_context()
        if not ctx or not ctx.is_valid:
            return {}

        trace_id_hex = f"{ctx.trace_id:032x}"
        span_id_hex = f"{ctx.span_id:016x}"
        # Per W3C Trace Context, trace_flags is an 8-bit integer (TraceFlags(int))
        # that uses bits as configuration flags; the least-significant (last) bit
        # (0x01) indicates whether the span is sampled (True: recorded/exported,
        # allowing Cloud Logging to link the log entry to Cloud Trace) or not
        # (False: not recorded). Using bitmask (& 0x01) handles both TraceFlags(0x01)
        # instances and raw TraceFlags.SAMPLED (int) constants passed to SpanContext.
        sampled = bool(ctx.trace_flags & 0x01)

        return {
            "trace_id": trace_id_hex,
            "span_id": span_id_hex,
            "logging.googleapis.com/trace": trace_id_hex,
            "logging.googleapis.com/spanId": span_id_hex,
            "logging.googleapis.com/trace_sampled": sampled,
        }
    except Exception:
        # Defensive fail-open: telemetry correlation must never crash an RPC call.
        return {}


def _extract_error_info_fields(target_exc: Any) -> tuple[Any, Any, Any]:
    """Resolves (domain, reason, metadata) from an exception, ErrorInfo, or dict."""
    # Prefer native GoogleAPICallError properties (.domain, .reason, .metadata)
    # when present; fall back to .error_info or raw gRPC trailing_metadata.
    error_info = getattr(target_exc, "error_info", None)
    if error_info is None and not (
        getattr(target_exc, "reason", None)
        or getattr(target_exc, "domain", None)
        or getattr(target_exc, "metadata", None)
    ):
        rpc_call = (
            target_exc
            if hasattr(target_exc, "trailing_metadata")
            else getattr(target_exc, "response", None)
        )
        if rpc_call is not None and hasattr(rpc_call, "trailing_metadata"):
            try:
                _, error_info = exceptions._parse_grpc_error_details(rpc_call)
            # Defensive fail-open: malformed trailing metadata must not abort
            # error attribute extraction.
            except Exception:
                pass

    source = error_info if error_info is not None else target_exc
    if isinstance(source, dict):
        return (
            source.get("domain"),
            source.get("reason"),
            source.get("metadata"),
        )
    return (
        getattr(source, "domain", None),
        getattr(source, "reason", None),
        getattr(source, "metadata", None),
    )


def _extract_error_message(
    target_exc: Any, http_response: Any = None, fallback: str | None = None
) -> str | None:
    """Resolves the human-readable error message across HTTP, gRPC, and Python errors."""
    http_msg = (
        _TraceContext._extract_http_error_message(http_response)
        if http_response is not None
        else None
    )
    details = getattr(target_exc, "details", None)
    details_msg = details() if callable(details) else details
    exc_msg = str(target_exc) if isinstance(target_exc, BaseException) else None
    raw_message = (
        http_msg
        or getattr(target_exc, "message", None)
        or details_msg
        or fallback
        or exc_msg
    )
    return str(raw_message) if raw_message else None


def build_telemetry_error_attributes(
    exc: BaseException | None,
    status_code: str | None = None,
    status_message: str | None = None,
    include_exception: bool = False,
) -> dict[str, Any]:
    """Extracts rpc.response.status_code, gcp.errors.*, error.type, status.message, and exception.* fields.

    Error details and ErrorInfo structures are resolved by inspecting:
    * Chained exceptions: Unwraps RetryError or __cause__ to the root error.
    * Canonical status code: Resolves rpc.response.status_code via
      exceptions._extract_status_code.
    * GoogleAPICallError & ErrorInfo attributes: Reads .domain, .reason, and
      .metadata directly (or from .error_info / gRPC trailing_metadata).
    * Unified attribute extraction: Populates gcp.errors.domain, error.type,
      gcp.errors.metadata.*, status.message, and optional exception.* fields.

    Args:
        exc (BaseException | None): An exception (e.g. GoogleAPICallError
            or grpc.RpcError) or ErrorInfo object.
        status_code (str | None): Optional pre-extracted or HTTP status code
            fallback when exc is None or lacks a status code.
        status_message (str | None): Optional status message fallback when
            exc is None or lacks a message.
        include_exception (bool): When True, also populates exception.type,
            exception.message, and exception.stacktrace.

    Returns:
        dict[str, Any]: Extracted error and exception attributes.
    """
    if exc is None:
        if status_code is None:
            return {}
        code_str = str(status_code)
        return {
            "rpc.response.status_code": code_str,
            "error.type": code_str,
            "status.message": status_message or f"HTTP {code_str}",
        }

    # Unwrap chained wrapper exceptions (e.g. RetryError) by one level to reach
    # the enriched GoogleAPICallError without unwrapping past it to the raw
    # transport error.
    target_exc = getattr(exc, "cause", None) or getattr(exc, "__cause__", None) or exc
    resolved_code = exceptions._extract_status_code(target_exc, default=status_code)
    domain, reason, metadata = _extract_error_info_fields(target_exc)

    # GoogleAPICallError.response holds either an HTTP Response or a gRPC Call
    # (which has trailing_metadata). Validate once up front so http_response is
    # only retained when it is an actual HTTP response with an integer status code.
    http_response = getattr(target_exc, "response", None)
    http_status = (
        getattr(http_response, "status_code", getattr(http_response, "status", None))
        if http_response is not None and not hasattr(http_response, "trailing_metadata")
        else None
    )
    if not isinstance(http_status, int) or isinstance(http_status, bool):
        http_status = None
        http_response = None

    # Populate OpenTelemetry semantic error attributes and ErrorInfo metadata
    attrs: dict[str, Any] = {"rpc.response.status_code": resolved_code}
    if domain:
        attrs["gcp.errors.domain"] = domain
    if reason:
        attrs["error.type"] = reason
    elif http_status is not None:
        attrs["error.type"] = str(http_status)
    else:
        # Every failed span or log records a low-cardinality error.type; reuse
        # the resolved canonical status code name or exception class name.
        attrs["error.type"] = resolved_code

    if metadata:
        attrs.update({f"gcp.errors.metadata.{k}": str(v) for k, v in metadata.items()})

    # Extract human-readable error description for cross-language parity
    message = _extract_error_message(target_exc, http_response, status_message)
    if message:
        attrs["status.message"] = message

    # Populate exception.* diagnostic fields for the terminal exception raised to
    # the caller when structured logging is enabled
    if include_exception:
        attrs["exception.type"] = exc.__class__.__name__
        attrs["exception.message"] = str(exc)
        attrs["exception.stacktrace"] = "".join(traceback.format_exception(exc))

    return attrs


def _decode_method_name(method: str | bytes | None) -> str:
    """Normalizes a string or bytes RPC method name to a UTF-8 string.

    Args:
        method (str | bytes | None): Raw RPC method name from call details.

    Returns:
        str: Decoded string method name (or empty string if None).
    """
    if isinstance(method, bytes):
        return method.decode("utf-8", errors="replace")
    return method or ""


def extract_rpc_identity(
    method_name: str | bytes | None,
) -> tuple[str, str, str]:
    """Extracts (full_rpc_name, service_name, rpc_method_name) from a gRPC method path.

    Args:
        method_name (str | bytes | None): Explicit gRPC method path
            (e.g. "/google.cloud.secretmanager.v1.SecretManagerService/GetSecret").

    Returns:
        tuple[str, str, str]: A 3-tuple of (full_rpc_name, service_name, rpc_method_name).
    """
    full_rpc_name = _decode_method_name(method_name).lstrip("/")
    service, _, method = full_rpc_name.rpartition("/")
    return full_rpc_name, service, method


def _resolve_rpc_system(kind: str | None = "grpc") -> str:
    """Normalizes a transport kind ('grpc', 'rest', 'rest_asyncio', 'http') to an OTel rpc.system.name.

    Args:
        kind (str | None): The transport kind identifier.

    Returns:
        str: "http" for REST/HTTP transports, or "grpc" otherwise.
    """
    if kind and kind.startswith(("rest", "http")):
        return "http"
    return "grpc"


def _get_service_logger(
    method_name: str | bytes | None = None,
    target: Callable[..., Any] | None = None,
) -> logging.Logger:
    """Resolves a service-scoped logger matching GOOGLE_SDK_PYTHON_LOGGING_SCOPE.

    - If `target` has a `__module__` starting with `google.` (excluding `google.api_core`),
      returns `logging.getLogger(target.__module__)`.
    - Otherwise, if `method_name` is a full gRPC method path (e.g.
      `/google.cloud.secretmanager.v1.SecretManagerService/GetSecret`), extracts
      the service package prefix (`google.cloud.secretmanager.v1`).
    - Falls back to `logging.getLogger("google.api_core._observability")`.

    Args:
        method_name (str | bytes | None): Full gRPC method path.
        target (Callable[..., Any] | None): The low-level RPC target callable.

    Returns:
        logging.Logger: The resolved service-scoped logger.
    """
    target_mod = getattr(target, "__module__", None)
    if (
        isinstance(target_mod, str)
        and target_mod.startswith("google.")
        and not target_mod.startswith("google.api_core")
    ):
        return logging.getLogger(target_mod)
    if method_name:
        # Example transformation:
        #   Input:        "/google.cloud.secretmanager.v1.SecretManagerService/GetSecret"
        #   service_name: "google.cloud.secretmanager.v1.SecretManagerService"
        #   pkg:          "google.cloud.secretmanager.v1"
        _, service_name, _ = extract_rpc_identity(method_name)
        pkg = service_name.rpartition(".")[0]
        if pkg.startswith("google."):
            return logging.getLogger(pkg)
    return _LOGGER


def _is_failed_attempt(
    norm_status: str | None,
    exc: BaseException | None,
) -> bool:
    """Determines whether a transport attempt ended with an error or exception.

    Args:
        norm_status (str | None): Normalized status code string (e.g. "OK", "200", "503").
        exc (BaseException | None): Exception raised or returned during the attempt.

    Returns:
        bool: True if the attempt failed, False if it succeeded.
    """
    if exc is not None:
        return True
    if norm_status is None or norm_status == "OK":
        return False
    return not (norm_status.isdecimal() and int(norm_status) < 400)


def _build_attempt_log_extra(
    span: opentelemetry.trace.Span | None,
    target: str | None,
    status_code: int | str | enum.Enum | None,
    norm_status: str | None,
    rpc_system: str,
    http_method: str | None,
    exc: BaseException | None,
    status_message: str | None,
) -> tuple[dict[str, Any], str | None]:
    """Builds the structured extra dictionary and resolved status for a failed wire attempt.

    Args:
        span (opentelemetry.trace.Span | None): Active OpenTelemetry span, if any.
        target (str | None): Full RPC method name (gRPC) or request URL (HTTP).
        status_code (int | str | enum.Enum | None): Raw HTTP status code or gRPC status name/enum.
        norm_status (str | None): Stringified status code if provided.
        rpc_system (str): Normalized OTel RPC system identifier ("grpc" or "http").
        http_method (str | None): HTTP request method (e.g. "GET", "POST").
        exc (BaseException | None): Exception raised or returned during the attempt.
        status_message (str | None): Explicit status message fallback.

    Returns:
        tuple[dict[str, Any], str | None]: A 2-tuple of (extra_payload, resolved_status).
    """
    error_attrs = build_telemetry_error_attributes(
        exc,
        status_code=norm_status,
        status_message=status_message,
        include_exception=True,
    )
    resolved_status = norm_status or error_attrs.get("rpc.response.status_code")
    extra_payload: dict[str, Any] = {
        "rpc.system.name": rpc_system,
        **error_attrs,
        "rpc.response.status_code": resolved_status,
        **extract_trace_context(span),
    }
    if rpc_system == "http":
        extra_payload["url.full"] = target
        extra_payload["httpRequest"] = {
            "requestMethod": http_method,
            "requestUrl": target,
            "status": (
                int(status_code)
                if isinstance(status_code, int)
                or (isinstance(status_code, str) and status_code.isdecimal())
                else status_code
            ),
        }
    else:
        extra_payload["rpc.method"] = target

    # Take a shallow copy before assigning json_fields so json_fields does not
    # reference extra_payload itself and cause a circular reference in json.dumps.
    extra_payload["json_fields"] = extra_payload.copy()
    return extra_payload, resolved_status


def log_transport_attempt(
    span: opentelemetry.trace.Span | None = None,
    target: str | None = None,
    status_code: int | str | enum.Enum | None = None,
    kind: str = "grpc",
    http_method: str | None = None,
    exc: BaseException | None = None,
    client_options: ClientOptions | dict[str, Any] | None = None,
    logger: logging.Logger | None = None,
    status_message: str | None = None,
) -> None:
    """Emits a DEBUG log for a failed wire attempt (retry/redirect/failure).

    Successful transport attempts (2xx HTTP or OK gRPC) return immediately without
    emitting logs to avoid hot-path allocations.

    Args:
        span (opentelemetry.trace.Span | None): Active OpenTelemetry span, if any.
        target (str | None): Full RPC method name (gRPC) or request URL (HTTP).
        status_code (int | str | enum.Enum | None): HTTP status code or gRPC status name/enum.
        kind (str): Transport kind identifier ("grpc", "rest", "rest_asyncio", or "http").
        http_method (str | None): HTTP request method (e.g. "GET", "POST").
        exc (BaseException | None): Exception raised or returned during the attempt.
        client_options (ClientOptions | dict[str, Any] | None): Client options
            used for feature gating.
        logger (logging.Logger | None): Explicit logger override.
        status_message (str | None): Explicit status message fallback.
    """
    if not client_logging.is_error_logging_enabled(client_options):
        return

    norm_status = (
        getattr(status_code, "name", str(status_code))
        if status_code is not None
        else None
    )
    if not _is_failed_attempt(norm_status, exc):
        return

    try:
        rpc_system = _resolve_rpc_system(kind)
        extra_payload, resolved_status = _build_attempt_log_extra(
            span=span,
            target=target,
            status_code=status_code,
            norm_status=norm_status,
            rpc_system=rpc_system,
            http_method=http_method,
            exc=exc,
            status_message=status_message,
        )
        target_logger = logger or _get_service_logger(
            target if rpc_system == "grpc" else None
        )
        target_logger.debug(
            "Transport attempt failed for %s (status=%s)",
            target or "unknown_target",
            resolved_status or "ERROR",
            extra=extra_payload,
        )
    except Exception:
        # Fail-open: never disrupt the caller's RPC flow on logging errors
        pass


def _extract_endpoint_attributes(
    client_options: ClientOptions | dict[str, Any] | None = None,
    default_host: str | None = None,
) -> dict[str, Any]:
    """Extracts server.address, server.port (if non-default), and url.domain from client options if present.

    Args:
        client_options (ClientOptions | dict[str, Any] | None): The client options
            object or dictionary.
        default_host (str | None): Fallback transport host when ``api_endpoint`` is not
            set on ``client_options``.

    Returns:
        dict[str, Any]: A dictionary containing url.domain and, if an api_endpoint or default_host
            is configured, server.address and non-default server.port.
    """
    attrs: dict[str, Any] = {}
    endpoint = None
    universe_domain = None

    if isinstance(client_options, dict):
        endpoint = client_options.get("api_endpoint") or default_host
        universe_domain = client_options.get("universe_domain")
    elif client_options is not None:
        endpoint = getattr(client_options, "api_endpoint", None) or default_host
        universe_domain = getattr(client_options, "universe_domain", None)
    else:
        endpoint = default_host

    attrs["url.domain"] = universe_domain or "googleapis.com"

    if endpoint and isinstance(endpoint, str):
        target = endpoint if "//" in endpoint else f"//{endpoint}"
        parsed = None
        hostname = None
        port = None
        try:
            parsed = urllib.parse.urlsplit(target)
            hostname = parsed.hostname
            port = parsed.port
        except ValueError:
            pass

        if hostname:
            attrs["server.address"] = hostname
        if port and parsed:
            scheme = parsed.scheme.lower()
            is_default_port = (port == 443 and scheme in ("https", "")) or (
                port == 80 and scheme == "http"
            )
            if not is_default_port:
                attrs["server.port"] = port
    return attrs


def _make_grpc_client_request_hook(
    endpoint_attrs: dict[str, Any] | None = None,
) -> Callable[[Any, Any], None]:
    """Creates an OpenTelemetry gRPC client request hook with optional endpoint attributes.

    Args:
        endpoint_attrs (dict[str, Any] | None): Optional static endpoint attributes to attach
            to every span.

    Returns:
        Callable[[Any, Any], None]: The request hook callback.
    """
    static_attrs = dict(endpoint_attrs) if endpoint_attrs else {}

    def client_request_hook(span: Any, request: Any) -> None:
        if span is None or not getattr(span, "is_recording", lambda: True)():
            return

        # Upstream opentelemetry-instrumentation-grpc may format span names with a
        # leading slash (e.g. "/package.Service/Method"). Normalize the span name
        # and ensure rpc.method is always captured as the clean, fully-qualified name.
        span_name = getattr(span, "name", None)
        if isinstance(span_name, str) and span_name:
            clean_method_name = span_name.lstrip("/")
            if span_name.startswith("/") and hasattr(span, "update_name"):
                span.update_name(clean_method_name)
            span.set_attribute("rpc.method", clean_method_name)

        attrs: dict[str, Any] = {
            "rpc.system.name": "grpc",
        }
        if static_attrs:
            attrs.update(static_attrs)
        for key, value in attrs.items():
            span.set_attribute(key, value)

    return client_request_hook


_grpc_client_request_hook = _make_grpc_client_request_hook()


def _grpc_client_response_hook(span: Any, response: Any) -> None:
    """OpenTelemetry gRPC client response hook to record successful response status.

    Upstream ``opentelemetry-instrumentation-grpc`` sets the integer status code
    ``rpc.grpc.status_code`` (e.g. 0), but does not record the modern string status
    ``rpc.response.status_code`` (e.g. "OK") required by Cloud Trace and current
    OpenTelemetry semantic conventions (v1.27.0+).

    This hook enriches successful RPC attempt spans with ``rpc.response.status_code = "OK"``.
    Errors and non-OK statuses are handled at the Tier 3 method span layer or upstream.

    Upstream handles synchronous and asynchronous invocations differently:
    - **Synchronous gRPC**: Upstream only invokes the response hook when an RPC call
      succeeds. On failure, the hook is bypassed entirely.
    - **Asynchronous gRPC**: Upstream invokes the response hook unconditionally for
      both successes and failures (passing exception details on error). However, it
      always marks ``span.status`` with an error status before calling the hook.

    Because of this disparity, this hook checks ``span.status`` to guard against
    async failure callbacks while allowing synchronous and successful asynchronous
    calls to be marked "OK".

    Note:
        If upstream ``opentelemetry-instrumentation-grpc`` adds native support for
        modern ``rpc.response.status_code`` in future releases, this hook can be retired.

    Args:
        span (Any | None): The OpenTelemetry span.
        response (Any): The gRPC response object or details.
    """
    if span is None or not getattr(span, "is_recording", lambda: False)():
        return

    # Guard against upstream async calls that invoke this hook on failures.
    status = getattr(span, "status", None)
    status_code = getattr(status, "status_code", None)
    if (
        getattr(status_code, "name", None) == "ERROR"
        or getattr(status_code, "value", None) == 2
    ):
        return

    span.set_attribute("rpc.response.status_code", "OK")


def _get_tracer_provider(
    client_options: ClientOptions | dict[str, Any] | None = None,
) -> opentelemetry.trace.TracerProvider | None:
    """Extracts the OpenTelemetry tracer provider from client options if present.

    Args:
        client_options (ClientOptions | dict[str, Any] | None): The client options
            object or dictionary.

    Returns:
        opentelemetry.trace.TracerProvider | None: The tracer provider if present,
            None otherwise.
    """
    if isinstance(client_options, dict):
        return client_options.get(_TRACER_PROVIDER)
    elif client_options is not None:
        return getattr(client_options, _TRACER_PROVIDER, None)
    return None


try:
    # flake8: `grpc` imported conditionally for runtime interceptor base classes
    import grpc  # noqa: F811
    from grpc import (
        StreamStreamClientInterceptor as _SyncStreamStreamClientInterceptor,
    )
    from grpc import (
        StreamUnaryClientInterceptor as _SyncStreamUnaryClientInterceptor,
    )
    from grpc import (
        UnaryStreamClientInterceptor as _SyncUnaryStreamClientInterceptor,
    )
    from grpc import (
        UnaryUnaryClientInterceptor as _SyncUnaryUnaryClientInterceptor,
    )
    from grpc.aio import (
        StreamStreamClientInterceptor as _AsyncStreamStreamClientInterceptor,
    )
    from grpc.aio import (
        StreamUnaryClientInterceptor as _AsyncStreamUnaryClientInterceptor,
    )
    from grpc.aio import (
        UnaryStreamClientInterceptor as _AsyncUnaryStreamClientInterceptor,
    )
    from grpc.aio import (
        UnaryUnaryClientInterceptor as _AsyncUnaryUnaryClientInterceptor,
    )
except ImportError:  # pragma: NO COVER
    # mypy: Fallbacks:  grpc sentinel when optional grpc is not installed in the environment.
    # and distinct empty classes avoid duplicate base class 'object' TypeError at runtime.
    grpc = None  # type: ignore[assignment]

    class _SyncUnaryUnaryClientInterceptor:  # type: ignore[no-redef]
        __slots__ = ()

    class _SyncUnaryStreamClientInterceptor:  # type: ignore[no-redef]
        __slots__ = ()

    class _SyncStreamUnaryClientInterceptor:  # type: ignore[no-redef]
        __slots__ = ()

    class _SyncStreamStreamClientInterceptor:  # type: ignore[no-redef]
        __slots__ = ()

    class _AsyncUnaryUnaryClientInterceptor:  # type: ignore[no-redef]
        __slots__ = ()

    class _AsyncUnaryStreamClientInterceptor:  # type: ignore[no-redef]
        __slots__ = ()

    class _AsyncStreamUnaryClientInterceptor:  # type: ignore[no-redef]
        __slots__ = ()

    class _AsyncStreamStreamClientInterceptor:  # type: ignore[no-redef]
        __slots__ = ()


class _SuppressingClientInterceptor(
    _SyncUnaryUnaryClientInterceptor,
    _SyncUnaryStreamClientInterceptor,
    _SyncStreamUnaryClientInterceptor,
    _SyncStreamStreamClientInterceptor,
):
    """Client interceptor that suppresses redundant downstream generic auto-instrumentation spans.

    When users enable global OpenTelemetry gRPC auto-instrumentation (e.g. GrpcInstrumentorClient),
    the underlying channel is wrapped with generic interceptors that emit bare-bones spans.
    This interceptor wraps downstream calls in OpenTelemetry's native `suppress_instrumentation`
    context manager so that our feature-rich Google Cloud SDK T4 span is emitted while
    redundant generic downstream spans are bypassed.
    """

    __slots__ = ()

    def intercept_unary_unary(
        self, continuation: Any, client_call_details: Any, request: Any
    ) -> Any:
        with _suppress_instrumentation():
            return continuation(client_call_details, request)

    def intercept_unary_stream(
        self, continuation: Any, client_call_details: Any, request: Any
    ) -> Any:
        with _suppress_instrumentation():
            return continuation(client_call_details, request)

    def intercept_stream_unary(
        self, continuation: Any, client_call_details: Any, request_iterator: Any
    ) -> Any:
        with _suppress_instrumentation():
            return continuation(client_call_details, request_iterator)

    def intercept_stream_stream(
        self, continuation: Any, client_call_details: Any, request_iterator: Any
    ) -> Any:
        with _suppress_instrumentation():
            return continuation(client_call_details, request_iterator)


class _AsyncSuppressingClientInterceptor(
    _AsyncUnaryUnaryClientInterceptor,
    _AsyncUnaryStreamClientInterceptor,
    _AsyncStreamUnaryClientInterceptor,
    _AsyncStreamStreamClientInterceptor,
):
    """AsyncIO client interceptor that suppresses redundant downstream generic auto-instrumentation spans."""

    __slots__ = ()

    async def intercept_unary_unary(
        self, continuation: Any, client_call_details: Any, request: Any
    ) -> Any:
        with _suppress_instrumentation():
            return await continuation(client_call_details, request)

    async def intercept_unary_stream(
        self, continuation: Any, client_call_details: Any, request: Any
    ) -> Any:
        with _suppress_instrumentation():
            return await continuation(client_call_details, request)

    async def intercept_stream_unary(
        self, continuation: Any, client_call_details: Any, request_iterator: Any
    ) -> Any:
        with _suppress_instrumentation():
            return await continuation(client_call_details, request_iterator)

    async def intercept_stream_stream(
        self, continuation: Any, client_call_details: Any, request_iterator: Any
    ) -> Any:
        with _suppress_instrumentation():
            return await continuation(client_call_details, request_iterator)


@contextlib.contextmanager
def _capture_grpc_attempt_exception(
    method_name: str,
    client_options: ClientOptions | dict[str, Any] | None = None,
) -> Iterator[None]:
    """Logs any unhandled exception raised during gRPC continuation dispatch and re-raises.

    Args:
        method_name (str): Decoded gRPC method name.
        client_options (ClientOptions | dict[str, Any] | None): Client options
            used for error logging gating.

    Yields:
        None
    """
    try:
        yield
    except BaseException as exc:
        log_transport_attempt(
            target=method_name,
            kind="grpc",
            exc=exc,
            client_options=client_options,
        )
        raise


class _GrpcAttemptLoggingInterceptor(_SyncUnaryUnaryClientInterceptor):
    """Sync gRPC client interceptor that logs failed wire attempts at DEBUG level.

    Args:
        client_options (ClientOptions | dict[str, Any] | None): Client options
            used for error logging gating.
    """

    __slots__ = ("_client_options",)

    def __init__(
        self, client_options: ClientOptions | dict[str, Any] | None = None
    ) -> None:
        self._client_options = client_options

    def intercept_unary_unary(
        self,
        continuation: Callable[..., Any],
        client_call_details: grpc.ClientCallDetails,
        request: Any,
    ) -> Any:
        """Intercepts a sync unary-unary gRPC call and logs failed wire attempts.

        Args:
            continuation (Callable[..., Any]): Next interceptor or channel continuation callable.
            client_call_details (grpc.ClientCallDetails): gRPC call details containing the method name.
            request (Any): Outbound protobuf request message.

        Returns:
            Any: The gRPC Call/Future response returned by ``continuation``.
        """
        method_name = _decode_method_name(getattr(client_call_details, "method", None))
        with _capture_grpc_attempt_exception(method_name, self._client_options):
            response = continuation(client_call_details, request)

        try:
            exc_fn = getattr(response, "exception", None)
            if callable(exc_fn) and (resp_exc := exc_fn()) is not None:
                code_fn = getattr(response, "code", None)
                log_transport_attempt(
                    target=method_name,
                    status_code=code_fn() if callable(code_fn) else None,
                    kind="grpc",
                    exc=resp_exc,
                    client_options=self._client_options,
                )
        except Exception:
            # Fail-open: never disrupt the caller's RPC flow on post-dispatch inspection errors
            pass
        return response


class _AsyncGrpcAttemptLoggingInterceptor(_AsyncUnaryUnaryClientInterceptor):
    """AsyncIO gRPC client interceptor that logs failed wire attempts at DEBUG level.

    Args:
        client_options (ClientOptions | dict[str, Any] | None): Client options
            used for error logging gating.
    """

    __slots__ = ("_client_options",)

    def __init__(
        self, client_options: ClientOptions | dict[str, Any] | None = None
    ) -> None:
        self._client_options = client_options

    async def intercept_unary_unary(
        self,
        continuation: Callable[..., Any],
        client_call_details: grpc.aio.ClientCallDetails,
        request: Any,
    ) -> Any:
        """Intercepts an async unary-unary gRPC call and logs failed wire attempts.

        Args:
            continuation (Callable[..., Any]): Next async interceptor or channel continuation callable.
            client_call_details (grpc.aio.ClientCallDetails): gRPC call details containing the method name.
            request (Any): Outbound protobuf request message.

        Returns:
            Any: The async gRPC call object returned by ``continuation``.
        """
        method_name = _decode_method_name(getattr(client_call_details, "method", None))
        with _capture_grpc_attempt_exception(method_name, self._client_options):
            call = await continuation(client_call_details, request)

        try:
            code_fn = getattr(call, "code", None)
            if (
                callable(code_fn)
                and getattr(code := await code_fn(), "name", str(code)) != "OK"
            ):
                details_fn = getattr(call, "details", None)
                details = await details_fn() if callable(details_fn) else ""
                log_transport_attempt(
                    target=method_name,
                    status_code=code,
                    kind="grpc",
                    exc=Exception(details) if details else None,
                    client_options=self._client_options,
                    status_message=details or None,
                )
        except Exception:
            # Fail-open: never disrupt the caller's RPC flow on post-dispatch inspection errors
            pass
        return call


def _build_otel_grpc_hook_kwargs(
    client_options: ClientOptions | dict[str, Any] | None = None,
    default_host: str | None = None,
) -> dict[str, Any]:
    """Builds the keyword arguments passed to OpenTelemetry's gRPC interceptor factories.

    Both the sync (`otel_grpc.client_interceptor`) and async
    (`otel_grpc.aio_client_interceptors`) factories in `opentelemetry.instrumentation.grpc`
    accept the same keyword arguments to configure how gRPC client spans are created
    and enriched with Google Cloud attributes.

    Args:
        client_options (ClientOptions | dict[str, Any] | None): Client options
            used to resolve endpoint attributes and a custom tracer provider.
        default_host (str | None): Fallback transport host when ``api_endpoint`` is not
            set on ``client_options``.

    Returns:
        dict[str, Any]: A dictionary with ``tracer_provider``, ``request_hook``, and
            ``response_hook`` ready to unpack (``**``) into the OpenTelemetry gRPC
            interceptor factory functions.
    """
    endpoint_attrs = _extract_endpoint_attributes(
        client_options, default_host=default_host
    )
    return {
        "tracer_provider": _get_tracer_provider(client_options),
        "request_hook": _make_grpc_client_request_hook(endpoint_attrs),
        "response_hook": _grpc_client_response_hook,
    }


def get_otel_interceptor(
    client_options: ClientOptions | dict[str, Any] | None = None,
    default_host: str | None = None,
) -> Callable[[grpc.Channel], grpc.Channel] | None:
    """Returns a callable that wraps a sync gRPC channel with tracing and/or error logging.

    Args:
        client_options (ClientOptions | dict[str, Any] | None): The client options
            object or dictionary used for feature gating and extracting the tracer provider.
        default_host (str | None): Fallback transport host when ``api_endpoint`` is not
            set on ``client_options``.

    Returns:
        Callable[[grpc.Channel], grpc.Channel] | None: A channel-wrapping callable if
            OpenTelemetry tracing or error logging is enabled, None otherwise.
    """
    tracing_enabled = is_otel_capabilities_enabled(client_options)
    error_logging_enabled = client_logging.is_error_logging_enabled(client_options)
    if not tracing_enabled and not error_logging_enabled:
        return None

    custom_interceptors: list[grpc.ClientInterceptor] = []
    tracing_interceptor: grpc.ClientInterceptor | None = None

    # Order matters (outer -> inner):
    #   1. tracing_interceptor (outermost: starts the Tier 4 gRPC span)
    #   2. _GrpcAttemptLoggingInterceptor (middle: logs failed attempts with the
    #      Tier 4 span active, outside of suppress_instrumentation)
    #   3. _SuppressingClientInterceptor (innermost: suppresses downstream
    #      generic auto-instrumentation without suppressing our attempt logs)
    if error_logging_enabled:
        custom_interceptors.append(_GrpcAttemptLoggingInterceptor(client_options))

    if tracing_enabled:
        import opentelemetry.instrumentation.grpc as otel_grpc  # type: ignore[import-not-found]

        tracing_interceptor = otel_grpc.client_interceptor(
            **_build_otel_grpc_hook_kwargs(client_options, default_host)
        )
        custom_interceptors.append(_SuppressingClientInterceptor())

    def apply_sync_otel_interceptors(channel: grpc.Channel) -> grpc.Channel:
        """Applies configured sync observability interceptors to a gRPC channel.

        Args:
            channel (grpc.Channel): The synchronous gRPC channel to wrap.

        Returns:
            grpc.Channel: The intercepted gRPC channel.
        """
        if grpc is not None and custom_interceptors:
            try:
                channel = grpc.intercept_channel(channel, *custom_interceptors)
            except (AttributeError, TypeError):
                # Fallback if grpc lacks intercept_channel or custom channel type rejects it.
                pass
        if tracing_interceptor is not None:
            return otel_grpc.intercept_channel(channel, tracing_interceptor)
        return channel

    # Ignored by mypy: Function attribute used to tag our interceptor wrapper
    apply_sync_otel_interceptors._is_otel_interceptor = True  # type: ignore[attr-defined]
    return apply_sync_otel_interceptors


def get_otel_async_interceptor(
    client_options: ClientOptions | dict[str, Any] | None = None,
    default_host: str | None = None,
) -> Sequence[grpc.aio.ClientInterceptor] | None:
    """Returns async gRPC client interceptors for OpenTelemetry tracing and/or error logging.

    Args:
        client_options (ClientOptions | dict[str, Any] | None): The client options
            object or dictionary used for feature gating and extracting the tracer provider.
        default_host (str | None): Fallback transport host when ``api_endpoint`` is not
            set on ``client_options``.

    Returns:
        Sequence[grpc.aio.ClientInterceptor] | None: Instantiated async client interceptors
            if OpenTelemetry tracing or error logging is enabled, None otherwise.
    """
    tracing_enabled = is_otel_capabilities_enabled(client_options)
    error_logging_enabled = client_logging.is_error_logging_enabled(client_options)
    if not tracing_enabled and not error_logging_enabled:
        return None

    # Order matters (outer -> inner):
    #   1. raw_interceptors (outermost: starts the Tier 4 async gRPC span)
    #   2. _AsyncGrpcAttemptLoggingInterceptor (middle: logs failed attempts with
    #      the Tier 4 span active, outside of suppress_instrumentation)
    #   3. _AsyncSuppressingClientInterceptor (innermost: suppresses downstream
    #      generic auto-instrumentation without suppressing our attempt logs)
    interceptors: list[grpc.aio.ClientInterceptor] = []
    if tracing_enabled:
        # Ignored by mypy: Optional dependency only loaded if tracing_enabled is True
        import opentelemetry.instrumentation.grpc as otel_grpc  # type: ignore[import-not-found]

        raw_interceptors = otel_grpc.aio_client_interceptors(
            **_build_otel_grpc_hook_kwargs(client_options, default_host)
        )
        interceptors.extend(
            raw_interceptors
            if isinstance(raw_interceptors, (list, tuple))
            else [raw_interceptors]
        )

    if error_logging_enabled:
        interceptors.append(_AsyncGrpcAttemptLoggingInterceptor(client_options))

    if tracing_enabled:
        interceptors.append(_AsyncSuppressingClientInterceptor())

    return interceptors


def apply_otel_async_channel_interceptors(
    channel: Any,
    client_options: ClientOptions | dict[str, Any] | Sequence[Any] | None = None,
    default_host: str | None = None,
) -> Any:
    """Creates and attaches OpenTelemetry client interceptors to the front of an async gRPC channel.

    In grpc.aio, channels maintain internal interceptor lists evaluated in index order.
    To ensure Google Cloud SDK telemetry wraps outside downstream interceptors and
    suppresses ambient generic auto-instrumentation, our interceptors are prepended
    to the front of the channel's interceptor lists.

    Args:
        channel: The async gRPC channel to intercept.
        client_options (ClientOptions | dict[str, Any] | Sequence[Any] | None): The client
            options used to resolve feature flags and tracer provider, or a sequence of
            pre-resolved interceptors.
        default_host (str | None): Fallback transport host when ``api_endpoint`` is not
            set on ``client_options``.

    Returns:
        The channel with interceptors prepended to its internal lists,
        or the original channel if tracing is disabled or not installed.
    """
    otel_interceptors: Sequence[Any] | None
    if isinstance(client_options, (ClientOptions, dict)) or client_options is None:
        otel_interceptors = get_otel_async_interceptor(
            client_options, default_host=default_host
        )
    elif isinstance(client_options, Sequence):
        otel_interceptors = client_options
    else:
        otel_interceptors = None

    if not otel_interceptors:
        return channel

    interceptor_list = list(otel_interceptors)

    # Section 1: Typed interceptors - prepend matching interceptors to each
    # corresponding channel list (unary-unary, unary-stream, etc.) in order.
    # See note in the docstring about why prepending is important here.
    for method_name, attr_name in _CHANNEL_INTERCEPTOR_MAPPING:
        target_list = getattr(channel, attr_name, None)
        if isinstance(target_list, list):
            matching = [
                i
                for i in interceptor_list
                if hasattr(i, method_name) and i not in target_list
            ]
            if matching:
                target_list[:0] = matching

    # Section 2: Untyped/generic fallback - prepend any remaining interceptors
    # lacking standard method names directly to the unary-unary list.
    unary_list = getattr(channel, "_unary_unary_interceptors", None)
    if isinstance(unary_list, list):
        fallback_items = [
            i
            for i in interceptor_list
            if not any(hasattr(i, m) for m in _STANDARD_INTERCEPTOR_METHODS)
            and i not in unary_list
        ]
        if fallback_items:
            unary_list[:0] = fallback_items

    return channel


class _TraceContext:
    """Context manager for tracing an HTTP wire request with OpenTelemetry.

    Manages span creation, semantic attribute attachment, W3C traceparent injection,
    and automatic error recording on failure without suppressing caller exceptions.

    Supports two calling conventions:
    - Pass a single `request` object (such as `requests.PreparedRequest`).
    - Pass explicit keyword arguments (`method`, `url`, `headers`, `body`, `client_options`).
    """

    @staticmethod
    def _get_trace_context_propagator() -> Any:
        global _TRACE_CONTEXT_PROPAGATOR
        if _TRACE_CONTEXT_PROPAGATOR is None:
            from opentelemetry.trace.propagation.tracecontext import (  # type: ignore[import-not-found]
                TraceContextTextMapPropagator,
            )

            _TRACE_CONTEXT_PROPAGATOR = TraceContextTextMapPropagator()
        return _TRACE_CONTEXT_PROPAGATOR

    # The HTTP tracing context manager deliberately supports two distinct invocation styles:
    # 1. Bundled Request Object: `trace_http_request(request, ...)`
    #    Used when callers already possess an HTTP request instance (such as
    #    requests.PreparedRequest or urllib.request.Request) with `.method`, `.url`, etc.
    # 2. Unpacked Keyword Arguments: `trace_http_request(method=..., url=..., headers=..., body=...)`
    #    Used by generated GAPIC REST transports (_shared_macros.j2).
    #    In GAPIC templates, requests are assembled from local strings and dictionaries before
    #    hitting the session. Supporting keyword arguments avoids the CPU and memory overhead
    #    of instantiating a throwaway dummy request object on every single RPC execution.
    @staticmethod
    def _build_http_span_attributes(
        request: Any = None,
        *,
        method: str | None = None,
        url: str | None = None,
        url_template: str | None = None,
        headers: dict[str, Any] | None = None,
        body: Any = None,
        client_options: ClientOptions | dict[str, Any] | None = None,
    ) -> tuple[str, dict[str, Any], Any]:
        """Extract span name, semantic attributes dictionary, and resolved headers.

        Supports two calling conventions:
        - Pass a single `request` object (such as `requests.PreparedRequest`).
        - Pass explicit keyword arguments (`method`, `url`, `headers`, `body`, `client_options`).

        Returns:
            tuple[str, dict[str, Any], Any]: A tuple of (span_name, attributes, resolved_headers).
        """
        if request is not None:
            resolved_method = getattr(request, "method", "HTTP") or "HTTP"
            resolved_url = getattr(request, "url", "") or ""
            resolved_headers = getattr(request, "headers", None)
            resolved_body = getattr(request, "body", None)
        else:
            resolved_method = method or "HTTP"
            resolved_url = url or ""
            resolved_headers = headers
            resolved_body = body

        resolved_method = resolved_method.upper()
        endpoint_attrs = _extract_endpoint_attributes(client_options)

        server_address = endpoint_attrs.get("server.address")
        server_port = endpoint_attrs.get("server.port")
        if not server_address and resolved_url:
            try:
                parsed = urllib.parse.urlsplit(resolved_url)
                server_address = parsed.hostname
                if not server_port and parsed.port:
                    server_port = parsed.port
            except Exception:  # Fail-open on malformed URL parsing
                pass

        span_name = (
            f"{resolved_method} {url_template}" if url_template else resolved_method
        )
        span_attributes: dict[str, Any] = {
            "rpc.system.name": "http",
            "http.request.method": resolved_method,
            "server.address": server_address or "",
            "server.port": server_port or 443,
            "url.domain": endpoint_attrs.get("url.domain", "googleapis.com"),
        }
        if url_template:
            span_attributes["url.template"] = url_template
        if resolved_url:
            span_attributes["url.full"] = resolved_url

        if resolved_body is not None and isinstance(resolved_body, (bytes, str)):
            span_attributes["http.request.body.size"] = len(resolved_body)

        return span_name, span_attributes, resolved_headers

    @staticmethod
    def _extract_http_error_message(response: Any) -> str | None:
        """Extract a human-readable error message from an HTTP error response."""
        json_fn = getattr(response, "json", None)
        if callable(json_fn):
            try:
                payload = json_fn()
                if isinstance(payload, dict):
                    err_obj = payload.get("error")
                    if isinstance(err_obj, dict):
                        msg = err_obj.get("message")
                        if isinstance(msg, str) and msg:
                            return msg
                    elif isinstance(err_obj, str) and err_obj:
                        return err_obj
            # Intentionally catch broad Exception so telemetry extraction
            # fails open and never disrupts the caller's RPC flow.
            except Exception:
                pass
        for attr in ("text", "reason"):
            try:
                val = getattr(response, attr, None)
                if isinstance(val, str) and val.strip():
                    return val.strip()
            # Intentionally catch broad Exception so telemetry extraction
            # fails open and never disrupts the caller's RPC flow.
            except Exception:
                continue
        return None

    def __init__(
        self,
        request: Any = None,
        *,
        method: str | None = None,
        url: str | None = None,
        url_template: str | None = None,
        headers: dict[str, Any] | None = None,
        body: Any = None,
        client_options: ClientOptions | dict[str, Any] | None = None,
    ):
        self._request = request
        self._method = method
        self._url = url
        self._url_template = url_template
        self._headers = headers
        self._body = body
        self._client_options = client_options
        self._span: Any = None
        self._parent_span: Any = None
        self._cm: Any = None

    def _log_http_attempt(
        self,
        status_code: int | str | None = None,
        exc: BaseException | None = None,
        status_message: str | None = None,
    ) -> None:
        """Emits a DEBUG transport attempt log for a failed HTTP request (fail-open).

        Args:
            status_code (int | str | None): HTTP response status code or error code.
            exc (BaseException | None): Exception raised during HTTP dispatch, if any.
            status_message (str | None): Extracted HTTP error message fallback.
        """
        try:
            resolved_url = (
                getattr(self._request, "url", None)
                if self._request is not None
                else self._url
            )
            resolved_method = (
                getattr(self._request, "method", None)
                if self._request is not None
                else self._method
            )
            log_transport_attempt(
                span=self._span,
                target=resolved_url,
                status_code=status_code,
                kind="http",
                http_method=resolved_method,
                exc=exc,
                client_options=self._client_options,
                status_message=status_message,
            )
        # Intentionally catch broad Exception so telemetry logging fails open
        # and never disrupts the caller's RPC flow.
        except Exception:
            pass

    def record_response(self, response: Any) -> None:
        """Record HTTP response attributes on the active span and log failed attempts.

        Args:
            response (Any): The HTTP response object (e.g. requests.Response).
        """
        status_code = getattr(
            response, "status_code", getattr(response, "status", None)
        )
        code_int: int | None = None
        error_msg: str | None = None
        if status_code is not None:
            try:
                code_int = int(status_code)
                if code_int >= 400:
                    error_msg = self._extract_http_error_message(response)
                    self._log_http_attempt(
                        status_code=code_int, status_message=error_msg
                    )
            # Intentionally catch broad Exception so telemetry extraction/logging
            # fails open and never disrupts the caller's RPC flow.
            except Exception:
                pass

        span = self._span
        if span is None or not hasattr(span, "set_attribute"):
            return

        try:
            from opentelemetry.trace.status import (  # type: ignore[import-not-found]
                Status,
                StatusCode,
            )

            if code_int is not None:
                span.set_attribute("http.response.status_code", code_int)
                if self._parent_span is not None:
                    self._parent_span.set_attribute(
                        "http.response.status_code", code_int
                    )
                if code_int >= 400:
                    span.set_status(Status(StatusCode.ERROR))
                    span.set_attribute("error.type", str(code_int))
                    if error_msg:
                        span.set_attribute("status.message", error_msg)

            headers = getattr(response, "headers", None)
            if headers and "Content-Length" in headers:
                try:
                    span.set_attribute(
                        "http.response.body.size", int(headers["Content-Length"])
                    )
                except (ValueError, TypeError):
                    pass
            elif getattr(response, "_content", None) is not None:
                span.set_attribute("http.response.body.size", len(response._content))
        # Intentionally catch broad Exception so telemetry span enrichment
        # fails open and never disrupts the caller's RPC flow.
        except Exception:
            pass

    # Alias for method name parity with Daniel's suggested convention
    record_http_response = record_response

    def record_error(self, exc: BaseException | None) -> None:
        """Record supplemental Cloud Observability error attributes on the active span and log failed attempts.

        Upstream OpenTelemetry's ``start_as_current_span`` context manager automatically
        records the exception event and marks the span status as ERROR when an unhandled
        exception escapes (via its default ``record_exception=True`` and
        ``set_status_on_exception=True`` settings).

        This method supplements that base OpenTelemetry behavior by enriching the span
        with semantic attributes required by Cloud Trace and the Google Cloud Observability
        specification:
        - ``error.type``: Low-cardinality status code string (e.g. "404") or exception class name.
        - ``status.message``: Error description message.

        Args:
            exc (BaseException | None): The exception raised during dispatch.
        """
        if exc is None:
            return

        status_code = getattr(exc, "code", None) or getattr(exc, "status_code", None)
        self._log_http_attempt(status_code=status_code, exc=exc)

        span = self._span
        if span is None:
            return

        try:
            if status_code:
                span.set_attribute("error.type", str(status_code))
            else:
                span.set_attribute("error.type", exc.__class__.__name__)
            msg = str(exc)
            if msg:
                span.set_attribute("status.message", msg)
        # Intentionally catch broad Exception so telemetry span enrichment
        # fails open and never disrupts the caller's RPC flow.
        except Exception:
            pass

    # Alias for method name parity with Daniel's suggested convention
    record_http_error = record_error

    def __enter__(self) -> "_TraceContext":
        if not is_otel_capabilities_enabled(self._client_options):
            return self

        try:
            from opentelemetry import trace

            tracer_provider = _get_tracer_provider(self._client_options)
            if tracer_provider is not None:
                tracer = tracer_provider.get_tracer("google.api_core")
            else:
                tracer = trace.get_tracer("google.api_core")

            span_name, span_attributes, resolved_headers = (
                self._build_http_span_attributes(
                    self._request,
                    method=self._method,
                    url=self._url,
                    url_template=self._url_template,
                    headers=self._headers,
                    body=self._body,
                    client_options=self._client_options,
                )
            )

            parent_span = trace.get_current_span()
            if (
                parent_span is not None
                and getattr(parent_span, "is_recording", lambda: False)() is True
                and hasattr(parent_span, "set_attribute")
            ):
                self._parent_span = parent_span
                if self._url_template:
                    try:
                        parent_attrs = getattr(parent_span, "attributes", None)
                        if parent_attrs is None or "url.template" not in parent_attrs:
                            parent_span.set_attribute(
                                "url.template", self._url_template
                            )
                    # Intentionally catch broad Exception so telemetry extraction
                    # fails open and never disrupts the caller's RPC flow.
                    except Exception:
                        pass

            self._cm = tracer.start_as_current_span(
                span_name,
                kind=trace.SpanKind.CLIENT,
                attributes=span_attributes,
            )
            self._span = self._cm.__enter__()

            if resolved_headers is not None and hasattr(
                resolved_headers, "__setitem__"
            ):
                try:
                    self._get_trace_context_propagator().inject(resolved_headers)
                except Exception:  # Fail-open on header injection failure
                    pass

            return self
        except Exception:
            # Fail-open: telemetry failures must never disrupt core RPC execution
            return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if self._cm is not None:
            try:
                if exc_val is not None:
                    self.record_error(exc_val)
            finally:
                self._cm.__exit__(exc_type, exc_val, exc_tb)
        elif exc_val is not None:
            self.record_error(exc_val)
        # Always return None so caller exceptions are never suppressed
        return None


def trace_http_request(
    request: Any = None,
    *,
    method: str | None = None,
    url: str | None = None,
    url_template: str | None = None,
    headers: dict[str, Any] | None = None,
    body: Any = None,
    client_options: ClientOptions | dict[str, Any] | None = None,
) -> _TraceContext:
    """Context manager factory for tracing an HTTP wire request with OpenTelemetry.

    Manages span creation, semantic attribute attachment, W3C traceparent injection,
    and automatic error recording on failure without suppressing caller exceptions.

    Supports two calling conventions:
    1. Bundled Request Object: `trace_http_request(request, ...)`
       Used when callers already possess an HTTP request instance (such as
       `requests.PreparedRequest` or `urllib.request.Request`) with `.method`, `.url`, etc.
    2. Unpacked Keyword Arguments: `trace_http_request(method=..., url=..., headers=..., body=...)`
       Used by generated GAPIC REST transports (_shared_macros.j2).
       In GAPIC templates, requests are assembled from local strings and dictionaries before
       hitting the session. Supporting keyword arguments avoids the CPU and memory overhead
       of instantiating a throwaway dummy request object on every single RPC execution.

    Args:
        request (Any | None): Bundled HTTP request object with .method, .url, .headers.
        method (str | None): Explicit HTTP method (e.g. "GET", "POST").
        url (str | None): Fully qualified request URL.
        url_template (str | None): Parameterized path template for url.template.
        headers (dict[str, Any] | None): Mutable dictionary of request headers.
        body (Any | None): Request payload (used for body size calculation).
        client_options (ClientOptions | dict[str, Any] | None): Client options
            containing custom endpoint and tracer provider configurations.

    Returns:
        _TraceContext: An active context manager managing the HTTP client span.
    """
    return _TraceContext(
        request=request,
        method=method,
        url=url,
        url_template=url_template,
        headers=headers,
        body=body,
        client_options=client_options,
    )
