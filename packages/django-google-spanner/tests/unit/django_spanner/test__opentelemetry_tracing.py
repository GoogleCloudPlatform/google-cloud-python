# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import importlib
import os
import sys
import unittest

import mock

try:
    from opentelemetry import trace as trace_api
    from opentelemetry.trace.status import StatusCode
except ImportError:
    pass

from google.api_core.exceptions import GoogleAPICallError

from django_spanner import _opentelemetry_tracing
from tests._helpers import HAS_OPENTELEMETRY_INSTALLED, OpenTelemetryBase

PROJECT = os.environ.get("GOOGLE_CLOUD_PROJECT", "test-project")
INSTANCE_ID = "instance_id"
DATABASE_ID = "database_id"
OPTIONS = {"option": "dummy"}


def _make_rpc_error(error_cls, trailing_metadata=None):
    import grpc

    grpc_error = mock.create_autospec(grpc.Call, instance=True)
    grpc_error.trailing_metadata.return_value = trailing_metadata
    return error_cls("error", errors=(grpc_error,))


def _make_connection():
    from django_spanner.base import DatabaseWrapper

    settings_dict = {
        "PROJECT": PROJECT,
        "INSTANCE": INSTANCE_ID,
        "NAME": DATABASE_ID,
        "OPTIONS": OPTIONS,
    }
    return DatabaseWrapper(settings_dict)


# Skip all of these tests if we don't have OpenTelemetry
if HAS_OPENTELEMETRY_INSTALLED:

    class TestNoTracing(unittest.TestCase):
        def setUp(self):
            self._temp_opentelemetry = sys.modules["opentelemetry"]

            sys.modules["opentelemetry"] = None
            importlib.reload(_opentelemetry_tracing)

        def tearDown(self):
            sys.modules["opentelemetry"] = self._temp_opentelemetry
            importlib.reload(_opentelemetry_tracing)

        def test_no_trace_call(self):
            with _opentelemetry_tracing.trace_call(
                "Test", _make_connection()
            ) as no_span:
                self.assertIsNone(no_span)

    class TestTracing(OpenTelemetryBase):
        def test_trace_call(self):
            extra_attributes = {
                "attribute1": "value1",
                # Since our database is mocked, we have to override the db.instance parameter so it is a string
                "db.instance": "database_name",
            }

            expected_attributes = {
                "db.type": "spanner",
                "db.engine": "django_spanner",
                "db.project": PROJECT,
                "db.instance": INSTANCE_ID,
                "db.name": DATABASE_ID,
            }
            expected_attributes.update(extra_attributes)

            with _opentelemetry_tracing.trace_call(
                "CloudSpannerDjango.Test", _make_connection(), extra_attributes
            ) as span:
                span.set_attribute("after_setup_attribute", 1)

            expected_attributes["after_setup_attribute"] = 1

            span_list = self.ot_exporter.get_finished_spans()
            self.assertEqual(len(span_list), 1)
            span = span_list[0]
            self.assertEqual(span.kind, trace_api.SpanKind.CLIENT)
            self.assertEqual(span.attributes, expected_attributes)
            self.assertEqual(span.name, "CloudSpannerDjango.Test")
            self.assertEqual(span.status.status_code, StatusCode.OK)

        def test_trace_error(self):
            extra_attributes = {"db.instance": "database_name"}

            expected_attributes = {
                "db.type": "spanner",
                "db.engine": "django_spanner",
                "db.project": os.environ.get("GOOGLE_CLOUD_PROJECT", "test-project"),
                "db.instance": "instance_id",
                "db.name": "database_id",
            }
            expected_attributes.update(extra_attributes)

            with self.assertRaises(GoogleAPICallError):
                with _opentelemetry_tracing.trace_call(
                    "CloudSpannerDjango.Test",
                    _make_connection(),
                    extra_attributes,
                ) as span:
                    from google.api_core.exceptions import InvalidArgument

                    raise _make_rpc_error(InvalidArgument)

            span_list = self.ot_exporter.get_finished_spans()
            self.assertEqual(len(span_list), 1)
            span = span_list[0]
            self.assertEqual(span.kind, trace_api.SpanKind.CLIENT)
            self.assertEqual(dict(span.attributes), expected_attributes)
            self.assertEqual(span.name, "CloudSpannerDjango.Test")
            self.assertEqual(span.status.status_code, StatusCode.ERROR)
