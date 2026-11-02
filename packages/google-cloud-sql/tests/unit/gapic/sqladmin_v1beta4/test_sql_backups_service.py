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
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
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

from google.cloud.sqladmin_v1beta4.services.sql_backups_service import (
    SqlBackupsServiceAsyncClient,
    SqlBackupsServiceClient,
    pagers,
    transports,
)
from google.cloud.sqladmin_v1beta4.types import cloud_sql, cloud_sql_resources

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

    assert SqlBackupsServiceClient._get_client_cert_source(None, False) is None
    assert (
        SqlBackupsServiceClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        SqlBackupsServiceClient._get_client_cert_source(mock_provided_cert_source, True)
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
                SqlBackupsServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                SqlBackupsServiceClient._get_client_cert_source(
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
    client = SqlBackupsServiceClient(credentials=cred)
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
    client = SqlBackupsServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (SqlBackupsServiceClient, "grpc"),
        (SqlBackupsServiceAsyncClient, "grpc_asyncio"),
        (SqlBackupsServiceClient, "rest"),
    ],
)
def test_sql_backups_service_client_from_service_account_info(
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
            "sqladmin.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://sqladmin.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.SqlBackupsServiceGrpcTransport, "grpc"),
        (transports.SqlBackupsServiceGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.SqlBackupsServiceRestTransport, "rest"),
    ],
)
def test_sql_backups_service_client_service_account_always_use_jwt(
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
        (SqlBackupsServiceClient, "grpc"),
        (SqlBackupsServiceAsyncClient, "grpc_asyncio"),
        (SqlBackupsServiceClient, "rest"),
    ],
)
def test_sql_backups_service_client_from_service_account_file(
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
            "sqladmin.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://sqladmin.googleapis.com"
        )


def test_sql_backups_service_client_get_transport_class():
    transport = SqlBackupsServiceClient.get_transport_class()
    available_transports = [
        transports.SqlBackupsServiceGrpcTransport,
        transports.SqlBackupsServiceRestTransport,
    ]
    assert transport in available_transports

    transport = SqlBackupsServiceClient.get_transport_class("grpc")
    assert transport == transports.SqlBackupsServiceGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (SqlBackupsServiceClient, transports.SqlBackupsServiceGrpcTransport, "grpc"),
        (
            SqlBackupsServiceAsyncClient,
            transports.SqlBackupsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (SqlBackupsServiceClient, transports.SqlBackupsServiceRestTransport, "rest"),
    ],
)
@mock.patch.object(
    SqlBackupsServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(SqlBackupsServiceClient),
)
@mock.patch.object(
    SqlBackupsServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(SqlBackupsServiceAsyncClient),
)
def test_sql_backups_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(SqlBackupsServiceClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(SqlBackupsServiceClient, "get_transport_class") as gtc:
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
            SqlBackupsServiceClient,
            transports.SqlBackupsServiceGrpcTransport,
            "grpc",
            "true",
        ),
        (
            SqlBackupsServiceAsyncClient,
            transports.SqlBackupsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            SqlBackupsServiceClient,
            transports.SqlBackupsServiceGrpcTransport,
            "grpc",
            "false",
        ),
        (
            SqlBackupsServiceAsyncClient,
            transports.SqlBackupsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (
            SqlBackupsServiceClient,
            transports.SqlBackupsServiceRestTransport,
            "rest",
            "true",
        ),
        (
            SqlBackupsServiceClient,
            transports.SqlBackupsServiceRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    SqlBackupsServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(SqlBackupsServiceClient),
)
@mock.patch.object(
    SqlBackupsServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(SqlBackupsServiceAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_sql_backups_service_client_mtls_env_auto(
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
    "client_class", [SqlBackupsServiceClient, SqlBackupsServiceAsyncClient]
)
@mock.patch.object(
    SqlBackupsServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(SqlBackupsServiceClient),
)
@mock.patch.object(
    SqlBackupsServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(SqlBackupsServiceAsyncClient),
)
def test_sql_backups_service_client_get_mtls_endpoint_and_cert_source(client_class):
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
    "client_class", [SqlBackupsServiceClient, SqlBackupsServiceAsyncClient]
)
@mock.patch.object(
    SqlBackupsServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(SqlBackupsServiceClient),
)
@mock.patch.object(
    SqlBackupsServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(SqlBackupsServiceAsyncClient),
)
def test_sql_backups_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = SqlBackupsServiceClient._DEFAULT_UNIVERSE
    default_endpoint = SqlBackupsServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = SqlBackupsServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
        (SqlBackupsServiceClient, transports.SqlBackupsServiceGrpcTransport, "grpc"),
        (
            SqlBackupsServiceAsyncClient,
            transports.SqlBackupsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (SqlBackupsServiceClient, transports.SqlBackupsServiceRestTransport, "rest"),
    ],
)
def test_sql_backups_service_client_client_options_scopes(
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
            SqlBackupsServiceClient,
            transports.SqlBackupsServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            SqlBackupsServiceAsyncClient,
            transports.SqlBackupsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (
            SqlBackupsServiceClient,
            transports.SqlBackupsServiceRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_sql_backups_service_client_client_options_credentials_file(
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


def test_sql_backups_service_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.sqladmin_v1beta4.services.sql_backups_service.transports.SqlBackupsServiceGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = SqlBackupsServiceClient(
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
            SqlBackupsServiceClient,
            transports.SqlBackupsServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            SqlBackupsServiceAsyncClient,
            transports.SqlBackupsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_sql_backups_service_client_create_channel_credentials_file(
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
        cloud_sql.CreateBackupRequest(),
        {},
    ],
)
def test_create_backup(request_type, transport: str = "grpc"):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_backup), "__call__") as call:
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
        response = client.create_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql.CreateBackupRequest()
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


def test_create_backup_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql.CreateBackupRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_backup), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_backup(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.CreateBackupRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_create_backup_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_backup in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_backup] = mock_rpc
        request = {}
        client.create_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_backup(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_backup_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_backup
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_backup
        ] = mock_rpc

        request = {}
        await client.create_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.create_backup(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql.CreateBackupRequest(),
        {},
    ],
)
async def test_create_backup_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_backup), "__call__") as call:
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
        response = await client.create_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql.CreateBackupRequest()
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


def test_create_backup_field_headers():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql.CreateBackupRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_backup), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.create_backup(request)

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
async def test_create_backup_field_headers_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql.CreateBackupRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_backup), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.create_backup(request)

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


def test_create_backup_flattened():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_backup), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_backup(
            parent="parent_value",
            backup=cloud_sql_resources.Backup(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].backup
        mock_val = cloud_sql_resources.Backup(name="name_value")
        assert arg == mock_val


def test_create_backup_flattened_error():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_backup(
            cloud_sql.CreateBackupRequest(),
            parent="parent_value",
            backup=cloud_sql_resources.Backup(name="name_value"),
        )


@pytest.mark.asyncio
async def test_create_backup_flattened_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_backup), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_backup(
            parent="parent_value",
            backup=cloud_sql_resources.Backup(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].backup
        mock_val = cloud_sql_resources.Backup(name="name_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_backup_flattened_error_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_backup(
            cloud_sql.CreateBackupRequest(),
            parent="parent_value",
            backup=cloud_sql_resources.Backup(name="name_value"),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql.GetBackupRequest(),
        {},
    ],
)
def test_get_backup(request_type, transport: str = "grpc"):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_backup), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Backup(
            name="name_value",
            kind="kind_value",
            self_link="self_link_value",
            type_=cloud_sql_resources.Backup.SqlBackupType.AUTOMATED,
            description="description_value",
            instance="instance_value",
            location="location_value",
            state=cloud_sql_resources.Backup.SqlBackupState.ENQUEUED,
            kms_key="kms_key_value",
            kms_key_version="kms_key_version_value",
            backup_kind=cloud_sql_resources.SqlBackupKind.SNAPSHOT,
            time_zone="time_zone_value",
            database_version=cloud_sql_resources.SqlDatabaseVersion.MYSQL_5_1,
            max_chargeable_bytes=2089,
            backup_run="backup_run_value",
            ttl_days=868,
        )
        response = client.get_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql.GetBackupRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Backup)
    assert response.name == "name_value"
    assert response.kind == "kind_value"
    assert response.self_link == "self_link_value"
    assert response.type_ == cloud_sql_resources.Backup.SqlBackupType.AUTOMATED
    assert response.description == "description_value"
    assert response.instance == "instance_value"
    assert response.location == "location_value"
    assert response.state == cloud_sql_resources.Backup.SqlBackupState.ENQUEUED
    assert response.kms_key == "kms_key_value"
    assert response.kms_key_version == "kms_key_version_value"
    assert response.backup_kind == cloud_sql_resources.SqlBackupKind.SNAPSHOT
    assert response.time_zone == "time_zone_value"
    assert response.database_version == cloud_sql_resources.SqlDatabaseVersion.MYSQL_5_1
    assert response.max_chargeable_bytes == 2089
    assert response.backup_run == "backup_run_value"


def test_get_backup_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql.GetBackupRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_backup), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_backup(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.GetBackupRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_backup_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_backup in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_backup] = mock_rpc
        request = {}
        client.get_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_backup(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_backup_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_backup
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_backup
        ] = mock_rpc

        request = {}
        await client.get_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_backup(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql.GetBackupRequest(),
        {},
    ],
)
async def test_get_backup_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_backup), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Backup(
                name="name_value",
                kind="kind_value",
                self_link="self_link_value",
                type_=cloud_sql_resources.Backup.SqlBackupType.AUTOMATED,
                description="description_value",
                instance="instance_value",
                location="location_value",
                state=cloud_sql_resources.Backup.SqlBackupState.ENQUEUED,
                kms_key="kms_key_value",
                kms_key_version="kms_key_version_value",
                backup_kind=cloud_sql_resources.SqlBackupKind.SNAPSHOT,
                time_zone="time_zone_value",
                database_version=cloud_sql_resources.SqlDatabaseVersion.MYSQL_5_1,
                max_chargeable_bytes=2089,
                backup_run="backup_run_value",
            )
        )
        response = await client.get_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql.GetBackupRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Backup)
    assert response.name == "name_value"
    assert response.kind == "kind_value"
    assert response.self_link == "self_link_value"
    assert response.type_ == cloud_sql_resources.Backup.SqlBackupType.AUTOMATED
    assert response.description == "description_value"
    assert response.instance == "instance_value"
    assert response.location == "location_value"
    assert response.state == cloud_sql_resources.Backup.SqlBackupState.ENQUEUED
    assert response.kms_key == "kms_key_value"
    assert response.kms_key_version == "kms_key_version_value"
    assert response.backup_kind == cloud_sql_resources.SqlBackupKind.SNAPSHOT
    assert response.time_zone == "time_zone_value"
    assert response.database_version == cloud_sql_resources.SqlDatabaseVersion.MYSQL_5_1
    assert response.max_chargeable_bytes == 2089
    assert response.backup_run == "backup_run_value"


def test_get_backup_field_headers():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql.GetBackupRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_backup), "__call__") as call:
        call.return_value = cloud_sql_resources.Backup()
        client.get_backup(request)

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
async def test_get_backup_field_headers_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql.GetBackupRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_backup), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Backup()
        )
        await client.get_backup(request)

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


def test_get_backup_flattened():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_backup), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Backup()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_backup(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_backup_flattened_error():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_backup(
            cloud_sql.GetBackupRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_backup_flattened_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_backup), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Backup()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Backup()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_backup(
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
async def test_get_backup_flattened_error_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_backup(
            cloud_sql.GetBackupRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql.ListBackupsRequest(),
        {},
    ],
)
def test_list_backups(request_type, transport: str = "grpc"):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_backups), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql.ListBackupsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_backups(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql.ListBackupsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListBackupsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_backups_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql.ListBackupsRequest(
        parent="parent_value",
        page_token="page_token_value",
        filter="filter_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_backups), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_backups(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.ListBackupsRequest(
            parent="parent_value",
            page_token="page_token_value",
            filter="filter_value",
        )
        assert args[0] == request_msg


def test_list_backups_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_backups in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_backups] = mock_rpc
        request = {}
        client.list_backups(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_backups(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_backups_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_backups
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_backups
        ] = mock_rpc

        request = {}
        await client.list_backups(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_backups(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql.ListBackupsRequest(),
        {},
    ],
)
async def test_list_backups_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_backups), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql.ListBackupsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_backups(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql.ListBackupsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListBackupsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_backups_field_headers():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql.ListBackupsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_backups), "__call__") as call:
        call.return_value = cloud_sql.ListBackupsResponse()
        client.list_backups(request)

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
async def test_list_backups_field_headers_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql.ListBackupsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_backups), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql.ListBackupsResponse()
        )
        await client.list_backups(request)

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


def test_list_backups_flattened():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_backups), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql.ListBackupsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_backups(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_backups_flattened_error():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_backups(
            cloud_sql.ListBackupsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_backups_flattened_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_backups), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql.ListBackupsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql.ListBackupsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_backups(
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
async def test_list_backups_flattened_error_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_backups(
            cloud_sql.ListBackupsRequest(),
            parent="parent_value",
        )


def test_list_backups_pager(transport_name: str = "grpc"):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_backups), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
                ],
                next_page_token="abc",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[],
                next_page_token="def",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                ],
                next_page_token="ghi",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
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
        pager = client.list_backups(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, cloud_sql_resources.Backup) for i in results)


def test_list_backups_pages(transport_name: str = "grpc"):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_backups), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
                ],
                next_page_token="abc",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[],
                next_page_token="def",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                ],
                next_page_token="ghi",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_backups(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_backups_async_pager():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_backups), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
                ],
                next_page_token="abc",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[],
                next_page_token="def",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                ],
                next_page_token="ghi",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_backups(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, cloud_sql_resources.Backup) for i in responses)


@pytest.mark.asyncio
async def test_list_backups_async_pages():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_backups), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
                ],
                next_page_token="abc",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[],
                next_page_token="def",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                ],
                next_page_token="ghi",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_backups(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql.UpdateBackupRequest(),
        {},
    ],
)
def test_update_backup(request_type, transport: str = "grpc"):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_backup), "__call__") as call:
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
        response = client.update_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql.UpdateBackupRequest()
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


def test_update_backup_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql.UpdateBackupRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_backup), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_backup(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.UpdateBackupRequest()
        assert args[0] == request_msg


def test_update_backup_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_backup in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_backup] = mock_rpc
        request = {}
        client.update_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_backup(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_backup_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_backup
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_backup
        ] = mock_rpc

        request = {}
        await client.update_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_backup(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql.UpdateBackupRequest(),
        {},
    ],
)
async def test_update_backup_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_backup), "__call__") as call:
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
        response = await client.update_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql.UpdateBackupRequest()
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


def test_update_backup_field_headers():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql.UpdateBackupRequest()

    request.backup.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_backup), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.update_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "backup.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_backup_field_headers_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql.UpdateBackupRequest()

    request.backup.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_backup), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.update_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "backup.name=name_value",
    ) in kw["metadata"]


def test_update_backup_flattened():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_backup), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_backup(
            backup=cloud_sql_resources.Backup(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].backup
        mock_val = cloud_sql_resources.Backup(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_backup_flattened_error():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_backup(
            cloud_sql.UpdateBackupRequest(),
            backup=cloud_sql_resources.Backup(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_backup_flattened_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_backup), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_backup(
            backup=cloud_sql_resources.Backup(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].backup
        mock_val = cloud_sql_resources.Backup(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_backup_flattened_error_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_backup(
            cloud_sql.UpdateBackupRequest(),
            backup=cloud_sql_resources.Backup(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql.DeleteBackupRequest(),
        {},
    ],
)
def test_delete_backup(request_type, transport: str = "grpc"):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_backup), "__call__") as call:
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
        response = client.delete_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloud_sql.DeleteBackupRequest()
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


def test_delete_backup_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloud_sql.DeleteBackupRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_backup), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.delete_backup(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.DeleteBackupRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_delete_backup_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_backup in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_backup] = mock_rpc
        request = {}
        client.delete_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_backup(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_delete_backup_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.delete_backup
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.delete_backup
        ] = mock_rpc

        request = {}
        await client.delete_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.delete_backup(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql.DeleteBackupRequest(),
        {},
    ],
)
async def test_delete_backup_async(request_type, transport: str = "grpc_asyncio"):
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_backup), "__call__") as call:
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
        response = await client.delete_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloud_sql.DeleteBackupRequest()
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


def test_delete_backup_field_headers():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql.DeleteBackupRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_backup), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.delete_backup(request)

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
async def test_delete_backup_field_headers_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloud_sql.DeleteBackupRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_backup), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        await client.delete_backup(request)

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


def test_delete_backup_flattened():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_backup), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_backup(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_backup_flattened_error():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_backup(
            cloud_sql.DeleteBackupRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_backup_flattened_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_backup), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloud_sql_resources.Operation()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Operation()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_backup(
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
async def test_delete_backup_flattened_error_async():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_backup(
            cloud_sql.DeleteBackupRequest(),
            name="name_value",
        )


def test_create_backup_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_backup in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_backup] = mock_rpc

        request = {}
        client.create_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_backup(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_backup_rest_required_fields(request_type=cloud_sql.CreateBackupRequest):
    transport_class = transports.SqlBackupsServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateBackup,
        "_BaseCreateBackup__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloud_sql_resources.Operation()
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
            return_value = cloud_sql_resources.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_backup(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_backup_rest_flattened():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloud_sql_resources.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            backup=cloud_sql_resources.Backup(name="name_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = cloud_sql_resources.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_backup(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/sql/v1beta4/{parent=projects/*}/backups" % client.transport._host,
            args[1],
        )


def test_create_backup_rest_flattened_error(transport: str = "rest"):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_backup(
            cloud_sql.CreateBackupRequest(),
            parent="parent_value",
            backup=cloud_sql_resources.Backup(name="name_value"),
        )


def test_get_backup_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_backup in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_backup] = mock_rpc

        request = {}
        client.get_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_backup(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_backup_rest_required_fields(request_type=cloud_sql.GetBackupRequest):
    transport_class = transports.SqlBackupsServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetBackup,
        "_BaseGetBackup__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloud_sql_resources.Backup()
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
            return_value = cloud_sql_resources.Backup.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_backup(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_backup_rest_flattened():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloud_sql_resources.Backup()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/backups/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = cloud_sql_resources.Backup.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_backup(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/sql/v1beta4/{name=projects/*/backups/*}" % client.transport._host,
            args[1],
        )


def test_get_backup_rest_flattened_error(transport: str = "rest"):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_backup(
            cloud_sql.GetBackupRequest(),
            name="name_value",
        )


def test_list_backups_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_backups in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_backups] = mock_rpc

        request = {}
        client.list_backups(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_backups(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_backups_rest_required_fields(request_type=cloud_sql.ListBackupsRequest):
    transport_class = transports.SqlBackupsServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListBackups,
        "_BaseListBackups__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloud_sql.ListBackupsResponse()
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
            return_value = cloud_sql.ListBackupsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_backups(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_backups_rest_flattened():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloud_sql.ListBackupsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = cloud_sql.ListBackupsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_backups(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/sql/v1beta4/{parent=projects/*}/backups" % client.transport._host,
            args[1],
        )


def test_list_backups_rest_flattened_error(transport: str = "rest"):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_backups(
            cloud_sql.ListBackupsRequest(),
            parent="parent_value",
        )


def test_list_backups_rest_pager(transport: str = "rest"):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
                ],
                next_page_token="abc",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[],
                next_page_token="def",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                ],
                next_page_token="ghi",
            ),
            cloud_sql.ListBackupsResponse(
                backups=[
                    cloud_sql_resources.Backup(),
                    cloud_sql_resources.Backup(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(cloud_sql.ListBackupsResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "projects/sample1"}

        pager = client.list_backups(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, cloud_sql_resources.Backup) for i in results)

        pages = list(client.list_backups(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_update_backup_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_backup in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_backup] = mock_rpc

        request = {}
        client.update_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_backup(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_backup_rest_required_fields(request_type=cloud_sql.UpdateBackupRequest):
    transport_class = transports.SqlBackupsServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateBackup,
        "_BaseUpdateBackup__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloud_sql_resources.Operation()
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
            return_value = cloud_sql_resources.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_backup(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_backup_rest_flattened():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloud_sql_resources.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {"backup": {"name": "projects/sample1/backups/sample2"}}

        # get truthy value for each flattened field
        mock_args = dict(
            backup=cloud_sql_resources.Backup(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = cloud_sql_resources.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_backup(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/sql/v1beta4/{backup.name=projects/*/backups/*}"
            % client.transport._host,
            args[1],
        )


def test_update_backup_rest_flattened_error(transport: str = "rest"):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_backup(
            cloud_sql.UpdateBackupRequest(),
            backup=cloud_sql_resources.Backup(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_delete_backup_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = SqlBackupsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_backup in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_backup] = mock_rpc

        request = {}
        client.delete_backup(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_backup(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_backup_rest_required_fields(request_type=cloud_sql.DeleteBackupRequest):
    transport_class = transports.SqlBackupsServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeleteBackup,
        "_BaseDeleteBackup__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloud_sql_resources.Operation()
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
                "method": "delete",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = cloud_sql_resources.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.delete_backup(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_backup_rest_flattened():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloud_sql_resources.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/backups/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = cloud_sql_resources.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.delete_backup(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/sql/v1beta4/{name=projects/*/backups/*}" % client.transport._host,
            args[1],
        )


def test_delete_backup_rest_flattened_error(transport: str = "rest"):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_backup(
            cloud_sql.DeleteBackupRequest(),
            name="name_value",
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.SqlBackupsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = SqlBackupsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.SqlBackupsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = SqlBackupsServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.SqlBackupsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = SqlBackupsServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = SqlBackupsServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.SqlBackupsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = SqlBackupsServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.SqlBackupsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = SqlBackupsServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.SqlBackupsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.SqlBackupsServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.SqlBackupsServiceGrpcTransport,
        transports.SqlBackupsServiceGrpcAsyncIOTransport,
        transports.SqlBackupsServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = SqlBackupsServiceClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_backup_empty_call_grpc():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_backup), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.create_backup(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.CreateBackupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_backup_empty_call_grpc():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_backup), "__call__") as call:
        call.return_value = cloud_sql_resources.Backup()
        client.get_backup(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.GetBackupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_backups_empty_call_grpc():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_backups), "__call__") as call:
        call.return_value = cloud_sql.ListBackupsResponse()
        client.list_backups(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.ListBackupsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_backup_empty_call_grpc():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_backup), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.update_backup(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.UpdateBackupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_backup_empty_call_grpc():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.delete_backup), "__call__") as call:
        call.return_value = cloud_sql_resources.Operation()
        client.delete_backup(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.DeleteBackupRequest()
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = SqlBackupsServiceAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_backup_empty_call_grpc_asyncio():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_backup), "__call__") as call:
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
        await client.create_backup(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.CreateBackupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_backup_empty_call_grpc_asyncio():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_backup), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql_resources.Backup(
                name="name_value",
                kind="kind_value",
                self_link="self_link_value",
                type_=cloud_sql_resources.Backup.SqlBackupType.AUTOMATED,
                description="description_value",
                instance="instance_value",
                location="location_value",
                state=cloud_sql_resources.Backup.SqlBackupState.ENQUEUED,
                kms_key="kms_key_value",
                kms_key_version="kms_key_version_value",
                backup_kind=cloud_sql_resources.SqlBackupKind.SNAPSHOT,
                time_zone="time_zone_value",
                database_version=cloud_sql_resources.SqlDatabaseVersion.MYSQL_5_1,
                max_chargeable_bytes=2089,
                backup_run="backup_run_value",
            )
        )
        await client.get_backup(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.GetBackupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_backups_empty_call_grpc_asyncio():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_backups), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloud_sql.ListBackupsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_backups(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.ListBackupsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_backup_empty_call_grpc_asyncio():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_backup), "__call__") as call:
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
        await client.update_backup(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.UpdateBackupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_backup_empty_call_grpc_asyncio():
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.delete_backup), "__call__") as call:
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
        await client.delete_backup(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.DeleteBackupRequest()
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = SqlBackupsServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_create_backup_rest_bad_request(request_type=cloud_sql.CreateBackupRequest):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
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
        client.create_backup(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql.CreateBackupRequest,
        dict,
    ],
)
def test_create_backup_rest_call_success(request_type):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request_init["backup"] = {
        "name": "name_value",
        "kind": "kind_value",
        "self_link": "self_link_value",
        "type_": 1,
        "description": "description_value",
        "instance": "instance_value",
        "location": "location_value",
        "backup_interval": {
            "start_time": {"seconds": 751, "nanos": 543},
            "end_time": {},
        },
        "state": 1,
        "error": {
            "kind": "kind_value",
            "code": "code_value",
            "message": "message_value",
        },
        "kms_key": "kms_key_value",
        "kms_key_version": "kms_key_version_value",
        "backup_kind": 1,
        "time_zone": "time_zone_value",
        "ttl_days": 868,
        "expiry_time": {},
        "database_version": 2,
        "max_chargeable_bytes": 2089,
        "instance_deletion_time": {},
        "instance_settings": {
            "kind": "kind_value",
            "state": 1,
            "database_version": 2,
            "settings": {
                "settings_version": {"value": 541},
                "authorized_gae_applications": [
                    "authorized_gae_applications_value1",
                    "authorized_gae_applications_value2",
                ],
                "tier": "tier_value",
                "kind": "kind_value",
                "user_labels": {},
                "availability_type": 1,
                "pricing_plan": 1,
                "replication_type": 1,
                "storage_auto_resize_limit": {},
                "activation_policy": 1,
                "ip_configuration": {
                    "ipv4_enabled": {"value": True},
                    "private_network": "private_network_value",
                    "require_ssl": {},
                    "authorized_networks": [
                        {
                            "value": "value_value",
                            "expiration_time": {},
                            "name": "name_value",
                            "kind": "kind_value",
                        }
                    ],
                    "allocated_ip_range": "allocated_ip_range_value",
                    "enable_private_path_for_google_cloud_services": {},
                    "ssl_mode": 1,
                    "psc_config": {
                        "psc_enabled": True,
                        "allowed_consumer_projects": [
                            "allowed_consumer_projects_value1",
                            "allowed_consumer_projects_value2",
                        ],
                        "psc_auto_connections": [
                            {
                                "consumer_project": "consumer_project_value",
                                "consumer_network": "consumer_network_value",
                                "ip_address": "ip_address_value",
                                "status": "status_value",
                                "consumer_network_status": "consumer_network_status_value",
                                "service_connection_policy": "service_connection_policy_value",
                                "service_connection_policy_creation_result": "service_connection_policy_creation_result_value",
                                "instance_auto_dns_status": 1,
                                "write_endpoint_auto_dns_status": 1,
                            }
                        ],
                        "network_attachment_uri": "network_attachment_uri_value",
                        "psc_auto_dns_enabled": True,
                        "psc_write_endpoint_dns_enabled": True,
                        "psc_auto_connection_policy_enabled": True,
                    },
                    "server_ca_mode": 1,
                    "custom_subject_alternative_names": [
                        "custom_subject_alternative_names_value1",
                        "custom_subject_alternative_names_value2",
                    ],
                    "server_ca_pool": "server_ca_pool_value",
                    "server_certificate_rotation_mode": 1,
                },
                "storage_auto_resize": {},
                "location_preference": {
                    "follow_gae_application": "follow_gae_application_value",
                    "zone": "zone_value",
                    "secondary_zone": "secondary_zone_value",
                    "kind": "kind_value",
                },
                "database_flags": [{"name": "name_value", "value": "value_value"}],
                "data_disk_type": 1,
                "maintenance_window": {
                    "hour": {"value": 541},
                    "day": {},
                    "update_track": 1,
                    "kind": "kind_value",
                },
                "backup_configuration": {
                    "start_time": "start_time_value",
                    "enabled": {},
                    "kind": "kind_value",
                    "binary_log_enabled": {},
                    "replication_log_archiving_enabled": {},
                    "location": "location_value",
                    "point_in_time_recovery_enabled": {},
                    "transaction_log_retention_days": {},
                    "backup_retention_settings": {
                        "retention_unit": 1,
                        "retained_backups": {},
                    },
                    "transactional_log_storage_state": 1,
                    "backup_tier": 1,
                },
                "database_replication_enabled": {},
                "crash_safe_replication_enabled": {},
                "data_disk_size_gb": {},
                "active_directory_config": {
                    "kind": "kind_value",
                    "domain": "domain_value",
                    "mode": 1,
                    "dns_servers": ["dns_servers_value1", "dns_servers_value2"],
                    "admin_credential_secret_name": "admin_credential_secret_name_value",
                    "organizational_unit": "organizational_unit_value",
                },
                "collation": "collation_value",
                "deny_maintenance_periods": [
                    {
                        "start_date": "start_date_value",
                        "end_date": "end_date_value",
                        "time": "time_value",
                    }
                ],
                "insights_config": {
                    "query_insights_enabled": True,
                    "record_client_address": True,
                    "record_application_tags": True,
                    "query_string_length": {},
                    "query_plans_per_minute": {},
                    "enhanced_query_insights_enabled": {},
                },
                "password_validation_policy": {
                    "min_length": {},
                    "complexity": 1,
                    "reuse_interval": {},
                    "disallow_username_substring": {},
                    "password_change_interval": {"seconds": 751, "nanos": 543},
                    "enable_password_policy": {},
                    "disallow_compromised_credentials": {},
                },
                "sql_server_audit_config": {
                    "kind": "kind_value",
                    "bucket": "bucket_value",
                    "retention_interval": {},
                    "upload_interval": {},
                },
                "edition": 2,
                "connector_enforcement": 1,
                "deletion_protection_enabled": {},
                "time_zone": "time_zone_value",
                "advanced_machine_features": {"threads_per_core": 1689},
                "data_cache_config": {"data_cache_enabled": True},
                "replication_lag_max_seconds": {},
                "enable_google_ml_integration": {},
                "enable_dataplex_integration": {},
                "retain_backups_on_delete": {},
                "data_disk_provisioned_iops": 2767,
                "data_disk_provisioned_throughput": 3438,
                "connection_pool_config": {
                    "connection_pooling_enabled": True,
                    "flags": [{"name": "name_value", "value": "value_value"}],
                    "pooler_count": 1305,
                },
                "final_backup_config": {"enabled": True, "retention_days": 1512},
                "read_pool_auto_scale_config": {
                    "enabled": True,
                    "min_node_count": 1489,
                    "max_node_count": 1491,
                    "target_metrics": [
                        {"metric": "metric_value", "target_value": 0.1283}
                    ],
                    "disable_scale_in": True,
                    "scale_in_cooldown_seconds": 2640,
                    "scale_out_cooldown_seconds": 2769,
                },
                "accelerated_replica_mode": {},
                "auto_upgrade_enabled": True,
                "entraid_config": {
                    "kind": "kind_value",
                    "tenant_id": "tenant_id_value",
                    "application_id": "application_id_value",
                },
                "data_api_access": 1,
                "performance_capture_config": {
                    "enabled": True,
                    "probing_interval_seconds": 2563,
                    "probe_threshold": 1604,
                    "running_threads_threshold": 2679,
                    "seconds_behind_source_threshold": 3284,
                    "transaction_duration_threshold": 3223,
                    "cpu_utilization_threshold_percent": 3551,
                    "memory_usage_threshold_percent": 3209,
                    "transaction_lock_wait_threshold_count": 3958,
                    "semaphore_wait_threshold_count": 3212,
                    "history_list_length_threshold_count": 3778,
                    "transaction_kill_threshold_seconds": 3627,
                    "transaction_kill_excluded_user_hosts": [
                        "transaction_kill_excluded_user_hosts_value1",
                        "transaction_kill_excluded_user_hosts_value2",
                    ],
                    "transaction_kill_type": 1,
                },
            },
            "etag": "etag_value",
            "failover_replica": {"name": "name_value", "available": {}},
            "master_instance_name": "master_instance_name_value",
            "replica_names": ["replica_names_value1", "replica_names_value2"],
            "max_disk_size": {},
            "current_disk_size": {},
            "ip_addresses": [
                {"type_": 1, "ip_address": "ip_address_value", "time_to_retire": {}}
            ],
            "server_ca_cert": {
                "kind": "kind_value",
                "cert_serial_number": "cert_serial_number_value",
                "cert": "cert_value",
                "create_time": {},
                "common_name": "common_name_value",
                "expiration_time": {},
                "sha1_fingerprint": "sha1_fingerprint_value",
                "instance": "instance_value",
                "self_link": "self_link_value",
            },
            "instance_type": 1,
            "project": "project_value",
            "ipv6_address": "ipv6_address_value",
            "service_account_email_address": "service_account_email_address_value",
            "on_premises_configuration": {
                "host_port": "host_port_value",
                "kind": "kind_value",
                "username": "username_value",
                "password": "password_value",
                "ca_certificate": "ca_certificate_value",
                "client_certificate": "client_certificate_value",
                "client_key": "client_key_value",
                "dump_file_path": "dump_file_path_value",
                "source_instance": {
                    "name": "name_value",
                    "region": "region_value",
                    "project": "project_value",
                },
                "selected_objects": [{"database": "database_value"}],
                "ssl_option": 1,
                "dms_managed": True,
            },
            "replica_configuration": {
                "kind": "kind_value",
                "mysql_replica_configuration": {
                    "dump_file_path": "dump_file_path_value",
                    "username": "username_value",
                    "password": "password_value",
                    "connect_retry_interval": {},
                    "master_heartbeat_period": {},
                    "ca_certificate": "ca_certificate_value",
                    "client_certificate": "client_certificate_value",
                    "client_key": "client_key_value",
                    "ssl_cipher": "ssl_cipher_value",
                    "verify_server_certificate": {},
                    "kind": "kind_value",
                },
                "failover_target": {},
                "cascadable_replica": {},
            },
            "backend_type": 1,
            "self_link": "self_link_value",
            "suspension_reason": [2],
            "connection_name": "connection_name_value",
            "name": "name_value",
            "region": "region_value",
            "gce_zone": "gce_zone_value",
            "secondary_gce_zone": "secondary_gce_zone_value",
            "disk_encryption_configuration": {
                "kms_key_name": "kms_key_name_value",
                "kind": "kind_value",
                "confidential_mode": True,
                "cmek_source_log_encryption_enforced": True,
            },
            "disk_encryption_status": {
                "kms_key_version_name": "kms_key_version_name_value",
                "kind": "kind_value",
            },
            "root_password": "root_password_value",
            "scheduled_maintenance": {
                "start_time": {},
                "can_defer": True,
                "can_reschedule": True,
                "schedule_deadline_time": {},
            },
            "satisfies_pzs": {},
            "database_installed_version": "database_installed_version_value",
            "out_of_disk_report": {
                "sql_out_of_disk_state": 1,
                "sql_min_recommended_increase_size_gb": 3776,
            },
            "create_time": {},
            "available_maintenance_versions": [
                "available_maintenance_versions_value1",
                "available_maintenance_versions_value2",
            ],
            "maintenance_version": "maintenance_version_value",
            "upgradable_database_versions": [
                {
                    "major_version": "major_version_value",
                    "name": "name_value",
                    "display_name": "display_name_value",
                }
            ],
            "sql_network_architecture": 1,
            "psc_service_attachment_link": "psc_service_attachment_link_value",
            "dns_name": "dns_name_value",
            "primary_dns_name": "primary_dns_name_value",
            "write_endpoint": "write_endpoint_value",
            "replication_cluster": {
                "psa_write_endpoint": "psa_write_endpoint_value",
                "failover_dr_replica_name": "failover_dr_replica_name_value",
                "dr_replica": True,
            },
            "gemini_config": {
                "entitled": True,
                "google_vacuum_mgmt_enabled": True,
                "oom_session_cancel_enabled": True,
                "active_query_enabled": True,
                "index_advisor_enabled": True,
                "flag_recommender_enabled": True,
            },
            "satisfies_pzi": {},
            "switch_transaction_logs_to_cloud_storage_enabled": {},
            "include_replicas_for_major_version_upgrade": {},
            "skip_precheck": {},
            "tags": {},
            "node_count": 1070,
            "nodes": [
                {
                    "name": "name_value",
                    "gce_zone": "gce_zone_value",
                    "ip_addresses": {},
                    "dns_name": "dns_name_value",
                    "state": 1,
                    "dns_names": [
                        {
                            "name": "name_value",
                            "connection_type": 1,
                            "dns_scope": 1,
                            "record_manager": 1,
                        }
                    ],
                    "psc_service_attachment_link": "psc_service_attachment_link_value",
                    "psc_auto_connections": {},
                }
            ],
            "dns_names": {},
            "deployment_info": {
                "deployment_id": "deployment_id_value",
                "source": {"target_id": {}},
                "target": {"source_id": {}},
                "state": 1,
            },
            "database_center_integration_enabled": {},
            "database_center_integration": 1,
        },
        "backup_run": "backup_run_value",
        "satisfies_pzs": {},
        "satisfies_pzi": {},
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = cloud_sql.CreateBackupRequest.meta.fields["backup"]

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
    for field, value in request_init["backup"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["backup"][field])):
                    del request_init["backup"][field][i][subfield]
            else:
                del request_init["backup"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloud_sql_resources.Operation(
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

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloud_sql_resources.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_backup(request)

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


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_backup_rest_interceptors(null_interceptor):
    transport = transports.SqlBackupsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.SqlBackupsServiceRestInterceptor(),
    )
    client = SqlBackupsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor, "post_create_backup"
        ) as post,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor,
            "post_create_backup_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor, "pre_create_backup"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloud_sql.CreateBackupRequest.pb(cloud_sql.CreateBackupRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = cloud_sql_resources.Operation.to_json(
            cloud_sql_resources.Operation()
        )
        req.return_value.content = return_value

        request = cloud_sql.CreateBackupRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloud_sql_resources.Operation()
        post_with_metadata.return_value = cloud_sql_resources.Operation(), metadata

        client.create_backup(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_backup_rest_bad_request(request_type=cloud_sql.GetBackupRequest):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/backups/sample2"}
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
        client.get_backup(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql.GetBackupRequest,
        dict,
    ],
)
def test_get_backup_rest_call_success(request_type):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/backups/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloud_sql_resources.Backup(
            name="name_value",
            kind="kind_value",
            self_link="self_link_value",
            type_=cloud_sql_resources.Backup.SqlBackupType.AUTOMATED,
            description="description_value",
            instance="instance_value",
            location="location_value",
            state=cloud_sql_resources.Backup.SqlBackupState.ENQUEUED,
            kms_key="kms_key_value",
            kms_key_version="kms_key_version_value",
            backup_kind=cloud_sql_resources.SqlBackupKind.SNAPSHOT,
            time_zone="time_zone_value",
            database_version=cloud_sql_resources.SqlDatabaseVersion.MYSQL_5_1,
            max_chargeable_bytes=2089,
            backup_run="backup_run_value",
            ttl_days=868,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloud_sql_resources.Backup.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_backup(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloud_sql_resources.Backup)
    assert response.name == "name_value"
    assert response.kind == "kind_value"
    assert response.self_link == "self_link_value"
    assert response.type_ == cloud_sql_resources.Backup.SqlBackupType.AUTOMATED
    assert response.description == "description_value"
    assert response.instance == "instance_value"
    assert response.location == "location_value"
    assert response.state == cloud_sql_resources.Backup.SqlBackupState.ENQUEUED
    assert response.kms_key == "kms_key_value"
    assert response.kms_key_version == "kms_key_version_value"
    assert response.backup_kind == cloud_sql_resources.SqlBackupKind.SNAPSHOT
    assert response.time_zone == "time_zone_value"
    assert response.database_version == cloud_sql_resources.SqlDatabaseVersion.MYSQL_5_1
    assert response.max_chargeable_bytes == 2089
    assert response.backup_run == "backup_run_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_backup_rest_interceptors(null_interceptor):
    transport = transports.SqlBackupsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.SqlBackupsServiceRestInterceptor(),
    )
    client = SqlBackupsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor, "post_get_backup"
        ) as post,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor, "post_get_backup_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor, "pre_get_backup"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloud_sql.GetBackupRequest.pb(cloud_sql.GetBackupRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = cloud_sql_resources.Backup.to_json(cloud_sql_resources.Backup())
        req.return_value.content = return_value

        request = cloud_sql.GetBackupRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloud_sql_resources.Backup()
        post_with_metadata.return_value = cloud_sql_resources.Backup(), metadata

        client.get_backup(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_backups_rest_bad_request(request_type=cloud_sql.ListBackupsRequest):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
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
        client.list_backups(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql.ListBackupsRequest,
        dict,
    ],
)
def test_list_backups_rest_call_success(request_type):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloud_sql.ListBackupsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloud_sql.ListBackupsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_backups(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListBackupsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_backups_rest_interceptors(null_interceptor):
    transport = transports.SqlBackupsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.SqlBackupsServiceRestInterceptor(),
    )
    client = SqlBackupsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor, "post_list_backups"
        ) as post,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor,
            "post_list_backups_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor, "pre_list_backups"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloud_sql.ListBackupsRequest.pb(cloud_sql.ListBackupsRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = cloud_sql.ListBackupsResponse.to_json(
            cloud_sql.ListBackupsResponse()
        )
        req.return_value.content = return_value

        request = cloud_sql.ListBackupsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloud_sql.ListBackupsResponse()
        post_with_metadata.return_value = cloud_sql.ListBackupsResponse(), metadata

        client.list_backups(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_backup_rest_bad_request(request_type=cloud_sql.UpdateBackupRequest):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"backup": {"name": "projects/sample1/backups/sample2"}}
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
        client.update_backup(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql.UpdateBackupRequest,
        dict,
    ],
)
def test_update_backup_rest_call_success(request_type):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"backup": {"name": "projects/sample1/backups/sample2"}}
    request_init["backup"] = {
        "name": "projects/sample1/backups/sample2",
        "kind": "kind_value",
        "self_link": "self_link_value",
        "type_": 1,
        "description": "description_value",
        "instance": "instance_value",
        "location": "location_value",
        "backup_interval": {
            "start_time": {"seconds": 751, "nanos": 543},
            "end_time": {},
        },
        "state": 1,
        "error": {
            "kind": "kind_value",
            "code": "code_value",
            "message": "message_value",
        },
        "kms_key": "kms_key_value",
        "kms_key_version": "kms_key_version_value",
        "backup_kind": 1,
        "time_zone": "time_zone_value",
        "ttl_days": 868,
        "expiry_time": {},
        "database_version": 2,
        "max_chargeable_bytes": 2089,
        "instance_deletion_time": {},
        "instance_settings": {
            "kind": "kind_value",
            "state": 1,
            "database_version": 2,
            "settings": {
                "settings_version": {"value": 541},
                "authorized_gae_applications": [
                    "authorized_gae_applications_value1",
                    "authorized_gae_applications_value2",
                ],
                "tier": "tier_value",
                "kind": "kind_value",
                "user_labels": {},
                "availability_type": 1,
                "pricing_plan": 1,
                "replication_type": 1,
                "storage_auto_resize_limit": {},
                "activation_policy": 1,
                "ip_configuration": {
                    "ipv4_enabled": {"value": True},
                    "private_network": "private_network_value",
                    "require_ssl": {},
                    "authorized_networks": [
                        {
                            "value": "value_value",
                            "expiration_time": {},
                            "name": "name_value",
                            "kind": "kind_value",
                        }
                    ],
                    "allocated_ip_range": "allocated_ip_range_value",
                    "enable_private_path_for_google_cloud_services": {},
                    "ssl_mode": 1,
                    "psc_config": {
                        "psc_enabled": True,
                        "allowed_consumer_projects": [
                            "allowed_consumer_projects_value1",
                            "allowed_consumer_projects_value2",
                        ],
                        "psc_auto_connections": [
                            {
                                "consumer_project": "consumer_project_value",
                                "consumer_network": "consumer_network_value",
                                "ip_address": "ip_address_value",
                                "status": "status_value",
                                "consumer_network_status": "consumer_network_status_value",
                                "service_connection_policy": "service_connection_policy_value",
                                "service_connection_policy_creation_result": "service_connection_policy_creation_result_value",
                                "instance_auto_dns_status": 1,
                                "write_endpoint_auto_dns_status": 1,
                            }
                        ],
                        "network_attachment_uri": "network_attachment_uri_value",
                        "psc_auto_dns_enabled": True,
                        "psc_write_endpoint_dns_enabled": True,
                        "psc_auto_connection_policy_enabled": True,
                    },
                    "server_ca_mode": 1,
                    "custom_subject_alternative_names": [
                        "custom_subject_alternative_names_value1",
                        "custom_subject_alternative_names_value2",
                    ],
                    "server_ca_pool": "server_ca_pool_value",
                    "server_certificate_rotation_mode": 1,
                },
                "storage_auto_resize": {},
                "location_preference": {
                    "follow_gae_application": "follow_gae_application_value",
                    "zone": "zone_value",
                    "secondary_zone": "secondary_zone_value",
                    "kind": "kind_value",
                },
                "database_flags": [{"name": "name_value", "value": "value_value"}],
                "data_disk_type": 1,
                "maintenance_window": {
                    "hour": {"value": 541},
                    "day": {},
                    "update_track": 1,
                    "kind": "kind_value",
                },
                "backup_configuration": {
                    "start_time": "start_time_value",
                    "enabled": {},
                    "kind": "kind_value",
                    "binary_log_enabled": {},
                    "replication_log_archiving_enabled": {},
                    "location": "location_value",
                    "point_in_time_recovery_enabled": {},
                    "transaction_log_retention_days": {},
                    "backup_retention_settings": {
                        "retention_unit": 1,
                        "retained_backups": {},
                    },
                    "transactional_log_storage_state": 1,
                    "backup_tier": 1,
                },
                "database_replication_enabled": {},
                "crash_safe_replication_enabled": {},
                "data_disk_size_gb": {},
                "active_directory_config": {
                    "kind": "kind_value",
                    "domain": "domain_value",
                    "mode": 1,
                    "dns_servers": ["dns_servers_value1", "dns_servers_value2"],
                    "admin_credential_secret_name": "admin_credential_secret_name_value",
                    "organizational_unit": "organizational_unit_value",
                },
                "collation": "collation_value",
                "deny_maintenance_periods": [
                    {
                        "start_date": "start_date_value",
                        "end_date": "end_date_value",
                        "time": "time_value",
                    }
                ],
                "insights_config": {
                    "query_insights_enabled": True,
                    "record_client_address": True,
                    "record_application_tags": True,
                    "query_string_length": {},
                    "query_plans_per_minute": {},
                    "enhanced_query_insights_enabled": {},
                },
                "password_validation_policy": {
                    "min_length": {},
                    "complexity": 1,
                    "reuse_interval": {},
                    "disallow_username_substring": {},
                    "password_change_interval": {"seconds": 751, "nanos": 543},
                    "enable_password_policy": {},
                    "disallow_compromised_credentials": {},
                },
                "sql_server_audit_config": {
                    "kind": "kind_value",
                    "bucket": "bucket_value",
                    "retention_interval": {},
                    "upload_interval": {},
                },
                "edition": 2,
                "connector_enforcement": 1,
                "deletion_protection_enabled": {},
                "time_zone": "time_zone_value",
                "advanced_machine_features": {"threads_per_core": 1689},
                "data_cache_config": {"data_cache_enabled": True},
                "replication_lag_max_seconds": {},
                "enable_google_ml_integration": {},
                "enable_dataplex_integration": {},
                "retain_backups_on_delete": {},
                "data_disk_provisioned_iops": 2767,
                "data_disk_provisioned_throughput": 3438,
                "connection_pool_config": {
                    "connection_pooling_enabled": True,
                    "flags": [{"name": "name_value", "value": "value_value"}],
                    "pooler_count": 1305,
                },
                "final_backup_config": {"enabled": True, "retention_days": 1512},
                "read_pool_auto_scale_config": {
                    "enabled": True,
                    "min_node_count": 1489,
                    "max_node_count": 1491,
                    "target_metrics": [
                        {"metric": "metric_value", "target_value": 0.1283}
                    ],
                    "disable_scale_in": True,
                    "scale_in_cooldown_seconds": 2640,
                    "scale_out_cooldown_seconds": 2769,
                },
                "accelerated_replica_mode": {},
                "auto_upgrade_enabled": True,
                "entraid_config": {
                    "kind": "kind_value",
                    "tenant_id": "tenant_id_value",
                    "application_id": "application_id_value",
                },
                "data_api_access": 1,
                "performance_capture_config": {
                    "enabled": True,
                    "probing_interval_seconds": 2563,
                    "probe_threshold": 1604,
                    "running_threads_threshold": 2679,
                    "seconds_behind_source_threshold": 3284,
                    "transaction_duration_threshold": 3223,
                    "cpu_utilization_threshold_percent": 3551,
                    "memory_usage_threshold_percent": 3209,
                    "transaction_lock_wait_threshold_count": 3958,
                    "semaphore_wait_threshold_count": 3212,
                    "history_list_length_threshold_count": 3778,
                    "transaction_kill_threshold_seconds": 3627,
                    "transaction_kill_excluded_user_hosts": [
                        "transaction_kill_excluded_user_hosts_value1",
                        "transaction_kill_excluded_user_hosts_value2",
                    ],
                    "transaction_kill_type": 1,
                },
            },
            "etag": "etag_value",
            "failover_replica": {"name": "name_value", "available": {}},
            "master_instance_name": "master_instance_name_value",
            "replica_names": ["replica_names_value1", "replica_names_value2"],
            "max_disk_size": {},
            "current_disk_size": {},
            "ip_addresses": [
                {"type_": 1, "ip_address": "ip_address_value", "time_to_retire": {}}
            ],
            "server_ca_cert": {
                "kind": "kind_value",
                "cert_serial_number": "cert_serial_number_value",
                "cert": "cert_value",
                "create_time": {},
                "common_name": "common_name_value",
                "expiration_time": {},
                "sha1_fingerprint": "sha1_fingerprint_value",
                "instance": "instance_value",
                "self_link": "self_link_value",
            },
            "instance_type": 1,
            "project": "project_value",
            "ipv6_address": "ipv6_address_value",
            "service_account_email_address": "service_account_email_address_value",
            "on_premises_configuration": {
                "host_port": "host_port_value",
                "kind": "kind_value",
                "username": "username_value",
                "password": "password_value",
                "ca_certificate": "ca_certificate_value",
                "client_certificate": "client_certificate_value",
                "client_key": "client_key_value",
                "dump_file_path": "dump_file_path_value",
                "source_instance": {
                    "name": "name_value",
                    "region": "region_value",
                    "project": "project_value",
                },
                "selected_objects": [{"database": "database_value"}],
                "ssl_option": 1,
                "dms_managed": True,
            },
            "replica_configuration": {
                "kind": "kind_value",
                "mysql_replica_configuration": {
                    "dump_file_path": "dump_file_path_value",
                    "username": "username_value",
                    "password": "password_value",
                    "connect_retry_interval": {},
                    "master_heartbeat_period": {},
                    "ca_certificate": "ca_certificate_value",
                    "client_certificate": "client_certificate_value",
                    "client_key": "client_key_value",
                    "ssl_cipher": "ssl_cipher_value",
                    "verify_server_certificate": {},
                    "kind": "kind_value",
                },
                "failover_target": {},
                "cascadable_replica": {},
            },
            "backend_type": 1,
            "self_link": "self_link_value",
            "suspension_reason": [2],
            "connection_name": "connection_name_value",
            "name": "name_value",
            "region": "region_value",
            "gce_zone": "gce_zone_value",
            "secondary_gce_zone": "secondary_gce_zone_value",
            "disk_encryption_configuration": {
                "kms_key_name": "kms_key_name_value",
                "kind": "kind_value",
                "confidential_mode": True,
                "cmek_source_log_encryption_enforced": True,
            },
            "disk_encryption_status": {
                "kms_key_version_name": "kms_key_version_name_value",
                "kind": "kind_value",
            },
            "root_password": "root_password_value",
            "scheduled_maintenance": {
                "start_time": {},
                "can_defer": True,
                "can_reschedule": True,
                "schedule_deadline_time": {},
            },
            "satisfies_pzs": {},
            "database_installed_version": "database_installed_version_value",
            "out_of_disk_report": {
                "sql_out_of_disk_state": 1,
                "sql_min_recommended_increase_size_gb": 3776,
            },
            "create_time": {},
            "available_maintenance_versions": [
                "available_maintenance_versions_value1",
                "available_maintenance_versions_value2",
            ],
            "maintenance_version": "maintenance_version_value",
            "upgradable_database_versions": [
                {
                    "major_version": "major_version_value",
                    "name": "name_value",
                    "display_name": "display_name_value",
                }
            ],
            "sql_network_architecture": 1,
            "psc_service_attachment_link": "psc_service_attachment_link_value",
            "dns_name": "dns_name_value",
            "primary_dns_name": "primary_dns_name_value",
            "write_endpoint": "write_endpoint_value",
            "replication_cluster": {
                "psa_write_endpoint": "psa_write_endpoint_value",
                "failover_dr_replica_name": "failover_dr_replica_name_value",
                "dr_replica": True,
            },
            "gemini_config": {
                "entitled": True,
                "google_vacuum_mgmt_enabled": True,
                "oom_session_cancel_enabled": True,
                "active_query_enabled": True,
                "index_advisor_enabled": True,
                "flag_recommender_enabled": True,
            },
            "satisfies_pzi": {},
            "switch_transaction_logs_to_cloud_storage_enabled": {},
            "include_replicas_for_major_version_upgrade": {},
            "skip_precheck": {},
            "tags": {},
            "node_count": 1070,
            "nodes": [
                {
                    "name": "name_value",
                    "gce_zone": "gce_zone_value",
                    "ip_addresses": {},
                    "dns_name": "dns_name_value",
                    "state": 1,
                    "dns_names": [
                        {
                            "name": "name_value",
                            "connection_type": 1,
                            "dns_scope": 1,
                            "record_manager": 1,
                        }
                    ],
                    "psc_service_attachment_link": "psc_service_attachment_link_value",
                    "psc_auto_connections": {},
                }
            ],
            "dns_names": {},
            "deployment_info": {
                "deployment_id": "deployment_id_value",
                "source": {"target_id": {}},
                "target": {"source_id": {}},
                "state": 1,
            },
            "database_center_integration_enabled": {},
            "database_center_integration": 1,
        },
        "backup_run": "backup_run_value",
        "satisfies_pzs": {},
        "satisfies_pzi": {},
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = cloud_sql.UpdateBackupRequest.meta.fields["backup"]

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
    for field, value in request_init["backup"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["backup"][field])):
                    del request_init["backup"][field][i][subfield]
            else:
                del request_init["backup"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloud_sql_resources.Operation(
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

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloud_sql_resources.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_backup(request)

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


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_backup_rest_interceptors(null_interceptor):
    transport = transports.SqlBackupsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.SqlBackupsServiceRestInterceptor(),
    )
    client = SqlBackupsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor, "post_update_backup"
        ) as post,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor,
            "post_update_backup_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor, "pre_update_backup"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloud_sql.UpdateBackupRequest.pb(cloud_sql.UpdateBackupRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = cloud_sql_resources.Operation.to_json(
            cloud_sql_resources.Operation()
        )
        req.return_value.content = return_value

        request = cloud_sql.UpdateBackupRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloud_sql_resources.Operation()
        post_with_metadata.return_value = cloud_sql_resources.Operation(), metadata

        client.update_backup(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_backup_rest_bad_request(request_type=cloud_sql.DeleteBackupRequest):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/backups/sample2"}
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
        client.delete_backup(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloud_sql.DeleteBackupRequest,
        dict,
    ],
)
def test_delete_backup_rest_call_success(request_type):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/backups/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloud_sql_resources.Operation(
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

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloud_sql_resources.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.delete_backup(request)

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


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_backup_rest_interceptors(null_interceptor):
    transport = transports.SqlBackupsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.SqlBackupsServiceRestInterceptor(),
    )
    client = SqlBackupsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor, "post_delete_backup"
        ) as post,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor,
            "post_delete_backup_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.SqlBackupsServiceRestInterceptor, "pre_delete_backup"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloud_sql.DeleteBackupRequest.pb(cloud_sql.DeleteBackupRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = cloud_sql_resources.Operation.to_json(
            cloud_sql_resources.Operation()
        )
        req.return_value.content = return_value

        request = cloud_sql.DeleteBackupRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloud_sql_resources.Operation()
        post_with_metadata.return_value = cloud_sql_resources.Operation(), metadata

        client.delete_backup(
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
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_backup_empty_call_rest():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_backup), "__call__") as call:
        client.create_backup(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.CreateBackupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_backup_empty_call_rest():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_backup), "__call__") as call:
        client.get_backup(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.GetBackupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_backups_empty_call_rest():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_backups), "__call__") as call:
        client.list_backups(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.ListBackupsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_backup_empty_call_rest():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_backup), "__call__") as call:
        client.update_backup(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.UpdateBackupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_backup_empty_call_rest():
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.delete_backup), "__call__") as call:
        client.delete_backup(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloud_sql.DeleteBackupRequest()
        assert args[0] == request_msg


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.SqlBackupsServiceGrpcTransport,
    )


def test_sql_backups_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.SqlBackupsServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_sql_backups_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.sqladmin_v1beta4.services.sql_backups_service.transports.SqlBackupsServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.SqlBackupsServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "create_backup",
        "get_backup",
        "list_backups",
        "update_backup",
        "delete_backup",
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


def test_sql_backups_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.cloud.sqladmin_v1beta4.services.sql_backups_service.transports.SqlBackupsServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.SqlBackupsServiceTransport(
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


def test_sql_backups_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.cloud.sqladmin_v1beta4.services.sql_backups_service.transports.SqlBackupsServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.SqlBackupsServiceTransport()
        adc.assert_called_once()


def test_sql_backups_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        SqlBackupsServiceClient()
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
        transports.SqlBackupsServiceGrpcTransport,
        transports.SqlBackupsServiceGrpcAsyncIOTransport,
    ],
)
def test_sql_backups_service_transport_auth_adc(transport_class):
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
        transports.SqlBackupsServiceGrpcTransport,
        transports.SqlBackupsServiceGrpcAsyncIOTransport,
        transports.SqlBackupsServiceRestTransport,
    ],
)
def test_sql_backups_service_transport_auth_gdch_credentials(transport_class):
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
        (transports.SqlBackupsServiceGrpcTransport, grpc_helpers),
        (transports.SqlBackupsServiceGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_sql_backups_service_transport_create_channel(transport_class, grpc_helpers):
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
        transports.SqlBackupsServiceGrpcTransport,
        transports.SqlBackupsServiceGrpcAsyncIOTransport,
    ],
)
def test_sql_backups_service_grpc_transport_client_cert_source_for_mtls(
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


def test_sql_backups_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.SqlBackupsServiceRestTransport(
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
def test_sql_backups_service_host_no_port(transport_name):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="sqladmin.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "sqladmin.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://sqladmin.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_sql_backups_service_host_with_port(transport_name):
    client = SqlBackupsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="sqladmin.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "sqladmin.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://sqladmin.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_sql_backups_service_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = SqlBackupsServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = SqlBackupsServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.create_backup._session
    session2 = client2.transport.create_backup._session
    assert session1 != session2
    session1 = client1.transport.get_backup._session
    session2 = client2.transport.get_backup._session
    assert session1 != session2
    session1 = client1.transport.list_backups._session
    session2 = client2.transport.list_backups._session
    assert session1 != session2
    session1 = client1.transport.update_backup._session
    session2 = client2.transport.update_backup._session
    assert session1 != session2
    session1 = client1.transport.delete_backup._session
    session2 = client2.transport.delete_backup._session
    assert session1 != session2


def test_sql_backups_service_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.SqlBackupsServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_sql_backups_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.SqlBackupsServiceGrpcAsyncIOTransport(
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
        transports.SqlBackupsServiceGrpcTransport,
        transports.SqlBackupsServiceGrpcAsyncIOTransport,
    ],
)
def test_sql_backups_service_transport_channel_mtls_with_client_cert_source(
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
        transports.SqlBackupsServiceGrpcTransport,
        transports.SqlBackupsServiceGrpcAsyncIOTransport,
    ],
)
def test_sql_backups_service_transport_channel_mtls_with_adc(transport_class):
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
    actual = SqlBackupsServiceClient.backup_path(project, backup)
    assert expected == actual


def test_parse_backup_path():
    expected = {
        "project": "whelk",
        "backup": "octopus",
    }
    path = SqlBackupsServiceClient.backup_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlBackupsServiceClient.parse_backup_path(path)
    assert expected == actual


def test_crypto_key_path():
    project = "oyster"
    location = "nudibranch"
    key_ring = "cuttlefish"
    crypto_key = "mussel"
    expected = "projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}".format(
        project=project,
        location=location,
        key_ring=key_ring,
        crypto_key=crypto_key,
    )
    actual = SqlBackupsServiceClient.crypto_key_path(
        project, location, key_ring, crypto_key
    )
    assert expected == actual


def test_parse_crypto_key_path():
    expected = {
        "project": "winkle",
        "location": "nautilus",
        "key_ring": "scallop",
        "crypto_key": "abalone",
    }
    path = SqlBackupsServiceClient.crypto_key_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlBackupsServiceClient.parse_crypto_key_path(path)
    assert expected == actual


def test_crypto_key_version_path():
    project = "squid"
    location = "clam"
    key_ring = "whelk"
    crypto_key = "octopus"
    crypto_key_version = "oyster"
    expected = "projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}".format(
        project=project,
        location=location,
        key_ring=key_ring,
        crypto_key=crypto_key,
        crypto_key_version=crypto_key_version,
    )
    actual = SqlBackupsServiceClient.crypto_key_version_path(
        project, location, key_ring, crypto_key, crypto_key_version
    )
    assert expected == actual


def test_parse_crypto_key_version_path():
    expected = {
        "project": "nudibranch",
        "location": "cuttlefish",
        "key_ring": "mussel",
        "crypto_key": "winkle",
        "crypto_key_version": "nautilus",
    }
    path = SqlBackupsServiceClient.crypto_key_version_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlBackupsServiceClient.parse_crypto_key_version_path(path)
    assert expected == actual


def test_network_attachment_path():
    project = "scallop"
    region = "abalone"
    network_attachment = "squid"
    expected = "projects/{project}/regions/{region}/networkAttachments/{network_attachment}".format(
        project=project,
        region=region,
        network_attachment=network_attachment,
    )
    actual = SqlBackupsServiceClient.network_attachment_path(
        project, region, network_attachment
    )
    assert expected == actual


def test_parse_network_attachment_path():
    expected = {
        "project": "clam",
        "region": "whelk",
        "network_attachment": "octopus",
    }
    path = SqlBackupsServiceClient.network_attachment_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlBackupsServiceClient.parse_network_attachment_path(path)
    assert expected == actual


def test_service_connection_policy_path():
    project = "oyster"
    region = "nudibranch"
    service_connection_policy = "cuttlefish"
    expected = "projects/{project}/regions/{region}/serviceConnectionPolicies/{service_connection_policy}".format(
        project=project,
        region=region,
        service_connection_policy=service_connection_policy,
    )
    actual = SqlBackupsServiceClient.service_connection_policy_path(
        project, region, service_connection_policy
    )
    assert expected == actual


def test_parse_service_connection_policy_path():
    expected = {
        "project": "mussel",
        "region": "winkle",
        "service_connection_policy": "nautilus",
    }
    path = SqlBackupsServiceClient.service_connection_policy_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlBackupsServiceClient.parse_service_connection_policy_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "scallop"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = SqlBackupsServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "abalone",
    }
    path = SqlBackupsServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlBackupsServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "squid"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = SqlBackupsServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "clam",
    }
    path = SqlBackupsServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlBackupsServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "whelk"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = SqlBackupsServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "octopus",
    }
    path = SqlBackupsServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlBackupsServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "oyster"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = SqlBackupsServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "nudibranch",
    }
    path = SqlBackupsServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlBackupsServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "cuttlefish"
    location = "mussel"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = SqlBackupsServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "winkle",
        "location": "nautilus",
    }
    path = SqlBackupsServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = SqlBackupsServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.SqlBackupsServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = SqlBackupsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.SqlBackupsServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = SqlBackupsServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_grpc():
    client = SqlBackupsServiceClient(
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
    client = SqlBackupsServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = SqlBackupsServiceClient(
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
        client = SqlBackupsServiceClient(
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
        (SqlBackupsServiceClient, transports.SqlBackupsServiceGrpcTransport),
        (
            SqlBackupsServiceAsyncClient,
            transports.SqlBackupsServiceGrpcAsyncIOTransport,
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
