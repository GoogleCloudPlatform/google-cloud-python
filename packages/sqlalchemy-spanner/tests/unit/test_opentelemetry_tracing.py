# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import importlib
import sys

import mock
import pytest

try:
    from opentelemetry import trace as trace_api
    from opentelemetry.trace.status import StatusCode
except ImportError:
    pass

from google.api_core.exceptions import GoogleAPICallError
from google.cloud.spanner_v1 import SpannerClient

from google.cloud.sqlalchemy_spanner import _opentelemetry_tracing
from tests._helpers import HAS_OPENTELEMETRY_INSTALLED, OpenTelemetryBase


def _make_rpc_error(error_cls, trailing_metadata=None):
    import grpc

    grpc_error = mock.create_autospec(grpc.Call, instance=True)
    grpc_error.trailing_metadata.return_value = trailing_metadata
    return error_cls("error", errors=(grpc_error,))


# Skip all of these tests if we don't have OpenTelemetry
if HAS_OPENTELEMETRY_INSTALLED:

    class NoTracingTest(OpenTelemetryBase):
        def setup_method(self):
            self._temp_opentelemetry = sys.modules["opentelemetry"]

            sys.modules["opentelemetry"] = None
            importlib.reload(_opentelemetry_tracing)

        def teardown_method(self):
            super(NoTracingTest, self).teardown_method()
            sys.modules["opentelemetry"] = self._temp_opentelemetry
            importlib.reload(_opentelemetry_tracing)

        def test_no_trace_call(self):
            with _opentelemetry_tracing.trace_call("Test") as no_span:
                assert no_span is None

    class TracingTest(OpenTelemetryBase):
        def test_trace_call(self):
            extra_attributes = {
                "attribute1": "value1",
                # Since our database is mocked, we have to override the
                # db.instance parameter so it is a string.
                "db.instance": "database_name",
            }

            expected_attributes = {
                "db.type": "spanner",
                "db.engine": "sqlalchemy_spanner",
                "db.url": SpannerClient.DEFAULT_ENDPOINT,
                "net.host.name": SpannerClient.DEFAULT_ENDPOINT,
            }
            expected_attributes.update(extra_attributes)

            with _opentelemetry_tracing.trace_call(
                "CloudSpannerSqlAlchemy.Test", extra_attributes
            ) as span:
                span.set_attribute("after_setup_attribute", 1)

            expected_attributes["after_setup_attribute"] = 1

            span_list = self.ot_exporter.get_finished_spans()
            assert len(span_list) == 1

            span = span_list[0]
            assert span.kind == trace_api.SpanKind.CLIENT
            span_attr = dict(span.attributes)
            for key in expected_attributes:
                assert key in span_attr
                assert span_attr[key] == expected_attributes[key]
            assert span.name == "CloudSpannerSqlAlchemy.Test"
            assert span.status.status_code == StatusCode.OK

        def test_trace_error(self):
            extra_attributes = {"db.instance": "database_name"}

            expected_attributes = {
                "db.type": "spanner",
                "db.engine": "sqlalchemy_spanner",
                "db.url": SpannerClient.DEFAULT_ENDPOINT,
                "net.host.name": SpannerClient.DEFAULT_ENDPOINT,
            }
            expected_attributes.update(extra_attributes)

            with pytest.raises(GoogleAPICallError):
                with _opentelemetry_tracing.trace_call(
                    "CloudSpannerSqlAlchemy.Test",
                    extra_attributes,
                ) as span:
                    from google.api_core.exceptions import InvalidArgument

                    raise _make_rpc_error(InvalidArgument)

            span_list = self.ot_exporter.get_finished_spans()
            assert len(span_list) == 1
            span = span_list[0]
            assert span.kind == trace_api.SpanKind.CLIENT
            span_attr = dict(span.attributes)
            for key in expected_attributes:
                assert key in span_attr
                assert span_attr[key] == expected_attributes[key]
            assert span.name == "CloudSpannerSqlAlchemy.Test"
            assert span.status.status_code == StatusCode.ERROR
