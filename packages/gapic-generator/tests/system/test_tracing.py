# Copyright 2026 Google LLC
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

import os
from unittest import mock

import grpc
import pytest

try:
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
        InMemorySpanExporter,
    )

    HAS_OPENTELEMETRY = True
except ImportError:
    HAS_OPENTELEMETRY = False

if not HAS_OPENTELEMETRY:
    pytest.skip("OpenTelemetry is not installed", allow_module_level=True)

try:
    from google.api_core import _observability

    HAS_TIER3_TRACING = hasattr(_observability, "_TraceContext")
except ImportError:
    HAS_TIER3_TRACING = False

if not HAS_TIER3_TRACING:
    pytest.skip(
        "Installed google-api-core lacks Tier 3 OpenTelemetry tracing",
        allow_module_level=True,
    )

from google import showcase
from google.api_core._feature_gating_helpers import FeatureGatingError
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from google.showcase import EchoAsyncClient, EchoClient

try:
    from google.api_core import _observability

    HAS_AUTO_INSTRUMENTATION_SUPPRESSION = _observability is not None and hasattr(
        _observability, "_AsyncSuppressingClientInterceptor"
    )
except ImportError:
    HAS_AUTO_INSTRUMENTATION_SUPPRESSION = False

try:
    from .conftest import construct_client
except (ImportError, ValueError):
    from conftest import construct_client


@pytest.fixture
def span_exporter():
    """Provides an isolated InMemorySpanExporter and TracerProvider for test assertions."""
    exporter = InMemorySpanExporter()
    provider = TracerProvider()
    processor = SimpleSpanProcessor(exporter)
    provider.add_span_processor(processor)

    yield exporter, provider

    exporter.clear()


@pytest.fixture
def otel_echo_client(span_exporter, use_mtls):
    """Constructs an EchoClient wired with an in-memory TracerProvider."""
    exporter, provider = span_exporter
    options = ClientOptions(
        tracer_provider=provider,
    )
    with mock.patch.dict(
        os.environ, {"GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED": "true"}
    ):
        client = construct_client(
            EchoClient,
            use_mtls,
            client_options=options,
            credentials=ga_credentials.AnonymousCredentials(),
        )
        yield client, exporter


def test_tracing_disabled_default(span_exporter, use_mtls):
    """Verifies that default client options emit zero spans (zero overhead guarantee).

    Ensures that without setting GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED=true,
    even if an ambient TracerProvider is active, zero spans are recorded and no
    tracing overhead is incurred. Also verifies that passing tracer_provider without
    the environment variable fails fast by raising FeatureGatingError.
    """
    exporter, provider = span_exporter

    # Providing a tracer_provider without enabling the experimental env var fails fast
    options_with_provider = ClientOptions(
        tracer_provider=provider,
    )
    with mock.patch.dict(
        os.environ, {"GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED": "false"}
    ):
        with pytest.raises(FeatureGatingError):
            construct_client(
                EchoClient,
                use_mtls,
                client_options=options_with_provider,
                credentials=ga_credentials.AnonymousCredentials(),
            )

    # Default client options emit zero spans
    options = ClientOptions()
    with mock.patch.dict(
        os.environ, {"GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED": "false"}
    ):
        client = construct_client(
            EchoClient,
            use_mtls,
            client_options=options,
            credentials=ga_credentials.AnonymousCredentials(),
        )

        response = client.echo(showcase.EchoRequest(content="no tracing"))
        assert response.content == "no tracing"

        # Zero spans must be emitted when tracing is disabled
        spans = exporter.get_finished_spans()
        assert len(spans) == 0


def test_custom_tracer_provider(use_mtls):
    """Verifies that spans are emitted exclusively to the injected custom TracerProvider.

    Ensures strict isolation of trace data: when a client is configured with a
    custom `TracerProvider`, generated RPC spans must be routed solely to that
    provider's exporters and never leak into the ambient/global `TracerProvider`.

    Configures an ambient global `TracerProvider` with `global_exporter`, while
    configuring the client with `custom_provider` and `custom_exporter`. After
    executing an RPC, the test asserts that `custom_exporter` captured the span
    while `global_exporter` recorded zero spans.
    """
    custom_exporter = InMemorySpanExporter()
    custom_provider = TracerProvider()
    custom_provider.add_span_processor(SimpleSpanProcessor(custom_exporter))

    global_exporter = InMemorySpanExporter()
    global_provider = TracerProvider()
    global_provider.add_span_processor(SimpleSpanProcessor(global_exporter))

    # Mock the ambient global tracer provider instead of mutating global state
    with mock.patch(
        "opentelemetry.trace.get_tracer_provider", return_value=global_provider
    ):
        options = ClientOptions(
            tracer_provider=custom_provider,
        )
        with mock.patch.dict(
            os.environ, {"GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED": "true"}
        ):
            client = construct_client(
                EchoClient,
                use_mtls,
                client_options=options,
                credentials=ga_credentials.AnonymousCredentials(),
            )

            response = client.echo(showcase.EchoRequest(content="isolated trace"))
            assert response.content == "isolated trace"

            custom_spans = custom_exporter.get_finished_spans()
            assert len(custom_spans) == 2
            global_spans = global_exporter.get_finished_spans()
            assert len(global_spans) == 0


def test_direct_client_initialization_tracing(span_exporter):
    """Verifies end-to-end trace injection via direct EchoClient instantiation.

    Validates the template wiring in `client.py.j2` directly. In system test
    harnesses, `construct_client` often creates the transport instance manually,
    which bypasses `client.py`'s `if not transport_provided:` branch. This test
    instantiates `EchoClient(client_options=...)` directly to prove that the client
    resolves `_observability.get_otel_interceptor` and passes it to `EchoGrpcTransport`.

    Constructs `EchoClient` without a pre-instantiated transport. Patches
    `EchoGrpcTransport.create_channel` solely to target the local insecure Showcase
    endpoint (`localhost:7469`). Executes `client.echo()` and asserts span generation.
    """
    exporter, provider = span_exporter
    options = ClientOptions(
        tracer_provider=provider,
    )

    with mock.patch.dict(
        os.environ, {"GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED": "true"}
    ):
        with mock.patch.object(
            EchoClient.get_transport_class("grpc"),
            "create_channel",
            side_effect=lambda host, **kwargs: grpc.insecure_channel("localhost:7469"),
        ):
            # Client constructs the transport and wires interceptors itself
            client = EchoClient(
                client_options=options,
                credentials=ga_credentials.AnonymousCredentials(),
            )
            response = client.echo(showcase.EchoRequest(content="direct client wiring"))
            assert response.content == "direct client wiring"

            spans = exporter.get_finished_spans()
            assert len(spans) == 2
            for span in spans:
                assert span.name == "google.showcase.v1beta1.Echo/Echo"
                assert span.attributes.get("rpc.system.name") == "grpc"


def test_env_var_opt_in(otel_echo_client):
    """Verifies that setting the environment variable enables tracing without tracing_enabled=True."""
    client, exporter = otel_echo_client

    response = client.echo(showcase.EchoRequest(content="env opt in"))
    assert response.content == "env opt in"

    spans = exporter.get_finished_spans()
    assert len(spans) == 2
    for span in spans:
        assert span.name == "google.showcase.v1beta1.Echo/Echo"


@pytest.mark.skipif(
    not HAS_AUTO_INSTRUMENTATION_SUPPRESSION,
    reason="Installed google-api-core lacks auto-instrumentation suppression",
)
def test_auto_instrumentation_suppression_sync(span_exporter):
    """Verifies that upstream gRPC client auto-instrumentation spans are suppressed in sync calls.

    When users enable global GrpcInstrumentorClient().instrument(), upstream injects a
    generic interceptor into channel creation. This test verifies that our downstream
    suppression interceptor prevents the duplicate, bare-bones upstream span from being
    emitted while preserving the full Google Cloud SDK T4 span.
    """
    grpc_instrumentation = pytest.importorskip("opentelemetry.instrumentation.grpc")

    exporter, provider = span_exporter
    instrumentor = grpc_instrumentation.GrpcInstrumentorClient()
    instrumentor.instrument(tracer_provider=provider)
    try:
        options = ClientOptions(
            api_endpoint="localhost:7469",
            tracer_provider=provider,
        )
        with mock.patch.dict(
            os.environ, {"GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED": "true"}
        ):
            channel = grpc.insecure_channel("localhost:7469")
            transport = EchoClient.get_transport_class("grpc")(
                channel=channel,
                client_options=options,
                credentials=ga_credentials.AnonymousCredentials(),
            )
            client = EchoClient(transport=transport, client_options=options)
            response = client.echo(
                showcase.EchoRequest(content="suppress sync duplicate")
            )
            assert response.content == "suppress sync duplicate"

            spans = exporter.get_finished_spans()
            assert len(spans) == 2

            root_spans = [s for s in spans if s.parent is None]
            child_spans = [s for s in spans if s.parent is not None]
            assert len(root_spans) == 1
            assert len(child_spans) == 1

            root_span = root_spans[0]
            child_span = child_spans[0]

            assert root_span.name == "google.showcase.v1beta1.Echo/Echo"
            assert child_span.name == "google.showcase.v1beta1.Echo/Echo"
            assert child_span.parent.span_id == root_span.context.span_id

            assert child_span.attributes.get("rpc.system.name") == "grpc"
            assert child_span.attributes.get("server.address") == "localhost"
            assert child_span.attributes.get("server.port") == 7469
            assert child_span.attributes.get("url.domain") == "googleapis.com"
            assert child_span.attributes.get("rpc.response.status_code") == "OK"
    finally:
        instrumentor.uninstrument()


@pytest.mark.asyncio
@pytest.mark.skipif(
    not HAS_AUTO_INSTRUMENTATION_SUPPRESSION,
    reason="Installed google-api-core lacks auto-instrumentation suppression",
)
async def test_auto_instrumentation_suppression_async(span_exporter):
    """Verifies that upstream gRPC client auto-instrumentation spans are suppressed in async calls.

    When users enable global GrpcAioInstrumentorClient().instrument(), upstream injects a
    generic interceptor into aio channel creation. This test verifies that our downstream
    suppression interceptor prevents the duplicate, bare-bones upstream span from being
    emitted while preserving the full Google Cloud SDK T4 span.
    """
    grpc_instrumentation = pytest.importorskip("opentelemetry.instrumentation.grpc")

    exporter, provider = span_exporter
    instrumentor = grpc_instrumentation.GrpcAioInstrumentorClient()
    instrumentor.instrument(tracer_provider=provider)
    try:
        options = ClientOptions(
            api_endpoint="localhost:7469",
            tracer_provider=provider,
        )
        with mock.patch.dict(
            os.environ, {"GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED": "true"}
        ):
            channel = grpc.aio.insecure_channel("localhost:7469")
            transport = EchoAsyncClient.get_transport_class("grpc_asyncio")(
                channel=channel,
                client_options=options,
                credentials=ga_credentials.AnonymousCredentials(),
            )
            client = EchoAsyncClient(transport=transport, client_options=options)
            response = await client.echo(
                showcase.EchoRequest(content="suppress async duplicate")
            )
            assert response.content == "suppress async duplicate"

            spans = exporter.get_finished_spans()
            assert len(spans) == 2

            root_spans = [s for s in spans if s.parent is None]
            child_spans = [s for s in spans if s.parent is not None]
            assert len(root_spans) == 1
            assert len(child_spans) == 1

            root_span = root_spans[0]
            child_span = child_spans[0]

            assert root_span.name == "google.showcase.v1beta1.Echo/Echo"
            assert child_span.name == "google.showcase.v1beta1.Echo/Echo"
            assert child_span.parent.span_id == root_span.context.span_id

            assert child_span.attributes.get("rpc.system.name") == "grpc"
            assert child_span.attributes.get("server.address") == "localhost"
            assert child_span.attributes.get("server.port") == 7469
            assert child_span.attributes.get("url.domain") == "googleapis.com"
            assert child_span.attributes.get("rpc.response.status_code") == "OK"
    finally:
        instrumentor.uninstrument()
