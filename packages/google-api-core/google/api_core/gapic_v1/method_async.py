# Copyright 2020 Google LLC
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
"""AsyncIO helpers for wrapping gRPC and REST methods with common functionality.

This is used by gapic clients to provide common error mapping, retry, timeout,
compression, pagination, and long-running operations to methods.
"""

import functools
import inspect

from google.api_core import grpc_helpers_async
from google.api_core.gapic_v1 import client_info
from google.api_core.gapic_v1.method import (  # noqa: F401
    DEFAULT,
    USE_DEFAULT_METADATA,
    _GapicCallable,
)

_TRANSPORT_KIND_GRPC_ASYNC = "grpc_asyncio"
_TRANSPORT_KIND_REST_ASYNC = "rest_asyncio"
_DEFAULT_ASYNC_TRANSPORT_KIND = _TRANSPORT_KIND_GRPC_ASYNC


class _AsyncGapicCallable(_GapicCallable):
    """Async callable object that wraps an async RPC method with retry, timeout, metadata, and tracing."""

    _SUPPORTED_TRACING_KINDS = (
        _TRANSPORT_KIND_GRPC_ASYNC,
        _TRANSPORT_KIND_REST_ASYNC,
    )

    async def __call__(
        self, *args, timeout=DEFAULT, retry=DEFAULT, compression=DEFAULT, **kwargs
    ):
        """Invoke the low-level async RPC with retry, timeout, compression, and metadata."""
        wrapped_func = self._prepare_call(timeout, retry, compression, kwargs)
        with self._trace_span():
            res = wrapped_func(*args, **kwargs)
            if inspect.isawaitable(res):
                return await res
            return res


def wrap_method(
    func,
    default_retry=None,
    default_timeout=None,
    default_compression=None,
    client_info=client_info.DEFAULT_CLIENT_INFO,
    kind=_DEFAULT_ASYNC_TRANSPORT_KIND,
    *,
    client_options=None,
    method_name=None,
    is_streaming=False,
):
    """Wrap an async RPC method with common behavior.

    Args:
        func (Callable): The low-level async RPC method.
        default_retry (Optional[google.api_core.retry_async.AsyncRetry]): The default
            retry strategy. If ``None``, the method will not retry by default.
        default_timeout (Optional[Union[google.api_core.timeout.Timeout, float]]): The
            default timeout strategy. Can also be specified as an int or float. If
            ``None``, the method will not have a timeout specified by default.
        default_compression (Optional[grpc.Compression]): The default
            grpc.Compression. If ``None``, the method will not have
            compression specified by default.
        client_info (Optional[google.api_core.gapic_v1.client_info.ClientInfo]):
            Client information used to create a user-agent string that's
            passed as gRPC metadata to the method. If unspecified, then
            a sane default will be used. If ``None``, then no user agent
            metadata will be provided to the RPC method.
        kind (str): The transport kind for the RPC method. Defaults to "grpc_asyncio".
            Allowed values for OpenTelemetry method tracing are "grpc_asyncio" and "rest_asyncio".
        client_options
            (Optional[google.api_core.client_options.ClientOptions]):
                Client options used to configure client-level behavior, such as
                custom OpenTelemetry tracer providers. Defaults to None.
        method_name (Optional[str]): Optional explicit full RPC method name
            (e.g. "/google.cloud.secretmanager.v1.SecretManagerService/AccessSecretVersion").
            Used to identify the RPC for observability.
        is_streaming (bool): Whether the RPC method is streaming. Defaults to False.
            Streaming methods are currently gated and do not generate Tier 3 spans.

    Returns:
        Callable: A new callable that takes optional ``retry``, ``timeout``,
            and ``compression`` arguments and applies the common error mapping,
            retry, timeout, metadata, and compression behavior to the low-level RPC method.
    """
    if kind == _DEFAULT_ASYNC_TRANSPORT_KIND:
        func = grpc_helpers_async.wrap_errors(func)

    metadata = [client_info.to_grpc_metadata()] if client_info is not None else None

    return functools.wraps(func)(
        _AsyncGapicCallable(
            func,
            default_retry,
            default_timeout,
            default_compression,
            metadata=metadata,
            client_options=client_options,
            method_name=method_name,
            is_streaming=is_streaming,
            client_info=client_info,
            kind=kind,
        )
    )
