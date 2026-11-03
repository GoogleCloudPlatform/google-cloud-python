# -*- coding: utf-8 -*-
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
#
"""Tests for the compatibility module for older versions of google-api-core."""

import json
import pytest
import os

from unittest import mock

import google.auth.transport.mtls

from google.cloud.eventarc_v1._compat import transcode_request
from google.cloud.eventarc_v1._compat import (
    get_universe_domain,
    get_api_endpoint,
    get_default_mtls_endpoint,
    should_use_client_cert,
    read_environment_variables,
    _observability,
    trace_http_request,
    apply_channel_interceptors,
    apply_async_channel_interceptors,
)

from google.auth.exceptions import MutualTLSChannelError
from google.api_core.universe import EmptyUniverseError
from google.protobuf import descriptor_pb2


def test_get_universe_domain():
    # When universe_domain is provided
    assert (
        get_universe_domain("foo.com", default_universe="default.com")
        == "foo.com"
    )
    assert (
        get_universe_domain("  foo.com  ", default_universe="default.com")
        == "foo.com"
    )

    # When universe_domain is None, falls back to default_universe
    assert (
        get_universe_domain(None, default_universe="default.com")
        == "default.com"
    )

    # When multiple potential universes are provided, resolves in order of preference
    assert (
        get_universe_domain(
            "foo.com", "bar.com", default_universe="default.com"
        )
        == "foo.com"
    )
    assert (
        get_universe_domain(None, "bar.com", default_universe="default.com")
        == "bar.com"
    )
    assert (
        get_universe_domain(None, None, default_universe="default.com")
        == "default.com"
    )

    # EmptyUniverseError raised when resolved value is empty string
    with pytest.raises(EmptyUniverseError) as excinfo:
        get_universe_domain("", default_universe="default.com")
    assert str(excinfo.value) == "Universe Domain cannot be an empty string."

    with pytest.raises(EmptyUniverseError) as excinfo:
        get_universe_domain("   ", default_universe="default.com")
    assert str(excinfo.value) == "Universe Domain cannot be an empty string."

    with pytest.raises(EmptyUniverseError) as excinfo:
        get_universe_domain(None, "", default_universe="default.com")
    assert str(excinfo.value) == "Universe Domain cannot be an empty string."


def test_get_default_mtls_endpoint():
    # Test valid API endpoints
    assert (
        get_default_mtls_endpoint("foo.googleapis.com")
        == "foo.mtls.googleapis.com"
    )
    assert (
        get_default_mtls_endpoint("foo.sandbox.googleapis.com")
        == "foo.mtls.sandbox.googleapis.com"
    )
    # Test case-insensitivity
    assert (
        get_default_mtls_endpoint("foo.GoogleAPIs.com")
        == "foo.mtls.googleapis.com"
    )
    assert (
        get_default_mtls_endpoint("foo.Sandbox.GoogleAPIs.com")
        == "foo.mtls.sandbox.googleapis.com"
    )

    # Test valid API endpoints with schemes
    assert (
        get_default_mtls_endpoint("https://foo.googleapis.com")
        == "https://foo.mtls.googleapis.com"
    )
    assert (
        get_default_mtls_endpoint("http://foo.googleapis.com:8080/v1")
        == "http://foo.mtls.googleapis.com:8080/v1"
    )

    # Test valid API endpoints with ports
    assert (
        get_default_mtls_endpoint("foo.googleapis.com:443")
        == "foo.mtls.googleapis.com:443"
    )
    assert (
        get_default_mtls_endpoint("foo.sandbox.googleapis.com:443")
        == "foo.mtls.sandbox.googleapis.com:443"
    )
    # Test case-insensitivity with ports
    assert (
        get_default_mtls_endpoint("foo.GoogleAPIs.com:443")
        == "foo.mtls.googleapis.com:443"
    )
    assert (
        get_default_mtls_endpoint("foo.Sandbox.GoogleAPIs.com:443")
        == "foo.mtls.sandbox.googleapis.com:443"
    )

    # Test endpoints that shouldn't be converted
    assert (
        get_default_mtls_endpoint("foo.mtls.googleapis.com")
        == "foo.mtls.googleapis.com"
    )
    assert get_default_mtls_endpoint("foo.com") == "foo.com"
    assert get_default_mtls_endpoint("foo.com:8080") == "foo.com:8080"

    # Test empty/None endpoints
    assert get_default_mtls_endpoint("") == ""
    assert get_default_mtls_endpoint(None) is None

    # Test endpoints without host
    assert get_default_mtls_endpoint("http://") == "http://"
    assert get_default_mtls_endpoint("https://") == "https://"


@pytest.mark.parametrize(
    "api_override,universe_domain,default_universe,default_mtls_endpoint,default_endpoint_template,use_mtls,expected",
    [
        (
            "foo.com",
            "googleapis.com",
            "googleapis.com",
            "foo.mtls.googleapis.com",
            "foo.{UNIVERSE_DOMAIN}",
            True,
            "foo.com",
        ),
        (
            None,
            "googleapis.com",
            "googleapis.com",
            "foo.mtls.googleapis.com",
            "foo.{UNIVERSE_DOMAIN}",
            True,
            "foo.mtls.googleapis.com",
        ),
        (
            None,
            "googleapis.com",
            "googleapis.com",
            "foo.mtls.googleapis.com",
            "foo.{UNIVERSE_DOMAIN}",
            False,
            "foo.googleapis.com",
        ),
        (
            None,
            "bar.com",
            "googleapis.com",
            "foo.mtls.googleapis.com",
            "foo.{UNIVERSE_DOMAIN}",
            True,
            MutualTLSChannelError,
        ),
        (
            None,
            "googleapis.com",
            "googleapis.com",
            None,
            "foo.{UNIVERSE_DOMAIN}",
            True,
            ValueError,
        ),
    ],
)
def test_get_api_endpoint(
    api_override,
    universe_domain,
    default_universe,
    default_mtls_endpoint,
    default_endpoint_template,
    use_mtls,
    expected,
):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            get_api_endpoint(
                api_override,
                universe_domain,
                default_universe,
                default_mtls_endpoint,
                default_endpoint_template,
                use_mtls,
            )
    else:
        assert (
            get_api_endpoint(
                api_override,
                universe_domain,
                default_universe,
                default_mtls_endpoint,
                default_endpoint_template,
                use_mtls,
            )
            == expected
        )


def test_should_use_client_cert_fallback_env():
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}, clear=True):
        assert should_use_client_cert() is True

    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"}, clear=True):
        assert should_use_client_cert() is False

    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "invalid"}, clear=True):
        if not hasattr(google.auth.transport.mtls, "should_use_client_cert"):
            with pytest.raises(ValueError, match="Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`"):
                should_use_client_cert()


def test_transcode_basic():
    # We use FieldDescriptorProto as it has standard primitive fields and nested messages.
    http_options = [
        {
            "method": "get",
            "uri": "/v1/test/{name}",
        }
    ]

    request = descriptor_pb2.FieldDescriptorProto()
    request.name = "my-field"
    request.number = 123

    transcoded, body, query_params = transcode_request(http_options, request)

    assert transcoded["method"] == "get"
    assert transcoded["uri"] == "/v1/test/my-field"
    assert body is None
    # 'number' should be in query parameters
    assert "number" in query_params
    assert query_params["number"] == 123


def test_transcode_with_nested_field():
    http_options = [
        {
            "method": "get",
            "uri": "/v1/test/{options.deprecated}/{name}",
        }
    ]

    request = descriptor_pb2.FieldDescriptorProto()
    request.name = "my-field"
    request.options.deprecated = True
    request.number = 123

    transcoded, body, query_params = transcode_request(http_options, request)

    assert transcoded["method"] == "get"
    assert transcoded["uri"] == "/v1/test/True/my-field"
    assert body is None
    assert "number" in query_params
    assert query_params["number"] == 123


def test_transcode_with_body():
    http_options = [
        {
            "method": "post",
            "uri": "/v1/test/{name}",
            "body": "options",
        }
    ]

    request = descriptor_pb2.FieldDescriptorProto()
    request.name = "my-field"
    request.options.deprecated = True
    request.number = 123

    transcoded, body, query_params = transcode_request(http_options, request)

    assert transcoded["method"] == "post"
    assert transcoded["uri"] == "/v1/test/my-field"
    assert body is not None
    body_data = json.loads(body)
    assert body_data["deprecated"] is True
    # Query parameters should not contain 'options' (the body)
    assert "number" in query_params
    assert query_params["number"] == 123
    assert "options" not in query_params


def test_transcode_with_required_fields_default_values():
    http_options = [
        {
            "method": "get",
            "uri": "/v1/test/{name}",
        }
    ]

    request = descriptor_pb2.FieldDescriptorProto()
    request.name = "my-field"

    required_defaults = {"requiredQueryParam": "default-val"}

    transcoded, body, query_params = transcode_request(
        http_options,
        request,
        required_fields_default_values=required_defaults,
    )

    assert query_params["requiredQueryParam"] == "default-val"


def test_transcode_with_numeric_enums():
    http_options = [
        {
            "method": "get",
            "uri": "/v1/test/{name}",
        }
    ]

    request = descriptor_pb2.FieldDescriptorProto()
    request.name = "my-field"
    request.type = descriptor_pb2.FieldDescriptorProto.TYPE_STRING

    # Without numeric enums
    _, _, query_params = transcode_request(
        http_options, request, rest_numeric_enums=False
    )
    assert query_params["type"] == "TYPE_STRING"

    # With numeric enums
    _, _, query_params = transcode_request(
        http_options, request, rest_numeric_enums=True
    )
    # Type number for TYPE_STRING is 9
    assert query_params["type"] == 9
    assert query_params["$alt"] == "json;enum-encoding=int"


def test_transcode_no_query_params():
    http_options = [{"method": "get", "uri": "/v1/test"}]
    request = descriptor_pb2.FieldDescriptorProto()

    with mock.patch(
        "google.api_core.path_template.transcode",
        return_value={"method": "get", "uri": "/v1/test"},
    ):
        transcoded, body, query_params = transcode_request(http_options, request)
        assert query_params == {}


def test_transcode_with_required_fields_existing_key():
    http_options = [
        {
            "method": "get",
            "uri": "/v1/test",
        }
    ]

    request = descriptor_pb2.FieldDescriptorProto()
    request.name = "custom-name"

    required_defaults = {"name": "default-name"}

    transcoded, body, query_params = transcode_request(
        http_options,
        request,
        required_fields_default_values=required_defaults,
    )

    assert query_params["name"] == "custom-name"


def test_transcode_request_invalid_request():
    http_options = [{"method": "get", "uri": "/v1/test"}]
    with pytest.raises(TypeError, match="request cannot be None"):
        transcode_request(http_options, None)


def test_transcode_request_proto_plus_wrapper():
    http_options = [{"method": "get", "uri": "/v1/test/{name}"}]
    mock_pb = descriptor_pb2.FieldDescriptorProto()
    mock_pb.name = "proto-plus-field"

    mock_proto_plus = mock.Mock()
    mock_proto_plus._pb = mock_pb

    transcoded, _, _ = transcode_request(http_options, mock_proto_plus)
    assert transcoded["uri"] == "/v1/test/proto-plus-field"


def test_read_environment_variables():
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true", "GOOGLE_API_USE_MTLS_ENDPOINT": "always", "GOOGLE_CLOUD_UNIVERSE_DOMAIN": "foo.com"}):
        use_cert, mtls_endpoint, universe_domain = read_environment_variables()
        assert use_cert is True
        assert mtls_endpoint == "always"
        assert universe_domain == "foo.com"

    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "invalid"}):
        with pytest.raises(MutualTLSChannelError):
            read_environment_variables()


def test_observability_compat():
    # _observability is exposed from _compat
    try:
        from google.api_core import _observability as core_observability
        assert _observability is core_observability
    except ImportError:  # pragma: NO COVER
        assert _observability is None  # pragma: NO COVER


def test_trace_http_request_compat():
    # trace_http_request is exposed from _compat and callable as context manager
    with trace_http_request(method="GET", url="https://example.com") as trace_ctx:
        trace_ctx.record_response(None)


def test_observability_compat_present(monkeypatch):
    import importlib
    import sys
    import google.api_core
    from google.cloud.eventarc_v1 import _compat

    # Simulate an environment where google.api_core._observability is available
    mock_obs = mock.MagicMock()
    mock_obs.trace_http_request = mock.MagicMock()
    monkeypatch.setitem(sys.modules, "google.api_core._observability", mock_obs)
    monkeypatch.setattr(google.api_core, "_observability", mock_obs, raising=False)
    reloaded = importlib.reload(_compat)
    try:
        assert reloaded._observability is mock_obs
        assert reloaded.trace_http_request is mock_obs.trace_http_request
    finally:
        monkeypatch.undo()
        importlib.reload(_compat)


def test_observability_compat_fallback(monkeypatch):
    import importlib
    import sys
    import google.api_core
    from google.cloud.eventarc_v1 import _compat

    # Simulate an environment where google.api_core._observability is not available
    monkeypatch.setitem(sys.modules, "google.api_core._observability", None)
    monkeypatch.setattr(google.api_core, "_observability", None, raising=False)
    reloaded = importlib.reload(_compat)
    try:
        assert reloaded._observability is None
        with reloaded.trace_http_request(method="GET", url="https://example.com") as trace_ctx:
            trace_ctx.record_response(None)
    finally:
        # Restore _compat to normal environment
        monkeypatch.undo()
        importlib.reload(_compat)


def test_apply_channel_interceptors_compat():
    # apply_channel_interceptors is exposed from _compat and callable
    dummy_channel = mock.Mock()
    result = apply_channel_interceptors(dummy_channel, None)
    assert result is dummy_channel


def test_apply_async_channel_interceptors_compat():
    # apply_async_channel_interceptors is exposed from _compat and callable
    dummy_channel = mock.Mock()
    result = apply_async_channel_interceptors(dummy_channel, None)
    assert result is dummy_channel
