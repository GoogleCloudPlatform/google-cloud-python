# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import contextvars
from typing import Dict, FrozenSet, Optional, Union

import google_crc32c
from google.api_core import exceptions

from google.cloud.storage import _opentelemetry_tracing
from google.cloud.storage._helpers import create_trace_span_helper


def raise_if_no_fast_crc32c():
    """Check if the C-accelerated version of google-crc32c is available.

    If not, raise an error to prevent silent performance degradation.

    raises google.api_core.exceptions.FailedPrecondition: If the C extension is not available.
    returns: True if the C extension is available.
    rtype: bool

    """
    if google_crc32c.implementation != "c":
        raise exceptions.FailedPrecondition(
            "The google-crc32c package is not installed with C support. "
            "C extension is required for faster data integrity checks."
            "For more information, see https://github.com/googleapis/python-crc32c."
        )


def update_write_handle_if_exists(obj, response):
    """Update the write_handle attribute of an object if it exists in the response."""
    if hasattr(response, "write_handle") and response.write_handle is not None:
        obj.write_handle = response.write_handle


try:
    from opentelemetry.trace.propagation.tracecontext import (
        TraceContextTextMapPropagator,
    )

    _TRACE_CONTEXT_PROPAGATOR = TraceContextTextMapPropagator()
except ImportError:  # pragma: NO COVER
    _TRACE_CONTEXT_PROPAGATOR = None


def inject_traceparent_to_metadata(metadata=None):
    """Inject W3C traceparent (and tracestate) into gRPC metadata tuple or list."""
    if (
        not _opentelemetry_tracing._is_otel_traces_enabled()
        or _TRACE_CONTEXT_PROPAGATOR is None
    ):
        return () if metadata is None else metadata

    carrier = {}
    try:
        _TRACE_CONTEXT_PROPAGATOR.inject(carrier)
    except Exception:
        return () if metadata is None else metadata

    if not carrier:
        return () if metadata is None else metadata

    meta_list = list(metadata) if metadata else []
    existing_keys = {k.lower() for k, _ in meta_list}
    for key, val in carrier.items():
        if key.lower() not in existing_keys:
            meta_list.append((key, val))

    return (
        tuple(meta_list)
        if isinstance(metadata, tuple) or metadata is None
        else meta_list
    )


_ACTIVE_T2_SPAN_OWNERS: contextvars.ContextVar[FrozenSet[int]] = contextvars.ContextVar(
    "_active_t2_span_owners", default=frozenset()
)


class _TopLevelSpanContext:
    """Async context manager that tracks active top-level T2 spans per task."""

    __slots__ = ("_owner_id", "_cm", "_token")

    def __init__(self, owner_id: int, cm):
        self._owner_id = owner_id
        self._cm = cm
        self._token: Optional[contextvars.Token] = None

    async def __aenter__(self):
        owners = _ACTIVE_T2_SPAN_OWNERS.get()
        self._token = _ACTIVE_T2_SPAN_OWNERS.set(owners | {self._owner_id})
        try:
            return await self._cm.__aenter__()
        except BaseException:
            _ACTIVE_T2_SPAN_OWNERS.reset(self._token)
            raise

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            return await self._cm.__aexit__(exc_type, exc_val, exc_tb)
        finally:
            _ACTIVE_T2_SPAN_OWNERS.reset(self._token)


def create_top_level_trace_span(
    owner,
    client,
    bucket_name: str,
    name: str,
    attributes: Optional[Dict[str, Union[str, int]]] = None,
):
    """Create a T2 OpenTelemetry span only for top-level public API calls per task."""
    owner_id = id(owner)
    if owner_id in _ACTIVE_T2_SPAN_OWNERS.get():
        return _opentelemetry_tracing._NOOP_TRACE_SPAN_CONTEXT
    cm = create_trace_span_helper(
        client,
        bucket_name,
        name,
        attributes=attributes,
        rpc_system="grpc",
    )
    if cm is _opentelemetry_tracing._NOOP_TRACE_SPAN_CONTEXT:
        return cm
    return _TopLevelSpanContext(owner_id, cm)
