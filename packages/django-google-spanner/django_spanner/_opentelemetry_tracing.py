# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

"""Manages OpenTelemetry trace creation and handling"""

from contextlib import contextmanager

from google.api_core.exceptions import GoogleAPICallError

try:
    from opentelemetry import trace
    from opentelemetry.trace.status import Status, StatusCode

    HAS_OPENTELEMETRY_INSTALLED = True
except ImportError:
    HAS_OPENTELEMETRY_INSTALLED = False


@contextmanager
def trace_call(name, connection, extra_attributes=None):
    if not HAS_OPENTELEMETRY_INSTALLED or not connection:
        # Empty context manager. Users will have to check if the generated value
        # is None or a span.
        yield None
        return

    tracer = trace.get_tracer(__name__)

    # Set base attributes that we know for every trace created
    attributes = {
        "db.type": "spanner",
        "db.engine": "django_spanner",
        "db.project": connection.settings_dict["PROJECT"],
        "db.instance": connection.settings_dict["INSTANCE"],
        "db.name": connection.settings_dict["NAME"],
    }

    if extra_attributes:
        attributes.update(extra_attributes)

    with tracer.start_as_current_span(
        name, kind=trace.SpanKind.CLIENT, attributes=attributes
    ) as span:
        try:
            yield span
            span.set_status(Status(StatusCode.OK))
        except GoogleAPICallError as error:
            span.set_status(Status(StatusCode.ERROR))
            span.record_exception(error)
            raise
