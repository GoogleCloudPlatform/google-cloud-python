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
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
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
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account

from google.devicesandservices.health_v4.services.data_points_service import (
    DataPointsServiceAsyncClient,
    DataPointsServiceClient,
    pagers,
    transports,
)
from google.devicesandservices.health_v4.types import (
    data_coordinates,
    data_model,
    data_points,
    data_source,
    medical_device_info,
)

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

    assert DataPointsServiceClient._get_client_cert_source(None, False) is None
    assert (
        DataPointsServiceClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        DataPointsServiceClient._get_client_cert_source(mock_provided_cert_source, True)
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
                DataPointsServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                DataPointsServiceClient._get_client_cert_source(
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
    client = DataPointsServiceClient(credentials=cred)
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
    client = DataPointsServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (DataPointsServiceClient, "grpc"),
        (DataPointsServiceAsyncClient, "grpc_asyncio"),
        (DataPointsServiceClient, "rest"),
    ],
)
def test_data_points_service_client_from_service_account_info(
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
        (transports.DataPointsServiceGrpcTransport, "grpc"),
        (transports.DataPointsServiceGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.DataPointsServiceRestTransport, "rest"),
    ],
)
def test_data_points_service_client_service_account_always_use_jwt(
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
        (DataPointsServiceClient, "grpc"),
        (DataPointsServiceAsyncClient, "grpc_asyncio"),
        (DataPointsServiceClient, "rest"),
    ],
)
def test_data_points_service_client_from_service_account_file(
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


def test_data_points_service_client_get_transport_class():
    transport = DataPointsServiceClient.get_transport_class()
    available_transports = [
        transports.DataPointsServiceGrpcTransport,
        transports.DataPointsServiceRestTransport,
    ]
    assert transport in available_transports

    transport = DataPointsServiceClient.get_transport_class("grpc")
    assert transport == transports.DataPointsServiceGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (DataPointsServiceClient, transports.DataPointsServiceGrpcTransport, "grpc"),
        (
            DataPointsServiceAsyncClient,
            transports.DataPointsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (DataPointsServiceClient, transports.DataPointsServiceRestTransport, "rest"),
    ],
)
@mock.patch.object(
    DataPointsServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(DataPointsServiceClient),
)
@mock.patch.object(
    DataPointsServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(DataPointsServiceAsyncClient),
)
def test_data_points_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(DataPointsServiceClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(DataPointsServiceClient, "get_transport_class") as gtc:
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
            DataPointsServiceClient,
            transports.DataPointsServiceGrpcTransport,
            "grpc",
            "true",
        ),
        (
            DataPointsServiceAsyncClient,
            transports.DataPointsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            DataPointsServiceClient,
            transports.DataPointsServiceGrpcTransport,
            "grpc",
            "false",
        ),
        (
            DataPointsServiceAsyncClient,
            transports.DataPointsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (
            DataPointsServiceClient,
            transports.DataPointsServiceRestTransport,
            "rest",
            "true",
        ),
        (
            DataPointsServiceClient,
            transports.DataPointsServiceRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    DataPointsServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(DataPointsServiceClient),
)
@mock.patch.object(
    DataPointsServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(DataPointsServiceAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_data_points_service_client_mtls_env_auto(
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
    "client_class", [DataPointsServiceClient, DataPointsServiceAsyncClient]
)
@mock.patch.object(
    DataPointsServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(DataPointsServiceClient),
)
@mock.patch.object(
    DataPointsServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(DataPointsServiceAsyncClient),
)
def test_data_points_service_client_get_mtls_endpoint_and_cert_source(client_class):
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
    "client_class", [DataPointsServiceClient, DataPointsServiceAsyncClient]
)
@mock.patch.object(
    DataPointsServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(DataPointsServiceClient),
)
@mock.patch.object(
    DataPointsServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(DataPointsServiceAsyncClient),
)
def test_data_points_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = DataPointsServiceClient._DEFAULT_UNIVERSE
    default_endpoint = DataPointsServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = DataPointsServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
        (DataPointsServiceClient, transports.DataPointsServiceGrpcTransport, "grpc"),
        (
            DataPointsServiceAsyncClient,
            transports.DataPointsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (DataPointsServiceClient, transports.DataPointsServiceRestTransport, "rest"),
    ],
)
def test_data_points_service_client_client_options_scopes(
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
            DataPointsServiceClient,
            transports.DataPointsServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            DataPointsServiceAsyncClient,
            transports.DataPointsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (
            DataPointsServiceClient,
            transports.DataPointsServiceRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_data_points_service_client_client_options_credentials_file(
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


def test_data_points_service_client_client_options_from_dict():
    with mock.patch(
        "google.devicesandservices.health_v4.services.data_points_service.transports.DataPointsServiceGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = DataPointsServiceClient(
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
            DataPointsServiceClient,
            transports.DataPointsServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            DataPointsServiceAsyncClient,
            transports.DataPointsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_data_points_service_client_create_channel_credentials_file(
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
                "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.writeonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.readonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.writeonly",
                "https://www.googleapis.com/auth/googlehealth.location.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.writeonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.readonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.writeonly",
                "https://www.googleapis.com/auth/googlehealth.nutrition.writeonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.readonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.writeonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.readonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.writeonly",
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
        data_points.GetDataPointRequest(),
        {},
    ],
)
def test_get_data_point(request_type, transport: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_data_point), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_points.DataPoint(
            name="name_value",
        )
        response = client.get_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = data_points.GetDataPointRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, data_points.DataPoint)
    assert response.name == "name_value"


def test_get_data_point_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = data_points.GetDataPointRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_data_point), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_data_point(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.GetDataPointRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_data_point_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_data_point in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_data_point] = mock_rpc
        request = {}
        client.get_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_data_point(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_data_point_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = DataPointsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_data_point
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_data_point
        ] = mock_rpc

        request = {}
        await client.get_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_data_point(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        data_points.GetDataPointRequest(),
        {},
    ],
)
async def test_get_data_point_async(request_type, transport: str = "grpc_asyncio"):
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_data_point), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.DataPoint(
                name="name_value",
            )
        )
        response = await client.get_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = data_points.GetDataPointRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, data_points.DataPoint)
    assert response.name == "name_value"


def test_get_data_point_field_headers():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.GetDataPointRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_data_point), "__call__") as call:
        call.return_value = data_points.DataPoint()
        client.get_data_point(request)

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
async def test_get_data_point_field_headers_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.GetDataPointRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_data_point), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.DataPoint()
        )
        await client.get_data_point(request)

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


def test_get_data_point_flattened():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_data_point), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_points.DataPoint()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_data_point(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_data_point_flattened_error():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_data_point(
            data_points.GetDataPointRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_data_point_flattened_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_data_point), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_points.DataPoint()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.DataPoint()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_data_point(
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
async def test_get_data_point_flattened_error_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_data_point(
            data_points.GetDataPointRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.ListDataPointsRequest(),
        {},
    ],
)
def test_list_data_points(request_type, transport: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_data_points), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_points.ListDataPointsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = data_points.ListDataPointsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListDataPointsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_data_points_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = data_points.ListDataPointsRequest(
        parent="parent_value",
        page_token="page_token_value",
        filter="filter_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_data_points), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_data_points(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.ListDataPointsRequest(
            parent="parent_value",
            page_token="page_token_value",
            filter="filter_value",
        )
        assert args[0] == request_msg


def test_list_data_points_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_data_points in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_data_points] = (
            mock_rpc
        )
        request = {}
        client.list_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_data_points_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = DataPointsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_data_points
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_data_points
        ] = mock_rpc

        request = {}
        await client.list_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        data_points.ListDataPointsRequest(),
        {},
    ],
)
async def test_list_data_points_async(request_type, transport: str = "grpc_asyncio"):
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_data_points), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.ListDataPointsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = data_points.ListDataPointsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListDataPointsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_data_points_field_headers():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.ListDataPointsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_data_points), "__call__") as call:
        call.return_value = data_points.ListDataPointsResponse()
        client.list_data_points(request)

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
async def test_list_data_points_field_headers_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.ListDataPointsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_data_points), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.ListDataPointsResponse()
        )
        await client.list_data_points(request)

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


def test_list_data_points_flattened():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_data_points), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_points.ListDataPointsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_data_points(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_data_points_flattened_error():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_data_points(
            data_points.ListDataPointsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_data_points_flattened_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_data_points), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_points.ListDataPointsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.ListDataPointsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_data_points(
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
async def test_list_data_points_flattened_error_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_data_points(
            data_points.ListDataPointsRequest(),
            parent="parent_value",
        )


def test_list_data_points_pager(transport_name: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_data_points), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                    data_points.DataPoint(),
                    data_points.DataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.ListDataPointsResponse(
                data_points=[],
                next_page_token="def",
            ),
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                    data_points.DataPoint(),
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
        pager = client.list_data_points(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, data_points.DataPoint) for i in results)


def test_list_data_points_pages(transport_name: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_data_points), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                    data_points.DataPoint(),
                    data_points.DataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.ListDataPointsResponse(
                data_points=[],
                next_page_token="def",
            ),
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                    data_points.DataPoint(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_data_points(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_data_points_async_pager():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_data_points), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                    data_points.DataPoint(),
                    data_points.DataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.ListDataPointsResponse(
                data_points=[],
                next_page_token="def",
            ),
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                    data_points.DataPoint(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_data_points(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, data_points.DataPoint) for i in responses)


@pytest.mark.asyncio
async def test_list_data_points_async_pages():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_data_points), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                    data_points.DataPoint(),
                    data_points.DataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.ListDataPointsResponse(
                data_points=[],
                next_page_token="def",
            ),
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                    data_points.DataPoint(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_data_points(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.CreateDataPointRequest(),
        {},
    ],
)
def test_create_data_point(request_type, transport: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_data_point), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.create_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = data_points.CreateDataPointRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_data_point_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = data_points.CreateDataPointRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_data_point), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_data_point(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.CreateDataPointRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_create_data_point_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_data_point in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_data_point] = (
            mock_rpc
        )
        request = {}
        client.create_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.create_data_point(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_data_point_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = DataPointsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_data_point
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_data_point
        ] = mock_rpc

        request = {}
        await client.create_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.create_data_point(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        data_points.CreateDataPointRequest(),
        {},
    ],
)
async def test_create_data_point_async(request_type, transport: str = "grpc_asyncio"):
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_data_point), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.create_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = data_points.CreateDataPointRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_data_point_field_headers():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.CreateDataPointRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_data_point), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_data_point(request)

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
async def test_create_data_point_field_headers_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.CreateDataPointRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_data_point), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.create_data_point(request)

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


def test_create_data_point_flattened():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_data_point), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_data_point(
            parent="parent_value",
            data_point=data_points.DataPoint(
                steps=data_model.Steps(
                    interval=data_coordinates.ObservationTimeInterval(
                        start_time=timestamp_pb2.Timestamp(seconds=751)
                    )
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
        arg = args[0].data_point
        mock_val = data_points.DataPoint(
            steps=data_model.Steps(
                interval=data_coordinates.ObservationTimeInterval(
                    start_time=timestamp_pb2.Timestamp(seconds=751)
                )
            )
        )
        assert arg == mock_val


def test_create_data_point_flattened_error():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_data_point(
            data_points.CreateDataPointRequest(),
            parent="parent_value",
            data_point=data_points.DataPoint(
                steps=data_model.Steps(
                    interval=data_coordinates.ObservationTimeInterval(
                        start_time=timestamp_pb2.Timestamp(seconds=751)
                    )
                )
            ),
        )


@pytest.mark.asyncio
async def test_create_data_point_flattened_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_data_point), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_data_point(
            parent="parent_value",
            data_point=data_points.DataPoint(
                steps=data_model.Steps(
                    interval=data_coordinates.ObservationTimeInterval(
                        start_time=timestamp_pb2.Timestamp(seconds=751)
                    )
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
        arg = args[0].data_point
        mock_val = data_points.DataPoint(
            steps=data_model.Steps(
                interval=data_coordinates.ObservationTimeInterval(
                    start_time=timestamp_pb2.Timestamp(seconds=751)
                )
            )
        )
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_data_point_flattened_error_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_data_point(
            data_points.CreateDataPointRequest(),
            parent="parent_value",
            data_point=data_points.DataPoint(
                steps=data_model.Steps(
                    interval=data_coordinates.ObservationTimeInterval(
                        start_time=timestamp_pb2.Timestamp(seconds=751)
                    )
                )
            ),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.UpdateDataPointRequest(),
        {},
    ],
)
def test_update_data_point(request_type, transport: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_point), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.update_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = data_points.UpdateDataPointRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_data_point_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = data_points.UpdateDataPointRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_point), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_data_point(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.UpdateDataPointRequest()
        assert args[0] == request_msg


def test_update_data_point_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_data_point in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_data_point] = (
            mock_rpc
        )
        request = {}
        client.update_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.update_data_point(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_data_point_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = DataPointsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_data_point
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_data_point
        ] = mock_rpc

        request = {}
        await client.update_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.update_data_point(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        data_points.UpdateDataPointRequest(),
        {},
    ],
)
async def test_update_data_point_async(request_type, transport: str = "grpc_asyncio"):
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_point), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.update_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = data_points.UpdateDataPointRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_data_point_field_headers():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.UpdateDataPointRequest()

    request.data_point.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_point), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.update_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "data_point.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_data_point_field_headers_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.UpdateDataPointRequest()

    request.data_point.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_point), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.update_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "data_point.name=name_value",
    ) in kw["metadata"]


def test_update_data_point_flattened():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_point), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_data_point(
            data_point=data_points.DataPoint(
                steps=data_model.Steps(
                    interval=data_coordinates.ObservationTimeInterval(
                        start_time=timestamp_pb2.Timestamp(seconds=751)
                    )
                )
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].data_point
        mock_val = data_points.DataPoint(
            steps=data_model.Steps(
                interval=data_coordinates.ObservationTimeInterval(
                    start_time=timestamp_pb2.Timestamp(seconds=751)
                )
            )
        )
        assert arg == mock_val


def test_update_data_point_flattened_error():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_data_point(
            data_points.UpdateDataPointRequest(),
            data_point=data_points.DataPoint(
                steps=data_model.Steps(
                    interval=data_coordinates.ObservationTimeInterval(
                        start_time=timestamp_pb2.Timestamp(seconds=751)
                    )
                )
            ),
        )


@pytest.mark.asyncio
async def test_update_data_point_flattened_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_point), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_data_point(
            data_point=data_points.DataPoint(
                steps=data_model.Steps(
                    interval=data_coordinates.ObservationTimeInterval(
                        start_time=timestamp_pb2.Timestamp(seconds=751)
                    )
                )
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].data_point
        mock_val = data_points.DataPoint(
            steps=data_model.Steps(
                interval=data_coordinates.ObservationTimeInterval(
                    start_time=timestamp_pb2.Timestamp(seconds=751)
                )
            )
        )
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_data_point_flattened_error_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_data_point(
            data_points.UpdateDataPointRequest(),
            data_point=data_points.DataPoint(
                steps=data_model.Steps(
                    interval=data_coordinates.ObservationTimeInterval(
                        start_time=timestamp_pb2.Timestamp(seconds=751)
                    )
                )
            ),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.BatchDeleteDataPointsRequest(),
        {},
    ],
)
def test_batch_delete_data_points(request_type, transport: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_delete_data_points), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.batch_delete_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = data_points.BatchDeleteDataPointsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_batch_delete_data_points_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = data_points.BatchDeleteDataPointsRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_delete_data_points), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.batch_delete_data_points(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.BatchDeleteDataPointsRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_batch_delete_data_points_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_delete_data_points
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_delete_data_points
        ] = mock_rpc
        request = {}
        client.batch_delete_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.batch_delete_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_batch_delete_data_points_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = DataPointsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.batch_delete_data_points
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.batch_delete_data_points
        ] = mock_rpc

        request = {}
        await client.batch_delete_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.batch_delete_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        data_points.BatchDeleteDataPointsRequest(),
        {},
    ],
)
async def test_batch_delete_data_points_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_delete_data_points), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.batch_delete_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = data_points.BatchDeleteDataPointsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_batch_delete_data_points_field_headers():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.BatchDeleteDataPointsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_delete_data_points), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.batch_delete_data_points(request)

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
async def test_batch_delete_data_points_field_headers_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.BatchDeleteDataPointsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_delete_data_points), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.batch_delete_data_points(request)

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


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.ReconcileDataPointsRequest(),
        {},
    ],
)
def test_reconcile_data_points(request_type, transport: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reconcile_data_points), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_points.ReconcileDataPointsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.reconcile_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = data_points.ReconcileDataPointsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ReconcileDataPointsPager)
    assert response.next_page_token == "next_page_token_value"


def test_reconcile_data_points_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = data_points.ReconcileDataPointsRequest(
        parent="parent_value",
        page_token="page_token_value",
        filter="filter_value",
        data_source_family="data_source_family_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reconcile_data_points), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.reconcile_data_points(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.ReconcileDataPointsRequest(
            parent="parent_value",
            page_token="page_token_value",
            filter="filter_value",
            data_source_family="data_source_family_value",
        )
        assert args[0] == request_msg


def test_reconcile_data_points_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.reconcile_data_points
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.reconcile_data_points] = (
            mock_rpc
        )
        request = {}
        client.reconcile_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.reconcile_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_reconcile_data_points_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = DataPointsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.reconcile_data_points
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.reconcile_data_points
        ] = mock_rpc

        request = {}
        await client.reconcile_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.reconcile_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        data_points.ReconcileDataPointsRequest(),
        {},
    ],
)
async def test_reconcile_data_points_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reconcile_data_points), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.ReconcileDataPointsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.reconcile_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = data_points.ReconcileDataPointsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ReconcileDataPointsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_reconcile_data_points_field_headers():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.ReconcileDataPointsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reconcile_data_points), "__call__"
    ) as call:
        call.return_value = data_points.ReconcileDataPointsResponse()
        client.reconcile_data_points(request)

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
async def test_reconcile_data_points_field_headers_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.ReconcileDataPointsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reconcile_data_points), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.ReconcileDataPointsResponse()
        )
        await client.reconcile_data_points(request)

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


def test_reconcile_data_points_pager(transport_name: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reconcile_data_points), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[],
                next_page_token="def",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
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
        pager = client.reconcile_data_points(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, data_points.ReconciledDataPoint) for i in results)


def test_reconcile_data_points_pages(transport_name: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reconcile_data_points), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[],
                next_page_token="def",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.reconcile_data_points(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_reconcile_data_points_async_pager():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reconcile_data_points),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[],
                next_page_token="def",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.reconcile_data_points(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, data_points.ReconciledDataPoint) for i in responses)


@pytest.mark.asyncio
async def test_reconcile_data_points_async_pages():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reconcile_data_points),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[],
                next_page_token="def",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.reconcile_data_points(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.RollUpDataPointsRequest(),
        {},
    ],
)
def test_roll_up_data_points(request_type, transport: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.roll_up_data_points), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_points.RollUpDataPointsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.roll_up_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = data_points.RollUpDataPointsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.RollUpDataPointsPager)
    assert response.next_page_token == "next_page_token_value"


def test_roll_up_data_points_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = data_points.RollUpDataPointsRequest(
        parent="parent_value",
        page_token="page_token_value",
        data_source_family="data_source_family_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.roll_up_data_points), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.roll_up_data_points(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.RollUpDataPointsRequest(
            parent="parent_value",
            page_token="page_token_value",
            data_source_family="data_source_family_value",
        )
        assert args[0] == request_msg


def test_roll_up_data_points_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.roll_up_data_points in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.roll_up_data_points] = (
            mock_rpc
        )
        request = {}
        client.roll_up_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.roll_up_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_roll_up_data_points_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = DataPointsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.roll_up_data_points
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.roll_up_data_points
        ] = mock_rpc

        request = {}
        await client.roll_up_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.roll_up_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        data_points.RollUpDataPointsRequest(),
        {},
    ],
)
async def test_roll_up_data_points_async(request_type, transport: str = "grpc_asyncio"):
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.roll_up_data_points), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.RollUpDataPointsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.roll_up_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = data_points.RollUpDataPointsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.RollUpDataPointsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_roll_up_data_points_field_headers():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.RollUpDataPointsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.roll_up_data_points), "__call__"
    ) as call:
        call.return_value = data_points.RollUpDataPointsResponse()
        client.roll_up_data_points(request)

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
async def test_roll_up_data_points_field_headers_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.RollUpDataPointsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.roll_up_data_points), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.RollUpDataPointsResponse()
        )
        await client.roll_up_data_points(request)

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


def test_roll_up_data_points_pager(transport_name: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.roll_up_data_points), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[],
                next_page_token="def",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
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
        pager = client.roll_up_data_points(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, data_points.RollupDataPoint) for i in results)


def test_roll_up_data_points_pages(transport_name: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.roll_up_data_points), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[],
                next_page_token="def",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.roll_up_data_points(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_roll_up_data_points_async_pager():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.roll_up_data_points),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[],
                next_page_token="def",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.roll_up_data_points(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, data_points.RollupDataPoint) for i in responses)


@pytest.mark.asyncio
async def test_roll_up_data_points_async_pages():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.roll_up_data_points),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[],
                next_page_token="def",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.roll_up_data_points(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.DailyRollUpDataPointsRequest(),
        {},
    ],
)
def test_daily_roll_up_data_points(request_type, transport: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.daily_roll_up_data_points), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_points.DailyRollUpDataPointsResponse()
        response = client.daily_roll_up_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = data_points.DailyRollUpDataPointsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, data_points.DailyRollUpDataPointsResponse)


def test_daily_roll_up_data_points_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = data_points.DailyRollUpDataPointsRequest(
        parent="parent_value",
        page_token="page_token_value",
        data_source_family="data_source_family_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.daily_roll_up_data_points), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.daily_roll_up_data_points(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.DailyRollUpDataPointsRequest(
            parent="parent_value",
            page_token="page_token_value",
            data_source_family="data_source_family_value",
        )
        assert args[0] == request_msg


def test_daily_roll_up_data_points_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.daily_roll_up_data_points
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.daily_roll_up_data_points
        ] = mock_rpc
        request = {}
        client.daily_roll_up_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.daily_roll_up_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_daily_roll_up_data_points_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = DataPointsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.daily_roll_up_data_points
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.daily_roll_up_data_points
        ] = mock_rpc

        request = {}
        await client.daily_roll_up_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.daily_roll_up_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        data_points.DailyRollUpDataPointsRequest(),
        {},
    ],
)
async def test_daily_roll_up_data_points_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.daily_roll_up_data_points), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.DailyRollUpDataPointsResponse()
        )
        response = await client.daily_roll_up_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = data_points.DailyRollUpDataPointsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, data_points.DailyRollUpDataPointsResponse)


def test_daily_roll_up_data_points_field_headers():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.DailyRollUpDataPointsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.daily_roll_up_data_points), "__call__"
    ) as call:
        call.return_value = data_points.DailyRollUpDataPointsResponse()
        client.daily_roll_up_data_points(request)

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
async def test_daily_roll_up_data_points_field_headers_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.DailyRollUpDataPointsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.daily_roll_up_data_points), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.DailyRollUpDataPointsResponse()
        )
        await client.daily_roll_up_data_points(request)

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


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.ExportExerciseTcxRequest(),
        {},
    ],
)
def test_export_exercise_tcx(request_type, transport: str = "grpc"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.export_exercise_tcx), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_points.ExportExerciseTcxResponse(
            tcx_data="tcx_data_value",
        )
        response = client.export_exercise_tcx(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = data_points.ExportExerciseTcxRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, data_points.ExportExerciseTcxResponse)
    assert response.tcx_data == "tcx_data_value"


def test_export_exercise_tcx_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = data_points.ExportExerciseTcxRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.export_exercise_tcx), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.export_exercise_tcx(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.ExportExerciseTcxRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_export_exercise_tcx_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.export_exercise_tcx in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.export_exercise_tcx] = (
            mock_rpc
        )
        request = {}
        client.export_exercise_tcx(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.export_exercise_tcx(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_export_exercise_tcx_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = DataPointsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.export_exercise_tcx
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.export_exercise_tcx
        ] = mock_rpc

        request = {}
        await client.export_exercise_tcx(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.export_exercise_tcx(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        data_points.ExportExerciseTcxRequest(),
        {},
    ],
)
async def test_export_exercise_tcx_async(request_type, transport: str = "grpc_asyncio"):
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.export_exercise_tcx), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.ExportExerciseTcxResponse(
                tcx_data="tcx_data_value",
            )
        )
        response = await client.export_exercise_tcx(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = data_points.ExportExerciseTcxRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, data_points.ExportExerciseTcxResponse)
    assert response.tcx_data == "tcx_data_value"


def test_export_exercise_tcx_field_headers():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.ExportExerciseTcxRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.export_exercise_tcx), "__call__"
    ) as call:
        call.return_value = data_points.ExportExerciseTcxResponse()
        client.export_exercise_tcx(request)

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
async def test_export_exercise_tcx_field_headers_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = data_points.ExportExerciseTcxRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.export_exercise_tcx), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.ExportExerciseTcxResponse()
        )
        await client.export_exercise_tcx(request)

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


def test_export_exercise_tcx_flattened():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.export_exercise_tcx), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_points.ExportExerciseTcxResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.export_exercise_tcx(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_export_exercise_tcx_flattened_error():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.export_exercise_tcx(
            data_points.ExportExerciseTcxRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_export_exercise_tcx_flattened_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.export_exercise_tcx), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = data_points.ExportExerciseTcxResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.ExportExerciseTcxResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.export_exercise_tcx(
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
async def test_export_exercise_tcx_flattened_error_async():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.export_exercise_tcx(
            data_points.ExportExerciseTcxRequest(),
            name="name_value",
        )


def test_get_data_point_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_data_point in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_data_point] = mock_rpc

        request = {}
        client.get_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_data_point(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_data_point_rest_required_fields(
    request_type=data_points.GetDataPointRequest,
):
    transport_class = transports.DataPointsServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetDataPoint,
        "_BaseGetDataPoint__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = data_points.DataPoint()
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
            return_value = data_points.DataPoint.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_data_point(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_data_point_rest_flattened():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = data_points.DataPoint()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "users/sample1/dataTypes/sample2/dataPoints/sample3"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = data_points.DataPoint.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_data_point(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v4/{name=users/*/dataTypes/*/dataPoints/*}" % client.transport._host,
            args[1],
        )


def test_get_data_point_rest_flattened_error(transport: str = "rest"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_data_point(
            data_points.GetDataPointRequest(),
            name="name_value",
        )


def test_list_data_points_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_data_points in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_data_points] = (
            mock_rpc
        )

        request = {}
        client.list_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_data_points_rest_required_fields(
    request_type=data_points.ListDataPointsRequest,
):
    transport_class = transports.DataPointsServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListDataPoints,
        "_BaseListDataPoints__REQUIRED_FIELDS_DEFAULT_VALUES",
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
            "filter",
            "pageSize",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = data_points.ListDataPointsResponse()
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
            return_value = data_points.ListDataPointsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_data_points(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_data_points_rest_flattened():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = data_points.ListDataPointsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "users/sample1/dataTypes/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = data_points.ListDataPointsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_data_points(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v4/{parent=users/*/dataTypes/*}/dataPoints" % client.transport._host,
            args[1],
        )


def test_list_data_points_rest_flattened_error(transport: str = "rest"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_data_points(
            data_points.ListDataPointsRequest(),
            parent="parent_value",
        )


def test_list_data_points_rest_pager(transport: str = "rest"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                    data_points.DataPoint(),
                    data_points.DataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.ListDataPointsResponse(
                data_points=[],
                next_page_token="def",
            ),
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.ListDataPointsResponse(
                data_points=[
                    data_points.DataPoint(),
                    data_points.DataPoint(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            data_points.ListDataPointsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "users/sample1/dataTypes/sample2"}

        pager = client.list_data_points(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, data_points.DataPoint) for i in results)

        pages = list(client.list_data_points(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_create_data_point_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_data_point in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_data_point] = (
            mock_rpc
        )

        request = {}
        client.create_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.create_data_point(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_data_point_rest_required_fields(
    request_type=data_points.CreateDataPointRequest,
):
    transport_class = transports.DataPointsServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateDataPoint,
        "_BaseCreateDataPoint__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = DataPointsServiceClient(
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

            response = client.create_data_point(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_data_point_rest_flattened():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "users/sample1/dataTypes/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            data_point=data_points.DataPoint(
                steps=data_model.Steps(
                    interval=data_coordinates.ObservationTimeInterval(
                        start_time=timestamp_pb2.Timestamp(seconds=751)
                    )
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

        client.create_data_point(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v4/{parent=users/*/dataTypes/*}/dataPoints" % client.transport._host,
            args[1],
        )


def test_create_data_point_rest_flattened_error(transport: str = "rest"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_data_point(
            data_points.CreateDataPointRequest(),
            parent="parent_value",
            data_point=data_points.DataPoint(
                steps=data_model.Steps(
                    interval=data_coordinates.ObservationTimeInterval(
                        start_time=timestamp_pb2.Timestamp(seconds=751)
                    )
                )
            ),
        )


def test_update_data_point_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_data_point in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_data_point] = (
            mock_rpc
        )

        request = {}
        client.update_data_point(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.update_data_point(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_data_point_rest_required_fields(
    request_type=data_points.UpdateDataPointRequest,
):
    transport_class = transports.DataPointsServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateDataPoint,
        "_BaseUpdateDataPoint__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    # verify required fields with non-default values are left alone

    client = DataPointsServiceClient(
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
                "method": "patch",
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

            response = client.update_data_point(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_data_point_rest_flattened():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "data_point": {"name": "users/sample1/dataTypes/sample2/dataPoints/sample3"}
        }

        # get truthy value for each flattened field
        mock_args = dict(
            data_point=data_points.DataPoint(
                steps=data_model.Steps(
                    interval=data_coordinates.ObservationTimeInterval(
                        start_time=timestamp_pb2.Timestamp(seconds=751)
                    )
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

        client.update_data_point(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v4/{data_point.name=users/*/dataTypes/*/dataPoints/*}"
            % client.transport._host,
            args[1],
        )


def test_update_data_point_rest_flattened_error(transport: str = "rest"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_data_point(
            data_points.UpdateDataPointRequest(),
            data_point=data_points.DataPoint(
                steps=data_model.Steps(
                    interval=data_coordinates.ObservationTimeInterval(
                        start_time=timestamp_pb2.Timestamp(seconds=751)
                    )
                )
            ),
        )


def test_batch_delete_data_points_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_delete_data_points
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_delete_data_points
        ] = mock_rpc

        request = {}
        client.batch_delete_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.batch_delete_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_delete_data_points_rest_required_fields(
    request_type=data_points.BatchDeleteDataPointsRequest,
):
    transport_class = transports.DataPointsServiceRestTransport

    request_init = {}
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchDeleteDataPoints,
        "_BaseBatchDeleteDataPoints__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = DataPointsServiceClient(
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

            response = client.batch_delete_data_points(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_reconcile_data_points_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.reconcile_data_points
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.reconcile_data_points] = (
            mock_rpc
        )

        request = {}
        client.reconcile_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.reconcile_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_reconcile_data_points_rest_required_fields(
    request_type=data_points.ReconcileDataPointsRequest,
):
    transport_class = transports.DataPointsServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseReconcileDataPoints,
        "_BaseReconcileDataPoints__REQUIRED_FIELDS_DEFAULT_VALUES",
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
            "dataSourceFamily",
            "filter",
            "pageSize",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = data_points.ReconcileDataPointsResponse()
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
            return_value = data_points.ReconcileDataPointsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.reconcile_data_points(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_reconcile_data_points_rest_pager(transport: str = "rest"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[],
                next_page_token="def",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.ReconcileDataPointsResponse(
                data_points=[
                    data_points.ReconciledDataPoint(),
                    data_points.ReconciledDataPoint(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            data_points.ReconcileDataPointsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "users/sample1/dataTypes/sample2"}

        pager = client.reconcile_data_points(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, data_points.ReconciledDataPoint) for i in results)

        pages = list(client.reconcile_data_points(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_roll_up_data_points_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.roll_up_data_points in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.roll_up_data_points] = (
            mock_rpc
        )

        request = {}
        client.roll_up_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.roll_up_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_roll_up_data_points_rest_required_fields(
    request_type=data_points.RollUpDataPointsRequest,
):
    transport_class = transports.DataPointsServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseRollUpDataPoints,
        "_BaseRollUpDataPoints__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = data_points.RollUpDataPointsResponse()
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

            # Convert return value to protobuf type
            return_value = data_points.RollUpDataPointsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.roll_up_data_points(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_roll_up_data_points_rest_pager(transport: str = "rest"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
                ],
                next_page_token="abc",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[],
                next_page_token="def",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                ],
                next_page_token="ghi",
            ),
            data_points.RollUpDataPointsResponse(
                rollup_data_points=[
                    data_points.RollupDataPoint(),
                    data_points.RollupDataPoint(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            data_points.RollUpDataPointsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "users/sample1/dataTypes/sample2"}

        pager = client.roll_up_data_points(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, data_points.RollupDataPoint) for i in results)

        pages = list(client.roll_up_data_points(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_daily_roll_up_data_points_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.daily_roll_up_data_points
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.daily_roll_up_data_points
        ] = mock_rpc

        request = {}
        client.daily_roll_up_data_points(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.daily_roll_up_data_points(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_daily_roll_up_data_points_rest_required_fields(
    request_type=data_points.DailyRollUpDataPointsRequest,
):
    transport_class = transports.DataPointsServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDailyRollUpDataPoints,
        "_BaseDailyRollUpDataPoints__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = data_points.DailyRollUpDataPointsResponse()
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

            # Convert return value to protobuf type
            return_value = data_points.DailyRollUpDataPointsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.daily_roll_up_data_points(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_export_exercise_tcx_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.export_exercise_tcx in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.export_exercise_tcx] = (
            mock_rpc
        )

        request = {}
        client.export_exercise_tcx(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.export_exercise_tcx(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_export_exercise_tcx_rest_required_fields(
    request_type=data_points.ExportExerciseTcxRequest,
):
    transport_class = transports.DataPointsServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseExportExerciseTcx,
        "_BaseExportExerciseTcx__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("partialData",))

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = data_points.ExportExerciseTcxResponse()
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
            return_value = data_points.ExportExerciseTcxResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.export_exercise_tcx(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_export_exercise_tcx_rest_flattened():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = data_points.ExportExerciseTcxResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "users/sample1/dataTypes/sample2/dataPoints/sample3"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = data_points.ExportExerciseTcxResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.export_exercise_tcx(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v4/{name=users/*/dataTypes/*/dataPoints/*}:exportExerciseTcx"
            % client.transport._host,
            args[1],
        )


def test_export_exercise_tcx_rest_flattened_error(transport: str = "rest"):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.export_exercise_tcx(
            data_points.ExportExerciseTcxRequest(),
            name="name_value",
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.DataPointsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.DataPointsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = DataPointsServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.DataPointsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = DataPointsServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = DataPointsServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.DataPointsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = DataPointsServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.DataPointsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = DataPointsServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.DataPointsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.DataPointsServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.DataPointsServiceGrpcTransport,
        transports.DataPointsServiceGrpcAsyncIOTransport,
        transports.DataPointsServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = DataPointsServiceClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_data_point_empty_call_grpc():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_data_point), "__call__") as call:
        call.return_value = data_points.DataPoint()
        client.get_data_point(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.GetDataPointRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_data_points_empty_call_grpc():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_data_points), "__call__") as call:
        call.return_value = data_points.ListDataPointsResponse()
        client.list_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.ListDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_data_point_empty_call_grpc():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_data_point), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_data_point(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.CreateDataPointRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_data_point_empty_call_grpc():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_point), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.update_data_point(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.UpdateDataPointRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_delete_data_points_empty_call_grpc():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_delete_data_points), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.batch_delete_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.BatchDeleteDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_reconcile_data_points_empty_call_grpc():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.reconcile_data_points), "__call__"
    ) as call:
        call.return_value = data_points.ReconcileDataPointsResponse()
        client.reconcile_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.ReconcileDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_roll_up_data_points_empty_call_grpc():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.roll_up_data_points), "__call__"
    ) as call:
        call.return_value = data_points.RollUpDataPointsResponse()
        client.roll_up_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.RollUpDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_daily_roll_up_data_points_empty_call_grpc():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.daily_roll_up_data_points), "__call__"
    ) as call:
        call.return_value = data_points.DailyRollUpDataPointsResponse()
        client.daily_roll_up_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.DailyRollUpDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_export_exercise_tcx_empty_call_grpc():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.export_exercise_tcx), "__call__"
    ) as call:
        call.return_value = data_points.ExportExerciseTcxResponse()
        client.export_exercise_tcx(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.ExportExerciseTcxRequest()
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = DataPointsServiceAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_data_point_empty_call_grpc_asyncio():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_data_point), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.DataPoint(
                name="name_value",
            )
        )
        await client.get_data_point(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.GetDataPointRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_data_points_empty_call_grpc_asyncio():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_data_points), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.ListDataPointsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.ListDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_data_point_empty_call_grpc_asyncio():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_data_point), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.create_data_point(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.CreateDataPointRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_data_point_empty_call_grpc_asyncio():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_point), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.update_data_point(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.UpdateDataPointRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_batch_delete_data_points_empty_call_grpc_asyncio():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_delete_data_points), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.batch_delete_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.BatchDeleteDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_reconcile_data_points_empty_call_grpc_asyncio():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.reconcile_data_points), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.ReconcileDataPointsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.reconcile_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.ReconcileDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_roll_up_data_points_empty_call_grpc_asyncio():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.roll_up_data_points), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.RollUpDataPointsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.roll_up_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.RollUpDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_daily_roll_up_data_points_empty_call_grpc_asyncio():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.daily_roll_up_data_points), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.DailyRollUpDataPointsResponse()
        )
        await client.daily_roll_up_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.DailyRollUpDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_export_exercise_tcx_empty_call_grpc_asyncio():
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.export_exercise_tcx), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            data_points.ExportExerciseTcxResponse(
                tcx_data="tcx_data_value",
            )
        )
        await client.export_exercise_tcx(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.ExportExerciseTcxRequest()
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = DataPointsServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_get_data_point_rest_bad_request(request_type=data_points.GetDataPointRequest):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "users/sample1/dataTypes/sample2/dataPoints/sample3"}
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
        client.get_data_point(request)


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.GetDataPointRequest,
        dict,
    ],
)
def test_get_data_point_rest_call_success(request_type):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "users/sample1/dataTypes/sample2/dataPoints/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = data_points.DataPoint(
            name="name_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = data_points.DataPoint.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_data_point(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, data_points.DataPoint)
    assert response.name == "name_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_data_point_rest_interceptors(null_interceptor):
    transport = transports.DataPointsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.DataPointsServiceRestInterceptor(),
    )
    client = DataPointsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "post_get_data_point"
        ) as post,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor,
            "post_get_data_point_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "pre_get_data_point"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = data_points.GetDataPointRequest.pb(
            data_points.GetDataPointRequest()
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
        return_value = data_points.DataPoint.to_json(data_points.DataPoint())
        req.return_value.content = return_value

        request = data_points.GetDataPointRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = data_points.DataPoint()
        post_with_metadata.return_value = data_points.DataPoint(), metadata

        client.get_data_point(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_data_points_rest_bad_request(
    request_type=data_points.ListDataPointsRequest,
):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "users/sample1/dataTypes/sample2"}
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
        client.list_data_points(request)


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.ListDataPointsRequest,
        dict,
    ],
)
def test_list_data_points_rest_call_success(request_type):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "users/sample1/dataTypes/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = data_points.ListDataPointsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = data_points.ListDataPointsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_data_points(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListDataPointsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_data_points_rest_interceptors(null_interceptor):
    transport = transports.DataPointsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.DataPointsServiceRestInterceptor(),
    )
    client = DataPointsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "post_list_data_points"
        ) as post,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor,
            "post_list_data_points_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "pre_list_data_points"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = data_points.ListDataPointsRequest.pb(
            data_points.ListDataPointsRequest()
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
        return_value = data_points.ListDataPointsResponse.to_json(
            data_points.ListDataPointsResponse()
        )
        req.return_value.content = return_value

        request = data_points.ListDataPointsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = data_points.ListDataPointsResponse()
        post_with_metadata.return_value = data_points.ListDataPointsResponse(), metadata

        client.list_data_points(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_data_point_rest_bad_request(
    request_type=data_points.CreateDataPointRequest,
):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "users/sample1/dataTypes/sample2"}
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
        client.create_data_point(request)


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.CreateDataPointRequest,
        dict,
    ],
)
def test_create_data_point_rest_call_success(request_type):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "users/sample1/dataTypes/sample2"}
    request_init["data_point"] = {
        "steps": {
            "interval": {
                "start_time": {"seconds": 751, "nanos": 543},
                "start_utc_offset": {"seconds": 751, "nanos": 543},
                "end_time": {},
                "end_utc_offset": {},
                "civil_start_time": {
                    "date": {"year": 433, "month": 550, "day": 318},
                    "time": {
                        "hours": 561,
                        "minutes": 773,
                        "seconds": 751,
                        "nanos": 543,
                    },
                },
                "civil_end_time": {},
            },
            "count": 553,
        },
        "floors": {"interval": {}, "count": 553},
        "heart_rate": {
            "sample_time": {"physical_time": {}, "utc_offset": {}, "civil_time": {}},
            "beats_per_minute": 1702,
            "metadata": {"motion_context": 1, "sensor_location": 1},
        },
        "sleep": {
            "interval": {
                "start_time": {},
                "start_utc_offset": {},
                "end_time": {},
                "end_utc_offset": {},
                "civil_start_time": {},
                "civil_end_time": {},
            },
            "type_": 1,
            "stages": [
                {
                    "start_time": {},
                    "start_utc_offset": {},
                    "end_time": {},
                    "end_utc_offset": {},
                    "type_": 1,
                    "create_time": {},
                    "update_time": {},
                }
            ],
            "out_of_bed_segments": [
                {
                    "start_time": {},
                    "start_utc_offset": {},
                    "end_time": {},
                    "end_utc_offset": {},
                }
            ],
            "metadata": {
                "stages_status": 1,
                "processed": True,
                "nap": True,
                "manually_edited": True,
                "external_id": "external_id_value",
                "main_sleep": True,
            },
            "summary": {
                "minutes_in_sleep_period": 2453,
                "minutes_after_wake_up": 2241,
                "minutes_to_fall_asleep": 2334,
                "minutes_asleep": 1502,
                "minutes_awake": 1389,
                "stages_summary": [{"type_": 1, "minutes": 773, "count": 553}],
            },
            "create_time": {},
            "update_time": {},
            "short_awakenings": {},
        },
        "daily_resting_heart_rate": {
            "date": {},
            "beats_per_minute": 1702,
            "daily_resting_heart_rate_metadata": {"calculation_method": 1},
        },
        "daily_heart_rate_variability": {
            "date": {},
            "average_heart_rate_variability_milliseconds": 0.4541,
            "non_rem_heart_rate_beats_per_minute": 3697,
            "entropy": 0.785,
            "deep_sleep_root_mean_square_of_successive_differences_milliseconds": 0.6971,
        },
        "exercise": {
            "interval": {},
            "exercise_type": 13,
            "splits": [
                {
                    "start_time": {},
                    "start_utc_offset": {},
                    "end_time": {},
                    "end_utc_offset": {},
                    "active_duration": {},
                    "metrics_summary": {
                        "calories_kcal": 0.1356,
                        "distance_millimeters": 0.2129,
                        "steps": 559,
                        "average_speed_millimeters_per_second": 0.3794,
                        "average_pace_seconds_per_meter": 0.3139,
                        "average_heart_rate_beats_per_minute": 3678,
                        "elevation_gain_millimeters": 0.2763,
                        "active_zone_minutes": 2043,
                        "run_vo2_max": 0.1136,
                        "total_swim_lengths": 0.1943,
                        "heart_rate_zone_durations": {
                            "light_time": {},
                            "moderate_time": {},
                            "vigorous_time": {},
                            "peak_time": {},
                        },
                        "mobility_metrics": {
                            "avg_cadence_steps_per_minute": 0.2949,
                            "avg_stride_length_millimeters": 3087,
                            "avg_vertical_oscillation_millimeters": 3837,
                            "avg_vertical_ratio": 0.19090000000000001,
                            "avg_ground_contact_time_duration": {},
                        },
                    },
                    "split_type": 1,
                }
            ],
            "exercise_events": [
                {"event_time": {}, "event_utc_offset": {}, "exercise_event_type": 1}
            ],
            "split_summaries": {},
            "metrics_summary": {},
            "exercise_metadata": {"pool_length_millimeters": 2465, "has_gps": True},
            "display_name": "display_name_value",
            "active_duration": {},
            "notes": "notes_value",
            "update_time": {},
            "create_time": {},
        },
        "weight": {
            "sample_time": {},
            "weight_grams": 0.12810000000000002,
            "notes": "notes_value",
        },
        "altitude": {"interval": {}, "gain_millimeters": 1701},
        "distance": {"interval": {}, "millimeters": 1191},
        "body_fat": {"sample_time": {}, "percentage": 0.10540000000000001},
        "active_zone_minutes": {
            "interval": {},
            "heart_rate_zone": 1,
            "active_zone_minutes": 2043,
        },
        "heart_rate_variability": {
            "sample_time": {},
            "root_mean_square_of_successive_differences_milliseconds": 0.5830000000000001,
            "standard_deviation_milliseconds": 0.32880000000000004,
            "metadata": {"high_frequency_power": 0.2141, "low_frequency_power": 0.2063},
        },
        "daily_sleep_temperature_derivations": {
            "date": {},
            "nightly_temperature_celsius": 0.29150000000000004,
            "baseline_temperature_celsius": 0.2983,
            "relative_nightly_stddev_30d_celsius": 0.36160000000000003,
        },
        "sedentary_period": {"interval": {}},
        "run_vo2_max": {"sample_time": {}, "run_vo2_max": 0.1136},
        "oxygen_saturation": {"sample_time": {}, "percentage": 0.10540000000000001},
        "daily_oxygen_saturation": {
            "date": {},
            "average_percentage": 0.188,
            "lower_bound_percentage": 0.2333,
            "upper_bound_percentage": 0.2336,
            "standard_deviation_percentage": 0.30560000000000004,
        },
        "activity_level": {"interval": {}, "activity_level_type": 1},
        "vo2_max": {
            "sample_time": {},
            "vo2_max": 0.7000000000000001,
            "measurement_method": 1,
        },
        "daily_vo2_max": {
            "date": {},
            "vo2_max": 0.7000000000000001,
            "estimated": True,
            "cardio_fitness_level": 1,
            "vo2_max_covariance": 0.18460000000000001,
        },
        "nutrition_log": {
            "interval": {},
            "nutrients": [
                {"quantity": {"grams": 0.538, "user_provided_unit": 1}, "nutrient": 1}
            ],
            "energy": {"kcal": 0.41100000000000003, "user_provided_unit": 1},
            "energy_from_fat": {},
            "total_carbohydrate": {},
            "total_fat": {},
            "meal_type": 1,
            "serving": {
                "amount": 0.66,
                "food_measurement_unit": "food_measurement_unit_value",
                "food_measurement_unit_display_name": "food_measurement_unit_display_name_value",
            },
            "food": "food_value",
            "food_display_name": "food_display_name_value",
        },
        "irregular_rhythm_notification": {
            "interval": {},
            "alert_windows": [
                {
                    "start_time": {},
                    "start_utc_offset": {},
                    "end_time": {},
                    "end_utc_offset": {},
                    "civil_start_time": {},
                    "civil_end_time": {},
                    "positive": True,
                    "heart_beats": [
                        {
                            "physical_time": {},
                            "utc_offset": {},
                            "civil_time": {},
                            "beats_per_minute": 1702,
                        }
                    ],
                }
            ],
            "medical_device_info": {
                "algorithm_version": "algorithm_version_value",
                "service_version": "service_version_value",
                "firmware_version": "firmware_version_value",
                "feature_version": "feature_version_value",
                "device_model": "device_model_value",
            },
        },
        "electrocardiogram": {
            "interval": {},
            "beats_per_minute_avg": 2115,
            "result_classification": 1,
            "waveform_samples": [1724, 1725],
            "sampling_frequency_hertz": 2584,
            "millivolts_scaling_factor": 2669,
            "lead_number": 1150,
            "medical_device_info": {},
        },
        "daily_heart_rate_zones": {
            "date": {},
            "heart_rate_zones": [
                {
                    "heart_rate_zone_type": 1,
                    "min_beats_per_minute": 2121,
                    "max_beats_per_minute": 2123,
                }
            ],
        },
        "hydration_log": {
            "interval": {},
            "amount_consumed": {"milliliters": 0.1194, "user_provided_unit": 1},
        },
        "food": {
            "display_name": "display_name_value",
            "brand": "brand_value",
            "access_level": 1,
            "description": "description_value",
            "language_code": "language_code_value",
            "meal_type": 1,
            "nutrients": {},
            "energy_from_fat": {},
            "total_carbohydrate": {},
            "total_fat": {},
            "energy_min": {},
            "energy_avg": {},
            "energy_max": {},
            "default_serving": {
                "amount": 0.66,
                "food_measurement_unit": "food_measurement_unit_value",
                "food_measurement_unit_display_name": "food_measurement_unit_display_name_value",
                "food_measurement_unit_display_name_plural": "food_measurement_unit_display_name_plural_value",
                "multiplier": 0.1095,
            },
            "servings": {},
        },
        "time_in_heart_rate_zone": {"interval": {}, "heart_rate_zone_type": 1},
        "active_minutes": {
            "interval": {},
            "active_minutes_by_activity_level": [
                {"activity_level": 1, "active_minutes": 1504}
            ],
        },
        "respiratory_rate_sleep_summary": {
            "sample_time": {},
            "deep_sleep_stats": {
                "breaths_per_minute": 0.192,
                "standard_deviation": 0.1907,
                "signal_to_noise": 0.1597,
            },
            "light_sleep_stats": {},
            "rem_sleep_stats": {},
            "full_sleep_stats": {},
        },
        "daily_respiratory_rate": {"date": {}, "breaths_per_minute": 0.192},
        "swim_lengths_data": {
            "interval": {},
            "swim_stroke_type": 1,
            "stroke_count": 1312,
        },
        "height": {"sample_time": {}, "height_millimeters": 1919},
        "basal_energy_burned": {"interval": {}, "kcal": 0.41100000000000003},
        "core_body_temperature": {
            "sample_time": {},
            "temperature_celsius": 0.2053,
            "measurement_location": 1,
            "id": "id_value",
        },
        "active_energy_burned": {"interval": {}, "kcal": 0.41100000000000003},
        "food_measurement_unit": {
            "display_name": "display_name_value",
            "plural_display_name": "plural_display_name_value",
        },
        "blood_glucose": {
            "sample_time": {},
            "blood_glucose_milligrams_per_deciliter": 0.4011,
            "measurement_source": 1,
            "meal_type": 1,
            "measurement_timing": 1,
            "specimen": 1,
            "notes": "notes_value",
        },
        "menstrual_period": {"interval": {}, "notes": "notes_value"},
        "ovulation_test": {"sample_time": {}, "result": 1},
        "symptoms": {"sample_time": {}, "symptoms": [1]},
        "moods": {"sample_time": {}, "moods": [1], "valences": [1]},
        "name": "name_value",
        "data_source": {
            "recording_method": 1,
            "device": {
                "form_factor": 1,
                "manufacturer": "manufacturer_value",
                "display_name": "display_name_value",
            },
            "application": {
                "package_name": "package_name_value",
                "web_client_id": "web_client_id_value",
                "google_web_client_id": "google_web_client_id_value",
            },
            "platform": 1,
        },
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = data_points.CreateDataPointRequest.meta.fields["data_point"]

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
    for field, value in request_init["data_point"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["data_point"][field])):
                    del request_init["data_point"][field][i][subfield]
            else:
                del request_init["data_point"][field][subfield]
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
        response = client.create_data_point(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_data_point_rest_interceptors(null_interceptor):
    transport = transports.DataPointsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.DataPointsServiceRestInterceptor(),
    )
    client = DataPointsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "post_create_data_point"
        ) as post,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor,
            "post_create_data_point_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "pre_create_data_point"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = data_points.CreateDataPointRequest.pb(
            data_points.CreateDataPointRequest()
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

        request = data_points.CreateDataPointRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.create_data_point(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_data_point_rest_bad_request(
    request_type=data_points.UpdateDataPointRequest,
):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "data_point": {"name": "users/sample1/dataTypes/sample2/dataPoints/sample3"}
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
        client.update_data_point(request)


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.UpdateDataPointRequest,
        dict,
    ],
)
def test_update_data_point_rest_call_success(request_type):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "data_point": {"name": "users/sample1/dataTypes/sample2/dataPoints/sample3"}
    }
    request_init["data_point"] = {
        "steps": {
            "interval": {
                "start_time": {"seconds": 751, "nanos": 543},
                "start_utc_offset": {"seconds": 751, "nanos": 543},
                "end_time": {},
                "end_utc_offset": {},
                "civil_start_time": {
                    "date": {"year": 433, "month": 550, "day": 318},
                    "time": {
                        "hours": 561,
                        "minutes": 773,
                        "seconds": 751,
                        "nanos": 543,
                    },
                },
                "civil_end_time": {},
            },
            "count": 553,
        },
        "floors": {"interval": {}, "count": 553},
        "heart_rate": {
            "sample_time": {"physical_time": {}, "utc_offset": {}, "civil_time": {}},
            "beats_per_minute": 1702,
            "metadata": {"motion_context": 1, "sensor_location": 1},
        },
        "sleep": {
            "interval": {
                "start_time": {},
                "start_utc_offset": {},
                "end_time": {},
                "end_utc_offset": {},
                "civil_start_time": {},
                "civil_end_time": {},
            },
            "type_": 1,
            "stages": [
                {
                    "start_time": {},
                    "start_utc_offset": {},
                    "end_time": {},
                    "end_utc_offset": {},
                    "type_": 1,
                    "create_time": {},
                    "update_time": {},
                }
            ],
            "out_of_bed_segments": [
                {
                    "start_time": {},
                    "start_utc_offset": {},
                    "end_time": {},
                    "end_utc_offset": {},
                }
            ],
            "metadata": {
                "stages_status": 1,
                "processed": True,
                "nap": True,
                "manually_edited": True,
                "external_id": "external_id_value",
                "main_sleep": True,
            },
            "summary": {
                "minutes_in_sleep_period": 2453,
                "minutes_after_wake_up": 2241,
                "minutes_to_fall_asleep": 2334,
                "minutes_asleep": 1502,
                "minutes_awake": 1389,
                "stages_summary": [{"type_": 1, "minutes": 773, "count": 553}],
            },
            "create_time": {},
            "update_time": {},
            "short_awakenings": {},
        },
        "daily_resting_heart_rate": {
            "date": {},
            "beats_per_minute": 1702,
            "daily_resting_heart_rate_metadata": {"calculation_method": 1},
        },
        "daily_heart_rate_variability": {
            "date": {},
            "average_heart_rate_variability_milliseconds": 0.4541,
            "non_rem_heart_rate_beats_per_minute": 3697,
            "entropy": 0.785,
            "deep_sleep_root_mean_square_of_successive_differences_milliseconds": 0.6971,
        },
        "exercise": {
            "interval": {},
            "exercise_type": 13,
            "splits": [
                {
                    "start_time": {},
                    "start_utc_offset": {},
                    "end_time": {},
                    "end_utc_offset": {},
                    "active_duration": {},
                    "metrics_summary": {
                        "calories_kcal": 0.1356,
                        "distance_millimeters": 0.2129,
                        "steps": 559,
                        "average_speed_millimeters_per_second": 0.3794,
                        "average_pace_seconds_per_meter": 0.3139,
                        "average_heart_rate_beats_per_minute": 3678,
                        "elevation_gain_millimeters": 0.2763,
                        "active_zone_minutes": 2043,
                        "run_vo2_max": 0.1136,
                        "total_swim_lengths": 0.1943,
                        "heart_rate_zone_durations": {
                            "light_time": {},
                            "moderate_time": {},
                            "vigorous_time": {},
                            "peak_time": {},
                        },
                        "mobility_metrics": {
                            "avg_cadence_steps_per_minute": 0.2949,
                            "avg_stride_length_millimeters": 3087,
                            "avg_vertical_oscillation_millimeters": 3837,
                            "avg_vertical_ratio": 0.19090000000000001,
                            "avg_ground_contact_time_duration": {},
                        },
                    },
                    "split_type": 1,
                }
            ],
            "exercise_events": [
                {"event_time": {}, "event_utc_offset": {}, "exercise_event_type": 1}
            ],
            "split_summaries": {},
            "metrics_summary": {},
            "exercise_metadata": {"pool_length_millimeters": 2465, "has_gps": True},
            "display_name": "display_name_value",
            "active_duration": {},
            "notes": "notes_value",
            "update_time": {},
            "create_time": {},
        },
        "weight": {
            "sample_time": {},
            "weight_grams": 0.12810000000000002,
            "notes": "notes_value",
        },
        "altitude": {"interval": {}, "gain_millimeters": 1701},
        "distance": {"interval": {}, "millimeters": 1191},
        "body_fat": {"sample_time": {}, "percentage": 0.10540000000000001},
        "active_zone_minutes": {
            "interval": {},
            "heart_rate_zone": 1,
            "active_zone_minutes": 2043,
        },
        "heart_rate_variability": {
            "sample_time": {},
            "root_mean_square_of_successive_differences_milliseconds": 0.5830000000000001,
            "standard_deviation_milliseconds": 0.32880000000000004,
            "metadata": {"high_frequency_power": 0.2141, "low_frequency_power": 0.2063},
        },
        "daily_sleep_temperature_derivations": {
            "date": {},
            "nightly_temperature_celsius": 0.29150000000000004,
            "baseline_temperature_celsius": 0.2983,
            "relative_nightly_stddev_30d_celsius": 0.36160000000000003,
        },
        "sedentary_period": {"interval": {}},
        "run_vo2_max": {"sample_time": {}, "run_vo2_max": 0.1136},
        "oxygen_saturation": {"sample_time": {}, "percentage": 0.10540000000000001},
        "daily_oxygen_saturation": {
            "date": {},
            "average_percentage": 0.188,
            "lower_bound_percentage": 0.2333,
            "upper_bound_percentage": 0.2336,
            "standard_deviation_percentage": 0.30560000000000004,
        },
        "activity_level": {"interval": {}, "activity_level_type": 1},
        "vo2_max": {
            "sample_time": {},
            "vo2_max": 0.7000000000000001,
            "measurement_method": 1,
        },
        "daily_vo2_max": {
            "date": {},
            "vo2_max": 0.7000000000000001,
            "estimated": True,
            "cardio_fitness_level": 1,
            "vo2_max_covariance": 0.18460000000000001,
        },
        "nutrition_log": {
            "interval": {},
            "nutrients": [
                {"quantity": {"grams": 0.538, "user_provided_unit": 1}, "nutrient": 1}
            ],
            "energy": {"kcal": 0.41100000000000003, "user_provided_unit": 1},
            "energy_from_fat": {},
            "total_carbohydrate": {},
            "total_fat": {},
            "meal_type": 1,
            "serving": {
                "amount": 0.66,
                "food_measurement_unit": "food_measurement_unit_value",
                "food_measurement_unit_display_name": "food_measurement_unit_display_name_value",
            },
            "food": "food_value",
            "food_display_name": "food_display_name_value",
        },
        "irregular_rhythm_notification": {
            "interval": {},
            "alert_windows": [
                {
                    "start_time": {},
                    "start_utc_offset": {},
                    "end_time": {},
                    "end_utc_offset": {},
                    "civil_start_time": {},
                    "civil_end_time": {},
                    "positive": True,
                    "heart_beats": [
                        {
                            "physical_time": {},
                            "utc_offset": {},
                            "civil_time": {},
                            "beats_per_minute": 1702,
                        }
                    ],
                }
            ],
            "medical_device_info": {
                "algorithm_version": "algorithm_version_value",
                "service_version": "service_version_value",
                "firmware_version": "firmware_version_value",
                "feature_version": "feature_version_value",
                "device_model": "device_model_value",
            },
        },
        "electrocardiogram": {
            "interval": {},
            "beats_per_minute_avg": 2115,
            "result_classification": 1,
            "waveform_samples": [1724, 1725],
            "sampling_frequency_hertz": 2584,
            "millivolts_scaling_factor": 2669,
            "lead_number": 1150,
            "medical_device_info": {},
        },
        "daily_heart_rate_zones": {
            "date": {},
            "heart_rate_zones": [
                {
                    "heart_rate_zone_type": 1,
                    "min_beats_per_minute": 2121,
                    "max_beats_per_minute": 2123,
                }
            ],
        },
        "hydration_log": {
            "interval": {},
            "amount_consumed": {"milliliters": 0.1194, "user_provided_unit": 1},
        },
        "food": {
            "display_name": "display_name_value",
            "brand": "brand_value",
            "access_level": 1,
            "description": "description_value",
            "language_code": "language_code_value",
            "meal_type": 1,
            "nutrients": {},
            "energy_from_fat": {},
            "total_carbohydrate": {},
            "total_fat": {},
            "energy_min": {},
            "energy_avg": {},
            "energy_max": {},
            "default_serving": {
                "amount": 0.66,
                "food_measurement_unit": "food_measurement_unit_value",
                "food_measurement_unit_display_name": "food_measurement_unit_display_name_value",
                "food_measurement_unit_display_name_plural": "food_measurement_unit_display_name_plural_value",
                "multiplier": 0.1095,
            },
            "servings": {},
        },
        "time_in_heart_rate_zone": {"interval": {}, "heart_rate_zone_type": 1},
        "active_minutes": {
            "interval": {},
            "active_minutes_by_activity_level": [
                {"activity_level": 1, "active_minutes": 1504}
            ],
        },
        "respiratory_rate_sleep_summary": {
            "sample_time": {},
            "deep_sleep_stats": {
                "breaths_per_minute": 0.192,
                "standard_deviation": 0.1907,
                "signal_to_noise": 0.1597,
            },
            "light_sleep_stats": {},
            "rem_sleep_stats": {},
            "full_sleep_stats": {},
        },
        "daily_respiratory_rate": {"date": {}, "breaths_per_minute": 0.192},
        "swim_lengths_data": {
            "interval": {},
            "swim_stroke_type": 1,
            "stroke_count": 1312,
        },
        "height": {"sample_time": {}, "height_millimeters": 1919},
        "basal_energy_burned": {"interval": {}, "kcal": 0.41100000000000003},
        "core_body_temperature": {
            "sample_time": {},
            "temperature_celsius": 0.2053,
            "measurement_location": 1,
            "id": "id_value",
        },
        "active_energy_burned": {"interval": {}, "kcal": 0.41100000000000003},
        "food_measurement_unit": {
            "display_name": "display_name_value",
            "plural_display_name": "plural_display_name_value",
        },
        "blood_glucose": {
            "sample_time": {},
            "blood_glucose_milligrams_per_deciliter": 0.4011,
            "measurement_source": 1,
            "meal_type": 1,
            "measurement_timing": 1,
            "specimen": 1,
            "notes": "notes_value",
        },
        "menstrual_period": {"interval": {}, "notes": "notes_value"},
        "ovulation_test": {"sample_time": {}, "result": 1},
        "symptoms": {"sample_time": {}, "symptoms": [1]},
        "moods": {"sample_time": {}, "moods": [1], "valences": [1]},
        "name": "users/sample1/dataTypes/sample2/dataPoints/sample3",
        "data_source": {
            "recording_method": 1,
            "device": {
                "form_factor": 1,
                "manufacturer": "manufacturer_value",
                "display_name": "display_name_value",
            },
            "application": {
                "package_name": "package_name_value",
                "web_client_id": "web_client_id_value",
                "google_web_client_id": "google_web_client_id_value",
            },
            "platform": 1,
        },
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = data_points.UpdateDataPointRequest.meta.fields["data_point"]

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
    for field, value in request_init["data_point"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["data_point"][field])):
                    del request_init["data_point"][field][i][subfield]
            else:
                del request_init["data_point"][field][subfield]
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
        response = client.update_data_point(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_data_point_rest_interceptors(null_interceptor):
    transport = transports.DataPointsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.DataPointsServiceRestInterceptor(),
    )
    client = DataPointsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "post_update_data_point"
        ) as post,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor,
            "post_update_data_point_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "pre_update_data_point"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = data_points.UpdateDataPointRequest.pb(
            data_points.UpdateDataPointRequest()
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

        request = data_points.UpdateDataPointRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.update_data_point(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_delete_data_points_rest_bad_request(
    request_type=data_points.BatchDeleteDataPointsRequest,
):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "users/sample1/dataTypes/sample2"}
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
        client.batch_delete_data_points(request)


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.BatchDeleteDataPointsRequest,
        dict,
    ],
)
def test_batch_delete_data_points_rest_call_success(request_type):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "users/sample1/dataTypes/sample2"}
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
        response = client.batch_delete_data_points(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_delete_data_points_rest_interceptors(null_interceptor):
    transport = transports.DataPointsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.DataPointsServiceRestInterceptor(),
    )
    client = DataPointsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "post_batch_delete_data_points"
        ) as post,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor,
            "post_batch_delete_data_points_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "pre_batch_delete_data_points"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = data_points.BatchDeleteDataPointsRequest.pb(
            data_points.BatchDeleteDataPointsRequest()
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

        request = data_points.BatchDeleteDataPointsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.batch_delete_data_points(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_reconcile_data_points_rest_bad_request(
    request_type=data_points.ReconcileDataPointsRequest,
):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "users/sample1/dataTypes/sample2"}
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
        client.reconcile_data_points(request)


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.ReconcileDataPointsRequest,
        dict,
    ],
)
def test_reconcile_data_points_rest_call_success(request_type):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "users/sample1/dataTypes/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = data_points.ReconcileDataPointsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = data_points.ReconcileDataPointsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.reconcile_data_points(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ReconcileDataPointsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_reconcile_data_points_rest_interceptors(null_interceptor):
    transport = transports.DataPointsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.DataPointsServiceRestInterceptor(),
    )
    client = DataPointsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "post_reconcile_data_points"
        ) as post,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor,
            "post_reconcile_data_points_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "pre_reconcile_data_points"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = data_points.ReconcileDataPointsRequest.pb(
            data_points.ReconcileDataPointsRequest()
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
        return_value = data_points.ReconcileDataPointsResponse.to_json(
            data_points.ReconcileDataPointsResponse()
        )
        req.return_value.content = return_value

        request = data_points.ReconcileDataPointsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = data_points.ReconcileDataPointsResponse()
        post_with_metadata.return_value = (
            data_points.ReconcileDataPointsResponse(),
            metadata,
        )

        client.reconcile_data_points(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_roll_up_data_points_rest_bad_request(
    request_type=data_points.RollUpDataPointsRequest,
):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "users/sample1/dataTypes/sample2"}
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
        client.roll_up_data_points(request)


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.RollUpDataPointsRequest,
        dict,
    ],
)
def test_roll_up_data_points_rest_call_success(request_type):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "users/sample1/dataTypes/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = data_points.RollUpDataPointsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = data_points.RollUpDataPointsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.roll_up_data_points(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.RollUpDataPointsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_roll_up_data_points_rest_interceptors(null_interceptor):
    transport = transports.DataPointsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.DataPointsServiceRestInterceptor(),
    )
    client = DataPointsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "post_roll_up_data_points"
        ) as post,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor,
            "post_roll_up_data_points_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "pre_roll_up_data_points"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = data_points.RollUpDataPointsRequest.pb(
            data_points.RollUpDataPointsRequest()
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
        return_value = data_points.RollUpDataPointsResponse.to_json(
            data_points.RollUpDataPointsResponse()
        )
        req.return_value.content = return_value

        request = data_points.RollUpDataPointsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = data_points.RollUpDataPointsResponse()
        post_with_metadata.return_value = (
            data_points.RollUpDataPointsResponse(),
            metadata,
        )

        client.roll_up_data_points(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_daily_roll_up_data_points_rest_bad_request(
    request_type=data_points.DailyRollUpDataPointsRequest,
):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "users/sample1/dataTypes/sample2"}
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
        client.daily_roll_up_data_points(request)


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.DailyRollUpDataPointsRequest,
        dict,
    ],
)
def test_daily_roll_up_data_points_rest_call_success(request_type):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "users/sample1/dataTypes/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = data_points.DailyRollUpDataPointsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = data_points.DailyRollUpDataPointsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.daily_roll_up_data_points(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, data_points.DailyRollUpDataPointsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_daily_roll_up_data_points_rest_interceptors(null_interceptor):
    transport = transports.DataPointsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.DataPointsServiceRestInterceptor(),
    )
    client = DataPointsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor,
            "post_daily_roll_up_data_points",
        ) as post,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor,
            "post_daily_roll_up_data_points_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "pre_daily_roll_up_data_points"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = data_points.DailyRollUpDataPointsRequest.pb(
            data_points.DailyRollUpDataPointsRequest()
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
        return_value = data_points.DailyRollUpDataPointsResponse.to_json(
            data_points.DailyRollUpDataPointsResponse()
        )
        req.return_value.content = return_value

        request = data_points.DailyRollUpDataPointsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = data_points.DailyRollUpDataPointsResponse()
        post_with_metadata.return_value = (
            data_points.DailyRollUpDataPointsResponse(),
            metadata,
        )

        client.daily_roll_up_data_points(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_export_exercise_tcx_rest_bad_request(
    request_type=data_points.ExportExerciseTcxRequest,
):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "users/sample1/dataTypes/sample2/dataPoints/sample3"}
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
        client.export_exercise_tcx(request)


@pytest.mark.parametrize(
    "request_type",
    [
        data_points.ExportExerciseTcxRequest,
        dict,
    ],
)
def test_export_exercise_tcx_rest_call_success(request_type):
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "users/sample1/dataTypes/sample2/dataPoints/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = data_points.ExportExerciseTcxResponse(
            tcx_data="tcx_data_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = data_points.ExportExerciseTcxResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.export_exercise_tcx(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, data_points.ExportExerciseTcxResponse)
    assert response.tcx_data == "tcx_data_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_export_exercise_tcx_rest_interceptors(null_interceptor):
    transport = transports.DataPointsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.DataPointsServiceRestInterceptor(),
    )
    client = DataPointsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "post_export_exercise_tcx"
        ) as post,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor,
            "post_export_exercise_tcx_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.DataPointsServiceRestInterceptor, "pre_export_exercise_tcx"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = data_points.ExportExerciseTcxRequest.pb(
            data_points.ExportExerciseTcxRequest()
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
        return_value = data_points.ExportExerciseTcxResponse.to_json(
            data_points.ExportExerciseTcxResponse()
        )
        req.return_value.content = return_value

        request = data_points.ExportExerciseTcxRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = data_points.ExportExerciseTcxResponse()
        post_with_metadata.return_value = (
            data_points.ExportExerciseTcxResponse(),
            metadata,
        )

        client.export_exercise_tcx(
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
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_data_point_empty_call_rest():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_data_point), "__call__") as call:
        client.get_data_point(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.GetDataPointRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_data_points_empty_call_rest():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_data_points), "__call__") as call:
        client.list_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.ListDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_data_point_empty_call_rest():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_data_point), "__call__"
    ) as call:
        client.create_data_point(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.CreateDataPointRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_data_point_empty_call_rest():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_data_point), "__call__"
    ) as call:
        client.update_data_point(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.UpdateDataPointRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_delete_data_points_empty_call_rest():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_delete_data_points), "__call__"
    ) as call:
        client.batch_delete_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.BatchDeleteDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_reconcile_data_points_empty_call_rest():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.reconcile_data_points), "__call__"
    ) as call:
        client.reconcile_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.ReconcileDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_roll_up_data_points_empty_call_rest():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.roll_up_data_points), "__call__"
    ) as call:
        client.roll_up_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.RollUpDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_daily_roll_up_data_points_empty_call_rest():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.daily_roll_up_data_points), "__call__"
    ) as call:
        client.daily_roll_up_data_points(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.DailyRollUpDataPointsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_export_exercise_tcx_empty_call_rest():
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.export_exercise_tcx), "__call__"
    ) as call:
        client.export_exercise_tcx(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = data_points.ExportExerciseTcxRequest()
        assert args[0] == request_msg


def test_data_points_service_rest_lro_client():
    client = DataPointsServiceClient(
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
    client = DataPointsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.DataPointsServiceGrpcTransport,
    )


def test_data_points_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.DataPointsServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_data_points_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.devicesandservices.health_v4.services.data_points_service.transports.DataPointsServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.DataPointsServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "get_data_point",
        "list_data_points",
        "create_data_point",
        "update_data_point",
        "batch_delete_data_points",
        "reconcile_data_points",
        "roll_up_data_points",
        "daily_roll_up_data_points",
        "export_exercise_tcx",
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


def test_data_points_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.devicesandservices.health_v4.services.data_points_service.transports.DataPointsServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.DataPointsServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly",
                "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.writeonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.readonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.writeonly",
                "https://www.googleapis.com/auth/googlehealth.location.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.writeonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.readonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.writeonly",
                "https://www.googleapis.com/auth/googlehealth.nutrition.writeonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.readonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.writeonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.readonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.writeonly",
            ),
            quota_project_id="octopus",
        )


def test_data_points_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.devicesandservices.health_v4.services.data_points_service.transports.DataPointsServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.DataPointsServiceTransport()
        adc.assert_called_once()


def test_data_points_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        DataPointsServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly",
                "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.writeonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.readonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.writeonly",
                "https://www.googleapis.com/auth/googlehealth.location.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.writeonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.readonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.writeonly",
                "https://www.googleapis.com/auth/googlehealth.nutrition.writeonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.readonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.writeonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.readonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.writeonly",
            ),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.DataPointsServiceGrpcTransport,
        transports.DataPointsServiceGrpcAsyncIOTransport,
    ],
)
def test_data_points_service_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(
                "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly",
                "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.writeonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.readonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.writeonly",
                "https://www.googleapis.com/auth/googlehealth.location.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.writeonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.readonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.writeonly",
                "https://www.googleapis.com/auth/googlehealth.nutrition.writeonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.readonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.writeonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.readonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.writeonly",
            ),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.DataPointsServiceGrpcTransport,
        transports.DataPointsServiceGrpcAsyncIOTransport,
        transports.DataPointsServiceRestTransport,
    ],
)
def test_data_points_service_transport_auth_gdch_credentials(transport_class):
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
        (transports.DataPointsServiceGrpcTransport, grpc_helpers),
        (transports.DataPointsServiceGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_data_points_service_transport_create_channel(transport_class, grpc_helpers):
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
                "https://www.googleapis.com/auth/googlehealth.activity_and_fitness.writeonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.readonly",
                "https://www.googleapis.com/auth/googlehealth.health_metrics_and_measurements.writeonly",
                "https://www.googleapis.com/auth/googlehealth.location.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.readonly",
                "https://www.googleapis.com/auth/googlehealth.logged_symptoms.writeonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.readonly",
                "https://www.googleapis.com/auth/googlehealth.mindfulness.writeonly",
                "https://www.googleapis.com/auth/googlehealth.nutrition.writeonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.readonly",
                "https://www.googleapis.com/auth/googlehealth.reproductive_health.writeonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.readonly",
                "https://www.googleapis.com/auth/googlehealth.sleep.writeonly",
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
        transports.DataPointsServiceGrpcTransport,
        transports.DataPointsServiceGrpcAsyncIOTransport,
    ],
)
def test_data_points_service_grpc_transport_client_cert_source_for_mtls(
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


def test_data_points_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.DataPointsServiceRestTransport(
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
def test_data_points_service_host_no_port(transport_name):
    client = DataPointsServiceClient(
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
def test_data_points_service_host_with_port(transport_name):
    client = DataPointsServiceClient(
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
def test_data_points_service_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = DataPointsServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = DataPointsServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.get_data_point._session
    session2 = client2.transport.get_data_point._session
    assert session1 != session2
    session1 = client1.transport.list_data_points._session
    session2 = client2.transport.list_data_points._session
    assert session1 != session2
    session1 = client1.transport.create_data_point._session
    session2 = client2.transport.create_data_point._session
    assert session1 != session2
    session1 = client1.transport.update_data_point._session
    session2 = client2.transport.update_data_point._session
    assert session1 != session2
    session1 = client1.transport.batch_delete_data_points._session
    session2 = client2.transport.batch_delete_data_points._session
    assert session1 != session2
    session1 = client1.transport.reconcile_data_points._session
    session2 = client2.transport.reconcile_data_points._session
    assert session1 != session2
    session1 = client1.transport.roll_up_data_points._session
    session2 = client2.transport.roll_up_data_points._session
    assert session1 != session2
    session1 = client1.transport.daily_roll_up_data_points._session
    session2 = client2.transport.daily_roll_up_data_points._session
    assert session1 != session2
    session1 = client1.transport.export_exercise_tcx._session
    session2 = client2.transport.export_exercise_tcx._session
    assert session1 != session2


def test_data_points_service_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.DataPointsServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_data_points_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.DataPointsServiceGrpcAsyncIOTransport(
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
        transports.DataPointsServiceGrpcTransport,
        transports.DataPointsServiceGrpcAsyncIOTransport,
    ],
)
def test_data_points_service_transport_channel_mtls_with_client_cert_source(
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
        transports.DataPointsServiceGrpcTransport,
        transports.DataPointsServiceGrpcAsyncIOTransport,
    ],
)
def test_data_points_service_transport_channel_mtls_with_adc(transport_class):
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


def test_data_points_service_grpc_lro_client():
    client = DataPointsServiceClient(
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


def test_data_points_service_grpc_lro_async_client():
    client = DataPointsServiceAsyncClient(
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


def test_data_point_path():
    user = "squid"
    data_type = "clam"
    data_point = "whelk"
    expected = "users/{user}/dataTypes/{data_type}/dataPoints/{data_point}".format(
        user=user,
        data_type=data_type,
        data_point=data_point,
    )
    actual = DataPointsServiceClient.data_point_path(user, data_type, data_point)
    assert expected == actual


def test_parse_data_point_path():
    expected = {
        "user": "octopus",
        "data_type": "oyster",
        "data_point": "nudibranch",
    }
    path = DataPointsServiceClient.data_point_path(**expected)

    # Check that the path construction is reversible.
    actual = DataPointsServiceClient.parse_data_point_path(path)
    assert expected == actual


def test_data_type_path():
    user = "cuttlefish"
    data_type = "mussel"
    expected = "users/{user}/dataTypes/{data_type}".format(
        user=user,
        data_type=data_type,
    )
    actual = DataPointsServiceClient.data_type_path(user, data_type)
    assert expected == actual


def test_parse_data_type_path():
    expected = {
        "user": "winkle",
        "data_type": "nautilus",
    }
    path = DataPointsServiceClient.data_type_path(**expected)

    # Check that the path construction is reversible.
    actual = DataPointsServiceClient.parse_data_type_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "scallop"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = DataPointsServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "abalone",
    }
    path = DataPointsServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = DataPointsServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "squid"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = DataPointsServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "clam",
    }
    path = DataPointsServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = DataPointsServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "whelk"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = DataPointsServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "octopus",
    }
    path = DataPointsServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = DataPointsServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "oyster"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = DataPointsServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "nudibranch",
    }
    path = DataPointsServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = DataPointsServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "cuttlefish"
    location = "mussel"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = DataPointsServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "winkle",
        "location": "nautilus",
    }
    path = DataPointsServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = DataPointsServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.DataPointsServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = DataPointsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.DataPointsServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = DataPointsServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_grpc():
    client = DataPointsServiceClient(
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
    client = DataPointsServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = DataPointsServiceClient(
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
        client = DataPointsServiceClient(
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
        (DataPointsServiceClient, transports.DataPointsServiceGrpcTransport),
        (
            DataPointsServiceAsyncClient,
            transports.DataPointsServiceGrpcAsyncIOTransport,
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
