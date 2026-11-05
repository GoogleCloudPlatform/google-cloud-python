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

"""An async client for interacting with Google Cloud Storage using the gRPC API."""

import asyncio
import ipaddress
import re
import time
from collections import deque
from typing import Any, Iterator, Optional, Tuple

import grpc
from google.auth import credentials as auth_credentials

from google.cloud import _storage_v2 as storage_v2
from google.cloud._storage_v2.services.storage.transports.base import (
    DEFAULT_CLIENT_INFO,
)
from google.cloud.storage import __version__, _opentelemetry_metrics
from google.cloud.storage._bucket_metadata_cache import BucketMetadataCache
from google.cloud.storage._helpers import create_trace_span_helper
from google.cloud.storage.asyncio import _utils
from google.cloud.storage.grpc_client import (
    _DEFAULT_HOST,
    _resolve_direct_path_interconnect,
    _rewrite_host_for_interconnect,
)

_GRPC_STATUS_NAMES = {sc.name for sc in grpc.StatusCode}
_DIRECTPATH_IPV4_NET = ipaddress.ip_network("34.126.0.0/18")
_DIRECTPATH_IPV6_NET = ipaddress.ip_network("2001:4860:8040::/42")
_GFE_METADATA_KEYS = frozenset({"x-goog-gfe-service-time", "x-guploader-uploadid"})
_PEER_IP_RE = re.compile(
    r"ipv4:([0-9.]+)|ipv6:(?:(?:\[|%5B|%5b)([0-9a-fA-F:.]+)(?:\]|%5D|%5d)|([0-9a-fA-F:]+))"
)


def _extract_rpc_method(method_name: Any) -> str:
    """Normalizes a gRPC method path into ``package.Service/Method``."""
    if isinstance(method_name, bytes):
        method_name = method_name.decode("utf-8", errors="replace")
    if not isinstance(method_name, str):
        return "UNKNOWN"
    normalized = method_name.strip().strip("/")
    return normalized if normalized else "UNKNOWN"


_extract_rpc_operation = _extract_rpc_method


def _extract_logical_operation(rpc_method: str) -> str:
    """Extracts the short logical ``gcp.storage.operation`` from a gRPC method path."""
    return _opentelemetry_metrics.normalize_logical_operation(rpc_method)


def _resolve_status_and_error(exc: BaseException) -> Tuple[Optional[str], str]:
    """Resolves ``(rpc.response.status_code, error.type)`` from an exception."""
    if isinstance(exc, asyncio.CancelledError):
        return "CANCELLED", "CANCELLED"

    status_code: Optional[str] = None
    for item in _opentelemetry_metrics._iter_exception_chain(exc):
        grpc_code = getattr(item, "grpc_status_code", None)
        if grpc_code is not None:
            name = getattr(grpc_code, "name", None)
            status_code = str(name) if name else str(grpc_code)
            break

        code_attr = getattr(item, "code", None)
        if callable(code_attr):
            try:
                rpc_status = code_attr()
                name = getattr(rpc_status, "name", None)
                if name:
                    status_code = str(name)
                    break
            except Exception:  # pragma: NO COVER
                pass

    error_type = _opentelemetry_metrics.classify_error_type(exc)
    if status_code is None and error_type in _GRPC_STATUS_NAMES:
        status_code = error_type
    return status_code, error_type


def _extract_peer_ip(text: str) -> Optional[str]:
    """Extracts the last valid peer IPv4/IPv6 address from a gRPC peer or debug string."""
    last_valid: Optional[str] = None
    for match in _PEER_IP_RE.finditer(text):
        candidate = match.group(1) or match.group(2) or match.group(3)
        try:
            ipaddress.ip_address(candidate)
            last_valid = candidate
        except ValueError:
            continue
    return last_valid


def _classify_ip(ip_str: str) -> str:
    """Classifies a validated IP address string into ``'directpath'`` or ``'cloudpath'``."""
    addr = ipaddress.ip_address(ip_str)
    if isinstance(addr, ipaddress.IPv6Address) and addr.ipv4_mapped is not None:
        addr = addr.ipv4_mapped
    if isinstance(addr, ipaddress.IPv4Address):
        return "directpath" if addr in _DIRECTPATH_IPV4_NET else "cloudpath"
    return "directpath" if addr in _DIRECTPATH_IPV6_NET else "cloudpath"


def _inspect_metadata(md: Any) -> Tuple[bool, bool]:
    """Inspects a gRPC metadata sequence for non-empty headers and GFE markers."""
    if not isinstance(md, (tuple, list, grpc.aio.Metadata)):
        return False, False
    has_entries = False
    for entry in md:
        has_entries = True
        key = getattr(entry, "key", None)
        if key is None and isinstance(entry, (tuple, list)) and len(entry) >= 1:
            key = entry[0]
        if isinstance(key, bytes):
            key = key.decode("utf-8", errors="replace")
        if isinstance(key, str) and key.lower() in _GFE_METADATA_KEYS:
            return True, True
    return has_entries, False


def _iter_wrapped_calls(call: Any) -> Iterator[Any]:
    """Yields ``call`` and any inner wrapped gRPC call objects."""
    seen = set()
    queue = deque([call])
    steps = 0
    while queue and steps < 16:
        steps += 1
        current = queue.popleft()
        if current is None or id(current) in seen:
            continue
        seen.add(id(current))
        yield current
        inst_dict = getattr(current, "__dict__", None)
        if not isinstance(inst_dict, dict):
            continue
        for attr in (
            "_call",
            "call",
            "_wrapped",
            "_last_returned_call_from_interceptors",
        ):
            inner = inst_dict.get(attr)
            if inner is not None:
                queue.append(inner)
        task = inst_dict.get("_interceptors_task")
        if task is not None and hasattr(task, "done") and task.done():
            try:
                queue.append(task.result())
            except Exception:  # pragma: NO COVER
                pass


def _resolve_network_path(
    call: Any = None,
    exc: Optional[BaseException] = None,
    direct_path_attempted: Optional[bool] = None,
    received_server_response: bool = False,
) -> str:
    """Resolves per-call ``network.path`` (``'directpath'``, ``'cloudpath'``, or ``'unknown'``).

    Detection priority:
    1. GFE response metadata headers (``x-goog-gfe-service-time``,
       ``x-guploader-uploadid``) on the Cython call or ``RpcError`` -> ``'cloudpath'``.
    2. Remote peer IP from ``call.peer()`` or C-core ``debug_error_string()``
       matched against DirectPath CIDRs ``34.126.0.0/18`` and
       ``2001:4860:8040::/42`` -> ``'directpath'`` or ``'cloudpath'``.
    3. Fallback when Python ``grpc.aio`` hides ``peer()`` and no GFE header is
       present: if the server responded, ``'directpath'`` when DirectPath was
       attempted on the channel else ``'cloudpath'``; if no server response was
       received (e.g. DNS or pre-connection failure), ``'unknown'``.
    """
    has_server_metadata = False
    detected_peer_ip: Optional[str] = None

    if call is not None:
        for current in _iter_wrapped_calls(call):
            if direct_path_attempted is None and isinstance(current, _TrackedCallBase):
                direct_path_attempted = current._direct_path_attempted

            inst_dict = getattr(current, "__dict__", None)
            cython_call = getattr(current, "_cython_call", None)
            status_obj = (
                getattr(cython_call, "_status", None)
                if cython_call is not None
                else None
            )
            status_trailing = None
            if status_obj is not None:
                trailing_fn = getattr(status_obj, "trailing_metadata", None)
                status_trailing = (
                    trailing_fn()
                    if callable(trailing_fn)
                    else getattr(status_obj, "_trailing_metadata", None)
                )

            md_candidates = [
                getattr(cython_call, "_initial_metadata", None)
                if cython_call is not None
                else None,
                getattr(cython_call, "_trailing_metadata", None)
                if cython_call is not None
                else None,
                status_trailing,
                inst_dict.get("_initial_metadata")
                if isinstance(inst_dict, dict)
                else None,
                inst_dict.get("_trailing_metadata")
                if isinstance(inst_dict, dict)
                else None,
            ]
            for md in md_candidates:
                entries, is_gfe = _inspect_metadata(md)
                if is_gfe:
                    return "cloudpath"
                if entries:
                    has_server_metadata = True

            if detected_peer_ip is None:
                peer_fn = getattr(current, "peer", None)
                if callable(peer_fn):
                    try:
                        peer_val = peer_fn()
                        if isinstance(peer_val, bytes):
                            peer_val = peer_val.decode("utf-8", errors="replace")
                        if isinstance(peer_val, str):
                            detected_peer_ip = _extract_peer_ip(peer_val)
                    except Exception:  # pragma: NO COVER
                        pass

            if detected_peer_ip is None and status_obj is not None:
                dbg_fn = getattr(status_obj, "debug_error_string", None)
                dbg_val = (
                    dbg_fn()
                    if callable(dbg_fn)
                    else getattr(status_obj, "_debug_error_string", None)
                )
                if isinstance(dbg_val, bytes):
                    dbg_val = dbg_val.decode("utf-8", errors="replace")
                if isinstance(dbg_val, str):
                    detected_peer_ip = _extract_peer_ip(dbg_val)

    if exc is not None:
        for item in _opentelemetry_metrics._iter_exception_chain(exc):
            for md_attr in ("initial_metadata", "trailing_metadata"):
                md_fn = getattr(item, md_attr, None)
                md = md_fn() if callable(md_fn) else md_fn
                entries, is_gfe = _inspect_metadata(md)
                if is_gfe:
                    return "cloudpath"
                if entries:
                    has_server_metadata = True

            if detected_peer_ip is None:
                dbg_fn = getattr(item, "debug_error_string", None)
                dbg_val = dbg_fn() if callable(dbg_fn) else dbg_fn
                if isinstance(dbg_val, bytes):
                    dbg_val = dbg_val.decode("utf-8", errors="replace")
                if isinstance(dbg_val, str):
                    detected_peer_ip = _extract_peer_ip(dbg_val)

    if detected_peer_ip is not None:
        return _classify_ip(detected_peer_ip)

    server_responded = received_server_response or has_server_metadata
    if direct_path_attempted is False:
        return "cloudpath" if server_responded else "unknown"
    if direct_path_attempted is True:
        return "directpath" if server_responded else "unknown"
    return "unknown"


def _mark_call_closing_cleanly(call: Any) -> None:
    """Marks a wrapped gRPC call as closing cleanly before normal cancellation."""
    for current in _iter_wrapped_calls(call):
        inst_dict = getattr(current, "__dict__", None)
        if isinstance(current, _TrackedCallBase) or (
            isinstance(inst_dict, dict) and "_closing_cleanly" in inst_dict
        ):
            current._closing_cleanly = True


def _record_call_exception(call: Any, exc: BaseException) -> bool:
    """Records ``exc`` on any wrapped ``_TrackedCallBase`` before stream teardown."""
    recorded = False
    for current in _iter_wrapped_calls(call):
        if isinstance(current, _TrackedCallBase):
            current._record_from_exception(exc)
            recorded = True
    return recorded


def _bind_call_to_operation(
    call: Any, op_state: Optional[_opentelemetry_metrics._OperationState]
) -> None:
    """Binds a long-lived gRPC stream call to the currently active operation."""
    if op_state is None:
        return
    for current in _iter_wrapped_calls(call):
        if isinstance(current, _TrackedCallBase):
            current._op_state = op_state


class _TrackedCallBase:
    """Base proxy for ``grpc.aio.Call`` objects that records attempt metrics once."""

    def __init__(
        self,
        call: Any,
        recorder: _opentelemetry_metrics._MetricsRecorder,
        rpc_method: str,
        logical_operation: str,
        start_time: float,
        op_state: Optional[_opentelemetry_metrics._OperationState],
        direct_path_attempted: bool = False,
    ) -> None:
        self._call = call
        self._recorder = recorder
        self._rpc_method = rpc_method
        self._logical_operation = logical_operation
        self._start_time = start_time
        self._initial_op_state = op_state
        self._op_state = op_state
        self._started_after_failure = (
            op_state is not None and op_state.last_failure_error_type is not None
        )
        self._direct_path_attempted = direct_path_attempted
        self._received_response = False
        self._ttfb_recorded = False
        self._recorded = False
        self._closing_cleanly = False

    def __getattr__(self, name: str) -> Any:
        return getattr(self._call, name)

    def _record_ttfb_once(
        self,
        duration: Optional[float] = None,
        network_path: Optional[str] = None,
    ) -> None:
        if not self._ttfb_recorded:
            self._ttfb_recorded = True
            ttfb_duration = (
                max(0.0, time.perf_counter() - self._start_time)
                if duration is None
                else duration
            )
            resolved_path = (
                _resolve_network_path(
                    call=self._call,
                    direct_path_attempted=self._direct_path_attempted,
                    received_server_response=True,
                )
                if network_path is None
                else network_path
            )
            self._recorder.record_ttfb(
                duration=ttfb_duration,
                operation=self._logical_operation,
                network_path=resolved_path,
            )

    def _record_once(
        self,
        status_code: Optional[str],
        error_type: str,
        exc: Optional[BaseException] = None,
        received_response: bool = False,
        record_ttfb: bool = False,
    ) -> None:
        if not self._recorded:
            self._recorded = True
            current_op = _opentelemetry_metrics.get_current_operation()
            fallback_op = (
                self._op_state
                if (self._op_state is not None and not self._op_state.finished)
                else None
            )
            active_op = current_op or fallback_op
            if (
                error_type != "OK"
                and active_op is not None
                and active_op is not self._initial_op_state
            ):
                effective_start = active_op.start_time
            else:
                effective_start = self._start_time
            duration = max(0.0, time.perf_counter() - effective_start)
            resolved_path = _resolve_network_path(
                call=self._call,
                exc=exc,
                direct_path_attempted=self._direct_path_attempted,
                received_server_response=received_response or self._received_response,
            )
            if record_ttfb:
                self._record_ttfb_once(
                    duration=duration,
                    network_path=resolved_path,
                )
            is_stale_teardown = (
                active_op is not None
                and active_op.last_failure_error_type is not None
                and not self._started_after_failure
            )
            saved_prior_error = (
                active_op.consume_retry_error() if is_stale_teardown else None
            )
            self._recorder.record_rpc_attempt(
                duration=duration,
                operation=self._logical_operation,
                status_code=status_code,
                error_type=error_type,
                rpc_method=self._rpc_method,
                network_path=resolved_path,
                op_state=active_op,
            )
            if is_stale_teardown:
                active_op.last_failure_error_type = saved_prior_error

    def _record_from_exception(self, exc: BaseException) -> None:
        if isinstance(exc, asyncio.CancelledError) and self._closing_cleanly:
            self._record_once(
                status_code="OK",
                error_type="OK",
                received_response=self._received_response,
            )
        else:
            status_code, error_type = _resolve_status_and_error(exc)
            self._record_once(status_code=status_code, error_type=error_type, exc=exc)

    async def wait_for_connection(self) -> None:
        try:
            await self._call.wait_for_connection()
        except BaseException as exc:
            self._record_from_exception(exc)
            raise

    def cancel(self) -> bool:
        result = self._call.cancel()
        if self._closing_cleanly:
            self._record_once(
                status_code="OK",
                error_type="OK",
                received_response=self._received_response,
            )
        else:
            self._record_once(status_code="CANCELLED", error_type="CANCELLED")
        return result

    def cancelled(self) -> bool:
        return self._call.cancelled()

    def done(self) -> bool:
        return self._call.done()

    def add_done_callback(self, callback: Any) -> None:
        self._call.add_done_callback(callback)

    def time_remaining(self) -> Optional[float]:
        return self._call.time_remaining()

    async def initial_metadata(self) -> Any:
        return await self._call.initial_metadata()

    async def trailing_metadata(self) -> Any:
        return await self._call.trailing_metadata()

    async def code(self) -> Any:
        return await self._call.code()

    async def details(self) -> str:
        return await self._call.details()

    async def debug_error_string(self) -> str:
        return await self._call.debug_error_string()


class _TrackedUnaryResponseMixin:
    """Mixin for unary-response gRPC calls."""

    async def _await_impl(self) -> Any:
        try:
            response = await self._call
        except BaseException as exc:
            self._record_from_exception(exc)
            raise
        else:
            self._received_response = True
            self._record_once(
                status_code="OK",
                error_type="OK",
                received_response=True,
                record_ttfb=True,
            )
            return response

    def __await__(self):
        return self._await_impl().__await__()


class _TrackedStreamResponseMixin:
    """Mixin for streaming-response gRPC calls."""

    async def _aiter_impl(self):
        completed_normally = False
        try:
            async for response in self._call:
                self._received_response = True
                self._record_ttfb_once()
                yield response
            completed_normally = True
        except GeneratorExit:
            if self._closing_cleanly:
                self._record_once(
                    status_code="OK",
                    error_type="OK",
                    received_response=self._received_response,
                )
            else:
                self._record_once(status_code="CANCELLED", error_type="CANCELLED")
            raise
        except BaseException as exc:
            self._record_from_exception(exc)
            raise
        finally:
            if completed_normally:
                self._record_once(
                    status_code="OK", error_type="OK", received_response=True
                )

    def __aiter__(self):
        return self._aiter_impl()

    async def read(self) -> Any:
        try:
            response = await self._call.read()
        except BaseException as exc:
            self._record_from_exception(exc)
            raise
        else:
            self._received_response = True
            if response is grpc.aio.EOF or response == grpc.aio.EOF:
                self._record_once(
                    status_code="OK", error_type="OK", received_response=True
                )
            else:
                self._record_ttfb_once()
            return response


class _TrackedStreamRequestMixin:
    """Mixin for streaming-request gRPC calls."""

    async def write(self, request: Any) -> None:
        try:
            await self._call.write(request)
        except BaseException as exc:
            self._record_from_exception(exc)
            raise

    async def done_writing(self) -> None:
        try:
            await self._call.done_writing()
        except BaseException as exc:
            self._record_from_exception(exc)
            raise

    @property
    def _done_writing_flag(self) -> bool:
        return getattr(self._call, "_done_writing_flag", False)

    @_done_writing_flag.setter
    def _done_writing_flag(self, value: bool) -> None:
        setattr(self._call, "_done_writing_flag", value)


class _TrackedUnaryUnaryCall(
    _TrackedUnaryResponseMixin, _TrackedCallBase, grpc.aio.UnaryUnaryCall
):
    """Tracked ``grpc.aio.UnaryUnaryCall`` proxy."""


class _TrackedUnaryStreamCall(
    _TrackedStreamResponseMixin, _TrackedCallBase, grpc.aio.UnaryStreamCall
):
    """Tracked ``grpc.aio.UnaryStreamCall`` proxy."""


class _TrackedStreamUnaryCall(
    _TrackedUnaryResponseMixin,
    _TrackedStreamRequestMixin,
    _TrackedCallBase,
    grpc.aio.StreamUnaryCall,
):
    """Tracked ``grpc.aio.StreamUnaryCall`` proxy."""


class _TrackedStreamStreamCall(
    _TrackedStreamResponseMixin,
    _TrackedStreamRequestMixin,
    _TrackedCallBase,
    grpc.aio.StreamStreamCall,
):
    """Tracked ``grpc.aio.StreamStreamCall`` proxy."""


class _MetricsUnaryUnaryInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    """Client interceptor recording metrics for unary-unary gRPC attempts."""

    def __init__(
        self,
        recorder: _opentelemetry_metrics._MetricsRecorder,
        direct_path_attempted: bool = False,
    ) -> None:
        self._recorder = recorder
        self._direct_path_attempted = direct_path_attempted

    async def intercept_unary_unary(self, continuation, client_call_details, request):
        rpc_method = _extract_rpc_method(getattr(client_call_details, "method", None))
        logical_operation = _extract_logical_operation(rpc_method)
        op_state = _opentelemetry_metrics.get_current_operation()
        start_time = time.perf_counter()
        try:
            call = await continuation(client_call_details, request)
        except BaseException as exc:
            duration = max(0.0, time.perf_counter() - start_time)
            status_code, error_type = _resolve_status_and_error(exc)
            resolved_path = _resolve_network_path(
                exc=exc,
                direct_path_attempted=self._direct_path_attempted,
                received_server_response=False,
            )
            self._recorder.record_rpc_attempt(
                duration=duration,
                operation=logical_operation,
                status_code=status_code,
                error_type=error_type,
                rpc_method=rpc_method,
                network_path=resolved_path,
                op_state=op_state,
            )
            raise
        return _TrackedUnaryUnaryCall(
            call,
            self._recorder,
            rpc_method,
            logical_operation,
            start_time,
            op_state,
            direct_path_attempted=self._direct_path_attempted,
        )


class _MetricsUnaryStreamInterceptor(grpc.aio.UnaryStreamClientInterceptor):
    """Client interceptor recording metrics for unary-stream gRPC attempts."""

    def __init__(
        self,
        recorder: _opentelemetry_metrics._MetricsRecorder,
        direct_path_attempted: bool = False,
    ) -> None:
        self._recorder = recorder
        self._direct_path_attempted = direct_path_attempted

    async def intercept_unary_stream(self, continuation, client_call_details, request):
        rpc_method = _extract_rpc_method(getattr(client_call_details, "method", None))
        logical_operation = _extract_logical_operation(rpc_method)
        op_state = _opentelemetry_metrics.get_current_operation()
        start_time = time.perf_counter()
        try:
            call = await continuation(client_call_details, request)
        except BaseException as exc:
            duration = max(0.0, time.perf_counter() - start_time)
            status_code, error_type = _resolve_status_and_error(exc)
            resolved_path = _resolve_network_path(
                exc=exc,
                direct_path_attempted=self._direct_path_attempted,
                received_server_response=False,
            )
            self._recorder.record_rpc_attempt(
                duration=duration,
                operation=logical_operation,
                status_code=status_code,
                error_type=error_type,
                rpc_method=rpc_method,
                network_path=resolved_path,
                op_state=op_state,
            )
            raise
        return _TrackedUnaryStreamCall(
            call,
            self._recorder,
            rpc_method,
            logical_operation,
            start_time,
            op_state,
            direct_path_attempted=self._direct_path_attempted,
        )


class _MetricsStreamUnaryInterceptor(grpc.aio.StreamUnaryClientInterceptor):
    """Client interceptor recording metrics for stream-unary gRPC attempts."""

    def __init__(
        self,
        recorder: _opentelemetry_metrics._MetricsRecorder,
        direct_path_attempted: bool = False,
    ) -> None:
        self._recorder = recorder
        self._direct_path_attempted = direct_path_attempted

    async def intercept_stream_unary(
        self, continuation, client_call_details, request_iterator
    ):
        rpc_method = _extract_rpc_method(getattr(client_call_details, "method", None))
        logical_operation = _extract_logical_operation(rpc_method)
        op_state = _opentelemetry_metrics.get_current_operation()
        start_time = time.perf_counter()
        try:
            call = await continuation(client_call_details, request_iterator)
        except BaseException as exc:
            duration = max(0.0, time.perf_counter() - start_time)
            status_code, error_type = _resolve_status_and_error(exc)
            resolved_path = _resolve_network_path(
                exc=exc,
                direct_path_attempted=self._direct_path_attempted,
                received_server_response=False,
            )
            self._recorder.record_rpc_attempt(
                duration=duration,
                operation=logical_operation,
                status_code=status_code,
                error_type=error_type,
                rpc_method=rpc_method,
                network_path=resolved_path,
                op_state=op_state,
            )
            raise
        return _TrackedStreamUnaryCall(
            call,
            self._recorder,
            rpc_method,
            logical_operation,
            start_time,
            op_state,
            direct_path_attempted=self._direct_path_attempted,
        )


class _MetricsStreamStreamInterceptor(grpc.aio.StreamStreamClientInterceptor):
    """Client interceptor recording metrics for stream-stream gRPC attempts."""

    def __init__(
        self,
        recorder: _opentelemetry_metrics._MetricsRecorder,
        direct_path_attempted: bool = False,
    ) -> None:
        self._recorder = recorder
        self._direct_path_attempted = direct_path_attempted

    async def intercept_stream_stream(
        self, continuation, client_call_details, request_iterator
    ):
        rpc_method = _extract_rpc_method(getattr(client_call_details, "method", None))
        logical_operation = _extract_logical_operation(rpc_method)
        op_state = _opentelemetry_metrics.get_current_operation()
        start_time = time.perf_counter()
        try:
            call = await continuation(client_call_details, request_iterator)
        except BaseException as exc:
            duration = max(0.0, time.perf_counter() - start_time)
            status_code, error_type = _resolve_status_and_error(exc)
            resolved_path = _resolve_network_path(
                exc=exc,
                direct_path_attempted=self._direct_path_attempted,
                received_server_response=False,
            )
            self._recorder.record_rpc_attempt(
                duration=duration,
                operation=logical_operation,
                status_code=status_code,
                error_type=error_type,
                rpc_method=rpc_method,
                network_path=resolved_path,
                op_state=op_state,
            )
            raise
        return _TrackedStreamStreamCall(
            call,
            self._recorder,
            rpc_method,
            logical_operation,
            start_time,
            op_state,
            direct_path_attempted=self._direct_path_attempted,
        )


def _create_metrics_interceptors(
    recorder: _opentelemetry_metrics._MetricsRecorder,
    direct_path_attempted: bool = False,
) -> Tuple[grpc.aio.ClientInterceptor, ...]:
    """Creates the 4 ``grpc.aio`` client interceptors for ``recorder``."""
    return (
        _MetricsUnaryUnaryInterceptor(
            recorder, direct_path_attempted=direct_path_attempted
        ),
        _MetricsUnaryStreamInterceptor(
            recorder, direct_path_attempted=direct_path_attempted
        ),
        _MetricsStreamUnaryInterceptor(
            recorder, direct_path_attempted=direct_path_attempted
        ),
        _MetricsStreamStreamInterceptor(
            recorder, direct_path_attempted=direct_path_attempted
        ),
    )


def _validate_metadata(metadata):
    """Validates that metadata is a sequence of (key, value) pairs."""
    if metadata is None:
        return
    if not isinstance(metadata, (list, tuple)):
        raise TypeError("metadata must be a list or tuple of (key, value) pairs.")
    for item in metadata:
        if not isinstance(item, (list, tuple)) or len(item) != 2:
            raise ValueError(
                "Each element in metadata must be a list or tuple of exactly 2 strings (key, value)."
            )
        key, value = item
        if not isinstance(key, str) or not isinstance(value, str):
            raise TypeError("Both key and value in metadata pairs must be strings.")


class AsyncGrpcClient:
    """An asynchronous client for interacting with Google Cloud Storage using the gRPC API.

    :type credentials: :class:`~google.auth.credentials.Credentials`
    :param credentials: (Optional) The OAuth2 Credentials to use for this
                        client. If not passed, falls back to the default
                        inferred from the environment.

    :type client_info: :class:`~google.api_core.client_info.ClientInfo`
    :param client_info:
        The client info used to send a user-agent string along with API
        requests. If ``None``, then default info will be used.

    :type client_options: :class:`~google.api_core.client_options.ClientOptions`
    :param client_options: (Optional) Client options used to set user options
        on the client.

    :type attempt_direct_path: bool
    :param attempt_direct_path:
        (Optional) Whether to attempt to use DirectPath for gRPC connections.
        Defaults to ``True``.

    :type attempt_direct_path_xds_over_interconnect: bool
    :param attempt_direct_path_xds_over_interconnect:
        (Optional) Whether to attempt DirectPath over Cloud Interconnect
        using xDS and standard TLS. Can also be overridden via the
        ``GOOGLE_CLOUD_ENABLE_DIRECT_PATH_XDS_OVER_INTERCONNECT`` environment
        variable (``"true"`` or ``"false"``). Defaults to ``False``.

    :type enable_metrics: bool or None
    :param enable_metrics:
        (Optional, Experimental) Whether to enable OpenTelemetry metrics. If
        ``None``, falls back to the ``GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS``
        environment variable, or ``False`` if unset.

    :type enable_debug_metrics: bool or None
    :param enable_debug_metrics:
        (Optional, Experimental) Whether to enable debug OpenTelemetry
        metrics. If ``None``, falls back to the
        ``GCP_STORAGE_PYTHON_ENABLE_OTEL_DEBUG_METRICS`` environment variable,
        or ``False`` if unset.

    :type meter_provider: :class:`~opentelemetry.metrics.MeterProvider` or None
    :param meter_provider:
        (Optional, Experimental) A custom OpenTelemetry ``MeterProvider``
        instance used to create metric instruments. If ``None``, falls back to
        the globally registered OpenTelemetry ``MeterProvider``.
    """

    def __init__(
        self,
        credentials=None,
        client_info=None,
        client_options=None,
        *,
        attempt_direct_path=True,
        attempt_direct_path_xds_over_interconnect=False,
        enable_metrics=None,
        enable_debug_metrics=None,
        meter_provider=None,
    ):
        self._enable_metrics = enable_metrics
        self._enable_debug_metrics = enable_debug_metrics
        self._meter_provider = meter_provider
        self._metrics_enabled = _opentelemetry_metrics.is_metrics_enabled(
            enable_metrics
        )
        self._debug_metrics_enabled = _opentelemetry_metrics.is_debug_metrics_enabled(
            enable_debug_metrics
        )
        self._is_async_grpc_client = True
        self._bucket_metadata_cache = BucketMetadataCache(self)

        api_endpoint = None
        if isinstance(client_options, dict):
            api_endpoint = client_options.get("api_endpoint")
        elif client_options is not None:
            api_endpoint = getattr(client_options, "api_endpoint", None)

        self._metrics_recorder = _opentelemetry_metrics._MetricsRecorder(
            enable_metrics=enable_metrics,
            enable_debug_metrics=enable_debug_metrics,
            meter_provider=meter_provider,
            api_endpoint=api_endpoint,
            rpc_system="grpc",
        )

        if isinstance(credentials, auth_credentials.AnonymousCredentials):
            if client_options is None or client_options.api_endpoint is None:
                raise ValueError(
                    "Either client_options or `client_option.api_endpoint` is None. Please provide api_endpoint when `AnonymousCredentials` is used "
                )
            self._grpc_client = self._create_anonymous_client(
                client_options, credentials
            )
            self._grpc_client._metrics_recorder = self._metrics_recorder
            return

        if client_info is None:
            client_info = DEFAULT_CLIENT_INFO
        client_info.client_library_version = __version__
        if client_info.user_agent is None:
            client_info.user_agent = ""
        agent_version = f"gcloud-python/{__version__}"
        if agent_version not in client_info.user_agent:
            client_info.user_agent += f" {agent_version} "

        use_dp_interconnect = _resolve_direct_path_interconnect(
            attempt_direct_path_xds_over_interconnect
        )

        self._grpc_client = self._create_async_grpc_client(
            credentials=credentials,
            client_info=client_info,
            client_options=client_options,
            attempt_direct_path=attempt_direct_path,
            attempt_direct_path_xds_over_interconnect=use_dp_interconnect,
        )
        self._grpc_client._metrics_recorder = self._metrics_recorder

    @property
    def metrics_enabled(self) -> bool:
        """(Experimental) Returns ``True`` if OpenTelemetry metrics recording is active for this client."""
        return self._metrics_enabled

    @property
    def debug_metrics_enabled(self) -> bool:
        """(Experimental) Returns ``True`` if debug metrics recording is active for this client."""
        return self._debug_metrics_enabled

    def _create_anonymous_client(self, client_options, credentials):
        if self._metrics_recorder.standard_enabled:
            channel = grpc.aio.insecure_channel(
                client_options.api_endpoint,
                interceptors=_create_metrics_interceptors(
                    self._metrics_recorder, direct_path_attempted=False
                ),
            )
        else:
            channel = grpc.aio.insecure_channel(client_options.api_endpoint)
        transport = storage_v2.services.storage.transports.StorageGrpcAsyncIOTransport(
            channel=channel, credentials=credentials
        )
        return storage_v2.StorageAsyncClient(transport=transport)

    @classmethod
    def _create_insecure_grpc_client(cls, client_options):
        return cls(
            credentials=auth_credentials.AnonymousCredentials(),
            client_options=client_options,
            attempt_direct_path=False,
        )

    def _create_async_grpc_client(
        self,
        credentials=None,
        client_info=None,
        client_options=None,
        attempt_direct_path=True,
        attempt_direct_path_xds_over_interconnect=False,
    ):
        transport_cls = storage_v2.StorageAsyncClient.get_transport_class(
            "grpc_asyncio"
        )

        primary_user_agent = client_info.to_user_agent()

        host = _DEFAULT_HOST
        quota_project_id = None
        if isinstance(client_options, dict):
            host = client_options.get("api_endpoint") or _DEFAULT_HOST
            quota_project_id = client_options.get("quota_project_id")
        elif client_options:
            host = getattr(client_options, "api_endpoint", None) or _DEFAULT_HOST
            quota_project_id = getattr(client_options, "quota_project_id", None)

        extra_channel_kwargs = {}
        if self._metrics_recorder.standard_enabled:
            direct_path_attempted = bool(
                attempt_direct_path or attempt_direct_path_xds_over_interconnect
            )
            extra_channel_kwargs["interceptors"] = _create_metrics_interceptors(
                self._metrics_recorder,
                direct_path_attempted=direct_path_attempted,
            )

        if attempt_direct_path_xds_over_interconnect:
            host = _rewrite_host_for_interconnect(host)
            channel = transport_cls.create_channel(
                host=host,
                quota_project_id=quota_project_id,
                attempt_direct_path=True,
                attempt_direct_path_xds_over_interconnect=True,
                credentials=credentials,
                options=(("grpc.primary_user_agent", primary_user_agent),),
                **extra_channel_kwargs,
            )
        else:
            channel = transport_cls.create_channel(
                host=host,
                quota_project_id=quota_project_id,
                attempt_direct_path=attempt_direct_path,
                credentials=credentials,
                options=(("grpc.primary_user_agent", primary_user_agent),),
                **extra_channel_kwargs,
            )
        transport = transport_cls(channel=channel)

        return storage_v2.StorageAsyncClient(
            transport=transport,
            client_info=client_info,
            client_options=client_options,
        )

    async def close(self) -> None:
        """Closes the underlying gRPC transport and flushes pending metrics."""
        try:
            await self._grpc_client.transport.close()
        finally:
            self._metrics_recorder.shutdown()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    @property
    def grpc_client(self):
        """The underlying gRPC client.

        This property gives users direct access to the `_storage_v2.StorageAsyncClient`
         instance. This can be useful for accessing
        newly added or experimental RPCs that are not yet exposed through
        the high-level GrpcClient.
        Returns:
            google.cloud._storage_v2.StorageAsyncClient: The configured GAPIC client.
        """
        return self._grpc_client

    async def delete_object(
        self,
        bucket_name,
        object_name,
        generation=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        metadata=(),
        timeout=None,
        retry=None,
        **kwargs,
    ):
        """Deletes an object and its metadata.

        :type bucket_name: str
        :param bucket_name: The name of the bucket in which the object resides.

        :type object_name: str
        :param object_name: The name of the object to delete.

        :type generation: int
        :param generation:
            (Optional) If present, permanently deletes a specific generation
            of an object.

        :type if_generation_match: int
        :param if_generation_match: (Optional)

        :type if_generation_not_match: int
        :param if_generation_not_match: (Optional)

        :type if_metageneration_match: int
        :param if_metageneration_match: (Optional)

        :type if_metageneration_not_match: int
        :param if_metageneration_not_match: (Optional)

        :type metadata: Sequence[Tuple[str, str]]
        :param metadata: (Optional) Additional metadata that is provided to the method.

        :type timeout: float or None
        :param timeout:
            (Optional) The amount of time, in seconds, to wait for the request to
            complete.

        :type retry: :class:`~google.api_core.retry_async.AsyncRetry` or None
        :param retry: (Optional) Designation of what errors, if any, should be retried.
        """
        recorder = _opentelemetry_metrics.get_active_recorder(self)
        with _opentelemetry_metrics.start_operation(
            recorder,
            client_method="storage.asyncio.AsyncGrpcClient.delete_object",
            operation="DeleteObject",
            rpc_method="google.storage.v2.Storage/DeleteObject",
        ):
            _validate_metadata(metadata)
            async with create_trace_span_helper(
                self,
                bucket_name,
                "Storage.AsyncGrpcClient.deleteObject",
                rpc_system="grpc",
            ):
                # The gRPC API requires the bucket name to be in the format "projects/_/buckets/bucket_name"
                bucket_path = f"projects/_/buckets/{bucket_name}"
                request = storage_v2.DeleteObjectRequest(
                    bucket=bucket_path,
                    object=object_name,
                    generation=generation,
                    if_generation_match=if_generation_match,
                    if_generation_not_match=if_generation_not_match,
                    if_metageneration_match=if_metageneration_match,
                    if_metageneration_not_match=if_metageneration_not_match,
                    **kwargs,
                )
                final_metadata = _utils.inject_traceparent_to_metadata(metadata)
                await self._grpc_client.delete_object(
                    request=request,
                    metadata=final_metadata,
                    timeout=timeout,
                    retry=retry,
                )

    async def get_object(
        self,
        bucket_name,
        object_name,
        generation=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        soft_deleted=None,
        metadata=(),
        timeout=None,
        retry=None,
        **kwargs,
    ):
        """Retrieves an object's metadata.

        In the gRPC API, this is performed by the GetObject RPC, which
        returns the object resource (metadata) without the object's data.

        :type bucket_name: str
        :param bucket_name: The name of the bucket in which the object resides.

        :type object_name: str
        :param object_name: The name of the object.

        :type generation: int
        :param generation:
            (Optional) If present, selects a specific generation of an object.

        :type if_generation_match: int
        :param if_generation_match: (Optional) Precondition for object generation match.

        :type if_generation_not_match: int
        :param if_generation_not_match: (Optional) Precondition for object generation mismatch.

        :type if_metageneration_match: int
        :param if_metageneration_match: (Optional) Precondition for metageneration match.

        :type if_metageneration_not_match: int
        :param if_metageneration_not_match: (Optional) Precondition for metageneration mismatch.

        :type soft_deleted: bool
        :param soft_deleted:
            (Optional) If True, return the soft-deleted version of this object.

        :type metadata: Sequence[Tuple[str, str]]
        :param metadata: (Optional) Additional metadata that is provided to the method.

        :type timeout: float or None
        :param timeout:
            (Optional) The amount of time, in seconds, to wait for the request to
            complete.

        :type retry: :class:`~google.api_core.retry_async.AsyncRetry` or None
        :param retry: (Optional) Designation of what errors, if any, should be retried.

        :rtype: :class:`google.cloud._storage_v2.types.Object`
        :returns: The object metadata resource.
        """
        recorder = _opentelemetry_metrics.get_active_recorder(self)
        with _opentelemetry_metrics.start_operation(
            recorder,
            client_method="storage.asyncio.AsyncGrpcClient.get_object",
            operation="GetObject",
            rpc_method="google.storage.v2.Storage/GetObject",
        ):
            _validate_metadata(metadata)
            async with create_trace_span_helper(
                self,
                bucket_name,
                "Storage.AsyncGrpcClient.getObject",
                rpc_system="grpc",
            ):
                bucket_path = f"projects/_/buckets/{bucket_name}"

                request = storage_v2.GetObjectRequest(
                    bucket=bucket_path,
                    object=object_name,
                    generation=generation,
                    if_generation_match=if_generation_match,
                    if_generation_not_match=if_generation_not_match,
                    if_metageneration_match=if_metageneration_match,
                    if_metageneration_not_match=if_metageneration_not_match,
                    soft_deleted=soft_deleted or False,
                    **kwargs,
                )

                final_metadata = _utils.inject_traceparent_to_metadata(metadata)
                # Calls the underlying GAPIC StorageAsyncClient.get_object method
                return await self._grpc_client.get_object(
                    request=request,
                    metadata=final_metadata,
                    timeout=timeout,
                    retry=retry,
                )
