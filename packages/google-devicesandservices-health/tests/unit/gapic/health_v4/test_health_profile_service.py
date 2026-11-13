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
import asyncio
import json
import math
import os
from collections.abc import AsyncIterable, Iterable, Mapping, Sequence
from unittest import mock
from unittest.mock import AsyncMock

import grpc
import pytest
from google.api_core import api_core_version
from google.protobuf import json_format
from grpc.experimental import aio
from proto.marshal.rules import wrappers
from proto.marshal.rules.dates import DurationRule, TimestampRule
from requests import PreparedRequest, Request, Response
from requests.sessions import Session

try:
    from google.auth.aio import credentials as ga_credentials_async

    HAS_GOOGLE_AUTH_AIO = True
except ImportError:  # pragma: NO COVER
    HAS_GOOGLE_AUTH_AIO = False

import google.auth
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
from google.api_core import (
    client_options,
    gapic_v1,
    grpc_helpers,
    grpc_helpers_async,
    path_template,
)
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.oauth2 import service_account

from google.devicesandservices.health_v4.services.health_profile_service import (
    HealthProfileServiceAsyncClient,
    HealthProfileServiceClient,
    pagers,
    transports,
)
from google.devicesandservices.health_v4.types import health_profile

CRED_INFO_JSON = {
    "credential_source": "/path/to/file",
    "credential_type": "service account credentials",
    "principal": "service-account@example.com",
}
CRED_INFO_STRING = json.dumps(CRED_INFO_JSON)


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
    return (
        "foo.googleapis.com"
        if ("localhost" in client.DEFAULT_ENDPOINT)
        else client.DEFAULT_ENDPOINT
    )


# If default endpoint template is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint template so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint_template(client):
    return (
        "test.{UNIVERSE_DOMAIN}"
        if ("localhost" in client._DEFAULT_ENDPOINT_TEMPLATE)
        else client._DEFAULT_ENDPOINT_TEMPLATE
    )


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

    assert HealthProfileServiceClient._get_client_cert_source(None, False) is None
    assert (
        HealthProfileServiceClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        HealthProfileServiceClient._get_client_cert_source(
            mock_provided_cert_source, True
        )
        == mock_provided_cert_source
    )

    with mock.patch(
        "google.auth.transport.mtls.has_default_client_cert_source", return_value=True
    ):
        with mock.patch(
            "google.auth.transport.mtls.default_client_cert_source",
            return_value=mock_default_cert_source,
        ):
            assert (
                HealthProfileServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                HealthProfileServiceClient._get_client_cert_source(
                    mock_provided_cert_source, "true"
                )
                is mock_provided_cert_source
            )


@pytest.mark.parametrize(
    "error_code,cred_info_json,show_cred_info",
    [
        (401, CRED_INFO_JSON, True),
        (403, CRED_INFO_JSON, True),
        (404, CRED_INFO_JSON, True),
        (500, CRED_INFO_JSON, False),
        (401, None, False),
        (403, None, False),
        (404, None, False),
        (500, None, False),
    ],
)
def test__add_cred_info_for_auth_errors(error_code, cred_info_json, show_cred_info):
    cred = mock.Mock(["get_cred_info"])
    cred.get_cred_info = mock.Mock(return_value=cred_info_json)
    client = HealthProfileServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=["foo"])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    if show_cred_info:
        assert error.details == ["foo", CRED_INFO_STRING]
    else:
        assert error.details == ["foo"]


@pytest.mark.parametrize("error_code", [401, 403, 404, 500])
def test__add_cred_info_for_auth_errors_no_get_cred_info(error_code):
    cred = mock.Mock([])
    assert not hasattr(cred, "get_cred_info")
    client = HealthProfileServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (HealthProfileServiceClient, "grpc"),
        (HealthProfileServiceAsyncClient, "grpc_asyncio"),
        (HealthProfileServiceClient, "rest"),
    ],
)
def test_health_profile_service_client_from_service_account_info(
    client_class, transport_name
):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_info"
    ) as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info, transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            "health.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://health.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.HealthProfileServiceGrpcTransport, "grpc"),
        (transports.HealthProfileServiceGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.HealthProfileServiceRestTransport, "rest"),
    ],
)
def test_health_profile_service_client_service_account_always_use_jwt(
    transport_class, transport_name
):
    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (HealthProfileServiceClient, "grpc"),
        (HealthProfileServiceAsyncClient, "grpc_asyncio"),
        (HealthProfileServiceClient, "rest"),
    ],
)
def test_health_profile_service_client_from_service_account_file(
    client_class, transport_name
):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file(
            "dummy/file/path.json", transport=transport_name
        )
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json(
            "dummy/file/path.json", transport=transport_name
        )
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            "health.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://health.googleapis.com"
        )


def test_health_profile_service_client_get_transport_class():
    transport = HealthProfileServiceClient.get_transport_class()
    available_transports = [
        transports.HealthProfileServiceGrpcTransport,
        transports.HealthProfileServiceRestTransport,
    ]
    assert transport in available_transports

    transport = HealthProfileServiceClient.get_transport_class("grpc")
    assert transport == transports.HealthProfileServiceGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            HealthProfileServiceClient,
            transports.HealthProfileServiceGrpcTransport,
            "grpc",
        ),
        (
            HealthProfileServiceAsyncClient,
            transports.HealthProfileServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            HealthProfileServiceClient,
            transports.HealthProfileServiceRestTransport,
            "rest",
        ),
    ],
)
@mock.patch.object(
    HealthProfileServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(HealthProfileServiceClient),
)
@mock.patch.object(
    HealthProfileServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(HealthProfileServiceAsyncClient),
)
def test_health_profile_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(HealthProfileServiceClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(HealthProfileServiceClient, "get_transport_class") as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, "__init__") as patched:
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
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                    UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
                ),
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
        with mock.patch.object(transport_class, "__init__") as patched:
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
    assert (
        str(excinfo.value)
        == "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
    )

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
            ),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )
    # Check the case api_endpoint is provided
    options = client_options.ClientOptions(
        api_audience="https://language.googleapis.com"
    )
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
            ),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience="https://language.googleapis.com",
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,use_client_cert_env",
    [
        (
            HealthProfileServiceClient,
            transports.HealthProfileServiceGrpcTransport,
            "grpc",
            "true",
        ),
        (
            HealthProfileServiceAsyncClient,
            transports.HealthProfileServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            HealthProfileServiceClient,
            transports.HealthProfileServiceGrpcTransport,
            "grpc",
            "false",
        ),
        (
            HealthProfileServiceAsyncClient,
            transports.HealthProfileServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (
            HealthProfileServiceClient,
            transports.HealthProfileServiceRestTransport,
            "rest",
            "true",
        ),
        (
            HealthProfileServiceClient,
            transports.HealthProfileServiceRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    HealthProfileServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(HealthProfileServiceClient),
)
@mock.patch.object(
    HealthProfileServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(HealthProfileServiceAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_health_profile_service_client_mtls_env_auto(
    client_class, transport_class, transport_name, use_client_cert_env
):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        options = client_options.ClientOptions(
            client_cert_source=client_cert_source_callback
        )
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client._DEFAULT_ENDPOINT_TEMPLATE.format(
                    UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
                )
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
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=True,
            ):
                with mock.patch(
                    "google.auth.transport.mtls.default_client_cert_source",
                    return_value=client_cert_source_callback,
                ):
                    if use_client_cert_env == "false":
                        expected_host = client._DEFAULT_ENDPOINT_TEMPLATE.format(
                            UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
                        )
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
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=False,
            ):
                patched.return_value = None
                client = client_class(transport=transport_name)
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                        UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
                    ),
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                    api_audience=None,
                )


@pytest.mark.parametrize(
    "client_class", [HealthProfileServiceClient, HealthProfileServiceAsyncClient]
)
@mock.patch.object(
    HealthProfileServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(HealthProfileServiceClient),
)
@mock.patch.object(
    HealthProfileServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(HealthProfileServiceAsyncClient),
)
def test_health_profile_service_client_get_mtls_endpoint_and_cert_source(client_class):
    mock_client_cert_source = mock.Mock()

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "true".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(
            client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint
        )
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
            options
        )
        assert api_endpoint == mock_api_endpoint
        assert cert_source == mock_client_cert_source

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "false".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"}):
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

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "Unsupported".
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}
    ):
        if hasattr(google.auth.transport.mtls, "should_use_client_cert"):
            mock_client_cert_source = mock.Mock()
            mock_api_endpoint = "foo"
            options = client_options.ClientOptions(
                client_cert_source=mock_client_cert_source,
                api_endpoint=mock_api_endpoint,
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
                with (
                    mock.patch("builtins.open", m),
                    mock.patch(
                        "os.path.exists",
                        side_effect=lambda path: os.path.basename(path)
                        == config_filename,
                    ),
                ):
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
                with (
                    mock.patch("builtins.open", m),
                    mock.patch(
                        "os.path.exists",
                        side_effect=lambda path: os.path.basename(path)
                        == config_filename,
                    ),
                ):
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
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=False,
        ):
            api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
            assert api_endpoint == client_class.DEFAULT_ENDPOINT
            assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert exists.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=True,
        ):
            with mock.patch(
                "google.auth.transport.mtls.default_client_cert_source",
                return_value=mock_client_cert_source,
            ):
                api_endpoint, cert_source = (
                    client_class.get_mtls_endpoint_and_cert_source()
                )
                assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
                assert cert_source == mock_client_cert_source

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError) as excinfo:
            client_class.get_mtls_endpoint_and_cert_source()

        assert (
            str(excinfo.value)
            == "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
        )


@pytest.mark.parametrize(
    "client_class", [HealthProfileServiceClient, HealthProfileServiceAsyncClient]
)
@mock.patch.object(
    HealthProfileServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(HealthProfileServiceClient),
)
@mock.patch.object(
    HealthProfileServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(HealthProfileServiceAsyncClient),
)
def test_health_profile_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = HealthProfileServiceClient._DEFAULT_UNIVERSE
    default_endpoint = HealthProfileServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = HealthProfileServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=mock_universe
    )

    # If ClientOptions.api_endpoint is set and GOOGLE_API_USE_CLIENT_CERTIFICATE="true",
    # use ClientOptions.api_endpoint as the api endpoint regardless.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
        ):
            options = client_options.ClientOptions(
                client_cert_source=mock_client_cert_source, api_endpoint=api_override
            )
            client = client_class(
                client_options=options,
                credentials=ga_credentials.AnonymousCredentials(),
            )
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
        client = client_class(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )
    else:
        client = client_class(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )
    assert client.api_endpoint == (
        mock_endpoint if universe_exists else default_endpoint
    )
    assert client.universe_domain == (
        mock_universe if universe_exists else default_universe
    )

    # If ClientOptions does not have a universe domain attribute and GOOGLE_API_USE_MTLS_ENDPOINT="never",
    # use the _DEFAULT_ENDPOINT_TEMPLATE populated with GDU as the api endpoint.
    options = client_options.ClientOptions()
    if hasattr(options, "universe_domain"):
        delattr(options, "universe_domain")
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        client = client_class(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )
        assert client.api_endpoint == default_endpoint


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            HealthProfileServiceClient,
            transports.HealthProfileServiceGrpcTransport,
            "grpc",
        ),
        (
            HealthProfileServiceAsyncClient,
            transports.HealthProfileServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            HealthProfileServiceClient,
            transports.HealthProfileServiceRestTransport,
            "rest",
        ),
    ],
)
def test_health_profile_service_client_client_options_scopes(
    client_class, transport_class, transport_name
):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(
        scopes=["1", "2"],
    )
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
            ),
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,grpc_helpers",
    [
        (
            HealthProfileServiceClient,
            transports.HealthProfileServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            HealthProfileServiceAsyncClient,
            transports.HealthProfileServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (
            HealthProfileServiceClient,
            transports.HealthProfileServiceRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_health_profile_service_client_client_options_credentials_file(
    client_class, transport_class, transport_name, grpc_helpers
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")

    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
            ),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )


def test_health_profile_service_client_client_options_from_dict():
    with mock.patch(
        "google.devicesandservices.health_v4.services.health_profile_service.transports.HealthProfileServiceGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = HealthProfileServiceClient(
            client_options={"api_endpoint": "squid.clam.whelk"}
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


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,grpc_helpers",
    [
        (
            HealthProfileServiceClient,
            transports.HealthProfileServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            HealthProfileServiceAsyncClient,
            transports.HealthProfileServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_health_profile_service_client_create_channel_credentials_file(
    client_class, transport_class, transport_name, grpc_helpers
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")

    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
            ),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

    # test that the credentials from file are saved and used as the credentials.
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch.object(grpc_helpers, "create_channel") as create_channel,
    ):
        creds = ga_credentials.AnonymousCredentials()
        file_creds = ga_credentials.AnonymousCredentials()
        load_creds.return_value = (file_creds, None)
        adc.return_value = (creds, None)
        client = client_class(client_options=options, transport=transport_name)
        create_channel.assert_called_with(
            "health.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
                "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly",
                "https://www.googleapis.com/auth/googlehealth.ecg.readonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.readonly",
                "https://www.googleapis.com/auth/googlehealth.irn.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.readonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.readonly",
                "https://www.googleapis.com/auth/googlehealth.profile.readonly",
                "https://www.googleapis.com/auth/googlehealth.profile.writeonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.readonly",
                "https://www.googleapis.com/auth/googlehealth.settings.readonly",
                "https://www.googleapis.com/auth/googlehealth.settings.writeonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.readonly",
            ),
            scopes=None,
            default_host="health.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetProfileRequest(),
        {},
    ],
)
def test_get_profile(request_type, transport: str = "grpc"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Profile(
            name="name_value",
            age=301,
            user_configured_walking_stride_length_mm=4244,
            user_configured_running_stride_length_mm=4264,
            auto_walking_stride_length_mm=3081,
            auto_running_stride_length_mm=3101,
        )
        response = client.get_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = health_profile.GetProfileRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Profile)
    assert response.name == "name_value"
    assert response.age == 301
    assert response.user_configured_walking_stride_length_mm == 4244
    assert response.user_configured_running_stride_length_mm == 4264
    assert response.auto_walking_stride_length_mm == 3081
    assert response.auto_running_stride_length_mm == 3101


def test_get_profile_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = health_profile.GetProfileRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_profile), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_profile(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetProfileRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_profile_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_profile in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_profile] = mock_rpc
        request = {}
        client.get_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_profile(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_profile_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = HealthProfileServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_profile
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_profile
        ] = mock_rpc

        request = {}
        await client.get_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_profile(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetProfileRequest(),
        {},
    ],
)
async def test_get_profile_async(request_type, transport: str = "grpc_asyncio"):
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Profile(
                name="name_value",
                age=301,
                user_configured_walking_stride_length_mm=4244,
                user_configured_running_stride_length_mm=4264,
                auto_walking_stride_length_mm=3081,
                auto_running_stride_length_mm=3101,
            )
        )
        response = await client.get_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = health_profile.GetProfileRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Profile)
    assert response.name == "name_value"
    assert response.age == 301
    assert response.user_configured_walking_stride_length_mm == 4244
    assert response.user_configured_running_stride_length_mm == 4264
    assert response.auto_walking_stride_length_mm == 3081
    assert response.auto_running_stride_length_mm == 3101


def test_get_profile_field_headers():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.GetProfileRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_profile), "__call__") as call:
        call.return_value = health_profile.Profile()
        client.get_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_profile_field_headers_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.GetProfileRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_profile), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Profile()
        )
        await client.get_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_get_profile_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Profile()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_profile(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_profile_flattened_error():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_profile(
            health_profile.GetProfileRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_profile_flattened_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Profile()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Profile()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_profile(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_profile_flattened_error_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_profile(
            health_profile.GetProfileRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.UpdateProfileRequest(),
        {},
    ],
)
def test_update_profile(request_type, transport: str = "grpc"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Profile(
            name="name_value",
            age=301,
            user_configured_walking_stride_length_mm=4244,
            user_configured_running_stride_length_mm=4264,
            auto_walking_stride_length_mm=3081,
            auto_running_stride_length_mm=3101,
        )
        response = client.update_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = health_profile.UpdateProfileRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Profile)
    assert response.name == "name_value"
    assert response.age == 301
    assert response.user_configured_walking_stride_length_mm == 4244
    assert response.user_configured_running_stride_length_mm == 4264
    assert response.auto_walking_stride_length_mm == 3081
    assert response.auto_running_stride_length_mm == 3101


def test_update_profile_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = health_profile.UpdateProfileRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_profile), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_profile(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.UpdateProfileRequest()
        assert args[0] == request_msg


def test_update_profile_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_profile in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_profile] = mock_rpc
        request = {}
        client.update_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_profile(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_profile_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = HealthProfileServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_profile
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_profile
        ] = mock_rpc

        request = {}
        await client.update_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_profile(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.UpdateProfileRequest(),
        {},
    ],
)
async def test_update_profile_async(request_type, transport: str = "grpc_asyncio"):
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Profile(
                name="name_value",
                age=301,
                user_configured_walking_stride_length_mm=4244,
                user_configured_running_stride_length_mm=4264,
                auto_walking_stride_length_mm=3081,
                auto_running_stride_length_mm=3101,
            )
        )
        response = await client.update_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = health_profile.UpdateProfileRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Profile)
    assert response.name == "name_value"
    assert response.age == 301
    assert response.user_configured_walking_stride_length_mm == 4244
    assert response.user_configured_running_stride_length_mm == 4264
    assert response.auto_walking_stride_length_mm == 3081
    assert response.auto_running_stride_length_mm == 3101


def test_update_profile_field_headers():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.UpdateProfileRequest()

    request.profile.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_profile), "__call__") as call:
        call.return_value = health_profile.Profile()
        client.update_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "profile.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_profile_field_headers_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.UpdateProfileRequest()

    request.profile.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_profile), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Profile()
        )
        await client.update_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "profile.name=name_value",
    ) in kw["metadata"]


def test_update_profile_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Profile()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_profile(
            profile=health_profile.Profile(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].profile
        mock_val = health_profile.Profile(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_profile_flattened_error():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_profile(
            health_profile.UpdateProfileRequest(),
            profile=health_profile.Profile(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_profile_flattened_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Profile()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Profile()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_profile(
            profile=health_profile.Profile(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].profile
        mock_val = health_profile.Profile(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_profile_flattened_error_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_profile(
            health_profile.UpdateProfileRequest(),
            profile=health_profile.Profile(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetSettingsRequest(),
        {},
    ],
)
def test_get_settings(request_type, transport: str = "grpc"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_settings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Settings(
            name="name_value",
            auto_stride_enabled=True,
            distance_unit=health_profile.Settings.DistanceUnit.DISTANCE_UNIT_MILES,
            glucose_unit=health_profile.Settings.GlucoseUnit.GLUCOSE_UNIT_MG_DL,
            height_unit=health_profile.Settings.HeightUnit.HEIGHT_UNIT_INCHES,
            language_locale="language_locale_value",
            stride_length_walking_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
            stride_length_running_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
            swim_unit=health_profile.Settings.SwimUnit.SWIM_UNIT_METERS,
            temperature_unit=health_profile.Settings.TemperatureUnit.TEMPERATURE_UNIT_CELSIUS,
            time_zone="time_zone_value",
            weight_unit=health_profile.Settings.WeightUnit.WEIGHT_UNIT_POUNDS,
            water_unit=health_profile.Settings.WaterUnit.WATER_UNIT_ML,
            food_language_code="food_language_code_value",
        )
        response = client.get_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = health_profile.GetSettingsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Settings)
    assert response.name == "name_value"
    assert response.auto_stride_enabled is True
    assert (
        response.distance_unit
        == health_profile.Settings.DistanceUnit.DISTANCE_UNIT_MILES
    )
    assert (
        response.glucose_unit == health_profile.Settings.GlucoseUnit.GLUCOSE_UNIT_MG_DL
    )
    assert response.height_unit == health_profile.Settings.HeightUnit.HEIGHT_UNIT_INCHES
    assert response.language_locale == "language_locale_value"
    assert (
        response.stride_length_walking_type
        == health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT
    )
    assert (
        response.stride_length_running_type
        == health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT
    )
    assert response.swim_unit == health_profile.Settings.SwimUnit.SWIM_UNIT_METERS
    assert (
        response.temperature_unit
        == health_profile.Settings.TemperatureUnit.TEMPERATURE_UNIT_CELSIUS
    )
    assert response.time_zone == "time_zone_value"
    assert response.weight_unit == health_profile.Settings.WeightUnit.WEIGHT_UNIT_POUNDS
    assert response.water_unit == health_profile.Settings.WaterUnit.WATER_UNIT_ML
    assert response.food_language_code == "food_language_code_value"


def test_get_settings_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = health_profile.GetSettingsRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_settings), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_settings(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetSettingsRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_settings_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_settings in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_settings] = mock_rpc
        request = {}
        client.get_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_settings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_settings_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = HealthProfileServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_settings
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_settings
        ] = mock_rpc

        request = {}
        await client.get_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_settings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetSettingsRequest(),
        {},
    ],
)
async def test_get_settings_async(request_type, transport: str = "grpc_asyncio"):
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_settings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Settings(
                name="name_value",
                auto_stride_enabled=True,
                distance_unit=health_profile.Settings.DistanceUnit.DISTANCE_UNIT_MILES,
                glucose_unit=health_profile.Settings.GlucoseUnit.GLUCOSE_UNIT_MG_DL,
                height_unit=health_profile.Settings.HeightUnit.HEIGHT_UNIT_INCHES,
                language_locale="language_locale_value",
                stride_length_walking_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
                stride_length_running_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
                swim_unit=health_profile.Settings.SwimUnit.SWIM_UNIT_METERS,
                temperature_unit=health_profile.Settings.TemperatureUnit.TEMPERATURE_UNIT_CELSIUS,
                time_zone="time_zone_value",
                weight_unit=health_profile.Settings.WeightUnit.WEIGHT_UNIT_POUNDS,
                water_unit=health_profile.Settings.WaterUnit.WATER_UNIT_ML,
                food_language_code="food_language_code_value",
            )
        )
        response = await client.get_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = health_profile.GetSettingsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Settings)
    assert response.name == "name_value"
    assert response.auto_stride_enabled is True
    assert (
        response.distance_unit
        == health_profile.Settings.DistanceUnit.DISTANCE_UNIT_MILES
    )
    assert (
        response.glucose_unit == health_profile.Settings.GlucoseUnit.GLUCOSE_UNIT_MG_DL
    )
    assert response.height_unit == health_profile.Settings.HeightUnit.HEIGHT_UNIT_INCHES
    assert response.language_locale == "language_locale_value"
    assert (
        response.stride_length_walking_type
        == health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT
    )
    assert (
        response.stride_length_running_type
        == health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT
    )
    assert response.swim_unit == health_profile.Settings.SwimUnit.SWIM_UNIT_METERS
    assert (
        response.temperature_unit
        == health_profile.Settings.TemperatureUnit.TEMPERATURE_UNIT_CELSIUS
    )
    assert response.time_zone == "time_zone_value"
    assert response.weight_unit == health_profile.Settings.WeightUnit.WEIGHT_UNIT_POUNDS
    assert response.water_unit == health_profile.Settings.WaterUnit.WATER_UNIT_ML
    assert response.food_language_code == "food_language_code_value"


def test_get_settings_field_headers():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.GetSettingsRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_settings), "__call__") as call:
        call.return_value = health_profile.Settings()
        client.get_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_settings_field_headers_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.GetSettingsRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_settings), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Settings()
        )
        await client.get_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_get_settings_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_settings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Settings()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_settings(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_settings_flattened_error():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_settings(
            health_profile.GetSettingsRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_settings_flattened_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_settings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Settings()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Settings()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_settings(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_settings_flattened_error_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_settings(
            health_profile.GetSettingsRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.UpdateSettingsRequest(),
        {},
    ],
)
def test_update_settings(request_type, transport: str = "grpc"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_settings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Settings(
            name="name_value",
            auto_stride_enabled=True,
            distance_unit=health_profile.Settings.DistanceUnit.DISTANCE_UNIT_MILES,
            glucose_unit=health_profile.Settings.GlucoseUnit.GLUCOSE_UNIT_MG_DL,
            height_unit=health_profile.Settings.HeightUnit.HEIGHT_UNIT_INCHES,
            language_locale="language_locale_value",
            stride_length_walking_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
            stride_length_running_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
            swim_unit=health_profile.Settings.SwimUnit.SWIM_UNIT_METERS,
            temperature_unit=health_profile.Settings.TemperatureUnit.TEMPERATURE_UNIT_CELSIUS,
            time_zone="time_zone_value",
            weight_unit=health_profile.Settings.WeightUnit.WEIGHT_UNIT_POUNDS,
            water_unit=health_profile.Settings.WaterUnit.WATER_UNIT_ML,
            food_language_code="food_language_code_value",
        )
        response = client.update_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = health_profile.UpdateSettingsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Settings)
    assert response.name == "name_value"
    assert response.auto_stride_enabled is True
    assert (
        response.distance_unit
        == health_profile.Settings.DistanceUnit.DISTANCE_UNIT_MILES
    )
    assert (
        response.glucose_unit == health_profile.Settings.GlucoseUnit.GLUCOSE_UNIT_MG_DL
    )
    assert response.height_unit == health_profile.Settings.HeightUnit.HEIGHT_UNIT_INCHES
    assert response.language_locale == "language_locale_value"
    assert (
        response.stride_length_walking_type
        == health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT
    )
    assert (
        response.stride_length_running_type
        == health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT
    )
    assert response.swim_unit == health_profile.Settings.SwimUnit.SWIM_UNIT_METERS
    assert (
        response.temperature_unit
        == health_profile.Settings.TemperatureUnit.TEMPERATURE_UNIT_CELSIUS
    )
    assert response.time_zone == "time_zone_value"
    assert response.weight_unit == health_profile.Settings.WeightUnit.WEIGHT_UNIT_POUNDS
    assert response.water_unit == health_profile.Settings.WaterUnit.WATER_UNIT_ML
    assert response.food_language_code == "food_language_code_value"


def test_update_settings_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = health_profile.UpdateSettingsRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_settings), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_settings(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.UpdateSettingsRequest()
        assert args[0] == request_msg


def test_update_settings_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_settings in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_settings] = mock_rpc
        request = {}
        client.update_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_settings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_settings_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = HealthProfileServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_settings
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_settings
        ] = mock_rpc

        request = {}
        await client.update_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_settings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.UpdateSettingsRequest(),
        {},
    ],
)
async def test_update_settings_async(request_type, transport: str = "grpc_asyncio"):
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_settings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Settings(
                name="name_value",
                auto_stride_enabled=True,
                distance_unit=health_profile.Settings.DistanceUnit.DISTANCE_UNIT_MILES,
                glucose_unit=health_profile.Settings.GlucoseUnit.GLUCOSE_UNIT_MG_DL,
                height_unit=health_profile.Settings.HeightUnit.HEIGHT_UNIT_INCHES,
                language_locale="language_locale_value",
                stride_length_walking_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
                stride_length_running_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
                swim_unit=health_profile.Settings.SwimUnit.SWIM_UNIT_METERS,
                temperature_unit=health_profile.Settings.TemperatureUnit.TEMPERATURE_UNIT_CELSIUS,
                time_zone="time_zone_value",
                weight_unit=health_profile.Settings.WeightUnit.WEIGHT_UNIT_POUNDS,
                water_unit=health_profile.Settings.WaterUnit.WATER_UNIT_ML,
                food_language_code="food_language_code_value",
            )
        )
        response = await client.update_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = health_profile.UpdateSettingsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Settings)
    assert response.name == "name_value"
    assert response.auto_stride_enabled is True
    assert (
        response.distance_unit
        == health_profile.Settings.DistanceUnit.DISTANCE_UNIT_MILES
    )
    assert (
        response.glucose_unit == health_profile.Settings.GlucoseUnit.GLUCOSE_UNIT_MG_DL
    )
    assert response.height_unit == health_profile.Settings.HeightUnit.HEIGHT_UNIT_INCHES
    assert response.language_locale == "language_locale_value"
    assert (
        response.stride_length_walking_type
        == health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT
    )
    assert (
        response.stride_length_running_type
        == health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT
    )
    assert response.swim_unit == health_profile.Settings.SwimUnit.SWIM_UNIT_METERS
    assert (
        response.temperature_unit
        == health_profile.Settings.TemperatureUnit.TEMPERATURE_UNIT_CELSIUS
    )
    assert response.time_zone == "time_zone_value"
    assert response.weight_unit == health_profile.Settings.WeightUnit.WEIGHT_UNIT_POUNDS
    assert response.water_unit == health_profile.Settings.WaterUnit.WATER_UNIT_ML
    assert response.food_language_code == "food_language_code_value"


def test_update_settings_field_headers():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.UpdateSettingsRequest()

    request.settings.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_settings), "__call__") as call:
        call.return_value = health_profile.Settings()
        client.update_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "settings.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_settings_field_headers_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.UpdateSettingsRequest()

    request.settings.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_settings), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Settings()
        )
        await client.update_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "settings.name=name_value",
    ) in kw["metadata"]


def test_update_settings_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_settings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Settings()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_settings(
            settings=health_profile.Settings(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].settings
        mock_val = health_profile.Settings(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_settings_flattened_error():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_settings(
            health_profile.UpdateSettingsRequest(),
            settings=health_profile.Settings(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_settings_flattened_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_settings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Settings()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Settings()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_settings(
            settings=health_profile.Settings(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].settings
        mock_val = health_profile.Settings(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_settings_flattened_error_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_settings(
            health_profile.UpdateSettingsRequest(),
            settings=health_profile.Settings(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetIdentityRequest(),
        {},
    ],
)
def test_get_identity(request_type, transport: str = "grpc"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_identity), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Identity(
            name="name_value",
            legacy_user_id="legacy_user_id_value",
            health_user_id="health_user_id_value",
        )
        response = client.get_identity(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = health_profile.GetIdentityRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Identity)
    assert response.name == "name_value"
    assert response.legacy_user_id == "legacy_user_id_value"
    assert response.health_user_id == "health_user_id_value"


def test_get_identity_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = health_profile.GetIdentityRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_identity), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_identity(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetIdentityRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_identity_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_identity in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_identity] = mock_rpc
        request = {}
        client.get_identity(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_identity(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_identity_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = HealthProfileServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_identity
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_identity
        ] = mock_rpc

        request = {}
        await client.get_identity(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_identity(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetIdentityRequest(),
        {},
    ],
)
async def test_get_identity_async(request_type, transport: str = "grpc_asyncio"):
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_identity), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Identity(
                name="name_value",
                legacy_user_id="legacy_user_id_value",
                health_user_id="health_user_id_value",
            )
        )
        response = await client.get_identity(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = health_profile.GetIdentityRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Identity)
    assert response.name == "name_value"
    assert response.legacy_user_id == "legacy_user_id_value"
    assert response.health_user_id == "health_user_id_value"


def test_get_identity_field_headers():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.GetIdentityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_identity), "__call__") as call:
        call.return_value = health_profile.Identity()
        client.get_identity(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_identity_field_headers_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.GetIdentityRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_identity), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Identity()
        )
        await client.get_identity(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_get_identity_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_identity), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Identity()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_identity(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_identity_flattened_error():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_identity(
            health_profile.GetIdentityRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_identity_flattened_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_identity), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.Identity()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Identity()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_identity(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_identity_flattened_error_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_identity(
            health_profile.GetIdentityRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetIrnProfileRequest(),
        {},
    ],
)
def test_get_irn_profile(request_type, transport: str = "grpc"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_irn_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.IrnProfile(
            name="name_value",
            onboarding_status=True,
            enrollment_status=True,
        )
        response = client.get_irn_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = health_profile.GetIrnProfileRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.IrnProfile)
    assert response.name == "name_value"
    assert response.onboarding_status is True
    assert response.enrollment_status is True


def test_get_irn_profile_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = health_profile.GetIrnProfileRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_irn_profile), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_irn_profile(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetIrnProfileRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_irn_profile_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_irn_profile in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_irn_profile] = mock_rpc
        request = {}
        client.get_irn_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_irn_profile(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_irn_profile_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = HealthProfileServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_irn_profile
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_irn_profile
        ] = mock_rpc

        request = {}
        await client.get_irn_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_irn_profile(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetIrnProfileRequest(),
        {},
    ],
)
async def test_get_irn_profile_async(request_type, transport: str = "grpc_asyncio"):
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_irn_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.IrnProfile(
                name="name_value",
                onboarding_status=True,
                enrollment_status=True,
            )
        )
        response = await client.get_irn_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = health_profile.GetIrnProfileRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.IrnProfile)
    assert response.name == "name_value"
    assert response.onboarding_status is True
    assert response.enrollment_status is True


def test_get_irn_profile_field_headers():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.GetIrnProfileRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_irn_profile), "__call__") as call:
        call.return_value = health_profile.IrnProfile()
        client.get_irn_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_irn_profile_field_headers_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.GetIrnProfileRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_irn_profile), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.IrnProfile()
        )
        await client.get_irn_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_get_irn_profile_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_irn_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.IrnProfile()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_irn_profile(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_irn_profile_flattened_error():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_irn_profile(
            health_profile.GetIrnProfileRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_irn_profile_flattened_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_irn_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.IrnProfile()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.IrnProfile()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_irn_profile(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_irn_profile_flattened_error_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_irn_profile(
            health_profile.GetIrnProfileRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetPairedDeviceRequest(),
        {},
    ],
)
def test_get_paired_device(request_type, transport: str = "grpc"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_paired_device), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.PairedDevice(
            name="name_value",
            device_type=health_profile.PairedDevice.DeviceType.TRACKER,
            battery_status="battery_status_value",
            battery_level=1394,
            device_version="device_version_value",
            mac_address="mac_address_value",
            features=["features_value"],
        )
        response = client.get_paired_device(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = health_profile.GetPairedDeviceRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.PairedDevice)
    assert response.name == "name_value"
    assert response.device_type == health_profile.PairedDevice.DeviceType.TRACKER
    assert response.battery_status == "battery_status_value"
    assert response.battery_level == 1394
    assert response.device_version == "device_version_value"
    assert response.mac_address == "mac_address_value"
    assert response.features == ["features_value"]


def test_get_paired_device_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = health_profile.GetPairedDeviceRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_paired_device), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_paired_device(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetPairedDeviceRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_paired_device_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_paired_device in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_paired_device] = (
            mock_rpc
        )
        request = {}
        client.get_paired_device(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_paired_device(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_paired_device_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = HealthProfileServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_paired_device
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_paired_device
        ] = mock_rpc

        request = {}
        await client.get_paired_device(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_paired_device(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetPairedDeviceRequest(),
        {},
    ],
)
async def test_get_paired_device_async(request_type, transport: str = "grpc_asyncio"):
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_paired_device), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.PairedDevice(
                name="name_value",
                device_type=health_profile.PairedDevice.DeviceType.TRACKER,
                battery_status="battery_status_value",
                battery_level=1394,
                device_version="device_version_value",
                mac_address="mac_address_value",
                features=["features_value"],
            )
        )
        response = await client.get_paired_device(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = health_profile.GetPairedDeviceRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.PairedDevice)
    assert response.name == "name_value"
    assert response.device_type == health_profile.PairedDevice.DeviceType.TRACKER
    assert response.battery_status == "battery_status_value"
    assert response.battery_level == 1394
    assert response.device_version == "device_version_value"
    assert response.mac_address == "mac_address_value"
    assert response.features == ["features_value"]


def test_get_paired_device_field_headers():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.GetPairedDeviceRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_paired_device), "__call__"
    ) as call:
        call.return_value = health_profile.PairedDevice()
        client.get_paired_device(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_paired_device_field_headers_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.GetPairedDeviceRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_paired_device), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.PairedDevice()
        )
        await client.get_paired_device(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=name_value",
    ) in kw["metadata"]


def test_get_paired_device_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_paired_device), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.PairedDevice()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_paired_device(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_paired_device_flattened_error():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_paired_device(
            health_profile.GetPairedDeviceRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_paired_device_flattened_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_paired_device), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.PairedDevice()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.PairedDevice()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_paired_device(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_paired_device_flattened_error_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_paired_device(
            health_profile.GetPairedDeviceRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.ListPairedDevicesRequest(),
        {},
    ],
)
def test_list_paired_devices(request_type, transport: str = "grpc"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_paired_devices), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.ListPairedDevicesResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_paired_devices(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = health_profile.ListPairedDevicesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListPairedDevicesPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_paired_devices_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = health_profile.ListPairedDevicesRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_paired_devices), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_paired_devices(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.ListPairedDevicesRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_paired_devices_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_paired_devices in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_paired_devices] = (
            mock_rpc
        )
        request = {}
        client.list_paired_devices(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_paired_devices(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_paired_devices_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = HealthProfileServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_paired_devices
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_paired_devices
        ] = mock_rpc

        request = {}
        await client.list_paired_devices(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_paired_devices(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.ListPairedDevicesRequest(),
        {},
    ],
)
async def test_list_paired_devices_async(request_type, transport: str = "grpc_asyncio"):
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_paired_devices), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.ListPairedDevicesResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_paired_devices(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = health_profile.ListPairedDevicesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListPairedDevicesAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_paired_devices_field_headers():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.ListPairedDevicesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_paired_devices), "__call__"
    ) as call:
        call.return_value = health_profile.ListPairedDevicesResponse()
        client.list_paired_devices(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_paired_devices_field_headers_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = health_profile.ListPairedDevicesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_paired_devices), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.ListPairedDevicesResponse()
        )
        await client.list_paired_devices(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "parent=parent_value",
    ) in kw["metadata"]


def test_list_paired_devices_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_paired_devices), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.ListPairedDevicesResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_paired_devices(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_paired_devices_flattened_error():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_paired_devices(
            health_profile.ListPairedDevicesRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_paired_devices_flattened_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_paired_devices), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = health_profile.ListPairedDevicesResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.ListPairedDevicesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_paired_devices(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_paired_devices_flattened_error_async():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_paired_devices(
            health_profile.ListPairedDevicesRequest(),
            parent="parent_value",
        )


def test_list_paired_devices_pager(transport_name: str = "grpc"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_paired_devices), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                ],
                next_page_token="abc",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[],
                next_page_token="def",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                ],
                next_page_token="ghi",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        expected_metadata = tuple(expected_metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", ""),)),
        )
        pager = client.list_paired_devices(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, health_profile.PairedDevice) for i in results)


def test_list_paired_devices_pages(transport_name: str = "grpc"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_paired_devices), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                ],
                next_page_token="abc",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[],
                next_page_token="def",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                ],
                next_page_token="ghi",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_paired_devices(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_paired_devices_async_pager():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_paired_devices),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                ],
                next_page_token="abc",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[],
                next_page_token="def",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                ],
                next_page_token="ghi",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_paired_devices(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, health_profile.PairedDevice) for i in responses)


@pytest.mark.asyncio
async def test_list_paired_devices_async_pages():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_paired_devices),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                ],
                next_page_token="abc",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[],
                next_page_token="def",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                ],
                next_page_token="ghi",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_paired_devices(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_get_profile_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_profile in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_profile] = mock_rpc

        request = {}
        client.get_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_profile(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_profile_rest_required_fields(
    request_type=health_profile.GetProfileRequest,
):
    transport_class = transports.HealthProfileServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetProfile,
        "_BaseGetProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = health_profile.Profile()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = health_profile.Profile.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_profile(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_profile_rest_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.Profile()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "users/sample1/profile"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = health_profile.Profile.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_profile(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v4/{name=users/*/profile}" % client.transport._host, args[1]
        )


def test_get_profile_rest_flattened_error(transport: str = "rest"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_profile(
            health_profile.GetProfileRequest(),
            name="name_value",
        )


def test_update_profile_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_profile in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_profile] = mock_rpc

        request = {}
        client.update_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_profile(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_profile_rest_required_fields(
    request_type=health_profile.UpdateProfileRequest,
):
    transport_class = transports.HealthProfileServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateProfile,
        "_BaseUpdateProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("updateMask",))

    # verify required fields with non-default values are left alone

    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = health_profile.Profile()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "patch",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = health_profile.Profile.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_profile(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_profile_rest_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.Profile()

        # get arguments that satisfy an http rule for this method
        sample_request = {"profile": {"name": "users/sample1/profile"}}

        # get truthy value for each flattened field
        mock_args = dict(
            profile=health_profile.Profile(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = health_profile.Profile.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_profile(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v4/{profile.name=users/*/profile}" % client.transport._host, args[1]
        )


def test_update_profile_rest_flattened_error(transport: str = "rest"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_profile(
            health_profile.UpdateProfileRequest(),
            profile=health_profile.Profile(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_get_settings_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_settings in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_settings] = mock_rpc

        request = {}
        client.get_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_settings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_settings_rest_required_fields(
    request_type=health_profile.GetSettingsRequest,
):
    transport_class = transports.HealthProfileServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetSettings,
        "_BaseGetSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = health_profile.Settings()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = health_profile.Settings.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_settings(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_settings_rest_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.Settings()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "users/sample1/settings"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = health_profile.Settings.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_settings(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v4/{name=users/*/settings}" % client.transport._host, args[1]
        )


def test_get_settings_rest_flattened_error(transport: str = "rest"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_settings(
            health_profile.GetSettingsRequest(),
            name="name_value",
        )


def test_update_settings_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_settings in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_settings] = mock_rpc

        request = {}
        client.update_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_settings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_settings_rest_required_fields(
    request_type=health_profile.UpdateSettingsRequest,
):
    transport_class = transports.HealthProfileServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateSettings,
        "_BaseUpdateSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("updateMask",))

    # verify required fields with non-default values are left alone

    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = health_profile.Settings()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "patch",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = health_profile.Settings.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_settings(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_settings_rest_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.Settings()

        # get arguments that satisfy an http rule for this method
        sample_request = {"settings": {"name": "users/sample1/settings"}}

        # get truthy value for each flattened field
        mock_args = dict(
            settings=health_profile.Settings(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = health_profile.Settings.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_settings(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v4/{settings.name=users/*/settings}" % client.transport._host, args[1]
        )


def test_update_settings_rest_flattened_error(transport: str = "rest"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_settings(
            health_profile.UpdateSettingsRequest(),
            settings=health_profile.Settings(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_get_identity_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_identity in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_identity] = mock_rpc

        request = {}
        client.get_identity(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_identity(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_identity_rest_required_fields(
    request_type=health_profile.GetIdentityRequest,
):
    transport_class = transports.HealthProfileServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetIdentity,
        "_BaseGetIdentity__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = health_profile.Identity()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = health_profile.Identity.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_identity(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_identity_rest_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.Identity()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "users/sample1/identity"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = health_profile.Identity.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_identity(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v4/{name=users/*/identity}" % client.transport._host, args[1]
        )


def test_get_identity_rest_flattened_error(transport: str = "rest"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_identity(
            health_profile.GetIdentityRequest(),
            name="name_value",
        )


def test_get_irn_profile_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_irn_profile in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_irn_profile] = mock_rpc

        request = {}
        client.get_irn_profile(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_irn_profile(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_irn_profile_rest_required_fields(
    request_type=health_profile.GetIrnProfileRequest,
):
    transport_class = transports.HealthProfileServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetIrnProfile,
        "_BaseGetIrnProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = health_profile.IrnProfile()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = health_profile.IrnProfile.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_irn_profile(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_irn_profile_rest_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.IrnProfile()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "users/sample1/irnProfile"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = health_profile.IrnProfile.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_irn_profile(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v4/{name=users/*/irnProfile}" % client.transport._host, args[1]
        )


def test_get_irn_profile_rest_flattened_error(transport: str = "rest"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_irn_profile(
            health_profile.GetIrnProfileRequest(),
            name="name_value",
        )


def test_get_paired_device_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_paired_device in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_paired_device] = (
            mock_rpc
        )

        request = {}
        client.get_paired_device(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_paired_device(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_paired_device_rest_required_fields(
    request_type=health_profile.GetPairedDeviceRequest,
):
    transport_class = transports.HealthProfileServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetPairedDevice,
        "_BaseGetPairedDevice__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = health_profile.PairedDevice()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = health_profile.PairedDevice.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_paired_device(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_paired_device_rest_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.PairedDevice()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "users/sample1/pairedDevices/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = health_profile.PairedDevice.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_paired_device(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v4/{name=users/*/pairedDevices/*}" % client.transport._host, args[1]
        )


def test_get_paired_device_rest_flattened_error(transport: str = "rest"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_paired_device(
            health_profile.GetPairedDeviceRequest(),
            name="name_value",
        )


def test_list_paired_devices_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_paired_devices in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_paired_devices] = (
            mock_rpc
        )

        request = {}
        client.list_paired_devices(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_paired_devices(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_paired_devices_rest_required_fields(
    request_type=health_profile.ListPairedDevicesRequest,
):
    transport_class = transports.HealthProfileServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListPairedDevices,
        "_BaseListPairedDevices__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "pageSize",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = health_profile.ListPairedDevicesResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = health_profile.ListPairedDevicesResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_paired_devices(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_paired_devices_rest_flattened():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.ListPairedDevicesResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "users/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = health_profile.ListPairedDevicesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_paired_devices(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v4/{parent=users/*}/pairedDevices" % client.transport._host, args[1]
        )


def test_list_paired_devices_rest_flattened_error(transport: str = "rest"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_paired_devices(
            health_profile.ListPairedDevicesRequest(),
            parent="parent_value",
        )


def test_list_paired_devices_rest_pager(transport: str = "rest"):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                ],
                next_page_token="abc",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[],
                next_page_token="def",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                ],
                next_page_token="ghi",
            ),
            health_profile.ListPairedDevicesResponse(
                paired_devices=[
                    health_profile.PairedDevice(),
                    health_profile.PairedDevice(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            health_profile.ListPairedDevicesResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "users/sample1"}

        pager = client.list_paired_devices(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, health_profile.PairedDevice) for i in results)

        pages = list(client.list_paired_devices(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.HealthProfileServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.HealthProfileServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = HealthProfileServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.HealthProfileServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = HealthProfileServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = HealthProfileServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.HealthProfileServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = HealthProfileServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.HealthProfileServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = HealthProfileServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.HealthProfileServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.HealthProfileServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.HealthProfileServiceGrpcTransport,
        transports.HealthProfileServiceGrpcAsyncIOTransport,
        transports.HealthProfileServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = HealthProfileServiceClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_profile_empty_call_grpc():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_profile), "__call__") as call:
        call.return_value = health_profile.Profile()
        client.get_profile(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetProfileRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_profile_empty_call_grpc():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_profile), "__call__") as call:
        call.return_value = health_profile.Profile()
        client.update_profile(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.UpdateProfileRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_settings_empty_call_grpc():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_settings), "__call__") as call:
        call.return_value = health_profile.Settings()
        client.get_settings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetSettingsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_settings_empty_call_grpc():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_settings), "__call__") as call:
        call.return_value = health_profile.Settings()
        client.update_settings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.UpdateSettingsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_identity_empty_call_grpc():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_identity), "__call__") as call:
        call.return_value = health_profile.Identity()
        client.get_identity(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetIdentityRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_irn_profile_empty_call_grpc():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_irn_profile), "__call__") as call:
        call.return_value = health_profile.IrnProfile()
        client.get_irn_profile(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetIrnProfileRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_paired_device_empty_call_grpc():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_paired_device), "__call__"
    ) as call:
        call.return_value = health_profile.PairedDevice()
        client.get_paired_device(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetPairedDeviceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_paired_devices_empty_call_grpc():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_paired_devices), "__call__"
    ) as call:
        call.return_value = health_profile.ListPairedDevicesResponse()
        client.list_paired_devices(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.ListPairedDevicesRequest()
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = HealthProfileServiceAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_profile_empty_call_grpc_asyncio():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Profile(
                name="name_value",
                age=301,
                user_configured_walking_stride_length_mm=4244,
                user_configured_running_stride_length_mm=4264,
                auto_walking_stride_length_mm=3081,
                auto_running_stride_length_mm=3101,
            )
        )
        await client.get_profile(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetProfileRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_profile_empty_call_grpc_asyncio():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Profile(
                name="name_value",
                age=301,
                user_configured_walking_stride_length_mm=4244,
                user_configured_running_stride_length_mm=4264,
                auto_walking_stride_length_mm=3081,
                auto_running_stride_length_mm=3101,
            )
        )
        await client.update_profile(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.UpdateProfileRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_settings_empty_call_grpc_asyncio():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_settings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Settings(
                name="name_value",
                auto_stride_enabled=True,
                distance_unit=health_profile.Settings.DistanceUnit.DISTANCE_UNIT_MILES,
                glucose_unit=health_profile.Settings.GlucoseUnit.GLUCOSE_UNIT_MG_DL,
                height_unit=health_profile.Settings.HeightUnit.HEIGHT_UNIT_INCHES,
                language_locale="language_locale_value",
                stride_length_walking_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
                stride_length_running_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
                swim_unit=health_profile.Settings.SwimUnit.SWIM_UNIT_METERS,
                temperature_unit=health_profile.Settings.TemperatureUnit.TEMPERATURE_UNIT_CELSIUS,
                time_zone="time_zone_value",
                weight_unit=health_profile.Settings.WeightUnit.WEIGHT_UNIT_POUNDS,
                water_unit=health_profile.Settings.WaterUnit.WATER_UNIT_ML,
                food_language_code="food_language_code_value",
            )
        )
        await client.get_settings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetSettingsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_settings_empty_call_grpc_asyncio():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_settings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Settings(
                name="name_value",
                auto_stride_enabled=True,
                distance_unit=health_profile.Settings.DistanceUnit.DISTANCE_UNIT_MILES,
                glucose_unit=health_profile.Settings.GlucoseUnit.GLUCOSE_UNIT_MG_DL,
                height_unit=health_profile.Settings.HeightUnit.HEIGHT_UNIT_INCHES,
                language_locale="language_locale_value",
                stride_length_walking_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
                stride_length_running_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
                swim_unit=health_profile.Settings.SwimUnit.SWIM_UNIT_METERS,
                temperature_unit=health_profile.Settings.TemperatureUnit.TEMPERATURE_UNIT_CELSIUS,
                time_zone="time_zone_value",
                weight_unit=health_profile.Settings.WeightUnit.WEIGHT_UNIT_POUNDS,
                water_unit=health_profile.Settings.WaterUnit.WATER_UNIT_ML,
                food_language_code="food_language_code_value",
            )
        )
        await client.update_settings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.UpdateSettingsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_identity_empty_call_grpc_asyncio():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_identity), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.Identity(
                name="name_value",
                legacy_user_id="legacy_user_id_value",
                health_user_id="health_user_id_value",
            )
        )
        await client.get_identity(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetIdentityRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_irn_profile_empty_call_grpc_asyncio():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_irn_profile), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.IrnProfile(
                name="name_value",
                onboarding_status=True,
                enrollment_status=True,
            )
        )
        await client.get_irn_profile(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetIrnProfileRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_paired_device_empty_call_grpc_asyncio():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_paired_device), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.PairedDevice(
                name="name_value",
                device_type=health_profile.PairedDevice.DeviceType.TRACKER,
                battery_status="battery_status_value",
                battery_level=1394,
                device_version="device_version_value",
                mac_address="mac_address_value",
                features=["features_value"],
            )
        )
        await client.get_paired_device(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetPairedDeviceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_paired_devices_empty_call_grpc_asyncio():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_paired_devices), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            health_profile.ListPairedDevicesResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_paired_devices(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.ListPairedDevicesRequest()
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = HealthProfileServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_get_profile_rest_bad_request(request_type=health_profile.GetProfileRequest):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "users/sample1/profile"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_profile(request)


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetProfileRequest,
        dict,
    ],
)
def test_get_profile_rest_call_success(request_type):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "users/sample1/profile"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.Profile(
            name="name_value",
            age=301,
            user_configured_walking_stride_length_mm=4244,
            user_configured_running_stride_length_mm=4264,
            auto_walking_stride_length_mm=3081,
            auto_running_stride_length_mm=3101,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = health_profile.Profile.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_profile(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Profile)
    assert response.name == "name_value"
    assert response.age == 301
    assert response.user_configured_walking_stride_length_mm == 4244
    assert response.user_configured_running_stride_length_mm == 4264
    assert response.auto_walking_stride_length_mm == 3081
    assert response.auto_running_stride_length_mm == 3101


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_profile_rest_interceptors(null_interceptor):
    transport = transports.HealthProfileServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.HealthProfileServiceRestInterceptor(),
    )
    client = HealthProfileServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "post_get_profile"
        ) as post,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor,
            "post_get_profile_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "pre_get_profile"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = health_profile.GetProfileRequest.pb(
            health_profile.GetProfileRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = health_profile.Profile.to_json(health_profile.Profile())
        req.return_value.content = return_value

        request = health_profile.GetProfileRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = health_profile.Profile()
        post_with_metadata.return_value = health_profile.Profile(), metadata

        client.get_profile(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_profile_rest_bad_request(
    request_type=health_profile.UpdateProfileRequest,
):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"profile": {"name": "users/sample1/profile"}}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.update_profile(request)


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.UpdateProfileRequest,
        dict,
    ],
)
def test_update_profile_rest_call_success(request_type):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"profile": {"name": "users/sample1/profile"}}
    request_init["profile"] = {
        "name": "users/sample1/profile",
        "age": 301,
        "membership_start_date": {"year": 433, "month": 550, "day": 318},
        "user_configured_walking_stride_length_mm": 4244,
        "user_configured_running_stride_length_mm": 4264,
        "auto_walking_stride_length_mm": 3081,
        "auto_running_stride_length_mm": 3101,
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = health_profile.UpdateProfileRequest.meta.fields["profile"]

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
            else:  # pragma: NO COVER
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
    for field, value in request_init["profile"].items():  # pragma: NO COVER
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
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(0, len(request_init["profile"][field])):
                    del request_init["profile"][field][i][subfield]
            else:
                del request_init["profile"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.Profile(
            name="name_value",
            age=301,
            user_configured_walking_stride_length_mm=4244,
            user_configured_running_stride_length_mm=4264,
            auto_walking_stride_length_mm=3081,
            auto_running_stride_length_mm=3101,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = health_profile.Profile.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_profile(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Profile)
    assert response.name == "name_value"
    assert response.age == 301
    assert response.user_configured_walking_stride_length_mm == 4244
    assert response.user_configured_running_stride_length_mm == 4264
    assert response.auto_walking_stride_length_mm == 3081
    assert response.auto_running_stride_length_mm == 3101


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_profile_rest_interceptors(null_interceptor):
    transport = transports.HealthProfileServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.HealthProfileServiceRestInterceptor(),
    )
    client = HealthProfileServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "post_update_profile"
        ) as post,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor,
            "post_update_profile_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "pre_update_profile"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = health_profile.UpdateProfileRequest.pb(
            health_profile.UpdateProfileRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = health_profile.Profile.to_json(health_profile.Profile())
        req.return_value.content = return_value

        request = health_profile.UpdateProfileRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = health_profile.Profile()
        post_with_metadata.return_value = health_profile.Profile(), metadata

        client.update_profile(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_settings_rest_bad_request(request_type=health_profile.GetSettingsRequest):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "users/sample1/settings"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_settings(request)


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetSettingsRequest,
        dict,
    ],
)
def test_get_settings_rest_call_success(request_type):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "users/sample1/settings"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.Settings(
            name="name_value",
            auto_stride_enabled=True,
            distance_unit=health_profile.Settings.DistanceUnit.DISTANCE_UNIT_MILES,
            glucose_unit=health_profile.Settings.GlucoseUnit.GLUCOSE_UNIT_MG_DL,
            height_unit=health_profile.Settings.HeightUnit.HEIGHT_UNIT_INCHES,
            language_locale="language_locale_value",
            stride_length_walking_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
            stride_length_running_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
            swim_unit=health_profile.Settings.SwimUnit.SWIM_UNIT_METERS,
            temperature_unit=health_profile.Settings.TemperatureUnit.TEMPERATURE_UNIT_CELSIUS,
            time_zone="time_zone_value",
            weight_unit=health_profile.Settings.WeightUnit.WEIGHT_UNIT_POUNDS,
            water_unit=health_profile.Settings.WaterUnit.WATER_UNIT_ML,
            food_language_code="food_language_code_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = health_profile.Settings.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_settings(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Settings)
    assert response.name == "name_value"
    assert response.auto_stride_enabled is True
    assert (
        response.distance_unit
        == health_profile.Settings.DistanceUnit.DISTANCE_UNIT_MILES
    )
    assert (
        response.glucose_unit == health_profile.Settings.GlucoseUnit.GLUCOSE_UNIT_MG_DL
    )
    assert response.height_unit == health_profile.Settings.HeightUnit.HEIGHT_UNIT_INCHES
    assert response.language_locale == "language_locale_value"
    assert (
        response.stride_length_walking_type
        == health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT
    )
    assert (
        response.stride_length_running_type
        == health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT
    )
    assert response.swim_unit == health_profile.Settings.SwimUnit.SWIM_UNIT_METERS
    assert (
        response.temperature_unit
        == health_profile.Settings.TemperatureUnit.TEMPERATURE_UNIT_CELSIUS
    )
    assert response.time_zone == "time_zone_value"
    assert response.weight_unit == health_profile.Settings.WeightUnit.WEIGHT_UNIT_POUNDS
    assert response.water_unit == health_profile.Settings.WaterUnit.WATER_UNIT_ML
    assert response.food_language_code == "food_language_code_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_settings_rest_interceptors(null_interceptor):
    transport = transports.HealthProfileServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.HealthProfileServiceRestInterceptor(),
    )
    client = HealthProfileServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "post_get_settings"
        ) as post,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor,
            "post_get_settings_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "pre_get_settings"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = health_profile.GetSettingsRequest.pb(
            health_profile.GetSettingsRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = health_profile.Settings.to_json(health_profile.Settings())
        req.return_value.content = return_value

        request = health_profile.GetSettingsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = health_profile.Settings()
        post_with_metadata.return_value = health_profile.Settings(), metadata

        client.get_settings(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_settings_rest_bad_request(
    request_type=health_profile.UpdateSettingsRequest,
):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"settings": {"name": "users/sample1/settings"}}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.update_settings(request)


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.UpdateSettingsRequest,
        dict,
    ],
)
def test_update_settings_rest_call_success(request_type):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"settings": {"name": "users/sample1/settings"}}
    request_init["settings"] = {
        "name": "users/sample1/settings",
        "auto_stride_enabled": True,
        "distance_unit": 1,
        "glucose_unit": 1,
        "height_unit": 1,
        "language_locale": "language_locale_value",
        "utc_offset": {"seconds": 751, "nanos": 543},
        "stride_length_walking_type": 1,
        "stride_length_running_type": 1,
        "swim_unit": 1,
        "temperature_unit": 1,
        "time_zone": "time_zone_value",
        "weight_unit": 1,
        "water_unit": 1,
        "food_language_code": "food_language_code_value",
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = health_profile.UpdateSettingsRequest.meta.fields["settings"]

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
            else:  # pragma: NO COVER
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
    for field, value in request_init["settings"].items():  # pragma: NO COVER
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
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(0, len(request_init["settings"][field])):
                    del request_init["settings"][field][i][subfield]
            else:
                del request_init["settings"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.Settings(
            name="name_value",
            auto_stride_enabled=True,
            distance_unit=health_profile.Settings.DistanceUnit.DISTANCE_UNIT_MILES,
            glucose_unit=health_profile.Settings.GlucoseUnit.GLUCOSE_UNIT_MG_DL,
            height_unit=health_profile.Settings.HeightUnit.HEIGHT_UNIT_INCHES,
            language_locale="language_locale_value",
            stride_length_walking_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
            stride_length_running_type=health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT,
            swim_unit=health_profile.Settings.SwimUnit.SWIM_UNIT_METERS,
            temperature_unit=health_profile.Settings.TemperatureUnit.TEMPERATURE_UNIT_CELSIUS,
            time_zone="time_zone_value",
            weight_unit=health_profile.Settings.WeightUnit.WEIGHT_UNIT_POUNDS,
            water_unit=health_profile.Settings.WaterUnit.WATER_UNIT_ML,
            food_language_code="food_language_code_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = health_profile.Settings.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_settings(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Settings)
    assert response.name == "name_value"
    assert response.auto_stride_enabled is True
    assert (
        response.distance_unit
        == health_profile.Settings.DistanceUnit.DISTANCE_UNIT_MILES
    )
    assert (
        response.glucose_unit == health_profile.Settings.GlucoseUnit.GLUCOSE_UNIT_MG_DL
    )
    assert response.height_unit == health_profile.Settings.HeightUnit.HEIGHT_UNIT_INCHES
    assert response.language_locale == "language_locale_value"
    assert (
        response.stride_length_walking_type
        == health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT
    )
    assert (
        response.stride_length_running_type
        == health_profile.Settings.StrideLengthType.STRIDE_LENGTH_TYPE_DEFAULT
    )
    assert response.swim_unit == health_profile.Settings.SwimUnit.SWIM_UNIT_METERS
    assert (
        response.temperature_unit
        == health_profile.Settings.TemperatureUnit.TEMPERATURE_UNIT_CELSIUS
    )
    assert response.time_zone == "time_zone_value"
    assert response.weight_unit == health_profile.Settings.WeightUnit.WEIGHT_UNIT_POUNDS
    assert response.water_unit == health_profile.Settings.WaterUnit.WATER_UNIT_ML
    assert response.food_language_code == "food_language_code_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_settings_rest_interceptors(null_interceptor):
    transport = transports.HealthProfileServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.HealthProfileServiceRestInterceptor(),
    )
    client = HealthProfileServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "post_update_settings"
        ) as post,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor,
            "post_update_settings_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "pre_update_settings"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = health_profile.UpdateSettingsRequest.pb(
            health_profile.UpdateSettingsRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = health_profile.Settings.to_json(health_profile.Settings())
        req.return_value.content = return_value

        request = health_profile.UpdateSettingsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = health_profile.Settings()
        post_with_metadata.return_value = health_profile.Settings(), metadata

        client.update_settings(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_identity_rest_bad_request(request_type=health_profile.GetIdentityRequest):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "users/sample1/identity"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_identity(request)


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetIdentityRequest,
        dict,
    ],
)
def test_get_identity_rest_call_success(request_type):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "users/sample1/identity"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.Identity(
            name="name_value",
            legacy_user_id="legacy_user_id_value",
            health_user_id="health_user_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = health_profile.Identity.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_identity(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.Identity)
    assert response.name == "name_value"
    assert response.legacy_user_id == "legacy_user_id_value"
    assert response.health_user_id == "health_user_id_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_identity_rest_interceptors(null_interceptor):
    transport = transports.HealthProfileServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.HealthProfileServiceRestInterceptor(),
    )
    client = HealthProfileServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "post_get_identity"
        ) as post,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor,
            "post_get_identity_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "pre_get_identity"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = health_profile.GetIdentityRequest.pb(
            health_profile.GetIdentityRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = health_profile.Identity.to_json(health_profile.Identity())
        req.return_value.content = return_value

        request = health_profile.GetIdentityRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = health_profile.Identity()
        post_with_metadata.return_value = health_profile.Identity(), metadata

        client.get_identity(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_irn_profile_rest_bad_request(
    request_type=health_profile.GetIrnProfileRequest,
):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "users/sample1/irnProfile"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_irn_profile(request)


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetIrnProfileRequest,
        dict,
    ],
)
def test_get_irn_profile_rest_call_success(request_type):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "users/sample1/irnProfile"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.IrnProfile(
            name="name_value",
            onboarding_status=True,
            enrollment_status=True,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = health_profile.IrnProfile.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_irn_profile(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.IrnProfile)
    assert response.name == "name_value"
    assert response.onboarding_status is True
    assert response.enrollment_status is True


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_irn_profile_rest_interceptors(null_interceptor):
    transport = transports.HealthProfileServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.HealthProfileServiceRestInterceptor(),
    )
    client = HealthProfileServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "post_get_irn_profile"
        ) as post,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor,
            "post_get_irn_profile_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "pre_get_irn_profile"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = health_profile.GetIrnProfileRequest.pb(
            health_profile.GetIrnProfileRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = health_profile.IrnProfile.to_json(health_profile.IrnProfile())
        req.return_value.content = return_value

        request = health_profile.GetIrnProfileRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = health_profile.IrnProfile()
        post_with_metadata.return_value = health_profile.IrnProfile(), metadata

        client.get_irn_profile(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_paired_device_rest_bad_request(
    request_type=health_profile.GetPairedDeviceRequest,
):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "users/sample1/pairedDevices/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_paired_device(request)


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.GetPairedDeviceRequest,
        dict,
    ],
)
def test_get_paired_device_rest_call_success(request_type):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "users/sample1/pairedDevices/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.PairedDevice(
            name="name_value",
            device_type=health_profile.PairedDevice.DeviceType.TRACKER,
            battery_status="battery_status_value",
            battery_level=1394,
            device_version="device_version_value",
            mac_address="mac_address_value",
            features=["features_value"],
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = health_profile.PairedDevice.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_paired_device(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, health_profile.PairedDevice)
    assert response.name == "name_value"
    assert response.device_type == health_profile.PairedDevice.DeviceType.TRACKER
    assert response.battery_status == "battery_status_value"
    assert response.battery_level == 1394
    assert response.device_version == "device_version_value"
    assert response.mac_address == "mac_address_value"
    assert response.features == ["features_value"]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_paired_device_rest_interceptors(null_interceptor):
    transport = transports.HealthProfileServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.HealthProfileServiceRestInterceptor(),
    )
    client = HealthProfileServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "post_get_paired_device"
        ) as post,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor,
            "post_get_paired_device_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "pre_get_paired_device"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = health_profile.GetPairedDeviceRequest.pb(
            health_profile.GetPairedDeviceRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = health_profile.PairedDevice.to_json(
            health_profile.PairedDevice()
        )
        req.return_value.content = return_value

        request = health_profile.GetPairedDeviceRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = health_profile.PairedDevice()
        post_with_metadata.return_value = health_profile.PairedDevice(), metadata

        client.get_paired_device(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_paired_devices_rest_bad_request(
    request_type=health_profile.ListPairedDevicesRequest,
):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "users/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list_paired_devices(request)


@pytest.mark.parametrize(
    "request_type",
    [
        health_profile.ListPairedDevicesRequest,
        dict,
    ],
)
def test_list_paired_devices_rest_call_success(request_type):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "users/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = health_profile.ListPairedDevicesResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = health_profile.ListPairedDevicesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_paired_devices(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListPairedDevicesPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_paired_devices_rest_interceptors(null_interceptor):
    transport = transports.HealthProfileServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.HealthProfileServiceRestInterceptor(),
    )
    client = HealthProfileServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "post_list_paired_devices"
        ) as post,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor,
            "post_list_paired_devices_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.HealthProfileServiceRestInterceptor, "pre_list_paired_devices"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = health_profile.ListPairedDevicesRequest.pb(
            health_profile.ListPairedDevicesRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = health_profile.ListPairedDevicesResponse.to_json(
            health_profile.ListPairedDevicesResponse()
        )
        req.return_value.content = return_value

        request = health_profile.ListPairedDevicesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = health_profile.ListPairedDevicesResponse()
        post_with_metadata.return_value = (
            health_profile.ListPairedDevicesResponse(),
            metadata,
        )

        client.list_paired_devices(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_initialize_client_w_rest():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_profile_empty_call_rest():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_profile), "__call__") as call:
        client.get_profile(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetProfileRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_profile_empty_call_rest():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_profile), "__call__") as call:
        client.update_profile(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.UpdateProfileRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_settings_empty_call_rest():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_settings), "__call__") as call:
        client.get_settings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetSettingsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_settings_empty_call_rest():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_settings), "__call__") as call:
        client.update_settings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.UpdateSettingsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_identity_empty_call_rest():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_identity), "__call__") as call:
        client.get_identity(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetIdentityRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_irn_profile_empty_call_rest():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_irn_profile), "__call__") as call:
        client.get_irn_profile(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetIrnProfileRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_paired_device_empty_call_rest():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_paired_device), "__call__"
    ) as call:
        client.get_paired_device(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.GetPairedDeviceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_paired_devices_empty_call_rest():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_paired_devices), "__call__"
    ) as call:
        client.list_paired_devices(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = health_profile.ListPairedDevicesRequest()
        assert args[0] == request_msg


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.HealthProfileServiceGrpcTransport,
    )


def test_health_profile_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.HealthProfileServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_health_profile_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.devicesandservices.health_v4.services.health_profile_service.transports.HealthProfileServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.HealthProfileServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "get_profile",
        "update_profile",
        "get_settings",
        "update_settings",
        "get_identity",
        "get_irn_profile",
        "get_paired_device",
        "list_paired_devices",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()

    # Catch all for all remaining methods and properties
    remainder = [
        "kind",
    ]
    for r in remainder:
        with pytest.raises(NotImplementedError):
            getattr(transport, r)()


def test_health_profile_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.devicesandservices.health_v4.services.health_profile_service.transports.HealthProfileServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.HealthProfileServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly",
                "https://www.googleapis.com/auth/googlehealth.ecg.readonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.readonly",
                "https://www.googleapis.com/auth/googlehealth.irn.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.readonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.readonly",
                "https://www.googleapis.com/auth/googlehealth.profile.readonly",
                "https://www.googleapis.com/auth/googlehealth.profile.writeonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.readonly",
                "https://www.googleapis.com/auth/googlehealth.settings.readonly",
                "https://www.googleapis.com/auth/googlehealth.settings.writeonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.readonly",
            ),
            quota_project_id="octopus",
        )


def test_health_profile_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.devicesandservices.health_v4.services.health_profile_service.transports.HealthProfileServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.HealthProfileServiceTransport()
        adc.assert_called_once()


def test_health_profile_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        HealthProfileServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly",
                "https://www.googleapis.com/auth/googlehealth.ecg.readonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.readonly",
                "https://www.googleapis.com/auth/googlehealth.irn.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.readonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.readonly",
                "https://www.googleapis.com/auth/googlehealth.profile.readonly",
                "https://www.googleapis.com/auth/googlehealth.profile.writeonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.readonly",
                "https://www.googleapis.com/auth/googlehealth.settings.readonly",
                "https://www.googleapis.com/auth/googlehealth.settings.writeonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.readonly",
            ),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.HealthProfileServiceGrpcTransport,
        transports.HealthProfileServiceGrpcAsyncIOTransport,
    ],
)
def test_health_profile_service_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(
                "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly",
                "https://www.googleapis.com/auth/googlehealth.ecg.readonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.readonly",
                "https://www.googleapis.com/auth/googlehealth.irn.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.readonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.readonly",
                "https://www.googleapis.com/auth/googlehealth.profile.readonly",
                "https://www.googleapis.com/auth/googlehealth.profile.writeonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.readonly",
                "https://www.googleapis.com/auth/googlehealth.settings.readonly",
                "https://www.googleapis.com/auth/googlehealth.settings.writeonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.readonly",
            ),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.HealthProfileServiceGrpcTransport,
        transports.HealthProfileServiceGrpcAsyncIOTransport,
        transports.HealthProfileServiceRestTransport,
    ],
)
def test_health_profile_service_transport_auth_gdch_credentials(transport_class):
    host = "https://language.com"
    api_audience_tests = [None, "https://language2.com"]
    api_audience_expect = [host, "https://language2.com"]
    for t, e in zip(api_audience_tests, api_audience_expect):
        with mock.patch.object(google.auth, "default", autospec=True) as adc:
            gdch_mock = mock.MagicMock()
            type(gdch_mock).with_gdch_audience = mock.PropertyMock(
                return_value=gdch_mock
            )
            adc.return_value = (gdch_mock, None)
            transport_class(host=host, api_audience=t)
            gdch_mock.with_gdch_audience.assert_called_once_with(e)


@pytest.mark.parametrize(
    "transport_class,grpc_helpers",
    [
        (transports.HealthProfileServiceGrpcTransport, grpc_helpers),
        (transports.HealthProfileServiceGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_health_profile_service_transport_create_channel(transport_class, grpc_helpers):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch.object(
            grpc_helpers, "create_channel", autospec=True
        ) as create_channel,
    ):
        creds = ga_credentials.AnonymousCredentials()
        adc.return_value = (creds, None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])

        create_channel.assert_called_with(
            "health.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
                "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly",
                "https://www.googleapis.com/auth/googlehealth.ecg.readonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.readonly",
                "https://www.googleapis.com/auth/googlehealth.irn.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.readonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.readonly",
                "https://www.googleapis.com/auth/googlehealth.profile.readonly",
                "https://www.googleapis.com/auth/googlehealth.profile.writeonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.readonly",
                "https://www.googleapis.com/auth/googlehealth.settings.readonly",
                "https://www.googleapis.com/auth/googlehealth.settings.writeonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.readonly",
            ),
            scopes=["1", "2"],
            default_host="health.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.HealthProfileServiceGrpcTransport,
        transports.HealthProfileServiceGrpcAsyncIOTransport,
    ],
)
def test_health_profile_service_grpc_transport_client_cert_source_for_mtls(
    transport_class,
):
    cred = ga_credentials.AnonymousCredentials()

    # Check ssl_channel_credentials is used if provided.
    with mock.patch.object(transport_class, "create_channel") as mock_create_channel:
        mock_ssl_channel_creds = mock.Mock()
        transport_class(
            host="squid.clam.whelk",
            credentials=cred,
            ssl_channel_credentials=mock_ssl_channel_creds,
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
                client_cert_source_for_mtls=client_cert_source_callback,
            )
            expected_cert, expected_key = client_cert_source_callback()
            mock_ssl_cred.assert_called_once_with(
                certificate_chain=expected_cert, private_key=expected_key
            )


def test_health_profile_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.HealthProfileServiceRestTransport(
            credentials=cred, client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_health_profile_service_host_no_port(transport_name):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="health.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "health.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://health.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_health_profile_service_host_with_port(transport_name):
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="health.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "health.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://health.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_health_profile_service_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = HealthProfileServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = HealthProfileServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.get_profile._session
    session2 = client2.transport.get_profile._session
    assert session1 != session2
    session1 = client1.transport.update_profile._session
    session2 = client2.transport.update_profile._session
    assert session1 != session2
    session1 = client1.transport.get_settings._session
    session2 = client2.transport.get_settings._session
    assert session1 != session2
    session1 = client1.transport.update_settings._session
    session2 = client2.transport.update_settings._session
    assert session1 != session2
    session1 = client1.transport.get_identity._session
    session2 = client2.transport.get_identity._session
    assert session1 != session2
    session1 = client1.transport.get_irn_profile._session
    session2 = client2.transport.get_irn_profile._session
    assert session1 != session2
    session1 = client1.transport.get_paired_device._session
    session2 = client2.transport.get_paired_device._session
    assert session1 != session2
    session1 = client1.transport.list_paired_devices._session
    session2 = client2.transport.list_paired_devices._session
    assert session1 != session2


def test_health_profile_service_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.HealthProfileServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_health_profile_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.HealthProfileServiceGrpcAsyncIOTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


# Remove this test when deprecated arguments (api_mtls_endpoint, client_cert_source) are
# removed from grpc/grpc_asyncio transport constructor.
@pytest.mark.filterwarnings("ignore::FutureWarning")
@pytest.mark.parametrize(
    "transport_class",
    [
        transports.HealthProfileServiceGrpcTransport,
        transports.HealthProfileServiceGrpcAsyncIOTransport,
    ],
)
def test_health_profile_service_transport_channel_mtls_with_client_cert_source(
    transport_class,
):
    with mock.patch(
        "grpc.ssl_channel_credentials", autospec=True
    ) as grpc_ssl_channel_cred:
        with mock.patch.object(
            transport_class, "create_channel"
        ) as grpc_create_channel:
            mock_ssl_cred = mock.Mock()
            grpc_ssl_channel_cred.return_value = mock_ssl_cred

            mock_grpc_channel = mock.Mock()
            grpc_create_channel.return_value = mock_grpc_channel

            cred = ga_credentials.AnonymousCredentials()
            with pytest.warns(DeprecationWarning):
                with mock.patch.object(google.auth, "default") as adc:
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
@pytest.mark.parametrize(
    "transport_class",
    [
        transports.HealthProfileServiceGrpcTransport,
        transports.HealthProfileServiceGrpcAsyncIOTransport,
    ],
)
def test_health_profile_service_transport_channel_mtls_with_adc(transport_class):
    mock_ssl_cred = mock.Mock()
    with mock.patch.multiple(
        "google.auth.transport.grpc.SslCredentials",
        __init__=mock.Mock(return_value=None),
        ssl_credentials=mock.PropertyMock(return_value=mock_ssl_cred),
    ):
        with mock.patch.object(
            transport_class, "create_channel"
        ) as grpc_create_channel:
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


def test_identity_path():
    user = "squid"
    expected = "users/{user}/identity".format(
        user=user,
    )
    actual = HealthProfileServiceClient.identity_path(user)
    assert expected == actual


def test_parse_identity_path():
    expected = {
        "user": "clam",
    }
    path = HealthProfileServiceClient.identity_path(**expected)

    # Check that the path construction is reversible.
    actual = HealthProfileServiceClient.parse_identity_path(path)
    assert expected == actual


def test_irn_profile_path():
    user = "whelk"
    expected = "users/{user}/irnProfile".format(
        user=user,
    )
    actual = HealthProfileServiceClient.irn_profile_path(user)
    assert expected == actual


def test_parse_irn_profile_path():
    expected = {
        "user": "octopus",
    }
    path = HealthProfileServiceClient.irn_profile_path(**expected)

    # Check that the path construction is reversible.
    actual = HealthProfileServiceClient.parse_irn_profile_path(path)
    assert expected == actual


def test_paired_device_path():
    user = "oyster"
    paired_device = "nudibranch"
    expected = "users/{user}/pairedDevices/{paired_device}".format(
        user=user,
        paired_device=paired_device,
    )
    actual = HealthProfileServiceClient.paired_device_path(user, paired_device)
    assert expected == actual


def test_parse_paired_device_path():
    expected = {
        "user": "cuttlefish",
        "paired_device": "mussel",
    }
    path = HealthProfileServiceClient.paired_device_path(**expected)

    # Check that the path construction is reversible.
    actual = HealthProfileServiceClient.parse_paired_device_path(path)
    assert expected == actual


def test_profile_path():
    user = "winkle"
    expected = "users/{user}/profile".format(
        user=user,
    )
    actual = HealthProfileServiceClient.profile_path(user)
    assert expected == actual


def test_parse_profile_path():
    expected = {
        "user": "nautilus",
    }
    path = HealthProfileServiceClient.profile_path(**expected)

    # Check that the path construction is reversible.
    actual = HealthProfileServiceClient.parse_profile_path(path)
    assert expected == actual


def test_settings_path():
    user = "scallop"
    expected = "users/{user}/settings".format(
        user=user,
    )
    actual = HealthProfileServiceClient.settings_path(user)
    assert expected == actual


def test_parse_settings_path():
    expected = {
        "user": "abalone",
    }
    path = HealthProfileServiceClient.settings_path(**expected)

    # Check that the path construction is reversible.
    actual = HealthProfileServiceClient.parse_settings_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = HealthProfileServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = HealthProfileServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = HealthProfileServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = HealthProfileServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = HealthProfileServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = HealthProfileServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = HealthProfileServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = HealthProfileServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = HealthProfileServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = HealthProfileServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = HealthProfileServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = HealthProfileServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = HealthProfileServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = HealthProfileServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = HealthProfileServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.HealthProfileServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.HealthProfileServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = HealthProfileServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_grpc():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        with client:
            close.assert_not_called()
        close.assert_called_once()


@pytest.mark.asyncio
async def test_transport_close_grpc_asyncio():
    client = HealthProfileServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = HealthProfileServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_session")), "close"
    ) as close:
        with client:
            close.assert_not_called()
        close.assert_called_once()


def test_client_ctx():
    transports = [
        "rest",
        "grpc",
    ]
    for transport in transports:
        client = HealthProfileServiceClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()


@pytest.mark.parametrize(
    "client_class,transport_class",
    [
        (HealthProfileServiceClient, transports.HealthProfileServiceGrpcTransport),
        (
            HealthProfileServiceAsyncClient,
            transports.HealthProfileServiceGrpcAsyncIOTransport,
        ),
    ],
)
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
                host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                    UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
                ),
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )
