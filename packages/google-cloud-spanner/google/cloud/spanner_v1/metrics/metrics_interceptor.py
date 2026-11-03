# Copyright 2025 Google LLC
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

"""Interceptor for collecting Cloud Spanner metrics."""

import functools
import inspect
import logging
import re
import threading
from typing import Any, Dict

import grpc
from grpc_interceptor import ClientInterceptor

from .constants import (
    GOOGLE_CLOUD_RESOURCE_KEY,
    SPANNER_METHOD_PREFIX,
    _safe_decode_utf8,
)
from .spanner_metrics_tracer_factory import SpannerMetricsTracerFactory

logger = logging.getLogger(__name__)

_RESOURCE_PATH_PATTERN = re.compile(
    r"^projects/(?P<project>[^/]+)(/instances/(?P<instance>[^/]+))?(/databases/(?P<database>[^/]+))?(/sessions/(?P<session>[^/]+))?.*$"
)

_RESOURCE_KEY_STR = GOOGLE_CLOUD_RESOURCE_KEY
_RESOURCE_KEY_BYTES = GOOGLE_CLOUD_RESOURCE_KEY.encode("utf-8")


@functools.lru_cache(maxsize=64)
def _format_method_name_str(method_str: str) -> str:
    return method_str.removeprefix(SPANNER_METHOD_PREFIX).replace("/", ".")


def _format_method_name(method_name_input: Any) -> str:
    """Format method name to be Spanner.<method_name> with caching."""
    if isinstance(method_name_input, str):
        return _format_method_name_str(method_name_input)
    return _format_method_name_str(_safe_decode_utf8(method_name_input))


@functools.lru_cache(maxsize=128)
def _parse_resource_path_cached(path: str) -> Dict[str, str]:
    """Parse resource path using regex with LRU caching."""
    match = _RESOURCE_PATH_PATTERN.match(path)
    if match:
        return {
            key: value for key, value in match.groupdict().items() if value is not None
        }
    return {}


class MetricsInterceptor(ClientInterceptor):
    """Interceptor that collects metrics for Cloud Spanner operations."""

    @staticmethod
    def _parse_resource_path(path: str) -> dict:
        """Parse the resource path to extract project, instance and database.

        Args:
            path (str): The resource path from the request

        Returns:
            dict: Extracted resource components
        """
        if not path or not isinstance(path, str):
            return {}

        return _parse_resource_path_cached(path).copy()

    @staticmethod
    def _extract_resource_from_path(metadata: Any) -> Dict[str, str]:
        """
        Extracts resource information from the metadata based on the path.

        Args:
            metadata (Any): A sequence or dictionary containing metadata information.

        Returns:
            Dict[str, str]: A dictionary containing extracted project, instance, and database information.
        """
        if not metadata:
            return {}

        path = ""
        if isinstance(metadata, dict):
            raw_path = metadata.get(_RESOURCE_KEY_STR) or metadata.get(
                _RESOURCE_KEY_BYTES
            )
            if raw_path is not None:
                path = _safe_decode_utf8(raw_path)
        else:
            try:
                metadata_iter = iter(metadata)
            except TypeError:
                return {}
            for item in metadata_iter:
                if not (isinstance(item, (list, tuple)) and len(item) == 2):
                    continue
                key, value = item
                if key == _RESOURCE_KEY_STR or key == _RESOURCE_KEY_BYTES:
                    path = _safe_decode_utf8(value)
                    break

        return MetricsInterceptor._parse_resource_path(path)

    @staticmethod
    def _set_metrics_tracer_attributes(
        resources: Dict[str, str], tracer: Any = None
    ) -> None:
        """
        Sets the metric tracer attributes based on the provided resources.

        This method updates the metric tracer's attributes with the project, instance, and database information extracted from the resources dictionary. If the metric tracer is not set, the method does nothing.

        Args:
            resources (Dict[str, str]): A dictionary containing project, instance, and database information.
            tracer (Any, optional): The metric tracer instance. If not provided, retrieves the current tracer.
        """
        if tracer is None:
            tracer = SpannerMetricsTracerFactory.get_current_tracer()
        if tracer is None:
            return

        if resources:
            if "project" in resources:
                tracer.set_project(resources["project"])
            if "instance" in resources:
                tracer.set_instance(resources["instance"])
            if "database" in resources:
                tracer.set_database(resources["database"])

    @staticmethod
    def _prepare_attempt(tracer: Any, call_details: Any) -> None:
        """Prepare tracer attributes and record attempt start from call details."""
        if not (
            tracer.client_attributes.get("project_id")
            and tracer.client_attributes.get("instance_id")
            and tracer.client_attributes.get("database")
        ):
            resources = MetricsInterceptor._extract_resource_from_path(
                call_details.metadata
            )
            MetricsInterceptor._set_metrics_tracer_attributes(resources, tracer=tracer)

        method_name = _format_method_name(call_details.method)
        tracer.set_method(method_name)
        tracer.record_attempt_start()

    def intercept(self, invoked_method, request_or_iterator, call_details):
        """Intercept gRPC calls to collect metrics.

        Args:
            invoked_method: The RPC method
            request_or_iterator: The RPC request
            call_details: Details about the RPC call

        Returns:
            The RPC response
        """
        factory = SpannerMetricsTracerFactory()
        tracer = SpannerMetricsTracerFactory.get_current_tracer()
        if tracer is None or not factory.enabled:
            return invoked_method(request_or_iterator, call_details)

        self._prepare_attempt(tracer, call_details)
        response = invoked_method(request_or_iterator, call_details)
        return _wrap_response(response, tracer)


def _wrap_response(response: Any, tracer: Any) -> Any:
    """Wraps the response if it is streaming, or records metrics immediately if unary."""
    if hasattr(response, "__next__"):
        return _StreamingResponseWrapper(response, tracer)
    else:
        # Unary call: execute completion and record metrics immediately
        try:
            tracer.record_attempt_completion()
            metadata = []
            if hasattr(response, "initial_metadata"):
                try:
                    metadata.extend(response.initial_metadata() or [])
                except Exception as e:
                    logger.warning(f"Failed to retrieve initial metadata: {e}")
            tracer.record_front_end_metrics(metadata)
        except Exception as e:
            logger.warning(f"Failed to record metrics: {e}")
        return response


class AsyncMetricsInterceptor(
    grpc.aio.UnaryUnaryClientInterceptor,
    grpc.aio.UnaryStreamClientInterceptor,
    grpc.aio.StreamUnaryClientInterceptor,
    grpc.aio.StreamStreamClientInterceptor,
):
    """Async Interceptor that collects metrics for Cloud Spanner operations."""

    async def intercept_unary_unary(self, continuation, client_call_details, request):
        return await self._async_intercept(
            continuation, client_call_details, request, is_streaming=False
        )

    async def intercept_unary_stream(self, continuation, client_call_details, request):
        return await self._async_intercept(
            continuation, client_call_details, request, is_streaming=True
        )

    async def intercept_stream_unary(
        self, continuation, client_call_details, request_iterator
    ):
        return await self._async_intercept(
            continuation, client_call_details, request_iterator, is_streaming=False
        )

    async def intercept_stream_stream(
        self, continuation, client_call_details, request_iterator
    ):
        return await self._async_intercept(
            continuation, client_call_details, request_iterator, is_streaming=True
        )

    async def _async_intercept(
        self,
        continuation: Any,
        call_details: grpc.ClientCallDetails,
        request_or_iterator: Any,
        is_streaming: bool = False,
    ) -> Any:
        # Implementation for async interceptor
        factory = SpannerMetricsTracerFactory()
        tracer = SpannerMetricsTracerFactory.get_current_tracer()
        if tracer is None or not factory.enabled:
            return await continuation(call_details, request_or_iterator)

        MetricsInterceptor._prepare_attempt(tracer, call_details)
        response = await continuation(call_details, request_or_iterator)
        if is_streaming:
            return _AsyncStreamingResponseWrapper(response, tracer)
        return _AsyncUnaryResponseWrapper(response, tracer)


class _StreamingResponseWrapper:
    """Wrapper for streaming RPC response iterators to defer metrics recording."""

    def __init__(self, response, tracer):
        self._response = response
        self._tracer = tracer
        self._metrics_recorded = False
        self._iterator = None
        self._lock = threading.Lock()

    def __iter__(self):
        self._iterator = iter(self._response)
        return self

    def __next__(self):
        if self._iterator is None:
            self._iterator = iter(self._response)
        try:
            return next(self._iterator)
        except StopIteration:
            self._record_metrics()
            raise
        except Exception:
            self._record_metrics()
            raise

    def _record_metrics(self):
        with self._lock:
            if self._metrics_recorded:
                return
            self._metrics_recorded = True
        try:
            # TODO: Extract and pass the actual gRPC status (e.g. from self._response.code()
            # or caught exceptions) to record_attempt_completion instead of defaulting to OK.
            self._tracer.record_attempt_completion()
            metadata = []
            if hasattr(self._response, "initial_metadata"):
                try:
                    metadata.extend(self._response.initial_metadata() or [])
                except Exception as e:
                    logger.warning(f"Failed to retrieve initial metadata: {e}")
            self._tracer.record_front_end_metrics(metadata)
        except Exception as e:
            logger.warning(f"Failed to record metrics: {e}")

    def cancel(self, *args, **kwargs):
        cancelled = None
        if hasattr(self._response, "cancel"):
            cancelled = self._response.cancel(*args, **kwargs)
        if cancelled is not False:
            with self._lock:
                if self._metrics_recorded:
                    return cancelled
                self._metrics_recorded = True
            try:
                self._tracer.record_attempt_completion(
                    status=grpc.StatusCode.CANCELLED.name
                )
                metadata = []
                if hasattr(self._response, "initial_metadata"):
                    try:
                        metadata.extend(self._response.initial_metadata() or [])
                    except Exception:
                        pass
                if metadata:
                    self._tracer.record_front_end_metrics(metadata)
            except Exception as e:
                logger.warning(f"Failed to record metrics on cancel: {e}")
        return cancelled

    def __del__(self):
        with self._lock:
            if self._metrics_recorded:
                return
            self._metrics_recorded = True
        try:
            self._tracer.record_attempt_completion(
                status=grpc.StatusCode.CANCELLED.name
            )
        except Exception:
            pass

    def __getattr__(self, name):
        return getattr(self._response, name)


class _BaseAsyncResponseWrapper:
    """Base wrapper for async RPC responses to defer metrics recording."""

    def __init__(self, response, tracer):
        self._response = response
        self._tracer = tracer
        self._metrics_recorded = False
        self._lock = threading.Lock()

    def add_done_callback(self, *args, **kwargs):
        return getattr(self._response, "add_done_callback")(*args, **kwargs)

    def cancel(self, *args, **kwargs):
        cancel_fn = getattr(self._response, "cancel", None)
        cancelled = cancel_fn(*args, **kwargs) if cancel_fn else True
        if cancelled is not False:
            with self._lock:
                if self._metrics_recorded:
                    return cancelled
                self._metrics_recorded = True
            try:
                self._tracer.record_attempt_completion(
                    status=grpc.StatusCode.CANCELLED.name
                )
                metadata = []
                if hasattr(self._response, "initial_metadata"):
                    try:
                        metadata_result = self._response.initial_metadata()
                        if inspect.isawaitable(metadata_result):
                            getattr(metadata_result, "close", lambda: None)()
                        else:
                            metadata.extend(metadata_result or [])
                    except Exception as e:
                        logger.warning(
                            f"Failed to retrieve initial metadata on cancel: {e}"
                        )
                if metadata:
                    self._tracer.record_front_end_metrics(metadata)
            except Exception as e:
                logger.warning(f"Failed to record metrics on cancel: {e}")
        return cancelled

    def cancelled(self, *args, **kwargs):
        return getattr(self._response, "cancelled")(*args, **kwargs)

    def code(self, *args, **kwargs):
        return getattr(self._response, "code")(*args, **kwargs)

    def details(self, *args, **kwargs):
        return getattr(self._response, "details")(*args, **kwargs)

    def done(self, *args, **kwargs):
        return getattr(self._response, "done")(*args, **kwargs)

    def initial_metadata(self, *args, **kwargs):
        return getattr(self._response, "initial_metadata")(*args, **kwargs)

    def time_remaining(self, *args, **kwargs):
        return getattr(self._response, "time_remaining")(*args, **kwargs)

    def trailing_metadata(self, *args, **kwargs):
        return getattr(self._response, "trailing_metadata")(*args, **kwargs)

    def wait_for_connection(self, *args, **kwargs):
        return getattr(self._response, "wait_for_connection")(*args, **kwargs)

    def write(self, *args, **kwargs):
        return getattr(self._response, "write")(*args, **kwargs)

    def done_writing(self, *args, **kwargs):
        return getattr(self._response, "done_writing")(*args, **kwargs)

    async def _record_metrics(self):
        with self._lock:
            if self._metrics_recorded:
                return
            self._metrics_recorded = True
        try:
            # TODO: Extract and pass the actual gRPC status (e.g. from self._response.code()
            # or caught exceptions) to record_attempt_completion instead of defaulting to OK.
            self._tracer.record_attempt_completion()
            metadata = []
            if hasattr(self._response, "initial_metadata"):
                try:
                    metadata_result = self._response.initial_metadata()
                    if inspect.isawaitable(metadata_result):
                        metadata_result = await metadata_result
                    metadata.extend(metadata_result or [])
                except Exception as e:
                    logger.warning(f"Failed to retrieve initial metadata: {e}")
            self._tracer.record_front_end_metrics(metadata)
        except Exception as e:
            logger.warning(f"Failed to record metrics: {e}")

    def __del__(self):
        with self._lock:
            if self._metrics_recorded:
                return
            self._metrics_recorded = True
        try:
            self._tracer.record_attempt_completion(
                status=grpc.StatusCode.CANCELLED.name
            )
        except Exception:
            pass

    def __getattr__(self, name):
        return getattr(self._response, name)


class _AsyncUnaryResponseWrapper(
    _BaseAsyncResponseWrapper,
    grpc.aio.UnaryUnaryCall,
    grpc.aio.StreamUnaryCall,
):
    """Wrapper for async unary RPC response to defer metrics recording until awaited."""

    def __await__(self):
        async def _wait():
            try:
                return await self._response
            finally:
                await self._record_metrics()

        return _wait().__await__()


class _AsyncStreamingResponseWrapper(
    _BaseAsyncResponseWrapper,
    grpc.aio.UnaryStreamCall,
    grpc.aio.StreamStreamCall,
):
    """Wrapper for async streaming RPC response iterators to defer metrics recording."""

    def __init__(self, response, tracer):
        super().__init__(response, tracer)
        self._iterator = None

    def read(self, *args, **kwargs):
        return getattr(self._response, "read")(*args, **kwargs)

    def __aiter__(self):
        if hasattr(self._response, "__aiter__"):
            self._iterator = self._response.__aiter__()
        else:
            self._iterator = self._response
        return self

    async def __anext__(self):
        if self._iterator is None:
            if hasattr(self._response, "__aiter__"):
                self._iterator = self._response.__aiter__()
            else:
                self._iterator = self._response
        try:
            return await self._iterator.__anext__()
        except StopAsyncIteration:
            await self._record_metrics()
            raise
        except Exception:
            await self._record_metrics()
            raise
