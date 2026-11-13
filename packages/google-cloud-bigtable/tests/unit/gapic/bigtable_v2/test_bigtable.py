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

from google.cloud.bigtable_v2.services.bigtable import (
    BigtableAsyncClient,
    BigtableClient,
    transports,
)
from google.cloud.bigtable_v2.types import bigtable, data, request_stats, types

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

    assert BigtableClient._get_client_cert_source(None, False) is None
    assert (
        BigtableClient._get_client_cert_source(mock_provided_cert_source, False) is None
    )
    assert (
        BigtableClient._get_client_cert_source(mock_provided_cert_source, True)
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
                BigtableClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                BigtableClient._get_client_cert_source(
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
    client = BigtableClient(credentials=cred)
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
    client = BigtableClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (BigtableClient, "grpc"),
        (BigtableAsyncClient, "grpc_asyncio"),
        (BigtableClient, "rest"),
    ],
)
def test_bigtable_client_from_service_account_info(client_class, transport_name):
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
            "bigtable.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://bigtable.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.BigtableGrpcTransport, "grpc"),
        (transports.BigtableGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.BigtableRestTransport, "rest"),
    ],
)
def test_bigtable_client_service_account_always_use_jwt(
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
        (BigtableClient, "grpc"),
        (BigtableAsyncClient, "grpc_asyncio"),
        (BigtableClient, "rest"),
    ],
)
def test_bigtable_client_from_service_account_file(client_class, transport_name):
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
            "bigtable.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://bigtable.googleapis.com"
        )


def test_bigtable_client_get_transport_class():
    transport = BigtableClient.get_transport_class()
    available_transports = [
        transports.BigtableGrpcTransport,
        transports.BigtableRestTransport,
    ]
    assert transport in available_transports

    transport = BigtableClient.get_transport_class("grpc")
    assert transport == transports.BigtableGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (BigtableClient, transports.BigtableGrpcTransport, "grpc"),
        (BigtableAsyncClient, transports.BigtableGrpcAsyncIOTransport, "grpc_asyncio"),
        (BigtableClient, transports.BigtableRestTransport, "rest"),
    ],
)
@mock.patch.object(
    BigtableClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(BigtableClient),
)
@mock.patch.object(
    BigtableAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(BigtableAsyncClient),
)
def test_bigtable_client_client_options(client_class, transport_class, transport_name):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(BigtableClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(BigtableClient, "get_transport_class") as gtc:
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
        (BigtableClient, transports.BigtableGrpcTransport, "grpc", "true"),
        (
            BigtableAsyncClient,
            transports.BigtableGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (BigtableClient, transports.BigtableGrpcTransport, "grpc", "false"),
        (
            BigtableAsyncClient,
            transports.BigtableGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (BigtableClient, transports.BigtableRestTransport, "rest", "true"),
        (BigtableClient, transports.BigtableRestTransport, "rest", "false"),
    ],
)
@mock.patch.object(
    BigtableClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(BigtableClient),
)
@mock.patch.object(
    BigtableAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(BigtableAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_bigtable_client_mtls_env_auto(
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


@pytest.mark.parametrize("client_class", [BigtableClient, BigtableAsyncClient])
@mock.patch.object(
    BigtableClient, "DEFAULT_ENDPOINT", modify_default_endpoint(BigtableClient)
)
@mock.patch.object(
    BigtableAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(BigtableAsyncClient),
)
def test_bigtable_client_get_mtls_endpoint_and_cert_source(client_class):
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


@pytest.mark.parametrize("client_class", [BigtableClient, BigtableAsyncClient])
@mock.patch.object(
    BigtableClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(BigtableClient),
)
@mock.patch.object(
    BigtableAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(BigtableAsyncClient),
)
def test_bigtable_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = BigtableClient._DEFAULT_UNIVERSE
    default_endpoint = BigtableClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = BigtableClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
        (BigtableClient, transports.BigtableGrpcTransport, "grpc"),
        (BigtableAsyncClient, transports.BigtableGrpcAsyncIOTransport, "grpc_asyncio"),
        (BigtableClient, transports.BigtableRestTransport, "rest"),
    ],
)
def test_bigtable_client_client_options_scopes(
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
        (BigtableClient, transports.BigtableGrpcTransport, "grpc", grpc_helpers),
        (
            BigtableAsyncClient,
            transports.BigtableGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (BigtableClient, transports.BigtableRestTransport, "rest", None),
    ],
)
def test_bigtable_client_client_options_credentials_file(
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


def test_bigtable_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.bigtable_v2.services.bigtable.transports.BigtableGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = BigtableClient(client_options={"api_endpoint": "squid.clam.whelk"})
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
        (BigtableClient, transports.BigtableGrpcTransport, "grpc", grpc_helpers),
        (
            BigtableAsyncClient,
            transports.BigtableGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_bigtable_client_create_channel_credentials_file(
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
            "bigtable.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
                "https://www.googleapis.com/auth/bigtable.data",
                "https://www.googleapis.com/auth/bigtable.data.readonly",
                "https://www.googleapis.com/auth/cloud-bigtable.data",
                "https://www.googleapis.com/auth/cloud-bigtable.data.readonly",
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/cloud-platform.read-only",
            ),
            scopes=None,
            default_host="bigtable.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.ReadRowsRequest(),
        {},
    ],
)
def test_read_rows(request_type, transport: str = "grpc"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.ReadRowsResponse()])
        response = client.read_rows(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = bigtable.ReadRowsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    for message in response:
        assert isinstance(message, bigtable.ReadRowsResponse)


def test_read_rows_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = bigtable.ReadRowsRequest(
        table_name="table_name_value",
        authorized_view_name="authorized_view_name_value",
        materialized_view_name="materialized_view_name_value",
        app_profile_id="app_profile_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.read_rows(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest(
            table_name="table_name_value",
            authorized_view_name="authorized_view_name_value",
            materialized_view_name="materialized_view_name_value",
            app_profile_id="app_profile_id_value",
        )
        assert args[0] == request_msg


def test_read_rows_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.read_rows in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.read_rows] = mock_rpc
        request = {}
        client.read_rows(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.read_rows(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_read_rows_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = BigtableAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.read_rows
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.read_rows
        ] = mock_rpc

        request = {}
        await client.read_rows(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.read_rows(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.ReadRowsRequest(),
        {},
    ],
)
async def test_read_rows_async(request_type, transport: str = "grpc_asyncio"):
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.ReadRowsResponse()]
        )
        response = await client.read_rows(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = bigtable.ReadRowsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    message = await response.read()
    assert isinstance(message, bigtable.ReadRowsResponse)


def test_read_rows_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.ReadRowsResponse()])
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.read_rows(
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


def test_read_rows_flattened_error():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.read_rows(
            bigtable.ReadRowsRequest(),
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.asyncio
async def test_read_rows_flattened_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.ReadRowsResponse()])

        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.read_rows(
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_read_rows_flattened_error_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.read_rows(
            bigtable.ReadRowsRequest(),
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.SampleRowKeysRequest(),
        {},
    ],
)
def test_sample_row_keys(request_type, transport: str = "grpc"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.SampleRowKeysResponse()])
        response = client.sample_row_keys(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = bigtable.SampleRowKeysRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    for message in response:
        assert isinstance(message, bigtable.SampleRowKeysResponse)


def test_sample_row_keys_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = bigtable.SampleRowKeysRequest(
        table_name="table_name_value",
        authorized_view_name="authorized_view_name_value",
        materialized_view_name="materialized_view_name_value",
        app_profile_id="app_profile_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.sample_row_keys(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest(
            table_name="table_name_value",
            authorized_view_name="authorized_view_name_value",
            materialized_view_name="materialized_view_name_value",
            app_profile_id="app_profile_id_value",
        )
        assert args[0] == request_msg


def test_sample_row_keys_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.sample_row_keys in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.sample_row_keys] = mock_rpc
        request = {}
        client.sample_row_keys(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.sample_row_keys(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_sample_row_keys_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = BigtableAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.sample_row_keys
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.sample_row_keys
        ] = mock_rpc

        request = {}
        await client.sample_row_keys(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.sample_row_keys(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.SampleRowKeysRequest(),
        {},
    ],
)
async def test_sample_row_keys_async(request_type, transport: str = "grpc_asyncio"):
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.SampleRowKeysResponse()]
        )
        response = await client.sample_row_keys(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = bigtable.SampleRowKeysRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    message = await response.read()
    assert isinstance(message, bigtable.SampleRowKeysResponse)


def test_sample_row_keys_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.SampleRowKeysResponse()])
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.sample_row_keys(
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


def test_sample_row_keys_flattened_error():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.sample_row_keys(
            bigtable.SampleRowKeysRequest(),
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.asyncio
async def test_sample_row_keys_flattened_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.SampleRowKeysResponse()])

        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.sample_row_keys(
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_sample_row_keys_flattened_error_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.sample_row_keys(
            bigtable.SampleRowKeysRequest(),
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.MutateRowRequest(),
        {},
    ],
)
def test_mutate_row(request_type, transport: str = "grpc"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.MutateRowResponse()
        response = client.mutate_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = bigtable.MutateRowRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.MutateRowResponse)


def test_mutate_row_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = bigtable.MutateRowRequest(
        table_name="table_name_value",
        authorized_view_name="authorized_view_name_value",
        app_profile_id="app_profile_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.mutate_row(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.MutateRowRequest(
            table_name="table_name_value",
            authorized_view_name="authorized_view_name_value",
            app_profile_id="app_profile_id_value",
        )
        assert args[0] == request_msg


def test_mutate_row_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.mutate_row in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.mutate_row] = mock_rpc
        request = {}
        client.mutate_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.mutate_row(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_mutate_row_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = BigtableAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.mutate_row
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.mutate_row
        ] = mock_rpc

        request = {}
        await client.mutate_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.mutate_row(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.MutateRowRequest(),
        {},
    ],
)
async def test_mutate_row_async(request_type, transport: str = "grpc_asyncio"):
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.MutateRowResponse()
        )
        response = await client.mutate_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = bigtable.MutateRowRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.MutateRowResponse)


def test_mutate_row_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.MutateRowResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.mutate_row(
            table_name="table_name_value",
            row_key=b"row_key_blob",
            mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].row_key
        mock_val = b"row_key_blob"
        assert arg == mock_val
        arg = args[0].mutations
        mock_val = [
            data.Mutation(
                set_cell=data.Mutation.SetCell(family_name="family_name_value")
            )
        ]
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


def test_mutate_row_flattened_error():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.mutate_row(
            bigtable.MutateRowRequest(),
            table_name="table_name_value",
            row_key=b"row_key_blob",
            mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.asyncio
async def test_mutate_row_flattened_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.MutateRowResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.MutateRowResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.mutate_row(
            table_name="table_name_value",
            row_key=b"row_key_blob",
            mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].row_key
        mock_val = b"row_key_blob"
        assert arg == mock_val
        arg = args[0].mutations
        mock_val = [
            data.Mutation(
                set_cell=data.Mutation.SetCell(family_name="family_name_value")
            )
        ]
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_mutate_row_flattened_error_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.mutate_row(
            bigtable.MutateRowRequest(),
            table_name="table_name_value",
            row_key=b"row_key_blob",
            mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.MutateRowsRequest(),
        {},
    ],
)
def test_mutate_rows(request_type, transport: str = "grpc"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.MutateRowsResponse()])
        response = client.mutate_rows(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = bigtable.MutateRowsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    for message in response:
        assert isinstance(message, bigtable.MutateRowsResponse)


def test_mutate_rows_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = bigtable.MutateRowsRequest(
        table_name="table_name_value",
        authorized_view_name="authorized_view_name_value",
        app_profile_id="app_profile_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.mutate_rows(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.MutateRowsRequest(
            table_name="table_name_value",
            authorized_view_name="authorized_view_name_value",
            app_profile_id="app_profile_id_value",
        )
        assert args[0] == request_msg


def test_mutate_rows_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.mutate_rows in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.mutate_rows] = mock_rpc
        request = {}
        client.mutate_rows(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.mutate_rows(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_mutate_rows_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = BigtableAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.mutate_rows
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.mutate_rows
        ] = mock_rpc

        request = {}
        await client.mutate_rows(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.mutate_rows(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.MutateRowsRequest(),
        {},
    ],
)
async def test_mutate_rows_async(request_type, transport: str = "grpc_asyncio"):
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.MutateRowsResponse()]
        )
        response = await client.mutate_rows(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = bigtable.MutateRowsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    message = await response.read()
    assert isinstance(message, bigtable.MutateRowsResponse)


def test_mutate_rows_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.MutateRowsResponse()])
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.mutate_rows(
            table_name="table_name_value",
            entries=[bigtable.MutateRowsRequest.Entry(row_key=b"row_key_blob")],
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].entries
        mock_val = [bigtable.MutateRowsRequest.Entry(row_key=b"row_key_blob")]
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


def test_mutate_rows_flattened_error():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.mutate_rows(
            bigtable.MutateRowsRequest(),
            table_name="table_name_value",
            entries=[bigtable.MutateRowsRequest.Entry(row_key=b"row_key_blob")],
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.asyncio
async def test_mutate_rows_flattened_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.MutateRowsResponse()])

        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.mutate_rows(
            table_name="table_name_value",
            entries=[bigtable.MutateRowsRequest.Entry(row_key=b"row_key_blob")],
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].entries
        mock_val = [bigtable.MutateRowsRequest.Entry(row_key=b"row_key_blob")]
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_mutate_rows_flattened_error_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.mutate_rows(
            bigtable.MutateRowsRequest(),
            table_name="table_name_value",
            entries=[bigtable.MutateRowsRequest.Entry(row_key=b"row_key_blob")],
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.CheckAndMutateRowRequest(),
        {},
    ],
)
def test_check_and_mutate_row(request_type, transport: str = "grpc"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.CheckAndMutateRowResponse(
            predicate_matched=True,
        )
        response = client.check_and_mutate_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = bigtable.CheckAndMutateRowRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.CheckAndMutateRowResponse)
    assert response.predicate_matched is True


def test_check_and_mutate_row_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = bigtable.CheckAndMutateRowRequest(
        table_name="table_name_value",
        authorized_view_name="authorized_view_name_value",
        app_profile_id="app_profile_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.check_and_mutate_row(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.CheckAndMutateRowRequest(
            table_name="table_name_value",
            authorized_view_name="authorized_view_name_value",
            app_profile_id="app_profile_id_value",
        )
        assert args[0] == request_msg


def test_check_and_mutate_row_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.check_and_mutate_row in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.check_and_mutate_row] = (
            mock_rpc
        )
        request = {}
        client.check_and_mutate_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.check_and_mutate_row(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_check_and_mutate_row_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = BigtableAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.check_and_mutate_row
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.check_and_mutate_row
        ] = mock_rpc

        request = {}
        await client.check_and_mutate_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.check_and_mutate_row(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.CheckAndMutateRowRequest(),
        {},
    ],
)
async def test_check_and_mutate_row_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.CheckAndMutateRowResponse(
                predicate_matched=True,
            )
        )
        response = await client.check_and_mutate_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = bigtable.CheckAndMutateRowRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.CheckAndMutateRowResponse)
    assert response.predicate_matched is True


def test_check_and_mutate_row_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.CheckAndMutateRowResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.check_and_mutate_row(
            table_name="table_name_value",
            row_key=b"row_key_blob",
            predicate_filter=data.RowFilter(
                chain=data.RowFilter.Chain(
                    filters=[
                        data.RowFilter(
                            chain=data.RowFilter.Chain(
                                filters=[data.RowFilter(chain=None)]
                            )
                        )
                    ]
                )
            ),
            true_mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            false_mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].row_key
        mock_val = b"row_key_blob"
        assert arg == mock_val
        arg = args[0].predicate_filter
        mock_val = data.RowFilter(
            chain=data.RowFilter.Chain(
                filters=[
                    data.RowFilter(
                        chain=data.RowFilter.Chain(filters=[data.RowFilter(chain=None)])
                    )
                ]
            )
        )
        assert arg == mock_val
        arg = args[0].true_mutations
        mock_val = [
            data.Mutation(
                set_cell=data.Mutation.SetCell(family_name="family_name_value")
            )
        ]
        assert arg == mock_val
        arg = args[0].false_mutations
        mock_val = [
            data.Mutation(
                set_cell=data.Mutation.SetCell(family_name="family_name_value")
            )
        ]
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


def test_check_and_mutate_row_flattened_error():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.check_and_mutate_row(
            bigtable.CheckAndMutateRowRequest(),
            table_name="table_name_value",
            row_key=b"row_key_blob",
            predicate_filter=data.RowFilter(
                chain=data.RowFilter.Chain(
                    filters=[
                        data.RowFilter(
                            chain=data.RowFilter.Chain(
                                filters=[data.RowFilter(chain=None)]
                            )
                        )
                    ]
                )
            ),
            true_mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            false_mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.asyncio
async def test_check_and_mutate_row_flattened_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.CheckAndMutateRowResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.CheckAndMutateRowResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.check_and_mutate_row(
            table_name="table_name_value",
            row_key=b"row_key_blob",
            predicate_filter=data.RowFilter(
                chain=data.RowFilter.Chain(
                    filters=[
                        data.RowFilter(
                            chain=data.RowFilter.Chain(
                                filters=[data.RowFilter(chain=None)]
                            )
                        )
                    ]
                )
            ),
            true_mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            false_mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].row_key
        mock_val = b"row_key_blob"
        assert arg == mock_val
        arg = args[0].predicate_filter
        mock_val = data.RowFilter(
            chain=data.RowFilter.Chain(
                filters=[
                    data.RowFilter(
                        chain=data.RowFilter.Chain(filters=[data.RowFilter(chain=None)])
                    )
                ]
            )
        )
        assert arg == mock_val
        arg = args[0].true_mutations
        mock_val = [
            data.Mutation(
                set_cell=data.Mutation.SetCell(family_name="family_name_value")
            )
        ]
        assert arg == mock_val
        arg = args[0].false_mutations
        mock_val = [
            data.Mutation(
                set_cell=data.Mutation.SetCell(family_name="family_name_value")
            )
        ]
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_check_and_mutate_row_flattened_error_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.check_and_mutate_row(
            bigtable.CheckAndMutateRowRequest(),
            table_name="table_name_value",
            row_key=b"row_key_blob",
            predicate_filter=data.RowFilter(
                chain=data.RowFilter.Chain(
                    filters=[
                        data.RowFilter(
                            chain=data.RowFilter.Chain(
                                filters=[data.RowFilter(chain=None)]
                            )
                        )
                    ]
                )
            ),
            true_mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            false_mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.PingAndWarmRequest(),
        {},
    ],
)
def test_ping_and_warm(request_type, transport: str = "grpc"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.ping_and_warm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.PingAndWarmResponse()
        response = client.ping_and_warm(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = bigtable.PingAndWarmRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.PingAndWarmResponse)


def test_ping_and_warm_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = bigtable.PingAndWarmRequest(
        name="name_value",
        app_profile_id="app_profile_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.ping_and_warm), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.ping_and_warm(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.PingAndWarmRequest(
            name="name_value",
            app_profile_id="app_profile_id_value",
        )
        assert args[0] == request_msg


def test_ping_and_warm_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.ping_and_warm in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.ping_and_warm] = mock_rpc
        request = {}
        client.ping_and_warm(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.ping_and_warm(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_ping_and_warm_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = BigtableAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.ping_and_warm
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.ping_and_warm
        ] = mock_rpc

        request = {}
        await client.ping_and_warm(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.ping_and_warm(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.PingAndWarmRequest(),
        {},
    ],
)
async def test_ping_and_warm_async(request_type, transport: str = "grpc_asyncio"):
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.ping_and_warm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.PingAndWarmResponse()
        )
        response = await client.ping_and_warm(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = bigtable.PingAndWarmRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.PingAndWarmResponse)


def test_ping_and_warm_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.ping_and_warm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.PingAndWarmResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.ping_and_warm(
            name="name_value",
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


def test_ping_and_warm_flattened_error():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.ping_and_warm(
            bigtable.PingAndWarmRequest(),
            name="name_value",
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.asyncio
async def test_ping_and_warm_flattened_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.ping_and_warm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.PingAndWarmResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.PingAndWarmResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.ping_and_warm(
            name="name_value",
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_ping_and_warm_flattened_error_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.ping_and_warm(
            bigtable.PingAndWarmRequest(),
            name="name_value",
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.ReadModifyWriteRowRequest(),
        {},
    ],
)
def test_read_modify_write_row(request_type, transport: str = "grpc"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.ReadModifyWriteRowResponse()
        response = client.read_modify_write_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = bigtable.ReadModifyWriteRowRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.ReadModifyWriteRowResponse)


def test_read_modify_write_row_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = bigtable.ReadModifyWriteRowRequest(
        table_name="table_name_value",
        authorized_view_name="authorized_view_name_value",
        app_profile_id="app_profile_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.read_modify_write_row(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ReadModifyWriteRowRequest(
            table_name="table_name_value",
            authorized_view_name="authorized_view_name_value",
            app_profile_id="app_profile_id_value",
        )
        assert args[0] == request_msg


def test_read_modify_write_row_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.read_modify_write_row
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.read_modify_write_row] = (
            mock_rpc
        )
        request = {}
        client.read_modify_write_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.read_modify_write_row(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_read_modify_write_row_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = BigtableAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.read_modify_write_row
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.read_modify_write_row
        ] = mock_rpc

        request = {}
        await client.read_modify_write_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.read_modify_write_row(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.ReadModifyWriteRowRequest(),
        {},
    ],
)
async def test_read_modify_write_row_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.ReadModifyWriteRowResponse()
        )
        response = await client.read_modify_write_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = bigtable.ReadModifyWriteRowRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.ReadModifyWriteRowResponse)


def test_read_modify_write_row_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.ReadModifyWriteRowResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.read_modify_write_row(
            table_name="table_name_value",
            row_key=b"row_key_blob",
            rules=[data.ReadModifyWriteRule(family_name="family_name_value")],
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].row_key
        mock_val = b"row_key_blob"
        assert arg == mock_val
        arg = args[0].rules
        mock_val = [data.ReadModifyWriteRule(family_name="family_name_value")]
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


def test_read_modify_write_row_flattened_error():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.read_modify_write_row(
            bigtable.ReadModifyWriteRowRequest(),
            table_name="table_name_value",
            row_key=b"row_key_blob",
            rules=[data.ReadModifyWriteRule(family_name="family_name_value")],
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.asyncio
async def test_read_modify_write_row_flattened_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.ReadModifyWriteRowResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.ReadModifyWriteRowResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.read_modify_write_row(
            table_name="table_name_value",
            row_key=b"row_key_blob",
            rules=[data.ReadModifyWriteRule(family_name="family_name_value")],
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].row_key
        mock_val = b"row_key_blob"
        assert arg == mock_val
        arg = args[0].rules
        mock_val = [data.ReadModifyWriteRule(family_name="family_name_value")]
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_read_modify_write_row_flattened_error_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.read_modify_write_row(
            bigtable.ReadModifyWriteRowRequest(),
            table_name="table_name_value",
            row_key=b"row_key_blob",
            rules=[data.ReadModifyWriteRule(family_name="family_name_value")],
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.GenerateInitialChangeStreamPartitionsRequest(),
        {},
    ],
)
def test_generate_initial_change_stream_partitions(
    request_type, transport: str = "grpc"
):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_initial_change_stream_partitions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter(
            [bigtable.GenerateInitialChangeStreamPartitionsResponse()]
        )
        response = client.generate_initial_change_stream_partitions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = bigtable.GenerateInitialChangeStreamPartitionsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    for message in response:
        assert isinstance(
            message, bigtable.GenerateInitialChangeStreamPartitionsResponse
        )


def test_generate_initial_change_stream_partitions_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = bigtable.GenerateInitialChangeStreamPartitionsRequest(
        table_name="table_name_value",
        app_profile_id="app_profile_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_initial_change_stream_partitions), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.generate_initial_change_stream_partitions(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.GenerateInitialChangeStreamPartitionsRequest(
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )
        assert args[0] == request_msg


def test_generate_initial_change_stream_partitions_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.generate_initial_change_stream_partitions
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.generate_initial_change_stream_partitions
        ] = mock_rpc
        request = {}
        client.generate_initial_change_stream_partitions(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.generate_initial_change_stream_partitions(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_generate_initial_change_stream_partitions_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = BigtableAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.generate_initial_change_stream_partitions
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.generate_initial_change_stream_partitions
        ] = mock_rpc

        request = {}
        await client.generate_initial_change_stream_partitions(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.generate_initial_change_stream_partitions(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.GenerateInitialChangeStreamPartitionsRequest(),
        {},
    ],
)
async def test_generate_initial_change_stream_partitions_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_initial_change_stream_partitions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.GenerateInitialChangeStreamPartitionsResponse()]
        )
        response = await client.generate_initial_change_stream_partitions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = bigtable.GenerateInitialChangeStreamPartitionsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    message = await response.read()
    assert isinstance(message, bigtable.GenerateInitialChangeStreamPartitionsResponse)


def test_generate_initial_change_stream_partitions_field_headers():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = bigtable.GenerateInitialChangeStreamPartitionsRequest()

    request.table_name = "table_name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_initial_change_stream_partitions), "__call__"
    ) as call:
        call.return_value = iter(
            [bigtable.GenerateInitialChangeStreamPartitionsResponse()]
        )
        client.generate_initial_change_stream_partitions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "table_name=table_name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_generate_initial_change_stream_partitions_field_headers_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = bigtable.GenerateInitialChangeStreamPartitionsRequest()

    request.table_name = "table_name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_initial_change_stream_partitions), "__call__"
    ) as call:
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.GenerateInitialChangeStreamPartitionsResponse()]
        )
        await client.generate_initial_change_stream_partitions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "table_name=table_name_value",
    ) in kw["metadata"]


def test_generate_initial_change_stream_partitions_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_initial_change_stream_partitions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter(
            [bigtable.GenerateInitialChangeStreamPartitionsResponse()]
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.generate_initial_change_stream_partitions(
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


def test_generate_initial_change_stream_partitions_flattened_error():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.generate_initial_change_stream_partitions(
            bigtable.GenerateInitialChangeStreamPartitionsRequest(),
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.asyncio
async def test_generate_initial_change_stream_partitions_flattened_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_initial_change_stream_partitions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter(
            [bigtable.GenerateInitialChangeStreamPartitionsResponse()]
        )

        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.generate_initial_change_stream_partitions(
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_generate_initial_change_stream_partitions_flattened_error_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.generate_initial_change_stream_partitions(
            bigtable.GenerateInitialChangeStreamPartitionsRequest(),
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.ReadChangeStreamRequest(),
        {},
    ],
)
def test_read_change_stream(request_type, transport: str = "grpc"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.read_change_stream), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.ReadChangeStreamResponse()])
        response = client.read_change_stream(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = bigtable.ReadChangeStreamRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    for message in response:
        assert isinstance(message, bigtable.ReadChangeStreamResponse)


def test_read_change_stream_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = bigtable.ReadChangeStreamRequest(
        table_name="table_name_value",
        app_profile_id="app_profile_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.read_change_stream), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.read_change_stream(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ReadChangeStreamRequest(
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )
        assert args[0] == request_msg


def test_read_change_stream_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.read_change_stream in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.read_change_stream] = (
            mock_rpc
        )
        request = {}
        client.read_change_stream(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.read_change_stream(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_read_change_stream_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = BigtableAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.read_change_stream
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.read_change_stream
        ] = mock_rpc

        request = {}
        await client.read_change_stream(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.read_change_stream(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.ReadChangeStreamRequest(),
        {},
    ],
)
async def test_read_change_stream_async(request_type, transport: str = "grpc_asyncio"):
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.read_change_stream), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.ReadChangeStreamResponse()]
        )
        response = await client.read_change_stream(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = bigtable.ReadChangeStreamRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    message = await response.read()
    assert isinstance(message, bigtable.ReadChangeStreamResponse)


def test_read_change_stream_field_headers():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = bigtable.ReadChangeStreamRequest()

    request.table_name = "table_name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.read_change_stream), "__call__"
    ) as call:
        call.return_value = iter([bigtable.ReadChangeStreamResponse()])
        client.read_change_stream(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "table_name=table_name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_read_change_stream_field_headers_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = bigtable.ReadChangeStreamRequest()

    request.table_name = "table_name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.read_change_stream), "__call__"
    ) as call:
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.ReadChangeStreamResponse()]
        )
        await client.read_change_stream(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "table_name=table_name_value",
    ) in kw["metadata"]


def test_read_change_stream_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.read_change_stream), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.ReadChangeStreamResponse()])
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.read_change_stream(
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


def test_read_change_stream_flattened_error():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.read_change_stream(
            bigtable.ReadChangeStreamRequest(),
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.asyncio
async def test_read_change_stream_flattened_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.read_change_stream), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.ReadChangeStreamResponse()])

        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.read_change_stream(
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].table_name
        mock_val = "table_name_value"
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_read_change_stream_flattened_error_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.read_change_stream(
            bigtable.ReadChangeStreamRequest(),
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.PrepareQueryRequest(),
        {},
    ],
)
def test_prepare_query(request_type, transport: str = "grpc"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.PrepareQueryResponse(
            prepared_query=b"prepared_query_blob",
        )
        response = client.prepare_query(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = bigtable.PrepareQueryRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.PrepareQueryResponse)
    assert response.prepared_query == b"prepared_query_blob"


def test_prepare_query_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = bigtable.PrepareQueryRequest(
        instance_name="instance_name_value",
        app_profile_id="app_profile_id_value",
        query="query_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.prepare_query(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.PrepareQueryRequest(
            instance_name="instance_name_value",
            app_profile_id="app_profile_id_value",
            query="query_value",
        )
        assert args[0] == request_msg


def test_prepare_query_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.prepare_query in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.prepare_query] = mock_rpc
        request = {}
        client.prepare_query(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.prepare_query(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_prepare_query_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = BigtableAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.prepare_query
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.prepare_query
        ] = mock_rpc

        request = {}
        await client.prepare_query(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.prepare_query(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.PrepareQueryRequest(),
        {},
    ],
)
async def test_prepare_query_async(request_type, transport: str = "grpc_asyncio"):
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.PrepareQueryResponse(
                prepared_query=b"prepared_query_blob",
            )
        )
        response = await client.prepare_query(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = bigtable.PrepareQueryRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.PrepareQueryResponse)
    assert response.prepared_query == b"prepared_query_blob"


def test_prepare_query_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.PrepareQueryResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.prepare_query(
            instance_name="instance_name_value",
            query="query_value",
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].instance_name
        mock_val = "instance_name_value"
        assert arg == mock_val
        arg = args[0].query
        mock_val = "query_value"
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


def test_prepare_query_flattened_error():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.prepare_query(
            bigtable.PrepareQueryRequest(),
            instance_name="instance_name_value",
            query="query_value",
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.asyncio
async def test_prepare_query_flattened_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = bigtable.PrepareQueryResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.PrepareQueryResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.prepare_query(
            instance_name="instance_name_value",
            query="query_value",
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].instance_name
        mock_val = "instance_name_value"
        assert arg == mock_val
        arg = args[0].query
        mock_val = "query_value"
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_prepare_query_flattened_error_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.prepare_query(
            bigtable.PrepareQueryRequest(),
            instance_name="instance_name_value",
            query="query_value",
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.ExecuteQueryRequest(),
        {},
    ],
)
def test_execute_query(request_type, transport: str = "grpc"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.ExecuteQueryResponse()])
        response = client.execute_query(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = bigtable.ExecuteQueryRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    for message in response:
        assert isinstance(message, bigtable.ExecuteQueryResponse)


def test_execute_query_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = bigtable.ExecuteQueryRequest(
        instance_name="instance_name_value",
        app_profile_id="app_profile_id_value",
        query="query_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.execute_query(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ExecuteQueryRequest(
            instance_name="instance_name_value",
            app_profile_id="app_profile_id_value",
            query="query_value",
        )
        assert args[0] == request_msg


def test_execute_query_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.execute_query in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.execute_query] = mock_rpc
        request = {}
        client.execute_query(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.execute_query(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_execute_query_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = BigtableAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.execute_query
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.execute_query
        ] = mock_rpc

        request = {}
        await client.execute_query(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.execute_query(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.ExecuteQueryRequest(),
        {},
    ],
)
async def test_execute_query_async(request_type, transport: str = "grpc_asyncio"):
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.ExecuteQueryResponse()]
        )
        response = await client.execute_query(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = bigtable.ExecuteQueryRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    message = await response.read()
    assert isinstance(message, bigtable.ExecuteQueryResponse)


def test_execute_query_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.ExecuteQueryResponse()])
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.execute_query(
            instance_name="instance_name_value",
            query="query_value",
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].instance_name
        mock_val = "instance_name_value"
        assert arg == mock_val
        arg = args[0].query
        mock_val = "query_value"
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


def test_execute_query_flattened_error():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.execute_query(
            bigtable.ExecuteQueryRequest(),
            instance_name="instance_name_value",
            query="query_value",
            app_profile_id="app_profile_id_value",
        )


@pytest.mark.asyncio
async def test_execute_query_flattened_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = iter([bigtable.ExecuteQueryResponse()])

        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.execute_query(
            instance_name="instance_name_value",
            query="query_value",
            app_profile_id="app_profile_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].instance_name
        mock_val = "instance_name_value"
        assert arg == mock_val
        arg = args[0].query
        mock_val = "query_value"
        assert arg == mock_val
        arg = args[0].app_profile_id
        mock_val = "app_profile_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_execute_query_flattened_error_async():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.execute_query(
            bigtable.ExecuteQueryRequest(),
            instance_name="instance_name_value",
            query="query_value",
            app_profile_id="app_profile_id_value",
        )


def test_read_rows_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.read_rows in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.read_rows] = mock_rpc

        request = {}
        client.read_rows(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.read_rows(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_read_rows_rest_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.ReadRowsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = bigtable.ReadRowsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        json_return_value = "[{}]".format(json_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        with mock.patch.object(response_value, "iter_content") as iter_content:
            iter_content.return_value = iter(json_return_value)
            client.read_rows(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v2/{table_name=projects/*/instances/*/tables/*}:readRows"
            % client.transport._host,
            args[1],
        )


def test_read_rows_rest_flattened_error(transport: str = "rest"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.read_rows(
            bigtable.ReadRowsRequest(),
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )


def test_sample_row_keys_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.sample_row_keys in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.sample_row_keys] = mock_rpc

        request = {}
        client.sample_row_keys(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.sample_row_keys(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_sample_row_keys_rest_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.SampleRowKeysResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = bigtable.SampleRowKeysResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        json_return_value = "[{}]".format(json_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        with mock.patch.object(response_value, "iter_content") as iter_content:
            iter_content.return_value = iter(json_return_value)
            client.sample_row_keys(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v2/{table_name=projects/*/instances/*/tables/*}:sampleRowKeys"
            % client.transport._host,
            args[1],
        )


def test_sample_row_keys_rest_flattened_error(transport: str = "rest"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.sample_row_keys(
            bigtable.SampleRowKeysRequest(),
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )


def test_mutate_row_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.mutate_row in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.mutate_row] = mock_rpc

        request = {}
        client.mutate_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.mutate_row(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_mutate_row_rest_required_fields(request_type=bigtable.MutateRowRequest):
    transport_class = transports.BigtableRestTransport

    request_init = {}
    request_init["row_key"] = b""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseMutateRow,
        "_BaseMutateRow__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["rowKey"] = b"row_key_blob"

    # verify required fields with non-default values are left alone
    assert "rowKey" in jsonified_request
    assert jsonified_request["rowKey"] == b"row_key_blob"

    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = bigtable.MutateRowResponse()
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
            return_value = bigtable.MutateRowResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.mutate_row(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_mutate_row_rest_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.MutateRowResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            table_name="table_name_value",
            row_key=b"row_key_blob",
            mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            app_profile_id="app_profile_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = bigtable.MutateRowResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.mutate_row(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v2/{table_name=projects/*/instances/*/tables/*}:mutateRow"
            % client.transport._host,
            args[1],
        )


def test_mutate_row_rest_flattened_error(transport: str = "rest"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.mutate_row(
            bigtable.MutateRowRequest(),
            table_name="table_name_value",
            row_key=b"row_key_blob",
            mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            app_profile_id="app_profile_id_value",
        )


def test_mutate_rows_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.mutate_rows in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.mutate_rows] = mock_rpc

        request = {}
        client.mutate_rows(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.mutate_rows(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_mutate_rows_rest_required_fields(request_type=bigtable.MutateRowsRequest):
    transport_class = transports.BigtableRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseMutateRows,
        "_BaseMutateRows__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    # verify required fields with non-default values are left alone

    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = bigtable.MutateRowsResponse()
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
            return_value = bigtable.MutateRowsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)
            json_return_value = "[{}]".format(json_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            with mock.patch.object(response_value, "iter_content") as iter_content:
                iter_content.return_value = iter(json_return_value)
                response = client.mutate_rows(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_mutate_rows_rest_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.MutateRowsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            table_name="table_name_value",
            entries=[bigtable.MutateRowsRequest.Entry(row_key=b"row_key_blob")],
            app_profile_id="app_profile_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = bigtable.MutateRowsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        json_return_value = "[{}]".format(json_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        with mock.patch.object(response_value, "iter_content") as iter_content:
            iter_content.return_value = iter(json_return_value)
            client.mutate_rows(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v2/{table_name=projects/*/instances/*/tables/*}:mutateRows"
            % client.transport._host,
            args[1],
        )


def test_mutate_rows_rest_flattened_error(transport: str = "rest"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.mutate_rows(
            bigtable.MutateRowsRequest(),
            table_name="table_name_value",
            entries=[bigtable.MutateRowsRequest.Entry(row_key=b"row_key_blob")],
            app_profile_id="app_profile_id_value",
        )


def test_check_and_mutate_row_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.check_and_mutate_row in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.check_and_mutate_row] = (
            mock_rpc
        )

        request = {}
        client.check_and_mutate_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.check_and_mutate_row(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_check_and_mutate_row_rest_required_fields(
    request_type=bigtable.CheckAndMutateRowRequest,
):
    transport_class = transports.BigtableRestTransport

    request_init = {}
    request_init["row_key"] = b""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCheckAndMutateRow,
        "_BaseCheckAndMutateRow__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["rowKey"] = b"row_key_blob"

    # verify required fields with non-default values are left alone
    assert "rowKey" in jsonified_request
    assert jsonified_request["rowKey"] == b"row_key_blob"

    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = bigtable.CheckAndMutateRowResponse()
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
            return_value = bigtable.CheckAndMutateRowResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.check_and_mutate_row(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_check_and_mutate_row_rest_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.CheckAndMutateRowResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            table_name="table_name_value",
            row_key=b"row_key_blob",
            predicate_filter=data.RowFilter(
                chain=data.RowFilter.Chain(
                    filters=[
                        data.RowFilter(
                            chain=data.RowFilter.Chain(
                                filters=[data.RowFilter(chain=None)]
                            )
                        )
                    ]
                )
            ),
            true_mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            false_mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            app_profile_id="app_profile_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = bigtable.CheckAndMutateRowResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.check_and_mutate_row(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v2/{table_name=projects/*/instances/*/tables/*}:checkAndMutateRow"
            % client.transport._host,
            args[1],
        )


def test_check_and_mutate_row_rest_flattened_error(transport: str = "rest"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.check_and_mutate_row(
            bigtable.CheckAndMutateRowRequest(),
            table_name="table_name_value",
            row_key=b"row_key_blob",
            predicate_filter=data.RowFilter(
                chain=data.RowFilter.Chain(
                    filters=[
                        data.RowFilter(
                            chain=data.RowFilter.Chain(
                                filters=[data.RowFilter(chain=None)]
                            )
                        )
                    ]
                )
            ),
            true_mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            false_mutations=[
                data.Mutation(
                    set_cell=data.Mutation.SetCell(family_name="family_name_value")
                )
            ],
            app_profile_id="app_profile_id_value",
        )


def test_ping_and_warm_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.ping_and_warm in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.ping_and_warm] = mock_rpc

        request = {}
        client.ping_and_warm(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.ping_and_warm(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_ping_and_warm_rest_required_fields(request_type=bigtable.PingAndWarmRequest):
    transport_class = transports.BigtableRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BasePingAndWarm,
        "_BasePingAndWarm__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = bigtable.PingAndWarmResponse()
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
            return_value = bigtable.PingAndWarmResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.ping_and_warm(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_ping_and_warm_rest_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.PingAndWarmResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/instances/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
            app_profile_id="app_profile_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = bigtable.PingAndWarmResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.ping_and_warm(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v2/{name=projects/*/instances/*}:ping" % client.transport._host, args[1]
        )


def test_ping_and_warm_rest_flattened_error(transport: str = "rest"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.ping_and_warm(
            bigtable.PingAndWarmRequest(),
            name="name_value",
            app_profile_id="app_profile_id_value",
        )


def test_read_modify_write_row_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.read_modify_write_row
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.read_modify_write_row] = (
            mock_rpc
        )

        request = {}
        client.read_modify_write_row(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.read_modify_write_row(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_read_modify_write_row_rest_required_fields(
    request_type=bigtable.ReadModifyWriteRowRequest,
):
    transport_class = transports.BigtableRestTransport

    request_init = {}
    request_init["row_key"] = b""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseReadModifyWriteRow,
        "_BaseReadModifyWriteRow__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["rowKey"] = b"row_key_blob"

    # verify required fields with non-default values are left alone
    assert "rowKey" in jsonified_request
    assert jsonified_request["rowKey"] == b"row_key_blob"

    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = bigtable.ReadModifyWriteRowResponse()
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
            return_value = bigtable.ReadModifyWriteRowResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.read_modify_write_row(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_read_modify_write_row_rest_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.ReadModifyWriteRowResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            table_name="table_name_value",
            row_key=b"row_key_blob",
            rules=[data.ReadModifyWriteRule(family_name="family_name_value")],
            app_profile_id="app_profile_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = bigtable.ReadModifyWriteRowResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.read_modify_write_row(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v2/{table_name=projects/*/instances/*/tables/*}:readModifyWriteRow"
            % client.transport._host,
            args[1],
        )


def test_read_modify_write_row_rest_flattened_error(transport: str = "rest"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.read_modify_write_row(
            bigtable.ReadModifyWriteRowRequest(),
            table_name="table_name_value",
            row_key=b"row_key_blob",
            rules=[data.ReadModifyWriteRule(family_name="family_name_value")],
            app_profile_id="app_profile_id_value",
        )


def test_generate_initial_change_stream_partitions_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.generate_initial_change_stream_partitions
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.generate_initial_change_stream_partitions
        ] = mock_rpc

        request = {}
        client.generate_initial_change_stream_partitions(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.generate_initial_change_stream_partitions(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_generate_initial_change_stream_partitions_rest_required_fields(
    request_type=bigtable.GenerateInitialChangeStreamPartitionsRequest,
):
    transport_class = transports.BigtableRestTransport

    request_init = {}
    request_init["table_name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGenerateInitialChangeStreamPartitions,
        "_BaseGenerateInitialChangeStreamPartitions__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["tableName"] = "table_name_value"

    # verify required fields with non-default values are left alone
    assert "tableName" in jsonified_request
    assert jsonified_request["tableName"] == "table_name_value"

    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = bigtable.GenerateInitialChangeStreamPartitionsResponse()
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
            return_value = bigtable.GenerateInitialChangeStreamPartitionsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)
            json_return_value = "[{}]".format(json_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            with mock.patch.object(response_value, "iter_content") as iter_content:
                iter_content.return_value = iter(json_return_value)
                response = client.generate_initial_change_stream_partitions(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_generate_initial_change_stream_partitions_rest_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.GenerateInitialChangeStreamPartitionsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = bigtable.GenerateInitialChangeStreamPartitionsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        json_return_value = "[{}]".format(json_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        with mock.patch.object(response_value, "iter_content") as iter_content:
            iter_content.return_value = iter(json_return_value)
            client.generate_initial_change_stream_partitions(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v2/{table_name=projects/*/instances/*/tables/*}:generateInitialChangeStreamPartitions"
            % client.transport._host,
            args[1],
        )


def test_generate_initial_change_stream_partitions_rest_flattened_error(
    transport: str = "rest",
):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.generate_initial_change_stream_partitions(
            bigtable.GenerateInitialChangeStreamPartitionsRequest(),
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )


def test_read_change_stream_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.read_change_stream in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.read_change_stream] = (
            mock_rpc
        )

        request = {}
        client.read_change_stream(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.read_change_stream(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_read_change_stream_rest_required_fields(
    request_type=bigtable.ReadChangeStreamRequest,
):
    transport_class = transports.BigtableRestTransport

    request_init = {}
    request_init["table_name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseReadChangeStream,
        "_BaseReadChangeStream__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["tableName"] = "table_name_value"

    # verify required fields with non-default values are left alone
    assert "tableName" in jsonified_request
    assert jsonified_request["tableName"] == "table_name_value"

    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = bigtable.ReadChangeStreamResponse()
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
            return_value = bigtable.ReadChangeStreamResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)
            json_return_value = "[{}]".format(json_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            with mock.patch.object(response_value, "iter_content") as iter_content:
                iter_content.return_value = iter(json_return_value)
                response = client.read_change_stream(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_read_change_stream_rest_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.ReadChangeStreamResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = bigtable.ReadChangeStreamResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        json_return_value = "[{}]".format(json_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        with mock.patch.object(response_value, "iter_content") as iter_content:
            iter_content.return_value = iter(json_return_value)
            client.read_change_stream(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v2/{table_name=projects/*/instances/*/tables/*}:readChangeStream"
            % client.transport._host,
            args[1],
        )


def test_read_change_stream_rest_flattened_error(transport: str = "rest"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.read_change_stream(
            bigtable.ReadChangeStreamRequest(),
            table_name="table_name_value",
            app_profile_id="app_profile_id_value",
        )


def test_prepare_query_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.prepare_query in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.prepare_query] = mock_rpc

        request = {}
        client.prepare_query(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.prepare_query(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_prepare_query_rest_required_fields(request_type=bigtable.PrepareQueryRequest):
    transport_class = transports.BigtableRestTransport

    request_init = {}
    request_init["instance_name"] = ""
    request_init["query"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BasePrepareQuery,
        "_BasePrepareQuery__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceName"] = "instance_name_value"
    jsonified_request["query"] = "query_value"

    # verify required fields with non-default values are left alone
    assert "instanceName" in jsonified_request
    assert jsonified_request["instanceName"] == "instance_name_value"
    assert "query" in jsonified_request
    assert jsonified_request["query"] == "query_value"

    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = bigtable.PrepareQueryResponse()
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
            return_value = bigtable.PrepareQueryResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.prepare_query(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_prepare_query_rest_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.PrepareQueryResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"instance_name": "projects/sample1/instances/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            instance_name="instance_name_value",
            query="query_value",
            app_profile_id="app_profile_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = bigtable.PrepareQueryResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.prepare_query(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v2/{instance_name=projects/*/instances/*}:prepareQuery"
            % client.transport._host,
            args[1],
        )


def test_prepare_query_rest_flattened_error(transport: str = "rest"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.prepare_query(
            bigtable.PrepareQueryRequest(),
            instance_name="instance_name_value",
            query="query_value",
            app_profile_id="app_profile_id_value",
        )


def test_execute_query_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.execute_query in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.execute_query] = mock_rpc

        request = {}
        client.execute_query(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.execute_query(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_execute_query_rest_required_fields(request_type=bigtable.ExecuteQueryRequest):
    transport_class = transports.BigtableRestTransport

    request_init = {}
    request_init["instance_name"] = ""
    request_init["query"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseExecuteQuery,
        "_BaseExecuteQuery__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceName"] = "instance_name_value"
    jsonified_request["query"] = "query_value"

    # verify required fields with non-default values are left alone
    assert "instanceName" in jsonified_request
    assert jsonified_request["instanceName"] == "instance_name_value"
    assert "query" in jsonified_request
    assert jsonified_request["query"] == "query_value"

    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = bigtable.ExecuteQueryResponse()
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
            return_value = bigtable.ExecuteQueryResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)
            json_return_value = "[{}]".format(json_return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            with mock.patch.object(response_value, "iter_content") as iter_content:
                iter_content.return_value = iter(json_return_value)
                response = client.execute_query(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_execute_query_rest_flattened():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.ExecuteQueryResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"instance_name": "projects/sample1/instances/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            instance_name="instance_name_value",
            query="query_value",
            app_profile_id="app_profile_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = bigtable.ExecuteQueryResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        json_return_value = "[{}]".format(json_return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        with mock.patch.object(response_value, "iter_content") as iter_content:
            iter_content.return_value = iter(json_return_value)
            client.execute_query(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v2/{instance_name=projects/*/instances/*}:executeQuery"
            % client.transport._host,
            args[1],
        )


def test_execute_query_rest_flattened_error(transport: str = "rest"):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.execute_query(
            bigtable.ExecuteQueryRequest(),
            instance_name="instance_name_value",
            query="query_value",
            app_profile_id="app_profile_id_value",
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.BigtableGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.BigtableGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = BigtableClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.BigtableGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = BigtableClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = BigtableClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.BigtableGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = BigtableClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.BigtableGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = BigtableClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.BigtableGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.BigtableGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.BigtableGrpcTransport,
        transports.BigtableGrpcAsyncIOTransport,
        transports.BigtableRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = BigtableClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_read_rows_empty_call_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        call.return_value = iter([bigtable.ReadRowsResponse()])
        client.read_rows(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_sample_row_keys_empty_call_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        call.return_value = iter([bigtable.SampleRowKeysResponse()])
        client.sample_row_keys(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_mutate_row_empty_call_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        call.return_value = bigtable.MutateRowResponse()
        client.mutate_row(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.MutateRowRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_mutate_rows_empty_call_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        call.return_value = iter([bigtable.MutateRowsResponse()])
        client.mutate_rows(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.MutateRowsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_check_and_mutate_row_empty_call_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        call.return_value = bigtable.CheckAndMutateRowResponse()
        client.check_and_mutate_row(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.CheckAndMutateRowRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_ping_and_warm_empty_call_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.ping_and_warm), "__call__") as call:
        call.return_value = bigtable.PingAndWarmResponse()
        client.ping_and_warm(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.PingAndWarmRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_read_modify_write_row_empty_call_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        call.return_value = bigtable.ReadModifyWriteRowResponse()
        client.read_modify_write_row(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ReadModifyWriteRowRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_generate_initial_change_stream_partitions_empty_call_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_initial_change_stream_partitions), "__call__"
    ) as call:
        call.return_value = iter(
            [bigtable.GenerateInitialChangeStreamPartitionsResponse()]
        )
        client.generate_initial_change_stream_partitions(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.GenerateInitialChangeStreamPartitionsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_read_change_stream_empty_call_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_change_stream), "__call__"
    ) as call:
        call.return_value = iter([bigtable.ReadChangeStreamResponse()])
        client.read_change_stream(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ReadChangeStreamRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_prepare_query_empty_call_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        call.return_value = bigtable.PrepareQueryResponse()
        client.prepare_query(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.PrepareQueryRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_execute_query_empty_call_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        call.return_value = iter([bigtable.ExecuteQueryResponse()])
        client.execute_query(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ExecuteQueryRequest()
        assert args[0] == request_msg


def test_read_rows_routing_parameters_request_1_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        call.return_value = iter([bigtable.ReadRowsResponse()])
        client.read_rows(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_read_rows_routing_parameters_request_2_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        call.return_value = iter([bigtable.ReadRowsResponse()])
        client.read_rows(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_read_rows_routing_parameters_request_3_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        call.return_value = iter([bigtable.ReadRowsResponse()])
        client.read_rows(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_read_rows_routing_parameters_request_4_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        call.return_value = iter([bigtable.ReadRowsResponse()])
        client.read_rows(
            request={
                "materialized_view_name": "projects/sample1/instances/sample2/sample3"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest(
            **{"materialized_view_name": "projects/sample1/instances/sample2/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_sample_row_keys_routing_parameters_request_1_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        call.return_value = iter([bigtable.SampleRowKeysResponse()])
        client.sample_row_keys(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_sample_row_keys_routing_parameters_request_2_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        call.return_value = iter([bigtable.SampleRowKeysResponse()])
        client.sample_row_keys(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_sample_row_keys_routing_parameters_request_3_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        call.return_value = iter([bigtable.SampleRowKeysResponse()])
        client.sample_row_keys(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_sample_row_keys_routing_parameters_request_4_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        call.return_value = iter([bigtable.SampleRowKeysResponse()])
        client.sample_row_keys(
            request={
                "materialized_view_name": "projects/sample1/instances/sample2/sample3"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest(
            **{"materialized_view_name": "projects/sample1/instances/sample2/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_mutate_row_routing_parameters_request_1_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        call.return_value = bigtable.MutateRowResponse()
        client.mutate_row(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_mutate_row_routing_parameters_request_2_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        call.return_value = bigtable.MutateRowResponse()
        client.mutate_row(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_mutate_row_routing_parameters_request_3_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        call.return_value = bigtable.MutateRowResponse()
        client.mutate_row(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_mutate_rows_routing_parameters_request_1_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        call.return_value = iter([bigtable.MutateRowsResponse()])
        client.mutate_rows(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowsRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_mutate_rows_routing_parameters_request_2_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        call.return_value = iter([bigtable.MutateRowsResponse()])
        client.mutate_rows(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowsRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_mutate_rows_routing_parameters_request_3_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        call.return_value = iter([bigtable.MutateRowsResponse()])
        client.mutate_rows(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowsRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_check_and_mutate_row_routing_parameters_request_1_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        call.return_value = bigtable.CheckAndMutateRowResponse()
        client.check_and_mutate_row(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.CheckAndMutateRowRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_check_and_mutate_row_routing_parameters_request_2_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        call.return_value = bigtable.CheckAndMutateRowResponse()
        client.check_and_mutate_row(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.CheckAndMutateRowRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_check_and_mutate_row_routing_parameters_request_3_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        call.return_value = bigtable.CheckAndMutateRowResponse()
        client.check_and_mutate_row(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.CheckAndMutateRowRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_ping_and_warm_routing_parameters_request_1_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.ping_and_warm), "__call__") as call:
        call.return_value = bigtable.PingAndWarmResponse()
        client.ping_and_warm(request={"name": "projects/sample1/instances/sample2"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.PingAndWarmRequest(
            **{"name": "projects/sample1/instances/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_ping_and_warm_routing_parameters_request_2_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.ping_and_warm), "__call__") as call:
        call.return_value = bigtable.PingAndWarmResponse()
        client.ping_and_warm(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.PingAndWarmRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_read_modify_write_row_routing_parameters_request_1_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        call.return_value = bigtable.ReadModifyWriteRowResponse()
        client.read_modify_write_row(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadModifyWriteRowRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_read_modify_write_row_routing_parameters_request_2_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        call.return_value = bigtable.ReadModifyWriteRowResponse()
        client.read_modify_write_row(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadModifyWriteRowRequest(
            **{"app_profile_id": "sample1"}
        )
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_read_modify_write_row_routing_parameters_request_3_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        call.return_value = bigtable.ReadModifyWriteRowResponse()
        client.read_modify_write_row(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadModifyWriteRowRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_prepare_query_routing_parameters_request_1_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        call.return_value = bigtable.PrepareQueryResponse()
        client.prepare_query(
            request={"instance_name": "projects/sample1/instances/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.PrepareQueryRequest(
            **{"instance_name": "projects/sample1/instances/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_prepare_query_routing_parameters_request_2_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        call.return_value = bigtable.PrepareQueryResponse()
        client.prepare_query(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.PrepareQueryRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_execute_query_routing_parameters_request_1_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        call.return_value = iter([bigtable.ExecuteQueryResponse()])
        client.execute_query(
            request={"instance_name": "projects/sample1/instances/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ExecuteQueryRequest(
            **{"instance_name": "projects/sample1/instances/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_execute_query_routing_parameters_request_2_grpc():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        call.return_value = iter([bigtable.ExecuteQueryResponse()])
        client.execute_query(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ExecuteQueryRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_transport_kind_grpc_asyncio():
    transport = BigtableAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_read_rows_empty_call_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.ReadRowsResponse()]
        )
        await client.read_rows(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_sample_row_keys_empty_call_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.SampleRowKeysResponse()]
        )
        await client.sample_row_keys(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_mutate_row_empty_call_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.MutateRowResponse()
        )
        await client.mutate_row(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.MutateRowRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_mutate_rows_empty_call_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.MutateRowsResponse()]
        )
        await client.mutate_rows(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.MutateRowsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_check_and_mutate_row_empty_call_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.CheckAndMutateRowResponse(
                predicate_matched=True,
            )
        )
        await client.check_and_mutate_row(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.CheckAndMutateRowRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_ping_and_warm_empty_call_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.ping_and_warm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.PingAndWarmResponse()
        )
        await client.ping_and_warm(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.PingAndWarmRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_read_modify_write_row_empty_call_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.ReadModifyWriteRowResponse()
        )
        await client.read_modify_write_row(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ReadModifyWriteRowRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_generate_initial_change_stream_partitions_empty_call_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_initial_change_stream_partitions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.GenerateInitialChangeStreamPartitionsResponse()]
        )
        await client.generate_initial_change_stream_partitions(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.GenerateInitialChangeStreamPartitionsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_read_change_stream_empty_call_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_change_stream), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.ReadChangeStreamResponse()]
        )
        await client.read_change_stream(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ReadChangeStreamRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_prepare_query_empty_call_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.PrepareQueryResponse(
                prepared_query=b"prepared_query_blob",
            )
        )
        await client.prepare_query(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.PrepareQueryRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_execute_query_empty_call_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.ExecuteQueryResponse()]
        )
        await client.execute_query(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ExecuteQueryRequest()
        assert args[0] == request_msg


@pytest.mark.asyncio
async def test_read_rows_routing_parameters_request_1_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.ReadRowsResponse()]
        )
        await client.read_rows(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_read_rows_routing_parameters_request_2_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.ReadRowsResponse()]
        )
        await client.read_rows(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_read_rows_routing_parameters_request_3_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.ReadRowsResponse()]
        )
        await client.read_rows(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_read_rows_routing_parameters_request_4_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.ReadRowsResponse()]
        )
        await client.read_rows(
            request={
                "materialized_view_name": "projects/sample1/instances/sample2/sample3"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest(
            **{"materialized_view_name": "projects/sample1/instances/sample2/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_sample_row_keys_routing_parameters_request_1_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.SampleRowKeysResponse()]
        )
        await client.sample_row_keys(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_sample_row_keys_routing_parameters_request_2_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.SampleRowKeysResponse()]
        )
        await client.sample_row_keys(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_sample_row_keys_routing_parameters_request_3_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.SampleRowKeysResponse()]
        )
        await client.sample_row_keys(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_sample_row_keys_routing_parameters_request_4_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.SampleRowKeysResponse()]
        )
        await client.sample_row_keys(
            request={
                "materialized_view_name": "projects/sample1/instances/sample2/sample3"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest(
            **{"materialized_view_name": "projects/sample1/instances/sample2/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_mutate_row_routing_parameters_request_1_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.MutateRowResponse()
        )
        await client.mutate_row(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_mutate_row_routing_parameters_request_2_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.MutateRowResponse()
        )
        await client.mutate_row(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_mutate_row_routing_parameters_request_3_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.MutateRowResponse()
        )
        await client.mutate_row(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_mutate_rows_routing_parameters_request_1_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.MutateRowsResponse()]
        )
        await client.mutate_rows(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowsRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_mutate_rows_routing_parameters_request_2_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.MutateRowsResponse()]
        )
        await client.mutate_rows(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowsRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_mutate_rows_routing_parameters_request_3_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.MutateRowsResponse()]
        )
        await client.mutate_rows(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowsRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_check_and_mutate_row_routing_parameters_request_1_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.CheckAndMutateRowResponse(
                predicate_matched=True,
            )
        )
        await client.check_and_mutate_row(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.CheckAndMutateRowRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_check_and_mutate_row_routing_parameters_request_2_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.CheckAndMutateRowResponse(
                predicate_matched=True,
            )
        )
        await client.check_and_mutate_row(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.CheckAndMutateRowRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_check_and_mutate_row_routing_parameters_request_3_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.CheckAndMutateRowResponse(
                predicate_matched=True,
            )
        )
        await client.check_and_mutate_row(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.CheckAndMutateRowRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_ping_and_warm_routing_parameters_request_1_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.ping_and_warm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.PingAndWarmResponse()
        )
        await client.ping_and_warm(
            request={"name": "projects/sample1/instances/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.PingAndWarmRequest(
            **{"name": "projects/sample1/instances/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_ping_and_warm_routing_parameters_request_2_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.ping_and_warm), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.PingAndWarmResponse()
        )
        await client.ping_and_warm(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.PingAndWarmRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_read_modify_write_row_routing_parameters_request_1_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.ReadModifyWriteRowResponse()
        )
        await client.read_modify_write_row(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadModifyWriteRowRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_read_modify_write_row_routing_parameters_request_2_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.ReadModifyWriteRowResponse()
        )
        await client.read_modify_write_row(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadModifyWriteRowRequest(
            **{"app_profile_id": "sample1"}
        )
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_read_modify_write_row_routing_parameters_request_3_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.ReadModifyWriteRowResponse()
        )
        await client.read_modify_write_row(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadModifyWriteRowRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_prepare_query_routing_parameters_request_1_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.PrepareQueryResponse(
                prepared_query=b"prepared_query_blob",
            )
        )
        await client.prepare_query(
            request={"instance_name": "projects/sample1/instances/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.PrepareQueryRequest(
            **{"instance_name": "projects/sample1/instances/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_prepare_query_routing_parameters_request_2_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            bigtable.PrepareQueryResponse(
                prepared_query=b"prepared_query_blob",
            )
        )
        await client.prepare_query(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.PrepareQueryRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_execute_query_routing_parameters_request_1_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.ExecuteQueryResponse()]
        )
        await client.execute_query(
            request={"instance_name": "projects/sample1/instances/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ExecuteQueryRequest(
            **{"instance_name": "projects/sample1/instances/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


@pytest.mark.asyncio
async def test_execute_query_routing_parameters_request_2_grpc_asyncio():
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = mock.Mock(aio.UnaryStreamCall, autospec=True)
        call.return_value.read = mock.AsyncMock(
            side_effect=[bigtable.ExecuteQueryResponse()]
        )
        await client.execute_query(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ExecuteQueryRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_transport_kind_rest():
    transport = BigtableClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_read_rows_rest_bad_request(request_type=bigtable.ReadRowsRequest):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
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
        client.read_rows(request)


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.ReadRowsRequest,
        dict,
    ],
)
def test_read_rows_rest_call_success(request_type):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.ReadRowsResponse(
            last_scanned_row_key=b"last_scanned_row_key_blob",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = bigtable.ReadRowsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        json_return_value = "[{}]".format(json_return_value)
        response_value.iter_content = mock.Mock(return_value=iter(json_return_value))
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.read_rows(request)

    assert isinstance(response, Iterable)
    response = next(response)

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.ReadRowsResponse)
    assert response.last_scanned_row_key == b"last_scanned_row_key_blob"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_read_rows_rest_interceptors(null_interceptor):
    transport = transports.BigtableRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.BigtableRestInterceptor(),
    )
    client = BigtableClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(transports.BigtableRestInterceptor, "post_read_rows") as post,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_read_rows_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(transports.BigtableRestInterceptor, "pre_read_rows") as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = bigtable.ReadRowsRequest.pb(bigtable.ReadRowsRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = bigtable.ReadRowsResponse.to_json(bigtable.ReadRowsResponse())
        req.return_value.iter_content = mock.Mock(return_value=iter(return_value))

        request = bigtable.ReadRowsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = bigtable.ReadRowsResponse()
        post_with_metadata.return_value = bigtable.ReadRowsResponse(), metadata

        client.read_rows(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_sample_row_keys_rest_bad_request(request_type=bigtable.SampleRowKeysRequest):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
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
        client.sample_row_keys(request)


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.SampleRowKeysRequest,
        dict,
    ],
)
def test_sample_row_keys_rest_call_success(request_type):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.SampleRowKeysResponse(
            row_key=b"row_key_blob",
            offset_bytes=1293,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = bigtable.SampleRowKeysResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        json_return_value = "[{}]".format(json_return_value)
        response_value.iter_content = mock.Mock(return_value=iter(json_return_value))
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.sample_row_keys(request)

    assert isinstance(response, Iterable)
    response = next(response)

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.SampleRowKeysResponse)
    assert response.row_key == b"row_key_blob"
    assert response.offset_bytes == 1293


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_sample_row_keys_rest_interceptors(null_interceptor):
    transport = transports.BigtableRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.BigtableRestInterceptor(),
    )
    client = BigtableClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_sample_row_keys"
        ) as post,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_sample_row_keys_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.BigtableRestInterceptor, "pre_sample_row_keys"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = bigtable.SampleRowKeysRequest.pb(bigtable.SampleRowKeysRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = bigtable.SampleRowKeysResponse.to_json(
            bigtable.SampleRowKeysResponse()
        )
        req.return_value.iter_content = mock.Mock(return_value=iter(return_value))

        request = bigtable.SampleRowKeysRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = bigtable.SampleRowKeysResponse()
        post_with_metadata.return_value = bigtable.SampleRowKeysResponse(), metadata

        client.sample_row_keys(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_mutate_row_rest_bad_request(request_type=bigtable.MutateRowRequest):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
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
        client.mutate_row(request)


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.MutateRowRequest,
        dict,
    ],
)
def test_mutate_row_rest_call_success(request_type):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.MutateRowResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = bigtable.MutateRowResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.mutate_row(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.MutateRowResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_mutate_row_rest_interceptors(null_interceptor):
    transport = transports.BigtableRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.BigtableRestInterceptor(),
    )
    client = BigtableClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_mutate_row"
        ) as post,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_mutate_row_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(transports.BigtableRestInterceptor, "pre_mutate_row") as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = bigtable.MutateRowRequest.pb(bigtable.MutateRowRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = bigtable.MutateRowResponse.to_json(bigtable.MutateRowResponse())
        req.return_value.content = return_value

        request = bigtable.MutateRowRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = bigtable.MutateRowResponse()
        post_with_metadata.return_value = bigtable.MutateRowResponse(), metadata

        client.mutate_row(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_mutate_rows_rest_bad_request(request_type=bigtable.MutateRowsRequest):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
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
        client.mutate_rows(request)


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.MutateRowsRequest,
        dict,
    ],
)
def test_mutate_rows_rest_call_success(request_type):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.MutateRowsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = bigtable.MutateRowsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        json_return_value = "[{}]".format(json_return_value)
        response_value.iter_content = mock.Mock(return_value=iter(json_return_value))
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.mutate_rows(request)

    assert isinstance(response, Iterable)
    response = next(response)

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.MutateRowsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_mutate_rows_rest_interceptors(null_interceptor):
    transport = transports.BigtableRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.BigtableRestInterceptor(),
    )
    client = BigtableClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_mutate_rows"
        ) as post,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_mutate_rows_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(transports.BigtableRestInterceptor, "pre_mutate_rows") as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = bigtable.MutateRowsRequest.pb(bigtable.MutateRowsRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = bigtable.MutateRowsResponse.to_json(
            bigtable.MutateRowsResponse()
        )
        req.return_value.iter_content = mock.Mock(return_value=iter(return_value))

        request = bigtable.MutateRowsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = bigtable.MutateRowsResponse()
        post_with_metadata.return_value = bigtable.MutateRowsResponse(), metadata

        client.mutate_rows(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_check_and_mutate_row_rest_bad_request(
    request_type=bigtable.CheckAndMutateRowRequest,
):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
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
        client.check_and_mutate_row(request)


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.CheckAndMutateRowRequest,
        dict,
    ],
)
def test_check_and_mutate_row_rest_call_success(request_type):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.CheckAndMutateRowResponse(
            predicate_matched=True,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = bigtable.CheckAndMutateRowResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.check_and_mutate_row(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.CheckAndMutateRowResponse)
    assert response.predicate_matched is True


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_check_and_mutate_row_rest_interceptors(null_interceptor):
    transport = transports.BigtableRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.BigtableRestInterceptor(),
    )
    client = BigtableClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_check_and_mutate_row"
        ) as post,
        mock.patch.object(
            transports.BigtableRestInterceptor,
            "post_check_and_mutate_row_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.BigtableRestInterceptor, "pre_check_and_mutate_row"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = bigtable.CheckAndMutateRowRequest.pb(
            bigtable.CheckAndMutateRowRequest()
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
        return_value = bigtable.CheckAndMutateRowResponse.to_json(
            bigtable.CheckAndMutateRowResponse()
        )
        req.return_value.content = return_value

        request = bigtable.CheckAndMutateRowRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = bigtable.CheckAndMutateRowResponse()
        post_with_metadata.return_value = bigtable.CheckAndMutateRowResponse(), metadata

        client.check_and_mutate_row(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_ping_and_warm_rest_bad_request(request_type=bigtable.PingAndWarmRequest):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/instances/sample2"}
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
        client.ping_and_warm(request)


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.PingAndWarmRequest,
        dict,
    ],
)
def test_ping_and_warm_rest_call_success(request_type):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/instances/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.PingAndWarmResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = bigtable.PingAndWarmResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.ping_and_warm(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.PingAndWarmResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_ping_and_warm_rest_interceptors(null_interceptor):
    transport = transports.BigtableRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.BigtableRestInterceptor(),
    )
    client = BigtableClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_ping_and_warm"
        ) as post,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_ping_and_warm_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.BigtableRestInterceptor, "pre_ping_and_warm"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = bigtable.PingAndWarmRequest.pb(bigtable.PingAndWarmRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = bigtable.PingAndWarmResponse.to_json(
            bigtable.PingAndWarmResponse()
        )
        req.return_value.content = return_value

        request = bigtable.PingAndWarmRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = bigtable.PingAndWarmResponse()
        post_with_metadata.return_value = bigtable.PingAndWarmResponse(), metadata

        client.ping_and_warm(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_read_modify_write_row_rest_bad_request(
    request_type=bigtable.ReadModifyWriteRowRequest,
):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
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
        client.read_modify_write_row(request)


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.ReadModifyWriteRowRequest,
        dict,
    ],
)
def test_read_modify_write_row_rest_call_success(request_type):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.ReadModifyWriteRowResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = bigtable.ReadModifyWriteRowResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.read_modify_write_row(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.ReadModifyWriteRowResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_read_modify_write_row_rest_interceptors(null_interceptor):
    transport = transports.BigtableRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.BigtableRestInterceptor(),
    )
    client = BigtableClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_read_modify_write_row"
        ) as post,
        mock.patch.object(
            transports.BigtableRestInterceptor,
            "post_read_modify_write_row_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.BigtableRestInterceptor, "pre_read_modify_write_row"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = bigtable.ReadModifyWriteRowRequest.pb(
            bigtable.ReadModifyWriteRowRequest()
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
        return_value = bigtable.ReadModifyWriteRowResponse.to_json(
            bigtable.ReadModifyWriteRowResponse()
        )
        req.return_value.content = return_value

        request = bigtable.ReadModifyWriteRowRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = bigtable.ReadModifyWriteRowResponse()
        post_with_metadata.return_value = (
            bigtable.ReadModifyWriteRowResponse(),
            metadata,
        )

        client.read_modify_write_row(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_generate_initial_change_stream_partitions_rest_bad_request(
    request_type=bigtable.GenerateInitialChangeStreamPartitionsRequest,
):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
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
        client.generate_initial_change_stream_partitions(request)


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.GenerateInitialChangeStreamPartitionsRequest,
        dict,
    ],
)
def test_generate_initial_change_stream_partitions_rest_call_success(request_type):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.GenerateInitialChangeStreamPartitionsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = bigtable.GenerateInitialChangeStreamPartitionsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        json_return_value = "[{}]".format(json_return_value)
        response_value.iter_content = mock.Mock(return_value=iter(json_return_value))
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.generate_initial_change_stream_partitions(request)

    assert isinstance(response, Iterable)
    response = next(response)

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.GenerateInitialChangeStreamPartitionsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_generate_initial_change_stream_partitions_rest_interceptors(null_interceptor):
    transport = transports.BigtableRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.BigtableRestInterceptor(),
    )
    client = BigtableClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.BigtableRestInterceptor,
            "post_generate_initial_change_stream_partitions",
        ) as post,
        mock.patch.object(
            transports.BigtableRestInterceptor,
            "post_generate_initial_change_stream_partitions_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.BigtableRestInterceptor,
            "pre_generate_initial_change_stream_partitions",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = bigtable.GenerateInitialChangeStreamPartitionsRequest.pb(
            bigtable.GenerateInitialChangeStreamPartitionsRequest()
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
        return_value = bigtable.GenerateInitialChangeStreamPartitionsResponse.to_json(
            bigtable.GenerateInitialChangeStreamPartitionsResponse()
        )
        req.return_value.iter_content = mock.Mock(return_value=iter(return_value))

        request = bigtable.GenerateInitialChangeStreamPartitionsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = bigtable.GenerateInitialChangeStreamPartitionsResponse()
        post_with_metadata.return_value = (
            bigtable.GenerateInitialChangeStreamPartitionsResponse(),
            metadata,
        )

        client.generate_initial_change_stream_partitions(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_read_change_stream_rest_bad_request(
    request_type=bigtable.ReadChangeStreamRequest,
):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
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
        client.read_change_stream(request)


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.ReadChangeStreamRequest,
        dict,
    ],
)
def test_read_change_stream_rest_call_success(request_type):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"table_name": "projects/sample1/instances/sample2/tables/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.ReadChangeStreamResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = bigtable.ReadChangeStreamResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        json_return_value = "[{}]".format(json_return_value)
        response_value.iter_content = mock.Mock(return_value=iter(json_return_value))
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.read_change_stream(request)

    assert isinstance(response, Iterable)
    response = next(response)

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.ReadChangeStreamResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_read_change_stream_rest_interceptors(null_interceptor):
    transport = transports.BigtableRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.BigtableRestInterceptor(),
    )
    client = BigtableClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_read_change_stream"
        ) as post,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_read_change_stream_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.BigtableRestInterceptor, "pre_read_change_stream"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = bigtable.ReadChangeStreamRequest.pb(
            bigtable.ReadChangeStreamRequest()
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
        return_value = bigtable.ReadChangeStreamResponse.to_json(
            bigtable.ReadChangeStreamResponse()
        )
        req.return_value.iter_content = mock.Mock(return_value=iter(return_value))

        request = bigtable.ReadChangeStreamRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = bigtable.ReadChangeStreamResponse()
        post_with_metadata.return_value = bigtable.ReadChangeStreamResponse(), metadata

        client.read_change_stream(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_prepare_query_rest_bad_request(request_type=bigtable.PrepareQueryRequest):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"instance_name": "projects/sample1/instances/sample2"}
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
        client.prepare_query(request)


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.PrepareQueryRequest,
        dict,
    ],
)
def test_prepare_query_rest_call_success(request_type):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"instance_name": "projects/sample1/instances/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.PrepareQueryResponse(
            prepared_query=b"prepared_query_blob",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = bigtable.PrepareQueryResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.prepare_query(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.PrepareQueryResponse)
    assert response.prepared_query == b"prepared_query_blob"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_prepare_query_rest_interceptors(null_interceptor):
    transport = transports.BigtableRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.BigtableRestInterceptor(),
    )
    client = BigtableClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_prepare_query"
        ) as post,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_prepare_query_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.BigtableRestInterceptor, "pre_prepare_query"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = bigtable.PrepareQueryRequest.pb(bigtable.PrepareQueryRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = bigtable.PrepareQueryResponse.to_json(
            bigtable.PrepareQueryResponse()
        )
        req.return_value.content = return_value

        request = bigtable.PrepareQueryRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = bigtable.PrepareQueryResponse()
        post_with_metadata.return_value = bigtable.PrepareQueryResponse(), metadata

        client.prepare_query(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_execute_query_rest_bad_request(request_type=bigtable.ExecuteQueryRequest):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"instance_name": "projects/sample1/instances/sample2"}
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
        client.execute_query(request)


@pytest.mark.parametrize(
    "request_type",
    [
        bigtable.ExecuteQueryRequest,
        dict,
    ],
)
def test_execute_query_rest_call_success(request_type):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"instance_name": "projects/sample1/instances/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = bigtable.ExecuteQueryResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = bigtable.ExecuteQueryResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        json_return_value = "[{}]".format(json_return_value)
        response_value.iter_content = mock.Mock(return_value=iter(json_return_value))
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.execute_query(request)

    assert isinstance(response, Iterable)
    response = next(response)

    # Establish that the response is the type that we expect.
    assert isinstance(response, bigtable.ExecuteQueryResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_execute_query_rest_interceptors(null_interceptor):
    transport = transports.BigtableRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None if null_interceptor else transports.BigtableRestInterceptor(),
    )
    client = BigtableClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_execute_query"
        ) as post,
        mock.patch.object(
            transports.BigtableRestInterceptor, "post_execute_query_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.BigtableRestInterceptor, "pre_execute_query"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = bigtable.ExecuteQueryRequest.pb(bigtable.ExecuteQueryRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = bigtable.ExecuteQueryResponse.to_json(
            bigtable.ExecuteQueryResponse()
        )
        req.return_value.iter_content = mock.Mock(return_value=iter(return_value))

        request = bigtable.ExecuteQueryRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = bigtable.ExecuteQueryResponse()
        post_with_metadata.return_value = bigtable.ExecuteQueryResponse(), metadata

        client.execute_query(
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
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_read_rows_empty_call_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        client.read_rows(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_sample_row_keys_empty_call_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        client.sample_row_keys(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_mutate_row_empty_call_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        client.mutate_row(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.MutateRowRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_mutate_rows_empty_call_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        client.mutate_rows(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.MutateRowsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_check_and_mutate_row_empty_call_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        client.check_and_mutate_row(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.CheckAndMutateRowRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_ping_and_warm_empty_call_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.ping_and_warm), "__call__") as call:
        client.ping_and_warm(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.PingAndWarmRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_read_modify_write_row_empty_call_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        client.read_modify_write_row(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ReadModifyWriteRowRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_generate_initial_change_stream_partitions_empty_call_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_initial_change_stream_partitions), "__call__"
    ) as call:
        client.generate_initial_change_stream_partitions(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.GenerateInitialChangeStreamPartitionsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_read_change_stream_empty_call_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_change_stream), "__call__"
    ) as call:
        client.read_change_stream(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ReadChangeStreamRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_prepare_query_empty_call_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        client.prepare_query(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.PrepareQueryRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_execute_query_empty_call_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        client.execute_query(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = bigtable.ExecuteQueryRequest()
        assert args[0] == request_msg


def test_read_rows_routing_parameters_request_1_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        client.read_rows(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_read_rows_routing_parameters_request_2_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        client.read_rows(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_read_rows_routing_parameters_request_3_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        client.read_rows(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_read_rows_routing_parameters_request_4_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.read_rows), "__call__") as call:
        client.read_rows(
            request={
                "materialized_view_name": "projects/sample1/instances/sample2/sample3"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadRowsRequest(
            **{"materialized_view_name": "projects/sample1/instances/sample2/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_sample_row_keys_routing_parameters_request_1_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        client.sample_row_keys(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_sample_row_keys_routing_parameters_request_2_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        client.sample_row_keys(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_sample_row_keys_routing_parameters_request_3_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        client.sample_row_keys(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_sample_row_keys_routing_parameters_request_4_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.sample_row_keys), "__call__") as call:
        client.sample_row_keys(
            request={
                "materialized_view_name": "projects/sample1/instances/sample2/sample3"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.SampleRowKeysRequest(
            **{"materialized_view_name": "projects/sample1/instances/sample2/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_mutate_row_routing_parameters_request_1_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        client.mutate_row(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_mutate_row_routing_parameters_request_2_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        client.mutate_row(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_mutate_row_routing_parameters_request_3_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_row), "__call__") as call:
        client.mutate_row(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_mutate_rows_routing_parameters_request_1_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        client.mutate_rows(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowsRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_mutate_rows_routing_parameters_request_2_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        client.mutate_rows(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowsRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_mutate_rows_routing_parameters_request_3_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.mutate_rows), "__call__") as call:
        client.mutate_rows(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.MutateRowsRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_check_and_mutate_row_routing_parameters_request_1_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        client.check_and_mutate_row(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.CheckAndMutateRowRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_check_and_mutate_row_routing_parameters_request_2_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        client.check_and_mutate_row(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.CheckAndMutateRowRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_check_and_mutate_row_routing_parameters_request_3_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.check_and_mutate_row), "__call__"
    ) as call:
        client.check_and_mutate_row(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.CheckAndMutateRowRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_ping_and_warm_routing_parameters_request_1_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.ping_and_warm), "__call__") as call:
        client.ping_and_warm(request={"name": "projects/sample1/instances/sample2"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.PingAndWarmRequest(
            **{"name": "projects/sample1/instances/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_ping_and_warm_routing_parameters_request_2_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.ping_and_warm), "__call__") as call:
        client.ping_and_warm(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.PingAndWarmRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_read_modify_write_row_routing_parameters_request_1_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        client.read_modify_write_row(
            request={"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadModifyWriteRowRequest(
            **{"table_name": "projects/sample1/instances/sample2/tables/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_read_modify_write_row_routing_parameters_request_2_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        client.read_modify_write_row(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadModifyWriteRowRequest(
            **{"app_profile_id": "sample1"}
        )
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_read_modify_write_row_routing_parameters_request_3_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.read_modify_write_row), "__call__"
    ) as call:
        client.read_modify_write_row(
            request={
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ReadModifyWriteRowRequest(
            **{
                "authorized_view_name": "projects/sample1/instances/sample2/tables/sample3/sample4"
            }
        )
        assert args[0] == request_msg

        expected_headers = {
            "table_name": "projects/sample1/instances/sample2/tables/sample3",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_prepare_query_routing_parameters_request_1_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        client.prepare_query(
            request={"instance_name": "projects/sample1/instances/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.PrepareQueryRequest(
            **{"instance_name": "projects/sample1/instances/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_prepare_query_routing_parameters_request_2_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.prepare_query), "__call__") as call:
        client.prepare_query(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.PrepareQueryRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_execute_query_routing_parameters_request_1_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        client.execute_query(
            request={"instance_name": "projects/sample1/instances/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ExecuteQueryRequest(
            **{"instance_name": "projects/sample1/instances/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {
            "name": "projects/sample1/instances/sample2",
            "app_profile_id": "",
        }
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_execute_query_routing_parameters_request_2_rest():
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.execute_query), "__call__") as call:
        client.execute_query(request={"app_profile_id": "sample1"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = bigtable.ExecuteQueryRequest(**{"app_profile_id": "sample1"})
        assert args[0] == request_msg

        expected_headers = {"app_profile_id": "sample1"}
        # assert the expected headers are present, in any order
        routing_string = next(
            iter([m[1] for m in kw["metadata"] if m[0] == "x-goog-request-params"])
        )
        assert all([f"{k}={v}" in routing_string for k, v in expected_headers.items()])


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.BigtableGrpcTransport,
    )


def test_bigtable_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.BigtableTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_bigtable_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.bigtable_v2.services.bigtable.transports.BigtableTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.BigtableTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "read_rows",
        "sample_row_keys",
        "mutate_row",
        "mutate_rows",
        "check_and_mutate_row",
        "ping_and_warm",
        "read_modify_write_row",
        "generate_initial_change_stream_partitions",
        "read_change_stream",
        "prepare_query",
        "execute_query",
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


def test_bigtable_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.cloud.bigtable_v2.services.bigtable.transports.BigtableTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.BigtableTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/bigtable.data",
                "https://www.googleapis.com/auth/bigtable.data.readonly",
                "https://www.googleapis.com/auth/cloud-bigtable.data",
                "https://www.googleapis.com/auth/cloud-bigtable.data.readonly",
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/cloud-platform.read-only",
            ),
            quota_project_id="octopus",
        )


def test_bigtable_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.cloud.bigtable_v2.services.bigtable.transports.BigtableTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.BigtableTransport()
        adc.assert_called_once()


def test_bigtable_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        BigtableClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/bigtable.data",
                "https://www.googleapis.com/auth/bigtable.data.readonly",
                "https://www.googleapis.com/auth/cloud-bigtable.data",
                "https://www.googleapis.com/auth/cloud-bigtable.data.readonly",
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/cloud-platform.read-only",
            ),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.BigtableGrpcTransport,
        transports.BigtableGrpcAsyncIOTransport,
    ],
)
def test_bigtable_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(
                "https://www.googleapis.com/auth/bigtable.data",
                "https://www.googleapis.com/auth/bigtable.data.readonly",
                "https://www.googleapis.com/auth/cloud-bigtable.data",
                "https://www.googleapis.com/auth/cloud-bigtable.data.readonly",
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/cloud-platform.read-only",
            ),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.BigtableGrpcTransport,
        transports.BigtableGrpcAsyncIOTransport,
        transports.BigtableRestTransport,
    ],
)
def test_bigtable_transport_auth_gdch_credentials(transport_class):
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
        (transports.BigtableGrpcTransport, grpc_helpers),
        (transports.BigtableGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_bigtable_transport_create_channel(transport_class, grpc_helpers):
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
            "bigtable.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
                "https://www.googleapis.com/auth/bigtable.data",
                "https://www.googleapis.com/auth/bigtable.data.readonly",
                "https://www.googleapis.com/auth/cloud-bigtable.data",
                "https://www.googleapis.com/auth/cloud-bigtable.data.readonly",
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/cloud-platform.read-only",
            ),
            scopes=["1", "2"],
            default_host="bigtable.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [transports.BigtableGrpcTransport, transports.BigtableGrpcAsyncIOTransport],
)
def test_bigtable_grpc_transport_client_cert_source_for_mtls(transport_class):
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


def test_bigtable_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.BigtableRestTransport(
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
def test_bigtable_host_no_port(transport_name):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="bigtable.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "bigtable.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://bigtable.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_bigtable_host_with_port(transport_name):
    client = BigtableClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="bigtable.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "bigtable.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://bigtable.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_bigtable_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = BigtableClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = BigtableClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.read_rows._session
    session2 = client2.transport.read_rows._session
    assert session1 != session2
    session1 = client1.transport.sample_row_keys._session
    session2 = client2.transport.sample_row_keys._session
    assert session1 != session2
    session1 = client1.transport.mutate_row._session
    session2 = client2.transport.mutate_row._session
    assert session1 != session2
    session1 = client1.transport.mutate_rows._session
    session2 = client2.transport.mutate_rows._session
    assert session1 != session2
    session1 = client1.transport.check_and_mutate_row._session
    session2 = client2.transport.check_and_mutate_row._session
    assert session1 != session2
    session1 = client1.transport.ping_and_warm._session
    session2 = client2.transport.ping_and_warm._session
    assert session1 != session2
    session1 = client1.transport.read_modify_write_row._session
    session2 = client2.transport.read_modify_write_row._session
    assert session1 != session2
    session1 = client1.transport.generate_initial_change_stream_partitions._session
    session2 = client2.transport.generate_initial_change_stream_partitions._session
    assert session1 != session2
    session1 = client1.transport.read_change_stream._session
    session2 = client2.transport.read_change_stream._session
    assert session1 != session2
    session1 = client1.transport.prepare_query._session
    session2 = client2.transport.prepare_query._session
    assert session1 != session2
    session1 = client1.transport.execute_query._session
    session2 = client2.transport.execute_query._session
    assert session1 != session2


def test_bigtable_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.BigtableGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_bigtable_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.BigtableGrpcAsyncIOTransport(
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
    [transports.BigtableGrpcTransport, transports.BigtableGrpcAsyncIOTransport],
)
def test_bigtable_transport_channel_mtls_with_client_cert_source(transport_class):
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
    [transports.BigtableGrpcTransport, transports.BigtableGrpcAsyncIOTransport],
)
def test_bigtable_transport_channel_mtls_with_adc(transport_class):
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


def test_authorized_view_path():
    project = "squid"
    instance = "clam"
    table = "whelk"
    authorized_view = "octopus"
    expected = "projects/{project}/instances/{instance}/tables/{table}/authorizedViews/{authorized_view}".format(
        project=project,
        instance=instance,
        table=table,
        authorized_view=authorized_view,
    )
    actual = BigtableClient.authorized_view_path(
        project, instance, table, authorized_view
    )
    assert expected == actual


def test_parse_authorized_view_path():
    expected = {
        "project": "oyster",
        "instance": "nudibranch",
        "table": "cuttlefish",
        "authorized_view": "mussel",
    }
    path = BigtableClient.authorized_view_path(**expected)

    # Check that the path construction is reversible.
    actual = BigtableClient.parse_authorized_view_path(path)
    assert expected == actual


def test_instance_path():
    project = "winkle"
    instance = "nautilus"
    expected = "projects/{project}/instances/{instance}".format(
        project=project,
        instance=instance,
    )
    actual = BigtableClient.instance_path(project, instance)
    assert expected == actual


def test_parse_instance_path():
    expected = {
        "project": "scallop",
        "instance": "abalone",
    }
    path = BigtableClient.instance_path(**expected)

    # Check that the path construction is reversible.
    actual = BigtableClient.parse_instance_path(path)
    assert expected == actual


def test_materialized_view_path():
    project = "squid"
    instance = "clam"
    materialized_view = "whelk"
    expected = "projects/{project}/instances/{instance}/materializedViews/{materialized_view}".format(
        project=project,
        instance=instance,
        materialized_view=materialized_view,
    )
    actual = BigtableClient.materialized_view_path(project, instance, materialized_view)
    assert expected == actual


def test_parse_materialized_view_path():
    expected = {
        "project": "octopus",
        "instance": "oyster",
        "materialized_view": "nudibranch",
    }
    path = BigtableClient.materialized_view_path(**expected)

    # Check that the path construction is reversible.
    actual = BigtableClient.parse_materialized_view_path(path)
    assert expected == actual


def test_table_path():
    project = "cuttlefish"
    instance = "mussel"
    table = "winkle"
    expected = "projects/{project}/instances/{instance}/tables/{table}".format(
        project=project,
        instance=instance,
        table=table,
    )
    actual = BigtableClient.table_path(project, instance, table)
    assert expected == actual


def test_parse_table_path():
    expected = {
        "project": "nautilus",
        "instance": "scallop",
        "table": "abalone",
    }
    path = BigtableClient.table_path(**expected)

    # Check that the path construction is reversible.
    actual = BigtableClient.parse_table_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = BigtableClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = BigtableClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = BigtableClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = BigtableClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = BigtableClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = BigtableClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = BigtableClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = BigtableClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = BigtableClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = BigtableClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = BigtableClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = BigtableClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = BigtableClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = BigtableClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = BigtableClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.BigtableTransport, "_prep_wrapped_messages"
    ) as prep:
        client = BigtableClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.BigtableTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = BigtableClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_grpc():
    client = BigtableClient(
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
    client = BigtableAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = BigtableClient(
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
        client = BigtableClient(
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
        (BigtableClient, transports.BigtableGrpcTransport),
        (BigtableAsyncClient, transports.BigtableGrpcAsyncIOTransport),
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
