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
import os
import asyncio
import re
from unittest import mock
from unittest.mock import AsyncMock

import grpc
from grpc.experimental import aio
from collections.abc import Iterable, AsyncIterable
from google.protobuf import json_format
import json
import math
import pytest
from collections.abc import Sequence, Mapping
from google.api_core import api_core_version
from proto.marshal.rules.dates import DurationRule, TimestampRule
from proto.marshal.rules import wrappers
from requests import Response
from requests import Request, PreparedRequest
from requests.sessions import Session
from google.protobuf import json_format

try:
    from google.auth.aio import credentials as ga_credentials_async
    HAS_GOOGLE_AUTH_AIO = True
except ImportError: # pragma: NO COVER
    HAS_GOOGLE_AUTH_AIO = False

from google.api_core import client_options
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import grpc_helpers
from google.api_core import grpc_helpers_async
from google.api_core import path_template
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.cloud.location import locations_pb2
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import options_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.longrunning import operations_pb2 # type: ignore
from google.oauth2 import service_account
from google.showcase_v1beta1.services.testing import TestingAsyncClient
from google.showcase_v1beta1.services.testing import TestingClient
from google.showcase_v1beta1.services.testing import pagers
from google.showcase_v1beta1.services.testing import transports
from google.showcase_v1beta1.services.testing.client import _observability
from google.showcase_v1beta1.types import testing
import google.auth



CRED_INFO_JSON = {
    "credential_source": "/path/to/file",
    "credential_type": "service account credentials",
    "principal": "service-account@example.com",
}
CRED_INFO_STRING = json.dumps(CRED_INFO_JSON)
_UUID4_RE = re.compile(r"[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}")


@pytest.fixture(autouse=True)
def disable_mtls_env():
    with mock.patch.dict(
        os.environ,
        {
            "GOOGLE_API_USE_CLIENT_CERTIFICATE": "false",
            "CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE": "false",
        },
    ):
        yield


async def mock_async_gen(data, chunk_size=1):
    for i in range(0, len(data)):  # pragma: NO COVER
        chunk = data[i : i + chunk_size]
        yield chunk.encode("utf-8")

def client_cert_source_callback():
    return b"cert bytes", b"key bytes"

# TODO: use async auth anon credentials by default once the minimum version of google-auth is upgraded.
# See related issue: https://github.com/googleapis/gapic-generator-python/issues/2107.
def async_anonymous_credentials():
    if HAS_GOOGLE_AUTH_AIO:
        return ga_credentials_async.AnonymousCredentials()
    return ga_credentials.AnonymousCredentials()

# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return "foo.googleapis.com" if ("localhost" in client.DEFAULT_ENDPOINT) else client.DEFAULT_ENDPOINT

# If default endpoint template is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint template so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint_template(client):
    return "test.{UNIVERSE_DOMAIN}" if ("localhost" in client._DEFAULT_ENDPOINT_TEMPLATE) else client._DEFAULT_ENDPOINT_TEMPLATE


@pytest.fixture(autouse=True)
def set_event_loop():
    try:
        asyncio.get_running_loop()
        yield
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            yield
        finally:
            loop.close()
            asyncio.set_event_loop(None)


def test__get_client_cert_source():
    mock_provided_cert_source = mock.Mock()
    mock_default_cert_source = mock.Mock()

    assert TestingClient._get_client_cert_source(None, False) is None
    assert TestingClient._get_client_cert_source(mock_provided_cert_source, False) is None
    assert TestingClient._get_client_cert_source(mock_provided_cert_source, True) == mock_provided_cert_source

    with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=True):
        with mock.patch('google.auth.transport.mtls.default_client_cert_source', return_value=mock_default_cert_source):
            assert TestingClient._get_client_cert_source(None, True) is mock_default_cert_source
            assert TestingClient._get_client_cert_source(mock_provided_cert_source, "true") is mock_provided_cert_source


@pytest.mark.parametrize("error_code,cred_info_json,show_cred_info", [
    (401, CRED_INFO_JSON, True),
    (403, CRED_INFO_JSON, True),
    (404, CRED_INFO_JSON, True),
    (500, CRED_INFO_JSON, False),
    (401, None, False),
    (403, None, False),
    (404, None, False),
    (500, None, False)
])
def test__add_cred_info_for_auth_errors(error_code, cred_info_json, show_cred_info):
    cred = mock.Mock(["get_cred_info"])
    cred.get_cred_info = mock.Mock(return_value=cred_info_json)
    client = TestingClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=["foo"])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    if show_cred_info:
        assert error.details == ["foo", CRED_INFO_STRING]
    else:
        assert error.details == ["foo"]

@pytest.mark.parametrize("error_code", [401,403,404,500])
def test__add_cred_info_for_auth_errors_no_get_cred_info(error_code):
    cred = mock.Mock([])
    assert not hasattr(cred, "get_cred_info")
    client = TestingClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []

@pytest.mark.parametrize("client_class,transport_name", [
    (TestingClient, "grpc"),
    (TestingAsyncClient, "grpc_asyncio"),
    (TestingClient, "rest"),
])
def test_testing_client_from_service_account_info(client_class, transport_name):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_info') as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info, transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            'localhost:7469'
            if transport_name in ['grpc', 'grpc_asyncio']
            else
            'https://localhost:7469'
        )


@pytest.mark.parametrize("transport_class,transport_name", [
    (transports.TestingGrpcTransport, "grpc"),
    (transports.TestingGrpcAsyncIOTransport, "grpc_asyncio"),
    (transports.TestingRestTransport, "rest"),
])
def test_testing_client_service_account_always_use_jwt(transport_class, transport_name):
    with mock.patch.object(service_account.Credentials, 'with_always_use_jwt_access', create=True) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(service_account.Credentials, 'with_always_use_jwt_access', create=True) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize("client_class,transport_name", [
    (TestingClient, "grpc"),
    (TestingAsyncClient, "grpc_asyncio"),
    (TestingClient, "rest"),
])
def test_testing_client_from_service_account_file(client_class, transport_name):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(service_account.Credentials, 'from_service_account_file') as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file("dummy/file/path.json", transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json("dummy/file/path.json", transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            'localhost:7469'
            if transport_name in ['grpc', 'grpc_asyncio']
            else
            'https://localhost:7469'
        )


def test_testing_client_get_transport_class():
    transport = TestingClient.get_transport_class()
    available_transports = [
        transports.TestingGrpcTransport,
        transports.TestingRestTransport,
    ]
    assert transport in available_transports

    transport = TestingClient.get_transport_class("grpc")
    assert transport == transports.TestingGrpcTransport


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (TestingClient, transports.TestingGrpcTransport, "grpc"),
    (TestingAsyncClient, transports.TestingGrpcAsyncIOTransport, "grpc_asyncio"),
    (TestingClient, transports.TestingRestTransport, "rest"),
])
@mock.patch.object(TestingClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(TestingClient))
@mock.patch.object(TestingAsyncClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(TestingAsyncClient))
def test_testing_client_client_options(client_class, transport_class, transport_name):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(TestingClient, 'get_transport_class') as gtc:
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials()
        )
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(TestingClient, 'get_transport_class') as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError) as excinfo:
            client = client_class(transport=transport_name)
    assert str(excinfo.value) == "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )
    # Check the case api_endpoint is provided
    options = client_options.ClientOptions(api_audience="https://language.googleapis.com")
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience="https://language.googleapis.com"
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name,use_client_cert_env", [
    (TestingClient, transports.TestingGrpcTransport, "grpc", "true"),
    (TestingAsyncClient, transports.TestingGrpcAsyncIOTransport, "grpc_asyncio", "true"),
    (TestingClient, transports.TestingGrpcTransport, "grpc", "false"),
    (TestingAsyncClient, transports.TestingGrpcAsyncIOTransport, "grpc_asyncio", "false"),
    (TestingClient, transports.TestingRestTransport, "rest", "true"),
    (TestingClient, transports.TestingRestTransport, "rest", "false"),
])
@mock.patch.object(TestingClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(TestingClient))
@mock.patch.object(TestingAsyncClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(TestingAsyncClient))
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_testing_client_mtls_env_auto(client_class, transport_class, transport_name, use_client_cert_env):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        options = client_options.ClientOptions(client_cert_source=client_cert_source_callback)
        with mock.patch.object(transport_class, '__init__') as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE)
            else:
                expected_client_cert_source = client_cert_source_callback
                expected_host = client.DEFAULT_MTLS_ENDPOINT

            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=expected_host,
                scopes=None,
                client_cert_source_for_mtls=expected_client_cert_source,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        with mock.patch.object(transport_class, '__init__') as patched:
            with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=True):
                with mock.patch('google.auth.transport.mtls.default_client_cert_source', return_value=client_cert_source_callback):
                    if use_client_cert_env == "false":
                        expected_host = client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE)
                        expected_client_cert_source = None
                    else:
                        expected_host = client.DEFAULT_MTLS_ENDPOINT
                        expected_client_cert_source = client_cert_source_callback

                    patched.return_value = None
                    client = client_class(transport=transport_name)
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                        always_use_jwt_access=True,
                        api_audience=None,
                    )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}):
        with mock.patch.object(transport_class, '__init__') as patched:
            with mock.patch("google.auth.transport.mtls.has_default_client_cert_source", return_value=False):
                patched.return_value = None
                client = client_class(transport=transport_name)
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                    api_audience=None,
                )


@pytest.mark.parametrize("client_class", [
    TestingClient, TestingAsyncClient
])
@mock.patch.object(TestingClient, "DEFAULT_ENDPOINT", modify_default_endpoint(TestingClient))
@mock.patch.object(TestingAsyncClient, "DEFAULT_ENDPOINT", modify_default_endpoint(TestingAsyncClient))
def test_testing_client_get_mtls_endpoint_and_cert_source(client_class):
    mock_client_cert_source = mock.Mock()

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "true".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint)
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(options)
        assert api_endpoint == mock_api_endpoint
        assert cert_source == mock_client_cert_source

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "false".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"}):
        mock_client_cert_source = mock.Mock()
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint)
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(options)
        assert api_endpoint == mock_api_endpoint
        assert cert_source is None

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "Unsupported".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}):
        if hasattr(google.auth.transport.mtls, "should_use_client_cert"):
            mock_client_cert_source = mock.Mock()
            mock_api_endpoint = "foo"
            options = client_options.ClientOptions(
                client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint
            )
            api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
                options
            )
            assert api_endpoint == mock_api_endpoint
            assert cert_source is None

    # Test cases for mTLS enablement when GOOGLE_API_USE_CLIENT_CERTIFICATE is unset.
    test_cases = [
        (
            # With workloads present in config, mTLS is enabled.
            {
                "version": 1,
                "cert_configs": {
                    "workload": {
                        "cert_path": "path/to/cert/file",
                        "key_path": "path/to/key/file",
                    }
                },
            },
            mock_client_cert_source,
        ),
        (
            # With workloads not present in config, mTLS is disabled.
            {
                "version": 1,
                "cert_configs": {},
            },
            None,
        ),
    ]
    if hasattr(google.auth.transport.mtls, "should_use_client_cert"):
        for config_data, expected_cert_source in test_cases:
            env = os.environ.copy()
            env.pop("GOOGLE_API_USE_CLIENT_CERTIFICATE", None)
            env.pop("CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE", None)
            with mock.patch.dict(os.environ, env, clear=True):
                    config_filename = "mock_certificate_config.json"
                    config_file_content = json.dumps(config_data)
                    m = mock.mock_open(read_data=config_file_content)
                    with mock.patch("builtins.open", m), mock.patch("os.path.exists", side_effect=lambda path: os.path.basename(path) == config_filename):
                        with mock.patch.dict(
                            os.environ, {"GOOGLE_API_CERTIFICATE_CONFIG": config_filename}
                        ):
                            mock_api_endpoint = "foo"
                            options = client_options.ClientOptions(
                                client_cert_source=mock_client_cert_source,
                                api_endpoint=mock_api_endpoint,
                            )
                            api_endpoint, cert_source = (
                                client_class.get_mtls_endpoint_and_cert_source(options)
                            )
                            assert api_endpoint == mock_api_endpoint
                            assert cert_source is expected_cert_source

    # Test cases for mTLS enablement when GOOGLE_API_USE_CLIENT_CERTIFICATE is unset(empty).
    test_cases = [
        (
            # With workloads present in config, mTLS is enabled.
            {
                "version": 1,
                "cert_configs": {
                    "workload": {
                        "cert_path": "path/to/cert/file",
                        "key_path": "path/to/key/file",
                    }
                },
            },
            mock_client_cert_source,
        ),
        (
            # With workloads not present in config, mTLS is disabled.
            {
                "version": 1,
                "cert_configs": {},
            },
            None,
        ),
    ]
    if hasattr(google.auth.transport.mtls, "should_use_client_cert"):
        for config_data, expected_cert_source in test_cases:
            env = os.environ.copy()
            env.pop("GOOGLE_API_USE_CLIENT_CERTIFICATE", "")
            env.pop("CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE", "")
            with mock.patch.dict(os.environ, env, clear=True):
                    config_filename = "mock_certificate_config.json"
                    config_file_content = json.dumps(config_data)
                    m = mock.mock_open(read_data=config_file_content)
                    with mock.patch("builtins.open", m), mock.patch("os.path.exists", side_effect=lambda path: os.path.basename(path) == config_filename):
                        with mock.patch.dict(
                            os.environ, {"GOOGLE_API_CERTIFICATE_CONFIG": config_filename}
                        ):
                            mock_api_endpoint = "foo"
                            options = client_options.ClientOptions(
                                client_cert_source=mock_client_cert_source,
                                api_endpoint=mock_api_endpoint,
                            )
                            api_endpoint, cert_source = (
                                client_class.get_mtls_endpoint_and_cert_source(options)
                            )
                            assert api_endpoint == mock_api_endpoint
                            assert cert_source is expected_cert_source

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert doesn't exist.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=False):
            api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
            assert api_endpoint == client_class.DEFAULT_ENDPOINT
            assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert exists.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch('google.auth.transport.mtls.has_default_client_cert_source', return_value=True):
            with mock.patch('google.auth.transport.mtls.default_client_cert_source', return_value=mock_client_cert_source):
                api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
                assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
                assert cert_source == mock_client_cert_source

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError) as excinfo:
            client_class.get_mtls_endpoint_and_cert_source()

        assert str(excinfo.value) == "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"

@pytest.mark.parametrize("client_class", [
    TestingClient, TestingAsyncClient
])
@mock.patch.object(TestingClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(TestingClient))
@mock.patch.object(TestingAsyncClient, "_DEFAULT_ENDPOINT_TEMPLATE", modify_default_endpoint_template(TestingAsyncClient))
def test_testing_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = TestingClient._DEFAULT_UNIVERSE
    default_endpoint = TestingClient._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=default_universe)
    mock_universe = "bar.com"
    mock_endpoint = TestingClient._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=mock_universe)

    # If ClientOptions.api_endpoint is set and GOOGLE_API_USE_CLIENT_CERTIFICATE="true",
    # use ClientOptions.api_endpoint as the api endpoint regardless.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch("google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"):
            options = client_options.ClientOptions(client_cert_source=mock_client_cert_source, api_endpoint=api_override)
            client = client_class(client_options=options, credentials=ga_credentials.AnonymousCredentials())
            assert client.api_endpoint == api_override

    # If ClientOptions.api_endpoint is not set and GOOGLE_API_USE_MTLS_ENDPOINT="never",
    # use the _DEFAULT_ENDPOINT_TEMPLATE populated with GDU as the api endpoint.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        client = client_class(credentials=ga_credentials.AnonymousCredentials())
        assert client.api_endpoint == default_endpoint

    # If ClientOptions.api_endpoint is not set and GOOGLE_API_USE_MTLS_ENDPOINT="always",
    # use the DEFAULT_MTLS_ENDPOINT as the api endpoint.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        client = client_class(credentials=ga_credentials.AnonymousCredentials())
        assert client.api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT

    # If ClientOptions.api_endpoint is not set, GOOGLE_API_USE_MTLS_ENDPOINT="auto" (default),
    # GOOGLE_API_USE_CLIENT_CERTIFICATE="false" (default), default cert source doesn't exist,
    # and ClientOptions.universe_domain="bar.com",
    # use the _DEFAULT_ENDPOINT_TEMPLATE populated with universe domain as the api endpoint.
    options = client_options.ClientOptions()
    universe_exists = hasattr(options, "universe_domain")
    if universe_exists:
        options = client_options.ClientOptions(universe_domain=mock_universe)
        client = client_class(client_options=options, credentials=ga_credentials.AnonymousCredentials())
    else:
        client = client_class(client_options=options, credentials=ga_credentials.AnonymousCredentials())
    assert client.api_endpoint == (mock_endpoint if universe_exists else default_endpoint)
    assert client.universe_domain == (mock_universe if universe_exists else default_universe)

    # If ClientOptions does not have a universe domain attribute and GOOGLE_API_USE_MTLS_ENDPOINT="never",
    # use the _DEFAULT_ENDPOINT_TEMPLATE populated with GDU as the api endpoint.
    options = client_options.ClientOptions()
    if hasattr(options, "universe_domain"):
        delattr(options, "universe_domain")
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        client = client_class(client_options=options, credentials=ga_credentials.AnonymousCredentials())
        assert client.api_endpoint == default_endpoint


@pytest.mark.parametrize("client_class,transport_class,transport_name", [
    (TestingClient, transports.TestingGrpcTransport, "grpc"),
    (TestingAsyncClient, transports.TestingGrpcAsyncIOTransport, "grpc_asyncio"),
    (TestingClient, transports.TestingRestTransport, "rest"),
])
def test_testing_client_client_options_scopes(client_class, transport_class, transport_name):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(
        scopes=["1", "2"],
    )
    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

@pytest.mark.parametrize("client_class,transport_class,transport_name,grpc_helpers", [
    (TestingClient, transports.TestingGrpcTransport, "grpc", grpc_helpers),
    (TestingAsyncClient, transports.TestingGrpcAsyncIOTransport, "grpc_asyncio", grpc_helpers_async),
    (TestingClient, transports.TestingRestTransport, "rest", None),
])
def test_testing_client_client_options_credentials_file(client_class, transport_class, transport_name, grpc_helpers):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(
        credentials_file="credentials.json"
    )

    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

def test_testing_client_client_options_from_dict():
    with mock.patch('google.showcase_v1beta1.services.testing.transports.TestingGrpcTransport.__init__') as grpc_transport:
        grpc_transport.return_value = None
        client = TestingClient(
            client_options={'api_endpoint': 'squid.clam.whelk'}
        )
        grpc_transport.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )


@pytest.mark.skipif(
    _observability is None,
    reason="Requires google-api-core with OpenTelemetry support (>= 2.36.0)",
)
@pytest.mark.parametrize("capabilities_enabled, expected_options_injected", [
    pytest.param(True, True, id="otel_injection_enabled"),
    pytest.param(False, False, id="otel_injection_disabled"),
])
def test_testing_client_otel_channel_injection(capabilities_enabled, expected_options_injected):
    with (
        mock.patch.object(
            _observability,
            "is_otel_capabilities_enabled",
            return_value=capabilities_enabled,
            autospec=True,
        ) as mock_is_otel_enabled,
        mock.patch.object(
            transports.TestingGrpcTransport, "__init__", return_value=None
        ) as patched_transport_init,
    ):
        client = TestingClient(transport="grpc")

        mock_is_otel_enabled.assert_called_once_with(client._client_options)
        called_kwargs = patched_transport_init.call_args.kwargs
        if expected_options_injected:
            assert called_kwargs.get("client_options") == client._client_options
        else:
            assert not called_kwargs.get("client_options")


def test_testing_grpc_transport_channel_interceptors():
    mock_interceptor = mock.Mock()
    mock_channel = mock.Mock()

    with (
        mock.patch.object(
            transports.TestingGrpcTransport,
            "create_channel",
            return_value=mock_channel,
        ),
        mock.patch.object(
            grpc_helpers,
            "apply_channel_interceptors",
            return_value=mock_channel,
            create=True,
        ) as mock_apply_interceptors,
    ):
        transport = transports.TestingGrpcTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            interceptors=[mock_interceptor],
        )

        mock_apply_interceptors.assert_called_once_with(
            mock_channel, [mock_interceptor]
        )
        assert transport.grpc_channel == mock_channel


@pytest.mark.skipif(
    _observability is None,
    reason="Requires google-api-core with OpenTelemetry support (>= 2.36.0)",
)
def test_testing_grpc_transport_otel_channel_interceptor():
    mock_otel_interceptor = mock.Mock()
    mock_channel = mock.Mock()

    with (
        mock.patch.object(
            _observability,
            "get_otel_interceptor",
            return_value=mock_otel_interceptor,
        ) as mock_get_interceptor,
        mock.patch.object(
            transports.TestingGrpcTransport,
            "create_channel",
            return_value=mock_channel,
        ),
        mock.patch.object(
            grpc_helpers,
            "apply_channel_interceptors",
            return_value=mock_channel,
            create=True,
        ) as mock_apply_interceptors,
    ):
        options = client_options.ClientOptions()
        transport = transports.TestingGrpcTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            client_options=options,
        )

        mock_get_interceptor.assert_called_once_with(options)
        mock_apply_interceptors.assert_called_once_with(
            mock_channel, [mock_otel_interceptor]
        )
        assert transport.grpc_channel == mock_channel


def test_testing_grpc_transport_custom_channel_interceptors():
    mock_interceptor = mock.Mock()
    mock_custom_channel = mock.Mock(spec=grpc.Channel)

    with mock.patch.object(
        grpc_helpers,
        "apply_channel_interceptors",
        return_value=mock_custom_channel,
        create=True,
    ) as mock_apply_interceptors:
        transport = transports.TestingGrpcTransport(
            channel=mock_custom_channel,
            interceptors=[mock_interceptor],
        )

        mock_apply_interceptors.assert_called_once_with(
            mock_custom_channel, [mock_interceptor]
        )
        assert transport.grpc_channel == mock_custom_channel


def test_testing_grpc_asyncio_transport_channel_interceptors():
    mock_interceptor = mock.Mock()
    mock_channel = mock.Mock()
    mock_channel._unary_unary_interceptors = []

    with mock.patch.object(
        transports.TestingGrpcAsyncIOTransport,
        "create_channel",
        return_value=mock_channel,
    ) as mock_create_channel:
        transport = transports.TestingGrpcAsyncIOTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            interceptors=[mock_interceptor],
        )

        assert mock_create_channel.call_count == 1
        assert mock_interceptor in transport.grpc_channel._unary_unary_interceptors
        assert transport.grpc_channel == mock_channel


@pytest.mark.skipif(
    _observability is None or not hasattr(_observability, "apply_otel_async_channel_interceptors"),
    reason="Requires google-api-core with OpenTelemetry async channel interceptors support (>= v2.43.0)",
)
def test_testing_grpc_asyncio_transport_otel_channel_interceptor():
    mock_channel = mock.Mock()
    mock_channel._unary_unary_interceptors = []

    with (
        mock.patch.object(
            _observability,
            "apply_otel_async_channel_interceptors",
            return_value=mock_channel,
        ) as mock_apply_async_interceptors,
        mock.patch.object(
            transports.TestingGrpcAsyncIOTransport,
            "create_channel",
            return_value=mock_channel,
        ) as mock_create_channel,
    ):
        options = client_options.ClientOptions()
        transport = transports.TestingGrpcAsyncIOTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            client_options=options,
        )

        mock_apply_async_interceptors.assert_called_once_with(mock_channel, options)
        assert mock_create_channel.call_count == 1
        assert transport.grpc_channel == mock_channel


def test_testing_grpc_asyncio_transport_custom_channel():
    mock_custom_channel = mock.Mock(spec=aio.Channel)

    with mock.patch.object(
        transports.TestingGrpcAsyncIOTransport,
        "create_channel",
    ) as mock_create_channel:
        transport = transports.TestingGrpcAsyncIOTransport(
            channel=mock_custom_channel,
        )

        assert mock_create_channel.call_count == 0
        assert transport.grpc_channel == mock_custom_channel


@pytest.mark.parametrize("client_class,transport_class,transport_name,grpc_helpers", [
    (TestingClient, transports.TestingGrpcTransport, "grpc", grpc_helpers),
    (TestingAsyncClient, transports.TestingGrpcAsyncIOTransport, "grpc_asyncio", grpc_helpers_async),
])
def test_testing_client_create_channel_credentials_file(client_class, transport_class, transport_name, grpc_helpers):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(
        credentials_file="credentials.json"
    )

    with mock.patch.object(transport_class, '__init__') as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

    # test that the credentials from file are saved and used as the credentials.
    with mock.patch.object(
        google.auth, "load_credentials_from_file", autospec=True
    ) as load_creds, mock.patch.object(
        google.auth, "default", autospec=True
    ) as adc, mock.patch.object(
        grpc_helpers, "create_channel"
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        file_creds = ga_credentials.AnonymousCredentials()
        load_creds.return_value = (file_creds, None)
        adc.return_value = (creds, None)
        client = client_class(client_options=options, transport=transport_name)
        create_channel.assert_called_with(
            "localhost:7469",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
),
            scopes=None,
            default_host="localhost:7469",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize("request_type", [
  testing.CreateSessionRequest(),
  {},
])
def test_create_session(request_type, transport: str = 'grpc'):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.create_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = testing.Session(
            name='name_value',
            version=testing.Session.Version.V1_LATEST,
        )
        response = client.create_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = testing.CreateSessionRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.Session)
    assert response.name == 'name_value'
    assert response.version == testing.Session.Version.V1_LATEST


def test_create_session_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = testing.CreateSessionRequest(
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.create_session),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.create_session(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.CreateSessionRequest(
        )
        assert args[0] == request_msg

def test_create_session_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_session in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.create_session] = mock_rpc
        request = {}
        client.create_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_session(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_create_session_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = TestingAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.create_session in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.create_session] = mock_rpc

        request = {}
        await client.create_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.create_session(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  testing.CreateSessionRequest(),
  {},
])
async def test_create_session_async(request_type, transport: str = 'grpc_asyncio'):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.create_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(testing.Session(
            name='name_value',
            version=testing.Session.Version.V1_LATEST,
        ))
        response = await client.create_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = testing.CreateSessionRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.Session)
    assert response.name == 'name_value'
    assert response.version == testing.Session.Version.V1_LATEST


@pytest.mark.parametrize("request_type", [
  testing.GetSessionRequest(),
  {},
])
def test_get_session(request_type, transport: str = 'grpc'):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = testing.Session(
            name='name_value',
            version=testing.Session.Version.V1_LATEST,
        )
        response = client.get_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = testing.GetSessionRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.Session)
    assert response.name == 'name_value'
    assert response.version == testing.Session.Version.V1_LATEST


def test_get_session_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = testing.GetSessionRequest(
        name='name_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_session),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.get_session(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.GetSessionRequest(
            name='name_value',
        )
        assert args[0] == request_msg

def test_get_session_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_session in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.get_session] = mock_rpc
        request = {}
        client.get_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_session(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_get_session_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = TestingAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.get_session in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.get_session] = mock_rpc

        request = {}
        await client.get_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_session(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  testing.GetSessionRequest(),
  {},
])
async def test_get_session_async(request_type, transport: str = 'grpc_asyncio'):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(testing.Session(
            name='name_value',
            version=testing.Session.Version.V1_LATEST,
        ))
        response = await client.get_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = testing.GetSessionRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.Session)
    assert response.name == 'name_value'
    assert response.version == testing.Session.Version.V1_LATEST

def test_get_session_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = testing.GetSessionRequest()

    request.name = 'name_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_session),
            '__call__') as call:
        call.return_value = testing.Session()
        client.get_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'name=name_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_get_session_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = testing.GetSessionRequest()

    request.name = 'name_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.get_session),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(testing.Session())
        await client.get_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'name=name_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  testing.ListSessionsRequest(),
  {},
])
def test_list_sessions(request_type, transport: str = 'grpc'):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_sessions),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = testing.ListSessionsResponse(
            next_page_token='next_page_token_value',
        )
        response = client.list_sessions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = testing.ListSessionsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListSessionsPager)
    assert response.next_page_token == 'next_page_token_value'


def test_list_sessions_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = testing.ListSessionsRequest(
        page_token='page_token_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_sessions),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.list_sessions(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.ListSessionsRequest(
            page_token='page_token_value',
        )
        assert args[0] == request_msg

def test_list_sessions_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_sessions in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.list_sessions] = mock_rpc
        request = {}
        client.list_sessions(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_sessions(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_list_sessions_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = TestingAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.list_sessions in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.list_sessions] = mock_rpc

        request = {}
        await client.list_sessions(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_sessions(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  testing.ListSessionsRequest(),
  {},
])
async def test_list_sessions_async(request_type, transport: str = 'grpc_asyncio'):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_sessions),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(testing.ListSessionsResponse(
            next_page_token='next_page_token_value',
        ))
        response = await client.list_sessions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = testing.ListSessionsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListSessionsAsyncPager)
    assert response.next_page_token == 'next_page_token_value'


def test_list_sessions_pager(transport_name: str = "grpc"):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_sessions),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                    testing.Session(),
                    testing.Session(),
                ],
                next_page_token='abc',
            ),
            testing.ListSessionsResponse(
                sessions=[],
                next_page_token='def',
            ),
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                ],
                next_page_token='ghi',
            ),
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                    testing.Session(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        pager = client.list_sessions(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == 'abc'
        assert str(pager).startswith(f'{pager.__class__.__name__}<')

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, testing.Session)
                   for i in results)
def test_list_sessions_pages(transport_name: str = "grpc"):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_sessions),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                    testing.Session(),
                    testing.Session(),
                ],
                next_page_token='abc',
            ),
            testing.ListSessionsResponse(
                sessions=[],
                next_page_token='def',
            ),
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                ],
                next_page_token='ghi',
            ),
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                    testing.Session(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_sessions(request={}).pages)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token

@pytest.mark.asyncio
async def test_list_sessions_async_pager():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_sessions),
            '__call__', new_callable=mock.AsyncMock) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                    testing.Session(),
                    testing.Session(),
                ],
                next_page_token='abc',
            ),
            testing.ListSessionsResponse(
                sessions=[],
                next_page_token='def',
            ),
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                ],
                next_page_token='ghi',
            ),
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                    testing.Session(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_sessions(request={},)
        assert async_pager.next_page_token == 'abc'
        assert str(async_pager).startswith(f'{async_pager.__class__.__name__}<')

        responses = []
        async for response in async_pager: # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, testing.Session)
                for i in responses)


@pytest.mark.asyncio
async def test_list_sessions_async_pages():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_sessions),
            '__call__', new_callable=mock.AsyncMock) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                    testing.Session(),
                    testing.Session(),
                ],
                next_page_token='abc',
            ),
            testing.ListSessionsResponse(
                sessions=[],
                next_page_token='def',
            ),
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                ],
                next_page_token='ghi',
            ),
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                    testing.Session(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.list_sessions(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token

@pytest.mark.parametrize("request_type", [
  testing.DeleteSessionRequest(),
  {},
])
def test_delete_session(request_type, transport: str = 'grpc'):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = testing.DeleteSessionRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_session_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = testing.DeleteSessionRequest(
        name='name_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_session),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.delete_session(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.DeleteSessionRequest(
            name='name_value',
        )
        assert args[0] == request_msg

def test_delete_session_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_session in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.delete_session] = mock_rpc
        request = {}
        client.delete_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_session(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_delete_session_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = TestingAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.delete_session in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.delete_session] = mock_rpc

        request = {}
        await client.delete_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.delete_session(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  testing.DeleteSessionRequest(),
  {},
])
async def test_delete_session_async(request_type, transport: str = 'grpc_asyncio'):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = testing.DeleteSessionRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None

def test_delete_session_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = testing.DeleteSessionRequest()

    request.name = 'name_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_session),
            '__call__') as call:
        call.return_value = None
        client.delete_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'name=name_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_delete_session_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = testing.DeleteSessionRequest()

    request.name = 'name_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_session),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'name=name_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  testing.ReportSessionRequest(),
  {},
])
def test_report_session(request_type, transport: str = 'grpc'):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.report_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = testing.ReportSessionResponse(
            result=testing.ReportSessionResponse.Result.PASSED,
        )
        response = client.report_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = testing.ReportSessionRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.ReportSessionResponse)
    assert response.result == testing.ReportSessionResponse.Result.PASSED


def test_report_session_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = testing.ReportSessionRequest(
        name='name_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.report_session),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.report_session(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.ReportSessionRequest(
            name='name_value',
        )
        assert args[0] == request_msg

def test_report_session_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.report_session in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.report_session] = mock_rpc
        request = {}
        client.report_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.report_session(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_report_session_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = TestingAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.report_session in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.report_session] = mock_rpc

        request = {}
        await client.report_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.report_session(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  testing.ReportSessionRequest(),
  {},
])
async def test_report_session_async(request_type, transport: str = 'grpc_asyncio'):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.report_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(testing.ReportSessionResponse(
            result=testing.ReportSessionResponse.Result.PASSED,
        ))
        response = await client.report_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = testing.ReportSessionRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.ReportSessionResponse)
    assert response.result == testing.ReportSessionResponse.Result.PASSED

def test_report_session_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = testing.ReportSessionRequest()

    request.name = 'name_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.report_session),
            '__call__') as call:
        call.return_value = testing.ReportSessionResponse()
        client.report_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'name=name_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_report_session_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = testing.ReportSessionRequest()

    request.name = 'name_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.report_session),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(testing.ReportSessionResponse())
        await client.report_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'name=name_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  testing.ListTestsRequest(),
  {},
])
def test_list_tests(request_type, transport: str = 'grpc'):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_tests),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = testing.ListTestsResponse(
            next_page_token='next_page_token_value',
        )
        response = client.list_tests(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = testing.ListTestsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListTestsPager)
    assert response.next_page_token == 'next_page_token_value'


def test_list_tests_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = testing.ListTestsRequest(
        parent='parent_value',
        page_token='page_token_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_tests),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.list_tests(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.ListTestsRequest(
            parent='parent_value',
            page_token='page_token_value',
        )
        assert args[0] == request_msg

def test_list_tests_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_tests in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.list_tests] = mock_rpc
        request = {}
        client.list_tests(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_tests(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_list_tests_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = TestingAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.list_tests in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.list_tests] = mock_rpc

        request = {}
        await client.list_tests(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_tests(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  testing.ListTestsRequest(),
  {},
])
async def test_list_tests_async(request_type, transport: str = 'grpc_asyncio'):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_tests),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(testing.ListTestsResponse(
            next_page_token='next_page_token_value',
        ))
        response = await client.list_tests(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = testing.ListTestsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListTestsAsyncPager)
    assert response.next_page_token == 'next_page_token_value'

def test_list_tests_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = testing.ListTestsRequest()

    request.parent = 'parent_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_tests),
            '__call__') as call:
        call.return_value = testing.ListTestsResponse()
        client.list_tests(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'parent=parent_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_list_tests_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = testing.ListTestsRequest()

    request.parent = 'parent_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_tests),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(testing.ListTestsResponse())
        await client.list_tests(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'parent=parent_value',
    ) in kw['metadata']


def test_list_tests_pager(transport_name: str = "grpc"):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_tests),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                    testing.Test(),
                    testing.Test(),
                ],
                next_page_token='abc',
            ),
            testing.ListTestsResponse(
                tests=[],
                next_page_token='def',
            ),
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                ],
                next_page_token='ghi',
            ),
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                    testing.Test(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        expected_metadata = tuple(expected_metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ('parent', ''),
            )),
        )
        pager = client.list_tests(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == 'abc'
        assert str(pager).startswith(f'{pager.__class__.__name__}<')

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, testing.Test)
                   for i in results)
def test_list_tests_pages(transport_name: str = "grpc"):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_tests),
            '__call__') as call:
        # Set the response to a series of pages.
        call.side_effect = (
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                    testing.Test(),
                    testing.Test(),
                ],
                next_page_token='abc',
            ),
            testing.ListTestsResponse(
                tests=[],
                next_page_token='def',
            ),
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                ],
                next_page_token='ghi',
            ),
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                    testing.Test(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_tests(request={}).pages)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token

@pytest.mark.asyncio
async def test_list_tests_async_pager():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_tests),
            '__call__', new_callable=mock.AsyncMock) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                    testing.Test(),
                    testing.Test(),
                ],
                next_page_token='abc',
            ),
            testing.ListTestsResponse(
                tests=[],
                next_page_token='def',
            ),
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                ],
                next_page_token='ghi',
            ),
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                    testing.Test(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_tests(request={},)
        assert async_pager.next_page_token == 'abc'
        assert str(async_pager).startswith(f'{async_pager.__class__.__name__}<')

        responses = []
        async for response in async_pager: # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, testing.Test)
                for i in responses)


@pytest.mark.asyncio
async def test_list_tests_async_pages():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_tests),
            '__call__', new_callable=mock.AsyncMock) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                    testing.Test(),
                    testing.Test(),
                ],
                next_page_token='abc',
            ),
            testing.ListTestsResponse(
                tests=[],
                next_page_token='def',
            ),
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                ],
                next_page_token='ghi',
            ),
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                    testing.Test(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.list_tests(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token

@pytest.mark.parametrize("request_type", [
  testing.DeleteTestRequest(),
  {},
])
def test_delete_test(request_type, transport: str = 'grpc'):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_test),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = testing.DeleteTestRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_test_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = testing.DeleteTestRequest(
        name='name_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_test),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.delete_test(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.DeleteTestRequest(
            name='name_value',
        )
        assert args[0] == request_msg

def test_delete_test_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_test in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.delete_test] = mock_rpc
        request = {}
        client.delete_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_test(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_delete_test_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = TestingAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.delete_test in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.delete_test] = mock_rpc

        request = {}
        await client.delete_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.delete_test(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  testing.DeleteTestRequest(),
  {},
])
async def test_delete_test_async(request_type, transport: str = 'grpc_asyncio'):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_test),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = testing.DeleteTestRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None

def test_delete_test_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = testing.DeleteTestRequest()

    request.name = 'name_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_test),
            '__call__') as call:
        call.return_value = None
        client.delete_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'name=name_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_delete_test_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = testing.DeleteTestRequest()

    request.name = 'name_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_test),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'name=name_value',
    ) in kw['metadata']


@pytest.mark.parametrize("request_type", [
  testing.VerifyTestRequest(),
  {},
])
def test_verify_test(request_type, transport: str = 'grpc'):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.verify_test),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = testing.VerifyTestResponse(
        )
        response = client.verify_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = testing.VerifyTestRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.VerifyTestResponse)


def test_verify_test_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = testing.VerifyTestRequest(
        name='name_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.verify_test),
            '__call__') as call:
        call.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client.verify_test(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.VerifyTestRequest(
            name='name_value',
        )
        assert args[0] == request_msg

def test_verify_test_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.verify_test in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.verify_test] = mock_rpc
        request = {}
        client.verify_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.verify_test(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
async def test_verify_test_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = TestingAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._client._transport.verify_test in client._client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.verify_test] = mock_rpc

        request = {}
        await client.verify_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.verify_test(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2

@pytest.mark.asyncio
@pytest.mark.parametrize("request_type", [
  testing.VerifyTestRequest(),
  {},
])
async def test_verify_test_async(request_type, transport: str = 'grpc_asyncio'):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.verify_test),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value =grpc_helpers_async.FakeUnaryUnaryCall(testing.VerifyTestResponse(
        ))
        response = await client.verify_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = testing.VerifyTestRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.VerifyTestResponse)

def test_verify_test_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = testing.VerifyTestRequest()

    request.name = 'name_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.verify_test),
            '__call__') as call:
        call.return_value = testing.VerifyTestResponse()
        client.verify_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'name=name_value',
    ) in kw['metadata']


@pytest.mark.asyncio
async def test_verify_test_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = testing.VerifyTestRequest()

    request.name = 'name_value'

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.verify_test),
            '__call__') as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(testing.VerifyTestResponse())
        await client.verify_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        'x-goog-request-params',
        'name=name_value',
    ) in kw['metadata']


def test_create_session_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_session in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.create_session] = mock_rpc

        request = {}
        client.create_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_session(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_session_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_session in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.get_session] = mock_rpc

        request = {}
        client.get_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_session(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_sessions_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_sessions in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.list_sessions] = mock_rpc

        request = {}
        client.list_sessions(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_sessions(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_sessions_rest_pager(transport: str = 'rest'):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        #with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                    testing.Session(),
                    testing.Session(),
                ],
                next_page_token='abc',
            ),
            testing.ListSessionsResponse(
                sessions=[],
                next_page_token='def',
            ),
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                ],
                next_page_token='ghi',
            ),
            testing.ListSessionsResponse(
                sessions=[
                    testing.Session(),
                    testing.Session(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(testing.ListSessionsResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode('UTF-8')
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {}

        pager = client.list_sessions(request=sample_request)

        assert pager.next_page_token == 'abc'
        assert str(pager).startswith(f'{pager.__class__.__name__}<')

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, testing.Session)
                for i in results)

        pages = list(client.list_sessions(request=sample_request).pages)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token


def test_delete_session_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_session in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.delete_session] = mock_rpc

        request = {}
        client.delete_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_session(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_report_session_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.report_session in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.report_session] = mock_rpc

        request = {}
        client.report_session(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.report_session(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_tests_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_tests in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.list_tests] = mock_rpc

        request = {}
        client.list_tests(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_tests(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_tests_rest_pager(transport: str = 'rest'):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        #with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                    testing.Test(),
                    testing.Test(),
                ],
                next_page_token='abc',
            ),
            testing.ListTestsResponse(
                tests=[],
                next_page_token='def',
            ),
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                ],
                next_page_token='ghi',
            ),
            testing.ListTestsResponse(
                tests=[
                    testing.Test(),
                    testing.Test(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(testing.ListTestsResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode('UTF-8')
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {'parent': 'sessions/sample1'}

        pager = client.list_tests(request=sample_request)

        assert pager.next_page_token == 'abc'
        assert str(pager).startswith(f'{pager.__class__.__name__}<')

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, testing.Test)
                for i in results)

        pages = list(client.list_tests(request=sample_request).pages)
        for page_, token in zip(pages, ['abc','def','ghi', '']):
            assert page_.raw_page.next_page_token == token


def test_delete_test_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_test in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.delete_test] = mock_rpc

        request = {}
        client.delete_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_test(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_verify_test_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.verify_test in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = "foo" # operation_request.operation in compute client(s) expect a string.
        client._transport._wrapped_methods[client._transport.verify_test] = mock_rpc

        request = {}
        client.verify_test(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.verify_test(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.TestingGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.TestingGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = TestingClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.TestingGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = TestingClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = TestingClient(
            client_options=options,
            credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.TestingGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = TestingClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.TestingGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = TestingClient(transport=transport)
    assert client.transport is transport

def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.TestingGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.TestingGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

@pytest.mark.parametrize("transport_class", [
    transports.TestingGrpcTransport,
    transports.TestingGrpcAsyncIOTransport,
    transports.TestingRestTransport,
])
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, 'default') as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()

def test_transport_kind_grpc():
    transport = TestingClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_session_empty_call_grpc():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.create_session),
            '__call__') as call:
        call.return_value = testing.Session()
        client.create_session(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.CreateSessionRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_session_empty_call_grpc():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.get_session),
            '__call__') as call:
        call.return_value = testing.Session()
        client.get_session(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.GetSessionRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_sessions_empty_call_grpc():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.list_sessions),
            '__call__') as call:
        call.return_value = testing.ListSessionsResponse()
        client.list_sessions(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.ListSessionsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_session_empty_call_grpc():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_session),
            '__call__') as call:
        call.return_value = None
        client.delete_session(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.DeleteSessionRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_report_session_empty_call_grpc():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.report_session),
            '__call__') as call:
        call.return_value = testing.ReportSessionResponse()
        client.report_session(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.ReportSessionRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_tests_empty_call_grpc():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.list_tests),
            '__call__') as call:
        call.return_value = testing.ListTestsResponse()
        client.list_tests(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.ListTestsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_test_empty_call_grpc():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_test),
            '__call__') as call:
        call.return_value = None
        client.delete_test(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.DeleteTestRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_verify_test_empty_call_grpc():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.verify_test),
            '__call__') as call:
        call.return_value = testing.VerifyTestResponse()
        client.verify_test(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.VerifyTestRequest()
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = TestingAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_session_empty_call_grpc_asyncio():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.create_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(testing.Session(
            name='name_value',
            version=testing.Session.Version.V1_LATEST,
        ))
        await client.create_session(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.CreateSessionRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_session_empty_call_grpc_asyncio():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.get_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(testing.Session(
            name='name_value',
            version=testing.Session.Version.V1_LATEST,
        ))
        await client.get_session(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.GetSessionRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_sessions_empty_call_grpc_asyncio():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.list_sessions),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(testing.ListSessionsResponse(
            next_page_token='next_page_token_value',
        ))
        await client.list_sessions(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.ListSessionsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_session_empty_call_grpc_asyncio():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_session(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.DeleteSessionRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_report_session_empty_call_grpc_asyncio():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.report_session),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(testing.ReportSessionResponse(
            result=testing.ReportSessionResponse.Result.PASSED,
        ))
        await client.report_session(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.ReportSessionRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_tests_empty_call_grpc_asyncio():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.list_tests),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(testing.ListTestsResponse(
            next_page_token='next_page_token_value',
        ))
        await client.list_tests(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.ListTestsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_test_empty_call_grpc_asyncio():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_test),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_test(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.DeleteTestRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_verify_test_empty_call_grpc_asyncio():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.verify_test),
            '__call__') as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(testing.VerifyTestResponse(
        ))
        await client.verify_test(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.VerifyTestRequest()
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = TestingClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_create_session_rest_bad_request(request_type=testing.CreateSessionRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.create_session(request)


@pytest.mark.parametrize("request_type", [
  testing.CreateSessionRequest,
  dict,
])
def test_create_session_rest_call_success(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request_init["session"] = {'name': 'name_value', 'version': 1}
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = testing.CreateSessionRequest.meta.fields["session"]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else: # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init["session"].items(): # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {"field": field, "subfield": subfield, "is_repeated": is_repeated}
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime: # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(0, len(request_init["session"][field])):
                    del request_init["session"][field][i][subfield]
            else:
                del request_init["session"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = testing.Session(
              name='name_value',
              version=testing.Session.Version.V1_LATEST,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = testing.Session.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_session(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.Session)
    assert response.name == 'name_value'
    assert response.version == testing.Session.Version.V1_LATEST


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_session_rest_interceptors(null_interceptor):
    transport = transports.TestingRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.TestingRestInterceptor(),
        )
    client = TestingClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.TestingRestInterceptor, "post_create_session") as post, \
        mock.patch.object(transports.TestingRestInterceptor, "post_create_session_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.TestingRestInterceptor, "pre_create_session") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = testing.CreateSessionRequest.pb(testing.CreateSessionRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = testing.Session.to_json(testing.Session())
        req.return_value.content = return_value

        request = testing.CreateSessionRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = testing.Session()
        post_with_metadata.return_value = testing.Session(), metadata

        client.create_session(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_session_rest_bad_request(request_type=testing.GetSessionRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {'name': 'sessions/sample1'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_session(request)


@pytest.mark.parametrize("request_type", [
  testing.GetSessionRequest,
  dict,
])
def test_get_session_rest_call_success(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {'name': 'sessions/sample1'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = testing.Session(
              name='name_value',
              version=testing.Session.Version.V1_LATEST,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = testing.Session.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_session(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.Session)
    assert response.name == 'name_value'
    assert response.version == testing.Session.Version.V1_LATEST


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_session_rest_interceptors(null_interceptor):
    transport = transports.TestingRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.TestingRestInterceptor(),
        )
    client = TestingClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.TestingRestInterceptor, "post_get_session") as post, \
        mock.patch.object(transports.TestingRestInterceptor, "post_get_session_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.TestingRestInterceptor, "pre_get_session") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = testing.GetSessionRequest.pb(testing.GetSessionRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = testing.Session.to_json(testing.Session())
        req.return_value.content = return_value

        request = testing.GetSessionRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = testing.Session()
        post_with_metadata.return_value = testing.Session(), metadata

        client.get_session(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_sessions_rest_bad_request(request_type=testing.ListSessionsRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list_sessions(request)


@pytest.mark.parametrize("request_type", [
  testing.ListSessionsRequest,
  dict,
])
def test_list_sessions_rest_call_success(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = testing.ListSessionsResponse(
              next_page_token='next_page_token_value',
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = testing.ListSessionsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_sessions(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListSessionsPager)
    assert response.next_page_token == 'next_page_token_value'


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_sessions_rest_interceptors(null_interceptor):
    transport = transports.TestingRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.TestingRestInterceptor(),
        )
    client = TestingClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.TestingRestInterceptor, "post_list_sessions") as post, \
        mock.patch.object(transports.TestingRestInterceptor, "post_list_sessions_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.TestingRestInterceptor, "pre_list_sessions") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = testing.ListSessionsRequest.pb(testing.ListSessionsRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = testing.ListSessionsResponse.to_json(testing.ListSessionsResponse())
        req.return_value.content = return_value

        request = testing.ListSessionsRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = testing.ListSessionsResponse()
        post_with_metadata.return_value = testing.ListSessionsResponse(), metadata

        client.list_sessions(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_session_rest_bad_request(request_type=testing.DeleteSessionRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {'name': 'sessions/sample1'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.delete_session(request)


@pytest.mark.parametrize("request_type", [
  testing.DeleteSessionRequest,
  dict,
])
def test_delete_session_rest_call_success(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {'name': 'sessions/sample1'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = ''
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.delete_session(request)

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_session_rest_interceptors(null_interceptor):
    transport = transports.TestingRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.TestingRestInterceptor(),
        )
    client = TestingClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.TestingRestInterceptor, "pre_delete_session") as pre:
        pre.assert_not_called()
        pb_message = testing.DeleteSessionRequest.pb(testing.DeleteSessionRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        request = testing.DeleteSessionRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata

        client.delete_session(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()


def test_report_session_rest_bad_request(request_type=testing.ReportSessionRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {'name': 'sessions/sample1'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.report_session(request)


@pytest.mark.parametrize("request_type", [
  testing.ReportSessionRequest,
  dict,
])
def test_report_session_rest_call_success(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {'name': 'sessions/sample1'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = testing.ReportSessionResponse(
              result=testing.ReportSessionResponse.Result.PASSED,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = testing.ReportSessionResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.report_session(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.ReportSessionResponse)
    assert response.result == testing.ReportSessionResponse.Result.PASSED


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_report_session_rest_interceptors(null_interceptor):
    transport = transports.TestingRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.TestingRestInterceptor(),
        )
    client = TestingClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.TestingRestInterceptor, "post_report_session") as post, \
        mock.patch.object(transports.TestingRestInterceptor, "post_report_session_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.TestingRestInterceptor, "pre_report_session") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = testing.ReportSessionRequest.pb(testing.ReportSessionRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = testing.ReportSessionResponse.to_json(testing.ReportSessionResponse())
        req.return_value.content = return_value

        request = testing.ReportSessionRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = testing.ReportSessionResponse()
        post_with_metadata.return_value = testing.ReportSessionResponse(), metadata

        client.report_session(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_tests_rest_bad_request(request_type=testing.ListTestsRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {'parent': 'sessions/sample1'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list_tests(request)


@pytest.mark.parametrize("request_type", [
  testing.ListTestsRequest,
  dict,
])
def test_list_tests_rest_call_success(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {'parent': 'sessions/sample1'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = testing.ListTestsResponse(
              next_page_token='next_page_token_value',
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = testing.ListTestsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_tests(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListTestsPager)
    assert response.next_page_token == 'next_page_token_value'


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_tests_rest_interceptors(null_interceptor):
    transport = transports.TestingRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.TestingRestInterceptor(),
        )
    client = TestingClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.TestingRestInterceptor, "post_list_tests") as post, \
        mock.patch.object(transports.TestingRestInterceptor, "post_list_tests_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.TestingRestInterceptor, "pre_list_tests") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = testing.ListTestsRequest.pb(testing.ListTestsRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = testing.ListTestsResponse.to_json(testing.ListTestsResponse())
        req.return_value.content = return_value

        request = testing.ListTestsRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = testing.ListTestsResponse()
        post_with_metadata.return_value = testing.ListTestsResponse(), metadata

        client.list_tests(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_test_rest_bad_request(request_type=testing.DeleteTestRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {'name': 'sessions/sample1/tests/sample2'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.delete_test(request)


@pytest.mark.parametrize("request_type", [
  testing.DeleteTestRequest,
  dict,
])
def test_delete_test_rest_call_success(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {'name': 'sessions/sample1/tests/sample2'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = ''
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.delete_test(request)

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_test_rest_interceptors(null_interceptor):
    transport = transports.TestingRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.TestingRestInterceptor(),
        )
    client = TestingClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.TestingRestInterceptor, "pre_delete_test") as pre:
        pre.assert_not_called()
        pb_message = testing.DeleteTestRequest.pb(testing.DeleteTestRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        request = testing.DeleteTestRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata

        client.delete_test(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()


def test_verify_test_rest_bad_request(request_type=testing.VerifyTestRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {'name': 'sessions/sample1/tests/sample2'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.verify_test(request)


@pytest.mark.parametrize("request_type", [
  testing.VerifyTestRequest,
  dict,
])
def test_verify_test_rest_call_success(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {'name': 'sessions/sample1/tests/sample2'}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = testing.VerifyTestResponse(
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = testing.VerifyTestResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.verify_test(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, testing.VerifyTestResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_verify_test_rest_interceptors(null_interceptor):
    transport = transports.TestingRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.TestingRestInterceptor(),
        )
    client = TestingClient(transport=transport)

    with mock.patch.object(type(client.transport._session), "request") as req, \
        mock.patch.object(path_template, "transcode")  as transcode, \
        mock.patch.object(transports.TestingRestInterceptor, "post_verify_test") as post, \
        mock.patch.object(transports.TestingRestInterceptor, "post_verify_test_with_metadata") as post_with_metadata, \
        mock.patch.object(transports.TestingRestInterceptor, "pre_verify_test") as pre:
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = testing.VerifyTestRequest.pb(testing.VerifyTestRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = testing.VerifyTestResponse.to_json(testing.VerifyTestResponse())
        req.return_value.content = return_value

        request = testing.VerifyTestRequest()
        metadata =[
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = testing.VerifyTestResponse()
        post_with_metadata.return_value = testing.VerifyTestResponse(), metadata

        client.verify_test(request, metadata=[("key", "val"), ("cephalopod", "squid"),])

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_locations_rest_bad_request(request_type=locations_pb2.ListLocationsRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'name': 'projects/sample1'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list_locations(request)


@pytest.mark.parametrize("request_type", [
    locations_pb2.ListLocationsRequest,
    dict,
])
def test_list_locations_rest(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'name': 'projects/sample1'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = locations_pb2.ListLocationsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.list_locations(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.ListLocationsResponse)


def test_get_location_rest_bad_request(request_type=locations_pb2.GetLocationRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'name': 'projects/sample1/locations/sample2'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_location(request)


@pytest.mark.parametrize("request_type", [
    locations_pb2.GetLocationRequest,
    dict,
])
def test_get_location_rest(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'name': 'projects/sample1/locations/sample2'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = locations_pb2.Location()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.get_location(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.Location)


def test_set_iam_policy_rest_bad_request(request_type=iam_policy_pb2.SetIamPolicyRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'resource': 'users/sample1'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.set_iam_policy(request)


@pytest.mark.parametrize("request_type", [
    iam_policy_pb2.SetIamPolicyRequest,
    dict,
])
def test_set_iam_policy_rest(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'resource': 'users/sample1'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = policy_pb2.Policy()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.set_iam_policy(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)


def test_get_iam_policy_rest_bad_request(request_type=iam_policy_pb2.GetIamPolicyRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'resource': 'users/sample1'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_iam_policy(request)


@pytest.mark.parametrize("request_type", [
    iam_policy_pb2.GetIamPolicyRequest,
    dict,
])
def test_get_iam_policy_rest(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'resource': 'users/sample1'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = policy_pb2.Policy()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.get_iam_policy(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)


def test_test_iam_permissions_rest_bad_request(request_type=iam_policy_pb2.TestIamPermissionsRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'resource': 'users/sample1'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.test_iam_permissions(request)


@pytest.mark.parametrize("request_type", [
    iam_policy_pb2.TestIamPermissionsRequest,
    dict,
])
def test_test_iam_permissions_rest(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'resource': 'users/sample1'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = iam_policy_pb2.TestIamPermissionsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.test_iam_permissions(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, iam_policy_pb2.TestIamPermissionsResponse)


def test_list_operations_rest_bad_request(request_type=operations_pb2.ListOperationsRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list_operations(request)


@pytest.mark.parametrize("request_type", [
    operations_pb2.ListOperationsRequest,
    dict,
])
def test_list_operations_rest(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.ListOperationsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.list_operations(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.ListOperationsResponse)


def test_get_operation_rest_bad_request(request_type=operations_pb2.GetOperationRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'name': 'operations/sample1'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_operation(request)


@pytest.mark.parametrize("request_type", [
    operations_pb2.GetOperationRequest,
    dict,
])
def test_get_operation_rest(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'name': 'operations/sample1'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.get_operation(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.Operation)


def test_delete_operation_rest_bad_request(request_type=operations_pb2.DeleteOperationRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'name': 'operations/sample1'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.delete_operation(request)


@pytest.mark.parametrize("request_type", [
    operations_pb2.DeleteOperationRequest,
    dict,
])
def test_delete_operation_rest(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'name': 'operations/sample1'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = '{}'
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.delete_operation(request)

    # Establish that the response is the type that we expect.
    assert response is None


def test_cancel_operation_rest_bad_request(request_type=operations_pb2.CancelOperationRequest):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({'name': 'operations/sample1'}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with mock.patch.object(Session, 'request') as req, pytest.raises(core_exceptions.BadRequest):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ''
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.cancel_operation(request)


@pytest.mark.parametrize("request_type", [
    operations_pb2.CancelOperationRequest,
    dict,
])
def test_cancel_operation_rest(request_type):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {'name': 'operations/sample1'}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, 'request') as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = '{}'
        response_value.content = json_return_value.encode('UTF-8')

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.cancel_operation(request)

    # Establish that the response is the type that we expect.
    assert response is None

def test_initialize_client_w_rest():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_session_empty_call_rest():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.create_session),
            '__call__') as call:
        client.create_session(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.CreateSessionRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_session_empty_call_rest():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.get_session),
            '__call__') as call:
        client.get_session(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.GetSessionRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_sessions_empty_call_rest():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.list_sessions),
            '__call__') as call:
        client.list_sessions(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.ListSessionsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_session_empty_call_rest():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_session),
            '__call__') as call:
        client.delete_session(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.DeleteSessionRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_report_session_empty_call_rest():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.report_session),
            '__call__') as call:
        client.report_session(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.ReportSessionRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_tests_empty_call_rest():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.list_tests),
            '__call__') as call:
        client.list_tests(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.ListTestsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_test_empty_call_rest():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.delete_test),
            '__call__') as call:
        client.delete_test(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.DeleteTestRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_verify_test_empty_call_rest():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
            type(client.transport.verify_test),
            '__call__') as call:
        client.verify_test(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = testing.VerifyTestRequest()
        assert args[0] == request_msg


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.TestingGrpcTransport,
    )

def test_testing_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.TestingTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json"
        )


def test_testing_base_transport():
    # Instantiate the base transport.
    with mock.patch('google.showcase_v1beta1.services.testing.transports.TestingTransport.__init__') as Transport:
        Transport.return_value = None
        transport = transports.TestingTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        'create_session',
        'get_session',
        'list_sessions',
        'delete_session',
        'report_session',
        'list_tests',
        'delete_test',
        'verify_test',
        'set_iam_policy',
        'get_iam_policy',
        'test_iam_permissions',
        'get_location',
        'list_locations',
        'get_operation',
        'cancel_operation',
        'delete_operation',
        'list_operations',
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()

    # Catch all for all remaining methods and properties
    remainder = [
        'kind',
    ]
    for r in remainder:
        with pytest.raises(NotImplementedError):
            getattr(transport, r)()


def test_testing_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with mock.patch.object(google.auth, 'load_credentials_from_file', autospec=True) as load_creds, mock.patch('google.showcase_v1beta1.services.testing.transports.TestingTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.TestingTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with("credentials.json",
            scopes=None,
            default_scopes=(
),
            quota_project_id="octopus",
        )


def test_testing_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc, mock.patch('google.showcase_v1beta1.services.testing.transports.TestingTransport._prep_wrapped_messages') as Transport:
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.TestingTransport()
        adc.assert_called_once()


def test_testing_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        TestingClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.TestingGrpcTransport,
        transports.TestingGrpcAsyncIOTransport,
    ],
)
def test_testing_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, 'default', autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.TestingGrpcTransport,
        transports.TestingGrpcAsyncIOTransport,
        transports.TestingRestTransport,
    ],
)
def test_testing_transport_auth_gdch_credentials(transport_class):
    host = 'https://language.com'
    api_audience_tests = [None, 'https://language2.com']
    api_audience_expect = [host, 'https://language2.com']
    for t, e in zip(api_audience_tests, api_audience_expect):
        with mock.patch.object(google.auth, 'default', autospec=True) as adc:
            gdch_mock = mock.MagicMock()
            type(gdch_mock).with_gdch_audience = mock.PropertyMock(return_value=gdch_mock)
            adc.return_value = (gdch_mock, None)
            transport_class(host=host, api_audience=t)
            gdch_mock.with_gdch_audience.assert_called_once_with(
                e
            )


@pytest.mark.parametrize(
    "transport_class,grpc_helpers",
    [
        (transports.TestingGrpcTransport, grpc_helpers),
        (transports.TestingGrpcAsyncIOTransport, grpc_helpers_async)
    ],
)
def test_testing_transport_create_channel(transport_class, grpc_helpers):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc, mock.patch.object(
        grpc_helpers, "create_channel", autospec=True
    ) as create_channel:
        creds = ga_credentials.AnonymousCredentials()
        adc.return_value = (creds, None)
        transport_class(
            quota_project_id="octopus",
            scopes=["1", "2"]
        )

        create_channel.assert_called_with(
            "localhost:7469",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
),
            scopes=["1", "2"],
            default_host="localhost:7469",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize("transport_class", [transports.TestingGrpcTransport, transports.TestingGrpcAsyncIOTransport])
def test_testing_grpc_transport_client_cert_source_for_mtls(
    transport_class
):
    cred = ga_credentials.AnonymousCredentials()

    # Check ssl_channel_credentials is used if provided.
    with mock.patch.object(transport_class, "create_channel") as mock_create_channel:
        mock_ssl_channel_creds = mock.Mock()
        transport_class(
            host="squid.clam.whelk",
            credentials=cred,
            ssl_channel_credentials=mock_ssl_channel_creds
        )
        mock_create_channel.assert_called_once_with(
            "squid.clam.whelk:443",
            credentials=cred,
            credentials_file=None,
            scopes=None,
            ssl_credentials=mock_ssl_channel_creds,
            quota_project_id=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )

    # Check if ssl_channel_credentials is not provided, then client_cert_source_for_mtls
    # is used.
    with mock.patch.object(transport_class, "create_channel", return_value=mock.Mock()):
        with mock.patch("grpc.ssl_channel_credentials") as mock_ssl_cred:
            transport_class(
                credentials=cred,
                client_cert_source_for_mtls=client_cert_source_callback
            )
            expected_cert, expected_key = client_cert_source_callback()
            mock_ssl_cred.assert_called_once_with(
                certificate_chain=expected_cert,
                private_key=expected_key
            )

def test_testing_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch("google.auth.transport.requests.AuthorizedSession.configure_mtls_channel") as mock_configure_mtls_channel:
        transports.TestingRestTransport (
            credentials=cred,
            client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


@pytest.mark.parametrize("transport_name", [
    "grpc",
    "grpc_asyncio",
    "rest",
])
def test_testing_host_no_port(transport_name):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='localhost'),
         transport=transport_name,
    )
    assert client.transport._host == (
        'localhost:443'
        if transport_name in ['grpc', 'grpc_asyncio']
        else 'https://localhost'
    )

@pytest.mark.parametrize("transport_name", [
    "grpc",
    "grpc_asyncio",
    "rest",
])
def test_testing_host_with_port(transport_name):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint='localhost:8000'),
        transport=transport_name,
    )
    assert client.transport._host == (
        'localhost:8000'
        if transport_name in ['grpc', 'grpc_asyncio']
        else 'https://localhost:8000'
    )

@pytest.mark.parametrize("transport_name", [
    "rest",
])
def test_testing_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = TestingClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = TestingClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.create_session._session
    session2 = client2.transport.create_session._session
    assert session1 != session2
    session1 = client1.transport.get_session._session
    session2 = client2.transport.get_session._session
    assert session1 != session2
    session1 = client1.transport.list_sessions._session
    session2 = client2.transport.list_sessions._session
    assert session1 != session2
    session1 = client1.transport.delete_session._session
    session2 = client2.transport.delete_session._session
    assert session1 != session2
    session1 = client1.transport.report_session._session
    session2 = client2.transport.report_session._session
    assert session1 != session2
    session1 = client1.transport.list_tests._session
    session2 = client2.transport.list_tests._session
    assert session1 != session2
    session1 = client1.transport.delete_test._session
    session2 = client2.transport.delete_test._session
    assert session1 != session2
    session1 = client1.transport.verify_test._session
    session2 = client2.transport.verify_test._session
    assert session1 != session2
def test_testing_grpc_transport_channel():
    channel = grpc.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.TestingGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_testing_grpc_asyncio_transport_channel():
    channel = aio.secure_channel('http://localhost/', grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.TestingGrpcAsyncIOTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.filterwarnings("ignore::FutureWarning")
@pytest.mark.parametrize("transport_class", [transports.TestingGrpcTransport, transports.TestingGrpcAsyncIOTransport])
def test_testing_transport_channel_mtls_with_client_cert_source(
    transport_class
):
    with mock.patch("grpc.ssl_channel_credentials", autospec=True) as grpc_ssl_channel_cred:
        with mock.patch.object(transport_class, "create_channel") as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = ga_credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(google.auth, 'default') as adc:
                    adc.return_value = (cred, None)
                    transport = transport_class(
                        host="squid.clam.whelk",
                        api_mtls_endpoint="mtls.squid.clam.whelk",
                        client_cert_source=client_cert_source_callback,
                    )
                    adc.assert_called_once()

            grpc_ssl_channel_cred.assert_called_once_with(
                certificate_chain=b"cert bytes", private_key=b"key bytes"
            )
            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel
            assert transport._ssl_channel_credentials == mock_ssl_cred


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.parametrize("transport_class", [transports.TestingGrpcTransport, transports.TestingGrpcAsyncIOTransport])
def test_testing_transport_channel_mtls_with_adc(
    transport_class
):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(transport_class, "create_channel") as grpc_create_channel:
            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel
            mock_cred = mock.Mock()

            with pytest.warns(DeprecationWarning):
                transport = transport_class(
                    host="squid.clam.whelk",
                    credentials=mock_cred,
                    api_mtls_endpoint="mtls.squid.clam.whelk",
                    client_cert_source=None,
                )

            grpc_create_channel.assert_called_once_with(
                "mtls.squid.clam.whelk:443",
                credentials=mock_cred,
                credentials_file=None,
                scopes=None,
                ssl_credentials=mock_ssl_cred,
                quota_project_id=None,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )
            assert transport.grpc_channel == mock_grpc_channel


def test_blueprint_path():
    session = "squid"
    test = "clam"
    blueprint = "whelk"
    expected = "sessions/{session}/tests/{test}/blueprints/{blueprint}".format(session=session, test=test, blueprint=blueprint, )
    actual = TestingClient.blueprint_path(session, test, blueprint)
    assert expected == actual


def test_parse_blueprint_path():
    expected = {
        "session": "octopus",
        "test": "oyster",
        "blueprint": "nudibranch",
    }
    path = TestingClient.blueprint_path(**expected)

    # Check that the path construction is reversible.
    actual = TestingClient.parse_blueprint_path(path)
    assert expected == actual

def test_session_path():
    session = "cuttlefish"
    expected = "sessions/{session}".format(session=session, )
    actual = TestingClient.session_path(session)
    assert expected == actual


def test_parse_session_path():
    expected = {
        "session": "mussel",
    }
    path = TestingClient.session_path(**expected)

    # Check that the path construction is reversible.
    actual = TestingClient.parse_session_path(path)
    assert expected == actual

def test_test_path():
    session = "winkle"
    test = "nautilus"
    expected = "sessions/{session}/tests/{test}".format(session=session, test=test, )
    actual = TestingClient.test_path(session, test)
    assert expected == actual


def test_parse_test_path():
    expected = {
        "session": "scallop",
        "test": "abalone",
    }
    path = TestingClient.test_path(**expected)

    # Check that the path construction is reversible.
    actual = TestingClient.parse_test_path(path)
    assert expected == actual

def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(billing_account=billing_account, )
    actual = TestingClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = TestingClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = TestingClient.parse_common_billing_account_path(path)
    assert expected == actual

def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(folder=folder, )
    actual = TestingClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = TestingClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = TestingClient.parse_common_folder_path(path)
    assert expected == actual

def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(organization=organization, )
    actual = TestingClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = TestingClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = TestingClient.parse_common_organization_path(path)
    assert expected == actual

def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(project=project, )
    actual = TestingClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = TestingClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = TestingClient.parse_common_project_path(path)
    assert expected == actual

def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(project=project, location=location, )
    actual = TestingClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = TestingClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = TestingClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(transports.TestingTransport, '_prep_wrapped_messages') as prep:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(transports.TestingTransport, '_prep_wrapped_messages') as prep:
        transport_class = TestingClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_delete_operation(transport: str = "grpc"):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.DeleteOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None

@pytest.mark.asyncio
async def test_delete_operation_async(transport: str = "grpc_asyncio"):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.DeleteOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        response = await client.delete_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_operation_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.DeleteOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        call.return_value =  None

        client.delete_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]

@pytest.mark.asyncio
async def test_delete_operation_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.DeleteOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        await client.delete_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]


def test_delete_operation_from_dict():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        response = client.delete_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()

@pytest.mark.asyncio
async def test_delete_operation_from_dict_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        response = await client.delete_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_delete_operation_flattened():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        client.delete_operation()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == operations_pb2.DeleteOperationRequest()

@pytest.mark.asyncio
async def test_delete_operation_flattened_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        await client.delete_operation()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == operations_pb2.DeleteOperationRequest()


def test_cancel_operation(transport: str = "grpc"):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.CancelOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.cancel_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None

@pytest.mark.asyncio
async def test_cancel_operation_async(transport: str = "grpc_asyncio"):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.CancelOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        response = await client.cancel_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_cancel_operation_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.CancelOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        call.return_value =  None

        client.cancel_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]

@pytest.mark.asyncio
async def test_cancel_operation_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.CancelOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        await client.cancel_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]


def test_cancel_operation_from_dict():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        response = client.cancel_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()

@pytest.mark.asyncio
async def test_cancel_operation_from_dict_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        response = await client.cancel_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_cancel_operation_flattened():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        client.cancel_operation()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == operations_pb2.CancelOperationRequest()

@pytest.mark.asyncio
async def test_cancel_operation_flattened_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            None
        )
        await client.cancel_operation()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == operations_pb2.CancelOperationRequest()


def test_get_operation(transport: str = "grpc"):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.GetOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation()
        response = client.get_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.Operation)

@pytest.mark.asyncio
async def test_get_operation_async(transport: str = "grpc_asyncio"):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.GetOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation()
        )
        response = await client.get_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.Operation)


def test_get_operation_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.GetOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_operation), "__call__") as call:
        call.return_value = operations_pb2.Operation()

        client.get_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]

@pytest.mark.asyncio
async def test_get_operation_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.GetOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_operation), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation()
        )
        await client.get_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]


def test_get_operation_from_dict():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation()

        response = client.get_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()

@pytest.mark.asyncio
async def test_get_operation_from_dict_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation()
        )
        response = await client.get_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_get_operation_flattened():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation()

        client.get_operation()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == operations_pb2.GetOperationRequest()

@pytest.mark.asyncio
async def test_get_operation_flattened_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation()
        )
        await client.get_operation()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == operations_pb2.GetOperationRequest()


def test_list_operations(transport: str = "grpc"):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.ListOperationsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_operations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.ListOperationsResponse()
        response = client.list_operations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.ListOperationsResponse)

@pytest.mark.asyncio
async def test_list_operations_async(transport: str = "grpc_asyncio"):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.ListOperationsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_operations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.ListOperationsResponse()
        )
        response = await client.list_operations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.ListOperationsResponse)


def test_list_operations_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.ListOperationsRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_operations), "__call__") as call:
        call.return_value = operations_pb2.ListOperationsResponse()

        client.list_operations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]

@pytest.mark.asyncio
async def test_list_operations_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.ListOperationsRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_operations), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.ListOperationsResponse()
        )
        await client.list_operations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]


def test_list_operations_from_dict():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_operations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.ListOperationsResponse()

        response = client.list_operations(
            request={
                "name": "locations",
            }
        )
        call.assert_called()

@pytest.mark.asyncio
async def test_list_operations_from_dict_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_operations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.ListOperationsResponse()
        )
        response = await client.list_operations(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_list_operations_flattened():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_operations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.ListOperationsResponse()

        client.list_operations()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == operations_pb2.ListOperationsRequest()

@pytest.mark.asyncio
async def test_list_operations_flattened_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_operations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.ListOperationsResponse()
        )
        await client.list_operations()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == operations_pb2.ListOperationsRequest()


def test_list_locations(transport: str = "grpc"):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = locations_pb2.ListLocationsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.ListLocationsResponse()
        response = client.list_locations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.ListLocationsResponse)

@pytest.mark.asyncio
async def test_list_locations_async(transport: str = "grpc_asyncio"):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = locations_pb2.ListLocationsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.ListLocationsResponse()
        )
        response = await client.list_locations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.ListLocationsResponse)


def test_list_locations_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = locations_pb2.ListLocationsRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        call.return_value = locations_pb2.ListLocationsResponse()

        client.list_locations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]

@pytest.mark.asyncio
async def test_list_locations_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = locations_pb2.ListLocationsRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.ListLocationsResponse()
        )
        await client.list_locations(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations",) in kw["metadata"]


def test_list_locations_from_dict():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.ListLocationsResponse()

        response = client.list_locations(
            request={
                "name": "locations",
            }
        )
        call.assert_called()

@pytest.mark.asyncio
async def test_list_locations_from_dict_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.ListLocationsResponse()
        )
        response = await client.list_locations(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_list_locations_flattened():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.ListLocationsResponse()

        client.list_locations()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == locations_pb2.ListLocationsRequest()

@pytest.mark.asyncio
async def test_list_locations_flattened_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.ListLocationsResponse()
        )
        await client.list_locations()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == locations_pb2.ListLocationsRequest()


def test_get_location(transport: str = "grpc"):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = locations_pb2.GetLocationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.Location()
        response = client.get_location(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.Location)

@pytest.mark.asyncio
async def test_get_location_async(transport: str = "grpc_asyncio"):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = locations_pb2.GetLocationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.Location()
        )
        response = await client.get_location(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, locations_pb2.Location)


def test_get_location_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials())

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = locations_pb2.GetLocationRequest()
    request.name = "locations/abc"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        call.return_value = locations_pb2.Location()

        client.get_location(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations/abc",) in kw["metadata"]

@pytest.mark.asyncio
async def test_get_location_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials()
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = locations_pb2.GetLocationRequest()
    request.name = "locations/abc"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.Location()
        )
        await client.get_location(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "name=locations/abc",) in kw["metadata"]


def test_get_location_from_dict():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.Location()

        response = client.get_location(
            request={
                "name": "locations/abc",
            }
        )
        call.assert_called()

@pytest.mark.asyncio
async def test_get_location_from_dict_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_locations), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.Location()
        )
        response = await client.get_location(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_get_location_flattened():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = locations_pb2.Location()

        client.get_location()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == locations_pb2.GetLocationRequest()

@pytest.mark.asyncio
async def test_get_location_flattened_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_location), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            locations_pb2.Location()
        )
        await client.get_location()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == locations_pb2.GetLocationRequest()


def test_set_iam_policy(transport: str = "grpc"):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.SetIamPolicyRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy(version=774, etag=b"etag_blob",)
        response = client.set_iam_policy(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)

    assert response.version == 774

    assert response.etag == b"etag_blob"

@pytest.mark.asyncio
async def test_set_iam_policy_async(transport: str = "grpc_asyncio"):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.SetIamPolicyRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            policy_pb2.Policy(version=774, etag=b"etag_blob",)
        )
        response = await client.set_iam_policy(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)

    assert response.version == 774

    assert response.etag == b"etag_blob"


def test_set_iam_policy_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.SetIamPolicyRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        call.return_value = policy_pb2.Policy()

        client.set_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "resource=resource/value",) in kw["metadata"]

@pytest.mark.asyncio
async def test_set_iam_policy_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.SetIamPolicyRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(policy_pb2.Policy())

        await client.set_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "resource=resource/value",) in kw["metadata"]


def test_set_iam_policy_from_dict():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy()

        response = client.set_iam_policy(
            request={
                "resource": "resource_value",
                "policy": policy_pb2.Policy(version=774),
            }
        )
        call.assert_called()


@pytest.mark.asyncio
async def test_set_iam_policy_from_dict_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            policy_pb2.Policy()
        )

        response = await client.set_iam_policy(
            request={
                "resource": "resource_value",
                "policy": policy_pb2.Policy(version=774),
            }
        )
        call.assert_called()


def test_set_iam_policy_flattened():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy()

        client.set_iam_policy()

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == iam_policy_pb2.SetIamPolicyRequest()


@pytest.mark.asyncio
async def test_set_iam_policy_flattened_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.set_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            policy_pb2.Policy()
        )

        await client.set_iam_policy()

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == iam_policy_pb2.SetIamPolicyRequest()

def test_get_iam_policy(transport: str = "grpc"):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.GetIamPolicyRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy(version=774, etag=b"etag_blob",)

        response = client.get_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)

    assert response.version == 774

    assert response.etag == b"etag_blob"


@pytest.mark.asyncio
async def test_get_iam_policy_async(transport: str = "grpc_asyncio"):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.GetIamPolicyRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_iam_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            policy_pb2.Policy(version=774, etag=b"etag_blob",)
        )

        response = await client.get_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, policy_pb2.Policy)

    assert response.version == 774

    assert response.etag == b"etag_blob"


def test_get_iam_policy_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.GetIamPolicyRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        call.return_value = policy_pb2.Policy()

        client.get_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "resource=resource/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_iam_policy_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.GetIamPolicyRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_iam_policy), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(policy_pb2.Policy())

        await client.get_iam_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "resource=resource/value",) in kw["metadata"]


def test_get_iam_policy_from_dict():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy()

        response = client.get_iam_policy(
            request={
                "resource": "resource_value",
                "options": options_pb2.GetPolicyOptions(requested_policy_version=2598),
            }
        )
        call.assert_called()

@pytest.mark.asyncio
async def test_get_iam_policy_from_dict_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            policy_pb2.Policy()
        )

        response = await client.get_iam_policy(
            request={
                "resource": "resource_value",
                "options": options_pb2.GetPolicyOptions(requested_policy_version=2598),
            }
        )
        call.assert_called()


def test_get_iam_policy_flattened():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = policy_pb2.Policy()

        client.get_iam_policy()

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == iam_policy_pb2.GetIamPolicyRequest()


@pytest.mark.asyncio
async def test_get_iam_policy_flattened_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_iam_policy), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            policy_pb2.Policy()
        )

        await client.get_iam_policy()

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == iam_policy_pb2.GetIamPolicyRequest()

def test_test_iam_permissions(transport: str = "grpc"):
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.TestIamPermissionsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = iam_policy_pb2.TestIamPermissionsResponse(
            permissions=["permissions_value"],
        )

        response = client.test_iam_permissions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, iam_policy_pb2.TestIamPermissionsResponse)

    assert response.permissions == ["permissions_value"]


@pytest.mark.asyncio
async def test_test_iam_permissions_async(transport: str = "grpc_asyncio"):
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(), transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = iam_policy_pb2.TestIamPermissionsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            iam_policy_pb2.TestIamPermissionsResponse(permissions=["permissions_value"],)
        )

        response = await client.test_iam_permissions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]

        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, iam_policy_pb2.TestIamPermissionsResponse)

    assert response.permissions == ["permissions_value"]


def test_test_iam_permissions_field_headers():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.TestIamPermissionsRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        call.return_value = iam_policy_pb2.TestIamPermissionsResponse()

        client.test_iam_permissions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "resource=resource/value",) in kw["metadata"]


@pytest.mark.asyncio
async def test_test_iam_permissions_field_headers_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = iam_policy_pb2.TestIamPermissionsRequest()
    request.resource = "resource/value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            iam_policy_pb2.TestIamPermissionsResponse()
        )

        await client.test_iam_permissions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert ("x-goog-request-params", "resource=resource/value",) in kw["metadata"]


def test_test_iam_permissions_from_dict():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = iam_policy_pb2.TestIamPermissionsResponse()

        response = client.test_iam_permissions(
            request={
                "resource": "resource_value",
                "permissions": ["permissions_value"],
            }
        )
        call.assert_called()

@pytest.mark.asyncio
async def test_test_iam_permissions_from_dict_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.test_iam_permissions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            iam_policy_pb2.TestIamPermissionsResponse()
        )

        response = await client.test_iam_permissions(
            request={
                "resource": "resource_value",
                "permissions": ["permissions_value"],
            }
        )
        call.assert_called()


def test_test_iam_permissions_flattened():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.test_iam_permissions), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = iam_policy_pb2.TestIamPermissionsResponse()

        client.test_iam_permissions()

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == iam_policy_pb2.TestIamPermissionsRequest()


@pytest.mark.asyncio
async def test_test_iam_permissions_flattened_async():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.test_iam_permissions), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            iam_policy_pb2.TestIamPermissionsResponse()
        )

        await client.test_iam_permissions()

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == iam_policy_pb2.TestIamPermissionsRequest()


def test_transport_close_grpc():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc"
    )
    with mock.patch.object(type(getattr(client.transport, "_grpc_channel")), "close") as close:
        with client:
            close.assert_not_called()
        close.assert_called_once()


@pytest.mark.asyncio
async def test_transport_close_grpc_asyncio():
    client = TestingAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio"
    )
    with mock.patch.object(type(getattr(client.transport, "_grpc_channel")), "close") as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = TestingClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest"
    )
    with mock.patch.object(type(getattr(client.transport, "_session")), "close") as close:
        with client:
            close.assert_not_called()
        close.assert_called_once()


def test_client_ctx():
    transports = [
        'rest',
        'grpc',
    ]
    for transport in transports:
        client = TestingClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()

@pytest.mark.parametrize("client_class,transport_class", [
    (TestingClient, transports.TestingGrpcTransport),
    (TestingAsyncClient, transports.TestingGrpcAsyncIOTransport),
])
def test_api_key_credentials(client_class, transport_class):
    with mock.patch.object(
        google.auth._default, "get_api_key_credentials", create=True
    ) as get_api_key_credentials:
        mock_cred = mock.Mock()
        get_api_key_credentials.return_value = mock_cred
        options = client_options.ClientOptions()
        options.api_key = "api_key"
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options)
            patched.assert_called_once_with(
                credentials=mock_cred,
                credentials_file=None,
                host=client._DEFAULT_ENDPOINT_TEMPLATE.format(UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE),
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )


def test_testing_base_transport_wrap_method_modern_api_core(monkeypatch):
    monkeypatch.setattr(transports.base, "_WRAP_METHOD_SUPPORTS_TRACING", True)
    # 1. Concrete transport: passes client_options=None and kind="grpc"
    with mock.patch.object(transports.base.gapic_v1.method, "wrap_method") as mock_wrap:
        transport = transports.TestingGrpcTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        transport._wrap_method(func)
        assert mock_wrap.call_args.kwargs["kind"] == "grpc"
        assert "client_options" in mock_wrap.call_args.kwargs

    # 2. Base transport: kind raises NotImplementedError and is cleanly omitted
    with mock.patch.object(transports.base.gapic_v1.method, "wrap_method") as mock_wrap:
        options = client_options.ClientOptions()
        base_transport = transports.TestingTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            client_options=options,
        )
        assert base_transport._client_options.api_endpoint == base_transport._host
        dict_options = {}
        dict_transport = transports.TestingTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            client_options=dict_options,
        )
        assert dict_transport._client_options["api_endpoint"] == dict_transport._host
        func = mock.MagicMock()
        base_transport._wrap_method(func)
        assert "kind" not in mock_wrap.call_args.kwargs
        assert "client_options" in mock_wrap.call_args.kwargs


def test_testing_base_transport_wrap_method_older_api_core_fallbacks(monkeypatch):
    monkeypatch.setattr(transports.base, "_WRAP_METHOD_SUPPORTS_TRACING", False)
    with mock.patch.object(transports.base.gapic_v1.method, "wrap_method"):
        transport = transports.TestingGrpcTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )

    # Era 1: Ancient google-api-core (< 2.29.0: can be removed once google-api-core < 2.29.0 is no longer supported)
    monkeypatch.setattr(transports.base, "_WRAP_METHOD_SUPPORTS_KIND", False)
    with mock.patch.object(transports.base.gapic_v1.method, "wrap_method") as mock_wrap:
        func = mock.MagicMock()
        transport._wrap_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert "kind" not in kwargs
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs

    with mock.patch.object(transports.base.gapic_v1.method, "wrap_method") as mock_wrap:
        base_transport = transports.TestingTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        base_transport._wrap_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert "kind" not in kwargs
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs

    # Era 2: Intermediate google-api-core (>= 2.29.0, < 2.36.0: can be removed once google-api-core < 2.36.0 is no longer supported)
    monkeypatch.setattr(transports.base, "_WRAP_METHOD_SUPPORTS_KIND", True)
    with mock.patch.object(transports.base.gapic_v1.method, "wrap_method") as mock_wrap:
        func = mock.MagicMock()
        transport._wrap_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert kwargs.get("kind") == "grpc"
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs

    with mock.patch.object(transports.base.gapic_v1.method, "wrap_method") as mock_wrap:
        base_transport = transports.TestingTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        base_transport._wrap_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert "kind" not in kwargs
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs


def test_testing_base_transport_wrap_async_method_modern_api_core(monkeypatch):
    monkeypatch.setattr(transports.base, "_ASYNC_WRAP_METHOD_SUPPORTS_TRACING", True)
    # 1. Concrete transport: passes client_options=None and kind="grpc_asyncio"
    with mock.patch.object(transports.base.gapic_v1.method_async, "wrap_method") as mock_wrap:
        transport = transports.TestingGrpcAsyncIOTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        transport._wrap_async_method(func)
        assert mock_wrap.call_args.kwargs["kind"] == "grpc_asyncio"
        assert "client_options" in mock_wrap.call_args.kwargs

    # 2. Base transport: kind raises NotImplementedError and is cleanly omitted
    with mock.patch.object(transports.base.gapic_v1.method_async, "wrap_method") as mock_wrap:
        base_transport = transports.TestingTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        base_transport._wrap_async_method(func)
        assert "kind" not in mock_wrap.call_args.kwargs
        assert "client_options" in mock_wrap.call_args.kwargs


def test_testing_base_transport_wrap_async_method_older_api_core_fallbacks(monkeypatch):
    monkeypatch.setattr(transports.base, "_ASYNC_WRAP_METHOD_SUPPORTS_TRACING", False)
    with mock.patch.object(transports.base.gapic_v1.method_async, "wrap_method"):
        transport = transports.TestingGrpcAsyncIOTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )

    # Era 1: Ancient google-api-core (< 2.29.0: can be removed once google-api-core < 2.29.0 is no longer supported)
    monkeypatch.setattr(transports.base, "_ASYNC_WRAP_METHOD_SUPPORTS_KIND", False)
    with mock.patch.object(transports.base.gapic_v1.method_async, "wrap_method") as mock_wrap:
        func = mock.MagicMock()
        transport._wrap_async_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert "kind" not in kwargs
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs

    with mock.patch.object(transports.base.gapic_v1.method_async, "wrap_method") as mock_wrap:
        base_transport = transports.TestingTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        base_transport._wrap_async_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert "kind" not in kwargs
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs

    # Era 2: Intermediate google-api-core (>= 2.29.0, < 2.36.0: can be removed once google-api-core < 2.36.0 is no longer supported)
    monkeypatch.setattr(transports.base, "_ASYNC_WRAP_METHOD_SUPPORTS_KIND", True)
    with mock.patch.object(transports.base.gapic_v1.method_async, "wrap_method") as mock_wrap:
        func = mock.MagicMock()
        transport._wrap_async_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert kwargs.get("kind") == "grpc_asyncio"
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs

    with mock.patch.object(transports.base.gapic_v1.method_async, "wrap_method") as mock_wrap:
        base_transport = transports.TestingTransport(
            credentials=ga_credentials.AnonymousCredentials()
        )
        func = mock.MagicMock()
        base_transport._wrap_async_method(
            func,
            client_options="fake_options",
            method_name="fake_method",
            is_streaming=False,
        )
        kwargs = mock_wrap.call_args.kwargs
        assert "kind" not in kwargs
        assert "client_options" not in kwargs
        assert "method_name" not in kwargs
        assert "is_streaming" not in kwargs
