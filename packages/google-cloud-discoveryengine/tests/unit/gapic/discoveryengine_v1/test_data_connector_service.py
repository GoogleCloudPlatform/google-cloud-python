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

import google.api_core.operation_async as operation_async  # type: ignore
import google.auth
import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.datetime_pb2 as datetime_pb2  # type: ignore
from google.api_core import (
    client_options,
    future,
    gapic_v1,
    grpc_helpers,
    grpc_helpers_async,
    operation,
    operations_v1,
    path_template,
)
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.cloud.location import locations_pb2
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account

from google.cloud.discoveryengine_v1.services.data_connector_service import (
    DataConnectorServiceAsyncClient,
    DataConnectorServiceClient,
    transports,
)
from google.cloud.discoveryengine_v1.types import (
    common,
    data_connector,
    data_connector_service,
    schema,
)
from google.cloud.discoveryengine_v1.types import data_connector as gcd_data_connector

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

    assert DataConnectorServiceClient._get_client_cert_source(None, False) is None
    assert (
        DataConnectorServiceClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        DataConnectorServiceClient._get_client_cert_source(
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
                DataConnectorServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                DataConnectorServiceClient._get_client_cert_source(
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
    client = DataConnectorServiceClient(credentials=cred)
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
    client = DataConnectorServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (DataConnectorServiceClient, "grpc"),
        (DataConnectorServiceAsyncClient, "grpc_asyncio"),
        (DataConnectorServiceClient, "rest"),
    ],
)
def test_data_connector_service_client_from_service_account_info(
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
            "discoveryengine.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://discoveryengine.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.DataConnectorServiceGrpcTransport, "grpc"),
        (transports.DataConnectorServiceGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.DataConnectorServiceRestTransport, "rest"),
    ],
)
def test_data_connector_service_client_service_account_always_use_jwt(
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
        (DataConnectorServiceClient, "grpc"),
        (DataConnectorServiceAsyncClient, "grpc_asyncio"),
        (DataConnectorServiceClient, "rest"),
    ],
)
def test_data_connector_service_client_from_service_account_file(
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
            "discoveryengine.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://discoveryengine.googleapis.com"
        )


def test_data_connector_service_client_get_transport_class():
    transport = DataConnectorServiceClient.get_transport_class()
    available_transports = [
        transports.DataConnectorServiceGrpcTransport,
        transports.DataConnectorServiceRestTransport,
    ]
    assert transport in available_transports

    transport = DataConnectorServiceClient.get_transport_class("grpc")
    assert transport == transports.DataConnectorServiceGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            DataConnectorServiceClient,
            transports.DataConnectorServiceGrpcTransport,
            "grpc",
        ),
        (
            DataConnectorServiceAsyncClient,
            transports.DataConnectorServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            DataConnectorServiceClient,
            transports.DataConnectorServiceRestTransport,
            "rest",
        ),
    ],
)
@mock.patch.object(
    DataConnectorServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(DataConnectorServiceClient),
)
@mock.patch.object(
    DataConnectorServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(DataConnectorServiceAsyncClient),
)
def test_data_connector_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(DataConnectorServiceClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(DataConnectorServiceClient, "get_transport_class") as gtc:
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
            DataConnectorServiceClient,
            transports.DataConnectorServiceGrpcTransport,
            "grpc",
            "true",
        ),
        (
            DataConnectorServiceAsyncClient,
            transports.DataConnectorServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            DataConnectorServiceClient,
            transports.DataConnectorServiceGrpcTransport,
            "grpc",
            "false",
        ),
        (
            DataConnectorServiceAsyncClient,
            transports.DataConnectorServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (
            DataConnectorServiceClient,
            transports.DataConnectorServiceRestTransport,
            "rest",
            "true",
        ),
        (
            DataConnectorServiceClient,
            transports.DataConnectorServiceRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    DataConnectorServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(DataConnectorServiceClient),
)
@mock.patch.object(
    DataConnectorServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(DataConnectorServiceAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_data_connector_service_client_mtls_env_auto(
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
    "client_class", [DataConnectorServiceClient, DataConnectorServiceAsyncClient]
)
@mock.patch.object(
    DataConnectorServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(DataConnectorServiceClient),
)
@mock.patch.object(
    DataConnectorServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(DataConnectorServiceAsyncClient),
)
def test_data_connector_service_client_get_mtls_endpoint_and_cert_source(client_class):
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
    "client_class", [DataConnectorServiceClient, DataConnectorServiceAsyncClient]
)
@mock.patch.object(
    DataConnectorServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(DataConnectorServiceClient),
)
@mock.patch.object(
    DataConnectorServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(DataConnectorServiceAsyncClient),
)
def test_data_connector_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = DataConnectorServiceClient._DEFAULT_UNIVERSE
    default_endpoint = DataConnectorServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = DataConnectorServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
            DataConnectorServiceClient,
            transports.DataConnectorServiceGrpcTransport,
            "grpc",
        ),
        (
            DataConnectorServiceAsyncClient,
            transports.DataConnectorServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            DataConnectorServiceClient,
            transports.DataConnectorServiceRestTransport,
            "rest",
        ),
    ],
)
def test_data_connector_service_client_client_options_scopes(
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
            DataConnectorServiceClient,
            transports.DataConnectorServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            DataConnectorServiceAsyncClient,
            transports.DataConnectorServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (
            DataConnectorServiceClient,
            transports.DataConnectorServiceRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_data_connector_service_client_client_options_credentials_file(
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


def test_data_connector_service_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.discoveryengine_v1.services.data_connector_service.transports.DataConnectorServiceGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = DataConnectorServiceClient(
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
            DataConnectorServiceClient,
            transports.DataConnectorServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            DataConnectorServiceAsyncClient,
            transports.DataConnectorServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_data_connector_service_client_create_channel_credentials_file(
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
            "discoveryengine.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/discoveryengine.assist.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.serving.readwrite",
            ),
            scopes=None,
            default_host="discoveryengine.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        data_connector_service.SetUpDataConnectorRequest(),
        {},
    ],
)
def test_set_up_data_connector(request_type, transport: str = "grpc"):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.set_up_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.set_up_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = data_connector_service.SetUpDataConnectorRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_set_up_data_connector_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = data_connector_service.SetUpDataConnectorRequest(
        parent="parent_value",
        collection_id="collection_id_value",
        collection_display_name="collection_display_name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.set_up_data_connector), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.set_up_data_connector(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_connector_service.SetUpDataConnectorRequest(
            parent="parent_value",
            collection_id="collection_id_value",
            collection_display_name="collection_display_name_value",
        )
        assert args[0] == request_msg


def test_set_up_data_connector_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataConnectorServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.set_up_data_connector
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.set_up_data_connector] = (
            mock_rpc
        )
        request = {}
        client.set_up_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.set_up_data_connector(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_set_up_data_connector_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = DataConnectorServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.set_up_data_connector
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.set_up_data_connector
        ] = mock_rpc

        request = {}
        await client.set_up_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.set_up_data_connector(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        data_connector_service.SetUpDataConnectorRequest(),
        {},
    ],
)
async def test_set_up_data_connector_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.set_up_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.set_up_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = data_connector_service.SetUpDataConnectorRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_set_up_data_connector_field_headers():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_connector_service.SetUpDataConnectorRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.set_up_data_connector), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.set_up_data_connector(request)

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
async def test_set_up_data_connector_field_headers_async():
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_connector_service.SetUpDataConnectorRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.set_up_data_connector), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.set_up_data_connector(request)

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


def test_set_up_data_connector_flattened():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.set_up_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.set_up_data_connector(
            parent="parent_value",
            collection_id="collection_id_value",
            collection_display_name="collection_display_name_value",
            data_connector=gcd_data_connector.DataConnector(
                params=struct_pb2.Struct(
                    fields={
                        "key_value": struct_pb2.Value(
                            null_value=struct_pb2.NullValue.NULL_VALUE
                        )
                    }
                )
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].collection_id
        mock_val = "collection_id_value"
        assert arg == mock_val
        arg = args[0].collection_display_name
        mock_val = "collection_display_name_value"
        assert arg == mock_val
        arg = args[0].data_connector
        mock_val = gcd_data_connector.DataConnector(
            params=struct_pb2.Struct(
                fields={
                    "key_value": struct_pb2.Value(
                        null_value=struct_pb2.NullValue.NULL_VALUE
                    )
                }
            )
        )
        assert arg == mock_val


def test_set_up_data_connector_flattened_error():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.set_up_data_connector(
            data_connector_service.SetUpDataConnectorRequest(),
            parent="parent_value",
            collection_id="collection_id_value",
            collection_display_name="collection_display_name_value",
            data_connector=gcd_data_connector.DataConnector(
                params=struct_pb2.Struct(
                    fields={
                        "key_value": struct_pb2.Value(
                            null_value=struct_pb2.NullValue.NULL_VALUE
                        )
                    }
                )
            ),
        )


@pytest.mark.asyncio
async def test_set_up_data_connector_flattened_async():
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.set_up_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.set_up_data_connector(
            parent="parent_value",
            collection_id="collection_id_value",
            collection_display_name="collection_display_name_value",
            data_connector=gcd_data_connector.DataConnector(
                params=struct_pb2.Struct(
                    fields={
                        "key_value": struct_pb2.Value(
                            null_value=struct_pb2.NullValue.NULL_VALUE
                        )
                    }
                )
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].collection_id
        mock_val = "collection_id_value"
        assert arg == mock_val
        arg = args[0].collection_display_name
        mock_val = "collection_display_name_value"
        assert arg == mock_val
        arg = args[0].data_connector
        mock_val = gcd_data_connector.DataConnector(
            params=struct_pb2.Struct(
                fields={
                    "key_value": struct_pb2.Value(
                        null_value=struct_pb2.NullValue.NULL_VALUE
                    )
                }
            )
        )
        assert arg == mock_val


@pytest.mark.asyncio
async def test_set_up_data_connector_flattened_error_async():
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.set_up_data_connector(
            data_connector_service.SetUpDataConnectorRequest(),
            parent="parent_value",
            collection_id="collection_id_value",
            collection_display_name="collection_display_name_value",
            data_connector=gcd_data_connector.DataConnector(
                params=struct_pb2.Struct(
                    fields={
                        "key_value": struct_pb2.Value(
                            null_value=struct_pb2.NullValue.NULL_VALUE
                        )
                    }
                )
            ),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        data_connector_service.GetDataConnectorRequest(),
        {},
    ],
)
def test_get_data_connector(request_type, transport: str = "grpc"):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_connector.DataConnector(
            name="name_value",
            state=data_connector.DataConnector.State.CREATING,
            data_source="data_source_value",
            remove_param_keys=["remove_param_keys_value"],
            sync_mode=data_connector.DataConnector.SyncMode.STREAMING,
            kms_key_name="kms_key_name_value",
            action_state=data_connector.DataConnector.State.CREATING,
            connector_modes=[data_connector.DataConnector.ConnectorMode.DATA_INGESTION],
            static_ip_enabled=True,
            static_ip_addresses=["static_ip_addresses_value"],
            oauth_static_ip_addresses=["oauth_static_ip_addresses_value"],
            blocking_reasons=[
                data_connector.DataConnector.BlockingReason.ALLOWLIST_STATIC_IP
            ],
            private_connectivity_project_id="private_connectivity_project_id_value",
            connector_type=data_connector.ConnectorType.THIRD_PARTY,
            realtime_state=data_connector.DataConnector.State.CREATING,
            acl_enabled=True,
            create_eua_saas=True,
            auto_run_disabled=True,
            incremental_sync_disabled=True,
            hybrid_ingestion_disabled=True,
            egress_fqdns=["egress_fqdns_value"],
            vpcsc_enabled=True,
            connector_source_id="connector_source_id_value",
            tag="tag_value",
            json_params="json_params_value",
        )
        response = client.get_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = data_connector_service.GetDataConnectorRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, data_connector.DataConnector)
    assert response.name == "name_value"
    assert response.state == data_connector.DataConnector.State.CREATING
    assert response.data_source == "data_source_value"
    assert response.remove_param_keys == ["remove_param_keys_value"]
    assert response.sync_mode == data_connector.DataConnector.SyncMode.STREAMING
    assert response.kms_key_name == "kms_key_name_value"
    assert response.action_state == data_connector.DataConnector.State.CREATING
    assert response.connector_modes == [
        data_connector.DataConnector.ConnectorMode.DATA_INGESTION
    ]
    assert response.static_ip_enabled is True
    assert response.static_ip_addresses == ["static_ip_addresses_value"]
    assert response.oauth_static_ip_addresses == ["oauth_static_ip_addresses_value"]
    assert response.blocking_reasons == [
        data_connector.DataConnector.BlockingReason.ALLOWLIST_STATIC_IP
    ]
    assert (
        response.private_connectivity_project_id
        == "private_connectivity_project_id_value"
    )
    assert response.connector_type == data_connector.ConnectorType.THIRD_PARTY
    assert response.realtime_state == data_connector.DataConnector.State.CREATING
    assert response.acl_enabled is True
    assert response.create_eua_saas is True
    assert response.auto_run_disabled is True
    assert response.incremental_sync_disabled is True
    assert response.hybrid_ingestion_disabled is True
    assert response.egress_fqdns == ["egress_fqdns_value"]
    assert response.vpcsc_enabled is True
    assert response.connector_source_id == "connector_source_id_value"
    assert response.tag == "tag_value"


def test_get_data_connector_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = data_connector_service.GetDataConnectorRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_data_connector), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_data_connector(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_connector_service.GetDataConnectorRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_data_connector_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataConnectorServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_data_connector in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_data_connector] = (
            mock_rpc
        )
        request = {}
        client.get_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_data_connector(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_data_connector_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = DataConnectorServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_data_connector
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_data_connector
        ] = mock_rpc

        request = {}
        await client.get_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_data_connector(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        data_connector_service.GetDataConnectorRequest(),
        {},
    ],
)
async def test_get_data_connector_async(request_type, transport: str = "grpc_asyncio"):
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_connector.DataConnector(
                name="name_value",
                state=data_connector.DataConnector.State.CREATING,
                data_source="data_source_value",
                remove_param_keys=["remove_param_keys_value"],
                sync_mode=data_connector.DataConnector.SyncMode.STREAMING,
                kms_key_name="kms_key_name_value",
                action_state=data_connector.DataConnector.State.CREATING,
                connector_modes=[
                    data_connector.DataConnector.ConnectorMode.DATA_INGESTION
                ],
                static_ip_enabled=True,
                static_ip_addresses=["static_ip_addresses_value"],
                oauth_static_ip_addresses=["oauth_static_ip_addresses_value"],
                blocking_reasons=[
                    data_connector.DataConnector.BlockingReason.ALLOWLIST_STATIC_IP
                ],
                private_connectivity_project_id="private_connectivity_project_id_value",
                connector_type=data_connector.ConnectorType.THIRD_PARTY,
                realtime_state=data_connector.DataConnector.State.CREATING,
                acl_enabled=True,
                create_eua_saas=True,
                auto_run_disabled=True,
                incremental_sync_disabled=True,
                hybrid_ingestion_disabled=True,
                egress_fqdns=["egress_fqdns_value"],
                vpcsc_enabled=True,
                connector_source_id="connector_source_id_value",
                tag="tag_value",
            )
        )
        response = await client.get_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = data_connector_service.GetDataConnectorRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, data_connector.DataConnector)
    assert response.name == "name_value"
    assert response.state == data_connector.DataConnector.State.CREATING
    assert response.data_source == "data_source_value"
    assert response.remove_param_keys == ["remove_param_keys_value"]
    assert response.sync_mode == data_connector.DataConnector.SyncMode.STREAMING
    assert response.kms_key_name == "kms_key_name_value"
    assert response.action_state == data_connector.DataConnector.State.CREATING
    assert response.connector_modes == [
        data_connector.DataConnector.ConnectorMode.DATA_INGESTION
    ]
    assert response.static_ip_enabled is True
    assert response.static_ip_addresses == ["static_ip_addresses_value"]
    assert response.oauth_static_ip_addresses == ["oauth_static_ip_addresses_value"]
    assert response.blocking_reasons == [
        data_connector.DataConnector.BlockingReason.ALLOWLIST_STATIC_IP
    ]
    assert (
        response.private_connectivity_project_id
        == "private_connectivity_project_id_value"
    )
    assert response.connector_type == data_connector.ConnectorType.THIRD_PARTY
    assert response.realtime_state == data_connector.DataConnector.State.CREATING
    assert response.acl_enabled is True
    assert response.create_eua_saas is True
    assert response.auto_run_disabled is True
    assert response.incremental_sync_disabled is True
    assert response.hybrid_ingestion_disabled is True
    assert response.egress_fqdns == ["egress_fqdns_value"]
    assert response.vpcsc_enabled is True
    assert response.connector_source_id == "connector_source_id_value"
    assert response.tag == "tag_value"


def test_get_data_connector_field_headers():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_connector_service.GetDataConnectorRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_data_connector), "__call__"
    ) as call:
        call.return_value = data_connector.DataConnector()
        client.get_data_connector(request)

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
async def test_get_data_connector_field_headers_async():
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_connector_service.GetDataConnectorRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_data_connector), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_connector.DataConnector()
        )
        await client.get_data_connector(request)

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


def test_get_data_connector_flattened():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_connector.DataConnector()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_data_connector(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_data_connector_flattened_error():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_data_connector(
            data_connector_service.GetDataConnectorRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_data_connector_flattened_async():
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_connector.DataConnector()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_connector.DataConnector()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_data_connector(
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
async def test_get_data_connector_flattened_error_async():
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_data_connector(
            data_connector_service.GetDataConnectorRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        data_connector_service.UpdateDataConnectorRequest(),
        {},
    ],
)
def test_update_data_connector(request_type, transport: str = "grpc"):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcd_data_connector.DataConnector(
            name="name_value",
            state=gcd_data_connector.DataConnector.State.CREATING,
            data_source="data_source_value",
            remove_param_keys=["remove_param_keys_value"],
            sync_mode=gcd_data_connector.DataConnector.SyncMode.STREAMING,
            kms_key_name="kms_key_name_value",
            action_state=gcd_data_connector.DataConnector.State.CREATING,
            connector_modes=[
                gcd_data_connector.DataConnector.ConnectorMode.DATA_INGESTION
            ],
            static_ip_enabled=True,
            static_ip_addresses=["static_ip_addresses_value"],
            oauth_static_ip_addresses=["oauth_static_ip_addresses_value"],
            blocking_reasons=[
                gcd_data_connector.DataConnector.BlockingReason.ALLOWLIST_STATIC_IP
            ],
            private_connectivity_project_id="private_connectivity_project_id_value",
            connector_type=gcd_data_connector.ConnectorType.THIRD_PARTY,
            realtime_state=gcd_data_connector.DataConnector.State.CREATING,
            acl_enabled=True,
            create_eua_saas=True,
            auto_run_disabled=True,
            incremental_sync_disabled=True,
            hybrid_ingestion_disabled=True,
            egress_fqdns=["egress_fqdns_value"],
            vpcsc_enabled=True,
            connector_source_id="connector_source_id_value",
            tag="tag_value",
            json_params="json_params_value",
        )
        response = client.update_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = data_connector_service.UpdateDataConnectorRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcd_data_connector.DataConnector)
    assert response.name == "name_value"
    assert response.state == gcd_data_connector.DataConnector.State.CREATING
    assert response.data_source == "data_source_value"
    assert response.remove_param_keys == ["remove_param_keys_value"]
    assert response.sync_mode == gcd_data_connector.DataConnector.SyncMode.STREAMING
    assert response.kms_key_name == "kms_key_name_value"
    assert response.action_state == gcd_data_connector.DataConnector.State.CREATING
    assert response.connector_modes == [
        gcd_data_connector.DataConnector.ConnectorMode.DATA_INGESTION
    ]
    assert response.static_ip_enabled is True
    assert response.static_ip_addresses == ["static_ip_addresses_value"]
    assert response.oauth_static_ip_addresses == ["oauth_static_ip_addresses_value"]
    assert response.blocking_reasons == [
        gcd_data_connector.DataConnector.BlockingReason.ALLOWLIST_STATIC_IP
    ]
    assert (
        response.private_connectivity_project_id
        == "private_connectivity_project_id_value"
    )
    assert response.connector_type == gcd_data_connector.ConnectorType.THIRD_PARTY
    assert response.realtime_state == gcd_data_connector.DataConnector.State.CREATING
    assert response.acl_enabled is True
    assert response.create_eua_saas is True
    assert response.auto_run_disabled is True
    assert response.incremental_sync_disabled is True
    assert response.hybrid_ingestion_disabled is True
    assert response.egress_fqdns == ["egress_fqdns_value"]
    assert response.vpcsc_enabled is True
    assert response.connector_source_id == "connector_source_id_value"
    assert response.tag == "tag_value"


def test_update_data_connector_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = data_connector_service.UpdateDataConnectorRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_connector), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_data_connector(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_connector_service.UpdateDataConnectorRequest()
        assert args[0] == request_msg


def test_update_data_connector_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataConnectorServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_data_connector
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_data_connector] = (
            mock_rpc
        )
        request = {}
        client.update_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_data_connector(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_data_connector_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = DataConnectorServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_data_connector
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_data_connector
        ] = mock_rpc

        request = {}
        await client.update_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_data_connector(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        data_connector_service.UpdateDataConnectorRequest(),
        {},
    ],
)
async def test_update_data_connector_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcd_data_connector.DataConnector(
                name="name_value",
                state=gcd_data_connector.DataConnector.State.CREATING,
                data_source="data_source_value",
                remove_param_keys=["remove_param_keys_value"],
                sync_mode=gcd_data_connector.DataConnector.SyncMode.STREAMING,
                kms_key_name="kms_key_name_value",
                action_state=gcd_data_connector.DataConnector.State.CREATING,
                connector_modes=[
                    gcd_data_connector.DataConnector.ConnectorMode.DATA_INGESTION
                ],
                static_ip_enabled=True,
                static_ip_addresses=["static_ip_addresses_value"],
                oauth_static_ip_addresses=["oauth_static_ip_addresses_value"],
                blocking_reasons=[
                    gcd_data_connector.DataConnector.BlockingReason.ALLOWLIST_STATIC_IP
                ],
                private_connectivity_project_id="private_connectivity_project_id_value",
                connector_type=gcd_data_connector.ConnectorType.THIRD_PARTY,
                realtime_state=gcd_data_connector.DataConnector.State.CREATING,
                acl_enabled=True,
                create_eua_saas=True,
                auto_run_disabled=True,
                incremental_sync_disabled=True,
                hybrid_ingestion_disabled=True,
                egress_fqdns=["egress_fqdns_value"],
                vpcsc_enabled=True,
                connector_source_id="connector_source_id_value",
                tag="tag_value",
            )
        )
        response = await client.update_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = data_connector_service.UpdateDataConnectorRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcd_data_connector.DataConnector)
    assert response.name == "name_value"
    assert response.state == gcd_data_connector.DataConnector.State.CREATING
    assert response.data_source == "data_source_value"
    assert response.remove_param_keys == ["remove_param_keys_value"]
    assert response.sync_mode == gcd_data_connector.DataConnector.SyncMode.STREAMING
    assert response.kms_key_name == "kms_key_name_value"
    assert response.action_state == gcd_data_connector.DataConnector.State.CREATING
    assert response.connector_modes == [
        gcd_data_connector.DataConnector.ConnectorMode.DATA_INGESTION
    ]
    assert response.static_ip_enabled is True
    assert response.static_ip_addresses == ["static_ip_addresses_value"]
    assert response.oauth_static_ip_addresses == ["oauth_static_ip_addresses_value"]
    assert response.blocking_reasons == [
        gcd_data_connector.DataConnector.BlockingReason.ALLOWLIST_STATIC_IP
    ]
    assert (
        response.private_connectivity_project_id
        == "private_connectivity_project_id_value"
    )
    assert response.connector_type == gcd_data_connector.ConnectorType.THIRD_PARTY
    assert response.realtime_state == gcd_data_connector.DataConnector.State.CREATING
    assert response.acl_enabled is True
    assert response.create_eua_saas is True
    assert response.auto_run_disabled is True
    assert response.incremental_sync_disabled is True
    assert response.hybrid_ingestion_disabled is True
    assert response.egress_fqdns == ["egress_fqdns_value"]
    assert response.vpcsc_enabled is True
    assert response.connector_source_id == "connector_source_id_value"
    assert response.tag == "tag_value"


def test_update_data_connector_field_headers():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_connector_service.UpdateDataConnectorRequest()

    request.data_connector.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_connector), "__call__"
    ) as call:
        call.return_value = gcd_data_connector.DataConnector()
        client.update_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "data_connector.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_data_connector_field_headers_async():
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_connector_service.UpdateDataConnectorRequest()

    request.data_connector.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_connector), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcd_data_connector.DataConnector()
        )
        await client.update_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "data_connector.name=name_value",
    ) in kw["metadata"]


def test_update_data_connector_flattened():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcd_data_connector.DataConnector()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_data_connector(
            data_connector=gcd_data_connector.DataConnector(
                params=struct_pb2.Struct(
                    fields={
                        "key_value": struct_pb2.Value(
                            null_value=struct_pb2.NullValue.NULL_VALUE
                        )
                    }
                )
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].data_connector
        mock_val = gcd_data_connector.DataConnector(
            params=struct_pb2.Struct(
                fields={
                    "key_value": struct_pb2.Value(
                        null_value=struct_pb2.NullValue.NULL_VALUE
                    )
                }
            )
        )
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_data_connector_flattened_error():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_data_connector(
            data_connector_service.UpdateDataConnectorRequest(),
            data_connector=gcd_data_connector.DataConnector(
                params=struct_pb2.Struct(
                    fields={
                        "key_value": struct_pb2.Value(
                            null_value=struct_pb2.NullValue.NULL_VALUE
                        )
                    }
                )
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_data_connector_flattened_async():
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcd_data_connector.DataConnector()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcd_data_connector.DataConnector()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_data_connector(
            data_connector=gcd_data_connector.DataConnector(
                params=struct_pb2.Struct(
                    fields={
                        "key_value": struct_pb2.Value(
                            null_value=struct_pb2.NullValue.NULL_VALUE
                        )
                    }
                )
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].data_connector
        mock_val = gcd_data_connector.DataConnector(
            params=struct_pb2.Struct(
                fields={
                    "key_value": struct_pb2.Value(
                        null_value=struct_pb2.NullValue.NULL_VALUE
                    )
                }
            )
        )
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_data_connector_flattened_error_async():
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_data_connector(
            data_connector_service.UpdateDataConnectorRequest(),
            data_connector=gcd_data_connector.DataConnector(
                params=struct_pb2.Struct(
                    fields={
                        "key_value": struct_pb2.Value(
                            null_value=struct_pb2.NullValue.NULL_VALUE
                        )
                    }
                )
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_set_up_data_connector_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataConnectorServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.set_up_data_connector
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.set_up_data_connector] = (
            mock_rpc
        )

        request = {}
        client.set_up_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.set_up_data_connector(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_set_up_data_connector_rest_required_fields(
    request_type=data_connector_service.SetUpDataConnectorRequest,
):
    transport_class = transports.DataConnectorServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["collection_id"] = ""
    request_init["collection_display_name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseSetUpDataConnector,
        "_BaseSetUpDataConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["collectionId"] = "collection_id_value"
    jsonified_request["collectionDisplayName"] = "collection_display_name_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "collectionId" in jsonified_request
    assert jsonified_request["collectionId"] == "collection_id_value"
    assert "collectionDisplayName" in jsonified_request
    assert jsonified_request["collectionDisplayName"] == "collection_display_name_value"

    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = operations_pb2.Operation(name="operations/spam")
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
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.set_up_data_connector(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_set_up_data_connector_rest_flattened():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1/locations/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            collection_id="collection_id_value",
            collection_display_name="collection_display_name_value",
            data_connector=gcd_data_connector.DataConnector(
                params=struct_pb2.Struct(
                    fields={
                        "key_value": struct_pb2.Value(
                            null_value=struct_pb2.NullValue.NULL_VALUE
                        )
                    }
                )
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.set_up_data_connector(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*}:setUpDataConnector"
            % client.transport._host,
            args[1],
        )


def test_set_up_data_connector_rest_flattened_error(transport: str = "rest"):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.set_up_data_connector(
            data_connector_service.SetUpDataConnectorRequest(),
            parent="parent_value",
            collection_id="collection_id_value",
            collection_display_name="collection_display_name_value",
            data_connector=gcd_data_connector.DataConnector(
                params=struct_pb2.Struct(
                    fields={
                        "key_value": struct_pb2.Value(
                            null_value=struct_pb2.NullValue.NULL_VALUE
                        )
                    }
                )
            ),
        )


def test_get_data_connector_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataConnectorServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_data_connector in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_data_connector] = (
            mock_rpc
        )

        request = {}
        client.get_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_data_connector(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_data_connector_rest_required_fields(
    request_type=data_connector_service.GetDataConnectorRequest,
):
    transport_class = transports.DataConnectorServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetDataConnector,
        "_BaseGetDataConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = data_connector.DataConnector()
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
            return_value = data_connector.DataConnector.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_data_connector(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_data_connector_rest_flattened():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = data_connector.DataConnector()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/collections/sample3/dataConnector"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = data_connector.DataConnector.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_data_connector(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/collections/*/dataConnector}"
            % client.transport._host,
            args[1],
        )


def test_get_data_connector_rest_flattened_error(transport: str = "rest"):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_data_connector(
            data_connector_service.GetDataConnectorRequest(),
            name="name_value",
        )


def test_update_data_connector_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataConnectorServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_data_connector
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_data_connector] = (
            mock_rpc
        )

        request = {}
        client.update_data_connector(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_data_connector(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_data_connector_rest_required_fields(
    request_type=data_connector_service.UpdateDataConnectorRequest,
):
    transport_class = transports.DataConnectorServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateDataConnector,
        "_BaseUpdateDataConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gcd_data_connector.DataConnector()
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
            return_value = gcd_data_connector.DataConnector.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_data_connector(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_data_connector_rest_flattened():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcd_data_connector.DataConnector()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "data_connector": {
                "name": "projects/sample1/locations/sample2/collections/sample3/dataConnector"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            data_connector=gcd_data_connector.DataConnector(
                params=struct_pb2.Struct(
                    fields={
                        "key_value": struct_pb2.Value(
                            null_value=struct_pb2.NullValue.NULL_VALUE
                        )
                    }
                )
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = gcd_data_connector.DataConnector.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_data_connector(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{data_connector.name=projects/*/locations/*/collections/*/dataConnector}"
            % client.transport._host,
            args[1],
        )


def test_update_data_connector_rest_flattened_error(transport: str = "rest"):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_data_connector(
            data_connector_service.UpdateDataConnectorRequest(),
            data_connector=gcd_data_connector.DataConnector(
                params=struct_pb2.Struct(
                    fields={
                        "key_value": struct_pb2.Value(
                            null_value=struct_pb2.NullValue.NULL_VALUE
                        )
                    }
                )
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.DataConnectorServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = DataConnectorServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.DataConnectorServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = DataConnectorServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.DataConnectorServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = DataConnectorServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = DataConnectorServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.DataConnectorServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = DataConnectorServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.DataConnectorServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = DataConnectorServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.DataConnectorServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.DataConnectorServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.DataConnectorServiceGrpcTransport,
        transports.DataConnectorServiceGrpcAsyncIOTransport,
        transports.DataConnectorServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = DataConnectorServiceClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_set_up_data_connector_empty_call_grpc():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.set_up_data_connector), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.set_up_data_connector(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_connector_service.SetUpDataConnectorRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_data_connector_empty_call_grpc():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_data_connector), "__call__"
    ) as call:
        call.return_value = data_connector.DataConnector()
        client.get_data_connector(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_connector_service.GetDataConnectorRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_data_connector_empty_call_grpc():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_connector), "__call__"
    ) as call:
        call.return_value = gcd_data_connector.DataConnector()
        client.update_data_connector(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_connector_service.UpdateDataConnectorRequest()
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = DataConnectorServiceAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_set_up_data_connector_empty_call_grpc_asyncio():
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.set_up_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.set_up_data_connector(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_connector_service.SetUpDataConnectorRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_data_connector_empty_call_grpc_asyncio():
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_connector.DataConnector(
                name="name_value",
                state=data_connector.DataConnector.State.CREATING,
                data_source="data_source_value",
                remove_param_keys=["remove_param_keys_value"],
                sync_mode=data_connector.DataConnector.SyncMode.STREAMING,
                kms_key_name="kms_key_name_value",
                action_state=data_connector.DataConnector.State.CREATING,
                connector_modes=[
                    data_connector.DataConnector.ConnectorMode.DATA_INGESTION
                ],
                static_ip_enabled=True,
                static_ip_addresses=["static_ip_addresses_value"],
                oauth_static_ip_addresses=["oauth_static_ip_addresses_value"],
                blocking_reasons=[
                    data_connector.DataConnector.BlockingReason.ALLOWLIST_STATIC_IP
                ],
                private_connectivity_project_id="private_connectivity_project_id_value",
                connector_type=data_connector.ConnectorType.THIRD_PARTY,
                realtime_state=data_connector.DataConnector.State.CREATING,
                acl_enabled=True,
                create_eua_saas=True,
                auto_run_disabled=True,
                incremental_sync_disabled=True,
                hybrid_ingestion_disabled=True,
                egress_fqdns=["egress_fqdns_value"],
                vpcsc_enabled=True,
                connector_source_id="connector_source_id_value",
                tag="tag_value",
            )
        )
        await client.get_data_connector(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_connector_service.GetDataConnectorRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_data_connector_empty_call_grpc_asyncio():
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_connector), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcd_data_connector.DataConnector(
                name="name_value",
                state=gcd_data_connector.DataConnector.State.CREATING,
                data_source="data_source_value",
                remove_param_keys=["remove_param_keys_value"],
                sync_mode=gcd_data_connector.DataConnector.SyncMode.STREAMING,
                kms_key_name="kms_key_name_value",
                action_state=gcd_data_connector.DataConnector.State.CREATING,
                connector_modes=[
                    gcd_data_connector.DataConnector.ConnectorMode.DATA_INGESTION
                ],
                static_ip_enabled=True,
                static_ip_addresses=["static_ip_addresses_value"],
                oauth_static_ip_addresses=["oauth_static_ip_addresses_value"],
                blocking_reasons=[
                    gcd_data_connector.DataConnector.BlockingReason.ALLOWLIST_STATIC_IP
                ],
                private_connectivity_project_id="private_connectivity_project_id_value",
                connector_type=gcd_data_connector.ConnectorType.THIRD_PARTY,
                realtime_state=gcd_data_connector.DataConnector.State.CREATING,
                acl_enabled=True,
                create_eua_saas=True,
                auto_run_disabled=True,
                incremental_sync_disabled=True,
                hybrid_ingestion_disabled=True,
                egress_fqdns=["egress_fqdns_value"],
                vpcsc_enabled=True,
                connector_source_id="connector_source_id_value",
                tag="tag_value",
            )
        )
        await client.update_data_connector(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_connector_service.UpdateDataConnectorRequest()
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = DataConnectorServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_set_up_data_connector_rest_bad_request(
    request_type=data_connector_service.SetUpDataConnectorRequest,
):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
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
        client.set_up_data_connector(request)


@pytest.mark.parametrize(
    "request_type",
    [
        data_connector_service.SetUpDataConnectorRequest,
        dict,
    ],
)
def test_set_up_data_connector_rest_call_success(request_type):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.set_up_data_connector(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_set_up_data_connector_rest_interceptors(null_interceptor):
    transport = transports.DataConnectorServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.DataConnectorServiceRestInterceptor(),
    )
    client = DataConnectorServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.DataConnectorServiceRestInterceptor, "post_set_up_data_connector"
        ) as post,
        mock.patch.object(
            transports.DataConnectorServiceRestInterceptor,
            "post_set_up_data_connector_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.DataConnectorServiceRestInterceptor, "pre_set_up_data_connector"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = data_connector_service.SetUpDataConnectorRequest.pb(
            data_connector_service.SetUpDataConnectorRequest()
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
        return_value = json_format.MessageToJson(operations_pb2.Operation())
        req.return_value.content = return_value

        request = data_connector_service.SetUpDataConnectorRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.set_up_data_connector(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_data_connector_rest_bad_request(
    request_type=data_connector_service.GetDataConnectorRequest,
):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/collections/sample3/dataConnector"
    }
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
        client.get_data_connector(request)


@pytest.mark.parametrize(
    "request_type",
    [
        data_connector_service.GetDataConnectorRequest,
        dict,
    ],
)
def test_get_data_connector_rest_call_success(request_type):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/collections/sample3/dataConnector"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = data_connector.DataConnector(
            name="name_value",
            state=data_connector.DataConnector.State.CREATING,
            data_source="data_source_value",
            remove_param_keys=["remove_param_keys_value"],
            sync_mode=data_connector.DataConnector.SyncMode.STREAMING,
            kms_key_name="kms_key_name_value",
            action_state=data_connector.DataConnector.State.CREATING,
            connector_modes=[data_connector.DataConnector.ConnectorMode.DATA_INGESTION],
            static_ip_enabled=True,
            static_ip_addresses=["static_ip_addresses_value"],
            oauth_static_ip_addresses=["oauth_static_ip_addresses_value"],
            blocking_reasons=[
                data_connector.DataConnector.BlockingReason.ALLOWLIST_STATIC_IP
            ],
            private_connectivity_project_id="private_connectivity_project_id_value",
            connector_type=data_connector.ConnectorType.THIRD_PARTY,
            realtime_state=data_connector.DataConnector.State.CREATING,
            acl_enabled=True,
            create_eua_saas=True,
            auto_run_disabled=True,
            incremental_sync_disabled=True,
            hybrid_ingestion_disabled=True,
            egress_fqdns=["egress_fqdns_value"],
            vpcsc_enabled=True,
            connector_source_id="connector_source_id_value",
            tag="tag_value",
            json_params="json_params_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = data_connector.DataConnector.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_data_connector(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, data_connector.DataConnector)
    assert response.name == "name_value"
    assert response.state == data_connector.DataConnector.State.CREATING
    assert response.data_source == "data_source_value"
    assert response.remove_param_keys == ["remove_param_keys_value"]
    assert response.sync_mode == data_connector.DataConnector.SyncMode.STREAMING
    assert response.kms_key_name == "kms_key_name_value"
    assert response.action_state == data_connector.DataConnector.State.CREATING
    assert response.connector_modes == [
        data_connector.DataConnector.ConnectorMode.DATA_INGESTION
    ]
    assert response.static_ip_enabled is True
    assert response.static_ip_addresses == ["static_ip_addresses_value"]
    assert response.oauth_static_ip_addresses == ["oauth_static_ip_addresses_value"]
    assert response.blocking_reasons == [
        data_connector.DataConnector.BlockingReason.ALLOWLIST_STATIC_IP
    ]
    assert (
        response.private_connectivity_project_id
        == "private_connectivity_project_id_value"
    )
    assert response.connector_type == data_connector.ConnectorType.THIRD_PARTY
    assert response.realtime_state == data_connector.DataConnector.State.CREATING
    assert response.acl_enabled is True
    assert response.create_eua_saas is True
    assert response.auto_run_disabled is True
    assert response.incremental_sync_disabled is True
    assert response.hybrid_ingestion_disabled is True
    assert response.egress_fqdns == ["egress_fqdns_value"]
    assert response.vpcsc_enabled is True
    assert response.connector_source_id == "connector_source_id_value"
    assert response.tag == "tag_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_data_connector_rest_interceptors(null_interceptor):
    transport = transports.DataConnectorServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.DataConnectorServiceRestInterceptor(),
    )
    client = DataConnectorServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.DataConnectorServiceRestInterceptor, "post_get_data_connector"
        ) as post,
        mock.patch.object(
            transports.DataConnectorServiceRestInterceptor,
            "post_get_data_connector_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.DataConnectorServiceRestInterceptor, "pre_get_data_connector"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = data_connector_service.GetDataConnectorRequest.pb(
            data_connector_service.GetDataConnectorRequest()
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
        return_value = data_connector.DataConnector.to_json(
            data_connector.DataConnector()
        )
        req.return_value.content = return_value

        request = data_connector_service.GetDataConnectorRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = data_connector.DataConnector()
        post_with_metadata.return_value = data_connector.DataConnector(), metadata

        client.get_data_connector(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_data_connector_rest_bad_request(
    request_type=data_connector_service.UpdateDataConnectorRequest,
):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "data_connector": {
            "name": "projects/sample1/locations/sample2/collections/sample3/dataConnector"
        }
    }
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
        client.update_data_connector(request)


@pytest.mark.parametrize(
    "request_type",
    [
        data_connector_service.UpdateDataConnectorRequest,
        dict,
    ],
)
def test_update_data_connector_rest_call_success(request_type):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "data_connector": {
            "name": "projects/sample1/locations/sample2/collections/sample3/dataConnector"
        }
    }
    request_init["data_connector"] = {
        "params": {"fields": {}},
        "json_params": "json_params_value",
        "name": "projects/sample1/locations/sample2/collections/sample3/dataConnector",
        "state": 1,
        "data_source": "data_source_value",
        "remove_param_keys": ["remove_param_keys_value1", "remove_param_keys_value2"],
        "refresh_interval": {"seconds": 751, "nanos": 543},
        "next_sync_time": {
            "year": 433,
            "month": 550,
            "day": 318,
            "hours": 561,
            "minutes": 773,
            "seconds": 751,
            "nanos": 543,
            "utc_offset": {},
            "time_zone": {"id": "id_value", "version": "version_value"},
        },
        "entities": [
            {
                "params": {},
                "json_params": "json_params_value",
                "entity_name": "entity_name_value",
                "key_property_mappings": {},
                "data_store": "data_store_value",
                "starting_schema": {
                    "struct_schema": {},
                    "json_schema": "json_schema_value",
                    "name": "name_value",
                },
                "healthcare_fhir_config": {
                    "enable_configurable_schema": True,
                    "enable_static_indexing_for_batch_ingestion": True,
                    "initial_filter_groups": [
                        "initial_filter_groups_value1",
                        "initial_filter_groups_value2",
                    ],
                },
            }
        ],
        "create_time": {"seconds": 751, "nanos": 543},
        "latest_pause_time": {},
        "last_sync_time": {},
        "update_time": {},
        "errors": [
            {
                "code": 411,
                "message": "message_value",
                "details": [
                    {
                        "type_url": "type.googleapis.com/google.protobuf.Duration",
                        "value": b"\x08\x0c\x10\xdb\x07",
                    }
                ],
            }
        ],
        "sync_mode": 1,
        "kms_key_name": "kms_key_name_value",
        "destination_configs": [
            {
                "params": {},
                "json_params": "json_params_value",
                "key": "key_value",
                "destinations": [{"host": "host_value", "port": 453}],
            }
        ],
        "action_state": 1,
        "action_config": {
            "action_params": {},
            "json_action_params": "json_action_params_value",
            "is_action_configured": True,
            "service_name": "service_name_value",
            "use_static_secrets": True,
            "create_bap_connection": True,
            "user_defined_scopes_mapping": {},
        },
        "end_user_config": {
            "auth_params": {},
            "json_auth_params": "json_auth_params_value",
            "additional_params": {},
            "tenant": {
                "id": "id_value",
                "uri": "uri_value",
                "display_name": "display_name_value",
            },
        },
        "federated_config": {
            "auth_params": {},
            "json_auth_params": "json_auth_params_value",
            "additional_params": {},
        },
        "connector_modes": [1],
        "static_ip_enabled": True,
        "static_ip_addresses": [
            "static_ip_addresses_value1",
            "static_ip_addresses_value2",
        ],
        "oauth_static_ip_addresses": [
            "oauth_static_ip_addresses_value1",
            "oauth_static_ip_addresses_value2",
        ],
        "blocking_reasons": [1],
        "identity_schedule_config": {"refresh_interval": {}, "next_sync_time": {}},
        "private_connectivity_project_id": "private_connectivity_project_id_value",
        "bap_config": {
            "supported_connector_modes": [1],
            "enabled_actions": ["enabled_actions_value1", "enabled_actions_value2"],
            "toolspec_override": {"tools": {}, "base_version": "base_version_value"},
        },
        "connector_type": 1,
        "realtime_state": 1,
        "alert_policy_configs": [
            {
                "alert_policy_name": "alert_policy_name_value",
                "alert_enrollments": [
                    {"alert_id": "alert_id_value", "enroll_state": 1}
                ],
            }
        ],
        "realtime_sync_config": {
            "webhook_uri": "webhook_uri_value",
            "realtime_sync_secret": "realtime_sync_secret_value",
            "streaming_error": {"streaming_error_reason": 1, "error": {}},
        },
        "acl_enabled": True,
        "create_eua_saas": True,
        "auto_run_disabled": True,
        "incremental_sync_disabled": True,
        "incremental_refresh_interval": {},
        "hybrid_ingestion_disabled": True,
        "data_protection_policy": {
            "sensitive_data_protection_policy": {"policy": "policy_value"}
        },
        "egress_fqdns": ["egress_fqdns_value1", "egress_fqdns_value2"],
        "vpcsc_enabled": True,
        "dynamic_tools": [
            {
                "name": "name_value",
                "description": "description_value",
                "enabled": True,
                "display_name": "display_name_value",
            }
        ],
        "cli_config": {
            "enabled_actions": ["enabled_actions_value1", "enabled_actions_value2"]
        },
        "connector_source_id": "connector_source_id_value",
        "tag": "tag_value",
        "metadata": {
            "title": "title_value",
            "description": "description_value",
            "short_description": "short_description_value",
            "author": "author_value",
            "note": "note_value",
        },
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = data_connector_service.UpdateDataConnectorRequest.meta.fields[
        "data_connector"
    ]

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
    for field, value in request_init["data_connector"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["data_connector"][field])):
                    del request_init["data_connector"][field][i][subfield]
            else:
                del request_init["data_connector"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcd_data_connector.DataConnector(
            name="name_value",
            state=gcd_data_connector.DataConnector.State.CREATING,
            data_source="data_source_value",
            remove_param_keys=["remove_param_keys_value"],
            sync_mode=gcd_data_connector.DataConnector.SyncMode.STREAMING,
            kms_key_name="kms_key_name_value",
            action_state=gcd_data_connector.DataConnector.State.CREATING,
            connector_modes=[
                gcd_data_connector.DataConnector.ConnectorMode.DATA_INGESTION
            ],
            static_ip_enabled=True,
            static_ip_addresses=["static_ip_addresses_value"],
            oauth_static_ip_addresses=["oauth_static_ip_addresses_value"],
            blocking_reasons=[
                gcd_data_connector.DataConnector.BlockingReason.ALLOWLIST_STATIC_IP
            ],
            private_connectivity_project_id="private_connectivity_project_id_value",
            connector_type=gcd_data_connector.ConnectorType.THIRD_PARTY,
            realtime_state=gcd_data_connector.DataConnector.State.CREATING,
            acl_enabled=True,
            create_eua_saas=True,
            auto_run_disabled=True,
            incremental_sync_disabled=True,
            hybrid_ingestion_disabled=True,
            egress_fqdns=["egress_fqdns_value"],
            vpcsc_enabled=True,
            connector_source_id="connector_source_id_value",
            tag="tag_value",
            json_params="json_params_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gcd_data_connector.DataConnector.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_data_connector(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcd_data_connector.DataConnector)
    assert response.name == "name_value"
    assert response.state == gcd_data_connector.DataConnector.State.CREATING
    assert response.data_source == "data_source_value"
    assert response.remove_param_keys == ["remove_param_keys_value"]
    assert response.sync_mode == gcd_data_connector.DataConnector.SyncMode.STREAMING
    assert response.kms_key_name == "kms_key_name_value"
    assert response.action_state == gcd_data_connector.DataConnector.State.CREATING
    assert response.connector_modes == [
        gcd_data_connector.DataConnector.ConnectorMode.DATA_INGESTION
    ]
    assert response.static_ip_enabled is True
    assert response.static_ip_addresses == ["static_ip_addresses_value"]
    assert response.oauth_static_ip_addresses == ["oauth_static_ip_addresses_value"]
    assert response.blocking_reasons == [
        gcd_data_connector.DataConnector.BlockingReason.ALLOWLIST_STATIC_IP
    ]
    assert (
        response.private_connectivity_project_id
        == "private_connectivity_project_id_value"
    )
    assert response.connector_type == gcd_data_connector.ConnectorType.THIRD_PARTY
    assert response.realtime_state == gcd_data_connector.DataConnector.State.CREATING
    assert response.acl_enabled is True
    assert response.create_eua_saas is True
    assert response.auto_run_disabled is True
    assert response.incremental_sync_disabled is True
    assert response.hybrid_ingestion_disabled is True
    assert response.egress_fqdns == ["egress_fqdns_value"]
    assert response.vpcsc_enabled is True
    assert response.connector_source_id == "connector_source_id_value"
    assert response.tag == "tag_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_data_connector_rest_interceptors(null_interceptor):
    transport = transports.DataConnectorServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.DataConnectorServiceRestInterceptor(),
    )
    client = DataConnectorServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.DataConnectorServiceRestInterceptor, "post_update_data_connector"
        ) as post,
        mock.patch.object(
            transports.DataConnectorServiceRestInterceptor,
            "post_update_data_connector_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.DataConnectorServiceRestInterceptor, "pre_update_data_connector"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = data_connector_service.UpdateDataConnectorRequest.pb(
            data_connector_service.UpdateDataConnectorRequest()
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
        return_value = gcd_data_connector.DataConnector.to_json(
            gcd_data_connector.DataConnector()
        )
        req.return_value.content = return_value

        request = data_connector_service.UpdateDataConnectorRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gcd_data_connector.DataConnector()
        post_with_metadata.return_value = gcd_data_connector.DataConnector(), metadata

        client.update_data_connector(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_cancel_operation_rest_bad_request(
    request_type=operations_pb2.CancelOperationRequest,
):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict(
        {"name": "projects/sample1/operations/sample2"}, request
    )

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.cancel_operation(request)


@pytest.mark.parametrize(
    "request_type",
    [
        operations_pb2.CancelOperationRequest,
        dict,
    ],
)
def test_cancel_operation_rest(request_type):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {"name": "projects/sample1/operations/sample2"}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = "{}"
        response_value.content = json_return_value.encode("UTF-8")

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.cancel_operation(request)

    # Establish that the response is the type that we expect.
    assert response is None


def test_get_operation_rest_bad_request(
    request_type=operations_pb2.GetOperationRequest,
):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict(
        {"name": "projects/sample1/operations/sample2"}, request
    )

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_operation(request)


@pytest.mark.parametrize(
    "request_type",
    [
        operations_pb2.GetOperationRequest,
        dict,
    ],
)
def test_get_operation_rest(request_type):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {"name": "projects/sample1/operations/sample2"}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.get_operation(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.Operation)


def test_list_operations_rest_bad_request(
    request_type=operations_pb2.ListOperationsRequest,
):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict({"name": "projects/sample1"}, request)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list_operations(request)


@pytest.mark.parametrize(
    "request_type",
    [
        operations_pb2.ListOperationsRequest,
        dict,
    ],
)
def test_list_operations_rest(request_type):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {"name": "projects/sample1"}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.ListOperationsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.list_operations(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.ListOperationsResponse)


def test_initialize_client_w_rest():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_set_up_data_connector_empty_call_rest():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.set_up_data_connector), "__call__"
    ) as call:
        client.set_up_data_connector(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_connector_service.SetUpDataConnectorRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_data_connector_empty_call_rest():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_data_connector), "__call__"
    ) as call:
        client.get_data_connector(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_connector_service.GetDataConnectorRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_data_connector_empty_call_rest():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_connector), "__call__"
    ) as call:
        client.update_data_connector(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_connector_service.UpdateDataConnectorRequest()
        assert args[0] == request_msg


def test_data_connector_service_rest_lro_client():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    transport = client.transport

    # Ensure that we have an api-core operations client.
    assert isinstance(
        transport.operations_client,
        operations_v1.AbstractOperationsClient,
    )

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.DataConnectorServiceGrpcTransport,
    )


def test_data_connector_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.DataConnectorServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_data_connector_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.discoveryengine_v1.services.data_connector_service.transports.DataConnectorServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.DataConnectorServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "set_up_data_connector",
        "get_data_connector",
        "update_data_connector",
        "get_operation",
        "cancel_operation",
        "list_operations",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()

    # Additionally, the LRO client (a property) should
    # also raise NotImplementedError
    with pytest.raises(NotImplementedError):
        transport.operations_client

    # Catch all for all remaining methods and properties
    remainder = [
        "kind",
    ]
    for r in remainder:
        with pytest.raises(NotImplementedError):
            getattr(transport, r)()


def test_data_connector_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.cloud.discoveryengine_v1.services.data_connector_service.transports.DataConnectorServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.DataConnectorServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/discoveryengine.assist.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.serving.readwrite",
            ),
            quota_project_id="octopus",
        )


def test_data_connector_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.cloud.discoveryengine_v1.services.data_connector_service.transports.DataConnectorServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.DataConnectorServiceTransport()
        adc.assert_called_once()


def test_data_connector_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        DataConnectorServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/discoveryengine.assist.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.serving.readwrite",
            ),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.DataConnectorServiceGrpcTransport,
        transports.DataConnectorServiceGrpcAsyncIOTransport,
    ],
)
def test_data_connector_service_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/discoveryengine.assist.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.serving.readwrite",
            ),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.DataConnectorServiceGrpcTransport,
        transports.DataConnectorServiceGrpcAsyncIOTransport,
        transports.DataConnectorServiceRestTransport,
    ],
)
def test_data_connector_service_transport_auth_gdch_credentials(transport_class):
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
        (transports.DataConnectorServiceGrpcTransport, grpc_helpers),
        (transports.DataConnectorServiceGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_data_connector_service_transport_create_channel(transport_class, grpc_helpers):
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
            "discoveryengine.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/discoveryengine.assist.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.readwrite",
                "https://www.googleapis.com/auth/discoveryengine.serving.readwrite",
            ),
            scopes=["1", "2"],
            default_host="discoveryengine.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.DataConnectorServiceGrpcTransport,
        transports.DataConnectorServiceGrpcAsyncIOTransport,
    ],
)
def test_data_connector_service_grpc_transport_client_cert_source_for_mtls(
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


def test_data_connector_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.DataConnectorServiceRestTransport(
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
def test_data_connector_service_host_no_port(transport_name):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="discoveryengine.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "discoveryengine.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://discoveryengine.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_data_connector_service_host_with_port(transport_name):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="discoveryengine.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "discoveryengine.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://discoveryengine.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_data_connector_service_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = DataConnectorServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = DataConnectorServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.set_up_data_connector._session
    session2 = client2.transport.set_up_data_connector._session
    assert session1 != session2
    session1 = client1.transport.get_data_connector._session
    session2 = client2.transport.get_data_connector._session
    assert session1 != session2
    session1 = client1.transport.update_data_connector._session
    session2 = client2.transport.update_data_connector._session
    assert session1 != session2


def test_data_connector_service_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.DataConnectorServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_data_connector_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.DataConnectorServiceGrpcAsyncIOTransport(
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
        transports.DataConnectorServiceGrpcTransport,
        transports.DataConnectorServiceGrpcAsyncIOTransport,
    ],
)
def test_data_connector_service_transport_channel_mtls_with_client_cert_source(
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
        transports.DataConnectorServiceGrpcTransport,
        transports.DataConnectorServiceGrpcAsyncIOTransport,
    ],
)
def test_data_connector_service_transport_channel_mtls_with_adc(transport_class):
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


def test_data_connector_service_grpc_lro_client():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )
    transport = client.transport

    # Ensure that we have a api-core operations client.
    assert isinstance(
        transport.operations_client,
        operations_v1.OperationsClient,
    )

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_data_connector_service_grpc_lro_async_client():
    client = DataConnectorServiceAsyncClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc_asyncio",
    )
    transport = client.transport

    # Ensure that we have a api-core operations client.
    assert isinstance(
        transport.operations_client,
        operations_v1.OperationsAsyncClient,
    )

    # Ensure that subsequent calls to the property send the exact same object.
    assert transport.operations_client is transport.operations_client


def test_content_policy_path():
    organization = "squid"
    location = "clam"
    content_policy = "whelk"
    expected = "organizations/{organization}/locations/{location}/contentPolicies/{content_policy}".format(
        organization=organization,
        location=location,
        content_policy=content_policy,
    )
    actual = DataConnectorServiceClient.content_policy_path(
        organization, location, content_policy
    )
    assert expected == actual


def test_parse_content_policy_path():
    expected = {
        "organization": "octopus",
        "location": "oyster",
        "content_policy": "nudibranch",
    }
    path = DataConnectorServiceClient.content_policy_path(**expected)

    # Check that the path construction is reversible.
    actual = DataConnectorServiceClient.parse_content_policy_path(path)
    assert expected == actual


def test_data_connector_path():
    project = "cuttlefish"
    location = "mussel"
    collection = "winkle"
    expected = "projects/{project}/locations/{location}/collections/{collection}/dataConnector".format(
        project=project,
        location=location,
        collection=collection,
    )
    actual = DataConnectorServiceClient.data_connector_path(
        project, location, collection
    )
    assert expected == actual


def test_parse_data_connector_path():
    expected = {
        "project": "nautilus",
        "location": "scallop",
        "collection": "abalone",
    }
    path = DataConnectorServiceClient.data_connector_path(**expected)

    # Check that the path construction is reversible.
    actual = DataConnectorServiceClient.parse_data_connector_path(path)
    assert expected == actual


def test_data_store_path():
    project = "squid"
    location = "clam"
    data_store = "whelk"
    expected = "projects/{project}/locations/{location}/dataStores/{data_store}".format(
        project=project,
        location=location,
        data_store=data_store,
    )
    actual = DataConnectorServiceClient.data_store_path(project, location, data_store)
    assert expected == actual


def test_parse_data_store_path():
    expected = {
        "project": "octopus",
        "location": "oyster",
        "data_store": "nudibranch",
    }
    path = DataConnectorServiceClient.data_store_path(**expected)

    # Check that the path construction is reversible.
    actual = DataConnectorServiceClient.parse_data_store_path(path)
    assert expected == actual


def test_location_path():
    project = "cuttlefish"
    location = "mussel"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = DataConnectorServiceClient.location_path(project, location)
    assert expected == actual


def test_parse_location_path():
    expected = {
        "project": "winkle",
        "location": "nautilus",
    }
    path = DataConnectorServiceClient.location_path(**expected)

    # Check that the path construction is reversible.
    actual = DataConnectorServiceClient.parse_location_path(path)
    assert expected == actual


def test_schema_path():
    project = "scallop"
    location = "abalone"
    data_store = "squid"
    schema = "clam"
    expected = "projects/{project}/locations/{location}/dataStores/{data_store}/schemas/{schema}".format(
        project=project,
        location=location,
        data_store=data_store,
        schema=schema,
    )
    actual = DataConnectorServiceClient.schema_path(
        project, location, data_store, schema
    )
    assert expected == actual


def test_parse_schema_path():
    expected = {
        "project": "whelk",
        "location": "octopus",
        "data_store": "oyster",
        "schema": "nudibranch",
    }
    path = DataConnectorServiceClient.schema_path(**expected)

    # Check that the path construction is reversible.
    actual = DataConnectorServiceClient.parse_schema_path(path)
    assert expected == actual


def test_service_path():
    project = "cuttlefish"
    location = "mussel"
    namespace = "winkle"
    service = "nautilus"
    expected = "projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}".format(
        project=project,
        location=location,
        namespace=namespace,
        service=service,
    )
    actual = DataConnectorServiceClient.service_path(
        project, location, namespace, service
    )
    assert expected == actual


def test_parse_service_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
        "namespace": "squid",
        "service": "clam",
    }
    path = DataConnectorServiceClient.service_path(**expected)

    # Check that the path construction is reversible.
    actual = DataConnectorServiceClient.parse_service_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "whelk"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = DataConnectorServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "octopus",
    }
    path = DataConnectorServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = DataConnectorServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "oyster"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = DataConnectorServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "nudibranch",
    }
    path = DataConnectorServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = DataConnectorServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "cuttlefish"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = DataConnectorServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "mussel",
    }
    path = DataConnectorServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = DataConnectorServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "winkle"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = DataConnectorServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "nautilus",
    }
    path = DataConnectorServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = DataConnectorServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "scallop"
    location = "abalone"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = DataConnectorServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "squid",
        "location": "clam",
    }
    path = DataConnectorServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = DataConnectorServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.DataConnectorServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = DataConnectorServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.DataConnectorServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = DataConnectorServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_cancel_operation(transport: str = "grpc"):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
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
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.CancelOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.cancel_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_cancel_operation_field_headers():
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.CancelOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        call.return_value = None

        client.cancel_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_cancel_operation_field_headers_async():
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.CancelOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.cancel_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


def test_cancel_operation_from_dict():
    client = DataConnectorServiceClient(
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
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.cancel_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_cancel_operation_flattened():
    client = DataConnectorServiceClient(
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
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.cancel_operation()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == operations_pb2.CancelOperationRequest()


def test_get_operation(transport: str = "grpc"):
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
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
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
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
    client = DataConnectorServiceClient(
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
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_operation_field_headers_async():
    client = DataConnectorServiceAsyncClient(
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
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


def test_get_operation_from_dict():
    client = DataConnectorServiceClient(
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
    client = DataConnectorServiceAsyncClient(
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
    client = DataConnectorServiceClient(
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
    client = DataConnectorServiceAsyncClient(
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
    client = DataConnectorServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
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
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
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
    client = DataConnectorServiceClient(
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
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_operations_field_headers_async():
    client = DataConnectorServiceAsyncClient(
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
    assert (
        "x-goog-request-params",
        "name=locations",
    ) in kw["metadata"]


def test_list_operations_from_dict():
    client = DataConnectorServiceClient(
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
    client = DataConnectorServiceAsyncClient(
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
    client = DataConnectorServiceClient(
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
    client = DataConnectorServiceAsyncClient(
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


def test_transport_close_grpc():
    client = DataConnectorServiceClient(
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
    client = DataConnectorServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = DataConnectorServiceClient(
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
        client = DataConnectorServiceClient(
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
        (DataConnectorServiceClient, transports.DataConnectorServiceGrpcTransport),
        (
            DataConnectorServiceAsyncClient,
            transports.DataConnectorServiceGrpcAsyncIOTransport,
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
