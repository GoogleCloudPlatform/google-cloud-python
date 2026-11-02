# Copyright 2024 Google LLC
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

import importlib
import os
import sys

import mock
import pytest
from google.api_core.exceptions import GoogleAPICallError

from google.cloud.storage import __version__, _opentelemetry_tracing


@pytest.fixture
def setup():
    """Setup OTel packages and tracer provider."""
    try:
        from opentelemetry import trace as trace_api
        from opentelemetry.sdk.trace import TracerProvider, export
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )
    except ImportError:  # pragma: NO COVER
        pytest.skip("This test suite requires OpenTelemetry pacakges.")

    tracer_provider = TracerProvider()
    memory_exporter = InMemorySpanExporter()
    span_processor = export.SimpleSpanProcessor(memory_exporter)
    tracer_provider.add_span_processor(span_processor)
    trace_api.set_tracer_provider(tracer_provider)
    importlib.reload(_opentelemetry_tracing)
    yield memory_exporter


@pytest.fixture()
def mock_os_environ(monkeypatch):
    """Mock os.environ."""
    monkeypatch.setattr(os, "environ", {})
    return os.environ


@pytest.fixture()
def setup_optin(mock_os_environ):
    """Mock envar to opt-in tracing for storage client."""
    mock_os_environ["ENABLE_GCS_PYTHON_CLIENT_OTEL_TRACES"] = True
    importlib.reload(_opentelemetry_tracing)


@pytest.fixture()
def setup_optout(mock_os_environ):
    """Mock envar to opt-in tracing for storage client."""
    mock_os_environ["ENABLE_GCS_PYTHON_CLIENT_OTEL_TRACES"] = "False"
    importlib.reload(_opentelemetry_tracing)


def test_opentelemetry_not_installed(setup, monkeypatch):
    monkeypatch.setitem(sys.modules, "opentelemetry", None)
    importlib.reload(_opentelemetry_tracing)
    # Test no-ops when OpenTelemetry is not installed.
    with _opentelemetry_tracing.create_trace_span("No-ops w/o opentelemetry") as span:
        assert span is None
    assert not _opentelemetry_tracing.HAS_OPENTELEMETRY


def test_opentelemetry_no_trace_optin(setup):
    assert _opentelemetry_tracing.HAS_OPENTELEMETRY
    assert not _opentelemetry_tracing.enable_otel_traces
    # Test no-ops when user has not opt-in.
    # This prevents customers accidentally being billed for tracing.
    with _opentelemetry_tracing.create_trace_span("No-ops w/o opt-in") as span:
        assert span is None


def test_enable_trace_yield_span(setup, setup_optin):
    assert _opentelemetry_tracing.HAS_OPENTELEMETRY
    assert _opentelemetry_tracing.enable_otel_traces
    with _opentelemetry_tracing.create_trace_span("No-ops for opentelemetry") as span:
        assert span is not None


def test_disable_traces(setup, setup_optout):
    assert _opentelemetry_tracing.HAS_OPENTELEMETRY
    assert not _opentelemetry_tracing.enable_otel_traces
    with _opentelemetry_tracing.create_trace_span("No-ops for opentelemetry") as span:
        assert span is None


def test_enable_trace_call(setup, setup_optin):
    from opentelemetry import trace as trace_api

    extra_attributes = {
        "attribute1": "value1",
    }
    expected_attributes = _opentelemetry_tracing._default_attributes.copy()
    expected_attributes.update(_opentelemetry_tracing._cloud_trace_adoption_attrs)
    expected_attributes.update(extra_attributes)

    with _opentelemetry_tracing.create_trace_span(
        "OtelTracing.Test", attributes=extra_attributes
    ) as span:
        span.set_attribute("after_setup_attribute", 1)

        expected_attributes["after_setup_attribute"] = 1

        assert span.kind == trace_api.SpanKind.CLIENT
        assert span.attributes == expected_attributes
        assert span.name == "OtelTracing.Test"


def test_enable_trace_error(setup, setup_optin):
    from opentelemetry import trace as trace_api

    extra_attributes = {
        "attribute1": "value1",
    }
    expected_attributes = _opentelemetry_tracing._default_attributes.copy()
    expected_attributes.update(_opentelemetry_tracing._cloud_trace_adoption_attrs)
    expected_attributes.update(extra_attributes)

    with pytest.raises(GoogleAPICallError):
        with _opentelemetry_tracing.create_trace_span(
            "OtelTracing.Test", attributes=extra_attributes
        ) as span:
            from google.cloud.exceptions import NotFound

            assert span.kind == trace_api.SpanKind.CLIENT
            assert span.attributes == expected_attributes
            assert span.name == "OtelTracing.Test"
            raise NotFound("Test catching NotFound error in trace span.")


def test_get_final_attributes(setup, setup_optin):
    from google.api_core import retry as api_retry

    test_span_name = "OtelTracing.Test"
    test_span_attributes = {
        "foo": "bar",
    }
    api_request = {
        "method": "GET",
        "path": "/foo/bar/baz?sensitive=true",
        "timeout": (100, 100),
    }
    retry_obj = api_retry.Retry()

    expected_attributes = {
        "foo": "bar",
        "rpc.service": "CloudStorage",
        "rpc.system": "http",
        "user_agent.original": f"gcloud-python/{__version__}",
        "http.request.method": "GET",
        "server.address": "testOtel.org",
        "url.path": "/foo/bar/baz",
        "url.scheme": "https",
        "connect_timeout,read_timeout": str((100, 100)),
        "retry": f"multiplier{retry_obj._multiplier}/deadline{retry_obj._deadline}/max{retry_obj._maximum}/initial{retry_obj._initial}/predicate{retry_obj._predicate}",
    }
    expected_attributes.update(_opentelemetry_tracing._cloud_trace_adoption_attrs)

    with mock.patch("google.cloud.storage.client.Client") as test_client:
        test_client.project = "test_project"
        test_client._connection.build_api_url.return_value = (
            "https://testOtel.org/foo/bar/baz?sensitive=true"
        )
        with _opentelemetry_tracing.create_trace_span(
            test_span_name,
            attributes=test_span_attributes,
            client=test_client,
            api_request=api_request,
            retry=retry_obj,
        ) as span:
            assert span is not None
            assert span.name == test_span_name
            assert "url.query" not in span.attributes
            assert span.attributes == expected_attributes


def test_set_conditional_retry_attr(setup, setup_optin):
    from google.api_core import retry as api_retry

    from google.cloud.storage.retry import ConditionalRetryPolicy

    test_span_name = "OtelTracing.Test"
    retry_policy = api_retry.Retry()
    conditional_predicate = mock.Mock()
    required_kwargs = ("kwarg",)
    retry_obj = ConditionalRetryPolicy(
        retry_policy, conditional_predicate, required_kwargs
    )

    retry_attrs = {
        "retry": f"multiplier{retry_policy._multiplier}/deadline{retry_policy._deadline}/max{retry_policy._maximum}/initial{retry_policy._initial}/predicate{conditional_predicate}",
    }
    expected_attributes = _opentelemetry_tracing._default_attributes.copy()
    expected_attributes.update(_opentelemetry_tracing._cloud_trace_adoption_attrs)
    expected_attributes.update(retry_attrs)

    with _opentelemetry_tracing.create_trace_span(
        test_span_name,
        retry=retry_obj,
    ) as span:
        assert span is not None
        assert span.name == test_span_name
        assert span.attributes == expected_attributes


def test__get_opentelemetry_attributes_from_url():
    url = "https://example.com:8080/path?query=true"
    expected = {
        "server.address": "example.com",
        "server.port": 8080,
        "url.scheme": "https",
        "url.path": "/path",
    }
    # Test stripping query
    attrs = _opentelemetry_tracing._get_opentelemetry_attributes_from_url(
        url, strip_query=True
    )
    assert attrs == expected
    assert "url.query" not in attrs

    # Test not stripping query
    expected["url.query"] = "query=true"
    attrs = _opentelemetry_tracing._get_opentelemetry_attributes_from_url(
        url, strip_query=False
    )
    assert attrs == expected


def test__get_opentelemetry_attributes_from_url_with_query():
    url = "https://example.com/path?query=true&another=false"
    expected = {
        "server.address": "example.com",
        "server.port": None,
        "url.scheme": "https",
        "url.path": "/path",
        "url.query": "query=true&another=false",
    }
    # Test not stripping query
    attrs = _opentelemetry_tracing._get_opentelemetry_attributes_from_url(
        url, strip_query=False
    )
    assert attrs == expected


def test_set_api_request_attr_with_pii_in_query():
    client = mock.Mock()
    client._connection.build_api_url.return_value = (
        "https://example.com/path?sensitive=true&token=secret"
    )

    request = {
        "method": "GET",
        "path": "/path?sensitive=true&token=secret",
        "timeout": 60,
    }
    expected_attributes = {
        "http.request.method": "GET",
        "server.address": "example.com",
        "server.port": None,
        "url.scheme": "https",
        "url.path": "/path",
        "connect_timeout,read_timeout": "60",
    }
    attr = _opentelemetry_tracing._set_api_request_attr(request, client)
    assert attr == expected_attributes
    assert "url.query" not in attr  # Ensure query with PII is not captured


def test_set_api_request_attr_no_timeout():
    client = mock.Mock()
    client._connection.build_api_url.return_value = "https://example.com/path"

    request = {"method": "GET", "path": "/path"}
    attr = _opentelemetry_tracing._set_api_request_attr(request, client)
    assert "connect_timeout,read_timeout" not in attr


@pytest.mark.parametrize(
    "env_value, default, expected",
    [
        # Test default values when env var is not set
        (None, False, False),
        (None, True, True),
        # Test truthy values
        ("1", False, True),
        ("true", False, True),
        ("yes", False, True),
        ("on", False, True),
        ("TRUE", False, True),
        (" Yes ", False, True),
        # Test falsy values
        ("0", False, False),
        ("false", False, False),
        ("no", False, False),
        ("off", False, False),
        ("any_other_string", False, False),
        ("", False, False),
        # Test with default=True and falsy values
        ("false", True, False),
        ("0", True, False),
    ],
)
def test__parse_bool_env(monkeypatch, env_value, default, expected):
    env_var_name = "TEST_ENV_VAR"
    monkeypatch.setenv(
        env_var_name, str(env_value)
    ) if env_value is not None else monkeypatch.delenv(env_var_name, raising=False)

    result = _opentelemetry_tracing._parse_bool_env(env_var_name, default)
    assert result is expected


@pytest.mark.parametrize(
    "env_value, expected",
    [
        # Test default (not set)
        (None, False),
        # Test truthy values
        ("true", True),
        ("1", True),
        ("yes", True),
        ("on", True),
        ("TRUE", True),
        (" Yes ", True),
        # Test falsy values
        ("false", False),
        ("0", False),
        ("no", False),
        ("off", False),
        ("any_other_string", False),
        ("", False),
    ],
)
def test__is_bucket_metadata_disabled(monkeypatch, env_value, expected):
    env_var_name = "DISABLE_GCS_PYTHON_CLIENT_OTEL_BUCKET_METADATA"
    if env_value is not None:
        monkeypatch.setenv(env_var_name, str(env_value))
    else:
        monkeypatch.delenv(env_var_name, raising=False)

    assert _opentelemetry_tracing._is_bucket_metadata_disabled() is expected
