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
import urllib.parse
from typing import TYPE_CHECKING, Any, Callable, Sequence

from google.api_core import _feature_gating_helpers
from google.api_core.client_options import ClientOptions

try:
    from opentelemetry.instrumentation.utils import (
        suppress_instrumentation as _suppress_instrumentation,
    )
except ImportError:
    _suppress_instrumentation = contextlib.nullcontext

if TYPE_CHECKING:
    # flake8: grpc, trace, and ClientInterceptor are imported only for static analysis and type annotations
    # The 'noqa: F401' comment avoids flake8 "imported but not used" errors.
    import grpc  # noqa: F401
    import opentelemetry.trace  # noqa: F401

    from google.api_core.grpc_helpers import ClientInterceptor  # noqa: F401

_TRACER_PROVIDER = "tracer_provider"


def is_otel_capabilities_enabled(
    client_options: ClientOptions | dict[str, Any] | None = None,
    env_var: str = "GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED",
) -> bool:
    """Checks if OTel capabilities are enabled and installed.

    Args:
        client_options (Optional[Union[ClientOptions, dict[str, Any]]]): The client options
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


def _extract_endpoint_attributes(
    client_options: ClientOptions | dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Extracts server.address, server.port (if non-default), and url.domain from client options if present.

    Args:
        client_options (Optional[Union[ClientOptions, dict[str, Any]]]): The client options
            object or dictionary.

    Returns:
        dict[str, Any]: A dictionary containing url.domain and, if an api_endpoint is configured,
            server.address and non-default server.port.
    """
    attrs: dict[str, Any] = {}
    endpoint = None
    universe_domain = None

    if isinstance(client_options, dict):
        endpoint = client_options.get("api_endpoint")
        universe_domain = client_options.get("universe_domain")
    elif client_options is not None:
        endpoint = getattr(client_options, "api_endpoint", None)
        universe_domain = getattr(client_options, "universe_domain", None)

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
        endpoint_attrs (Optional[dict[str, Any]]): Optional static endpoint attributes to attach
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
        span (Optional[Any]): The OpenTelemetry span.
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
        client_options (Optional[Union[ClientOptions, dict[str, Any]]]): The client options
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


def get_otel_interceptor(
    client_options: ClientOptions | dict[str, Any] | None = None,
) -> Callable[[grpc.Channel], grpc.Channel] | None:
    """Returns an interceptor callable that wraps a sync gRPC channel with OpenTelemetry tracing.

    Args:
        client_options (Optional[Union[ClientOptions, dict[str, Any]]]): The client options
            object or dictionary used for feature gating and extracting the tracer provider.

    Returns:
        Callable[[grpc.Channel], grpc.Channel] | None: An interceptor callable if OpenTelemetry
            tracing is enabled and installed, None otherwise.
    """
    if not is_otel_capabilities_enabled(client_options):
        return None

    import opentelemetry.instrumentation.grpc as otel_grpc  # type: ignore[import-not-found]

    endpoint_attrs = _extract_endpoint_attributes(client_options)
    request_hook = _make_grpc_client_request_hook(endpoint_attrs)

    interceptor: ClientInterceptor = otel_grpc.client_interceptor(
        tracer_provider=_get_tracer_provider(client_options),
        request_hook=request_hook,
        response_hook=_grpc_client_response_hook,
    )
    suppressor = _SuppressingClientInterceptor()

    def otel_interceptor(channel: grpc.Channel) -> grpc.Channel:
        if grpc is not None:
            try:
                channel = grpc.intercept_channel(channel, suppressor)
            except (AttributeError, TypeError):
                # Fallback if grpc lacks intercept_channel or custom channel type rejects it.
                pass
        return otel_grpc.intercept_channel(channel, interceptor)

    otel_interceptor._is_otel_interceptor = True  # type: ignore[attr-defined]
    return otel_interceptor


def get_otel_async_interceptor(
    client_options: ClientOptions | dict[str, Any] | None = None,
) -> Sequence[grpc.aio.ClientInterceptor] | None:
    """Returns async gRPC client interceptors for OpenTelemetry tracing.

    Args:
        client_options (Optional[Union[ClientOptions, dict[str, Any]]]): The client options
            object or dictionary used for feature gating and extracting the tracer provider.

    Returns:
        Sequence[grpc.aio.ClientInterceptor] | None: Instantiated OpenTelemetry async
            client interceptors if tracing is enabled and installed, None otherwise.
    """
    if not is_otel_capabilities_enabled(client_options):
        return None

    # Ignored by mypy: Optional dependency only loaded if early-return is skipped
    import opentelemetry.instrumentation.grpc as otel_grpc  # type: ignore[import-not-found]

    endpoint_attrs = _extract_endpoint_attributes(client_options)
    request_hook = _make_grpc_client_request_hook(endpoint_attrs)

    raw_interceptors = otel_grpc.aio_client_interceptors(
        tracer_provider=_get_tracer_provider(client_options),
        request_hook=request_hook,
        response_hook=_grpc_client_response_hook,
    )
    interceptors = (
        list(raw_interceptors)
        if isinstance(raw_interceptors, (list, tuple))
        else [raw_interceptors]
    )
    interceptors.append(_AsyncSuppressingClientInterceptor())

    return interceptors


_CHANNEL_INTERCEPTOR_MAPPING = (
    ("intercept_unary_unary", "_unary_unary_interceptors"),
    ("intercept_unary_stream", "_unary_stream_interceptors"),
    ("intercept_stream_unary", "_stream_unary_interceptors"),
    ("intercept_stream_stream", "_stream_stream_interceptors"),
)


def apply_otel_async_channel_interceptors(
    channel: Any,
    client_options: ClientOptions | dict[str, Any] | Sequence[Any] | None = None,
) -> Any:
    """Creates and attaches OpenTelemetry client interceptors to the front of an async gRPC channel.

    In grpc.aio, channels maintain internal interceptor lists evaluated in index order.
    To ensure Google Cloud SDK telemetry wraps outside downstream interceptors and
    suppresses ambient generic auto-instrumentation, our interceptors are prepended
    to the front of the channel's interceptor lists.

    Args:
        channel: The async gRPC channel to intercept.
        client_options (Optional[Union[ClientOptions, dict[str, Any], Sequence[Any]]]): The client
            options used to resolve feature flags and tracer provider, or a sequence of
            pre-resolved interceptors.

    Returns:
        The channel with interceptors prepended to its internal lists,
        or the original channel if tracing is disabled or not installed.
    """
    otel_interceptors: Sequence[Any] | None
    if isinstance(client_options, (ClientOptions, dict)) or client_options is None:
        otel_interceptors = get_otel_async_interceptor(client_options)
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
        standard_methods = tuple(method for method, _ in _CHANNEL_INTERCEPTOR_MAPPING)
        fallback_items = [
            i
            for i in interceptor_list
            if not any(hasattr(i, m) for m in standard_methods) and i not in unary_list
        ]
        if fallback_items:
            unary_list[:0] = fallback_items

    return channel


_TRACE_CONTEXT_PROPAGATOR: Any = None


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

    def record_response(self, response: Any) -> None:
        """Record HTTP response attributes on the active span.

        Args:
            response (Any): The HTTP response object (e.g. requests.Response).
        """
        span = self._span
        if span is None or not hasattr(span, "set_attribute"):
            return

        try:
            from opentelemetry.trace.status import (  # type: ignore[import-not-found]
                Status,
                StatusCode,
            )

            status_code = getattr(
                response, "status_code", getattr(response, "status", None)
            )
            if status_code is not None:
                code_int = int(status_code)
                span.set_attribute("http.response.status_code", code_int)
                if self._parent_span is not None:
                    self._parent_span.set_attribute(
                        "http.response.status_code", code_int
                    )
                if code_int >= 400:
                    span.set_status(Status(StatusCode.ERROR))
                    span.set_attribute("error.type", str(code_int))
                    error_msg = self._extract_http_error_message(response)
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
            elif hasattr(response, "_content") and response._content is not None:
                try:
                    span.set_attribute(
                        "http.response.body.size", len(response._content)
                    )
                except Exception:
                    pass
        except Exception:
            pass

    # Alias for method name parity with Daniel's suggested convention
    record_http_response = record_response

    def record_error(self, exc: BaseException | None) -> None:
        """Record supplemental Cloud Observability error attributes on the active span.

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
            exc (Optional[BaseException]): The exception raised during dispatch.
        """
        span = self._span
        if span is None or exc is None:
            return

        try:
            if hasattr(span, "set_attribute"):
                status_code = getattr(exc, "code", None) or getattr(
                    exc, "status_code", None
                )
                if status_code:
                    span.set_attribute("error.type", str(status_code))
                else:
                    span.set_attribute("error.type", exc.__class__.__name__)
                msg = str(exc)
                if msg:
                    span.set_attribute("status.message", msg)
        except Exception:  # Fail-open on error attribute extraction failure
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
                if exc_val is not None and self._span is not None:
                    self.record_error(exc_val)
            finally:
                self._cm.__exit__(exc_type, exc_val, exc_tb)
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
        request (Optional[Any]): Bundled HTTP request object with .method, .url, .headers.
        method (Optional[str]): Explicit HTTP method (e.g. "GET", "POST").
        url (Optional[str]): Fully qualified request URL.
        url_template (Optional[str]): Parameterized path template for url.template.
        headers (Optional[dict[str, Any]]): Mutable dictionary of request headers.
        body (Optional[Any]): Request payload (used for body size calculation).
        client_options (Optional[Union[ClientOptions, dict[str, Any]]]): Client options
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
