# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


import configparser
import os
import pathlib

import mock
from sqlalchemy.testing import fixtures

try:
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
        InMemorySpanExporter,
    )
    from opentelemetry.trace.status import StatusCode

    trace.set_tracer_provider(TracerProvider())

    HAS_OPENTELEMETRY_INSTALLED = True
except ImportError:
    HAS_OPENTELEMETRY_INSTALLED = False

    StatusCode = mock.Mock()

_TEST_OT_EXPORTER = None
_TEST_OT_PROVIDER_INITIALIZED = False


PROJECT = os.getenv(
    "GOOGLE_CLOUD_PROJECT",
    os.getenv("PROJECT_ID", "emulator-test-project"),
)
DB_URL = (
    f"spanner:///projects/{PROJECT}/instances/"
    "sqlalchemy-dialect-test/databases/compliance-test"
)


def get_db_url():
    """Retrieve the database URL from the active session config file.

    Respects the SQLALCHEMY_SPANNER_CONFIG environment variable set by Nox
    to ensure each parallel test session connects to its own isolated database.
    """
    config = configparser.ConfigParser()
    config_filename = os.getenv("SQLALCHEMY_SPANNER_CONFIG", "test.cfg")
    config_path = pathlib.Path(config_filename)
    if config_path.exists():
        config.read(config_path)
    else:
        config.read("setup.cfg")
    return config.get("db", "default", fallback=DB_URL)


def get_test_ot_exporter():
    global _TEST_OT_EXPORTER

    if _TEST_OT_EXPORTER is None:
        _TEST_OT_EXPORTER = InMemorySpanExporter()
    return _TEST_OT_EXPORTER


def use_test_ot_exporter():
    global _TEST_OT_PROVIDER_INITIALIZED

    if _TEST_OT_PROVIDER_INITIALIZED:
        return

    provider = trace.get_tracer_provider()
    if not hasattr(provider, "add_span_processor"):
        return
    provider.add_span_processor(SimpleSpanProcessor(get_test_ot_exporter()))
    _TEST_OT_PROVIDER_INITIALIZED = True


def get_project():
    return PROJECT


class OpenTelemetryBase(fixtures.TestBase):
    @classmethod
    def setup_class(cls):
        if HAS_OPENTELEMETRY_INSTALLED:
            use_test_ot_exporter()
            cls.ot_exporter = get_test_ot_exporter()

    def teardown_method(self):
        if HAS_OPENTELEMETRY_INSTALLED:
            self.ot_exporter.clear()

    def assertNoSpans(self):
        if HAS_OPENTELEMETRY_INSTALLED:
            span_list = self.ot_exporter.get_finished_spans()
            self.assertEqual(len(span_list), 0)

    def assertSpanAttributes(
        self, name, status=StatusCode.OK, attributes=None, span=None
    ):
        if HAS_OPENTELEMETRY_INSTALLED:
            if not span:
                span_list = self.ot_exporter.get_finished_spans()
                self.assertEqual(len(span_list), 1)
                span = span_list[0]

            self.assertEqual(span.name, name)
            self.assertEqual(span.status.status_code, status)
            self.assertEqual(dict(span.attributes), attributes)
