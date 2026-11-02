# Copyright 2021 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

import google.auth.credentials
import pytest
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter


@pytest.fixture
def creds():
    """
    Provide test creds to unit tests so that they can run without
    GOOGLE_APPLICATION_CREDENTIALS set.
    """
    yield google.auth.credentials.AnonymousCredentials()


@pytest.fixture(scope="session", autouse=True)
def set_trace_provider():
    provider = TracerProvider()
    trace.set_tracer_provider(provider)


@pytest.fixture(scope="function")
def span_exporter():
    """Provides an InMemorySpanExporter for testing OpenTelemetry traces.

    Registers a SimpleSpanProcessor with the global TracerProvider at start,
    and removes it during teardown to prevent trace/span processor accumulation
    and test pollution across tests.
    """
    exporter = InMemorySpanExporter()
    processor = SimpleSpanProcessor(exporter)
    provider = trace.get_tracer_provider()
    provider.add_span_processor(processor)
    try:
        yield exporter
    finally:
        if hasattr(provider, "_active_span_processor") and hasattr(
            provider._active_span_processor, "_span_processors"
        ):
            processors = provider._active_span_processor._span_processors
            if isinstance(processors, tuple):
                provider._active_span_processor._span_processors = tuple(
                    p for p in processors if p is not processor
                )


@pytest.fixture()
def modify_google_logger_propagation():
    """
    Allow propagation of logs to the root logger for tests
    that depend on the caplog fixture. Restore the default
    propagation setting after the test finishes.
    """
    logger = logging.getLogger("google")
    original_propagate = logger.propagate
    logger.propagate = True
    try:
        yield
    finally:
        logger.propagate = original_propagate
