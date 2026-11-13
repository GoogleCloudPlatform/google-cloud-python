# Copyright 2017 Google LLC
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

import concurrent.futures
import datetime
import logging
import sys
import types
from unittest import mock

import pytest

try:
    import grpc  # noqa: F401
except ImportError:
    pytest.skip("No GRPC", allow_module_level=True)


import google.api_core.gapic_v1.method
import google.api_core.page_iterator
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions, retry, timeout
from google.api_core.gapic_v1 import client_info
from tests.helpers import assert_uninstrumented_gapic_callable

_DEFAULT_SPAN_ATTRIBUTES = {
    "rpc.system.name": "grpc",
    "rpc.method": "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
    "url.domain": "googleapis.com",
}


def _utcnow_monotonic():
    curr_value = datetime.datetime.min
    delta = datetime.timedelta(seconds=0.5)
    while True:
        yield curr_value
        curr_value += delta


def test_wrap_method_basic():
    method = mock.Mock(spec=["__call__"], return_value=42)

    wrapped_method = google.api_core.gapic_v1.method.wrap_method(method)

    result = wrapped_method(1, 2, meep="moop")

    assert result == 42
    method.assert_called_once_with(1, 2, meep="moop", metadata=mock.ANY)

    # Check that the default client info was specified in the metadata.
    metadata = method.call_args[1]["metadata"]
    assert len(metadata) == 1
    client_info = google.api_core.gapic_v1.client_info.DEFAULT_CLIENT_INFO
    user_agent_metadata = client_info.to_grpc_metadata()
    assert user_agent_metadata in metadata


def test_wrap_method_with_no_client_info():
    method = mock.Mock(spec=["__call__"])

    wrapped_method = google.api_core.gapic_v1.method.wrap_method(
        method, client_info=None
    )

    wrapped_method(1, 2, meep="moop")

    method.assert_called_once_with(1, 2, meep="moop")


def test_wrap_method_with_custom_client_info():
    client_info = google.api_core.gapic_v1.client_info.ClientInfo(
        python_version=1,
        grpc_version=2,
        api_core_version=3,
        gapic_version=4,
        client_library_version=5,
        protobuf_runtime_version=6,
    )
    method = mock.Mock(spec=["__call__"])

    wrapped_method = google.api_core.gapic_v1.method.wrap_method(
        method, client_info=client_info
    )

    wrapped_method(1, 2, meep="moop")

    method.assert_called_once_with(1, 2, meep="moop", metadata=mock.ANY)

    # Check that the custom client info was specified in the metadata.
    metadata = method.call_args[1]["metadata"]
    assert client_info.to_grpc_metadata() in metadata


def test_invoke_wrapped_method_with_metadata():
    method = mock.Mock(spec=["__call__"])

    wrapped_method = google.api_core.gapic_v1.method.wrap_method(method)

    wrapped_method(mock.sentinel.request, metadata=[("a", "b")])

    method.assert_called_once_with(mock.sentinel.request, metadata=mock.ANY)
    metadata = method.call_args[1]["metadata"]
    # Metadata should have two items: the client info metadata and our custom
    # metadata.
    assert len(metadata) == 2
    assert ("a", "b") in metadata


def test_invoke_wrapped_method_with_metadata_as_none():
    method = mock.Mock(spec=["__call__"])

    wrapped_method = google.api_core.gapic_v1.method.wrap_method(method)

    wrapped_method(mock.sentinel.request, metadata=None)

    method.assert_called_once_with(mock.sentinel.request, metadata=mock.ANY)
    metadata = method.call_args[1]["metadata"]
    # Metadata should have just one items: the client info metadata.
    assert len(metadata) == 1


def test_invoke_wrapped_method_no_client_info_with_custom_metadata():
    method = mock.Mock(spec=["__call__"])

    wrapped_method = google.api_core.gapic_v1.method.wrap_method(
        method, client_info=None
    )

    wrapped_method(mock.sentinel.request, metadata=[("custom-header", "value")])

    method.assert_called_once_with(
        mock.sentinel.request, metadata=[("custom-header", "value")]
    )


def test_extract_metrics_header_duplicate_tokens():
    metadata = [
        ("x-goog-api-client", "token1 token2"),
        ("x-goog-api-client", "token2 token3 token1"),
        ("other-header", "value"),
        ("x-goog-api-client", "token4 token2"),
    ]

    metric_str, arbitrary_metadata = (
        google.api_core.gapic_v1.method._extract_metrics_header(metadata)
    )

    # Should maintain order of first appearance and eliminate duplicates
    assert metric_str == "token1 token2 token3 token4"
    assert arbitrary_metadata == [("other-header", "value")]


def test_invoke_wrapped_method_with_duplicate_x_goog_api_client_metadata():
    method = mock.Mock(spec=["__call__"])

    # Create a custom ClientInfo with defined properties so we know exactly what is returned
    client_info = google.api_core.gapic_v1.client_info.ClientInfo(
        user_agent="custom-user-agent/1.0",
        python_version="3.14.0",
        grpc_version="1.76.0",
        api_core_version="2.29.0",
    )

    wrapped_method = google.api_core.gapic_v1.method.wrap_method(
        method, client_info=client_info
    )

    # Invoke the wrapped method with an explicit user-provided custom header that contains duplicates
    # both within its own items and overlapping with the default client_info
    wrapped_method(
        mock.sentinel.request,
        metadata=[
            ("x-goog-api-client", "override-client/2.0"),
            (
                "x-goog-api-client",
                "override-client/2.0 grpc/1.76.0 custom-user-agent/1.0",
            ),
            ("other-header", "value"),
        ],
    )

    method.assert_called_once_with(mock.sentinel.request, metadata=mock.ANY)
    metadata = method.call_args[1]["metadata"]

    # There should only be one "x-goog-api-client" header, containing both values joined by space,
    # plus the other-header.
    assert len(metadata) == 2
    metadata_dict = dict(metadata)
    assert "other-header" in metadata_dict
    assert metadata_dict["other-header"] == "value"
    assert "x-goog-api-client" in metadata_dict
    # Verify both the user-provided override value and the library system telemetry are merged explicitly
    assert (
        metadata_dict["x-goog-api-client"]
        == "custom-user-agent/1.0 gl-python/3.14.0 grpc/1.76.0 gax/2.29.0 override-client/2.0"
    )


@mock.patch("time.sleep")
def test_wrap_method_with_default_retry_and_timeout_and_compression(unused_sleep):
    method = mock.Mock(
        spec=["__call__"], side_effect=[exceptions.InternalServerError(None), 42]
    )
    default_retry = retry.Retry()
    default_timeout = timeout.ConstantTimeout(60)
    default_compression = grpc.Compression.Gzip
    wrapped_method = google.api_core.gapic_v1.method.wrap_method(
        method, default_retry, default_timeout, default_compression
    )

    result = wrapped_method()

    assert result == 42
    assert method.call_count == 2
    method.assert_called_with(
        timeout=60, compression=default_compression, metadata=mock.ANY
    )


@mock.patch("time.sleep")
def test_wrap_method_with_default_retry_and_timeout_using_sentinel(unused_sleep):
    method = mock.Mock(
        spec=["__call__"], side_effect=[exceptions.InternalServerError(None), 42]
    )
    default_retry = retry.Retry()
    default_timeout = timeout.ConstantTimeout(60)
    default_compression = grpc.Compression.Gzip
    wrapped_method = google.api_core.gapic_v1.method.wrap_method(
        method, default_retry, default_timeout, default_compression
    )

    result = wrapped_method(
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        compression=google.api_core.gapic_v1.method.DEFAULT,
    )

    assert result == 42
    assert method.call_count == 2
    method.assert_called_with(
        timeout=60, compression=default_compression, metadata=mock.ANY
    )


@mock.patch("time.sleep")
def test_wrap_method_with_overriding_retry_timeout_compression(unused_sleep):
    method = mock.Mock(spec=["__call__"], side_effect=[exceptions.NotFound(None), 42])
    default_retry = retry.Retry()
    default_timeout = timeout.ConstantTimeout(60)
    default_compression = grpc.Compression.Gzip
    wrapped_method = google.api_core.gapic_v1.method.wrap_method(
        method, default_retry, default_timeout, default_compression
    )

    result = wrapped_method(
        retry=retry.Retry(retry.if_exception_type(exceptions.NotFound)),
        timeout=timeout.ConstantTimeout(22),
        compression=grpc.Compression.Deflate,
    )

    assert result == 42
    assert method.call_count == 2
    method.assert_called_with(
        timeout=22,
        compression=grpc.Compression.Deflate,
        metadata=mock.ANY,
    )


@pytest.mark.skip(reason="Known flaky due to floating point comparison. #866")
def test_wrap_method_with_overriding_timeout_as_a_number():
    method = mock.Mock(spec=["__call__"], return_value=42)
    default_retry = retry.Retry()
    default_timeout = timeout.ConstantTimeout(60)
    wrapped_method = google.api_core.gapic_v1.method.wrap_method(
        method, default_retry, default_timeout
    )

    # Using "result = wrapped_method(timeout=22)" fails since wrapped_method
    # does floating point calculations that results in 21.987.. instead of 22
    result = wrapped_method(timeout=22)

    assert result == 42

    actual_timeout = method.call_args[1]["timeout"]
    metadata = method.call_args[1]["metadata"]
    assert metadata == mock.ANY
    assert actual_timeout == pytest.approx(22, abs=0.01)


def test_wrap_method_with_overriding_constant_timeout():
    method = mock.Mock(spec=["__call__"], return_value=42)
    default_retry = retry.Retry()
    default_timeout = timeout.ConstantTimeout(60)
    wrapped_method = google.api_core.gapic_v1.method.wrap_method(
        method, default_retry, default_timeout
    )

    result = wrapped_method(timeout=timeout.ConstantTimeout(22))

    assert result == 42

    actual_timeout = method.call_args[1]["timeout"]
    metadata = method.call_args[1]["metadata"]
    assert metadata == mock.ANY
    assert actual_timeout == 22


def test_wrap_method_with_call():
    method = mock.Mock()
    mock_call = mock.Mock()
    method.with_call.return_value = 42, mock_call

    wrapped_method = google.api_core.gapic_v1.method.wrap_method(method, with_call=True)
    result = wrapped_method()
    assert len(result) == 2
    assert result[0] == 42
    assert result[1] == mock_call


def test_wrap_method_with_call_not_supported():
    """Raises an error if wrapped callable doesn't have with_call method."""
    method = lambda: None  # noqa: E731

    with pytest.raises(ValueError) as exc_info:
        google.api_core.gapic_v1.method.wrap_method(method, with_call=True)
    assert "with_call=True is only supported for unary calls" in str(exc_info.value)


@pytest.mark.parametrize(
    "headers,expected",
    [
        ((), ""),
        (("",), ""),
        ((None,), ""),
        (("", None, ""), ""),
        (("token1",), "token1"),
        (("token1 token1",), "token1"),
        (("token1", "token1"), "token1"),
        (("token1 token2 token1",), "token1 token2"),
        (("token1", "token2", "token1"), "token1 token2"),
        (("token1 token2", "token2 token3"), "token1 token2 token3"),
        (("token1", None, "token2", "", "token1"), "token1 token2"),
    ],
)
def test__deduplicate_metadata_tokens(headers, expected):
    dedup = google.api_core.gapic_v1.method._deduplicate_metadata_tokens
    assert dedup(*headers) == expected


@pytest.mark.parametrize(
    "kwargs,capabilities_enabled",
    [
        (
            {
                "method_name": "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets"
            },
            False,
        ),
        ({}, True),
        (
            {
                "method_name": "/google.cloud.secretmanager.v1.SecretManagerService/StreamingRead",
                "is_streaming": True,
            },
            True,
        ),
        (
            {
                "method_name": "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
                "kind": "custom_unsupported",
            },
            True,
        ),
        (
            {
                "method_name": "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
                "kind": "rest_asyncio",
            },
            True,
        ),
        (
            {
                "method_name": "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
                "kind": "grpc_asyncio",
            },
            True,
        ),
        (
            {
                "method_name": "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
                "kind": "http",
            },
            True,
        ),
    ],
    ids=[
        "disabled_by_flag",
        "omitted_method_name",
        "streaming_skipped",
        "custom_unsupported_kind_skipped",
        "rest_asyncio_kind_skipped",
        "grpc_asyncio_kind_skipped",
        "http_kind_skipped",
    ],
)
def test_wrap_method_otel_tracing_skips_span(monkeypatch, kwargs, capabilities_enabled):
    """Proves that under various gating conditions, no Tier 3 span is created."""
    mock_target = mock.Mock(return_value="success")
    mock_trace = mock.Mock()

    with (
        mock.patch(
            "google.api_core._observability.is_otel_capabilities_enabled",
            return_value=capabilities_enabled,
        ),
        mock.patch.dict(
            sys.modules,
            {
                "opentelemetry": mock.Mock(trace=mock_trace),
                "opentelemetry.trace": mock_trace,
            },
        ),
    ):
        wrapped = google.api_core.gapic_v1.method.wrap_method(mock_target, **kwargs)
        result = wrapped()

    assert_uninstrumented_gapic_callable(
        wrapped, result, mock_target, mock_trace=mock_trace
    )


@pytest.mark.parametrize("kind", ["grpc", "rest"])
def test_wrap_method_otel_tracing_enabled_success(mock_otel, kind):
    """Proves that when OpenTelemetry tracing is enabled and method_name is passed, a T3 client span is started."""
    mock_target = mock.Mock(return_value="success")

    wrapped = google.api_core.gapic_v1.method.wrap_method(
        mock_target,
        default_timeout=60,
        method_name="/google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
        kind=kind,
    )
    result = wrapped()

    assert result == "success"
    expected_attributes = {
        "rpc.system.name": "http" if kind == "rest" else "grpc",
        "rpc.method": "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
        "url.domain": "googleapis.com",
    }
    mock_otel.tracer.start_as_current_span.assert_called_once_with(
        "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
        kind="INTERNAL",
        attributes=expected_attributes,
    )
    mock_otel.span.set_attribute.assert_called_with("rpc.response.status_code", "OK")


def test_wrap_method_otel_tracing_custom_client_options(mock_otel):
    """Proves that providing client_options with a custom tracer_provider uses that provider."""
    mock_target = mock.Mock(return_value="success")

    mock_provider = mock.Mock()
    mock_provider.get_tracer.return_value = mock_otel.tracer

    client_options = client_options_lib.ClientOptions(tracer_provider=mock_provider)

    wrapped = google.api_core.gapic_v1.method.wrap_method(
        mock_target,
        client_options=client_options,
        method_name="/google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
    )
    result = wrapped()

    assert result == "success"
    mock_provider.get_tracer.assert_called_once_with("google.api_core")
    mock_otel.tracer.start_as_current_span.assert_called_once_with(
        "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
        kind="INTERNAL",
        attributes=_DEFAULT_SPAN_ATTRIBUTES,
    )
    mock_otel.span.set_attribute.assert_called_with("rpc.response.status_code", "OK")


def test_wrap_method_otel_tracing_dict_client_options(mock_otel):
    """Proves that providing client_options as a dict with tracer_provider uses that provider."""
    mock_target = mock.Mock(return_value="success")

    mock_provider = mock.Mock()
    mock_provider.get_tracer.return_value = mock_otel.tracer

    client_options = {"tracer_provider": mock_provider}

    wrapped = google.api_core.gapic_v1.method.wrap_method(
        mock_target,
        client_options=client_options,
        method_name="/google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
    )
    result = wrapped()

    assert result == "success"
    mock_provider.get_tracer.assert_called_once_with("google.api_core")
    mock_otel.tracer.start_as_current_span.assert_called_once_with(
        "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
        kind="INTERNAL",
        attributes=_DEFAULT_SPAN_ATTRIBUTES,
    )
    mock_otel.span.set_attribute.assert_called_with("rpc.response.status_code", "OK")


def test_wrap_method_otel_tracing_enabled_error(mock_otel):
    """Proves that when an RPC fails, the T3 client span enriches the status code attribute."""
    err = RuntimeError("gRPC connection reset")
    mock_target = mock.Mock(side_effect=err)

    wrapped = google.api_core.gapic_v1.method.wrap_method(
        mock_target,
        method_name="/google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
    )
    with pytest.raises(RuntimeError):
        wrapped()

    mock_target.assert_called_once()
    mock_otel.span.set_attribute.assert_any_call(
        "rpc.response.status_code", "RuntimeError"
    )
    mock_otel.span.set_attribute.assert_any_call("error.type", "RuntimeError")
    mock_otel.span.set_attribute.assert_any_call(
        "status.message", "gRPC connection reset"
    )


@pytest.mark.parametrize("interrupt_exc", [KeyboardInterrupt, SystemExit])
def test_wrap_method_otel_tracing_interrupt_bypasses_error_attributes(
    mock_otel, interrupt_exc
):
    """Proves that process-level interrupts are re-raised without polluting span error attributes."""
    mock_target = mock.Mock(side_effect=interrupt_exc())

    wrapped = google.api_core.gapic_v1.method.wrap_method(
        mock_target,
        method_name="/google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
    )
    with pytest.raises(interrupt_exc):
        wrapped()

    # The span should NOT record error attributes for process-level interruptions
    for call in mock_otel.span.set_attribute.call_args_list:
        attr_name = call[0][0]
        assert attr_name not in (
            "rpc.response.status_code",
            "error.type",
            "status.message",
        )


@pytest.mark.parametrize(
    "exc,expected_status",
    [
        (exceptions.NotFound("not found"), "NOT_FOUND"),
        (exceptions.ServiceUnavailable("unavail"), "UNAVAILABLE"),
        (
            exceptions.RetryError(
                "timeout", cause=exceptions.ServiceUnavailable("err")
            ),
            "UNAVAILABLE",
        ),
    ],
    ids=["not_found", "unavailable", "retry_error_with_cause"],
)
def test_wrap_method_otel_tracing_error_status_code_mapping(
    mock_otel, exc, expected_status
):
    """Proves that exceptions are cleanly mapped to canonical rpc.response.status_code and error.type names."""
    mock_target = mock.Mock(side_effect=exc)

    wrapped = google.api_core.gapic_v1.method.wrap_method(
        mock_target,
        method_name="/google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
    )
    with pytest.raises(type(exc)):
        wrapped()

    mock_otel.span.set_attribute.assert_any_call(
        "rpc.response.status_code", expected_status
    )
    mock_otel.span.set_attribute.assert_any_call("error.type", expected_status)
    expected_msg = exc.cause.message if getattr(exc, "cause", None) else exc.message
    mock_otel.span.set_attribute.assert_any_call("status.message", expected_msg)


def test_wrap_method_otel_tracing_import_error(monkeypatch):
    """Proves that if opentelemetry raises ImportError, execution proceeds gracefully."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    mock_target = mock.Mock(return_value="success")

    with (
        mock.patch(
            "google.api_core._observability.is_otel_capabilities_enabled",
            return_value=True,
        ),
        mock.patch.dict(
            sys.modules,
            {
                "opentelemetry": None,
                "opentelemetry.trace": None,
            },
        ),
    ):
        wrapped = google.api_core.gapic_v1.method.wrap_method(
            mock_target,
            method_name="google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
        )
        result = wrapped()

    assert_uninstrumented_gapic_callable(wrapped, result, mock_target)


@pytest.mark.parametrize(
    "exc",
    [
        AttributeError("Malformed provider interface"),
        TypeError("get_tracer takes unexpected arguments"),
    ],
    ids=["attribute_error", "type_error"],
)
def test_wrap_method_otel_tracing_provider_error(monkeypatch, exc):
    """Proves that if tracer_provider raises AttributeError or TypeError, execution proceeds gracefully."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    mock_target = mock.Mock(return_value="success")

    mock_provider = mock.Mock()
    mock_provider.get_tracer.side_effect = exc
    client_options = client_options_lib.ClientOptions(tracer_provider=mock_provider)

    with mock.patch(
        "google.api_core._observability.is_otel_capabilities_enabled",
        return_value=True,
    ):
        wrapped = google.api_core.gapic_v1.method.wrap_method(
            mock_target,
            client_options=client_options,
            method_name="google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
        )
        result = wrapped()

    assert_uninstrumented_gapic_callable(wrapped, result, mock_target)


def test_wrap_method_otel_tracing_start_span_error_bypasses_tracing(mock_otel):
    """Proves that if start_as_current_span raises an Exception, execution proceeds gracefully with nullcontext."""
    mock_target = mock.Mock(return_value="success")
    mock_otel.tracer.start_as_current_span.side_effect = RuntimeError(
        "Tracing context failed"
    )

    wrapped = google.api_core.gapic_v1.method.wrap_method(
        mock_target,
        method_name="google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
    )
    result = wrapped()

    assert result == "success"
    mock_target.assert_called_once()
    mock_otel.tracer.start_as_current_span.assert_called_once()


def test_wrap_method_otel_tracing_attributes_deferred_gcp_client_omitted(mock_otel):
    """Proves that deferred gcp.client.* attributes are omitted even when client_info is provided."""
    mock_target = mock.Mock(return_value="success")

    info = client_info.ClientInfo(
        client_library_version="2.16.0",
        gapic_version="1.5.0",
    )
    info.client_repo = "googleapis/google-cloud-python-test"
    info.client_artifact = "google-cloud-secretmanager"

    wrapped = google.api_core.gapic_v1.method.wrap_method(
        mock_target,
        client_info=info,
        method_name="/google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
    )
    result = wrapped()

    assert result == "success"
    mock_otel.tracer.start_as_current_span.assert_called_once_with(
        "google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
        kind="INTERNAL",
        attributes=_DEFAULT_SPAN_ATTRIBUTES,
    )


def test_wrap_method_otel_tracing_attributes_no_service(mock_otel):
    """Proves span attributes when method_name has no service prefix."""
    mock_target = mock.Mock(return_value="success")

    wrapped = google.api_core.gapic_v1.method.wrap_method(
        mock_target,
        client_info=None,
        method_name="ListSecrets",
    )
    result = wrapped()

    assert result == "success"
    mock_otel.tracer.start_as_current_span.assert_called_once_with(
        "ListSecrets",
        kind="INTERNAL",
        attributes={
            **_DEFAULT_SPAN_ATTRIBUTES,
            "rpc.method": "ListSecrets",
        },
    )


def test_wrap_method_otel_tracing_endpoint_attributes_from_client_options(
    mock_otel,
):
    """Proves that T3 spans include url.domain, server.address, and server.port from client_options."""
    mock_target = mock.Mock(return_value="ok")
    options = client_options_lib.ClientOptions(
        api_endpoint="localhost:7469",
        universe_domain="custom.domain.com",
    )
    wrapped = google.api_core.gapic_v1.method.wrap_method(
        mock_target,
        client_options=options,
        method_name="/google.showcase.v1beta1.Echo/Echo",
        kind="grpc",
    )
    assert wrapped() == "ok"
    mock_otel.tracer.start_as_current_span.assert_called_once_with(
        "google.showcase.v1beta1.Echo/Echo",
        kind="INTERNAL",
        attributes={
            "rpc.system.name": "grpc",
            "rpc.method": "google.showcase.v1beta1.Echo/Echo",
            "url.domain": "custom.domain.com",
            "server.address": "localhost",
            "server.port": 7469,
        },
    )


def test_wrap_method_otel_tracing_endpoint_attributes_from_default_host(
    mock_otel,
):
    """Proves that T3 spans fall back to default_host when client_options.api_endpoint is unset."""
    mock_target = mock.Mock(return_value="ok")
    options = client_options_lib.ClientOptions()
    wrapped = google.api_core.gapic_v1.method.wrap_method(
        mock_target,
        client_options=options,
        method_name="/google.showcase.v1beta1.Echo/Echo",
        kind="grpc",
        default_host="localhost:7469",
    )
    assert wrapped() == "ok"
    mock_otel.tracer.start_as_current_span.assert_called_once_with(
        "google.showcase.v1beta1.Echo/Echo",
        kind="INTERNAL",
        attributes={
            "rpc.system.name": "grpc",
            "rpc.method": "google.showcase.v1beta1.Echo/Echo",
            "url.domain": "googleapis.com",
            "server.address": "localhost",
            "server.port": 7469,
        },
    )


def test_wrap_method_otel_tracing_records_gcp_error_attributes(mock_otel):
    """Proves that method spans record gcp.errors.* attributes when ErrorInfo is present."""
    error_info = types.SimpleNamespace(
        domain="googleapis.com",
        reason="RESOURCE_EXHAUSTED",
        metadata={"quota_limit": "100"},
    )
    exc = exceptions.ResourceExhausted("quota exceeded")
    exc.error_info = error_info
    mock_target = mock.Mock(side_effect=exc)

    wrapped = google.api_core.gapic_v1.method.wrap_method(
        mock_target,
        method_name="google.cloud.secretmanager.v1.SecretManagerService/ListSecrets",
    )
    with pytest.raises(exceptions.ResourceExhausted):
        wrapped()

    mock_otel.span.set_attribute.assert_any_call(
        "rpc.response.status_code", "RESOURCE_EXHAUSTED"
    )
    mock_otel.span.set_attribute.assert_any_call("gcp.errors.domain", "googleapis.com")
    mock_otel.span.set_attribute.assert_any_call("error.type", "RESOURCE_EXHAUSTED")
    mock_otel.span.set_attribute.assert_any_call(
        "gcp.errors.metadata.quota_limit", "100"
    )
    mock_otel.span.set_attribute.assert_any_call("status.message", "quota exceeded")


def test_wrap_method_otel_tracing_partial_span_capabilities(mock_otel):
    """Proves handling when span has or lacks set_attribute."""
    # Test span with set_attribute
    mock_target = mock.Mock(side_effect=ValueError("boom"))
    mock_span1 = mock.Mock(spec=["set_attribute"])
    mock_otel.tracer.start_as_current_span.return_value.__enter__.return_value = (
        mock_span1
    )

    wrapped1 = google.api_core.gapic_v1.method.wrap_method(
        mock_target,
        method_name="Service/Method",
    )
    with pytest.raises(ValueError):
        wrapped1()
    mock_span1.set_attribute.assert_any_call("rpc.response.status_code", "ValueError")
    mock_span1.set_attribute.assert_any_call("error.type", "ValueError")

    # Test span without set_attribute (e.g. mock or stub lacking set_attribute)
    mock_span2 = mock.Mock(spec=[])
    mock_otel.tracer.start_as_current_span.return_value.__enter__.return_value = (
        mock_span2
    )

    wrapped2 = google.api_core.gapic_v1.method.wrap_method(
        mock_target,
        method_name="Service/Method",
    )
    with pytest.raises(ValueError):
        wrapped2()


def test_wrap_method_uninstrumented_exception():
    """Proves that exceptions are re-raised cleanly when tracing is not enabled (span is None)."""
    mock_target = mock.Mock(side_effect=RuntimeError("uninstrumented error"))
    wrapped = google.api_core.gapic_v1.method.wrap_method(mock_target)

    with pytest.raises(RuntimeError, match="uninstrumented error"):
        wrapped()


def test_gapic_callable_logging_silent_on_success(mock_service_logger):
    """Proves _GapicCallable does not emit error logs when the RPC succeeds."""
    wrapped_ok = google.api_core.gapic_v1.method.wrap_method(
        mock.Mock(return_value="ok"),
        method_name="/google.cloud.secretmanager.v1.SecretManagerService/GetSecret",
    )
    assert wrapped_ok() == "ok"
    mock_service_logger.log.assert_not_called()


def test_gapic_callable_logging_terminal_error(mock_otel, mock_service_logger):
    """Proves _GapicCallable enriches spans and emits an ERROR log with ErrorInfo on failure."""
    error_info = types.SimpleNamespace(
        domain="googleapis.com",
        reason="SECRET_NOT_FOUND",
        metadata={"project": "my-proj"},
    )
    err = exceptions.NotFound("Secret missing")
    err._error_info = error_info
    mock_otel.span.get_span_context.return_value = types.SimpleNamespace(
        is_valid=True,
        trace_id=0x0123456789ABCDEF0123456789ABCDEF,
        span_id=0x0123456789ABCDEF,
        trace_flags=0x01,
    )
    wrapped_fail = google.api_core.gapic_v1.method.wrap_method(
        mock.Mock(side_effect=err),
        method_name="/google.cloud.secretmanager.v1.SecretManagerService/GetSecret",
        kind="rest",
    )

    with pytest.raises(exceptions.NotFound):
        wrapped_fail()

    mock_service_logger.log.assert_called_once()
    args, kwargs = mock_service_logger.log.call_args
    assert args[0] == logging.ERROR
    assert kwargs["exc_info"] is True
    extra = kwargs["extra"]
    assert (
        extra["rpcName"]
        == "/google.cloud.secretmanager.v1.SecretManagerService/GetSecret"
    )
    assert extra["rpc.system.name"] == "http"
    assert extra["rpc.response.status_code"] == "NOT_FOUND"
    assert extra["error.type"] == "SECRET_NOT_FOUND"
    assert extra["gcp.errors.domain"] == "googleapis.com"
    assert extra["gcp.errors.metadata.project"] == "my-proj"
    assert extra["status.message"] == "Secret missing"
    assert extra["exception.type"] == "NotFound"
    assert "exception.stacktrace" in extra
    assert extra["trace_id"] == "0123456789abcdef0123456789abcdef"
    assert extra["span_id"] == "0123456789abcdef"
    assert extra["json_fields"]["error.type"] == "SECRET_NOT_FOUND"


@pytest.mark.parametrize(
    "cancel_exc_factory,expected_error_type",
    [
        pytest.param(
            lambda: exceptions.Cancelled("Call cancelled"),
            "CANCELLED",
            id="google_api_core_cancelled",
        ),
        pytest.param(
            lambda: concurrent.futures.CancelledError("Future cancelled"),
            "CancelledError",
            id="concurrent_futures_cancelled_error",
        ),
    ],
)
def test_gapic_callable_logging_cancellation(
    mock_otel, mock_service_logger, cancel_exc_factory, expected_error_type
):
    """Proves _GapicCallable emits DEBUG without stacktrace on RPC or Future cancellation."""
    err = cancel_exc_factory()
    wrapped_cancel = google.api_core.gapic_v1.method.wrap_method(
        mock.Mock(side_effect=err),
        method_name="/google.cloud.secretmanager.v1.SecretManagerService/GetSecret",
    )
    with pytest.raises(type(err)):
        wrapped_cancel()

    mock_service_logger.log.assert_called_once()
    c_args, c_kwargs = mock_service_logger.log.call_args
    assert c_args[0] == logging.DEBUG
    assert c_kwargs["exc_info"] is False
    assert "exception.stacktrace" not in c_kwargs["extra"]
    assert c_kwargs["extra"]["rpc.response.status_code"] == "CANCELLED"
    assert c_kwargs["extra"]["error.type"] == expected_error_type


def test_gapic_callable_logging_fail_open_resilience(mock_otel, mock_service_logger):
    """Proves _GapicCallable fails open and re-raises caller exception if span or logger raises."""
    mock_otel.span.set_attribute.side_effect = RuntimeError("span broken")
    mock_service_logger.log.side_effect = RuntimeError("logger broken")

    wrapped_fail = google.api_core.gapic_v1.method.wrap_method(
        mock.Mock(side_effect=exceptions.NotFound("Secret missing")),
        method_name="/google.cloud.secretmanager.v1.SecretManagerService/GetSecret",
    )
    with pytest.raises(exceptions.NotFound, match="Secret missing"):
        wrapped_fail()
