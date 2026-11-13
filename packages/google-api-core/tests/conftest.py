# Copyright 2026 Google LLC
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

import os
import sys
import types
from unittest import mock

import pytest


@pytest.fixture(scope="session", autouse=True)
def mock_mtls_env():
    """Autouse session-scoped fixture to isolate unit tests from workstation mTLS environments."""
    with mock.patch.dict(
        os.environ,
        {
            "GOOGLE_API_USE_CLIENT_CERTIFICATE": "false",
            "CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE": "false",
        },
    ):
        yield


@pytest.fixture
def mock_otel(monkeypatch):
    """Provides a mocked OpenTelemetry environment with tracing enabled."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    mock_span = mock.MagicMock()
    mock_tracer = mock.MagicMock()
    mock_tracer.start_as_current_span.return_value.__enter__.return_value = mock_span

    mock_trace = mock.Mock()
    mock_trace.get_tracer.return_value = mock_tracer
    mock_trace.SpanKind.CLIENT = "CLIENT"
    mock_trace.SpanKind.INTERNAL = "INTERNAL"
    mock_trace.StatusCode.ERROR = "ERROR"

    with (
        mock.patch(
            "google.api_core._observability.is_otel_capabilities_enabled",
            return_value=True,
        ),
        mock.patch.dict(
            sys.modules,
            {
                "opentelemetry": mock.Mock(trace=mock_trace),
                "opentelemetry.trace": mock_trace,
                "opentelemetry.trace.status": mock.Mock(),
                "opentelemetry.trace.propagation.tracecontext": mock.Mock(),
                "opentelemetry.instrumentation.grpc": mock.Mock(),
            },
        ),
    ):
        yield types.SimpleNamespace(
            trace=mock_trace,
            tracer=mock_tracer,
            span=mock_span,
        )


@pytest.fixture
def mock_otel_grpc(monkeypatch):
    """Provides a mocked opentelemetry.instrumentation.grpc module environment.

    Unlike `mock_otel` (which mocks `opentelemetry.trace` to test span generation
    in client methods), this fixture simulates the installation of the gRPC
    auto-instrumentation package (`opentelemetry.instrumentation.grpc`) in `sys.modules`.
    This allows testing gRPC channel interceptor resolution and capability checks.
    """
    mock_otel = mock.Mock()
    mock_grpc = mock_otel.instrumentation.grpc
    monkeypatch.setitem(sys.modules, "opentelemetry", mock_otel)
    monkeypatch.setitem(
        sys.modules, "opentelemetry.instrumentation", mock_otel.instrumentation
    )
    monkeypatch.setitem(sys.modules, "opentelemetry.instrumentation.grpc", mock_grpc)
    return mock_grpc


@pytest.fixture
def mock_async_channel():
    """Provides a mock grpc.aio.Channel with standard interceptor list attributes."""
    channel = mock.Mock()
    channel._unary_unary_interceptors = []
    channel._unary_stream_interceptors = []
    channel._stream_unary_interceptors = []
    channel._stream_stream_interceptors = []
    return channel
