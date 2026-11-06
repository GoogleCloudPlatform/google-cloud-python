# Copyright 2017 Google LLC
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

"""Helpers for wrapping low-level gRPC methods with common functionality.

This is used by gapic clients to provide common error mapping, retry, timeout,
compression, pagination, and long-running operations to gRPC methods.
"""

from __future__ import annotations

import contextlib
import enum
import functools
from typing import List, Tuple

from google.api_core import _observability, grpc_helpers
from google.api_core.gapic_v1 import client_info
from google.api_core.gapic_v1.client_info import METRICS_METADATA_KEY
from google.api_core.timeout import TimeToDeadlineTimeout

USE_DEFAULT_METADATA = object()


class _MethodDefault(enum.Enum):
    # Uses enum so that pytype/mypy knows that this is the only possible value.
    # https://stackoverflow.com/a/60605919/101923
    _DEFAULT_VALUE = object()


DEFAULT = _MethodDefault._DEFAULT_VALUE
"""Sentinel value indicating that a retry, timeout, or compression argument was unspecified,
so the default should be used."""

_TRANSPORT_KIND_GRPC = "grpc"
_TRANSPORT_KIND_REST = "rest"
_DEFAULT_TRANSPORT_KIND = _TRANSPORT_KIND_GRPC


def _is_not_none_or_false(value):
    return value is not None and value is not False


def _apply_decorators(func, decorators):
    """Apply a list of decorators to a given function.

    ``decorators`` may contain items that are ``None`` or ``False`` which will
    be ignored.
    """
    filtered_decorators = filter(_is_not_none_or_false, reversed(decorators))

    for decorator in filtered_decorators:
        func = decorator(func)

    return func


def _deduplicate_metadata_tokens(*headers: str | None) -> str:
    """
    Given one or more metadata payload strings, create a combined
    string with deduplicated tokens, while preserving token order.

    Inputs are expected to contain a set of metadata tokens separated by spaces
    Example: `gl-python/3.14.0 grpc/1.76.0 gax/2.29.0 gapic/3.8.0 pb/6.33.4`

    Args:
      *headers: one or more metadata payload strings

    Returns:
        a single combined payload string
    """
    # Split all non-empty headers into individual tokens
    token_list = " ".join(filter(None, headers)).split()
    # Deduplicate while preserving order
    return " ".join(dict.fromkeys(token_list))


def _extract_metrics_header(metadata) -> Tuple[str, List[Tuple[str, str]]]:
    """Extract x-google-api-client header from metadata list.

    Args:
        metadata (Sequence[Tuple[str, str]]): The metadata to extract from.

    Returns:
        A tuple containing:
            - a string representing the header value.
            - A sequence of remaining metadata tuples.
    """
    if not metadata:
        return "", []

    key_to_find = METRICS_METADATA_KEY

    metric_str = _deduplicate_metadata_tokens(
        " ".join([v for k, v in metadata if k == key_to_find])
    )
    if not metric_str:
        return "", list(metadata)

    arbitrary_metadata = [item for item in metadata if item[0] != key_to_find]
    return metric_str, arbitrary_metadata


class _GapicCallable(object):
    """Callable that applies retry, timeout, and metadata logic.

    Args:
        target (Callable): The low-level RPC method.
        retry (google.api_core.retry.Retry): The default retry for the
            callable. If ``None``, this callable will not retry by default
        timeout (google.api_core.timeout.Timeout): The default timeout for the
            callable (i.e. duration of time within which an RPC must terminate
            after its start, not to be confused with deadline). If ``None``,
            this callable will not specify a timeout argument to the low-level
            RPC method.
        compression (grpc.Compression): The default compression for the callable.
            If ``None``, this callable will not specify a compression argument
            to the low-level RPC method.
        metadata (Sequence[Tuple[str, str]]): Additional metadata that is
            provided to the RPC method on every invocation. This is merged with
            any metadata specified during invocation. If ``None``, no
            additional metadata will be passed to the RPC method.
        client_options
            (Optional[google.api_core.client_options.ClientOptions]):
                Client options used to configure client-level behavior, such as
                custom OpenTelemetry tracer providers. Defaults to None.
        method_name (Optional[str]): The optional explicit full RPC method name
            (e.g. "/google.cloud.secretmanager.v1.SecretManagerService/AccessSecretVersion").
        is_streaming (bool): Whether the RPC method is streaming. Defaults to False.
            Note: Streaming methods do not currently generate Tier 3 observability spans.
        client_info (Optional[google.api_core.gapic_v1.client_info.ClientInfo]):
            Client information used for metadata headers. Defaults to None.
        kind (str): The transport kind for the RPC method. Defaults to "grpc".
            Allowed values for OpenTelemetry method tracing are "grpc" and "rest".
        default_host (Optional[str]): Fallback transport host when ``api_endpoint``
            is not set on ``client_options``. Defaults to None.
    """

    _SUPPORTED_TRACING_KINDS = (_TRANSPORT_KIND_GRPC, _TRANSPORT_KIND_REST)

    def __init__(
        self,
        target,
        retry,
        timeout,
        compression,
        metadata=None,
        client_options=None,
        method_name=None,
        is_streaming=False,
        client_info=None,
        kind=_DEFAULT_TRANSPORT_KIND,
        default_host=None,
    ):
        self._target = target
        self._retry = retry
        self._timeout = timeout
        self._compression = compression
        self._client_options = client_options
        self._method_name = method_name
        self._rpc_system = _observability._resolve_rpc_system(kind)

        # Pre-extract the x-goog-api-client header from the initialized metadata.
        self._x_goog_api_client, remaining = _extract_metrics_header(metadata)
        self._static_metadata = tuple(remaining)
        if self._x_goog_api_client:
            self._default_metadata = (
                (METRICS_METADATA_KEY, self._x_goog_api_client),
                *self._static_metadata,
            )
        else:
            self._default_metadata = self._static_metadata

        # Configure the OpenTelemetry span factory once at initialization.
        # For now, method tracing is gated to non-streaming calls where an explicit method_name is provided.
        self._start_span_fn = None
        if (
            not is_streaming
            and kind in self._SUPPORTED_TRACING_KINDS
            and method_name is not None
            and _observability.is_otel_capabilities_enabled(client_options)
        ):
            try:
                from opentelemetry import trace

                tracer_provider = _observability._get_tracer_provider(client_options)
                if tracer_provider is not None:
                    tracer = tracer_provider.get_tracer("google.api_core")
                else:
                    tracer = trace.get_tracer("google.api_core")

                span_name, _, _ = _observability.extract_rpc_identity(method_name)
                endpoint_attrs = _observability._extract_endpoint_attributes(
                    client_options, default_host=default_host
                )
                span_attributes = {
                    "rpc.system.name": self._rpc_system,
                    "rpc.method": span_name,
                    **endpoint_attrs,
                }
                self._start_span_fn = functools.partial(
                    tracer.start_as_current_span,
                    span_name,
                    kind=trace.SpanKind.INTERNAL,
                    attributes=span_attributes,
                )
            except (ImportError, AttributeError, TypeError):
                # Gracefully disable tracing if OpenTelemetry or custom provider fails
                self._start_span_fn = None

    def _prepare_call(self, timeout, retry, compression, kwargs):
        if retry is DEFAULT:
            retry = self._retry

        if timeout is DEFAULT:
            timeout = self._timeout

        if compression is DEFAULT:
            compression = self._compression

        if isinstance(timeout, (int, float)):
            timeout = TimeToDeadlineTimeout(timeout=timeout)

        # Apply all applicable decorators.
        wrapped_func = _apply_decorators(self._target, [retry, timeout])

        if user_metadata := kwargs.get("metadata"):
            # Add the user agent metadata to the call.
            final_metadata = list(self._static_metadata)
            user_x_goog, remaining = _extract_metrics_header(user_metadata)

            merged_header = _deduplicate_metadata_tokens(
                self._x_goog_api_client, user_x_goog
            )
            if merged_header:
                final_metadata.append((METRICS_METADATA_KEY, merged_header))
            final_metadata.extend(remaining)
            kwargs["metadata"] = final_metadata
        elif self._default_metadata:
            kwargs["metadata"] = self._default_metadata

        if compression is not None:
            kwargs["compression"] = compression

        return wrapped_func

    @contextlib.contextmanager
    def _trace_span(self):
        span_cm = contextlib.nullcontext()
        if self._start_span_fn is not None:
            try:
                span_cm = self._start_span_fn()
            except Exception:
                # Fail-open: proceed without span if tracing initialization fails
                span_cm = contextlib.nullcontext()

        with span_cm as span:
            try:
                yield
                if span is not None and hasattr(span, "set_attribute"):
                    span.set_attribute("rpc.response.status_code", "OK")
            except (KeyboardInterrupt, SystemExit, GeneratorExit):
                raise
            except BaseException as exc:
                if span is not None and hasattr(span, "set_attribute"):
                    for k, v in _observability.build_telemetry_error_attributes(
                        exc
                    ).items():
                        span.set_attribute(k, v)
                raise

    def __call__(
        self, *args, timeout=DEFAULT, retry=DEFAULT, compression=DEFAULT, **kwargs
    ):
        """Invoke the low-level RPC with retry, timeout, compression, and metadata."""
        wrapped_func = self._prepare_call(timeout, retry, compression, kwargs)
        with self._trace_span():
            return wrapped_func(*args, **kwargs)


def wrap_method(
    func,
    default_retry=None,
    default_timeout=None,
    default_compression=None,
    client_info=client_info.DEFAULT_CLIENT_INFO,
    *,
    with_call=False,
    client_options=None,
    method_name=None,
    is_streaming=False,
    kind=_DEFAULT_TRANSPORT_KIND,
    default_host=None,
):
    """Wrap an RPC method with common behavior.

    This applies common error wrapping, retry, timeout, and compression behavior to a function.
    The wrapped function will take optional ``retry``, ``timeout``, and ``compression``
    arguments.

    For example::

        import google.api_core.gapic_v1.method
        from google.api_core import retry
        from google.api_core import timeout
        from grpc import Compression

        # The original RPC method.
        def get_topic(name, timeout=None):
            request = publisher_v2.GetTopicRequest(name=name)
            return publisher_stub.GetTopic(request, timeout=timeout)

        default_retry = retry.Retry(deadline=60)
        default_timeout = timeout.Timeout(deadline=60)
        default_compression = Compression.NoCompression
        wrapped_get_topic = google.api_core.gapic_v1.method.wrap_method(
            get_topic, default_retry)

        # Execute get_topic with default retry and timeout:
        response = wrapped_get_topic()

        # Execute get_topic without doing any retying but with the default
        # timeout:
        response = wrapped_get_topic(retry=None)

        # Execute get_topic but only retry on 5xx errors:
        my_retry = retry.Retry(retry.if_exception_type(
            exceptions.InternalServerError))
        response = wrapped_get_topic(retry=my_retry)

    The way this works is by late-wrapping the given function with the retry
    and timeout decorators. Essentially, when ``wrapped_get_topic()`` is
    called:

    * ``get_topic()`` is first wrapped with the ``timeout`` into
      ``get_topic_with_timeout``.
    * ``get_topic_with_timeout`` is wrapped with the ``retry`` into
      ``get_topic_with_timeout_and_retry()``.
    * The final ``get_topic_with_timeout_and_retry`` is called passing through
      the ``args``  and ``kwargs``.

    The callstack is therefore::

        method.__call__() ->
            Retry.__call__() ->
                Timeout.__call__() ->
                    wrap_errors() ->
                        get_topic()

    Note that if ``timeout`` or ``retry`` is ``None``, then they are not
    applied to the function. For example,
    ``wrapped_get_topic(timeout=None, retry=None)`` is more or less
    equivalent to just calling ``get_topic`` but with error re-mapping.

    Args:
        func (Callable[Any]): The function to wrap. It should accept an
            optional ``timeout`` argument. If ``metadata`` is not ``None``, it
            should accept a ``metadata`` argument.
        default_retry (Optional[google.api_core.Retry]): The default retry
            strategy. If ``None``, the method will not retry by default.
        default_timeout (Optional[google.api_core.Timeout]): The default
            timeout strategy. Can also be specified as an int or float. If
            ``None``, the method will not have timeout specified by default.
        default_compression (Optional[grpc.Compression]): The default
            grpc.Compression. If ``None``, the method will not have
            compression specified by default.
        client_info
            (Optional[google.api_core.gapic_v1.client_info.ClientInfo]):
                Client information used to create a user-agent string that's
                passed as gRPC metadata to the method. If unspecified, then
                a sane default will be used. If ``None``, then no user agent
                metadata will be provided to the RPC method.
        with_call (bool): If True, wrapped grpc.UnaryUnaryMulticallables will
            return a tuple of (response, grpc.Call) instead of just the response.
            This is useful for extracting trailing metadata from unary calls.
            Defaults to False.
        client_options
            (Optional[google.api_core.client_options.ClientOptions]):
                Client options used to configure client-level behavior, such as
                custom OpenTelemetry tracer providers. Defaults to None.
        method_name (Optional[str]): Optional explicit full RPC method name
            (e.g. "/google.cloud.secretmanager.v1.SecretManagerService/AccessSecretVersion").
            Used to identify the RPC for observability.
        is_streaming (bool): Whether the RPC method is streaming. Defaults to False.
            Streaming methods are currently gated and do not generate Tier 3 spans.
        kind (str): The transport kind for the RPC method. Defaults to "grpc".
            Allowed values for OpenTelemetry method tracing are "grpc" and "rest".
        default_host (Optional[str]): Fallback transport host when ``api_endpoint``
            is not set on ``client_options``. Defaults to None.

    Returns:
        Callable: A new callable that takes optional ``retry``, ``timeout``,
            and ``compression``
            arguments and applies the common error mapping, retry, timeout, compression,
            and metadata behavior to the low-level RPC method.
    """
    if with_call:
        try:
            func = func.with_call
        except AttributeError as exc:
            raise ValueError(
                "with_call=True is only supported for unary calls."
            ) from exc
    func = grpc_helpers.wrap_errors(func)
    if client_info is not None:
        user_agent_metadata = [client_info.to_grpc_metadata()]
    else:
        user_agent_metadata = None

    return functools.wraps(func)(
        _GapicCallable(
            func,
            default_retry,
            default_timeout,
            default_compression,
            metadata=user_agent_metadata,
            client_options=client_options,
            method_name=method_name,
            is_streaming=is_streaming,
            client_info=client_info,
            kind=kind,
            default_host=default_host,
        )
    )
