# Copyright 2020 Google LLC All rights reserved.
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

"""Manages OpenTelemetry trace creation and handling"""

import os
from collections.abc import Mapping
from contextlib import contextmanager
from datetime import datetime

from opentelemetry import trace
from opentelemetry.trace.status import Status, StatusCode

from google.cloud.spanner_v1._helpers import (
    _get_cloud_region,
    _metadata_with_span_context,
)
from google.cloud.spanner_v1.gapic_version import __version__ as gapic_version
from google.cloud.spanner_v1.services.spanner.client import SpannerClient

TRACER_NAME = "cloud.google.com/python/spanner"
TRACER_VERSION = gapic_version
GCP_RESOURCE_NAME_PREFIX = "//spanner.googleapis.com/"
extended_tracing_globally_disabled = (
    os.getenv("SPANNER_ENABLE_EXTENDED_TRACING", "").lower() == "false"
)
end_to_end_tracing_globally_enabled = (
    os.getenv("SPANNER_ENABLE_END_TO_END_TRACING", "").lower() == "true"
)


def _is_tracer_noop(tracer: trace.Tracer) -> bool:
    """Check if a tracer is a no-op tracer or an uninitialized proxy tracer."""
    if tracer is None or isinstance(tracer, trace.NoOpTracer):
        return True
    if isinstance(tracer, trace.ProxyTracer):
        underlying = getattr(tracer, "_tracer", None)
        return isinstance(underlying, trace.NoOpTracer)
    return False


def get_tracer(tracer_provider=None):
    """
    get_tracer is a utility to unify and simplify retrieval of the tracer, without
    leaking implementation details given that retrieving a tracer requires providing
    the full qualified library name and version.
    When the tracer_provider is set, it'll retrieve the tracer from it, otherwise
    it'll fall back to the global tracer provider and use this library's specific semantics.
    """
    if not tracer_provider:
        # Acquire the global tracer provider.
        tracer_provider = trace.get_tracer_provider()

    return tracer_provider.get_tracer(TRACER_NAME, TRACER_VERSION)


@contextmanager
def trace_call(
    name, session=None, extra_attributes=None, observability_options=None, metadata=None
):
    if session:
        session._last_use_time = datetime.now()

    tracer_provider = None
    enable_end_to_end_tracing = False

    has_options = isinstance(observability_options, Mapping)
    if has_options:
        tracer_provider = observability_options.get("tracer_provider", None)
        enable_end_to_end_tracing = observability_options.get(
            "enable_end_to_end_tracing", False
        )

    if end_to_end_tracing_globally_enabled:
        enable_end_to_end_tracing = True

    tracer = get_tracer(tracer_provider)

    # Fast path: when no TracerProvider is registered or a no-op tracer is active,
    # skip attribute dictionary construction and span creation entirely.
    if _is_tracer_noop(tracer):
        current_span = trace.get_current_span()
        if (
            current_span is not trace.INVALID_SPAN
            and current_span.get_span_context().is_valid
        ):
            child_span = trace.NonRecordingSpan(current_span.get_span_context())
            with trace.use_span(child_span):
                if enable_end_to_end_tracing:
                    _metadata_with_span_context(metadata)
                yield child_span
            return

        if enable_end_to_end_tracing:
            _metadata_with_span_context(metadata)
        yield trace.INVALID_SPAN
        return

    # Slow path: resolve attributes and configure span when tracing is active.
    enable_extended_tracing = True
    db_name = ""

    if session and getattr(session, "_database", None):
        db_name = session._database.name

    if has_options:
        enable_extended_tracing = observability_options.get(
            "enable_extended_tracing", enable_extended_tracing
        )
        db_name = observability_options.get("db_name", db_name)

    cloud_region = _get_cloud_region()

    # Set base attributes that we know for every trace created
    attributes = {
        "db.type": "spanner",
        "db.url": SpannerClient.DEFAULT_ENDPOINT,
        "db.instance": db_name,
        "net.host.name": SpannerClient.DEFAULT_ENDPOINT,
        "otel.scope.name": TRACER_NAME,
        "cloud.region": cloud_region,
        "otel.scope.version": TRACER_VERSION,
        # Standard GCP attributes for OTel, attributes are used for internal purpose and are subjected to change
        "gcp.client.service": "spanner",
        "gcp.client.version": TRACER_VERSION,
        "gcp.client.repo": "googleapis/python-spanner",
        "gcp.resource.name": GCP_RESOURCE_NAME_PREFIX + db_name,
    }

    if extra_attributes:
        attributes.update(extra_attributes)

    if "request_options" in attributes:
        request_options = attributes.pop("request_options")
        if request_options and request_options.request_tag:
            attributes["request.tag"] = request_options.request_tag

    if extended_tracing_globally_disabled:
        enable_extended_tracing = False

    if not enable_extended_tracing:
        attributes.pop("db.statement", False)

    with tracer.start_as_current_span(
        name, kind=trace.SpanKind.CLIENT, attributes=attributes
    ) as span:
        try:
            if enable_end_to_end_tracing:
                _metadata_with_span_context(metadata)
            yield span
        except Exception as error:
            span.set_status(Status(StatusCode.ERROR, str(error)))
            # OpenTelemetry-Python imposes invoking span.record_exception on __exit__
            # on any exception. We should file a bug later on with them to only
            # invoke .record_exception if not already invoked, hence we should not
            # invoke .record_exception on our own else we shall have 2 exceptions.
            raise
        else:
            # All spans still have set_status available even if for example
            # NonRecordingSpan doesn't have "_status".
            absent_span_status = getattr(span, "_status", None) is None
            if absent_span_status or span._status.status_code == StatusCode.UNSET:
                # OpenTelemetry-Python only allows a status change
                # if the current code is UNSET or ERROR. At the end
                # of the generator's consumption, only set it to OK
                # it wasn't previously set otherwise.
                # https://github.com/googleapis/python-spanner/issues/1246
                span.set_status(Status(StatusCode.OK))


def get_current_span():
    return trace.get_current_span()


def add_span_event(span, event_name, event_attributes=None):
    if span and span.is_recording():
        span.add_event(event_name, event_attributes)
