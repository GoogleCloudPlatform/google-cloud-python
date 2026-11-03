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
from collections.abc import Mapping, Sequence
from unittest import mock
from unittest.mock import AsyncMock

import grpc
import pytest
from google.api_core import api_core_version
from grpc.experimental import aio
from proto.marshal.rules import wrappers
from proto.marshal.rules.dates import DurationRule, TimestampRule

try:
    from google.auth.aio import credentials as ga_credentials_async

    HAS_GOOGLE_AUTH_AIO = True
except ImportError:  # pragma: NO COVER
    HAS_GOOGLE_AUTH_AIO = False

import google.auth
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
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
from google.cloud.location import locations_pb2
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account

from google.cloud.sqladmin_v1.services.sql_instances_service import (
    SqlInstancesServiceAsyncClient,
    SqlInstancesServiceClient,
    pagers,
    transports,
)
from google.cloud.sqladmin_v1.types import cloud_sql_instances, cloud_sql_resources

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

    assert SqlInstancesServiceClient._get_client_cert_source(None, False) is None
    assert (
        SqlInstancesServiceClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        SqlInstancesServiceClient._get_client_cert_source(
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
                SqlInstancesServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                SqlInstancesServiceClient._get_client_cert_source(
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
    client = SqlInstancesServiceClient(credentials=cred)
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
    client = SqlInstancesServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (SqlInstancesServiceClient, "grpc"),
        (SqlInstancesServiceAsyncClient, "grpc_asyncio"),
    ],
)
def test_sql_instances_service_client_from_service_account_info(
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

        assert client.transport._host == ("sqladmin.googleapis.com:443")


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.SqlInstancesServiceGrpcTransport, "grpc"),
        (transports.SqlInstancesServiceGrpcAsyncIOTransport, "grpc_asyncio"),
    ],
)
def test_sql_instances_service_client_service_account_always_use_jwt(
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
        (SqlInstancesServiceClient, "grpc"),
        (SqlInstancesServiceAsyncClient, "grpc_asyncio"),
    ],
)
def test_sql_instances_service_client_from_service_account_file(
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

        assert client.transport._host == ("sqladmin.googleapis.com:443")


def test_sql_instances_service_client_get_transport_class():
    transport = SqlInstancesServiceClient.get_transport_class()
    available_transports = [
        transports.SqlInstancesServiceGrpcTransport,
    ]
    assert transport in available_transports

    transport = SqlInstancesServiceClient.get_transport_class("grpc")
    assert transport == transports.SqlInstancesServiceGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            SqlInstancesServiceClient,
            transports.SqlInstancesServiceGrpcTransport,
            "grpc",
        ),
        (
            SqlInstancesServiceAsyncClient,
            transports.SqlInstancesServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
    ],
)
@mock.patch.object(
    SqlInstancesServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(SqlInstancesServiceClient),
)
@mock.patch.object(
    SqlInstancesServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(SqlInstancesServiceAsyncClient),
)
def test_sql_instances_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(SqlInstancesServiceClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(SqlInstancesServiceClient, "get_transport_class") as gtc:
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
            SqlInstancesServiceClient,
            transports.SqlInstancesServiceGrpcTransport,
            "grpc",
            "true",
        ),
        (
            SqlInstancesServiceAsyncClient,
            transports.SqlInstancesServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            SqlInstancesServiceClient,
            transports.SqlInstancesServiceGrpcTransport,
            "grpc",
            "false",
        ),
        (
            SqlInstancesServiceAsyncClient,
            transports.SqlInstancesServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
    ],
)
@mock.patch.object(
    SqlInstancesServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(SqlInstancesServiceClient),
)
@mock.patch.object(
    SqlInstancesServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(SqlInstancesServiceAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_sql_instances_service_client_mtls_env_auto(
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
    "client_class", [SqlInstancesServiceClient, SqlInstancesServiceAsyncClient]
)
@mock.patch.object(
    SqlInstancesServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(SqlInstancesServiceClient),
)
@mock.patch.object(
    SqlInstancesServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(SqlInstancesServiceAsyncClient),
)
def test_sql_instances_service_client_get_mtls_endpoint_and_cert_source(client_class):
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
    "client_class", [SqlInstancesServiceClient, SqlInstancesServiceAsyncClient]
)
@mock.patch.object(
    SqlInstancesServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(SqlInstancesServiceClient),
)
@mock.patch.object(
    SqlInstancesServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(SqlInstancesServiceAsyncClient),
)
def test_sql_instances_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = SqlInstancesServiceClient._DEFAULT_UNIVERSE
    default_endpoint = SqlInstancesServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = SqlInstancesServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
            SqlInstancesServiceClient,
            transports.SqlInstancesServiceGrpcTransport,
            "grpc",
        ),
        (
            SqlInstancesServiceAsyncClient,
            transports.SqlInstancesServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
    ],
)
def test_sql_instances_service_client_client_options_scopes(
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
            SqlInstancesServiceClient,
            transports.SqlInstancesServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            SqlInstancesServiceAsyncClient,
            transports.SqlInstancesServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_sql_instances_service_client_client_options_credentials_file(
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


def test_sql_instances_service_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.sqladmin_v1.services.sql_instances_service.transports.SqlInstancesServiceGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = SqlInstancesServiceClient(
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
            SqlInstancesServiceClient,
            transports.SqlInstancesServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            SqlInstancesServiceAsyncClient,
            transports.SqlInstancesServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_sql_instances_service_client_create_channel_credentials_file(
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
            "sqladmin.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/sqlservice.admin",
            ),
            scopes=None,
            default_host="sqladmin.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesAddServerCaRequest(),
        {},
    ],
)
def test_add_server_ca(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.add_server_ca), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.add_server_ca(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesAddServerCaRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_add_server_ca_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesAddServerCaRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.add_server_ca), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.add_server_ca(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesAddServerCaRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_add_server_ca_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.add_server_ca in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.add_server_ca] = mock_rpc
        request = {}
        client.add_server_ca(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.add_server_ca(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_add_server_ca_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.add_server_ca
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.add_server_ca
        ] = mock_rpc

        request = {}
        await client.add_server_ca(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.add_server_ca(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesAddServerCaRequest(),
        {},
    ],
)
async def test_add_server_ca_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.add_server_ca), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.add_server_ca(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesAddServerCaRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_add_server_ca_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesAddServerCaRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.add_server_ca), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.add_server_ca(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_add_server_ca_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesAddServerCaRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.add_server_ca), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.add_server_ca(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesAddServerCertificateRequest(),
        {},
    ],
)
def test_add_server_certificate(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.add_server_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.add_server_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesAddServerCertificateRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_add_server_certificate_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesAddServerCertificateRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.add_server_certificate), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.add_server_certificate(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesAddServerCertificateRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_add_server_certificate_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.add_server_certificate
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.add_server_certificate] = (
            mock_rpc
        )
        request = {}
        client.add_server_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.add_server_certificate(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_add_server_certificate_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.add_server_certificate
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.add_server_certificate
        ] = mock_rpc

        request = {}
        await client.add_server_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.add_server_certificate(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesAddServerCertificateRequest(),
        {},
    ],
)
async def test_add_server_certificate_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.add_server_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.add_server_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesAddServerCertificateRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_add_server_certificate_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesAddServerCertificateRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.add_server_certificate), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.add_server_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_add_server_certificate_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesAddServerCertificateRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.add_server_certificate), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.add_server_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesAddEntraIdCertificateRequest(),
        {},
    ],
)
def test_add_entra_id_certificate(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.add_entra_id_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.add_entra_id_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesAddEntraIdCertificateRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_add_entra_id_certificate_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesAddEntraIdCertificateRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.add_entra_id_certificate), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.add_entra_id_certificate(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesAddEntraIdCertificateRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_add_entra_id_certificate_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.add_entra_id_certificate
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.add_entra_id_certificate
        ] = mock_rpc
        request = {}
        client.add_entra_id_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.add_entra_id_certificate(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_add_entra_id_certificate_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.add_entra_id_certificate
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.add_entra_id_certificate
        ] = mock_rpc

        request = {}
        await client.add_entra_id_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.add_entra_id_certificate(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesAddEntraIdCertificateRequest(),
        {},
    ],
)
async def test_add_entra_id_certificate_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.add_entra_id_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.add_entra_id_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesAddEntraIdCertificateRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_add_entra_id_certificate_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesAddEntraIdCertificateRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.add_entra_id_certificate), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.add_entra_id_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_add_entra_id_certificate_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesAddEntraIdCertificateRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.add_entra_id_certificate), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.add_entra_id_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesCloneRequest(),
        {},
    ],
)
def test_clone(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.clone), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.clone(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesCloneRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_clone_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesCloneRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.clone), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.clone(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesCloneRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_clone_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.clone in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.clone] = mock_rpc
        request = {}
        client.clone(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.clone(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_clone_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.clone
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.clone] = (
            mock_rpc
        )

        request = {}
        await client.clone(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.clone(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesCloneRequest(),
        {},
    ],
)
async def test_clone_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.clone), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.clone(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesCloneRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_clone_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesCloneRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.clone), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.clone(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_clone_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesCloneRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.clone), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.clone(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesDeleteRequest(),
        {},
    ],
)
def test_delete(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.delete(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesDeleteRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_delete_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesDeleteRequest(
        instance="instance_value",
        project="project_value",
        final_backup_description="final_backup_description_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.delete(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesDeleteRequest(
            instance="instance_value",
            project="project_value",
            final_backup_description="final_backup_description_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_delete_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete] = mock_rpc
        request = {}
        client.delete(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_delete_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.delete
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.delete] = (
            mock_rpc
        )

        request = {}
        await client.delete(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.delete(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesDeleteRequest(),
        {},
    ],
)
async def test_delete_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.delete(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesDeleteRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_delete_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesDeleteRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.delete(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_delete_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesDeleteRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.delete(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesDemoteMasterRequest(),
        {},
    ],
)
def test_demote_master(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.demote_master), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.demote_master(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesDemoteMasterRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_demote_master_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesDemoteMasterRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.demote_master), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.demote_master(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesDemoteMasterRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_demote_master_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.demote_master in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.demote_master] = mock_rpc
        request = {}
        client.demote_master(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.demote_master(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_demote_master_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.demote_master
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.demote_master
        ] = mock_rpc

        request = {}
        await client.demote_master(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.demote_master(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesDemoteMasterRequest(),
        {},
    ],
)
async def test_demote_master_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.demote_master), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.demote_master(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesDemoteMasterRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_demote_master_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesDemoteMasterRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.demote_master), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.demote_master(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_demote_master_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesDemoteMasterRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.demote_master), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.demote_master(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesDemoteRequest(),
        {},
    ],
)
def test_demote(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.demote), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.demote(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesDemoteRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_demote_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesDemoteRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.demote), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.demote(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesDemoteRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_demote_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.demote in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.demote] = mock_rpc
        request = {}
        client.demote(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.demote(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_demote_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.demote
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.demote] = (
            mock_rpc
        )

        request = {}
        await client.demote(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.demote(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesDemoteRequest(),
        {},
    ],
)
async def test_demote_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.demote), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.demote(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesDemoteRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_demote_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesDemoteRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.demote), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.demote(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_demote_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesDemoteRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.demote), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.demote(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesExportRequest(),
        {},
    ],
)
def test_export(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.export), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.export(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesExportRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_export_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesExportRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.export), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.export(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesExportRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_export_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.export in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.export] = mock_rpc
        request = {}
        client.export(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.export(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_export_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.export
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.export] = (
            mock_rpc
        )

        request = {}
        await client.export(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.export(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesExportRequest(),
        {},
    ],
)
async def test_export_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.export), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.export(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesExportRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_export_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesExportRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.export), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.export(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_export_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesExportRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.export), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.export(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesFailoverRequest(),
        {},
    ],
)
def test_failover(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.failover), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.failover(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesFailoverRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_failover_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesFailoverRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.failover), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.failover(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesFailoverRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_failover_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.failover in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.failover] = mock_rpc
        request = {}
        client.failover(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.failover(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_failover_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.failover
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.failover
        ] = mock_rpc

        request = {}
        await client.failover(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.failover(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesFailoverRequest(),
        {},
    ],
)
async def test_failover_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.failover), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.failover(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesFailoverRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_failover_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesFailoverRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.failover), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.failover(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_failover_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesFailoverRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.failover), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.failover(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesReencryptRequest(),
        {},
    ],
)
def test_reencrypt(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.reencrypt), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.reencrypt(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesReencryptRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_reencrypt_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesReencryptRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.reencrypt), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.reencrypt(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesReencryptRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_reencrypt_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.reencrypt in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.reencrypt] = mock_rpc
        request = {}
        client.reencrypt(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.reencrypt(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_reencrypt_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.reencrypt
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.reencrypt
        ] = mock_rpc

        request = {}
        await client.reencrypt(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.reencrypt(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesReencryptRequest(),
        {},
    ],
)
async def test_reencrypt_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.reencrypt), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.reencrypt(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesReencryptRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_reencrypt_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesReencryptRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.reencrypt), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.reencrypt(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_reencrypt_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesReencryptRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.reencrypt), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.reencrypt(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesGetRequest(),
        {},
    ],
)
def test_get(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_instances.DatabaseInstance(
            kind="kind_value",
            state=cloud_sql_instances.DatabaseInstance.SqlInstanceState.RUNNABLE,
            database_version=cloud_sql_resources.SqlDatabaseVersion.MYSQL_5_1,
            etag="etag_value",
            master_instance_name="master_instance_name_value",
            replica_names=["replica_names_value"],
            instance_type=cloud_sql_instances.SqlInstanceType.CLOUD_SQL_INSTANCE,
            project="project_value",
            ipv6_address="ipv6_address_value",
            service_account_email_address="service_account_email_address_value",
            backend_type=cloud_sql_resources.SqlBackendType.FIRST_GEN,
            self_link="self_link_value",
            suspension_reason=[cloud_sql_instances.SqlSuspensionReason.BILLING_ISSUE],
            connection_name="connection_name_value",
            name="name_value",
            region="region_value",
            gce_zone="gce_zone_value",
            secondary_gce_zone="secondary_gce_zone_value",
            root_password="root_password_value",
            database_installed_version="database_installed_version_value",
            available_maintenance_versions=["available_maintenance_versions_value"],
            maintenance_version="maintenance_version_value",
            sql_network_architecture=cloud_sql_instances.DatabaseInstance.SqlNetworkArchitecture.NEW_NETWORK_ARCHITECTURE,
            psc_service_attachment_link="psc_service_attachment_link_value",
            dns_name="dns_name_value",
            primary_dns_name="primary_dns_name_value",
            write_endpoint="write_endpoint_value",
            node_count=1070,
            database_center_integration=cloud_sql_instances.DatabaseInstance.DatabaseCenterIntegration.ENABLED,
        )
        response = client.get(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesGetRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_instances.DatabaseInstance)
    assert response.kind == "kind_value"
    assert (
        response.state == cloud_sql_instances.DatabaseInstance.SqlInstanceState.RUNNABLE
    )
    assert response.database_version == cloud_sql_resources.SqlDatabaseVersion.MYSQL_5_1
    assert response.etag == "etag_value"
    assert response.master_instance_name == "master_instance_name_value"
    assert response.replica_names == ["replica_names_value"]
    assert (
        response.instance_type == cloud_sql_instances.SqlInstanceType.CLOUD_SQL_INSTANCE
    )
    assert response.project == "project_value"
    assert response.ipv6_address == "ipv6_address_value"
    assert (
        response.service_account_email_address == "service_account_email_address_value"
    )
    assert response.backend_type == cloud_sql_resources.SqlBackendType.FIRST_GEN
    assert response.self_link == "self_link_value"
    assert response.suspension_reason == [
        cloud_sql_instances.SqlSuspensionReason.BILLING_ISSUE
    ]
    assert response.connection_name == "connection_name_value"
    assert response.name == "name_value"
    assert response.region == "region_value"
    assert response.gce_zone == "gce_zone_value"
    assert response.secondary_gce_zone == "secondary_gce_zone_value"
    assert response.root_password == "root_password_value"
    assert response.database_installed_version == "database_installed_version_value"
    assert response.available_maintenance_versions == [
        "available_maintenance_versions_value"
    ]
    assert response.maintenance_version == "maintenance_version_value"
    assert (
        response.sql_network_architecture
        == cloud_sql_instances.DatabaseInstance.SqlNetworkArchitecture.NEW_NETWORK_ARCHITECTURE
    )
    assert response.psc_service_attachment_link == "psc_service_attachment_link_value"
    assert response.dns_name == "dns_name_value"
    assert response.primary_dns_name == "primary_dns_name_value"
    assert response.write_endpoint == "write_endpoint_value"
    assert response.node_count == 1070
    assert (
        response.database_center_integration
        == cloud_sql_instances.DatabaseInstance.DatabaseCenterIntegration.ENABLED
    )


def test_get_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesGetRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesGetRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_get_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get] = mock_rpc
        request = {}
        client.get(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.get] = (
            mock_rpc
        )

        request = {}
        await client.get(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesGetRequest(),
        {},
    ],
)
async def test_get_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.DatabaseInstance(
                kind="kind_value",
                state=cloud_sql_instances.DatabaseInstance.SqlInstanceState.RUNNABLE,
                database_version=cloud_sql_resources.SqlDatabaseVersion.MYSQL_5_1,
                etag="etag_value",
                master_instance_name="master_instance_name_value",
                replica_names=["replica_names_value"],
                instance_type=cloud_sql_instances.SqlInstanceType.CLOUD_SQL_INSTANCE,
                project="project_value",
                ipv6_address="ipv6_address_value",
                service_account_email_address="service_account_email_address_value",
                backend_type=cloud_sql_resources.SqlBackendType.FIRST_GEN,
                self_link="self_link_value",
                suspension_reason=[
                    cloud_sql_instances.SqlSuspensionReason.BILLING_ISSUE
                ],
                connection_name="connection_name_value",
                name="name_value",
                region="region_value",
                gce_zone="gce_zone_value",
                secondary_gce_zone="secondary_gce_zone_value",
                root_password="root_password_value",
                database_installed_version="database_installed_version_value",
                available_maintenance_versions=["available_maintenance_versions_value"],
                maintenance_version="maintenance_version_value",
                sql_network_architecture=cloud_sql_instances.DatabaseInstance.SqlNetworkArchitecture.NEW_NETWORK_ARCHITECTURE,
                psc_service_attachment_link="psc_service_attachment_link_value",
                dns_name="dns_name_value",
                primary_dns_name="primary_dns_name_value",
                write_endpoint="write_endpoint_value",
                node_count=1070,
                database_center_integration=cloud_sql_instances.DatabaseInstance.DatabaseCenterIntegration.ENABLED,
            )
        )
        response = await client.get(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesGetRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_instances.DatabaseInstance)
    assert response.kind == "kind_value"
    assert (
        response.state == cloud_sql_instances.DatabaseInstance.SqlInstanceState.RUNNABLE
    )
    assert response.database_version == cloud_sql_resources.SqlDatabaseVersion.MYSQL_5_1
    assert response.etag == "etag_value"
    assert response.master_instance_name == "master_instance_name_value"
    assert response.replica_names == ["replica_names_value"]
    assert (
        response.instance_type == cloud_sql_instances.SqlInstanceType.CLOUD_SQL_INSTANCE
    )
    assert response.project == "project_value"
    assert response.ipv6_address == "ipv6_address_value"
    assert (
        response.service_account_email_address == "service_account_email_address_value"
    )
    assert response.backend_type == cloud_sql_resources.SqlBackendType.FIRST_GEN
    assert response.self_link == "self_link_value"
    assert response.suspension_reason == [
        cloud_sql_instances.SqlSuspensionReason.BILLING_ISSUE
    ]
    assert response.connection_name == "connection_name_value"
    assert response.name == "name_value"
    assert response.region == "region_value"
    assert response.gce_zone == "gce_zone_value"
    assert response.secondary_gce_zone == "secondary_gce_zone_value"
    assert response.root_password == "root_password_value"
    assert response.database_installed_version == "database_installed_version_value"
    assert response.available_maintenance_versions == [
        "available_maintenance_versions_value"
    ]
    assert response.maintenance_version == "maintenance_version_value"
    assert (
        response.sql_network_architecture
        == cloud_sql_instances.DatabaseInstance.SqlNetworkArchitecture.NEW_NETWORK_ARCHITECTURE
    )
    assert response.psc_service_attachment_link == "psc_service_attachment_link_value"
    assert response.dns_name == "dns_name_value"
    assert response.primary_dns_name == "primary_dns_name_value"
    assert response.write_endpoint == "write_endpoint_value"
    assert response.node_count == 1070
    assert (
        response.database_center_integration
        == cloud_sql_instances.DatabaseInstance.DatabaseCenterIntegration.ENABLED
    )


def test_get_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesGetRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get), "__call__") as call:
        call.return_value = cloud_sql_instances.DatabaseInstance()
        client.get(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesGetRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.DatabaseInstance()
        )
        await client.get(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesImportRequest(),
        {},
    ],
)
def test_import_(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.import_), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.import_(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesImportRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_import__non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesImportRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.import_), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.import_(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesImportRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_import__use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.import_ in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.import_] = mock_rpc
        request = {}
        client.import_(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.import_(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_import__async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.import_
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.import_
        ] = mock_rpc

        request = {}
        await client.import_(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.import_(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesImportRequest(),
        {},
    ],
)
async def test_import__async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.import_), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.import_(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesImportRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_import__field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesImportRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.import_), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.import_(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_import__field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesImportRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.import_), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.import_(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesInsertRequest(),
        {},
    ],
)
def test_insert(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.insert), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.insert(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesInsertRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_insert_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesInsertRequest(
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.insert), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.insert(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesInsertRequest(
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_insert_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.insert in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.insert] = mock_rpc
        request = {}
        client.insert(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.insert(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_insert_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.insert
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.insert] = (
            mock_rpc
        )

        request = {}
        await client.insert(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.insert(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesInsertRequest(),
        {},
    ],
)
async def test_insert_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.insert), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.insert(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesInsertRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesListRequest(),
        {},
    ],
)
def test_list(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_instances.InstancesListResponse(
            kind="kind_value",
            next_page_token="next_page_token_value",
        )
        response = client.list(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesListRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListPager)
    assert response.kind == "kind_value"
    assert response.next_page_token == "next_page_token_value"


def test_list_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesListRequest(
        filter="filter_value",
        page_token="page_token_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesListRequest(
            filter="filter_value",
            page_token="page_token_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_list_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list] = mock_rpc
        request = {}
        client.list(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.list] = (
            mock_rpc
        )

        request = {}
        await client.list(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesListRequest(),
        {},
    ],
)
async def test_list_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.InstancesListResponse(
                kind="kind_value",
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesListRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListAsyncPager)
    assert response.kind == "kind_value"
    assert response.next_page_token == "next_page_token_value"


def test_list_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesListRequest()

    request.project = "project_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list), "__call__") as call:
        call.return_value = cloud_sql_instances.InstancesListResponse()
        client.list(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesListRequest()

    request.project = "project_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.InstancesListResponse()
        )
        await client.list(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value",
    ) in kw["metadata"]


def test_list_pager(transport_name: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloud_sql_instances.InstancesListResponse(
                warnings=[
                    cloud_sql_resources.ApiWarning(),
                    cloud_sql_resources.ApiWarning(),
                    cloud_sql_resources.ApiWarning(),
                ],
                next_page_token="abc",
            ),
            cloud_sql_instances.InstancesListResponse(
                warnings=[],
                next_page_token="def",
            ),
            cloud_sql_instances.InstancesListResponse(
                warnings=[
                    cloud_sql_resources.ApiWarning(),
                ],
                next_page_token="ghi",
            ),
            cloud_sql_instances.InstancesListResponse(
                warnings=[
                    cloud_sql_resources.ApiWarning(),
                    cloud_sql_resources.ApiWarning(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        expected_metadata = tuple(expected_metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("project", ""),)),
        )
        pager = client.list(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, cloud_sql_resources.ApiWarning) for i in results)


def test_list_pages(transport_name: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloud_sql_instances.InstancesListResponse(
                warnings=[
                    cloud_sql_resources.ApiWarning(),
                    cloud_sql_resources.ApiWarning(),
                    cloud_sql_resources.ApiWarning(),
                ],
                next_page_token="abc",
            ),
            cloud_sql_instances.InstancesListResponse(
                warnings=[],
                next_page_token="def",
            ),
            cloud_sql_instances.InstancesListResponse(
                warnings=[
                    cloud_sql_resources.ApiWarning(),
                ],
                next_page_token="ghi",
            ),
            cloud_sql_instances.InstancesListResponse(
                warnings=[
                    cloud_sql_resources.ApiWarning(),
                    cloud_sql_resources.ApiWarning(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_async_pager():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloud_sql_instances.InstancesListResponse(
                warnings=[
                    cloud_sql_resources.ApiWarning(),
                    cloud_sql_resources.ApiWarning(),
                    cloud_sql_resources.ApiWarning(),
                ],
                next_page_token="abc",
            ),
            cloud_sql_instances.InstancesListResponse(
                warnings=[],
                next_page_token="def",
            ),
            cloud_sql_instances.InstancesListResponse(
                warnings=[
                    cloud_sql_resources.ApiWarning(),
                ],
                next_page_token="ghi",
            ),
            cloud_sql_instances.InstancesListResponse(
                warnings=[
                    cloud_sql_resources.ApiWarning(),
                    cloud_sql_resources.ApiWarning(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, cloud_sql_resources.ApiWarning) for i in responses)


@pytest.mark.asyncio
async def test_list_async_pages():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloud_sql_instances.InstancesListResponse(
                warnings=[
                    cloud_sql_resources.ApiWarning(),
                    cloud_sql_resources.ApiWarning(),
                    cloud_sql_resources.ApiWarning(),
                ],
                next_page_token="abc",
            ),
            cloud_sql_instances.InstancesListResponse(
                warnings=[],
                next_page_token="def",
            ),
            cloud_sql_instances.InstancesListResponse(
                warnings=[
                    cloud_sql_resources.ApiWarning(),
                ],
                next_page_token="ghi",
            ),
            cloud_sql_instances.InstancesListResponse(
                warnings=[
                    cloud_sql_resources.ApiWarning(),
                    cloud_sql_resources.ApiWarning(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesListServerCasRequest(),
        {},
    ],
)
def test_list_server_cas(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_server_cas), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_instances.InstancesListServerCasResponse(
            active_version="active_version_value",
            kind="kind_value",
        )
        response = client.list_server_cas(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesListServerCasRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_instances.InstancesListServerCasResponse)
    assert response.active_version == "active_version_value"
    assert response.kind == "kind_value"


def test_list_server_cas_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesListServerCasRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_server_cas), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_server_cas(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesListServerCasRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_list_server_cas_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_server_cas in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_server_cas] = mock_rpc
        request = {}
        client.list_server_cas(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_server_cas(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_server_cas_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_server_cas
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_server_cas
        ] = mock_rpc

        request = {}
        await client.list_server_cas(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_server_cas(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesListServerCasRequest(),
        {},
    ],
)
async def test_list_server_cas_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_server_cas), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.InstancesListServerCasResponse(
                active_version="active_version_value",
                kind="kind_value",
            )
        )
        response = await client.list_server_cas(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesListServerCasRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_instances.InstancesListServerCasResponse)
    assert response.active_version == "active_version_value"
    assert response.kind == "kind_value"


def test_list_server_cas_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesListServerCasRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_server_cas), "__call__") as call:
        call.return_value = cloud_sql_instances.InstancesListServerCasResponse()
        client.list_server_cas(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_server_cas_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesListServerCasRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_server_cas), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.InstancesListServerCasResponse()
        )
        await client.list_server_cas(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesListServerCertificatesRequest(),
        {},
    ],
)
def test_list_server_certificates(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_server_certificates), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_instances.InstancesListServerCertificatesResponse(
            active_version="active_version_value",
            kind="kind_value",
        )
        response = client.list_server_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesListServerCertificatesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, cloud_sql_instances.InstancesListServerCertificatesResponse
    )
    assert response.active_version == "active_version_value"
    assert response.kind == "kind_value"


def test_list_server_certificates_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesListServerCertificatesRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_server_certificates), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_server_certificates(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesListServerCertificatesRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_list_server_certificates_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_server_certificates
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_server_certificates
        ] = mock_rpc
        request = {}
        client.list_server_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_server_certificates(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_server_certificates_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_server_certificates
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_server_certificates
        ] = mock_rpc

        request = {}
        await client.list_server_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_server_certificates(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesListServerCertificatesRequest(),
        {},
    ],
)
async def test_list_server_certificates_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_server_certificates), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.InstancesListServerCertificatesResponse(
                active_version="active_version_value",
                kind="kind_value",
            )
        )
        response = await client.list_server_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesListServerCertificatesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, cloud_sql_instances.InstancesListServerCertificatesResponse
    )
    assert response.active_version == "active_version_value"
    assert response.kind == "kind_value"


def test_list_server_certificates_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesListServerCertificatesRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_server_certificates), "__call__"
    ) as call:
        call.return_value = (
            cloud_sql_instances.InstancesListServerCertificatesResponse()
        )
        client.list_server_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_server_certificates_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesListServerCertificatesRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_server_certificates), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.InstancesListServerCertificatesResponse()
        )
        await client.list_server_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesListEntraIdCertificatesRequest(),
        {},
    ],
)
def test_list_entra_id_certificates(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_entra_id_certificates), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            cloud_sql_instances.InstancesListEntraIdCertificatesResponse(
                active_version="active_version_value",
                kind="kind_value",
            )
        )
        response = client.list_entra_id_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesListEntraIdCertificatesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, cloud_sql_instances.InstancesListEntraIdCertificatesResponse
    )
    assert response.active_version == "active_version_value"
    assert response.kind == "kind_value"


def test_list_entra_id_certificates_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesListEntraIdCertificatesRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_entra_id_certificates), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_entra_id_certificates(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesListEntraIdCertificatesRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_list_entra_id_certificates_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_entra_id_certificates
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_entra_id_certificates
        ] = mock_rpc
        request = {}
        client.list_entra_id_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_entra_id_certificates(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_entra_id_certificates_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_entra_id_certificates
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_entra_id_certificates
        ] = mock_rpc

        request = {}
        await client.list_entra_id_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_entra_id_certificates(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesListEntraIdCertificatesRequest(),
        {},
    ],
)
async def test_list_entra_id_certificates_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_entra_id_certificates), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.InstancesListEntraIdCertificatesResponse(
                active_version="active_version_value",
                kind="kind_value",
            )
        )
        response = await client.list_entra_id_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesListEntraIdCertificatesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, cloud_sql_instances.InstancesListEntraIdCertificatesResponse
    )
    assert response.active_version == "active_version_value"
    assert response.kind == "kind_value"


def test_list_entra_id_certificates_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesListEntraIdCertificatesRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_entra_id_certificates), "__call__"
    ) as call:
        call.return_value = (
            cloud_sql_instances.InstancesListEntraIdCertificatesResponse()
        )
        client.list_entra_id_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_list_entra_id_certificates_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesListEntraIdCertificatesRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_entra_id_certificates), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.InstancesListEntraIdCertificatesResponse()
        )
        await client.list_entra_id_certificates(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesPatchRequest(),
        {},
    ],
)
def test_patch(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.patch), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.patch(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesPatchRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_patch_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesPatchRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.patch), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.patch(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesPatchRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_patch_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.patch in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.patch] = mock_rpc
        request = {}
        client.patch(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.patch(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_patch_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.patch
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.patch] = (
            mock_rpc
        )

        request = {}
        await client.patch(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.patch(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesPatchRequest(),
        {},
    ],
)
async def test_patch_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.patch), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.patch(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesPatchRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_patch_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesPatchRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.patch), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.patch(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_patch_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesPatchRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.patch), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.patch(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesPromoteReplicaRequest(),
        {},
    ],
)
def test_promote_replica(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.promote_replica), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.promote_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesPromoteReplicaRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_promote_replica_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesPromoteReplicaRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.promote_replica), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.promote_replica(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesPromoteReplicaRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_promote_replica_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.promote_replica in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.promote_replica] = mock_rpc
        request = {}
        client.promote_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.promote_replica(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_promote_replica_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.promote_replica
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.promote_replica
        ] = mock_rpc

        request = {}
        await client.promote_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.promote_replica(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesPromoteReplicaRequest(),
        {},
    ],
)
async def test_promote_replica_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.promote_replica), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.promote_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesPromoteReplicaRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_promote_replica_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesPromoteReplicaRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.promote_replica), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.promote_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_promote_replica_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesPromoteReplicaRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.promote_replica), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.promote_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesSwitchoverRequest(),
        {},
    ],
)
def test_switchover(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.switchover), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.switchover(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesSwitchoverRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_switchover_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesSwitchoverRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.switchover), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.switchover(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesSwitchoverRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_switchover_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.switchover in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.switchover] = mock_rpc
        request = {}
        client.switchover(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.switchover(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_switchover_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.switchover
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.switchover
        ] = mock_rpc

        request = {}
        await client.switchover(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.switchover(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesSwitchoverRequest(),
        {},
    ],
)
async def test_switchover_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.switchover), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.switchover(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesSwitchoverRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_switchover_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesSwitchoverRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.switchover), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.switchover(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_switchover_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesSwitchoverRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.switchover), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.switchover(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesResetSslConfigRequest(),
        {},
    ],
)
def test_reset_ssl_config(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.reset_ssl_config), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.reset_ssl_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesResetSslConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_reset_ssl_config_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesResetSslConfigRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.reset_ssl_config), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.reset_ssl_config(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesResetSslConfigRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_reset_ssl_config_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.reset_ssl_config in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.reset_ssl_config] = (
            mock_rpc
        )
        request = {}
        client.reset_ssl_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.reset_ssl_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_reset_ssl_config_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.reset_ssl_config
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.reset_ssl_config
        ] = mock_rpc

        request = {}
        await client.reset_ssl_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.reset_ssl_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesResetSslConfigRequest(),
        {},
    ],
)
async def test_reset_ssl_config_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.reset_ssl_config), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.reset_ssl_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesResetSslConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_reset_ssl_config_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesResetSslConfigRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.reset_ssl_config), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.reset_ssl_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_reset_ssl_config_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesResetSslConfigRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.reset_ssl_config), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.reset_ssl_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesRestartRequest(),
        {},
    ],
)
def test_restart(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.restart), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.restart(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesRestartRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_restart_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesRestartRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.restart), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.restart(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRestartRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_restart_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.restart in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.restart] = mock_rpc
        request = {}
        client.restart(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.restart(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_restart_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.restart
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.restart
        ] = mock_rpc

        request = {}
        await client.restart(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.restart(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesRestartRequest(),
        {},
    ],
)
async def test_restart_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.restart), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.restart(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesRestartRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_restart_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesRestartRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.restart), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.restart(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_restart_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesRestartRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.restart), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.restart(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesRestoreBackupRequest(),
        {},
    ],
)
def test_restore_backup(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.restore_backup), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.restore_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesRestoreBackupRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_restore_backup_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesRestoreBackupRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.restore_backup), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.restore_backup(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRestoreBackupRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_restore_backup_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.restore_backup in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.restore_backup] = mock_rpc
        request = {}
        client.restore_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.restore_backup(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_restore_backup_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.restore_backup
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.restore_backup
        ] = mock_rpc

        request = {}
        await client.restore_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.restore_backup(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesRestoreBackupRequest(),
        {},
    ],
)
async def test_restore_backup_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.restore_backup), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.restore_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesRestoreBackupRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_restore_backup_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesRestoreBackupRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.restore_backup), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.restore_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_restore_backup_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesRestoreBackupRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.restore_backup), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.restore_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesRotateServerCaRequest(),
        {},
    ],
)
def test_rotate_server_ca(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.rotate_server_ca), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.rotate_server_ca(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesRotateServerCaRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_rotate_server_ca_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesRotateServerCaRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.rotate_server_ca), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.rotate_server_ca(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRotateServerCaRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_rotate_server_ca_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.rotate_server_ca in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.rotate_server_ca] = (
            mock_rpc
        )
        request = {}
        client.rotate_server_ca(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.rotate_server_ca(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_rotate_server_ca_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.rotate_server_ca
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.rotate_server_ca
        ] = mock_rpc

        request = {}
        await client.rotate_server_ca(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.rotate_server_ca(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesRotateServerCaRequest(),
        {},
    ],
)
async def test_rotate_server_ca_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.rotate_server_ca), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.rotate_server_ca(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesRotateServerCaRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_rotate_server_ca_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesRotateServerCaRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.rotate_server_ca), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.rotate_server_ca(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_rotate_server_ca_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesRotateServerCaRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.rotate_server_ca), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.rotate_server_ca(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesRotateServerCertificateRequest(),
        {},
    ],
)
def test_rotate_server_certificate(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.rotate_server_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.rotate_server_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesRotateServerCertificateRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_rotate_server_certificate_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesRotateServerCertificateRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.rotate_server_certificate), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.rotate_server_certificate(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRotateServerCertificateRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_rotate_server_certificate_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.rotate_server_certificate
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.rotate_server_certificate
        ] = mock_rpc
        request = {}
        client.rotate_server_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.rotate_server_certificate(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_rotate_server_certificate_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.rotate_server_certificate
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.rotate_server_certificate
        ] = mock_rpc

        request = {}
        await client.rotate_server_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.rotate_server_certificate(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesRotateServerCertificateRequest(),
        {},
    ],
)
async def test_rotate_server_certificate_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.rotate_server_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.rotate_server_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesRotateServerCertificateRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_rotate_server_certificate_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesRotateServerCertificateRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.rotate_server_certificate), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.rotate_server_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_rotate_server_certificate_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesRotateServerCertificateRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.rotate_server_certificate), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.rotate_server_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesRotateEntraIdCertificateRequest(),
        {},
    ],
)
def test_rotate_entra_id_certificate(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.rotate_entra_id_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.rotate_entra_id_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesRotateEntraIdCertificateRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_rotate_entra_id_certificate_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesRotateEntraIdCertificateRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.rotate_entra_id_certificate), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.rotate_entra_id_certificate(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRotateEntraIdCertificateRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_rotate_entra_id_certificate_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.rotate_entra_id_certificate
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.rotate_entra_id_certificate
        ] = mock_rpc
        request = {}
        client.rotate_entra_id_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.rotate_entra_id_certificate(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_rotate_entra_id_certificate_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.rotate_entra_id_certificate
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.rotate_entra_id_certificate
        ] = mock_rpc

        request = {}
        await client.rotate_entra_id_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.rotate_entra_id_certificate(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesRotateEntraIdCertificateRequest(),
        {},
    ],
)
async def test_rotate_entra_id_certificate_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.rotate_entra_id_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.rotate_entra_id_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesRotateEntraIdCertificateRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_rotate_entra_id_certificate_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesRotateEntraIdCertificateRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.rotate_entra_id_certificate), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.rotate_entra_id_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_rotate_entra_id_certificate_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesRotateEntraIdCertificateRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.rotate_entra_id_certificate), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.rotate_entra_id_certificate(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesStartReplicaRequest(),
        {},
    ],
)
def test_start_replica(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.start_replica), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.start_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesStartReplicaRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_start_replica_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesStartReplicaRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.start_replica), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.start_replica(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesStartReplicaRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_start_replica_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.start_replica in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.start_replica] = mock_rpc
        request = {}
        client.start_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.start_replica(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_start_replica_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.start_replica
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.start_replica
        ] = mock_rpc

        request = {}
        await client.start_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.start_replica(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesStartReplicaRequest(),
        {},
    ],
)
async def test_start_replica_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.start_replica), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.start_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesStartReplicaRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_start_replica_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesStartReplicaRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.start_replica), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.start_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_start_replica_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesStartReplicaRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.start_replica), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.start_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesStopReplicaRequest(),
        {},
    ],
)
def test_stop_replica(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.stop_replica), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.stop_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesStopReplicaRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_stop_replica_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesStopReplicaRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.stop_replica), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.stop_replica(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesStopReplicaRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_stop_replica_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.stop_replica in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.stop_replica] = mock_rpc
        request = {}
        client.stop_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.stop_replica(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_stop_replica_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.stop_replica
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.stop_replica
        ] = mock_rpc

        request = {}
        await client.stop_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.stop_replica(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesStopReplicaRequest(),
        {},
    ],
)
async def test_stop_replica_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.stop_replica), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.stop_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesStopReplicaRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_stop_replica_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesStopReplicaRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.stop_replica), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.stop_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_stop_replica_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesStopReplicaRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.stop_replica), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.stop_replica(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesTruncateLogRequest(),
        {},
    ],
)
def test_truncate_log(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.truncate_log), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.truncate_log(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesTruncateLogRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_truncate_log_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesTruncateLogRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.truncate_log), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.truncate_log(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesTruncateLogRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_truncate_log_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.truncate_log in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.truncate_log] = mock_rpc
        request = {}
        client.truncate_log(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.truncate_log(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_truncate_log_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.truncate_log
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.truncate_log
        ] = mock_rpc

        request = {}
        await client.truncate_log(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.truncate_log(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesTruncateLogRequest(),
        {},
    ],
)
async def test_truncate_log_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.truncate_log), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.truncate_log(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesTruncateLogRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_truncate_log_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesTruncateLogRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.truncate_log), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.truncate_log(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_truncate_log_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesTruncateLogRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.truncate_log), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.truncate_log(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesUpdateRequest(),
        {},
    ],
)
def test_update(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.update(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesUpdateRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_update_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesUpdateRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesUpdateRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_update_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update] = mock_rpc
        request = {}
        client.update(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[client._client._transport.update] = (
            mock_rpc
        )

        request = {}
        await client.update(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesUpdateRequest(),
        {},
    ],
)
async def test_update_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.update(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesUpdateRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_update_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesUpdateRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.update(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesUpdateRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.update(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesCreateEphemeralCertRequest(),
        {},
    ],
)
def test_create_ephemeral(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_ephemeral), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.SslCert(
            kind="kind_value",
            cert_serial_number="cert_serial_number_value",
            cert="cert_value",
            common_name="common_name_value",
            sha1_fingerprint="sha1_fingerprint_value",
            instance="instance_value",
            self_link="self_link_value",
        )
        response = client.create_ephemeral(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesCreateEphemeralCertRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.SslCert)
    assert response.kind == "kind_value"
    assert response.cert_serial_number == "cert_serial_number_value"
    assert response.cert == "cert_value"
    assert response.common_name == "common_name_value"
    assert response.sha1_fingerprint == "sha1_fingerprint_value"
    assert response.instance == "instance_value"
    assert response.self_link == "self_link_value"


def test_create_ephemeral_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesCreateEphemeralCertRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_ephemeral), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_ephemeral(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesCreateEphemeralCertRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_create_ephemeral_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_ephemeral in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_ephemeral] = (
            mock_rpc
        )
        request = {}
        client.create_ephemeral(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_ephemeral(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_ephemeral_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_ephemeral
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_ephemeral
        ] = mock_rpc

        request = {}
        await client.create_ephemeral(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.create_ephemeral(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesCreateEphemeralCertRequest(),
        {},
    ],
)
async def test_create_ephemeral_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_ephemeral), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.SslCert(
                kind="kind_value",
                cert_serial_number="cert_serial_number_value",
                cert="cert_value",
                common_name="common_name_value",
                sha1_fingerprint="sha1_fingerprint_value",
                instance="instance_value",
                self_link="self_link_value",
            )
        )
        response = await client.create_ephemeral(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesCreateEphemeralCertRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.SslCert)
    assert response.kind == "kind_value"
    assert response.cert_serial_number == "cert_serial_number_value"
    assert response.cert == "cert_value"
    assert response.common_name == "common_name_value"
    assert response.sha1_fingerprint == "sha1_fingerprint_value"
    assert response.instance == "instance_value"
    assert response.self_link == "self_link_value"


def test_create_ephemeral_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesCreateEphemeralCertRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_ephemeral), "__call__") as call:
        call.return_value = cloud_sql_resources.SslCert()
        client.create_ephemeral(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_create_ephemeral_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesCreateEphemeralCertRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_ephemeral), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.SslCert()
        )
        await client.create_ephemeral(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesRescheduleMaintenanceRequest(),
        {},
    ],
)
def test_reschedule_maintenance(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reschedule_maintenance), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.reschedule_maintenance(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesRescheduleMaintenanceRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_reschedule_maintenance_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesRescheduleMaintenanceRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reschedule_maintenance), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.reschedule_maintenance(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRescheduleMaintenanceRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_reschedule_maintenance_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.reschedule_maintenance
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.reschedule_maintenance] = (
            mock_rpc
        )
        request = {}
        client.reschedule_maintenance(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.reschedule_maintenance(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_reschedule_maintenance_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.reschedule_maintenance
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.reschedule_maintenance
        ] = mock_rpc

        request = {}
        await client.reschedule_maintenance(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.reschedule_maintenance(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesRescheduleMaintenanceRequest(),
        {},
    ],
)
async def test_reschedule_maintenance_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reschedule_maintenance), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.reschedule_maintenance(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesRescheduleMaintenanceRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_reschedule_maintenance_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesRescheduleMaintenanceRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reschedule_maintenance), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.reschedule_maintenance(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_reschedule_maintenance_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesRescheduleMaintenanceRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reschedule_maintenance), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.reschedule_maintenance(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsRequest(),
        {},
    ],
)
def test_verify_external_sync_settings(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.verify_external_sync_settings), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsResponse(
                kind="kind_value",
            )
        )
        response = client.verify_external_sync_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsResponse
    )
    assert response.kind == "kind_value"


def test_verify_external_sync_settings_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.verify_external_sync_settings), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.verify_external_sync_settings(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_verify_external_sync_settings_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.verify_external_sync_settings
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.verify_external_sync_settings
        ] = mock_rpc
        request = {}
        client.verify_external_sync_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.verify_external_sync_settings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_verify_external_sync_settings_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.verify_external_sync_settings
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.verify_external_sync_settings
        ] = mock_rpc

        request = {}
        await client.verify_external_sync_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.verify_external_sync_settings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsRequest(),
        {},
    ],
)
async def test_verify_external_sync_settings_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.verify_external_sync_settings), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsResponse(
                kind="kind_value",
            )
        )
        response = await client.verify_external_sync_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsResponse
    )
    assert response.kind == "kind_value"


def test_verify_external_sync_settings_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.verify_external_sync_settings), "__call__"
    ) as call:
        call.return_value = (
            cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsResponse()
        )
        client.verify_external_sync_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_verify_external_sync_settings_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.verify_external_sync_settings), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsResponse()
        )
        await client.verify_external_sync_settings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesStartExternalSyncRequest(),
        {},
    ],
)
def test_start_external_sync(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.start_external_sync), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.start_external_sync(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesStartExternalSyncRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_start_external_sync_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesStartExternalSyncRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.start_external_sync), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.start_external_sync(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesStartExternalSyncRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_start_external_sync_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.start_external_sync in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.start_external_sync] = (
            mock_rpc
        )
        request = {}
        client.start_external_sync(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.start_external_sync(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_start_external_sync_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.start_external_sync
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.start_external_sync
        ] = mock_rpc

        request = {}
        await client.start_external_sync(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.start_external_sync(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesStartExternalSyncRequest(),
        {},
    ],
)
async def test_start_external_sync_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.start_external_sync), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.start_external_sync(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesStartExternalSyncRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_start_external_sync_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesStartExternalSyncRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.start_external_sync), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.start_external_sync(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_start_external_sync_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesStartExternalSyncRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.start_external_sync), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.start_external_sync(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesPerformDiskShrinkRequest(),
        {},
    ],
)
def test_perform_disk_shrink(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.perform_disk_shrink), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.perform_disk_shrink(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesPerformDiskShrinkRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_perform_disk_shrink_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesPerformDiskShrinkRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.perform_disk_shrink), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.perform_disk_shrink(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesPerformDiskShrinkRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_perform_disk_shrink_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.perform_disk_shrink in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.perform_disk_shrink] = (
            mock_rpc
        )
        request = {}
        client.perform_disk_shrink(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.perform_disk_shrink(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_perform_disk_shrink_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.perform_disk_shrink
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.perform_disk_shrink
        ] = mock_rpc

        request = {}
        await client.perform_disk_shrink(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.perform_disk_shrink(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesPerformDiskShrinkRequest(),
        {},
    ],
)
async def test_perform_disk_shrink_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.perform_disk_shrink), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.perform_disk_shrink(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesPerformDiskShrinkRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_perform_disk_shrink_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesPerformDiskShrinkRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.perform_disk_shrink), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.perform_disk_shrink(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_perform_disk_shrink_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesPerformDiskShrinkRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.perform_disk_shrink), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.perform_disk_shrink(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesGetDiskShrinkConfigRequest(),
        {},
    ],
)
def test_get_disk_shrink_config(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_disk_shrink_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_instances.SqlInstancesGetDiskShrinkConfigResponse(
            kind="kind_value",
            minimal_target_size_gb=2319,
            message="message_value",
        )
        response = client.get_disk_shrink_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesGetDiskShrinkConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, cloud_sql_instances.SqlInstancesGetDiskShrinkConfigResponse
    )
    assert response.kind == "kind_value"
    assert response.minimal_target_size_gb == 2319
    assert response.message == "message_value"


def test_get_disk_shrink_config_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesGetDiskShrinkConfigRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_disk_shrink_config), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_disk_shrink_config(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesGetDiskShrinkConfigRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_get_disk_shrink_config_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_disk_shrink_config
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_disk_shrink_config] = (
            mock_rpc
        )
        request = {}
        client.get_disk_shrink_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_disk_shrink_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_disk_shrink_config_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_disk_shrink_config
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_disk_shrink_config
        ] = mock_rpc

        request = {}
        await client.get_disk_shrink_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_disk_shrink_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesGetDiskShrinkConfigRequest(),
        {},
    ],
)
async def test_get_disk_shrink_config_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_disk_shrink_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesGetDiskShrinkConfigResponse(
                kind="kind_value",
                minimal_target_size_gb=2319,
                message="message_value",
            )
        )
        response = await client.get_disk_shrink_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesGetDiskShrinkConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, cloud_sql_instances.SqlInstancesGetDiskShrinkConfigResponse
    )
    assert response.kind == "kind_value"
    assert response.minimal_target_size_gb == 2319
    assert response.message == "message_value"


def test_get_disk_shrink_config_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesGetDiskShrinkConfigRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_disk_shrink_config), "__call__"
    ) as call:
        call.return_value = (
            cloud_sql_instances.SqlInstancesGetDiskShrinkConfigResponse()
        )
        client.get_disk_shrink_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_disk_shrink_config_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesGetDiskShrinkConfigRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_disk_shrink_config), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesGetDiskShrinkConfigResponse()
        )
        await client.get_disk_shrink_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesResetReplicaSizeRequest(),
        {},
    ],
)
def test_reset_replica_size(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reset_replica_size), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.reset_replica_size(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesResetReplicaSizeRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_reset_replica_size_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesResetReplicaSizeRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reset_replica_size), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.reset_replica_size(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesResetReplicaSizeRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_reset_replica_size_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.reset_replica_size in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.reset_replica_size] = (
            mock_rpc
        )
        request = {}
        client.reset_replica_size(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.reset_replica_size(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_reset_replica_size_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.reset_replica_size
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.reset_replica_size
        ] = mock_rpc

        request = {}
        await client.reset_replica_size(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.reset_replica_size(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesResetReplicaSizeRequest(),
        {},
    ],
)
async def test_reset_replica_size_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reset_replica_size), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.reset_replica_size(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesResetReplicaSizeRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_reset_replica_size_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesResetReplicaSizeRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reset_replica_size), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.reset_replica_size(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_reset_replica_size_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesResetReplicaSizeRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.reset_replica_size), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.reset_replica_size(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeRequest(),
        {},
    ],
)
def test_get_latest_recovery_time(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_latest_recovery_time), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeResponse(
                kind="kind_value",
            )
        )
        response = client.get_latest_recovery_time(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeResponse
    )
    assert response.kind == "kind_value"


def test_get_latest_recovery_time_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_latest_recovery_time), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_latest_recovery_time(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_get_latest_recovery_time_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_latest_recovery_time
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_latest_recovery_time
        ] = mock_rpc
        request = {}
        client.get_latest_recovery_time(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_latest_recovery_time(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_latest_recovery_time_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_latest_recovery_time
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_latest_recovery_time
        ] = mock_rpc

        request = {}
        await client.get_latest_recovery_time(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_latest_recovery_time(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeRequest(),
        {},
    ],
)
async def test_get_latest_recovery_time_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_latest_recovery_time), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeResponse(
                kind="kind_value",
            )
        )
        response = await client.get_latest_recovery_time(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeResponse
    )
    assert response.kind == "kind_value"


def test_get_latest_recovery_time_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_latest_recovery_time), "__call__"
    ) as call:
        call.return_value = (
            cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeResponse()
        )
        client.get_latest_recovery_time(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_get_latest_recovery_time_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_latest_recovery_time), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeResponse()
        )
        await client.get_latest_recovery_time(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesExecuteSqlRequest(),
        {},
    ],
)
def test_execute_sql(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.execute_sql), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_instances.SqlInstancesExecuteSqlResponse()
        response = client.execute_sql(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesExecuteSqlRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_instances.SqlInstancesExecuteSqlResponse)


def test_execute_sql_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesExecuteSqlRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.execute_sql), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.execute_sql(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesExecuteSqlRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_execute_sql_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.execute_sql in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.execute_sql] = mock_rpc
        request = {}
        client.execute_sql(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.execute_sql(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_execute_sql_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.execute_sql
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.execute_sql
        ] = mock_rpc

        request = {}
        await client.execute_sql(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.execute_sql(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesExecuteSqlRequest(),
        {},
    ],
)
async def test_execute_sql_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.execute_sql), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesExecuteSqlResponse()
        )
        response = await client.execute_sql(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesExecuteSqlRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_instances.SqlInstancesExecuteSqlResponse)


def test_execute_sql_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesExecuteSqlRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.execute_sql), "__call__") as call:
        call.return_value = cloud_sql_instances.SqlInstancesExecuteSqlResponse()
        client.execute_sql(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_execute_sql_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesExecuteSqlRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.execute_sql), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesExecuteSqlResponse()
        )
        await client.execute_sql(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesAcquireSsrsLeaseRequest(),
        {},
    ],
)
def test_acquire_ssrs_lease(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.acquire_ssrs_lease), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_instances.SqlInstancesAcquireSsrsLeaseResponse(
            operation_id="operation_id_value",
        )
        response = client.acquire_ssrs_lease(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesAcquireSsrsLeaseRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, cloud_sql_instances.SqlInstancesAcquireSsrsLeaseResponse
    )
    assert response.operation_id == "operation_id_value"


def test_acquire_ssrs_lease_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesAcquireSsrsLeaseRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.acquire_ssrs_lease), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.acquire_ssrs_lease(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesAcquireSsrsLeaseRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_acquire_ssrs_lease_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.acquire_ssrs_lease in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.acquire_ssrs_lease] = (
            mock_rpc
        )
        request = {}
        client.acquire_ssrs_lease(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.acquire_ssrs_lease(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_acquire_ssrs_lease_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.acquire_ssrs_lease
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.acquire_ssrs_lease
        ] = mock_rpc

        request = {}
        await client.acquire_ssrs_lease(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.acquire_ssrs_lease(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesAcquireSsrsLeaseRequest(),
        {},
    ],
)
async def test_acquire_ssrs_lease_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.acquire_ssrs_lease), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesAcquireSsrsLeaseResponse(
                operation_id="operation_id_value",
            )
        )
        response = await client.acquire_ssrs_lease(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesAcquireSsrsLeaseRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, cloud_sql_instances.SqlInstancesAcquireSsrsLeaseResponse
    )
    assert response.operation_id == "operation_id_value"


def test_acquire_ssrs_lease_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesAcquireSsrsLeaseRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.acquire_ssrs_lease), "__call__"
    ) as call:
        call.return_value = cloud_sql_instances.SqlInstancesAcquireSsrsLeaseResponse()
        client.acquire_ssrs_lease(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_acquire_ssrs_lease_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesAcquireSsrsLeaseRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.acquire_ssrs_lease), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesAcquireSsrsLeaseResponse()
        )
        await client.acquire_ssrs_lease(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesReleaseSsrsLeaseRequest(),
        {},
    ],
)
def test_release_ssrs_lease(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.release_ssrs_lease), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_instances.SqlInstancesReleaseSsrsLeaseResponse(
            operation_id="operation_id_value",
        )
        response = client.release_ssrs_lease(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesReleaseSsrsLeaseRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, cloud_sql_instances.SqlInstancesReleaseSsrsLeaseResponse
    )
    assert response.operation_id == "operation_id_value"


def test_release_ssrs_lease_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesReleaseSsrsLeaseRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.release_ssrs_lease), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.release_ssrs_lease(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesReleaseSsrsLeaseRequest(
            instance="instance_value",
            project="project_value",
            location="location_value",
        )
        assert args[0] == request_msg


def test_release_ssrs_lease_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.release_ssrs_lease in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.release_ssrs_lease] = (
            mock_rpc
        )
        request = {}
        client.release_ssrs_lease(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.release_ssrs_lease(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_release_ssrs_lease_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.release_ssrs_lease
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.release_ssrs_lease
        ] = mock_rpc

        request = {}
        await client.release_ssrs_lease(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.release_ssrs_lease(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesReleaseSsrsLeaseRequest(),
        {},
    ],
)
async def test_release_ssrs_lease_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.release_ssrs_lease), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesReleaseSsrsLeaseResponse(
                operation_id="operation_id_value",
            )
        )
        response = await client.release_ssrs_lease(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesReleaseSsrsLeaseRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, cloud_sql_instances.SqlInstancesReleaseSsrsLeaseResponse
    )
    assert response.operation_id == "operation_id_value"


def test_release_ssrs_lease_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesReleaseSsrsLeaseRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.release_ssrs_lease), "__call__"
    ) as call:
        call.return_value = cloud_sql_instances.SqlInstancesReleaseSsrsLeaseResponse()
        client.release_ssrs_lease(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_release_ssrs_lease_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesReleaseSsrsLeaseRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.release_ssrs_lease), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesReleaseSsrsLeaseResponse()
        )
        await client.release_ssrs_lease(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesPreCheckMajorVersionUpgradeRequest(),
        {},
    ],
)
def test_pre_check_major_version_upgrade(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.pre_check_major_version_upgrade), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.pre_check_major_version_upgrade(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesPreCheckMajorVersionUpgradeRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_pre_check_major_version_upgrade_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesPreCheckMajorVersionUpgradeRequest(
        instance="instance_value",
        project="project_value",
        location="location_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.pre_check_major_version_upgrade), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.pre_check_major_version_upgrade(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            cloud_sql_instances.SqlInstancesPreCheckMajorVersionUpgradeRequest(
                instance="instance_value",
                project="project_value",
                location="location_value",
            )
        )
        assert args[0] == request_msg


def test_pre_check_major_version_upgrade_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.pre_check_major_version_upgrade
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.pre_check_major_version_upgrade
        ] = mock_rpc
        request = {}
        client.pre_check_major_version_upgrade(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.pre_check_major_version_upgrade(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_pre_check_major_version_upgrade_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.pre_check_major_version_upgrade
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.pre_check_major_version_upgrade
        ] = mock_rpc

        request = {}
        await client.pre_check_major_version_upgrade(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.pre_check_major_version_upgrade(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesPreCheckMajorVersionUpgradeRequest(),
        {},
    ],
)
async def test_pre_check_major_version_upgrade_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.pre_check_major_version_upgrade), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.pre_check_major_version_upgrade(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesPreCheckMajorVersionUpgradeRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_pre_check_major_version_upgrade_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesPreCheckMajorVersionUpgradeRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.pre_check_major_version_upgrade), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.pre_check_major_version_upgrade(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_pre_check_major_version_upgrade_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesPreCheckMajorVersionUpgradeRequest()

    request.project = "project_value"
    request.instance = "instance_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.pre_check_major_version_upgrade), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.pre_check_major_version_upgrade(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project=project_value&instance=instance_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesPointInTimeRestoreRequest(),
        {},
    ],
)
def test_point_in_time_restore(request_type, transport: str = "grpc"):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.point_in_time_restore), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation(
            kind="kind_value",
            target_link="target_link_value",
            status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
            user="user_value",
            operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
            name="name_value",
            target_id="target_id_value",
            self_link="self_link_value",
            target_project="target_project_value",
        )
        response = client.point_in_time_restore(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesPointInTimeRestoreRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_point_in_time_restore_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql_instances.SqlInstancesPointInTimeRestoreRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.point_in_time_restore), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.point_in_time_restore(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesPointInTimeRestoreRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_point_in_time_restore_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.point_in_time_restore
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.point_in_time_restore] = (
            mock_rpc
        )
        request = {}
        client.point_in_time_restore(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.point_in_time_restore(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_point_in_time_restore_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlInstancesServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.point_in_time_restore
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.point_in_time_restore
        ] = mock_rpc

        request = {}
        await client.point_in_time_restore(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.point_in_time_restore(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql_instances.SqlInstancesPointInTimeRestoreRequest(),
        {},
    ],
)
async def test_point_in_time_restore_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.point_in_time_restore), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        response = await client.point_in_time_restore(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql_instances.SqlInstancesPointInTimeRestoreRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Operation)
    assert response.kind == "kind_value"
    assert response.target_link == "target_link_value"
    assert response.status == cloud_sql_resources.Operation.SqlOperationStatus.PENDING
    assert response.user == "user_value"
    assert (
        response.operation_type == cloud_sql_resources.Operation.SqlOperationType.IMPORT
    )
    assert response.name == "name_value"
    assert response.target_id == "target_id_value"
    assert response.self_link == "self_link_value"
    assert response.target_project == "target_project_value"


def test_point_in_time_restore_field_headers():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesPointInTimeRestoreRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.point_in_time_restore), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.point_in_time_restore(request)

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
async def test_point_in_time_restore_field_headers_async():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql_instances.SqlInstancesPointInTimeRestoreRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.point_in_time_restore), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.point_in_time_restore(request)

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


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.SqlInstancesServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.SqlInstancesServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = SqlInstancesServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.SqlInstancesServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = SqlInstancesServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = SqlInstancesServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.SqlInstancesServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = SqlInstancesServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.SqlInstancesServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = SqlInstancesServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.SqlInstancesServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.SqlInstancesServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.SqlInstancesServiceGrpcTransport,
        transports.SqlInstancesServiceGrpcAsyncIOTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = SqlInstancesServiceClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_add_server_ca_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.add_server_ca), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.add_server_ca(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesAddServerCaRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_add_server_certificate_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.add_server_certificate), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.add_server_certificate(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesAddServerCertificateRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_add_entra_id_certificate_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.add_entra_id_certificate), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.add_entra_id_certificate(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesAddEntraIdCertificateRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_clone_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.clone), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.clone(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesCloneRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.delete), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.delete(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesDeleteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_demote_master_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.demote_master), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.demote_master(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesDemoteMasterRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_demote_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.demote), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.demote(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesDemoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_export_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.export), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.export(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesExportRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_failover_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.failover), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.failover(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesFailoverRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_reencrypt_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.reencrypt), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.reencrypt(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesReencryptRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get), "__call__") as call:
        call.return_value = cloud_sql_instances.DatabaseInstance()
        client.get(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesGetRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_import__empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.import_), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.import_(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesImportRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_insert_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.insert), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.insert(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesInsertRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list), "__call__") as call:
        call.return_value = cloud_sql_instances.InstancesListResponse()
        client.list(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesListRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_server_cas_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_server_cas), "__call__") as call:
        call.return_value = cloud_sql_instances.InstancesListServerCasResponse()
        client.list_server_cas(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesListServerCasRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_server_certificates_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_server_certificates), "__call__"
    ) as call:
        call.return_value = (
            cloud_sql_instances.InstancesListServerCertificatesResponse()
        )
        client.list_server_certificates(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesListServerCertificatesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_entra_id_certificates_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_entra_id_certificates), "__call__"
    ) as call:
        call.return_value = (
            cloud_sql_instances.InstancesListEntraIdCertificatesResponse()
        )
        client.list_entra_id_certificates(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesListEntraIdCertificatesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_patch_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.patch), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.patch(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesPatchRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_promote_replica_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.promote_replica), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.promote_replica(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesPromoteReplicaRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_switchover_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.switchover), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.switchover(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesSwitchoverRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_reset_ssl_config_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.reset_ssl_config), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.reset_ssl_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesResetSslConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_restart_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.restart), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.restart(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRestartRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_restore_backup_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.restore_backup), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.restore_backup(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRestoreBackupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_rotate_server_ca_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.rotate_server_ca), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.rotate_server_ca(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRotateServerCaRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_rotate_server_certificate_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.rotate_server_certificate), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.rotate_server_certificate(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRotateServerCertificateRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_rotate_entra_id_certificate_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.rotate_entra_id_certificate), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.rotate_entra_id_certificate(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRotateEntraIdCertificateRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_start_replica_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.start_replica), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.start_replica(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesStartReplicaRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_stop_replica_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.stop_replica), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.stop_replica(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesStopReplicaRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_truncate_log_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.truncate_log), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.truncate_log(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesTruncateLogRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.update(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesUpdateRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_ephemeral_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_ephemeral), "__call__") as call:
        call.return_value = cloud_sql_resources.SslCert()
        client.create_ephemeral(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesCreateEphemeralCertRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_reschedule_maintenance_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.reschedule_maintenance), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.reschedule_maintenance(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRescheduleMaintenanceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_verify_external_sync_settings_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.verify_external_sync_settings), "__call__"
    ) as call:
        call.return_value = (
            cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsResponse()
        )
        client.verify_external_sync_settings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_start_external_sync_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.start_external_sync), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.start_external_sync(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesStartExternalSyncRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_perform_disk_shrink_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.perform_disk_shrink), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.perform_disk_shrink(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesPerformDiskShrinkRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_disk_shrink_config_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_disk_shrink_config), "__call__"
    ) as call:
        call.return_value = (
            cloud_sql_instances.SqlInstancesGetDiskShrinkConfigResponse()
        )
        client.get_disk_shrink_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesGetDiskShrinkConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_reset_replica_size_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.reset_replica_size), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.reset_replica_size(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesResetReplicaSizeRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_latest_recovery_time_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_latest_recovery_time), "__call__"
    ) as call:
        call.return_value = (
            cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeResponse()
        )
        client.get_latest_recovery_time(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_execute_sql_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.execute_sql), "__call__") as call:
        call.return_value = cloud_sql_instances.SqlInstancesExecuteSqlResponse()
        client.execute_sql(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesExecuteSqlRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_acquire_ssrs_lease_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.acquire_ssrs_lease), "__call__"
    ) as call:
        call.return_value = cloud_sql_instances.SqlInstancesAcquireSsrsLeaseResponse()
        client.acquire_ssrs_lease(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesAcquireSsrsLeaseRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_release_ssrs_lease_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.release_ssrs_lease), "__call__"
    ) as call:
        call.return_value = cloud_sql_instances.SqlInstancesReleaseSsrsLeaseResponse()
        client.release_ssrs_lease(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesReleaseSsrsLeaseRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_pre_check_major_version_upgrade_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.pre_check_major_version_upgrade), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.pre_check_major_version_upgrade(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            cloud_sql_instances.SqlInstancesPreCheckMajorVersionUpgradeRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_point_in_time_restore_empty_call_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.point_in_time_restore), "__call__"
    ) as call:
        call.return_value = cloud_sql_resources.Operation()
        client.point_in_time_restore(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesPointInTimeRestoreRequest()
        assert args[0] == request_msg


def test_insert_routing_parameters_request_1_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.insert), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.insert(request={"project": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesInsertRequest(
            **{"project": "sample1"}
        )
        assert args[0] == request_msg

        expected_headers = {"project": "sample1"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_insert_routing_parameters_request_2_grpc():
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.insert), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.insert(request={"body": {"region": "sample1"}})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesInsertRequest(
            **{"body": {"region": "sample1"}}
        )
        assert args[0] == request_msg

        expected_headers = {"region": "sample1"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_transport_kind_grpc_asyncio():
    transport = SqlInstancesServiceAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_add_server_ca_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.add_server_ca), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.add_server_ca(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesAddServerCaRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_add_server_certificate_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.add_server_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.add_server_certificate(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesAddServerCertificateRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_add_entra_id_certificate_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.add_entra_id_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.add_entra_id_certificate(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesAddEntraIdCertificateRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_clone_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.clone), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.clone(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesCloneRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.delete), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.delete(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesDeleteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_demote_master_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.demote_master), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.demote_master(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesDemoteMasterRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_demote_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.demote), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.demote(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesDemoteRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_export_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.export), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.export(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesExportRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_failover_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.failover), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.failover(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesFailoverRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_reencrypt_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.reencrypt), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.reencrypt(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesReencryptRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.DatabaseInstance(
                kind="kind_value",
                state=cloud_sql_instances.DatabaseInstance.SqlInstanceState.RUNNABLE,
                database_version=cloud_sql_resources.SqlDatabaseVersion.MYSQL_5_1,
                etag="etag_value",
                master_instance_name="master_instance_name_value",
                replica_names=["replica_names_value"],
                instance_type=cloud_sql_instances.SqlInstanceType.CLOUD_SQL_INSTANCE,
                project="project_value",
                ipv6_address="ipv6_address_value",
                service_account_email_address="service_account_email_address_value",
                backend_type=cloud_sql_resources.SqlBackendType.FIRST_GEN,
                self_link="self_link_value",
                suspension_reason=[
                    cloud_sql_instances.SqlSuspensionReason.BILLING_ISSUE
                ],
                connection_name="connection_name_value",
                name="name_value",
                region="region_value",
                gce_zone="gce_zone_value",
                secondary_gce_zone="secondary_gce_zone_value",
                root_password="root_password_value",
                database_installed_version="database_installed_version_value",
                available_maintenance_versions=["available_maintenance_versions_value"],
                maintenance_version="maintenance_version_value",
                sql_network_architecture=cloud_sql_instances.DatabaseInstance.SqlNetworkArchitecture.NEW_NETWORK_ARCHITECTURE,
                psc_service_attachment_link="psc_service_attachment_link_value",
                dns_name="dns_name_value",
                primary_dns_name="primary_dns_name_value",
                write_endpoint="write_endpoint_value",
                node_count=1070,
                database_center_integration=cloud_sql_instances.DatabaseInstance.DatabaseCenterIntegration.ENABLED,
            )
        )
        await client.get(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesGetRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_import__empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.import_), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.import_(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesImportRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_insert_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.insert), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.insert(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesInsertRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.InstancesListResponse(
                kind="kind_value",
                next_page_token="next_page_token_value",
            )
        )
        await client.list(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesListRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_server_cas_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_server_cas), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.InstancesListServerCasResponse(
                active_version="active_version_value",
                kind="kind_value",
            )
        )
        await client.list_server_cas(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesListServerCasRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_server_certificates_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_server_certificates), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.InstancesListServerCertificatesResponse(
                active_version="active_version_value",
                kind="kind_value",
            )
        )
        await client.list_server_certificates(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesListServerCertificatesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_entra_id_certificates_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_entra_id_certificates), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.InstancesListEntraIdCertificatesResponse(
                active_version="active_version_value",
                kind="kind_value",
            )
        )
        await client.list_entra_id_certificates(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesListEntraIdCertificatesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_patch_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.patch), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.patch(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesPatchRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_promote_replica_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.promote_replica), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.promote_replica(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesPromoteReplicaRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_switchover_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.switchover), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.switchover(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesSwitchoverRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_reset_ssl_config_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.reset_ssl_config), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.reset_ssl_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesResetSslConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_restart_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.restart), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.restart(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRestartRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_restore_backup_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.restore_backup), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.restore_backup(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRestoreBackupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_rotate_server_ca_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.rotate_server_ca), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.rotate_server_ca(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRotateServerCaRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_rotate_server_certificate_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.rotate_server_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.rotate_server_certificate(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRotateServerCertificateRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_rotate_entra_id_certificate_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.rotate_entra_id_certificate), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.rotate_entra_id_certificate(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRotateEntraIdCertificateRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_start_replica_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.start_replica), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.start_replica(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesStartReplicaRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_stop_replica_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.stop_replica), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.stop_replica(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesStopReplicaRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_truncate_log_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.truncate_log), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.truncate_log(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesTruncateLogRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.update(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesUpdateRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_ephemeral_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_ephemeral), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.SslCert(
                kind="kind_value",
                cert_serial_number="cert_serial_number_value",
                cert="cert_value",
                common_name="common_name_value",
                sha1_fingerprint="sha1_fingerprint_value",
                instance="instance_value",
                self_link="self_link_value",
            )
        )
        await client.create_ephemeral(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesCreateEphemeralCertRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_reschedule_maintenance_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.reschedule_maintenance), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.reschedule_maintenance(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesRescheduleMaintenanceRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_verify_external_sync_settings_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.verify_external_sync_settings), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsResponse(
                kind="kind_value",
            )
        )
        await client.verify_external_sync_settings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            cloud_sql_instances.SqlInstancesVerifyExternalSyncSettingsRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_start_external_sync_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.start_external_sync), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.start_external_sync(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesStartExternalSyncRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_perform_disk_shrink_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.perform_disk_shrink), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.perform_disk_shrink(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesPerformDiskShrinkRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_disk_shrink_config_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_disk_shrink_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesGetDiskShrinkConfigResponse(
                kind="kind_value",
                minimal_target_size_gb=2319,
                message="message_value",
            )
        )
        await client.get_disk_shrink_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesGetDiskShrinkConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_reset_replica_size_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.reset_replica_size), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.reset_replica_size(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesResetReplicaSizeRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_latest_recovery_time_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_latest_recovery_time), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeResponse(
                kind="kind_value",
            )
        )
        await client.get_latest_recovery_time(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesGetLatestRecoveryTimeRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_execute_sql_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.execute_sql), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesExecuteSqlResponse()
        )
        await client.execute_sql(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesExecuteSqlRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_acquire_ssrs_lease_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.acquire_ssrs_lease), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesAcquireSsrsLeaseResponse(
                operation_id="operation_id_value",
            )
        )
        await client.acquire_ssrs_lease(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesAcquireSsrsLeaseRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_release_ssrs_lease_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.release_ssrs_lease), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_instances.SqlInstancesReleaseSsrsLeaseResponse(
                operation_id="operation_id_value",
            )
        )
        await client.release_ssrs_lease(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesReleaseSsrsLeaseRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_pre_check_major_version_upgrade_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.pre_check_major_version_upgrade), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.pre_check_major_version_upgrade(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            cloud_sql_instances.SqlInstancesPreCheckMajorVersionUpgradeRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_point_in_time_restore_empty_call_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.point_in_time_restore), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.point_in_time_restore(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesPointInTimeRestoreRequest()
        assert args[0] == request_msg


@pytest.mark.asyncio
async def test_insert_routing_parameters_request_1_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.insert), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.insert(request={"project": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesInsertRequest(
            **{"project": "sample1"}
        )
        assert args[0] == request_msg

        expected_headers = {"project": "sample1"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_insert_routing_parameters_request_2_grpc_asyncio():
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.insert), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation(
                kind="kind_value",
                target_link="target_link_value",
                status=cloud_sql_resources.Operation.SqlOperationStatus.PENDING,
                user="user_value",
                operation_type=cloud_sql_resources.Operation.SqlOperationType.IMPORT,
                name="name_value",
                target_id="target_id_value",
                self_link="self_link_value",
                target_project="target_project_value",
            )
        )
        await client.insert(request={"body": {"region": "sample1"}})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloud_sql_instances.SqlInstancesInsertRequest(
            **{"body": {"region": "sample1"}}
        )
        assert args[0] == request_msg

        expected_headers = {"region": "sample1"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.SqlInstancesServiceGrpcTransport,
    )


def test_sql_instances_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.SqlInstancesServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_sql_instances_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.sqladmin_v1.services.sql_instances_service.transports.SqlInstancesServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.SqlInstancesServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "add_server_ca",
        "add_server_certificate",
        "add_entra_id_certificate",
        "clone",
        "delete",
        "demote_master",
        "demote",
        "export",
        "failover",
        "reencrypt",
        "get",
        "import_",
        "insert",
        "list",
        "list_server_cas",
        "list_server_certificates",
        "list_entra_id_certificates",
        "patch",
        "promote_replica",
        "switchover",
        "reset_ssl_config",
        "restart",
        "restore_backup",
        "rotate_server_ca",
        "rotate_server_certificate",
        "rotate_entra_id_certificate",
        "start_replica",
        "stop_replica",
        "truncate_log",
        "update",
        "create_ephemeral",
        "reschedule_maintenance",
        "verify_external_sync_settings",
        "start_external_sync",
        "perform_disk_shrink",
        "get_disk_shrink_config",
        "reset_replica_size",
        "get_latest_recovery_time",
        "execute_sql",
        "acquire_ssrs_lease",
        "release_ssrs_lease",
        "pre_check_major_version_upgrade",
        "point_in_time_restore",
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


def test_sql_instances_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.cloud.sqladmin_v1.services.sql_instances_service.transports.SqlInstancesServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.SqlInstancesServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/sqlservice.admin",
            ),
            quota_project_id="octopus",
        )


def test_sql_instances_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.cloud.sqladmin_v1.services.sql_instances_service.transports.SqlInstancesServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.SqlInstancesServiceTransport()
        adc.assert_called_once()


def test_sql_instances_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        SqlInstancesServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/sqlservice.admin",
            ),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.SqlInstancesServiceGrpcTransport,
        transports.SqlInstancesServiceGrpcAsyncIOTransport,
    ],
)
def test_sql_instances_service_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/sqlservice.admin",
            ),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.SqlInstancesServiceGrpcTransport,
        transports.SqlInstancesServiceGrpcAsyncIOTransport,
    ],
)
def test_sql_instances_service_transport_auth_gdch_credentials(transport_class):
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
        (transports.SqlInstancesServiceGrpcTransport, grpc_helpers),
        (transports.SqlInstancesServiceGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_sql_instances_service_transport_create_channel(transport_class, grpc_helpers):
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
            "sqladmin.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/sqlservice.admin",
            ),
            scopes=["1", "2"],
            default_host="sqladmin.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.SqlInstancesServiceGrpcTransport,
        transports.SqlInstancesServiceGrpcAsyncIOTransport,
    ],
)
def test_sql_instances_service_grpc_transport_client_cert_source_for_mtls(
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


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
    ],
)
def test_sql_instances_service_host_no_port(transport_name):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="sqladmin.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == ("sqladmin.googleapis.com:443")


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
    ],
)
def test_sql_instances_service_host_with_port(transport_name):
    client = SqlInstancesServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="sqladmin.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == ("sqladmin.googleapis.com:8000")


def test_sql_instances_service_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.SqlInstancesServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_sql_instances_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.SqlInstancesServiceGrpcAsyncIOTransport(
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
        transports.SqlInstancesServiceGrpcTransport,
        transports.SqlInstancesServiceGrpcAsyncIOTransport,
    ],
)
def test_sql_instances_service_transport_channel_mtls_with_client_cert_source(
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
        transports.SqlInstancesServiceGrpcTransport,
        transports.SqlInstancesServiceGrpcAsyncIOTransport,
    ],
)
def test_sql_instances_service_transport_channel_mtls_with_adc(transport_class):
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


def test_backup_path():
    project = "squid"
    backup = "clam"
    expected = "projects/{project}/backups/{backup}".format(
        project=project,
        backup=backup,
    )
    actual = SqlInstancesServiceClient.backup_path(project, backup)
    assert expected == actual


def test_parse_backup_path():
    expected = {
        "project": "whelk",
        "backup": "octopus",
    }
    path = SqlInstancesServiceClient.backup_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlInstancesServiceClient.parse_backup_path(path)
    assert expected == actual


def test_backup_dr_backup_path():
    project = "oyster"
    location = "nudibranch"
    backupvault = "cuttlefish"
    datasource = "mussel"
    backup = "winkle"
    expected = "projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}/backups/{backup}".format(
        project=project,
        location=location,
        backupvault=backupvault,
        datasource=datasource,
        backup=backup,
    )
    actual = SqlInstancesServiceClient.backup_dr_backup_path(
        project, location, backupvault, datasource, backup
    )
    assert expected == actual


def test_parse_backup_dr_backup_path():
    expected = {
        "project": "nautilus",
        "location": "scallop",
        "backupvault": "abalone",
        "datasource": "squid",
        "backup": "clam",
    }
    path = SqlInstancesServiceClient.backup_dr_backup_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlInstancesServiceClient.parse_backup_dr_backup_path(path)
    assert expected == actual


def test_crypto_key_path():
    project = "whelk"
    location = "octopus"
    key_ring = "oyster"
    crypto_key = "nudibranch"
    expected = "projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}".format(
        project=project,
        location=location,
        key_ring=key_ring,
        crypto_key=crypto_key,
    )
    actual = SqlInstancesServiceClient.crypto_key_path(
        project, location, key_ring, crypto_key
    )
    assert expected == actual


def test_parse_crypto_key_path():
    expected = {
        "project": "cuttlefish",
        "location": "mussel",
        "key_ring": "winkle",
        "crypto_key": "nautilus",
    }
    path = SqlInstancesServiceClient.crypto_key_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlInstancesServiceClient.parse_crypto_key_path(path)
    assert expected == actual


def test_crypto_key_version_path():
    project = "scallop"
    location = "abalone"
    key_ring = "squid"
    crypto_key = "clam"
    crypto_key_version = "whelk"
    expected = "projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}".format(
        project=project,
        location=location,
        key_ring=key_ring,
        crypto_key=crypto_key,
        crypto_key_version=crypto_key_version,
    )
    actual = SqlInstancesServiceClient.crypto_key_version_path(
        project, location, key_ring, crypto_key, crypto_key_version
    )
    assert expected == actual


def test_parse_crypto_key_version_path():
    expected = {
        "project": "octopus",
        "location": "oyster",
        "key_ring": "nudibranch",
        "crypto_key": "cuttlefish",
        "crypto_key_version": "mussel",
    }
    path = SqlInstancesServiceClient.crypto_key_version_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlInstancesServiceClient.parse_crypto_key_version_path(path)
    assert expected == actual


def test_network_path():
    project = "winkle"
    network = "nautilus"
    expected = "projects/{project}/global/networks/{network}".format(
        project=project,
        network=network,
    )
    actual = SqlInstancesServiceClient.network_path(project, network)
    assert expected == actual


def test_parse_network_path():
    expected = {
        "project": "scallop",
        "network": "abalone",
    }
    path = SqlInstancesServiceClient.network_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlInstancesServiceClient.parse_network_path(path)
    assert expected == actual


def test_network_attachment_path():
    project = "squid"
    region = "clam"
    network_attachment = "whelk"
    expected = "projects/{project}/regions/{region}/networkAttachments/{network_attachment}".format(
        project=project,
        region=region,
        network_attachment=network_attachment,
    )
    actual = SqlInstancesServiceClient.network_attachment_path(
        project, region, network_attachment
    )
    assert expected == actual


def test_parse_network_attachment_path():
    expected = {
        "project": "octopus",
        "region": "oyster",
        "network_attachment": "nudibranch",
    }
    path = SqlInstancesServiceClient.network_attachment_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlInstancesServiceClient.parse_network_attachment_path(path)
    assert expected == actual


def test_secret_version_path():
    project = "cuttlefish"
    secret = "mussel"
    secret_version = "winkle"
    expected = "projects/{project}/secrets/{secret}/versions/{secret_version}".format(
        project=project,
        secret=secret,
        secret_version=secret_version,
    )
    actual = SqlInstancesServiceClient.secret_version_path(
        project, secret, secret_version
    )
    assert expected == actual


def test_parse_secret_version_path():
    expected = {
        "project": "nautilus",
        "secret": "scallop",
        "secret_version": "abalone",
    }
    path = SqlInstancesServiceClient.secret_version_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlInstancesServiceClient.parse_secret_version_path(path)
    assert expected == actual


def test_service_connection_policy_path():
    project = "squid"
    region = "clam"
    service_connection_policy = "whelk"
    expected = "projects/{project}/regions/{region}/serviceConnectionPolicies/{service_connection_policy}".format(
        project=project,
        region=region,
        service_connection_policy=service_connection_policy,
    )
    actual = SqlInstancesServiceClient.service_connection_policy_path(
        project, region, service_connection_policy
    )
    assert expected == actual


def test_parse_service_connection_policy_path():
    expected = {
        "project": "octopus",
        "region": "oyster",
        "service_connection_policy": "nudibranch",
    }
    path = SqlInstancesServiceClient.service_connection_policy_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlInstancesServiceClient.parse_service_connection_policy_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "cuttlefish"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = SqlInstancesServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "mussel",
    }
    path = SqlInstancesServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlInstancesServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "winkle"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = SqlInstancesServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "nautilus",
    }
    path = SqlInstancesServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlInstancesServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "scallop"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = SqlInstancesServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "abalone",
    }
    path = SqlInstancesServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlInstancesServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "squid"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = SqlInstancesServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "clam",
    }
    path = SqlInstancesServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlInstancesServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "whelk"
    location = "octopus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = SqlInstancesServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
    }
    path = SqlInstancesServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlInstancesServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.SqlInstancesServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = SqlInstancesServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.SqlInstancesServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = SqlInstancesServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_grpc():
    client = SqlInstancesServiceClient(
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
    client = SqlInstancesServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_client_ctx():
    transports = [
        "grpc",
    ]
    for transport in transports:
        client = SqlInstancesServiceClient(
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
        (SqlInstancesServiceClient, transports.SqlInstancesServiceGrpcTransport),
        (
            SqlInstancesServiceAsyncClient,
            transports.SqlInstancesServiceGrpcAsyncIOTransport,
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
