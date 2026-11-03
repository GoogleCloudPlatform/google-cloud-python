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

import sys
import types
import urllib.parse
from unittest import mock

import pytest

from google.api_core import _observability
from google.api_core._feature_gating_helpers import FeatureGatingError
from google.api_core.client_options import ClientOptions


def test_is_otel_capabilities_enabled_disabled(monkeypatch):
    """Proves that is_otel_capabilities_enabled returns False when the tracing environment variable is disabled."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "false")
    assert not _observability.is_otel_capabilities_enabled()


def test_is_otel_capabilities_enabled_otel_missing(monkeypatch):
    """Proves that is_otel_capabilities_enabled returns False when tracing is enabled
    but OpenTelemetry gRPC instrumentation is not installed.
    """
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    # Simulate OTel not being installed by blocking imports
    monkeypatch.setitem(sys.modules, "opentelemetry.instrumentation.grpc", None)

    assert not _observability.is_otel_capabilities_enabled()


def test_is_otel_capabilities_enabled_otel_installed(monkeypatch, mock_otel_grpc):
    """Proves that is_otel_capabilities_enabled returns True when tracing is enabled
    and OpenTelemetry gRPC instrumentation is installed.
    """
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    assert _observability.is_otel_capabilities_enabled()


def test_is_otel_capabilities_enabled_experimental_requires_env_var(monkeypatch):
    """Proves that passing client_options with tracer_provider without the experimental
    env var set to 'true' raises FeatureGatingError (Fail Fast).
    """
    monkeypatch.delenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", raising=False)
    options = ClientOptions(tracer_provider=mock.Mock())

    with pytest.raises(
        FeatureGatingError,
        match="requires GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED",
    ):
        _observability.is_otel_capabilities_enabled(options)


def test_is_otel_capabilities_enabled_experimental_enabled_with_config(
    monkeypatch, mock_otel_grpc
):
    """Proves that when GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED=true and tracer_provider
    is supplied via client_options, is_otel_capabilities_enabled returns True.
    """
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    options = ClientOptions(tracer_provider=mock.Mock())
    assert _observability.is_otel_capabilities_enabled(options)


@pytest.mark.parametrize(
    "boundary_options",
    [
        pytest.param(None, id="options_none"),
        pytest.param({}, id="options_empty_dict"),
        pytest.param({"irrelevant_field": 123}, id="options_missing_tracer_provider"),
    ],
)
def test_observability_handles_boundary_client_options(boundary_options):
    """Verifies boundary handling when client options lack telemetry attributes."""
    enabled = _observability.is_otel_capabilities_enabled(boundary_options)
    assert enabled is False

    endpoint_attrs = _observability._extract_endpoint_attributes(boundary_options)
    assert endpoint_attrs == {"url.domain": "googleapis.com"}


def test_get_tracer_provider_default():
    """Proves that _get_tracer_provider returns None when no client_options are supplied."""
    assert _observability._get_tracer_provider() is None


def test_get_tracer_provider_config():
    """Proves that _get_tracer_provider extracts the tracer provider when supplied
    via a ClientOptions instance.
    """
    mock_tracer_provider = mock.Mock()
    options = ClientOptions(tracer_provider=mock_tracer_provider)
    assert _observability._get_tracer_provider(options) is mock_tracer_provider


def test_get_tracer_provider_dict_config():
    """Proves that _get_tracer_provider extracts the tracer provider when supplied
    via a dictionary configuration.
    """
    mock_tracer_provider = mock.Mock()
    options = {"tracer_provider": mock_tracer_provider}
    assert _observability._get_tracer_provider(options) is mock_tracer_provider


@pytest.mark.parametrize(
    "interceptor_getter",
    [
        _observability.get_otel_interceptor,
        _observability.get_otel_async_interceptor,
    ],
    ids=["sync_interceptor", "async_interceptor"],
)
def test_get_otel_interceptor_disabled(monkeypatch, interceptor_getter):
    """Proves that interceptor getters return None when tracing is disabled."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "false")
    assert interceptor_getter() is None


@pytest.mark.parametrize(
    "interceptor_getter",
    [
        _observability.get_otel_interceptor,
        _observability.get_otel_async_interceptor,
    ],
    ids=["sync_interceptor", "async_interceptor"],
)
def test_get_otel_interceptor_otel_missing(monkeypatch, interceptor_getter):
    """Proves that interceptor getters return None when OpenTelemetry gRPC
    instrumentation is not installed.
    """
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    monkeypatch.setitem(sys.modules, "opentelemetry.instrumentation.grpc", None)
    assert interceptor_getter() is None


def test_get_otel_interceptor_enabled(monkeypatch, mock_otel_grpc):
    """Proves that get_otel_interceptor creates a synchronous OpenTelemetry client
    interceptor with the resolved tracer provider and returns a channel-intercepting callable.
    """
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    mock_tracer_provider = mock.Mock()
    options = ClientOptions(tracer_provider=mock_tracer_provider)

    mock_raw_channel = mock.Mock(name="raw_channel")
    mock_wrapped_channel = mock.Mock(name="wrapped_channel")
    mock_interceptor = mock.Mock(name="otel_interceptor")

    mock_otel_grpc.client_interceptor.return_value = mock_interceptor
    mock_otel_grpc.intercept_channel.return_value = mock_wrapped_channel

    interceptor = _observability.get_otel_interceptor(client_options=options)
    assert callable(interceptor)

    mock_otel_grpc.client_interceptor.assert_called_once_with(
        tracer_provider=mock_tracer_provider,
        request_hook=mock.ANY,
        response_hook=_observability._grpc_client_response_hook,
    )
    req_hook = mock_otel_grpc.client_interceptor.call_args[1]["request_hook"]
    mock_span = mock.Mock()
    mock_span.is_recording.return_value = True
    req_hook(mock_span, None)
    mock_span.set_attribute.assert_any_call("url.domain", "googleapis.com")

    result = interceptor(mock_raw_channel)
    assert result is mock_wrapped_channel
    assert mock_otel_grpc.intercept_channel.call_count == 1
    chan_arg, interceptor_arg = mock_otel_grpc.intercept_channel.call_args[0]
    assert interceptor_arg is mock_interceptor


def test_get_otel_interceptor_with_apply_channel_interceptors(
    monkeypatch, mock_otel_grpc
):
    """Proves that get_otel_interceptor integrates seamlessly into apply_channel_interceptors."""
    pytest.importorskip("grpc")
    from google.api_core import grpc_helpers

    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    mock_tracer_provider = mock.Mock()
    options = ClientOptions(tracer_provider=mock_tracer_provider)

    mock_raw_channel = mock.Mock(name="raw_channel")
    mock_wrapped_channel = mock.Mock(name="wrapped_channel")
    mock_interceptor = mock.Mock(name="otel_interceptor")

    mock_otel_grpc.client_interceptor.return_value = mock_interceptor
    mock_otel_grpc.intercept_channel.return_value = mock_wrapped_channel

    otel_interceptor = _observability.get_otel_interceptor(client_options=options)
    assert callable(otel_interceptor)

    result = grpc_helpers.apply_channel_interceptors(
        mock_raw_channel, interceptors=[otel_interceptor]
    )
    assert result is mock_wrapped_channel
    assert mock_otel_grpc.intercept_channel.call_count == 1
    chan_arg, interceptor_arg = mock_otel_grpc.intercept_channel.call_args[0]
    assert interceptor_arg is mock_interceptor


@pytest.mark.skipif(_observability.grpc is None, reason="grpc is not installed")
@pytest.mark.parametrize("error_cls", [AttributeError, TypeError])
def test_get_otel_interceptor_grpc_intercept_channel_fallback(
    monkeypatch, mock_otel_grpc, error_cls
):
    """Proves that otel_interceptor falls back gracefully if grpc.intercept_channel raises AttributeError or TypeError."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    options = ClientOptions()
    mock_raw_channel = mock.Mock(name="raw_channel")
    mock_wrapped_channel = mock.Mock(name="wrapped_channel")
    mock_otel_grpc.client_interceptor.return_value = mock.Mock()
    mock_otel_grpc.intercept_channel.return_value = mock_wrapped_channel

    otel_interceptor = _observability.get_otel_interceptor(client_options=options)
    with mock.patch.object(
        _observability.grpc,
        "intercept_channel",
        side_effect=error_cls("Mock intercept error"),
    ):
        result = otel_interceptor(mock_raw_channel)
        assert result is mock_wrapped_channel


def test_get_otel_interceptor_grpc_none(monkeypatch, mock_otel_grpc):
    """Proves that otel_interceptor proceeds cleanly when grpc is None."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    options = ClientOptions()
    mock_raw_channel = mock.Mock(name="raw_channel")
    mock_wrapped_channel = mock.Mock(name="wrapped_channel")
    mock_otel_grpc.client_interceptor.return_value = mock.Mock()
    mock_otel_grpc.intercept_channel.return_value = mock_wrapped_channel

    otel_interceptor = _observability.get_otel_interceptor(client_options=options)
    with mock.patch.object(_observability, "grpc", None):
        result = otel_interceptor(mock_raw_channel)
        assert result is mock_wrapped_channel


def test_get_otel_async_interceptor_enabled(monkeypatch, mock_otel_grpc):
    """Proves that get_otel_async_interceptor instantiates and returns asynchronous
    OpenTelemetry client interceptors with the resolved tracer provider.
    """
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    mock_tracer_provider = mock.Mock()
    options = ClientOptions(tracer_provider=mock_tracer_provider)

    mock_async_interceptors = [mock.Mock(name="otel_async_interceptor")]
    mock_otel_grpc.aio_client_interceptors.return_value = mock_async_interceptors

    result = _observability.get_otel_async_interceptor(client_options=options)
    assert mock_async_interceptors[0] in result
    assert any(
        isinstance(i, _observability._AsyncSuppressingClientInterceptor) for i in result
    )
    mock_otel_grpc.aio_client_interceptors.assert_called_once_with(
        tracer_provider=mock_tracer_provider,
        request_hook=mock.ANY,
        response_hook=_observability._grpc_client_response_hook,
    )

    req_hook = mock_otel_grpc.aio_client_interceptors.call_args[1]["request_hook"]
    mock_span = mock.Mock()
    mock_span.is_recording.return_value = True
    req_hook(mock_span, None)
    mock_span.set_attribute.assert_any_call("url.domain", "googleapis.com")


def test_get_otel_async_interceptor_single_return(monkeypatch, mock_otel_grpc):
    """Verifies that a single interceptor returned by upstream OTel is safely wrapped into a list."""
    # Step 1: Opt-in to experimental SDK tracing via environment variable.
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")

    # Step 2: Configure the mock OpenTelemetry gRPC instrumentation fixture.
    # While upstream normally returns a sequence (list or tuple), third-party
    # instrumentation or older versions may return a lone interceptor object.
    # We simulate this edge case by returning a single mock interceptor.
    single_interceptor = mock.Mock(name="single_otel_interceptor")
    mock_otel_grpc.aio_client_interceptors.return_value = single_interceptor

    # Step 3: Call get_otel_async_interceptor with standard ClientOptions.
    options = ClientOptions()
    result = _observability.get_otel_async_interceptor(client_options=options)

    # Step 4: Validate list normalization and downstream suppression interceptor injection.
    # The result must be a 2-item list:
    #   [0]: The single upstream interceptor wrapped in a list.
    #   [1]: Our internal _AsyncSuppressingClientInterceptor appended to prevent redundant wire spans.
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] is single_interceptor
    assert isinstance(result[1], _observability._AsyncSuppressingClientInterceptor)


@pytest.mark.parametrize(
    "client_options,expected_attrs",
    [
        (None, {"url.domain": "googleapis.com"}),
        ({}, {"url.domain": "googleapis.com"}),
        (ClientOptions(api_endpoint=None), {"url.domain": "googleapis.com"}),
        ({"universe_domain": "myuniverse.com"}, {"url.domain": "myuniverse.com"}),
        (
            ClientOptions(universe_domain="custom.domain"),
            {"url.domain": "custom.domain"},
        ),
        (
            {"api_endpoint": "secretmanager.googleapis.com"},
            {
                "server.address": "secretmanager.googleapis.com",
                "url.domain": "googleapis.com",
            },
        ),
        (
            {"api_endpoint": "secretmanager.googleapis.com:443"},
            {
                "server.address": "secretmanager.googleapis.com",
                "url.domain": "googleapis.com",
            },
        ),
        (
            {"api_endpoint": "https://secretmanager.googleapis.com:443"},
            {
                "server.address": "secretmanager.googleapis.com",
                "url.domain": "googleapis.com",
            },
        ),
        (
            {"api_endpoint": "http://localhost:80"},
            {"server.address": "localhost", "url.domain": "googleapis.com"},
        ),
        (
            ClientOptions(api_endpoint="https://my-custom-host.com:8443/"),
            {
                "server.address": "my-custom-host.com",
                "server.port": 8443,
                "url.domain": "googleapis.com",
            },
        ),
        (
            ClientOptions(api_endpoint="http://[::1]:8080"),
            {
                "server.address": "::1",
                "server.port": 8080,
                "url.domain": "googleapis.com",
            },
        ),
        (
            ClientOptions(api_endpoint="http:///"),
            {"url.domain": "googleapis.com"},
        ),
        (
            ClientOptions(api_endpoint="example.com:not_a_port"),
            {"server.address": "example.com", "url.domain": "googleapis.com"},
        ),
        (
            ClientOptions(api_endpoint="http://[invalid:ipv6:80/"),
            {"url.domain": "googleapis.com"},
        ),
        (
            ClientOptions(api_endpoint="example.com:99999"),
            {"server.address": "example.com", "url.domain": "googleapis.com"},
        ),
    ],
)
def test_extract_endpoint_attributes(client_options, expected_attrs):
    """Proves that _extract_endpoint_attributes correctly parses server.address, non-default server.port, and url.domain."""
    assert _observability._extract_endpoint_attributes(client_options) == expected_attrs


def test_grpc_client_request_hook():
    """Proves that _grpc_client_request_hook attaches extracted T4 attributes to recording spans,
    normalizes span names, sets fully qualified rpc.method, and allows legacy rpc.system to coexist.
    """
    # Non-recording span should not set attributes
    mock_span_non_rec = mock.Mock()
    mock_span_non_rec.is_recording.return_value = False
    _observability._grpc_client_request_hook(mock_span_non_rec, mock.Mock())
    mock_span_non_rec.set_attribute.assert_not_called()

    # None span should safely return
    _observability._grpc_client_request_hook(None, mock.Mock())

    # Recording span with default hook, leading slash in span.name, and legacy rpc.system
    mock_span_rec = mock.Mock()
    mock_span_rec.is_recording.return_value = True
    mock_span_rec.name = (
        "/google.cloud.secretmanager.v1.SecretManagerService/ListSecrets"
    )
    mock_span_rec._attributes = {"rpc.system": "grpc"}

    _observability._grpc_client_request_hook(mock_span_rec, mock.Mock())

    # Verify span name normalized and rpc.method set to fully qualified name
    mock_span_rec.update_name.assert_called_once_with(
        "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets"
    )
    mock_span_rec.set_attribute.assert_any_call(
        "rpc.method", "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets"
    )

    # Verify rpc.system.name set and legacy rpc.system left intact
    mock_span_rec.set_attribute.assert_any_call("rpc.system.name", "grpc")
    assert mock_span_rec._attributes["rpc.system"] == "grpc"

    # Custom hook with endpoint attributes and already-clean span name (no leading slash)
    endpoint_hook = _observability._make_grpc_client_request_hook(
        {"server.address": "custom.api.com", "server.port": 443}
    )
    mock_span_custom = mock.Mock()
    mock_span_custom.is_recording.return_value = True
    mock_span_custom.name = (
        "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets"
    )
    endpoint_hook(mock_span_custom, None)
    mock_span_custom.set_attribute.assert_any_call("server.address", "custom.api.com")
    mock_span_custom.set_attribute.assert_any_call("server.port", 443)
    mock_span_custom.set_attribute.assert_any_call(
        "rpc.method", "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets"
    )
    mock_span_custom.update_name.assert_not_called()


def test_grpc_client_request_hook_span_edge_cases():
    """Proves that _grpc_client_request_hook handles spans lacking update_name,
    spans with None or non-string names, and empty string names gracefully.
    """
    # 1. Leading slash in span.name but span lacks update_name
    mock_span_no_update = mock.Mock(spec=["is_recording", "name", "set_attribute"])
    mock_span_no_update.is_recording.return_value = True
    mock_span_no_update.name = "/package.Service/Method"
    _observability._grpc_client_request_hook(mock_span_no_update, None)
    mock_span_no_update.set_attribute.assert_any_call(
        "rpc.method", "package.Service/Method"
    )
    mock_span_no_update.set_attribute.assert_any_call("rpc.system.name", "grpc")

    # 2. Span with None name
    mock_span_none_name = mock.Mock(spec=["is_recording", "name", "set_attribute"])
    mock_span_none_name.is_recording.return_value = True
    mock_span_none_name.name = None
    _observability._grpc_client_request_hook(mock_span_none_name, None)
    mock_span_none_name.set_attribute.assert_any_call("rpc.system.name", "grpc")
    assert not any(
        call.args[0] == "rpc.method"
        for call in mock_span_none_name.set_attribute.call_args_list
    )

    # 3. Span with empty string name
    mock_span_empty_name = mock.Mock(spec=["is_recording", "name", "set_attribute"])
    mock_span_empty_name.is_recording.return_value = True
    mock_span_empty_name.name = ""
    _observability._grpc_client_request_hook(mock_span_empty_name, None)
    mock_span_empty_name.set_attribute.assert_any_call("rpc.system.name", "grpc")
    assert not any(
        call.args[0] == "rpc.method"
        for call in mock_span_empty_name.set_attribute.call_args_list
    )


def test_get_otel_interceptor_with_api_endpoint(monkeypatch):
    """Proves that get_otel_interceptor injects server.address, server.port, and url.domain when api_endpoint is set."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    options = ClientOptions(
        api_endpoint="secretmanager.googleapis.com:8443",
        universe_domain="custom-domain.com",
    )

    mock_otel = mock.Mock()
    mock_otel_grpc = mock_otel.instrumentation.grpc
    monkeypatch.setitem(sys.modules, "opentelemetry", mock_otel)
    monkeypatch.setitem(
        sys.modules, "opentelemetry.instrumentation", mock_otel.instrumentation
    )
    monkeypatch.setitem(
        sys.modules, "opentelemetry.instrumentation.grpc", mock_otel_grpc
    )

    interceptor = _observability.get_otel_interceptor(client_options=options)
    assert callable(interceptor)

    # Verify custom request hook was passed
    args, kwargs = mock_otel_grpc.client_interceptor.call_args
    req_hook = kwargs["request_hook"]
    assert req_hook is not _observability._grpc_client_request_hook
    assert kwargs["response_hook"] is _observability._grpc_client_response_hook

    # Test invoking the custom hook
    mock_span = mock.Mock()
    mock_span.is_recording.return_value = True
    req_hook(mock_span, None)
    mock_span.set_attribute.assert_any_call(
        "server.address", "secretmanager.googleapis.com"
    )
    mock_span.set_attribute.assert_any_call("server.port", 8443)
    mock_span.set_attribute.assert_any_call("url.domain", "custom-domain.com")


def test_get_otel_async_interceptor_with_api_endpoint(monkeypatch):
    """Proves that get_otel_async_interceptor injects server.address, server.port, and url.domain when api_endpoint is set."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    options = ClientOptions(
        api_endpoint="secretmanager.googleapis.com:8443",
        universe_domain="custom-domain.com",
    )

    mock_otel = mock.Mock()
    mock_otel_grpc = mock_otel.instrumentation.grpc
    monkeypatch.setitem(sys.modules, "opentelemetry", mock_otel)
    monkeypatch.setitem(
        sys.modules, "opentelemetry.instrumentation", mock_otel.instrumentation
    )
    monkeypatch.setitem(
        sys.modules, "opentelemetry.instrumentation.grpc", mock_otel_grpc
    )

    result = _observability.get_otel_async_interceptor(client_options=options)
    assert result is not None

    args, kwargs = mock_otel_grpc.aio_client_interceptors.call_args
    req_hook = kwargs["request_hook"]
    assert req_hook is not _observability._grpc_client_request_hook
    assert kwargs["response_hook"] is _observability._grpc_client_response_hook

    mock_span = mock.Mock()
    mock_span.is_recording.return_value = True
    req_hook(mock_span, None)
    mock_span.set_attribute.assert_any_call(
        "server.address", "secretmanager.googleapis.com"
    )
    mock_span.set_attribute.assert_any_call("server.port", 8443)
    mock_span.set_attribute.assert_any_call("url.domain", "custom-domain.com")


def test_grpc_client_response_hook_success():
    """Proves that _grpc_client_response_hook sets rpc.response.status_code to 'OK' on success."""
    mock_span = mock.Mock()
    mock_span.is_recording.return_value = True
    _observability._grpc_client_response_hook(mock_span, mock.Mock())
    mock_span.set_attribute.assert_called_once_with("rpc.response.status_code", "OK")


def test_grpc_client_response_hook_not_recording():
    """Proves that _grpc_client_response_hook skips non-recording spans."""
    mock_span = mock.Mock()
    mock_span.is_recording.return_value = False
    _observability._grpc_client_response_hook(mock_span, mock.Mock())
    mock_span.set_attribute.assert_not_called()


def test_grpc_client_response_hook_error_status():
    """Proves that _grpc_client_response_hook skips spans marked with ERROR status."""
    mock_span = mock.Mock()
    mock_span.is_recording.return_value = True
    mock_span.status.status_code.name = "ERROR"
    _observability._grpc_client_response_hook(mock_span, mock.Mock())
    mock_span.set_attribute.assert_not_called()


def test_grpc_client_response_hook_error_status_value():
    """Proves that _grpc_client_response_hook skips spans with StatusCode.ERROR value (2)."""
    mock_span = mock.Mock()
    mock_span.is_recording.return_value = True
    mock_span.status.status_code.name = "UNKNOWN"
    mock_span.status.status_code.value = 2
    _observability._grpc_client_response_hook(mock_span, mock.Mock())
    mock_span.set_attribute.assert_not_called()


def test_grpc_client_response_hook_none_span():
    """Proves that _grpc_client_response_hook gracefully handles span=None without error."""
    _observability._grpc_client_response_hook(None, mock.Mock())


def test_get_otel_interceptor_sentinel_attribute(monkeypatch):
    """Proves that get_otel_interceptor tags the returned closure with _is_otel_interceptor=True."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    options = ClientOptions()

    mock_otel = mock.Mock()
    monkeypatch.setitem(sys.modules, "opentelemetry", mock_otel)
    monkeypatch.setitem(
        sys.modules, "opentelemetry.instrumentation", mock_otel.instrumentation
    )
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.instrumentation.grpc",
        mock_otel.instrumentation.grpc,
    )

    interceptor = _observability.get_otel_interceptor(client_options=options)
    assert callable(interceptor)
    assert getattr(interceptor, "_is_otel_interceptor", None) is True


def test_build_http_span_attributes_with_request():
    """Proves that _build_http_span_attributes extracts attributes from a request object."""
    headers = {"key": "val"}
    request = mock.Mock(
        method="post",
        url="https://example.com:8443/v1/echo",
        headers=headers,
        body=b"bytes-payload",
    )
    name, attrs, res_headers = _observability._TraceContext._build_http_span_attributes(
        request, url_template="/v1/echo"
    )
    assert name == "POST /v1/echo"
    assert attrs["http.request.method"] == "POST"
    assert attrs["server.address"] == "example.com"
    assert attrs["server.port"] == 8443
    assert attrs["url.template"] == "/v1/echo"
    assert attrs["url.full"] == "https://example.com:8443/v1/echo"
    assert attrs["http.request.body.size"] == len(b"bytes-payload")
    assert res_headers is headers


def test_build_http_span_attributes_with_kwargs():
    """Proves that _build_http_span_attributes works with explicit kwargs and string body."""
    headers = {"key": "val"}
    options = ClientOptions(api_endpoint="custom.endpoint.com:9443")
    name, attrs, res_headers = _observability._TraceContext._build_http_span_attributes(
        method="get",
        url="https://custom.endpoint.com:9443/v1/items",
        url_template="/v1/items",
        headers=headers,
        body="string-body",
        client_options=options,
    )
    assert name == "GET /v1/items"
    assert attrs["server.address"] == "custom.endpoint.com"
    assert attrs["server.port"] == 9443
    assert attrs["http.request.body.size"] == len("string-body")
    assert res_headers is headers


def test_build_http_span_attributes_client_options():
    """Proves that _build_http_span_attributes extracts server.address from client_options."""
    options = ClientOptions(api_endpoint="custom.endpoint.com:443")
    name, attrs, res_headers = _observability._TraceContext._build_http_span_attributes(
        method="GET",
        url="https://custom.endpoint.com:443/test",
        client_options=options,
    )
    assert name == "GET"
    assert attrs["server.address"] == "custom.endpoint.com"


def test_build_http_span_attributes_url_parsing_fallbacks():
    """Proves that _build_http_span_attributes gracefully handles empty or invalid URLs."""
    # Empty url
    name, attrs, _ = _observability._TraceContext._build_http_span_attributes(
        method="DELETE", url=""
    )
    assert name == "DELETE"
    assert attrs["server.address"] == ""
    assert attrs["server.port"] == 443

    # Malformed URL
    with mock.patch.object(
        urllib.parse, "urlsplit", side_effect=ValueError("boom"), autospec=True
    ):
        name, attrs, _ = _observability._TraceContext._build_http_span_attributes(
            method="PUT", url="http://[invalid"
        )
        assert name == "PUT"
        assert attrs["server.address"] == ""


def test_trace_http_request_disabled():
    """Proves that trace_http_request yields a context with no active span when tracing is disabled."""
    request = mock.Mock(method="GET", url="https://example.com/api", headers={})
    with _observability.trace_http_request(
        request, client_options=ClientOptions()
    ) as ctx:
        assert isinstance(ctx, _observability._TraceContext)
        assert ctx._span is None
        ctx.record_response(mock.Mock())


def test_trace_http_request_active(monkeypatch):
    """Proves that trace_http_request creates a span, sets attributes, and injects W3C headers."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")

    mock_tracer = mock.MagicMock()
    mock_span = mock.MagicMock()
    mock_tracer.start_as_current_span.return_value.__enter__.return_value = mock_span

    mock_provider = mock.Mock()
    mock_provider.get_tracer.return_value = mock_tracer

    mock_otel = mock.MagicMock()
    mock_propagator = mock.Mock()
    mock_otel.trace.propagation.tracecontext.TraceContextTextMapPropagator.return_value = mock_propagator
    monkeypatch.setattr(_observability, "_TRACE_CONTEXT_PROPAGATOR", mock_propagator)

    monkeypatch.setitem(sys.modules, "opentelemetry", mock_otel)
    monkeypatch.setitem(sys.modules, "opentelemetry.trace", mock_otel.trace)
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.trace.propagation.tracecontext",
        mock_otel.trace.propagation.tracecontext,
    )
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.instrumentation.grpc",
        mock.Mock(),
    )

    options = ClientOptions(
        api_endpoint="custom.googleapis.com:8443",
        tracer_provider=mock_provider,
    )
    headers = {}
    request = mock.Mock(
        method="POST",
        url="https://custom.googleapis.com:8443/v1/test",
        headers=headers,
        body=b"test-body",
    )

    with _observability.trace_http_request(
        request, url_template="/v1/test", client_options=options
    ) as ctx:
        assert ctx._span is mock_span

    mock_tracer.start_as_current_span.assert_called_once()
    call_args, call_kwargs = mock_tracer.start_as_current_span.call_args
    assert call_args[0] == "POST /v1/test"
    attrs = call_kwargs["attributes"]
    assert attrs["rpc.system.name"] == "http"
    assert attrs["http.request.method"] == "POST"
    assert attrs["server.address"] == "custom.googleapis.com"
    assert attrs["server.port"] == 8443
    assert attrs["url.template"] == "/v1/test"
    assert attrs["http.request.body.size"] == 9
    mock_propagator.inject.assert_called_once_with(headers)


def test_trace_context_record_response_success(monkeypatch):
    """Proves that _TraceContext.record_response records status code and size attributes while leaving status UNSET."""
    mock_span = mock.Mock()
    response = mock.Mock(status_code=200, headers={"Content-Length": "42"})

    mock_status_mod = mock.Mock()
    monkeypatch.setitem(sys.modules, "opentelemetry.trace.status", mock_status_mod)

    ctx = _observability._TraceContext()
    ctx._span = mock_span
    ctx.record_response(response)
    mock_span.set_attribute.assert_any_call("http.response.status_code", 200)
    mock_span.set_attribute.assert_any_call("http.response.body.size", 42)
    mock_span.set_status.assert_not_called()


@pytest.mark.parametrize(
    "status_code,json_fn,expected_message",
    [
        pytest.param(
            400,
            lambda: {"error": {"message": "Invalid argument"}},
            "Invalid argument",
            id="400_bad_request_with_message",
        ),
        pytest.param(
            503,
            lambda: {"error": {"message": "Temporary glitch"}},
            "Temporary glitch",
            id="503_service_unavailable_with_message",
        ),
        pytest.param(
            503,
            None,
            None,
            id="503_without_extractable_message",
        ),
    ],
)
def test_trace_context_record_response_error_status(
    mock_otel, status_code, json_fn, expected_message
):
    """Proves that _TraceContext.record_response sets error status, error.type, and status.message on 4xx/5xx responses."""
    mock_span = mock.Mock(spec_set=["set_attribute", "set_status"])
    mock_parent_span = mock.Mock(spec_set=["set_attribute"])
    response = types.SimpleNamespace(
        status_code=status_code,
        headers={},
        json=json_fn,
    )

    ctx = _observability._TraceContext()
    ctx._span = mock_span
    ctx._parent_span = mock_parent_span
    ctx.record_response(response)

    mock_span.set_attribute.assert_any_call("http.response.status_code", status_code)
    mock_span.set_attribute.assert_any_call("error.type", str(status_code))
    if expected_message is not None:
        mock_span.set_attribute.assert_any_call("status.message", expected_message)
    mock_parent_span.set_attribute.assert_called_once_with(
        "http.response.status_code", status_code
    )
    mock_span.set_status.assert_called_once()


@pytest.mark.parametrize(
    "json_fn,text,reason,expected",
    [
        pytest.param(
            lambda: {"error": {"message": "Invalid argument"}},
            None,
            None,
            "Invalid argument",
            id="nested_dict_error_message",
        ),
        pytest.param(
            lambda: {"error": "Simple error"},
            None,
            None,
            "Simple error",
            id="string_error_field",
        ),
        pytest.param(
            lambda: {"error": {"message": ""}},
            "  Gateway timeout  ",
            None,
            "Gateway timeout",
            id="empty_json_message_falls_back_to_text",
        ),
        pytest.param(
            mock.Mock(side_effect=ValueError("No JSON"), spec_set=True),
            "",
            "Service Unavailable",
            "Service Unavailable",
            id="json_value_error_falls_back_to_reason",
        ),
        pytest.param(
            None,
            "   \n\t  ",
            "Valid Fallback Reason",
            "Valid Fallback Reason",
            id="whitespace_only_text_falls_back_to_reason",
        ),
        pytest.param(None, None, None, None, id="empty_response"),
        pytest.param(lambda: ["not-a-dict"], None, None, None, id="json_list_payload"),
        pytest.param(lambda: {"error": 123}, None, None, None, id="non_string_error"),
    ],
)
def test_extract_http_error_message_variants(json_fn, text, reason, expected):
    """Proves that _extract_http_error_message handles JSON dicts, string errors, text/reason fallbacks, and empty responses."""
    resp = types.SimpleNamespace(json=json_fn, text=text, reason=reason)
    assert _observability._TraceContext._extract_http_error_message(resp) == expected


def test_extract_http_error_message_text_property_exception():
    """Proves that _extract_http_error_message fails open when accessing .text raises an exception and falls back to .reason."""

    class _BrokenTextResponse:
        json = None
        reason = "Fallback after broken text"

        @property
        def text(self):
            raise RuntimeError("broken text property")

    assert (
        _observability._TraceContext._extract_http_error_message(_BrokenTextResponse())
        == "Fallback after broken text"
    )


def test_trace_http_request_propagates_to_parent_span(mock_otel):
    """Proves that trace_http_request propagates url.template (first attempt) and http.response.status_code to parent T3 span."""
    parent_attrs = {}
    mock_parent_span = types.SimpleNamespace(
        is_recording=lambda: True,
        attributes=parent_attrs,
        set_attribute=parent_attrs.__setitem__,
    )
    mock_otel.trace.get_current_span.return_value = mock_parent_span

    # First attempt: sets url.template on parent_span
    with _observability.trace_http_request(
        method="POST",
        url="https://example.com/v1/first",
        url_template="/v1/first",
        client_options=ClientOptions(),
    ) as ctx:
        assert ctx._parent_span is mock_parent_span
    assert parent_attrs["url.template"] == "/v1/first"

    # Second attempt with a different url_template: does NOT overwrite first attempt's url.template
    with _observability.trace_http_request(
        method="POST",
        url="https://example.com/v1/second",
        url_template="/v1/second",
        client_options=ClientOptions(),
    ):
        pass
    assert parent_attrs["url.template"] == "/v1/first"

    # Third attempt with url_template=None
    with _observability.trace_http_request(
        method="POST",
        url="https://example.com/v1/none",
        url_template=None,
        client_options=ClientOptions(),
    ):
        pass


@pytest.mark.parametrize(
    "invalid_parent_span",
    [
        pytest.param(
            types.SimpleNamespace(
                is_recording=lambda: False, set_attribute=lambda k, v: None
            ),
            id="parent_span_not_recording",
        ),
        pytest.param(
            types.SimpleNamespace(is_recording=lambda: True),
            id="parent_span_missing_set_attribute",
        ),
    ],
)
def test_trace_http_request_parent_span_capability_guards(
    mock_otel, invalid_parent_span
):
    """Proves that trace_http_request skips parent span propagation when the parent span is not recording or lacks set_attribute."""
    mock_otel.trace.get_current_span.return_value = invalid_parent_span
    with _observability.trace_http_request(
        method="POST",
        url="https://example.com/v1/guarded",
        url_template="/v1/guarded",
        client_options=ClientOptions(),
    ) as ctx:
        assert ctx._parent_span is None


def test_trace_http_request_parent_span_set_attribute_fails_open(mock_otel):
    """Proves that trace_http_request fails open when parent_span.set_attribute raises an exception."""
    failing_parent_span = types.SimpleNamespace(
        is_recording=lambda: True,
        attributes={},
        set_attribute=mock.Mock(side_effect=RuntimeError("set_attribute boom")),
    )
    mock_otel.trace.get_current_span.return_value = failing_parent_span
    with _observability.trace_http_request(
        method="POST",
        url="https://example.com/v1/fail-open",
        url_template="/v1/fail-open",
        client_options=ClientOptions(),
    ) as ctx:
        assert ctx._parent_span is failing_parent_span


def test_trace_context_record_error(monkeypatch):
    """Proves that _TraceContext.record_error records supplemental error attributes."""
    mock_span = mock.Mock()
    exc = ValueError("Network failure")

    mock_status_mod = mock.Mock()
    monkeypatch.setitem(sys.modules, "opentelemetry.trace.status", mock_status_mod)

    ctx = _observability._TraceContext()
    ctx._span = mock_span
    ctx.record_error(exc)
    mock_span.set_attribute.assert_any_call("error.type", "ValueError")
    mock_span.set_attribute.assert_any_call("status.message", "Network failure")

    # Also verify record_http_error alias
    mock_span.reset_mock()
    ctx.record_http_error(exc)
    mock_span.set_attribute.assert_any_call("error.type", "ValueError")
    mock_span.set_attribute.assert_any_call("status.message", "Network failure")


def test_trace_http_request_with_kwargs(monkeypatch):
    """Proves that trace_http_request works when invoked using keyword arguments only."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")

    mock_tracer = mock.MagicMock()
    mock_span = mock.MagicMock()
    mock_tracer.start_as_current_span.return_value.__enter__.return_value = mock_span

    mock_provider = mock.Mock()
    mock_provider.get_tracer.return_value = mock_tracer

    mock_otel = mock.MagicMock()
    mock_propagator = mock.Mock()
    mock_otel.trace.propagation.tracecontext.TraceContextTextMapPropagator.return_value = mock_propagator
    monkeypatch.setattr(_observability, "_TRACE_CONTEXT_PROPAGATOR", mock_propagator)

    monkeypatch.setitem(sys.modules, "opentelemetry", mock_otel)
    monkeypatch.setitem(sys.modules, "opentelemetry.trace", mock_otel.trace)
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.trace.propagation.tracecontext",
        mock_otel.trace.propagation.tracecontext,
    )
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.instrumentation.grpc",
        mock.Mock(),
    )

    options = ClientOptions(
        api_endpoint="custom.googleapis.com:8443",
        tracer_provider=mock_provider,
    )
    headers = {}

    with _observability.trace_http_request(
        method="post",
        url="https://custom.googleapis.com:8443/v1/test",
        headers=headers,
        body="string-payload",
        url_template="/v1/test",
        client_options=options,
    ) as ctx:
        assert ctx._span is mock_span

    call_args, call_kwargs = mock_tracer.start_as_current_span.call_args
    assert call_args[0] == "POST /v1/test"
    attrs = call_kwargs["attributes"]
    assert attrs["http.request.method"] == "POST"
    assert attrs["http.request.body.size"] == len("string-payload")
    mock_propagator.inject.assert_called_once_with(headers)


def test_trace_http_request_client_options(monkeypatch):
    """Proves that trace_http_request respects client_options when passed as keyword argument."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")

    mock_tracer = mock.MagicMock()
    mock_span = mock.MagicMock()
    mock_tracer.start_as_current_span.return_value.__enter__.return_value = mock_span

    mock_provider = mock.Mock()
    mock_provider.get_tracer.return_value = mock_tracer

    mock_otel = mock.MagicMock()
    monkeypatch.setitem(sys.modules, "opentelemetry", mock_otel)
    monkeypatch.setitem(sys.modules, "opentelemetry.trace", mock_otel.trace)
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.trace.propagation.tracecontext",
        mock_otel.trace.propagation.tracecontext,
    )
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.trace.status",
        mock.Mock(),
    )
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.instrumentation.grpc",
        mock.Mock(),
    )

    options = ClientOptions(
        api_endpoint="custom.googleapis.com:8443",
        tracer_provider=mock_provider,
    )

    ctx = _observability.trace_http_request(
        method="GET",
        url="https://custom.googleapis.com:8443/v1/test",
        client_options=options,
    )
    with ctx as trace_ctx:
        assert trace_ctx._span is mock_span
        # Test record_response method on trace context
        mock_resp = mock.Mock(status_code=200, headers={"Content-Length": "42"})
        trace_ctx.record_response(mock_resp)
        mock_span.set_attribute.assert_any_call("http.response.status_code", 200)
        mock_span.set_attribute.assert_any_call("http.response.body.size", 42)


def test_trace_http_request_default_tracer_and_url_parse(monkeypatch):
    """Proves that trace_http_request uses trace.get_tracer when tracer_provider is None,
    and extracts server.address and port from url if not present in options.
    """
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")

    mock_tracer = mock.MagicMock()
    mock_span = mock.MagicMock()
    mock_tracer.start_as_current_span.return_value.__enter__.return_value = mock_span

    mock_otel = mock.MagicMock()
    mock_otel.trace.get_tracer.return_value = mock_tracer
    monkeypatch.setitem(sys.modules, "opentelemetry", mock_otel)
    monkeypatch.setitem(sys.modules, "opentelemetry.trace", mock_otel.trace)
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.trace.propagation.tracecontext",
        mock_otel.trace.propagation.tracecontext,
    )
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.instrumentation.grpc",
        mock.Mock(),
    )

    options = ClientOptions()  # No api_endpoint, tracer_provider=None

    with _observability.trace_http_request(
        client_options=options,
        method="GET",
        url="https://parsed-host.org:9443/v1/items",
    ) as ctx:
        assert ctx._span is mock_span

    mock_otel.trace.get_tracer.assert_called_once_with("google.api_core")
    call_args, call_kwargs = mock_tracer.start_as_current_span.call_args
    attrs = call_kwargs["attributes"]
    assert attrs["server.address"] == "parsed-host.org"
    assert attrs["server.port"] == 9443


def test_trace_http_request_propagator_error(monkeypatch):
    """Proves that trace_http_request catches propagation errors silently."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")

    mock_tracer = mock.MagicMock()
    mock_span = mock.MagicMock()
    mock_tracer.start_as_current_span.return_value.__enter__.return_value = mock_span

    mock_provider = mock.Mock()
    mock_provider.get_tracer.return_value = mock_tracer

    mock_otel = mock.MagicMock()
    mock_propagator = mock.Mock()
    mock_propagator.inject.side_effect = RuntimeError("Propagator failed")
    mock_otel.trace.propagation.tracecontext.TraceContextTextMapPropagator.return_value = mock_propagator
    monkeypatch.setattr(_observability, "_TRACE_CONTEXT_PROPAGATOR", mock_propagator)

    monkeypatch.setitem(sys.modules, "opentelemetry", mock_otel)
    monkeypatch.setitem(sys.modules, "opentelemetry.trace", mock_otel.trace)
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.trace.propagation.tracecontext",
        mock_otel.trace.propagation.tracecontext,
    )
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.instrumentation.grpc",
        mock.Mock(),
    )

    options = ClientOptions(tracer_provider=mock_provider)
    headers = {}

    with _observability.trace_http_request(
        client_options=options,
        method="GET",
        url="https://example.com",
        headers=headers,
    ) as ctx:
        assert ctx._span is mock_span


def test_trace_http_request_unexpected_error(monkeypatch):
    """Proves that trace_http_request yields None when an unexpected error occurs during setup."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")

    mock_otel = mock.MagicMock()
    mock_otel.trace.get_tracer.side_effect = RuntimeError("Unexpected tracer crash")
    monkeypatch.setitem(sys.modules, "opentelemetry", mock_otel)
    monkeypatch.setitem(sys.modules, "opentelemetry.trace", mock_otel.trace)
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.instrumentation.grpc",
        mock.Mock(),
    )

    options = ClientOptions()
    with _observability.trace_http_request(
        client_options=options,
        method="GET",
        url="https://example.com",
    ) as ctx:
        assert isinstance(ctx, _observability._TraceContext)
        assert ctx._span is None
        ctx.record_response(mock.Mock())


def test_trace_context_record_response_none_or_missing_attribute():
    """Proves that _TraceContext.record_response handles None or non-span gracefully."""
    ctx_none = _observability._TraceContext()
    ctx_none._span = None
    ctx_none.record_response(mock.Mock())

    ctx_obj = _observability._TraceContext()
    ctx_obj._span = object()
    ctx_obj.record_response(mock.Mock())


def test_trace_context_record_response_content_fallback_and_invalid_content_length(
    monkeypatch,
):
    """Proves that _TraceContext.record_response handles invalid Content-Length and falls back to _content."""
    mock_span = mock.Mock()
    # Invalid Content-Length string
    response_invalid_len = mock.Mock(
        status_code=200, headers={"Content-Length": "not-an-int"}
    )
    mock_status_mod = mock.Mock()
    monkeypatch.setitem(sys.modules, "opentelemetry.trace.status", mock_status_mod)

    ctx = _observability._TraceContext()
    ctx._span = mock_span
    ctx.record_response(response_invalid_len)
    mock_span.set_attribute.assert_called_once_with("http.response.status_code", 200)

    mock_span.reset_mock()
    # No Content-Length header, but response._content is present
    response_with_content = mock.Mock(
        status_code=None, headers={}, _content=b"hello-content"
    )
    ctx.record_response(response_with_content)
    mock_span.set_attribute.assert_called_once_with(
        "http.response.body.size", len(b"hello-content")
    )


def test_trace_context_record_response_exception_handled(monkeypatch):
    """Proves that _TraceContext.record_response catches exceptions gracefully."""
    mock_span = mock.Mock()
    mock_span.set_attribute.side_effect = RuntimeError("attribute error")
    mock_status_mod = mock.Mock()
    monkeypatch.setitem(sys.modules, "opentelemetry.trace.status", mock_status_mod)

    ctx = _observability._TraceContext()
    ctx._span = mock_span
    # Should not raise
    ctx.record_response(mock.Mock(status_code=200, headers={}))


def test_trace_context_record_error_none_span():
    """Proves that _TraceContext.record_error handles span=None gracefully."""
    ctx = _observability._TraceContext()
    ctx._span = None
    ctx.record_error(ValueError("test"))


def test_trace_context_record_error_with_status_code_and_empty_msg(monkeypatch):
    """Proves that _TraceContext.record_error uses exc.code or exc.status_code when present,
    and skips status.message when str(exc) is empty.
    """
    mock_span = mock.Mock()
    exc = Exception()
    exc.code = 404

    mock_status_mod = mock.Mock()
    monkeypatch.setitem(sys.modules, "opentelemetry.trace.status", mock_status_mod)

    ctx = _observability._TraceContext()
    ctx._span = mock_span
    ctx.record_error(exc)
    mock_span.set_attribute.assert_any_call("error.type", "404")
    # str(exc) is empty, status.message should not be set
    calls = [c[0][0] for c in mock_span.set_attribute.call_args_list]
    assert "status.message" not in calls


def test_trace_context_record_error_exception_handled(monkeypatch):
    """Proves that _TraceContext.record_error catches exceptions gracefully."""
    mock_span = mock.Mock()
    mock_span.set_attribute.side_effect = RuntimeError("crash")
    mock_status_mod = mock.Mock()
    monkeypatch.setitem(sys.modules, "opentelemetry.trace.status", mock_status_mod)

    # Should not raise
    ctx = _observability._TraceContext()
    ctx._span = mock_span
    ctx.record_error(ValueError("test"))


def test_trace_http_request_url_parse_exception(monkeypatch):
    """Proves that trace_http_request handles url parsing errors gracefully."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")

    mock_tracer = mock.MagicMock()
    mock_span = mock.MagicMock()
    mock_tracer.start_as_current_span.return_value.__enter__.return_value = mock_span

    mock_otel = mock.MagicMock()
    mock_otel.trace.get_tracer.return_value = mock_tracer
    monkeypatch.setitem(sys.modules, "opentelemetry", mock_otel)
    monkeypatch.setitem(sys.modules, "opentelemetry.trace", mock_otel.trace)
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.trace.propagation.tracecontext",
        mock_otel.trace.propagation.tracecontext,
    )
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.instrumentation.grpc",
        mock.Mock(),
    )

    with mock.patch.object(
        urllib.parse, "urlsplit", side_effect=ValueError("Invalid URL"), autospec=True
    ):
        options = ClientOptions()
        with _observability.trace_http_request(
            client_options=options,
            method="GET",
            url="http://[invalid-url",
        ) as ctx:
            assert ctx._span is mock_span


def test_trace_http_request_empty_url(monkeypatch):
    """Proves that trace_http_request works when url is empty or None."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")

    mock_tracer = mock.MagicMock()
    mock_span = mock.MagicMock()
    mock_tracer.start_as_current_span.return_value.__enter__.return_value = mock_span

    mock_otel = mock.MagicMock()
    mock_otel.trace.get_tracer.return_value = mock_tracer
    monkeypatch.setitem(sys.modules, "opentelemetry", mock_otel)
    monkeypatch.setitem(sys.modules, "opentelemetry.trace", mock_otel.trace)
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.trace.propagation.tracecontext",
        mock_otel.trace.propagation.tracecontext,
    )
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.instrumentation.grpc",
        mock.Mock(),
    )

    options = ClientOptions()
    with _observability.trace_http_request(
        client_options=options,
        method="GET",
        url="",
    ) as ctx:
        assert ctx._span is mock_span


def test_trace_context_record_response_content_len_error(monkeypatch):
    """Proves _TraceContext.record_response catches errors in response._content length calculation."""
    mock_span = mock.Mock()
    mock_status_mod = mock.Mock()
    monkeypatch.setitem(sys.modules, "opentelemetry.trace.status", mock_status_mod)

    response = mock.Mock(status_code=200, headers={})
    # Set _content to an object that raises TypeError on len()
    response._content = object()

    ctx = _observability._TraceContext()
    ctx._span = mock_span
    ctx.record_response(response)


def test_trace_context_record_error_partial_span(monkeypatch):
    """Proves that _TraceContext.record_error handles spans with missing methods."""
    mock_status_mod = mock.Mock()
    monkeypatch.setitem(sys.modules, "opentelemetry.trace.status", mock_status_mod)

    # Object with set_attribute
    class MinimalSpan:
        def __init__(self):
            self.attrs = {}

        def set_attribute(self, k, v):
            self.attrs[k] = v

    span = MinimalSpan()
    ctx = _observability._TraceContext()
    ctx._span = span
    ctx.record_error(ValueError("partial span"))
    assert span.attrs["error.type"] == "ValueError"

    # Object lacking set_attribute
    class NoAttrSpan:
        pass

    span2 = NoAttrSpan()
    ctx2 = _observability._TraceContext()
    ctx2._span = span2
    # Should not raise AttributeError
    ctx2.record_error(ValueError("no attr span"))


def test_trace_context_record_response_no_content_length_and_no_content(monkeypatch):
    """Proves that _TraceContext.record_response handles responses with neither Content-Length nor _content."""
    mock_span = mock.Mock()
    mock_status_mod = mock.Mock()
    monkeypatch.setitem(sys.modules, "opentelemetry.trace.status", mock_status_mod)

    response = mock.Mock(spec=["status_code", "headers"], status_code=200, headers={})
    ctx = _observability._TraceContext()
    ctx._span = mock_span
    ctx.record_response(response)
    mock_span.set_attribute.assert_called_once_with("http.response.status_code", 200)


def test_trace_http_request_records_error_and_reraises(monkeypatch):
    """Proves that trace_http_request records error on active span when exception occurs."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")

    mock_span = mock.MagicMock()
    mock_tracer = mock.MagicMock()
    mock_tracer.start_as_current_span.return_value.__enter__.return_value = mock_span

    mock_otel = mock.MagicMock()
    mock_otel.trace.get_tracer.return_value = mock_tracer
    monkeypatch.setitem(sys.modules, "opentelemetry", mock_otel)
    monkeypatch.setitem(sys.modules, "opentelemetry.trace", mock_otel.trace)
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.trace.propagation.tracecontext",
        mock_otel.trace.propagation.tracecontext,
    )
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.instrumentation.grpc",
        mock.Mock(),
    )
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.trace.status",
        mock_otel.trace.status,
    )

    err = RuntimeError("network broke")
    with pytest.raises(RuntimeError, match="network broke"):
        with _observability.trace_http_request(
            method="GET",
            url="https://example.com/fail",
            headers={},
        ):
            raise err

    mock_span.set_attribute.assert_any_call("error.type", "RuntimeError")
    mock_span.set_attribute.assert_any_call("status.message", "network broke")


def test_trace_http_request_no_multi_yield_bug(monkeypatch):
    """Proves that exceptions in caller block cleanly propagate without RuntimeError."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")

    mock_span = mock.MagicMock()
    mock_tracer = mock.MagicMock()
    mock_tracer.start_as_current_span.return_value.__enter__.return_value = mock_span

    mock_otel = mock.MagicMock()
    mock_otel.trace.get_tracer.return_value = mock_tracer
    monkeypatch.setitem(sys.modules, "opentelemetry", mock_otel)
    monkeypatch.setitem(sys.modules, "opentelemetry.trace", mock_otel.trace)
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.trace.propagation.tracecontext",
        mock_otel.trace.propagation.tracecontext,
    )
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.instrumentation.grpc",
        mock.Mock(),
    )

    err = ConnectionResetError("connection reset by peer")
    with pytest.raises(ConnectionResetError, match="connection reset by peer"):
        with _observability.trace_http_request(
            method="GET",
            url="https://example.com/api",
        ):
            raise err


def test_trace_http_request_initialization_fails_open(monkeypatch):
    """Proves that unexpected exceptions during telemetry initialization fail open and yield None."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    monkeypatch.setitem(
        sys.modules,
        "opentelemetry.instrumentation.grpc",
        mock.Mock(),
    )
    with mock.patch(
        "opentelemetry.trace.get_tracer",
        side_effect=RuntimeError("OTel crashed"),
    ):
        with _observability.trace_http_request(
            client_options=ClientOptions(),
            method="GET",
            url="https://example.com",
        ) as ctx:
            assert isinstance(ctx, _observability._TraceContext)
            assert ctx._span is None
            ctx.record_response(mock.Mock())


@pytest.mark.parametrize(
    "method_name",
    [
        "intercept_unary_unary",
        "intercept_unary_stream",
        "intercept_stream_unary",
        "intercept_stream_stream",
    ],
    ids=["unary_unary", "unary_stream", "stream_unary", "stream_stream"],
)
def test_sync_suppressing_interceptor_invocations(method_name):
    """Verifies that _SuppressingClientInterceptor wraps downstream calls in suppress_instrumentation.

    When global OpenTelemetry gRPC auto-instrumentation is enabled, it emits
    generic, un-enriched attempt spans. We wrap downstream calls in
    suppress_instrumentation so only our enriched Google Cloud SDK T4 span is emitted.
    """
    suppressor = _observability._SuppressingClientInterceptor()

    with mock.patch(
        "google.api_core._observability._suppress_instrumentation"
    ) as mock_suppress:
        mock_continuation = mock.Mock(return_value="expected_response")
        interceptor_method = getattr(suppressor, method_name)
        result = interceptor_method(
            mock_continuation, "call_details", "request_or_iterator"
        )

        assert result == "expected_response"
        mock_continuation.assert_called_once_with("call_details", "request_or_iterator")
        mock_suppress.assert_called_once()


def test_suppressing_interceptors_define_slots():
    """Verifies that suppressing interceptor classes explicitly define __slots__ = ()."""
    assert _observability._SuppressingClientInterceptor.__slots__ == ()
    assert _observability._AsyncSuppressingClientInterceptor.__slots__ == ()
    assert "__dict__" not in _observability._SuppressingClientInterceptor.__dict__
    assert "__dict__" not in _observability._AsyncSuppressingClientInterceptor.__dict__
