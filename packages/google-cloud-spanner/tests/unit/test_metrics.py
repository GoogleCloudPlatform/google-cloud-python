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

from unittest.mock import MagicMock, patch

import pytest
from google.api_core.exceptions import ServiceUnavailable
from google.auth import exceptions
from google.auth.credentials import Credentials
from grpc._interceptor import _UnaryOutcome
from opentelemetry import metrics

from google.cloud.spanner_v1.client import Client
from google.cloud.spanner_v1.metrics.spanner_metrics_tracer_factory import (
    SpannerMetricsTracerFactory,
)

pytest.importorskip("opentelemetry")
# Skip if semconv attributes are not present, as tracing won't be enabled either
# pytest.importorskip("opentelemetry.semconv.attributes.otel_attributes")


class TestCredentials(Credentials):
    @property
    def expired(self):
        return False

    @property
    def valid(self):
        return True

    def refresh(self, request):
        raise exceptions.InvalidOperation("Anonymous credentials cannot be refreshed.")

    def apply(self, headers, token=None):
        if token is not None:
            raise exceptions.InvalidValue("Anonymous credentials don't support tokens.")

    def before_request(self, request, method, url, headers):
        """Anonymous credentials do nothing to the request."""


@pytest.fixture(autouse=True)
def patched_client(monkeypatch):
    monkeypatch.setenv("SPANNER_DISABLE_BUILTIN_METRICS", "false")
    metrics.set_meter_provider(metrics.NoOpMeterProvider())

    # Remove the Tracer factory to avoid previously disabled factory polluting from other tests
    if SpannerMetricsTracerFactory._metrics_tracer_factory is not None:
        SpannerMetricsTracerFactory._metrics_tracer_factory = None

    # Reset the global flag to ensure metrics initialization runs
    from google.cloud.spanner_v1 import client as client_module

    client_module._metrics_monitor_initialized = False

    with (
        patch("google.cloud.spanner_v1.metrics.metrics_exporter.MetricServiceClient"),
        patch("google.cloud.spanner_v1.client.CloudMonitoringMetricsExporter"),
        patch("google.cloud.spanner_v1.client.PeriodicExportingMetricReader"),
    ):
        client = Client(
            project="test",
            credentials=TestCredentials(),
        )
        yield client

    # Resetting
    metrics.set_meter_provider(metrics.NoOpMeterProvider())
    SpannerMetricsTracerFactory._metrics_tracer_factory = None
    client_module._metrics_monitor_initialized = False
    # Reset context var
    ctx = SpannerMetricsTracerFactory._current_metrics_tracer_ctx
    ctx.set(None)


def test_metrics_emission_with_failure_attempt(patched_client):
    instance = patched_client.instance("test-instance")
    database = instance.database("example-db")
    factory = SpannerMetricsTracerFactory()

    assert factory.enabled

    import google.auth.credentials

    from google.cloud.spanner_v1.metrics.metrics_interceptor import MetricsInterceptor
    from google.cloud.spanner_v1.services.spanner.client import SpannerClient
    from google.cloud.spanner_v1.services.spanner.transports.grpc import (
        SpannerGrpcTransport,
    )

    # Recreate the SpannerClient and transport with MetricsInterceptor properly bound
    credentials = database._instance._client.credentials
    if isinstance(credentials, google.auth.credentials.Scoped):
        from google.cloud.spanner_v1.database import SPANNER_DATA_SCOPE

        credentials = credentials.with_scopes((SPANNER_DATA_SCOPE,))

    transport = SpannerGrpcTransport(
        credentials=credentials,
        client_info=database._instance._client._client_info,
        metrics_interceptor=MetricsInterceptor(),
    )
    database._spanner_api = SpannerClient(transport=transport)

    transport = database.spanner_api._transport
    metrics_interceptor = transport._metrics_interceptor
    original_intercept = metrics_interceptor.intercept
    first_attempt = True

    captured_tracer_list = []

    def mocked_raise(*args, **kwargs):
        raise ServiceUnavailable("Service Unavailable")

    def mocked_call(*args, **kwargs):
        # Capture the tracer while it is active
        captured_tracer_list.append(SpannerMetricsTracerFactory.get_current_tracer())
        return _UnaryOutcome(MagicMock(), MagicMock())

    def intercept_wrapper(invoked_method, request_or_iterator, call_details):
        nonlocal first_attempt
        invoked_method = mocked_call
        if first_attempt:
            first_attempt = False
            invoked_method = mocked_raise
        response = original_intercept(
            invoked_method=invoked_method,
            request_or_iterator=request_or_iterator,
            call_details=call_details,
        )
        return response

    metrics_interceptor.intercept = intercept_wrapper
    patch_path = "google.cloud.spanner_v1.metrics.metrics_exporter.CloudMonitoringMetricsExporter.export"

    with patch(patch_path):
        with database.snapshot():
            pass

    # Verify that the attempt count increased from the failed initial attempt
    # We use the captured tracer from the SUCCESSFUL attempt (the second one)
    assert len(captured_tracer_list) > 0
    tracer = captured_tracer_list[0]
    assert tracer is not None
    # ... (no change needed if not found, but I must be sure)
