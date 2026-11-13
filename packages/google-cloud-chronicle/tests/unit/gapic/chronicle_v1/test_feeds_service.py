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

import google.api.httpbody_pb2 as httpbody_pb2  # type: ignore
import google.auth
import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
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
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account

from google.cloud.chronicle_v1.services.feeds_service import (
    FeedsServiceAsyncClient,
    FeedsServiceClient,
    pagers,
    transports,
)
from google.cloud.chronicle_v1.types import feed
from google.cloud.chronicle_v1.types import feed as gcc_feed

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

    assert FeedsServiceClient._get_client_cert_source(None, False) is None
    assert (
        FeedsServiceClient._get_client_cert_source(mock_provided_cert_source, False)
        is None
    )
    assert (
        FeedsServiceClient._get_client_cert_source(mock_provided_cert_source, True)
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
                FeedsServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                FeedsServiceClient._get_client_cert_source(
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
    client = FeedsServiceClient(credentials=cred)
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
    client = FeedsServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (FeedsServiceClient, "grpc"),
        (FeedsServiceAsyncClient, "grpc_asyncio"),
        (FeedsServiceClient, "rest"),
    ],
)
def test_feeds_service_client_from_service_account_info(client_class, transport_name):
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
            "chronicle.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://chronicle.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.FeedsServiceGrpcTransport, "grpc"),
        (transports.FeedsServiceGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.FeedsServiceRestTransport, "rest"),
    ],
)
def test_feeds_service_client_service_account_always_use_jwt(
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
        (FeedsServiceClient, "grpc"),
        (FeedsServiceAsyncClient, "grpc_asyncio"),
        (FeedsServiceClient, "rest"),
    ],
)
def test_feeds_service_client_from_service_account_file(client_class, transport_name):
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
            "chronicle.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://chronicle.googleapis.com"
        )


def test_feeds_service_client_get_transport_class():
    transport = FeedsServiceClient.get_transport_class()
    available_transports = [
        transports.FeedsServiceGrpcTransport,
        transports.FeedsServiceRestTransport,
    ]
    assert transport in available_transports

    transport = FeedsServiceClient.get_transport_class("grpc")
    assert transport == transports.FeedsServiceGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (FeedsServiceClient, transports.FeedsServiceGrpcTransport, "grpc"),
        (
            FeedsServiceAsyncClient,
            transports.FeedsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (FeedsServiceClient, transports.FeedsServiceRestTransport, "rest"),
    ],
)
@mock.patch.object(
    FeedsServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(FeedsServiceClient),
)
@mock.patch.object(
    FeedsServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(FeedsServiceAsyncClient),
)
def test_feeds_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(FeedsServiceClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(FeedsServiceClient, "get_transport_class") as gtc:
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
        (FeedsServiceClient, transports.FeedsServiceGrpcTransport, "grpc", "true"),
        (
            FeedsServiceAsyncClient,
            transports.FeedsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (FeedsServiceClient, transports.FeedsServiceGrpcTransport, "grpc", "false"),
        (
            FeedsServiceAsyncClient,
            transports.FeedsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (FeedsServiceClient, transports.FeedsServiceRestTransport, "rest", "true"),
        (FeedsServiceClient, transports.FeedsServiceRestTransport, "rest", "false"),
    ],
)
@mock.patch.object(
    FeedsServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(FeedsServiceClient),
)
@mock.patch.object(
    FeedsServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(FeedsServiceAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_feeds_service_client_mtls_env_auto(
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


@pytest.mark.parametrize("client_class", [FeedsServiceClient, FeedsServiceAsyncClient])
@mock.patch.object(
    FeedsServiceClient, "DEFAULT_ENDPOINT", modify_default_endpoint(FeedsServiceClient)
)
@mock.patch.object(
    FeedsServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(FeedsServiceAsyncClient),
)
def test_feeds_service_client_get_mtls_endpoint_and_cert_source(client_class):
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


@pytest.mark.parametrize("client_class", [FeedsServiceClient, FeedsServiceAsyncClient])
@mock.patch.object(
    FeedsServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(FeedsServiceClient),
)
@mock.patch.object(
    FeedsServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(FeedsServiceAsyncClient),
)
def test_feeds_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = FeedsServiceClient._DEFAULT_UNIVERSE
    default_endpoint = FeedsServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = FeedsServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
        (FeedsServiceClient, transports.FeedsServiceGrpcTransport, "grpc"),
        (
            FeedsServiceAsyncClient,
            transports.FeedsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (FeedsServiceClient, transports.FeedsServiceRestTransport, "rest"),
    ],
)
def test_feeds_service_client_client_options_scopes(
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
            FeedsServiceClient,
            transports.FeedsServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            FeedsServiceAsyncClient,
            transports.FeedsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (FeedsServiceClient, transports.FeedsServiceRestTransport, "rest", None),
    ],
)
def test_feeds_service_client_client_options_credentials_file(
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


def test_feeds_service_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.chronicle_v1.services.feeds_service.transports.FeedsServiceGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = FeedsServiceClient(client_options={"api_endpoint": "squid.clam.whelk"})
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
            FeedsServiceClient,
            transports.FeedsServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            FeedsServiceAsyncClient,
            transports.FeedsServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_feeds_service_client_create_channel_credentials_file(
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
            "chronicle.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
                "https://www.googleapis.com/auth/chronicle",
                "https://www.googleapis.com/auth/chronicle.readonly",
                "https://www.googleapis.com/auth/cloud-platform",
            ),
            scopes=None,
            default_host="chronicle.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        feed.FetchServiceAccountForCustomerRequest(),
        {},
    ],
)
def test_fetch_service_account_for_customer(request_type, transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_service_account_for_customer), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.FeedServiceAccount(
            name="name_value",
            subject_id="subject_id_value",
        )
        response = client.fetch_service_account_for_customer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = feed.FetchServiceAccountForCustomerRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.FeedServiceAccount)
    assert response.name == "name_value"
    assert response.subject_id == "subject_id_value"


def test_fetch_service_account_for_customer_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = feed.FetchServiceAccountForCustomerRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_service_account_for_customer), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.fetch_service_account_for_customer(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.FetchServiceAccountForCustomerRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_fetch_service_account_for_customer_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.fetch_service_account_for_customer
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.fetch_service_account_for_customer
        ] = mock_rpc
        request = {}
        client.fetch_service_account_for_customer(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fetch_service_account_for_customer(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_fetch_service_account_for_customer_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FeedsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.fetch_service_account_for_customer
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.fetch_service_account_for_customer
        ] = mock_rpc

        request = {}
        await client.fetch_service_account_for_customer(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.fetch_service_account_for_customer(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        feed.FetchServiceAccountForCustomerRequest(),
        {},
    ],
)
async def test_fetch_service_account_for_customer_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_service_account_for_customer), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.FeedServiceAccount(
                name="name_value",
                subject_id="subject_id_value",
            )
        )
        response = await client.fetch_service_account_for_customer(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = feed.FetchServiceAccountForCustomerRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.FeedServiceAccount)
    assert response.name == "name_value"
    assert response.subject_id == "subject_id_value"


def test_fetch_service_account_for_customer_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.FetchServiceAccountForCustomerRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_service_account_for_customer), "__call__"
    ) as call:
        call.return_value = feed.FeedServiceAccount()
        client.fetch_service_account_for_customer(request)

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
async def test_fetch_service_account_for_customer_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.FetchServiceAccountForCustomerRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_service_account_for_customer), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.FeedServiceAccount()
        )
        await client.fetch_service_account_for_customer(request)

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


def test_fetch_service_account_for_customer_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_service_account_for_customer), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.FeedServiceAccount()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.fetch_service_account_for_customer(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_fetch_service_account_for_customer_flattened_error():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.fetch_service_account_for_customer(
            feed.FetchServiceAccountForCustomerRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_fetch_service_account_for_customer_flattened_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_service_account_for_customer), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.FeedServiceAccount()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.FeedServiceAccount()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.fetch_service_account_for_customer(
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
async def test_fetch_service_account_for_customer_flattened_error_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.fetch_service_account_for_customer(
            feed.FetchServiceAccountForCustomerRequest(),
            parent="parent_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        gcc_feed.CreateFeedRequest(),
        {},
    ],
)
def test_create_feed(request_type, transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcc_feed.Feed(
            name="name_value",
            uid="uid_value",
            display_name="display_name_value",
            state=gcc_feed.Feed.State.ACTIVE,
            failure_msg="failure_msg_value",
            read_only=True,
            reference_id="reference_id_value",
        )
        response = client.create_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gcc_feed.CreateFeedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcc_feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == gcc_feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


def test_create_feed_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gcc_feed.CreateFeedRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_feed), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_feed(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_feed.CreateFeedRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_create_feed_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_feed in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_feed] = mock_rpc
        request = {}
        client.create_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_feed_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FeedsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_feed
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_feed
        ] = mock_rpc

        request = {}
        await client.create_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.create_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        gcc_feed.CreateFeedRequest(),
        {},
    ],
)
async def test_create_feed_async(request_type, transport: str = "grpc_asyncio"):
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcc_feed.Feed(
                name="name_value",
                uid="uid_value",
                display_name="display_name_value",
                state=gcc_feed.Feed.State.ACTIVE,
                failure_msg="failure_msg_value",
                read_only=True,
                reference_id="reference_id_value",
            )
        )
        response = await client.create_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gcc_feed.CreateFeedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcc_feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == gcc_feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


def test_create_feed_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = gcc_feed.CreateFeedRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_feed), "__call__") as call:
        call.return_value = gcc_feed.Feed()
        client.create_feed(request)

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
async def test_create_feed_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = gcc_feed.CreateFeedRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_feed), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gcc_feed.Feed())
        await client.create_feed(request)

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


def test_create_feed_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcc_feed.Feed()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_feed(
            parent="parent_value",
            feed=gcc_feed.Feed(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].feed
        mock_val = gcc_feed.Feed(name="name_value")
        assert arg == mock_val


def test_create_feed_flattened_error():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_feed(
            gcc_feed.CreateFeedRequest(),
            parent="parent_value",
            feed=gcc_feed.Feed(name="name_value"),
        )


@pytest.mark.asyncio
async def test_create_feed_flattened_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcc_feed.Feed()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gcc_feed.Feed())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_feed(
            parent="parent_value",
            feed=gcc_feed.Feed(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].feed
        mock_val = gcc_feed.Feed(name="name_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_feed_flattened_error_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_feed(
            gcc_feed.CreateFeedRequest(),
            parent="parent_value",
            feed=gcc_feed.Feed(name="name_value"),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        feed.GetFeedRequest(),
        {},
    ],
)
def test_get_feed(request_type, transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.Feed(
            name="name_value",
            uid="uid_value",
            display_name="display_name_value",
            state=feed.Feed.State.ACTIVE,
            failure_msg="failure_msg_value",
            read_only=True,
            reference_id="reference_id_value",
        )
        response = client.get_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = feed.GetFeedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


def test_get_feed_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = feed.GetFeedRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_feed), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_feed(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.GetFeedRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_feed_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_feed in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_feed] = mock_rpc
        request = {}
        client.get_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_feed_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FeedsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_feed
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_feed
        ] = mock_rpc

        request = {}
        await client.get_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        feed.GetFeedRequest(),
        {},
    ],
)
async def test_get_feed_async(request_type, transport: str = "grpc_asyncio"):
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.Feed(
                name="name_value",
                uid="uid_value",
                display_name="display_name_value",
                state=feed.Feed.State.ACTIVE,
                failure_msg="failure_msg_value",
                read_only=True,
                reference_id="reference_id_value",
            )
        )
        response = await client.get_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = feed.GetFeedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


def test_get_feed_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.GetFeedRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_feed), "__call__") as call:
        call.return_value = feed.Feed()
        client.get_feed(request)

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
async def test_get_feed_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.GetFeedRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_feed), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(feed.Feed())
        await client.get_feed(request)

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


def test_get_feed_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.Feed()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_feed(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_feed_flattened_error():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_feed(
            feed.GetFeedRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_feed_flattened_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.Feed()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(feed.Feed())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_feed(
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
async def test_get_feed_flattened_error_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_feed(
            feed.GetFeedRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        feed.DeleteFeedRequest(),
        {},
    ],
)
def test_delete_feed(request_type, transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = feed.DeleteFeedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_feed_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = feed.DeleteFeedRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_feed), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.delete_feed(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.DeleteFeedRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_delete_feed_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_feed in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_feed] = mock_rpc
        request = {}
        client.delete_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_delete_feed_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FeedsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.delete_feed
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.delete_feed
        ] = mock_rpc

        request = {}
        await client.delete_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.delete_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        feed.DeleteFeedRequest(),
        {},
    ],
)
async def test_delete_feed_async(request_type, transport: str = "grpc_asyncio"):
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = feed.DeleteFeedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_feed_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.DeleteFeedRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_feed), "__call__") as call:
        call.return_value = None
        client.delete_feed(request)

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
async def test_delete_feed_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.DeleteFeedRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_feed), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_feed(request)

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


def test_delete_feed_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_feed(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_feed_flattened_error():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_feed(
            feed.DeleteFeedRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_feed_flattened_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_feed(
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
async def test_delete_feed_flattened_error_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_feed(
            feed.DeleteFeedRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        feed.EnableFeedRequest(),
        {},
    ],
)
def test_enable_feed(request_type, transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.enable_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.Feed(
            name="name_value",
            uid="uid_value",
            display_name="display_name_value",
            state=feed.Feed.State.ACTIVE,
            failure_msg="failure_msg_value",
            read_only=True,
            reference_id="reference_id_value",
        )
        response = client.enable_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = feed.EnableFeedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


def test_enable_feed_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = feed.EnableFeedRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.enable_feed), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.enable_feed(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.EnableFeedRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_enable_feed_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.enable_feed in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.enable_feed] = mock_rpc
        request = {}
        client.enable_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.enable_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_enable_feed_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FeedsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.enable_feed
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.enable_feed
        ] = mock_rpc

        request = {}
        await client.enable_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.enable_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        feed.EnableFeedRequest(),
        {},
    ],
)
async def test_enable_feed_async(request_type, transport: str = "grpc_asyncio"):
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.enable_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.Feed(
                name="name_value",
                uid="uid_value",
                display_name="display_name_value",
                state=feed.Feed.State.ACTIVE,
                failure_msg="failure_msg_value",
                read_only=True,
                reference_id="reference_id_value",
            )
        )
        response = await client.enable_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = feed.EnableFeedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


def test_enable_feed_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.EnableFeedRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.enable_feed), "__call__") as call:
        call.return_value = feed.Feed()
        client.enable_feed(request)

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
async def test_enable_feed_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.EnableFeedRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.enable_feed), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(feed.Feed())
        await client.enable_feed(request)

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


def test_enable_feed_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.enable_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.Feed()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.enable_feed(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_enable_feed_flattened_error():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.enable_feed(
            feed.EnableFeedRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_enable_feed_flattened_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.enable_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.Feed()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(feed.Feed())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.enable_feed(
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
async def test_enable_feed_flattened_error_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.enable_feed(
            feed.EnableFeedRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        feed.DisableFeedRequest(),
        {},
    ],
)
def test_disable_feed(request_type, transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.disable_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.Feed(
            name="name_value",
            uid="uid_value",
            display_name="display_name_value",
            state=feed.Feed.State.ACTIVE,
            failure_msg="failure_msg_value",
            read_only=True,
            reference_id="reference_id_value",
        )
        response = client.disable_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = feed.DisableFeedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


def test_disable_feed_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = feed.DisableFeedRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.disable_feed), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.disable_feed(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.DisableFeedRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_disable_feed_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.disable_feed in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.disable_feed] = mock_rpc
        request = {}
        client.disable_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.disable_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_disable_feed_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FeedsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.disable_feed
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.disable_feed
        ] = mock_rpc

        request = {}
        await client.disable_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.disable_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        feed.DisableFeedRequest(),
        {},
    ],
)
async def test_disable_feed_async(request_type, transport: str = "grpc_asyncio"):
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.disable_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.Feed(
                name="name_value",
                uid="uid_value",
                display_name="display_name_value",
                state=feed.Feed.State.ACTIVE,
                failure_msg="failure_msg_value",
                read_only=True,
                reference_id="reference_id_value",
            )
        )
        response = await client.disable_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = feed.DisableFeedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


def test_disable_feed_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.DisableFeedRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.disable_feed), "__call__") as call:
        call.return_value = feed.Feed()
        client.disable_feed(request)

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
async def test_disable_feed_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.DisableFeedRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.disable_feed), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(feed.Feed())
        await client.disable_feed(request)

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


def test_disable_feed_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.disable_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.Feed()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.disable_feed(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_disable_feed_flattened_error():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.disable_feed(
            feed.DisableFeedRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_disable_feed_flattened_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.disable_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.Feed()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(feed.Feed())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.disable_feed(
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
async def test_disable_feed_flattened_error_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.disable_feed(
            feed.DisableFeedRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        feed.ListFeedsRequest(),
        {},
    ],
)
def test_list_feeds(request_type, transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feeds), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.ListFeedsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_feeds(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = feed.ListFeedsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFeedsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_feeds_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = feed.ListFeedsRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feeds), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_feeds(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListFeedsRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_feeds_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_feeds in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_feeds] = mock_rpc
        request = {}
        client.list_feeds(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_feeds(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_feeds_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FeedsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_feeds
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_feeds
        ] = mock_rpc

        request = {}
        await client.list_feeds(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_feeds(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        feed.ListFeedsRequest(),
        {},
    ],
)
async def test_list_feeds_async(request_type, transport: str = "grpc_asyncio"):
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feeds), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListFeedsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_feeds(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = feed.ListFeedsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFeedsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_feeds_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.ListFeedsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feeds), "__call__") as call:
        call.return_value = feed.ListFeedsResponse()
        client.list_feeds(request)

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
async def test_list_feeds_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.ListFeedsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feeds), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListFeedsResponse()
        )
        await client.list_feeds(request)

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


def test_list_feeds_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feeds), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.ListFeedsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_feeds(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_feeds_flattened_error():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_feeds(
            feed.ListFeedsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_feeds_flattened_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feeds), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.ListFeedsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListFeedsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_feeds(
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
async def test_list_feeds_flattened_error_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_feeds(
            feed.ListFeedsRequest(),
            parent="parent_value",
        )


def test_list_feeds_pager(transport_name: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feeds), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                    feed.Feed(),
                    feed.Feed(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedsResponse(
                feeds=[],
                next_page_token="def",
            ),
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                    feed.Feed(),
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
        pager = client.list_feeds(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, feed.Feed) for i in results)


def test_list_feeds_pages(transport_name: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feeds), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                    feed.Feed(),
                    feed.Feed(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedsResponse(
                feeds=[],
                next_page_token="def",
            ),
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                    feed.Feed(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_feeds(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_feeds_async_pager():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feeds), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                    feed.Feed(),
                    feed.Feed(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedsResponse(
                feeds=[],
                next_page_token="def",
            ),
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                    feed.Feed(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_feeds(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, feed.Feed) for i in responses)


@pytest.mark.asyncio
async def test_list_feeds_async_pages():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feeds), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                    feed.Feed(),
                    feed.Feed(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedsResponse(
                feeds=[],
                next_page_token="def",
            ),
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                    feed.Feed(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_feeds(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        feed.ListFeedPacksRequest(),
        {},
    ],
)
def test_list_feed_packs(request_type, transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feed_packs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.ListFeedPacksResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_feed_packs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = feed.ListFeedPacksRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFeedPacksPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_feed_packs_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = feed.ListFeedPacksRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feed_packs), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_feed_packs(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListFeedPacksRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_feed_packs_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_feed_packs in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_feed_packs] = mock_rpc
        request = {}
        client.list_feed_packs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_feed_packs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_feed_packs_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FeedsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_feed_packs
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_feed_packs
        ] = mock_rpc

        request = {}
        await client.list_feed_packs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_feed_packs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        feed.ListFeedPacksRequest(),
        {},
    ],
)
async def test_list_feed_packs_async(request_type, transport: str = "grpc_asyncio"):
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feed_packs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListFeedPacksResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_feed_packs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = feed.ListFeedPacksRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFeedPacksAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_feed_packs_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.ListFeedPacksRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feed_packs), "__call__") as call:
        call.return_value = feed.ListFeedPacksResponse()
        client.list_feed_packs(request)

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
async def test_list_feed_packs_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.ListFeedPacksRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feed_packs), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListFeedPacksResponse()
        )
        await client.list_feed_packs(request)

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


def test_list_feed_packs_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feed_packs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.ListFeedPacksResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_feed_packs(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_feed_packs_flattened_error():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_feed_packs(
            feed.ListFeedPacksRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_feed_packs_flattened_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feed_packs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.ListFeedPacksResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListFeedPacksResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_feed_packs(
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
async def test_list_feed_packs_flattened_error_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_feed_packs(
            feed.ListFeedPacksRequest(),
            parent="parent_value",
        )


def test_list_feed_packs_pager(transport_name: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feed_packs), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                    feed.FeedPack(),
                    feed.FeedPack(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[],
                next_page_token="def",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                    feed.FeedPack(),
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
        pager = client.list_feed_packs(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, feed.FeedPack) for i in results)


def test_list_feed_packs_pages(transport_name: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_feed_packs), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                    feed.FeedPack(),
                    feed.FeedPack(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[],
                next_page_token="def",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                    feed.FeedPack(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_feed_packs(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_feed_packs_async_pager():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_packs), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                    feed.FeedPack(),
                    feed.FeedPack(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[],
                next_page_token="def",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                    feed.FeedPack(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_feed_packs(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, feed.FeedPack) for i in responses)


@pytest.mark.asyncio
async def test_list_feed_packs_async_pages():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_packs), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                    feed.FeedPack(),
                    feed.FeedPack(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[],
                next_page_token="def",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                    feed.FeedPack(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_feed_packs(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        feed.GetFeedPackRequest(),
        {},
    ],
)
def test_get_feed_pack(request_type, transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_feed_pack), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.FeedPack(
            name="name_value",
            display_name="display_name_value",
            description="description_value",
            icon=b"icon_blob",
            categories=["categories_value"],
            pack_type=feed.FeedPack.PackType.PRODUCT_BASED,
            hidden=True,
            pack_documentation="pack_documentation_value",
        )
        response = client.get_feed_pack(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = feed.GetFeedPackRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.FeedPack)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.description == "description_value"
    assert response.icon == b"icon_blob"
    assert response.categories == ["categories_value"]
    assert response.pack_type == feed.FeedPack.PackType.PRODUCT_BASED
    assert response.hidden is True
    assert response.pack_documentation == "pack_documentation_value"


def test_get_feed_pack_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = feed.GetFeedPackRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_feed_pack), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_feed_pack(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.GetFeedPackRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_feed_pack_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_feed_pack in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_feed_pack] = mock_rpc
        request = {}
        client.get_feed_pack(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_feed_pack(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_feed_pack_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FeedsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_feed_pack
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_feed_pack
        ] = mock_rpc

        request = {}
        await client.get_feed_pack(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_feed_pack(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        feed.GetFeedPackRequest(),
        {},
    ],
)
async def test_get_feed_pack_async(request_type, transport: str = "grpc_asyncio"):
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_feed_pack), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.FeedPack(
                name="name_value",
                display_name="display_name_value",
                description="description_value",
                icon=b"icon_blob",
                categories=["categories_value"],
                pack_type=feed.FeedPack.PackType.PRODUCT_BASED,
                hidden=True,
                pack_documentation="pack_documentation_value",
            )
        )
        response = await client.get_feed_pack(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = feed.GetFeedPackRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.FeedPack)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.description == "description_value"
    assert response.icon == b"icon_blob"
    assert response.categories == ["categories_value"]
    assert response.pack_type == feed.FeedPack.PackType.PRODUCT_BASED
    assert response.hidden is True
    assert response.pack_documentation == "pack_documentation_value"


def test_get_feed_pack_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.GetFeedPackRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_feed_pack), "__call__") as call:
        call.return_value = feed.FeedPack()
        client.get_feed_pack(request)

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
async def test_get_feed_pack_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.GetFeedPackRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_feed_pack), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(feed.FeedPack())
        await client.get_feed_pack(request)

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


def test_get_feed_pack_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_feed_pack), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.FeedPack()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_feed_pack(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_feed_pack_flattened_error():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_feed_pack(
            feed.GetFeedPackRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_feed_pack_flattened_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_feed_pack), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.FeedPack()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(feed.FeedPack())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_feed_pack(
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
async def test_get_feed_pack_flattened_error_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_feed_pack(
            feed.GetFeedPackRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        gcc_feed.UpdateFeedRequest(),
        {},
    ],
)
def test_update_feed(request_type, transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcc_feed.Feed(
            name="name_value",
            uid="uid_value",
            display_name="display_name_value",
            state=gcc_feed.Feed.State.ACTIVE,
            failure_msg="failure_msg_value",
            read_only=True,
            reference_id="reference_id_value",
        )
        response = client.update_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gcc_feed.UpdateFeedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcc_feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == gcc_feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


def test_update_feed_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gcc_feed.UpdateFeedRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_feed), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_feed(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_feed.UpdateFeedRequest()
        assert args[0] == request_msg


def test_update_feed_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_feed in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_feed] = mock_rpc
        request = {}
        client.update_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_feed_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FeedsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_feed
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_feed
        ] = mock_rpc

        request = {}
        await client.update_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        gcc_feed.UpdateFeedRequest(),
        {},
    ],
)
async def test_update_feed_async(request_type, transport: str = "grpc_asyncio"):
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcc_feed.Feed(
                name="name_value",
                uid="uid_value",
                display_name="display_name_value",
                state=gcc_feed.Feed.State.ACTIVE,
                failure_msg="failure_msg_value",
                read_only=True,
                reference_id="reference_id_value",
            )
        )
        response = await client.update_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gcc_feed.UpdateFeedRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcc_feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == gcc_feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


def test_update_feed_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = gcc_feed.UpdateFeedRequest()

    request.feed.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_feed), "__call__") as call:
        call.return_value = gcc_feed.Feed()
        client.update_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "feed.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_feed_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = gcc_feed.UpdateFeedRequest()

    request.feed.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_feed), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gcc_feed.Feed())
        await client.update_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "feed.name=name_value",
    ) in kw["metadata"]


def test_update_feed_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcc_feed.Feed()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_feed(
            feed=gcc_feed.Feed(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].feed
        mock_val = gcc_feed.Feed(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_feed_flattened_error():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_feed(
            gcc_feed.UpdateFeedRequest(),
            feed=gcc_feed.Feed(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_feed_flattened_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.update_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcc_feed.Feed()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(gcc_feed.Feed())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_feed(
            feed=gcc_feed.Feed(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].feed
        mock_val = gcc_feed.Feed(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_feed_flattened_error_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_feed(
            gcc_feed.UpdateFeedRequest(),
            feed=gcc_feed.Feed(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        feed.ListFeedSourceTypeSchemasRequest(),
        {},
    ],
)
def test_list_feed_source_type_schemas(request_type, transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_source_type_schemas), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.ListFeedSourceTypeSchemasResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_feed_source_type_schemas(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = feed.ListFeedSourceTypeSchemasRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFeedSourceTypeSchemasPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_feed_source_type_schemas_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = feed.ListFeedSourceTypeSchemasRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_source_type_schemas), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_feed_source_type_schemas(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListFeedSourceTypeSchemasRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_feed_source_type_schemas_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_feed_source_type_schemas
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_feed_source_type_schemas
        ] = mock_rpc
        request = {}
        client.list_feed_source_type_schemas(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_feed_source_type_schemas(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_feed_source_type_schemas_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FeedsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_feed_source_type_schemas
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_feed_source_type_schemas
        ] = mock_rpc

        request = {}
        await client.list_feed_source_type_schemas(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_feed_source_type_schemas(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        feed.ListFeedSourceTypeSchemasRequest(),
        {},
    ],
)
async def test_list_feed_source_type_schemas_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_source_type_schemas), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListFeedSourceTypeSchemasResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_feed_source_type_schemas(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = feed.ListFeedSourceTypeSchemasRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFeedSourceTypeSchemasAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_feed_source_type_schemas_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.ListFeedSourceTypeSchemasRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_source_type_schemas), "__call__"
    ) as call:
        call.return_value = feed.ListFeedSourceTypeSchemasResponse()
        client.list_feed_source_type_schemas(request)

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
async def test_list_feed_source_type_schemas_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.ListFeedSourceTypeSchemasRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_source_type_schemas), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListFeedSourceTypeSchemasResponse()
        )
        await client.list_feed_source_type_schemas(request)

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


def test_list_feed_source_type_schemas_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_source_type_schemas), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.ListFeedSourceTypeSchemasResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_feed_source_type_schemas(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_feed_source_type_schemas_flattened_error():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_feed_source_type_schemas(
            feed.ListFeedSourceTypeSchemasRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_feed_source_type_schemas_flattened_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_source_type_schemas), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.ListFeedSourceTypeSchemasResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListFeedSourceTypeSchemasResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_feed_source_type_schemas(
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
async def test_list_feed_source_type_schemas_flattened_error_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_feed_source_type_schemas(
            feed.ListFeedSourceTypeSchemasRequest(),
            parent="parent_value",
        )


def test_list_feed_source_type_schemas_pager(transport_name: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_source_type_schemas), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[],
                next_page_token="def",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
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
        pager = client.list_feed_source_type_schemas(
            request={}, retry=retry, timeout=timeout
        )

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, feed.FeedSourceTypeSchema) for i in results)


def test_list_feed_source_type_schemas_pages(transport_name: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_source_type_schemas), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[],
                next_page_token="def",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_feed_source_type_schemas(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_feed_source_type_schemas_async_pager():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_source_type_schemas),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[],
                next_page_token="def",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_feed_source_type_schemas(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, feed.FeedSourceTypeSchema) for i in responses)


@pytest.mark.asyncio
async def test_list_feed_source_type_schemas_async_pages():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_source_type_schemas),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[],
                next_page_token="def",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.list_feed_source_type_schemas(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        feed.ListLogTypeSchemasRequest(),
        {},
    ],
)
def test_list_log_type_schemas(request_type, transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_log_type_schemas), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.ListLogTypeSchemasResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_log_type_schemas(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = feed.ListLogTypeSchemasRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListLogTypeSchemasPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_log_type_schemas_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = feed.ListLogTypeSchemasRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_log_type_schemas), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_log_type_schemas(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListLogTypeSchemasRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_log_type_schemas_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_log_type_schemas
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_log_type_schemas] = (
            mock_rpc
        )
        request = {}
        client.list_log_type_schemas(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_log_type_schemas(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_log_type_schemas_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FeedsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_log_type_schemas
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_log_type_schemas
        ] = mock_rpc

        request = {}
        await client.list_log_type_schemas(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_log_type_schemas(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        feed.ListLogTypeSchemasRequest(),
        {},
    ],
)
async def test_list_log_type_schemas_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_log_type_schemas), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListLogTypeSchemasResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_log_type_schemas(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = feed.ListLogTypeSchemasRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListLogTypeSchemasAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_log_type_schemas_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.ListLogTypeSchemasRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_log_type_schemas), "__call__"
    ) as call:
        call.return_value = feed.ListLogTypeSchemasResponse()
        client.list_log_type_schemas(request)

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
async def test_list_log_type_schemas_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.ListLogTypeSchemasRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_log_type_schemas), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListLogTypeSchemasResponse()
        )
        await client.list_log_type_schemas(request)

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


def test_list_log_type_schemas_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_log_type_schemas), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.ListLogTypeSchemasResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_log_type_schemas(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_log_type_schemas_flattened_error():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_log_type_schemas(
            feed.ListLogTypeSchemasRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_log_type_schemas_flattened_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_log_type_schemas), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.ListLogTypeSchemasResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListLogTypeSchemasResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_log_type_schemas(
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
async def test_list_log_type_schemas_flattened_error_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_log_type_schemas(
            feed.ListLogTypeSchemasRequest(),
            parent="parent_value",
        )


def test_list_log_type_schemas_pager(transport_name: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_log_type_schemas), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
                ],
                next_page_token="abc",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[],
                next_page_token="def",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                ],
                next_page_token="ghi",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
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
        pager = client.list_log_type_schemas(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, feed.LogTypeSchema) for i in results)


def test_list_log_type_schemas_pages(transport_name: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_log_type_schemas), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
                ],
                next_page_token="abc",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[],
                next_page_token="def",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                ],
                next_page_token="ghi",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_log_type_schemas(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_log_type_schemas_async_pager():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_log_type_schemas),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
                ],
                next_page_token="abc",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[],
                next_page_token="def",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                ],
                next_page_token="ghi",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_log_type_schemas(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, feed.LogTypeSchema) for i in responses)


@pytest.mark.asyncio
async def test_list_log_type_schemas_async_pages():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_log_type_schemas),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
                ],
                next_page_token="abc",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[],
                next_page_token="def",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                ],
                next_page_token="ghi",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_log_type_schemas(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        feed.ImportPushLogsRequest(),
        {},
    ],
)
def test_import_push_logs(request_type, transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.import_push_logs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = httpbody_pb2.HttpBody(
            content_type="content_type_value",
            data=b"data_blob",
        )
        response = client.import_push_logs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = feed.ImportPushLogsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, httpbody_pb2.HttpBody)
    assert response.content_type == "content_type_value"
    assert response.data == b"data_blob"


def test_import_push_logs_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = feed.ImportPushLogsRequest(
        parent="parent_value",
        secret="secret_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.import_push_logs), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.import_push_logs(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ImportPushLogsRequest(
            parent="parent_value",
            secret="secret_value",
        )
        assert args[0] == request_msg


def test_import_push_logs_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.import_push_logs in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.import_push_logs] = (
            mock_rpc
        )
        request = {}
        client.import_push_logs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.import_push_logs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_import_push_logs_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FeedsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.import_push_logs
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.import_push_logs
        ] = mock_rpc

        request = {}
        await client.import_push_logs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.import_push_logs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        feed.ImportPushLogsRequest(),
        {},
    ],
)
async def test_import_push_logs_async(request_type, transport: str = "grpc_asyncio"):
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.import_push_logs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            httpbody_pb2.HttpBody(
                content_type="content_type_value",
                data=b"data_blob",
            )
        )
        response = await client.import_push_logs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = feed.ImportPushLogsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, httpbody_pb2.HttpBody)
    assert response.content_type == "content_type_value"
    assert response.data == b"data_blob"


def test_import_push_logs_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.ImportPushLogsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.import_push_logs), "__call__") as call:
        call.return_value = httpbody_pb2.HttpBody()
        client.import_push_logs(request)

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
async def test_import_push_logs_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.ImportPushLogsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.import_push_logs), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            httpbody_pb2.HttpBody()
        )
        await client.import_push_logs(request)

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


def test_import_push_logs_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.import_push_logs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = httpbody_pb2.HttpBody()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.import_push_logs(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_import_push_logs_flattened_error():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.import_push_logs(
            feed.ImportPushLogsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_import_push_logs_flattened_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.import_push_logs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = httpbody_pb2.HttpBody()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            httpbody_pb2.HttpBody()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.import_push_logs(
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
async def test_import_push_logs_flattened_error_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.import_push_logs(
            feed.ImportPushLogsRequest(),
            parent="parent_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        feed.GenerateSecretRequest(),
        {},
    ],
)
def test_generate_secret(request_type, transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.generate_secret), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.GenerateSecretResponse(
            secret="secret_value",
        )
        response = client.generate_secret(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = feed.GenerateSecretRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.GenerateSecretResponse)
    assert response.secret == "secret_value"


def test_generate_secret_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = feed.GenerateSecretRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.generate_secret), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.generate_secret(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.GenerateSecretRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_generate_secret_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.generate_secret in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.generate_secret] = mock_rpc
        request = {}
        client.generate_secret(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.generate_secret(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_generate_secret_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = FeedsServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.generate_secret
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.generate_secret
        ] = mock_rpc

        request = {}
        await client.generate_secret(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.generate_secret(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        feed.GenerateSecretRequest(),
        {},
    ],
)
async def test_generate_secret_async(request_type, transport: str = "grpc_asyncio"):
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.generate_secret), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.GenerateSecretResponse(
                secret="secret_value",
            )
        )
        response = await client.generate_secret(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = feed.GenerateSecretRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.GenerateSecretResponse)
    assert response.secret == "secret_value"


def test_generate_secret_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.GenerateSecretRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.generate_secret), "__call__") as call:
        call.return_value = feed.GenerateSecretResponse()
        client.generate_secret(request)

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
async def test_generate_secret_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = feed.GenerateSecretRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.generate_secret), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.GenerateSecretResponse()
        )
        await client.generate_secret(request)

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


def test_generate_secret_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.generate_secret), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.GenerateSecretResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.generate_secret(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_generate_secret_flattened_error():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.generate_secret(
            feed.GenerateSecretRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_generate_secret_flattened_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.generate_secret), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = feed.GenerateSecretResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.GenerateSecretResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.generate_secret(
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
async def test_generate_secret_flattened_error_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.generate_secret(
            feed.GenerateSecretRequest(),
            name="name_value",
        )


def test_fetch_service_account_for_customer_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.fetch_service_account_for_customer
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.fetch_service_account_for_customer
        ] = mock_rpc

        request = {}
        client.fetch_service_account_for_customer(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fetch_service_account_for_customer(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_fetch_service_account_for_customer_rest_required_fields(
    request_type=feed.FetchServiceAccountForCustomerRequest,
):
    transport_class = transports.FeedsServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseFetchServiceAccountForCustomer,
        "_BaseFetchServiceAccountForCustomer__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = feed.FeedServiceAccount()
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
            return_value = feed.FeedServiceAccount.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.fetch_service_account_for_customer(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_fetch_service_account_for_customer_rest_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.FeedServiceAccount()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = feed.FeedServiceAccount.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.fetch_service_account_for_customer(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*/instances/*}/feedServiceAccounts:fetchServiceAccountForCustomer"
            % client.transport._host,
            args[1],
        )


def test_fetch_service_account_for_customer_rest_flattened_error(
    transport: str = "rest",
):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.fetch_service_account_for_customer(
            feed.FetchServiceAccountForCustomerRequest(),
            parent="parent_value",
        )


def test_create_feed_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_feed in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_feed] = mock_rpc

        request = {}
        client.create_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_feed_rest_required_fields(request_type=gcc_feed.CreateFeedRequest):
    transport_class = transports.FeedsServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateFeed,
        "_BaseCreateFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gcc_feed.Feed()
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
            return_value = gcc_feed.Feed.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_feed(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_feed_rest_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcc_feed.Feed()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            feed=gcc_feed.Feed(name="name_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = gcc_feed.Feed.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_feed(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*/instances/*}/feeds"
            % client.transport._host,
            args[1],
        )


def test_create_feed_rest_flattened_error(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_feed(
            gcc_feed.CreateFeedRequest(),
            parent="parent_value",
            feed=gcc_feed.Feed(name="name_value"),
        )


def test_get_feed_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_feed in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_feed] = mock_rpc

        request = {}
        client.get_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_feed_rest_required_fields(request_type=feed.GetFeedRequest):
    transport_class = transports.FeedsServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetFeed,
        "_BaseGetFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = feed.Feed()
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
            return_value = feed.Feed.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_feed(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_feed_rest_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.Feed()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
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
        return_value = feed.Feed.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_feed(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/instances/*/feeds/*}"
            % client.transport._host,
            args[1],
        )


def test_get_feed_rest_flattened_error(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_feed(
            feed.GetFeedRequest(),
            name="name_value",
        )


def test_delete_feed_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_feed in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_feed] = mock_rpc

        request = {}
        client.delete_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_feed_rest_required_fields(request_type=feed.DeleteFeedRequest):
    transport_class = transports.FeedsServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeleteFeed,
        "_BaseDeleteFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("deleteBacklog",))

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = None
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
            json_return_value = ""

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.delete_feed(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_feed_rest_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = ""
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.delete_feed(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/instances/*/feeds/*}"
            % client.transport._host,
            args[1],
        )


def test_delete_feed_rest_flattened_error(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_feed(
            feed.DeleteFeedRequest(),
            name="name_value",
        )


def test_enable_feed_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.enable_feed in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.enable_feed] = mock_rpc

        request = {}
        client.enable_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.enable_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_enable_feed_rest_required_fields(request_type=feed.EnableFeedRequest):
    transport_class = transports.FeedsServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseEnableFeed,
        "_BaseEnableFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = feed.Feed()
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
            return_value = feed.Feed.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.enable_feed(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_enable_feed_rest_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.Feed()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
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
        return_value = feed.Feed.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.enable_feed(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/instances/*/feeds/*}:enable"
            % client.transport._host,
            args[1],
        )


def test_enable_feed_rest_flattened_error(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.enable_feed(
            feed.EnableFeedRequest(),
            name="name_value",
        )


def test_disable_feed_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.disable_feed in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.disable_feed] = mock_rpc

        request = {}
        client.disable_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.disable_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_disable_feed_rest_required_fields(request_type=feed.DisableFeedRequest):
    transport_class = transports.FeedsServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDisableFeed,
        "_BaseDisableFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = feed.Feed()
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
            return_value = feed.Feed.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.disable_feed(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_disable_feed_rest_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.Feed()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
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
        return_value = feed.Feed.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.disable_feed(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/instances/*/feeds/*}:disable"
            % client.transport._host,
            args[1],
        )


def test_disable_feed_rest_flattened_error(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.disable_feed(
            feed.DisableFeedRequest(),
            name="name_value",
        )


def test_list_feeds_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_feeds in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_feeds] = mock_rpc

        request = {}
        client.list_feeds(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_feeds(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_feeds_rest_required_fields(request_type=feed.ListFeedsRequest):
    transport_class = transports.FeedsServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListFeeds,
        "_BaseListFeeds__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = feed.ListFeedsResponse()
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
            return_value = feed.ListFeedsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_feeds(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_feeds_rest_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.ListFeedsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = feed.ListFeedsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_feeds(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*/instances/*}/feeds"
            % client.transport._host,
            args[1],
        )


def test_list_feeds_rest_flattened_error(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_feeds(
            feed.ListFeedsRequest(),
            parent="parent_value",
        )


def test_list_feeds_rest_pager(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                    feed.Feed(),
                    feed.Feed(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedsResponse(
                feeds=[],
                next_page_token="def",
            ),
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedsResponse(
                feeds=[
                    feed.Feed(),
                    feed.Feed(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(feed.ListFeedsResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3"
        }

        pager = client.list_feeds(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, feed.Feed) for i in results)

        pages = list(client.list_feeds(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_list_feed_packs_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_feed_packs in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_feed_packs] = mock_rpc

        request = {}
        client.list_feed_packs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_feed_packs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_feed_packs_rest_required_fields(request_type=feed.ListFeedPacksRequest):
    transport_class = transports.FeedsServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListFeedPacks,
        "_BaseListFeedPacks__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = feed.ListFeedPacksResponse()
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
            return_value = feed.ListFeedPacksResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_feed_packs(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_feed_packs_rest_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.ListFeedPacksResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = feed.ListFeedPacksResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_feed_packs(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*/instances/*}/feedPacks"
            % client.transport._host,
            args[1],
        )


def test_list_feed_packs_rest_flattened_error(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_feed_packs(
            feed.ListFeedPacksRequest(),
            parent="parent_value",
        )


def test_list_feed_packs_rest_pager(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                    feed.FeedPack(),
                    feed.FeedPack(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[],
                next_page_token="def",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedPacksResponse(
                feed_packs=[
                    feed.FeedPack(),
                    feed.FeedPack(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(feed.ListFeedPacksResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3"
        }

        pager = client.list_feed_packs(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, feed.FeedPack) for i in results)

        pages = list(client.list_feed_packs(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_get_feed_pack_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_feed_pack in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_feed_pack] = mock_rpc

        request = {}
        client.get_feed_pack(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_feed_pack(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_feed_pack_rest_required_fields(request_type=feed.GetFeedPackRequest):
    transport_class = transports.FeedsServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetFeedPack,
        "_BaseGetFeedPack__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = feed.FeedPack()
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
            return_value = feed.FeedPack.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_feed_pack(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_feed_pack_rest_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.FeedPack()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/instances/sample3/feedPacks/sample4"
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
        return_value = feed.FeedPack.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_feed_pack(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/instances/*/feedPacks/*}"
            % client.transport._host,
            args[1],
        )


def test_get_feed_pack_rest_flattened_error(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_feed_pack(
            feed.GetFeedPackRequest(),
            name="name_value",
        )


def test_update_feed_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_feed in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_feed] = mock_rpc

        request = {}
        client.update_feed(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_feed(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_feed_rest_required_fields(request_type=gcc_feed.UpdateFeedRequest):
    transport_class = transports.FeedsServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateFeed,
        "_BaseUpdateFeed__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gcc_feed.Feed()
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
            return_value = gcc_feed.Feed.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_feed(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_feed_rest_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcc_feed.Feed()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "feed": {
                "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            feed=gcc_feed.Feed(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = gcc_feed.Feed.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_feed(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{feed.name=projects/*/locations/*/instances/*/feeds/*}"
            % client.transport._host,
            args[1],
        )


def test_update_feed_rest_flattened_error(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_feed(
            gcc_feed.UpdateFeedRequest(),
            feed=gcc_feed.Feed(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_list_feed_source_type_schemas_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_feed_source_type_schemas
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_feed_source_type_schemas
        ] = mock_rpc

        request = {}
        client.list_feed_source_type_schemas(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_feed_source_type_schemas(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_feed_source_type_schemas_rest_required_fields(
    request_type=feed.ListFeedSourceTypeSchemasRequest,
):
    transport_class = transports.FeedsServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListFeedSourceTypeSchemas,
        "_BaseListFeedSourceTypeSchemas__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = feed.ListFeedSourceTypeSchemasResponse()
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
            return_value = feed.ListFeedSourceTypeSchemasResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_feed_source_type_schemas(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_feed_source_type_schemas_rest_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.ListFeedSourceTypeSchemasResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = feed.ListFeedSourceTypeSchemasResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_feed_source_type_schemas(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*/instances/*}/feedSourceTypeSchemas"
            % client.transport._host,
            args[1],
        )


def test_list_feed_source_type_schemas_rest_flattened_error(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_feed_source_type_schemas(
            feed.ListFeedSourceTypeSchemasRequest(),
            parent="parent_value",
        )


def test_list_feed_source_type_schemas_rest_pager(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
                ],
                next_page_token="abc",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[],
                next_page_token="def",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                ],
                next_page_token="ghi",
            ),
            feed.ListFeedSourceTypeSchemasResponse(
                feed_source_type_schemas=[
                    feed.FeedSourceTypeSchema(),
                    feed.FeedSourceTypeSchema(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            feed.ListFeedSourceTypeSchemasResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3"
        }

        pager = client.list_feed_source_type_schemas(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, feed.FeedSourceTypeSchema) for i in results)

        pages = list(client.list_feed_source_type_schemas(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_list_log_type_schemas_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_log_type_schemas
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_log_type_schemas] = (
            mock_rpc
        )

        request = {}
        client.list_log_type_schemas(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_log_type_schemas(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_log_type_schemas_rest_required_fields(
    request_type=feed.ListLogTypeSchemasRequest,
):
    transport_class = transports.FeedsServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListLogTypeSchemas,
        "_BaseListLogTypeSchemas__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = feed.ListLogTypeSchemasResponse()
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
            return_value = feed.ListLogTypeSchemasResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_log_type_schemas(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_log_type_schemas_rest_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.ListLogTypeSchemasResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3/feedSourceTypeSchemas/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = feed.ListLogTypeSchemasResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_log_type_schemas(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*/instances/*/feedSourceTypeSchemas/*}/logTypeSchemas"
            % client.transport._host,
            args[1],
        )


def test_list_log_type_schemas_rest_flattened_error(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_log_type_schemas(
            feed.ListLogTypeSchemasRequest(),
            parent="parent_value",
        )


def test_list_log_type_schemas_rest_pager(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
                ],
                next_page_token="abc",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[],
                next_page_token="def",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                ],
                next_page_token="ghi",
            ),
            feed.ListLogTypeSchemasResponse(
                log_type_schemas=[
                    feed.LogTypeSchema(),
                    feed.LogTypeSchema(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(feed.ListLogTypeSchemasResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3/feedSourceTypeSchemas/sample4"
        }

        pager = client.list_log_type_schemas(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, feed.LogTypeSchema) for i in results)

        pages = list(client.list_log_type_schemas(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_import_push_logs_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.import_push_logs in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.import_push_logs] = (
            mock_rpc
        )

        request = {}
        client.import_push_logs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.import_push_logs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_import_push_logs_rest_required_fields(request_type=feed.ImportPushLogsRequest):
    transport_class = transports.FeedsServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseImportPushLogs,
        "_BaseImportPushLogs__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = httpbody_pb2.HttpBody()
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

            response = client.import_push_logs(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_import_push_logs_rest_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = httpbody_pb2.HttpBody()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.import_push_logs(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*/instances/*/feeds/*}:importPushLogs"
            % client.transport._host,
            args[1],
        )


def test_import_push_logs_rest_flattened_error(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.import_push_logs(
            feed.ImportPushLogsRequest(),
            parent="parent_value",
        )


def test_generate_secret_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.generate_secret in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.generate_secret] = mock_rpc

        request = {}
        client.generate_secret(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.generate_secret(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_generate_secret_rest_required_fields(request_type=feed.GenerateSecretRequest):
    transport_class = transports.FeedsServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGenerateSecret,
        "_BaseGenerateSecret__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = feed.GenerateSecretResponse()
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
            return_value = feed.GenerateSecretResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.generate_secret(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_generate_secret_rest_flattened():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.GenerateSecretResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
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
        return_value = feed.GenerateSecretResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.generate_secret(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/instances/*/feeds/*}:generateSecret"
            % client.transport._host,
            args[1],
        )


def test_generate_secret_rest_flattened_error(transport: str = "rest"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.generate_secret(
            feed.GenerateSecretRequest(),
            name="name_value",
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.FeedsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.FeedsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = FeedsServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.FeedsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = FeedsServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = FeedsServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.FeedsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = FeedsServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.FeedsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = FeedsServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.FeedsServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.FeedsServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.FeedsServiceGrpcTransport,
        transports.FeedsServiceGrpcAsyncIOTransport,
        transports.FeedsServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = FeedsServiceClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fetch_service_account_for_customer_empty_call_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_service_account_for_customer), "__call__"
    ) as call:
        call.return_value = feed.FeedServiceAccount()
        client.fetch_service_account_for_customer(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.FetchServiceAccountForCustomerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_feed_empty_call_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_feed), "__call__") as call:
        call.return_value = gcc_feed.Feed()
        client.create_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_feed.CreateFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_feed_empty_call_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_feed), "__call__") as call:
        call.return_value = feed.Feed()
        client.get_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.GetFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_feed_empty_call_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.delete_feed), "__call__") as call:
        call.return_value = None
        client.delete_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.DeleteFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_enable_feed_empty_call_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.enable_feed), "__call__") as call:
        call.return_value = feed.Feed()
        client.enable_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.EnableFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_disable_feed_empty_call_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.disable_feed), "__call__") as call:
        call.return_value = feed.Feed()
        client.disable_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.DisableFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_feeds_empty_call_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_feeds), "__call__") as call:
        call.return_value = feed.ListFeedsResponse()
        client.list_feeds(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListFeedsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_feed_packs_empty_call_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_feed_packs), "__call__") as call:
        call.return_value = feed.ListFeedPacksResponse()
        client.list_feed_packs(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListFeedPacksRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_feed_pack_empty_call_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_feed_pack), "__call__") as call:
        call.return_value = feed.FeedPack()
        client.get_feed_pack(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.GetFeedPackRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_feed_empty_call_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_feed), "__call__") as call:
        call.return_value = gcc_feed.Feed()
        client.update_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_feed.UpdateFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_feed_source_type_schemas_empty_call_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_source_type_schemas), "__call__"
    ) as call:
        call.return_value = feed.ListFeedSourceTypeSchemasResponse()
        client.list_feed_source_type_schemas(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListFeedSourceTypeSchemasRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_log_type_schemas_empty_call_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_log_type_schemas), "__call__"
    ) as call:
        call.return_value = feed.ListLogTypeSchemasResponse()
        client.list_log_type_schemas(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListLogTypeSchemasRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_import_push_logs_empty_call_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.import_push_logs), "__call__") as call:
        call.return_value = httpbody_pb2.HttpBody()
        client.import_push_logs(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ImportPushLogsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_generate_secret_empty_call_grpc():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.generate_secret), "__call__") as call:
        call.return_value = feed.GenerateSecretResponse()
        client.generate_secret(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.GenerateSecretRequest()
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = FeedsServiceAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_fetch_service_account_for_customer_empty_call_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_service_account_for_customer), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.FeedServiceAccount(
                name="name_value",
                subject_id="subject_id_value",
            )
        )
        await client.fetch_service_account_for_customer(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.FetchServiceAccountForCustomerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_feed_empty_call_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcc_feed.Feed(
                name="name_value",
                uid="uid_value",
                display_name="display_name_value",
                state=gcc_feed.Feed.State.ACTIVE,
                failure_msg="failure_msg_value",
                read_only=True,
                reference_id="reference_id_value",
            )
        )
        await client.create_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_feed.CreateFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_feed_empty_call_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.Feed(
                name="name_value",
                uid="uid_value",
                display_name="display_name_value",
                state=feed.Feed.State.ACTIVE,
                failure_msg="failure_msg_value",
                read_only=True,
                reference_id="reference_id_value",
            )
        )
        await client.get_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.GetFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_feed_empty_call_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.delete_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.DeleteFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_enable_feed_empty_call_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.enable_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.Feed(
                name="name_value",
                uid="uid_value",
                display_name="display_name_value",
                state=feed.Feed.State.ACTIVE,
                failure_msg="failure_msg_value",
                read_only=True,
                reference_id="reference_id_value",
            )
        )
        await client.enable_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.EnableFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_disable_feed_empty_call_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.disable_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.Feed(
                name="name_value",
                uid="uid_value",
                display_name="display_name_value",
                state=feed.Feed.State.ACTIVE,
                failure_msg="failure_msg_value",
                read_only=True,
                reference_id="reference_id_value",
            )
        )
        await client.disable_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.DisableFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_feeds_empty_call_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_feeds), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListFeedsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_feeds(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListFeedsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_feed_packs_empty_call_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_feed_packs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListFeedPacksResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_feed_packs(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListFeedPacksRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_feed_pack_empty_call_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_feed_pack), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.FeedPack(
                name="name_value",
                display_name="display_name_value",
                description="description_value",
                icon=b"icon_blob",
                categories=["categories_value"],
                pack_type=feed.FeedPack.PackType.PRODUCT_BASED,
                hidden=True,
                pack_documentation="pack_documentation_value",
            )
        )
        await client.get_feed_pack(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.GetFeedPackRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_feed_empty_call_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_feed), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcc_feed.Feed(
                name="name_value",
                uid="uid_value",
                display_name="display_name_value",
                state=gcc_feed.Feed.State.ACTIVE,
                failure_msg="failure_msg_value",
                read_only=True,
                reference_id="reference_id_value",
            )
        )
        await client.update_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_feed.UpdateFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_feed_source_type_schemas_empty_call_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_source_type_schemas), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListFeedSourceTypeSchemasResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_feed_source_type_schemas(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListFeedSourceTypeSchemasRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_log_type_schemas_empty_call_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_log_type_schemas), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.ListLogTypeSchemasResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_log_type_schemas(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListLogTypeSchemasRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_import_push_logs_empty_call_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.import_push_logs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            httpbody_pb2.HttpBody(
                content_type="content_type_value",
                data=b"data_blob",
            )
        )
        await client.import_push_logs(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ImportPushLogsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_generate_secret_empty_call_grpc_asyncio():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.generate_secret), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            feed.GenerateSecretResponse(
                secret="secret_value",
            )
        )
        await client.generate_secret(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.GenerateSecretRequest()
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = FeedsServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_fetch_service_account_for_customer_rest_bad_request(
    request_type=feed.FetchServiceAccountForCustomerRequest,
):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/instances/sample3"}
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
        client.fetch_service_account_for_customer(request)


@pytest.mark.parametrize(
    "request_type",
    [
        feed.FetchServiceAccountForCustomerRequest,
        dict,
    ],
)
def test_fetch_service_account_for_customer_rest_call_success(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/instances/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.FeedServiceAccount(
            name="name_value",
            subject_id="subject_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = feed.FeedServiceAccount.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.fetch_service_account_for_customer(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.FeedServiceAccount)
    assert response.name == "name_value"
    assert response.subject_id == "subject_id_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_fetch_service_account_for_customer_rest_interceptors(null_interceptor):
    transport = transports.FeedsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FeedsServiceRestInterceptor(),
    )
    client = FeedsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor,
            "post_fetch_service_account_for_customer",
        ) as post,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor,
            "post_fetch_service_account_for_customer_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor,
            "pre_fetch_service_account_for_customer",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = feed.FetchServiceAccountForCustomerRequest.pb(
            feed.FetchServiceAccountForCustomerRequest()
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
        return_value = feed.FeedServiceAccount.to_json(feed.FeedServiceAccount())
        req.return_value.content = return_value

        request = feed.FetchServiceAccountForCustomerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = feed.FeedServiceAccount()
        post_with_metadata.return_value = feed.FeedServiceAccount(), metadata

        client.fetch_service_account_for_customer(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_feed_rest_bad_request(request_type=gcc_feed.CreateFeedRequest):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/instances/sample3"}
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
        client.create_feed(request)


@pytest.mark.parametrize(
    "request_type",
    [
        gcc_feed.CreateFeedRequest,
        dict,
    ],
)
def test_create_feed_rest_call_success(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/instances/sample3"}
    request_init["feed"] = {
        "name": "name_value",
        "uid": "uid_value",
        "display_name": "display_name_value",
        "details": {
            "anomali_settings": {
                "authentication": {"user": "user_value", "secret": "secret_value"},
                "hostname": "hostname_value",
            },
            "azure_ad_context_settings": {
                "authentication": {
                    "client_id": "client_id_value",
                    "client_secret": "client_secret_value",
                },
                "retrieve_devices": True,
                "retrieve_groups": True,
                "tenant_id": "tenant_id_value",
                "hostname": "hostname_value",
                "auth_endpoint": "auth_endpoint_value",
            },
            "cloud_passage_settings": {
                "authentication": {},
                "event_types": ["event_types_value1", "event_types_value2"],
            },
            "cortex_xdr_settings": {
                "authentication": {
                    "header_key_values": [{"key": "key_value", "value": "value_value"}]
                },
                "hostname": "hostname_value",
                "endpoint": "endpoint_value",
            },
            "duo_auth_settings": {"authentication": {}, "hostname": "hostname_value"},
            "duo_user_context_settings": {
                "authentication": {},
                "hostname": "hostname_value",
            },
            "microsoft_graph_alert_settings": {
                "authentication": {},
                "tenant_id": "tenant_id_value",
                "hostname": "hostname_value",
                "auth_endpoint": "auth_endpoint_value",
            },
            "microsoft_security_center_alert_settings": {
                "authentication": {},
                "subscription_id": "subscription_id_value",
                "tenant_id": "tenant_id_value",
                "hostname": "hostname_value",
                "auth_endpoint": "auth_endpoint_value",
            },
            "mimecast_mail_settings": {
                "authentication": {},
                "hostname": "hostname_value",
            },
            "office365_settings": {
                "authentication": {},
                "tenant_id": "tenant_id_value",
                "content_type": 1,
                "hostname": "hostname_value",
                "auth_endpoint": "auth_endpoint_value",
            },
            "proofpoint_mail_settings": {"authentication": {}},
            "recorded_future_ioc_settings": {"authentication": {}},
            "workday_settings": {
                "authentication": {
                    "user": "user_value",
                    "secret": "secret_value",
                    "token_endpoint": "token_endpoint_value",
                    "client_id": "client_id_value",
                    "client_secret": "client_secret_value",
                    "refresh_token": "refresh_token_value",
                },
                "hostname": "hostname_value",
                "tenant_id": "tenant_id_value",
            },
            "pan_ioc_settings": {
                "authentication": {},
                "feed_id": "feed_id_value",
                "feed": "feed_value",
            },
            "okta_settings": {"authentication": {}, "hostname": "hostname_value"},
            "okta_user_context_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "manager_id_reference_field": "manager_id_reference_field_value",
            },
            "fox_it_stix_settings": {
                "authentication": {},
                "ssl": {
                    "encoded_private_key": "encoded_private_key_value",
                    "ssl_certificate": "ssl_certificate_value",
                },
                "poll_service_uri": "poll_service_uri_value",
                "collection": "collection_value",
            },
            "threat_connect_ioc_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "owners": ["owners_value1", "owners_value2"],
            },
            "service_now_cmdb_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "feedname": "feedname_value",
            },
            "imperva_waf_settings": {"authentication": {}},
            "thinkst_canary_settings": {
                "authentication": {},
                "hostname": "hostname_value",
            },
            "rh_isac_ioc_settings": {
                "authentication": {
                    "token_endpoint": "token_endpoint_value",
                    "client_id": "client_id_value",
                    "client_secret": "client_secret_value",
                }
            },
            "rapid7_insight_settings": {
                "authentication": {},
                "endpoint": "endpoint_value",
                "hostname": "hostname_value",
            },
            "salesforce_settings": {
                "oauth_password_grant_auth": {
                    "token_endpoint": "token_endpoint_value",
                    "client_id": "client_id_value",
                    "client_secret": "client_secret_value",
                    "user": "user_value",
                    "password": "password_value",
                },
                "oauth_jwt_credentials": {
                    "rs_credentials": {"private_key": "private_key_value"},
                    "token_endpoint": "token_endpoint_value",
                    "claims": {
                        "issuer": "issuer_value",
                        "subject": "subject_value",
                        "audience": "audience_value",
                    },
                },
                "hostname": "hostname_value",
            },
            "netskope_alert_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "feedname": "feedname_value",
                "content_type": "content_type_value",
            },
            "azure_mdm_intune_settings": {
                "authentication": {},
                "tenant_id": "tenant_id_value",
                "hostname": "hostname_value",
                "auth_endpoint": "auth_endpoint_value",
            },
            "azure_ad_settings": {
                "authentication": {},
                "tenant_id": "tenant_id_value",
                "hostname": "hostname_value",
                "auth_endpoint": "auth_endpoint_value",
            },
            "proofpoint_on_demand_settings": {
                "authentication": {},
                "cluster_id": "cluster_id_value",
            },
            "workspace_users_settings": {
                "authentication": {},
                "workspace_customer_id": "workspace_customer_id_value",
                "projection_type": 1,
            },
            "workspace_activity_settings": {
                "authentication": {},
                "workspace_customer_id": "workspace_customer_id_value",
                "applications": ["applications_value1", "applications_value2"],
            },
            "workspace_alerts_settings": {
                "authentication": {},
                "workspace_customer_id": "workspace_customer_id_value",
            },
            "workspace_privileges_settings": {
                "authentication": {},
                "workspace_customer_id": "workspace_customer_id_value",
            },
            "workspace_mobile_settings": {
                "authentication": {},
                "workspace_customer_id": "workspace_customer_id_value",
            },
            "workspace_chrome_os_settings": {
                "authentication": {},
                "workspace_customer_id": "workspace_customer_id_value",
            },
            "workspace_groups_settings": {
                "authentication": {},
                "workspace_customer_id": "workspace_customer_id_value",
            },
            "azure_ad_audit_settings": {
                "authentication": {},
                "tenant_id": "tenant_id_value",
                "hostname": "hostname_value",
                "auth_endpoint": "auth_endpoint_value",
            },
            "symantec_event_export_settings": {
                "authentication": {
                    "token_endpoint": "token_endpoint_value",
                    "client_id": "client_id_value",
                    "client_secret": "client_secret_value",
                    "refresh_token": "refresh_token_value",
                }
            },
            "qualys_vm_settings": {"authentication": {}, "hostname": "hostname_value"},
            "pan_prisma_cloud_settings": {
                "authentication": {"user": "user_value", "password": "password_value"},
                "hostname": "hostname_value",
            },
            "gcs_settings": {
                "bucket_uri": "bucket_uri_value",
                "source_type": 1,
                "source_deletion_option": 1,
                "chronicle_service_account": "chronicle_service_account_value",
            },
            "http_settings": {
                "uri": "uri_value",
                "source_type": 1,
                "source_deletion_option": 1,
            },
            "sftp_settings": {
                "authentication": {
                    "username": "username_value",
                    "password": "password_value",
                    "private_key": "private_key_value",
                    "private_key_passphrase": "private_key_passphrase_value",
                },
                "uri": "uri_value",
                "source_type": 1,
                "source_deletion_option": 1,
            },
            "amazon_s3_settings": {
                "authentication": {
                    "access_key_id": "access_key_id_value",
                    "secret_access_key": "secret_access_key_value",
                    "client_id": "client_id_value",
                    "client_secret": "client_secret_value",
                    "refresh_uri": "refresh_uri_value",
                    "region": 1,
                },
                "s3_uri": "s3_uri_value",
                "source_type": 1,
                "source_deletion_option": 1,
            },
            "azure_blob_store_settings": {
                "authentication": {
                    "shared_key": "shared_key_value",
                    "sas_token": "sas_token_value",
                },
                "azure_uri": "azure_uri_value",
                "source_type": 1,
                "source_deletion_option": 1,
            },
            "amazon_sqs_settings": {
                "region": 1,
                "queue": "queue_value",
                "account_number": "account_number_value",
                "authentication": {
                    "sqs_access_key_secret_auth": {
                        "access_key_id": "access_key_id_value",
                        "secret_access_key": "secret_access_key_value",
                    },
                    "additional_s3_access_key_secret_auth": {
                        "access_key_id": "access_key_id_value",
                        "secret_access_key": "secret_access_key_value",
                    },
                },
                "source_deletion_option": 1,
            },
            "google_cloud_identity_devices_settings": {
                "authentication": {},
                "api_version": "api_version_value",
            },
            "google_cloud_identity_device_users_settings": {"authentication": {}},
            "crowdstrike_detects_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "ingestion_type": 1,
            },
            "mandiant_ioc_settings": {
                "authentication": {},
                "start_time": {"seconds": 751, "nanos": 543},
            },
            "sentinelone_alert_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "initial_start_time": "initial_start_time_value",
                "is_alert_api_subscribed": True,
            },
            "qualys_scan_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "api_type": 1,
            },
            "pubsub_settings": {
                "google_service_account_email": "google_service_account_email_value"
            },
            "amazon_kinesis_firehose_settings": {},
            "webhook_settings": {},
            "dummy_log_type_settings": {
                "authentication": {},
                "api_endpoint": "api_endpoint_value",
            },
            "https_push_google_cloud_pubsub_settings": {
                "split_delimiter": "split_delimiter_value"
            },
            "https_push_amazon_kinesis_firehose_settings": {
                "split_delimiter": "split_delimiter_value"
            },
            "https_push_webhook_settings": {"split_delimiter": "split_delimiter_value"},
            "aws_ec2_hosts_settings": {"authentication": {}},
            "aws_ec2_instances_settings": {"authentication": {}},
            "aws_ec2_vpcs_settings": {"authentication": {}},
            "aws_iam_settings": {"authentication": {}, "api_type": 1},
            "netskope_alert_v2_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "content_category": "content_category_value",
                "content_types": ["content_types_value1", "content_types_value2"],
            },
            "gcs_v2_settings": {
                "bucket_uri": "bucket_uri_value",
                "source_deletion_option": 1,
                "chronicle_service_account": "chronicle_service_account_value",
                "max_lookback_days": 1787,
                "include_prefixes": [
                    "include_prefixes_value1",
                    "include_prefixes_value2",
                ],
            },
            "amazon_s3_v2_settings": {
                "authentication": {
                    "access_key_secret_auth": {
                        "access_key_id": "access_key_id_value",
                        "secret_access_key": "secret_access_key_value",
                    },
                    "aws_iam_role_auth": {
                        "aws_iam_role_arn": "aws_iam_role_arn_value",
                        "subject_id": "subject_id_value",
                    },
                },
                "s3_uri": "s3_uri_value",
                "source_deletion_option": 1,
                "max_lookback_days": 1787,
                "chronicle_service_account": "chronicle_service_account_value",
                "include_prefixes": [
                    "include_prefixes_value1",
                    "include_prefixes_value2",
                ],
            },
            "amazon_sqs_v2_settings": {
                "queue": "queue_value",
                "s3_uri": "s3_uri_value",
                "authentication": {
                    "sqs_v2_access_key_secret_auth": {
                        "access_key_id": "access_key_id_value",
                        "secret_access_key": "secret_access_key_value",
                    },
                    "aws_iam_role_auth": {
                        "aws_iam_role_arn": "aws_iam_role_arn_value",
                        "subject_id": "subject_id_value",
                    },
                },
                "source_deletion_option": 1,
                "max_lookback_days": 1787,
                "chronicle_service_account": "chronicle_service_account_value",
                "include_prefixes": [
                    "include_prefixes_value1",
                    "include_prefixes_value2",
                ],
            },
            "azure_event_hub_settings": {
                "name": "name_value",
                "consumer_group": "consumer_group_value",
                "event_hub_connection_string": "event_hub_connection_string_value",
                "azure_storage_connection_string": "azure_storage_connection_string_value",
                "azure_storage_container": "azure_storage_container_value",
                "azure_sas_token": "azure_sas_token_value",
                "event_hub_namespace": "event_hub_namespace_value",
            },
            "trellix_hx_hosts_settings": {
                "authentication": {
                    "msso": {
                        "username": "username_value",
                        "password": "password_value",
                        "api_endpoint": "api_endpoint_value",
                    },
                    "trellix_iam": {
                        "client_id": "client_id_value",
                        "client_secret": "client_secret_value",
                        "scope": "scope_value",
                    },
                    "trellix_local": {
                        "username": "username_value",
                        "password": "password_value",
                        "token_endpoint": "token_endpoint_value",
                        "token_header": "token_header_value",
                    },
                },
                "endpoint": "endpoint_value",
            },
            "azure_blob_store_v2_settings": {
                "azure_uri": "azure_uri_value",
                "authentication": {
                    "access_key": "access_key_value",
                    "sas_token": "sas_token_value",
                    "azure_v2_workload_identity_federation": {
                        "client_id": "client_id_value",
                        "tenant_id": "tenant_id_value",
                        "subject_id": "subject_id_value",
                    },
                },
                "source_deletion_option": 1,
                "max_lookback_days": 1787,
                "chronicle_service_account": "chronicle_service_account_value",
                "include_prefixes": [
                    "include_prefixes_value1",
                    "include_prefixes_value2",
                ],
            },
            "trellix_hx_alerts_settings": {
                "authentication": {},
                "endpoint": "endpoint_value",
            },
            "google_cloud_storage_event_driven_settings": {
                "bucket_uri": "bucket_uri_value",
                "pubsub_subscription": "pubsub_subscription_value",
                "source_deletion_option": 1,
                "chronicle_service_account": "chronicle_service_account_value",
                "max_lookback_days": 1787,
                "include_prefixes": [
                    "include_prefixes_value1",
                    "include_prefixes_value2",
                ],
            },
            "crowdstrike_alerts_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "ingestion_type": 1,
            },
            "trellix_hx_bulk_acqs_settings": {
                "authentication": {},
                "endpoint": "endpoint_value",
            },
            "mimecast_mail_v2_settings": {
                "auth_credentials": {
                    "client_id": "client_id_value",
                    "client_secret": "client_secret_value",
                }
            },
            "threat_connect_ioc_v3_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "owners": ["owners_value1", "owners_value2"],
                "tql_query": "tql_query_value",
                "fields": ["fields_value1", "fields_value2"],
                "schedule": 845,
            },
            "custom_api_settings": {
                "no_auth": {},
                "basic_auth": {},
                "oauth_client_credentials": {},
                "header_auth": {
                    "header_key_values": [{"key": "key_value", "value": "value_value"}]
                },
                "query_auth": {
                    "query_key_values": [{"key": "key_value", "value": "value_value"}]
                },
                "base_url": "base_url_value",
                "polling_frequency": 1830,
                "primary_request": {
                    "request_settings": {
                        "endpoint_path": "endpoint_path_value",
                        "http_method": 1,
                        "request_body": "request_body_value",
                        "query_parameters": {},
                        "custom_headers": {},
                        "max_requests_per_minute": 2488,
                    },
                    "response_mapping": {
                        "target_data_path": [
                            "target_data_path_value1",
                            "target_data_path_value2",
                        ]
                    },
                    "pagination_strategy": {
                        "none": {},
                        "token": {
                            "next_page_token_json_path": "next_page_token_json_path_value",
                            "query_param": "query_param_value",
                        },
                        "link": {
                            "next_page_link_json_path": "next_page_link_json_path_value"
                        },
                        "offset": {"offset_query_param": "offset_query_param_value"},
                        "page_number": {
                            "page_number_query_param": "page_number_query_param_value"
                        },
                    },
                    "checkpointing": {
                        "none_strategy": {},
                        "latest_timestamp_strategy": {
                            "checkpoint_value_path": "checkpoint_value_path_value",
                            "checkpoint_variable": "checkpoint_variable_value",
                        },
                        "latest_record_strategy": {
                            "checkpoint_value_path": "checkpoint_value_path_value",
                            "checkpoint_variable": "checkpoint_variable_value",
                        },
                        "iterator_strategy": {
                            "checkpoint_value_path": "checkpoint_value_path_value",
                            "checkpoint_variable": "checkpoint_variable_value",
                        },
                    },
                    "dependent_requests_config": {
                        "item_id_json_path": "item_id_json_path_value",
                        "item_id_variable": "item_id_variable_value",
                        "dependent_requests": {},
                    },
                },
            },
            "feed_source_type": 1,
            "log_type": "log_type_value",
            "asset_namespace": "asset_namespace_value",
            "labels": {},
            "sts_migration_readiness": 1,
            "last_v2_migration_attempt_time": {},
        },
        "state": 1,
        "failure_msg": "failure_msg_value",
        "read_only": True,
        "last_feed_initiation_time": {},
        "failure_details": {
            "error_code": "error_code_value",
            "http_error_code": 1603,
            "error_cause": "error_cause_value",
            "error_action": "error_action_value",
        },
        "reference_id": "reference_id_value",
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = gcc_feed.CreateFeedRequest.meta.fields["feed"]

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
    for field, value in request_init["feed"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["feed"][field])):
                    del request_init["feed"][field][i][subfield]
            else:
                del request_init["feed"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcc_feed.Feed(
            name="name_value",
            uid="uid_value",
            display_name="display_name_value",
            state=gcc_feed.Feed.State.ACTIVE,
            failure_msg="failure_msg_value",
            read_only=True,
            reference_id="reference_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gcc_feed.Feed.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_feed(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcc_feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == gcc_feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_feed_rest_interceptors(null_interceptor):
    transport = transports.FeedsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FeedsServiceRestInterceptor(),
    )
    client = FeedsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_create_feed"
        ) as post,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_create_feed_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "pre_create_feed"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gcc_feed.CreateFeedRequest.pb(gcc_feed.CreateFeedRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = gcc_feed.Feed.to_json(gcc_feed.Feed())
        req.return_value.content = return_value

        request = gcc_feed.CreateFeedRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gcc_feed.Feed()
        post_with_metadata.return_value = gcc_feed.Feed(), metadata

        client.create_feed(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_feed_rest_bad_request(request_type=feed.GetFeedRequest):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
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
        client.get_feed(request)


@pytest.mark.parametrize(
    "request_type",
    [
        feed.GetFeedRequest,
        dict,
    ],
)
def test_get_feed_rest_call_success(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.Feed(
            name="name_value",
            uid="uid_value",
            display_name="display_name_value",
            state=feed.Feed.State.ACTIVE,
            failure_msg="failure_msg_value",
            read_only=True,
            reference_id="reference_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = feed.Feed.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_feed(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_feed_rest_interceptors(null_interceptor):
    transport = transports.FeedsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FeedsServiceRestInterceptor(),
    )
    client = FeedsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_get_feed"
        ) as post,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_get_feed_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "pre_get_feed"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = feed.GetFeedRequest.pb(feed.GetFeedRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = feed.Feed.to_json(feed.Feed())
        req.return_value.content = return_value

        request = feed.GetFeedRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = feed.Feed()
        post_with_metadata.return_value = feed.Feed(), metadata

        client.get_feed(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_feed_rest_bad_request(request_type=feed.DeleteFeedRequest):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
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
        client.delete_feed(request)


@pytest.mark.parametrize(
    "request_type",
    [
        feed.DeleteFeedRequest,
        dict,
    ],
)
def test_delete_feed_rest_call_success(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = ""
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.delete_feed(request)

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_feed_rest_interceptors(null_interceptor):
    transport = transports.FeedsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FeedsServiceRestInterceptor(),
    )
    client = FeedsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "pre_delete_feed"
        ) as pre,
    ):
        pre.assert_not_called()
        pb_message = feed.DeleteFeedRequest.pb(feed.DeleteFeedRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        request = feed.DeleteFeedRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata

        client.delete_feed(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()


def test_enable_feed_rest_bad_request(request_type=feed.EnableFeedRequest):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
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
        client.enable_feed(request)


@pytest.mark.parametrize(
    "request_type",
    [
        feed.EnableFeedRequest,
        dict,
    ],
)
def test_enable_feed_rest_call_success(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.Feed(
            name="name_value",
            uid="uid_value",
            display_name="display_name_value",
            state=feed.Feed.State.ACTIVE,
            failure_msg="failure_msg_value",
            read_only=True,
            reference_id="reference_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = feed.Feed.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.enable_feed(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_enable_feed_rest_interceptors(null_interceptor):
    transport = transports.FeedsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FeedsServiceRestInterceptor(),
    )
    client = FeedsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_enable_feed"
        ) as post,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_enable_feed_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "pre_enable_feed"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = feed.EnableFeedRequest.pb(feed.EnableFeedRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = feed.Feed.to_json(feed.Feed())
        req.return_value.content = return_value

        request = feed.EnableFeedRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = feed.Feed()
        post_with_metadata.return_value = feed.Feed(), metadata

        client.enable_feed(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_disable_feed_rest_bad_request(request_type=feed.DisableFeedRequest):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
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
        client.disable_feed(request)


@pytest.mark.parametrize(
    "request_type",
    [
        feed.DisableFeedRequest,
        dict,
    ],
)
def test_disable_feed_rest_call_success(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.Feed(
            name="name_value",
            uid="uid_value",
            display_name="display_name_value",
            state=feed.Feed.State.ACTIVE,
            failure_msg="failure_msg_value",
            read_only=True,
            reference_id="reference_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = feed.Feed.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.disable_feed(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_disable_feed_rest_interceptors(null_interceptor):
    transport = transports.FeedsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FeedsServiceRestInterceptor(),
    )
    client = FeedsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_disable_feed"
        ) as post,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_disable_feed_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "pre_disable_feed"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = feed.DisableFeedRequest.pb(feed.DisableFeedRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = feed.Feed.to_json(feed.Feed())
        req.return_value.content = return_value

        request = feed.DisableFeedRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = feed.Feed()
        post_with_metadata.return_value = feed.Feed(), metadata

        client.disable_feed(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_feeds_rest_bad_request(request_type=feed.ListFeedsRequest):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/instances/sample3"}
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
        client.list_feeds(request)


@pytest.mark.parametrize(
    "request_type",
    [
        feed.ListFeedsRequest,
        dict,
    ],
)
def test_list_feeds_rest_call_success(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/instances/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.ListFeedsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = feed.ListFeedsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_feeds(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFeedsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_feeds_rest_interceptors(null_interceptor):
    transport = transports.FeedsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FeedsServiceRestInterceptor(),
    )
    client = FeedsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_list_feeds"
        ) as post,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_list_feeds_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "pre_list_feeds"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = feed.ListFeedsRequest.pb(feed.ListFeedsRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = feed.ListFeedsResponse.to_json(feed.ListFeedsResponse())
        req.return_value.content = return_value

        request = feed.ListFeedsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = feed.ListFeedsResponse()
        post_with_metadata.return_value = feed.ListFeedsResponse(), metadata

        client.list_feeds(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_feed_packs_rest_bad_request(request_type=feed.ListFeedPacksRequest):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/instances/sample3"}
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
        client.list_feed_packs(request)


@pytest.mark.parametrize(
    "request_type",
    [
        feed.ListFeedPacksRequest,
        dict,
    ],
)
def test_list_feed_packs_rest_call_success(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/instances/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.ListFeedPacksResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = feed.ListFeedPacksResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_feed_packs(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFeedPacksPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_feed_packs_rest_interceptors(null_interceptor):
    transport = transports.FeedsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FeedsServiceRestInterceptor(),
    )
    client = FeedsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_list_feed_packs"
        ) as post,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_list_feed_packs_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "pre_list_feed_packs"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = feed.ListFeedPacksRequest.pb(feed.ListFeedPacksRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = feed.ListFeedPacksResponse.to_json(feed.ListFeedPacksResponse())
        req.return_value.content = return_value

        request = feed.ListFeedPacksRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = feed.ListFeedPacksResponse()
        post_with_metadata.return_value = feed.ListFeedPacksResponse(), metadata

        client.list_feed_packs(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_feed_pack_rest_bad_request(request_type=feed.GetFeedPackRequest):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/feedPacks/sample4"
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
        client.get_feed_pack(request)


@pytest.mark.parametrize(
    "request_type",
    [
        feed.GetFeedPackRequest,
        dict,
    ],
)
def test_get_feed_pack_rest_call_success(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/feedPacks/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.FeedPack(
            name="name_value",
            display_name="display_name_value",
            description="description_value",
            icon=b"icon_blob",
            categories=["categories_value"],
            pack_type=feed.FeedPack.PackType.PRODUCT_BASED,
            hidden=True,
            pack_documentation="pack_documentation_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = feed.FeedPack.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_feed_pack(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.FeedPack)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.description == "description_value"
    assert response.icon == b"icon_blob"
    assert response.categories == ["categories_value"]
    assert response.pack_type == feed.FeedPack.PackType.PRODUCT_BASED
    assert response.hidden is True
    assert response.pack_documentation == "pack_documentation_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_feed_pack_rest_interceptors(null_interceptor):
    transport = transports.FeedsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FeedsServiceRestInterceptor(),
    )
    client = FeedsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_get_feed_pack"
        ) as post,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_get_feed_pack_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "pre_get_feed_pack"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = feed.GetFeedPackRequest.pb(feed.GetFeedPackRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = feed.FeedPack.to_json(feed.FeedPack())
        req.return_value.content = return_value

        request = feed.GetFeedPackRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = feed.FeedPack()
        post_with_metadata.return_value = feed.FeedPack(), metadata

        client.get_feed_pack(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_feed_rest_bad_request(request_type=gcc_feed.UpdateFeedRequest):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "feed": {
            "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
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
        client.update_feed(request)


@pytest.mark.parametrize(
    "request_type",
    [
        gcc_feed.UpdateFeedRequest,
        dict,
    ],
)
def test_update_feed_rest_call_success(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "feed": {
            "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
        }
    }
    request_init["feed"] = {
        "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4",
        "uid": "uid_value",
        "display_name": "display_name_value",
        "details": {
            "anomali_settings": {
                "authentication": {"user": "user_value", "secret": "secret_value"},
                "hostname": "hostname_value",
            },
            "azure_ad_context_settings": {
                "authentication": {
                    "client_id": "client_id_value",
                    "client_secret": "client_secret_value",
                },
                "retrieve_devices": True,
                "retrieve_groups": True,
                "tenant_id": "tenant_id_value",
                "hostname": "hostname_value",
                "auth_endpoint": "auth_endpoint_value",
            },
            "cloud_passage_settings": {
                "authentication": {},
                "event_types": ["event_types_value1", "event_types_value2"],
            },
            "cortex_xdr_settings": {
                "authentication": {
                    "header_key_values": [{"key": "key_value", "value": "value_value"}]
                },
                "hostname": "hostname_value",
                "endpoint": "endpoint_value",
            },
            "duo_auth_settings": {"authentication": {}, "hostname": "hostname_value"},
            "duo_user_context_settings": {
                "authentication": {},
                "hostname": "hostname_value",
            },
            "microsoft_graph_alert_settings": {
                "authentication": {},
                "tenant_id": "tenant_id_value",
                "hostname": "hostname_value",
                "auth_endpoint": "auth_endpoint_value",
            },
            "microsoft_security_center_alert_settings": {
                "authentication": {},
                "subscription_id": "subscription_id_value",
                "tenant_id": "tenant_id_value",
                "hostname": "hostname_value",
                "auth_endpoint": "auth_endpoint_value",
            },
            "mimecast_mail_settings": {
                "authentication": {},
                "hostname": "hostname_value",
            },
            "office365_settings": {
                "authentication": {},
                "tenant_id": "tenant_id_value",
                "content_type": 1,
                "hostname": "hostname_value",
                "auth_endpoint": "auth_endpoint_value",
            },
            "proofpoint_mail_settings": {"authentication": {}},
            "recorded_future_ioc_settings": {"authentication": {}},
            "workday_settings": {
                "authentication": {
                    "user": "user_value",
                    "secret": "secret_value",
                    "token_endpoint": "token_endpoint_value",
                    "client_id": "client_id_value",
                    "client_secret": "client_secret_value",
                    "refresh_token": "refresh_token_value",
                },
                "hostname": "hostname_value",
                "tenant_id": "tenant_id_value",
            },
            "pan_ioc_settings": {
                "authentication": {},
                "feed_id": "feed_id_value",
                "feed": "feed_value",
            },
            "okta_settings": {"authentication": {}, "hostname": "hostname_value"},
            "okta_user_context_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "manager_id_reference_field": "manager_id_reference_field_value",
            },
            "fox_it_stix_settings": {
                "authentication": {},
                "ssl": {
                    "encoded_private_key": "encoded_private_key_value",
                    "ssl_certificate": "ssl_certificate_value",
                },
                "poll_service_uri": "poll_service_uri_value",
                "collection": "collection_value",
            },
            "threat_connect_ioc_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "owners": ["owners_value1", "owners_value2"],
            },
            "service_now_cmdb_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "feedname": "feedname_value",
            },
            "imperva_waf_settings": {"authentication": {}},
            "thinkst_canary_settings": {
                "authentication": {},
                "hostname": "hostname_value",
            },
            "rh_isac_ioc_settings": {
                "authentication": {
                    "token_endpoint": "token_endpoint_value",
                    "client_id": "client_id_value",
                    "client_secret": "client_secret_value",
                }
            },
            "rapid7_insight_settings": {
                "authentication": {},
                "endpoint": "endpoint_value",
                "hostname": "hostname_value",
            },
            "salesforce_settings": {
                "oauth_password_grant_auth": {
                    "token_endpoint": "token_endpoint_value",
                    "client_id": "client_id_value",
                    "client_secret": "client_secret_value",
                    "user": "user_value",
                    "password": "password_value",
                },
                "oauth_jwt_credentials": {
                    "rs_credentials": {"private_key": "private_key_value"},
                    "token_endpoint": "token_endpoint_value",
                    "claims": {
                        "issuer": "issuer_value",
                        "subject": "subject_value",
                        "audience": "audience_value",
                    },
                },
                "hostname": "hostname_value",
            },
            "netskope_alert_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "feedname": "feedname_value",
                "content_type": "content_type_value",
            },
            "azure_mdm_intune_settings": {
                "authentication": {},
                "tenant_id": "tenant_id_value",
                "hostname": "hostname_value",
                "auth_endpoint": "auth_endpoint_value",
            },
            "azure_ad_settings": {
                "authentication": {},
                "tenant_id": "tenant_id_value",
                "hostname": "hostname_value",
                "auth_endpoint": "auth_endpoint_value",
            },
            "proofpoint_on_demand_settings": {
                "authentication": {},
                "cluster_id": "cluster_id_value",
            },
            "workspace_users_settings": {
                "authentication": {},
                "workspace_customer_id": "workspace_customer_id_value",
                "projection_type": 1,
            },
            "workspace_activity_settings": {
                "authentication": {},
                "workspace_customer_id": "workspace_customer_id_value",
                "applications": ["applications_value1", "applications_value2"],
            },
            "workspace_alerts_settings": {
                "authentication": {},
                "workspace_customer_id": "workspace_customer_id_value",
            },
            "workspace_privileges_settings": {
                "authentication": {},
                "workspace_customer_id": "workspace_customer_id_value",
            },
            "workspace_mobile_settings": {
                "authentication": {},
                "workspace_customer_id": "workspace_customer_id_value",
            },
            "workspace_chrome_os_settings": {
                "authentication": {},
                "workspace_customer_id": "workspace_customer_id_value",
            },
            "workspace_groups_settings": {
                "authentication": {},
                "workspace_customer_id": "workspace_customer_id_value",
            },
            "azure_ad_audit_settings": {
                "authentication": {},
                "tenant_id": "tenant_id_value",
                "hostname": "hostname_value",
                "auth_endpoint": "auth_endpoint_value",
            },
            "symantec_event_export_settings": {
                "authentication": {
                    "token_endpoint": "token_endpoint_value",
                    "client_id": "client_id_value",
                    "client_secret": "client_secret_value",
                    "refresh_token": "refresh_token_value",
                }
            },
            "qualys_vm_settings": {"authentication": {}, "hostname": "hostname_value"},
            "pan_prisma_cloud_settings": {
                "authentication": {"user": "user_value", "password": "password_value"},
                "hostname": "hostname_value",
            },
            "gcs_settings": {
                "bucket_uri": "bucket_uri_value",
                "source_type": 1,
                "source_deletion_option": 1,
                "chronicle_service_account": "chronicle_service_account_value",
            },
            "http_settings": {
                "uri": "uri_value",
                "source_type": 1,
                "source_deletion_option": 1,
            },
            "sftp_settings": {
                "authentication": {
                    "username": "username_value",
                    "password": "password_value",
                    "private_key": "private_key_value",
                    "private_key_passphrase": "private_key_passphrase_value",
                },
                "uri": "uri_value",
                "source_type": 1,
                "source_deletion_option": 1,
            },
            "amazon_s3_settings": {
                "authentication": {
                    "access_key_id": "access_key_id_value",
                    "secret_access_key": "secret_access_key_value",
                    "client_id": "client_id_value",
                    "client_secret": "client_secret_value",
                    "refresh_uri": "refresh_uri_value",
                    "region": 1,
                },
                "s3_uri": "s3_uri_value",
                "source_type": 1,
                "source_deletion_option": 1,
            },
            "azure_blob_store_settings": {
                "authentication": {
                    "shared_key": "shared_key_value",
                    "sas_token": "sas_token_value",
                },
                "azure_uri": "azure_uri_value",
                "source_type": 1,
                "source_deletion_option": 1,
            },
            "amazon_sqs_settings": {
                "region": 1,
                "queue": "queue_value",
                "account_number": "account_number_value",
                "authentication": {
                    "sqs_access_key_secret_auth": {
                        "access_key_id": "access_key_id_value",
                        "secret_access_key": "secret_access_key_value",
                    },
                    "additional_s3_access_key_secret_auth": {
                        "access_key_id": "access_key_id_value",
                        "secret_access_key": "secret_access_key_value",
                    },
                },
                "source_deletion_option": 1,
            },
            "google_cloud_identity_devices_settings": {
                "authentication": {},
                "api_version": "api_version_value",
            },
            "google_cloud_identity_device_users_settings": {"authentication": {}},
            "crowdstrike_detects_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "ingestion_type": 1,
            },
            "mandiant_ioc_settings": {
                "authentication": {},
                "start_time": {"seconds": 751, "nanos": 543},
            },
            "sentinelone_alert_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "initial_start_time": "initial_start_time_value",
                "is_alert_api_subscribed": True,
            },
            "qualys_scan_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "api_type": 1,
            },
            "pubsub_settings": {
                "google_service_account_email": "google_service_account_email_value"
            },
            "amazon_kinesis_firehose_settings": {},
            "webhook_settings": {},
            "dummy_log_type_settings": {
                "authentication": {},
                "api_endpoint": "api_endpoint_value",
            },
            "https_push_google_cloud_pubsub_settings": {
                "split_delimiter": "split_delimiter_value"
            },
            "https_push_amazon_kinesis_firehose_settings": {
                "split_delimiter": "split_delimiter_value"
            },
            "https_push_webhook_settings": {"split_delimiter": "split_delimiter_value"},
            "aws_ec2_hosts_settings": {"authentication": {}},
            "aws_ec2_instances_settings": {"authentication": {}},
            "aws_ec2_vpcs_settings": {"authentication": {}},
            "aws_iam_settings": {"authentication": {}, "api_type": 1},
            "netskope_alert_v2_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "content_category": "content_category_value",
                "content_types": ["content_types_value1", "content_types_value2"],
            },
            "gcs_v2_settings": {
                "bucket_uri": "bucket_uri_value",
                "source_deletion_option": 1,
                "chronicle_service_account": "chronicle_service_account_value",
                "max_lookback_days": 1787,
                "include_prefixes": [
                    "include_prefixes_value1",
                    "include_prefixes_value2",
                ],
            },
            "amazon_s3_v2_settings": {
                "authentication": {
                    "access_key_secret_auth": {
                        "access_key_id": "access_key_id_value",
                        "secret_access_key": "secret_access_key_value",
                    },
                    "aws_iam_role_auth": {
                        "aws_iam_role_arn": "aws_iam_role_arn_value",
                        "subject_id": "subject_id_value",
                    },
                },
                "s3_uri": "s3_uri_value",
                "source_deletion_option": 1,
                "max_lookback_days": 1787,
                "chronicle_service_account": "chronicle_service_account_value",
                "include_prefixes": [
                    "include_prefixes_value1",
                    "include_prefixes_value2",
                ],
            },
            "amazon_sqs_v2_settings": {
                "queue": "queue_value",
                "s3_uri": "s3_uri_value",
                "authentication": {
                    "sqs_v2_access_key_secret_auth": {
                        "access_key_id": "access_key_id_value",
                        "secret_access_key": "secret_access_key_value",
                    },
                    "aws_iam_role_auth": {
                        "aws_iam_role_arn": "aws_iam_role_arn_value",
                        "subject_id": "subject_id_value",
                    },
                },
                "source_deletion_option": 1,
                "max_lookback_days": 1787,
                "chronicle_service_account": "chronicle_service_account_value",
                "include_prefixes": [
                    "include_prefixes_value1",
                    "include_prefixes_value2",
                ],
            },
            "azure_event_hub_settings": {
                "name": "name_value",
                "consumer_group": "consumer_group_value",
                "event_hub_connection_string": "event_hub_connection_string_value",
                "azure_storage_connection_string": "azure_storage_connection_string_value",
                "azure_storage_container": "azure_storage_container_value",
                "azure_sas_token": "azure_sas_token_value",
                "event_hub_namespace": "event_hub_namespace_value",
            },
            "trellix_hx_hosts_settings": {
                "authentication": {
                    "msso": {
                        "username": "username_value",
                        "password": "password_value",
                        "api_endpoint": "api_endpoint_value",
                    },
                    "trellix_iam": {
                        "client_id": "client_id_value",
                        "client_secret": "client_secret_value",
                        "scope": "scope_value",
                    },
                    "trellix_local": {
                        "username": "username_value",
                        "password": "password_value",
                        "token_endpoint": "token_endpoint_value",
                        "token_header": "token_header_value",
                    },
                },
                "endpoint": "endpoint_value",
            },
            "azure_blob_store_v2_settings": {
                "azure_uri": "azure_uri_value",
                "authentication": {
                    "access_key": "access_key_value",
                    "sas_token": "sas_token_value",
                    "azure_v2_workload_identity_federation": {
                        "client_id": "client_id_value",
                        "tenant_id": "tenant_id_value",
                        "subject_id": "subject_id_value",
                    },
                },
                "source_deletion_option": 1,
                "max_lookback_days": 1787,
                "chronicle_service_account": "chronicle_service_account_value",
                "include_prefixes": [
                    "include_prefixes_value1",
                    "include_prefixes_value2",
                ],
            },
            "trellix_hx_alerts_settings": {
                "authentication": {},
                "endpoint": "endpoint_value",
            },
            "google_cloud_storage_event_driven_settings": {
                "bucket_uri": "bucket_uri_value",
                "pubsub_subscription": "pubsub_subscription_value",
                "source_deletion_option": 1,
                "chronicle_service_account": "chronicle_service_account_value",
                "max_lookback_days": 1787,
                "include_prefixes": [
                    "include_prefixes_value1",
                    "include_prefixes_value2",
                ],
            },
            "crowdstrike_alerts_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "ingestion_type": 1,
            },
            "trellix_hx_bulk_acqs_settings": {
                "authentication": {},
                "endpoint": "endpoint_value",
            },
            "mimecast_mail_v2_settings": {
                "auth_credentials": {
                    "client_id": "client_id_value",
                    "client_secret": "client_secret_value",
                }
            },
            "threat_connect_ioc_v3_settings": {
                "authentication": {},
                "hostname": "hostname_value",
                "owners": ["owners_value1", "owners_value2"],
                "tql_query": "tql_query_value",
                "fields": ["fields_value1", "fields_value2"],
                "schedule": 845,
            },
            "custom_api_settings": {
                "no_auth": {},
                "basic_auth": {},
                "oauth_client_credentials": {},
                "header_auth": {
                    "header_key_values": [{"key": "key_value", "value": "value_value"}]
                },
                "query_auth": {
                    "query_key_values": [{"key": "key_value", "value": "value_value"}]
                },
                "base_url": "base_url_value",
                "polling_frequency": 1830,
                "primary_request": {
                    "request_settings": {
                        "endpoint_path": "endpoint_path_value",
                        "http_method": 1,
                        "request_body": "request_body_value",
                        "query_parameters": {},
                        "custom_headers": {},
                        "max_requests_per_minute": 2488,
                    },
                    "response_mapping": {
                        "target_data_path": [
                            "target_data_path_value1",
                            "target_data_path_value2",
                        ]
                    },
                    "pagination_strategy": {
                        "none": {},
                        "token": {
                            "next_page_token_json_path": "next_page_token_json_path_value",
                            "query_param": "query_param_value",
                        },
                        "link": {
                            "next_page_link_json_path": "next_page_link_json_path_value"
                        },
                        "offset": {"offset_query_param": "offset_query_param_value"},
                        "page_number": {
                            "page_number_query_param": "page_number_query_param_value"
                        },
                    },
                    "checkpointing": {
                        "none_strategy": {},
                        "latest_timestamp_strategy": {
                            "checkpoint_value_path": "checkpoint_value_path_value",
                            "checkpoint_variable": "checkpoint_variable_value",
                        },
                        "latest_record_strategy": {
                            "checkpoint_value_path": "checkpoint_value_path_value",
                            "checkpoint_variable": "checkpoint_variable_value",
                        },
                        "iterator_strategy": {
                            "checkpoint_value_path": "checkpoint_value_path_value",
                            "checkpoint_variable": "checkpoint_variable_value",
                        },
                    },
                    "dependent_requests_config": {
                        "item_id_json_path": "item_id_json_path_value",
                        "item_id_variable": "item_id_variable_value",
                        "dependent_requests": {},
                    },
                },
            },
            "feed_source_type": 1,
            "log_type": "log_type_value",
            "asset_namespace": "asset_namespace_value",
            "labels": {},
            "sts_migration_readiness": 1,
            "last_v2_migration_attempt_time": {},
        },
        "state": 1,
        "failure_msg": "failure_msg_value",
        "read_only": True,
        "last_feed_initiation_time": {},
        "failure_details": {
            "error_code": "error_code_value",
            "http_error_code": 1603,
            "error_cause": "error_cause_value",
            "error_action": "error_action_value",
        },
        "reference_id": "reference_id_value",
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = gcc_feed.UpdateFeedRequest.meta.fields["feed"]

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
    for field, value in request_init["feed"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["feed"][field])):
                    del request_init["feed"][field][i][subfield]
            else:
                del request_init["feed"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcc_feed.Feed(
            name="name_value",
            uid="uid_value",
            display_name="display_name_value",
            state=gcc_feed.Feed.State.ACTIVE,
            failure_msg="failure_msg_value",
            read_only=True,
            reference_id="reference_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gcc_feed.Feed.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_feed(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcc_feed.Feed)
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.display_name == "display_name_value"
    assert response.state == gcc_feed.Feed.State.ACTIVE
    assert response.failure_msg == "failure_msg_value"
    assert response.read_only is True
    assert response.reference_id == "reference_id_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_feed_rest_interceptors(null_interceptor):
    transport = transports.FeedsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FeedsServiceRestInterceptor(),
    )
    client = FeedsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_update_feed"
        ) as post,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_update_feed_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "pre_update_feed"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gcc_feed.UpdateFeedRequest.pb(gcc_feed.UpdateFeedRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = gcc_feed.Feed.to_json(gcc_feed.Feed())
        req.return_value.content = return_value

        request = gcc_feed.UpdateFeedRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gcc_feed.Feed()
        post_with_metadata.return_value = gcc_feed.Feed(), metadata

        client.update_feed(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_feed_source_type_schemas_rest_bad_request(
    request_type=feed.ListFeedSourceTypeSchemasRequest,
):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/instances/sample3"}
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
        client.list_feed_source_type_schemas(request)


@pytest.mark.parametrize(
    "request_type",
    [
        feed.ListFeedSourceTypeSchemasRequest,
        dict,
    ],
)
def test_list_feed_source_type_schemas_rest_call_success(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2/instances/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.ListFeedSourceTypeSchemasResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = feed.ListFeedSourceTypeSchemasResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_feed_source_type_schemas(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFeedSourceTypeSchemasPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_feed_source_type_schemas_rest_interceptors(null_interceptor):
    transport = transports.FeedsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FeedsServiceRestInterceptor(),
    )
    client = FeedsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_list_feed_source_type_schemas"
        ) as post,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor,
            "post_list_feed_source_type_schemas_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "pre_list_feed_source_type_schemas"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = feed.ListFeedSourceTypeSchemasRequest.pb(
            feed.ListFeedSourceTypeSchemasRequest()
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
        return_value = feed.ListFeedSourceTypeSchemasResponse.to_json(
            feed.ListFeedSourceTypeSchemasResponse()
        )
        req.return_value.content = return_value

        request = feed.ListFeedSourceTypeSchemasRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = feed.ListFeedSourceTypeSchemasResponse()
        post_with_metadata.return_value = (
            feed.ListFeedSourceTypeSchemasResponse(),
            metadata,
        )

        client.list_feed_source_type_schemas(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_log_type_schemas_rest_bad_request(
    request_type=feed.ListLogTypeSchemasRequest,
):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "parent": "projects/sample1/locations/sample2/instances/sample3/feedSourceTypeSchemas/sample4"
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
        client.list_log_type_schemas(request)


@pytest.mark.parametrize(
    "request_type",
    [
        feed.ListLogTypeSchemasRequest,
        dict,
    ],
)
def test_list_log_type_schemas_rest_call_success(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "parent": "projects/sample1/locations/sample2/instances/sample3/feedSourceTypeSchemas/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.ListLogTypeSchemasResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = feed.ListLogTypeSchemasResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_log_type_schemas(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListLogTypeSchemasPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_log_type_schemas_rest_interceptors(null_interceptor):
    transport = transports.FeedsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FeedsServiceRestInterceptor(),
    )
    client = FeedsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_list_log_type_schemas"
        ) as post,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor,
            "post_list_log_type_schemas_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "pre_list_log_type_schemas"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = feed.ListLogTypeSchemasRequest.pb(feed.ListLogTypeSchemasRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = feed.ListLogTypeSchemasResponse.to_json(
            feed.ListLogTypeSchemasResponse()
        )
        req.return_value.content = return_value

        request = feed.ListLogTypeSchemasRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = feed.ListLogTypeSchemasResponse()
        post_with_metadata.return_value = feed.ListLogTypeSchemasResponse(), metadata

        client.list_log_type_schemas(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_import_push_logs_rest_bad_request(request_type=feed.ImportPushLogsRequest):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "parent": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
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
        client.import_push_logs(request)


@pytest.mark.parametrize(
    "request_type",
    [
        feed.ImportPushLogsRequest,
        dict,
    ],
)
def test_import_push_logs_rest_call_success(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "parent": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = httpbody_pb2.HttpBody(
            content_type="content_type_value",
            data=b"data_blob",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.import_push_logs(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, httpbody_pb2.HttpBody)
    assert response.content_type == "content_type_value"
    assert response.data == b"data_blob"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_import_push_logs_rest_interceptors(null_interceptor):
    transport = transports.FeedsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FeedsServiceRestInterceptor(),
    )
    client = FeedsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_import_push_logs"
        ) as post,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor,
            "post_import_push_logs_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "pre_import_push_logs"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = feed.ImportPushLogsRequest.pb(feed.ImportPushLogsRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = json_format.MessageToJson(httpbody_pb2.HttpBody())
        req.return_value.content = return_value

        request = feed.ImportPushLogsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = httpbody_pb2.HttpBody()
        post_with_metadata.return_value = httpbody_pb2.HttpBody(), metadata

        client.import_push_logs(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_generate_secret_rest_bad_request(request_type=feed.GenerateSecretRequest):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
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
        client.generate_secret(request)


@pytest.mark.parametrize(
    "request_type",
    [
        feed.GenerateSecretRequest,
        dict,
    ],
)
def test_generate_secret_rest_call_success(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/feeds/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = feed.GenerateSecretResponse(
            secret="secret_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = feed.GenerateSecretResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.generate_secret(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, feed.GenerateSecretResponse)
    assert response.secret == "secret_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_generate_secret_rest_interceptors(null_interceptor):
    transport = transports.FeedsServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.FeedsServiceRestInterceptor(),
    )
    client = FeedsServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_generate_secret"
        ) as post,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "post_generate_secret_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.FeedsServiceRestInterceptor, "pre_generate_secret"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = feed.GenerateSecretRequest.pb(feed.GenerateSecretRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = feed.GenerateSecretResponse.to_json(
            feed.GenerateSecretResponse()
        )
        req.return_value.content = return_value

        request = feed.GenerateSecretRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = feed.GenerateSecretResponse()
        post_with_metadata.return_value = feed.GenerateSecretResponse(), metadata

        client.generate_secret(
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
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict(
        {
            "name": "projects/sample1/locations/sample2/instances/sample3/operations/sample4"
        },
        request,
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
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/operations/sample4"
    }
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


def test_delete_operation_rest_bad_request(
    request_type=operations_pb2.DeleteOperationRequest,
):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict(
        {
            "name": "projects/sample1/locations/sample2/instances/sample3/operations/sample4"
        },
        request,
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
        client.delete_operation(request)


@pytest.mark.parametrize(
    "request_type",
    [
        operations_pb2.DeleteOperationRequest,
        dict,
    ],
)
def test_delete_operation_rest(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/operations/sample4"
    }
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

        response = client.delete_operation(request)

    # Establish that the response is the type that we expect.
    assert response is None


def test_get_operation_rest_bad_request(
    request_type=operations_pb2.GetOperationRequest,
):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict(
        {
            "name": "projects/sample1/locations/sample2/instances/sample3/operations/sample4"
        },
        request,
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
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {
        "name": "projects/sample1/locations/sample2/instances/sample3/operations/sample4"
    }
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
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict(
        {"name": "projects/sample1/locations/sample2/instances/sample3"}, request
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
        client.list_operations(request)


@pytest.mark.parametrize(
    "request_type",
    [
        operations_pb2.ListOperationsRequest,
        dict,
    ],
)
def test_list_operations_rest(request_type):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {"name": "projects/sample1/locations/sample2/instances/sample3"}
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
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fetch_service_account_for_customer_empty_call_rest():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_service_account_for_customer), "__call__"
    ) as call:
        client.fetch_service_account_for_customer(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.FetchServiceAccountForCustomerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_feed_empty_call_rest():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_feed), "__call__") as call:
        client.create_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_feed.CreateFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_feed_empty_call_rest():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_feed), "__call__") as call:
        client.get_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.GetFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_feed_empty_call_rest():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.delete_feed), "__call__") as call:
        client.delete_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.DeleteFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_enable_feed_empty_call_rest():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.enable_feed), "__call__") as call:
        client.enable_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.EnableFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_disable_feed_empty_call_rest():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.disable_feed), "__call__") as call:
        client.disable_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.DisableFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_feeds_empty_call_rest():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_feeds), "__call__") as call:
        client.list_feeds(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListFeedsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_feed_packs_empty_call_rest():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_feed_packs), "__call__") as call:
        client.list_feed_packs(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListFeedPacksRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_feed_pack_empty_call_rest():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_feed_pack), "__call__") as call:
        client.get_feed_pack(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.GetFeedPackRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_feed_empty_call_rest():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_feed), "__call__") as call:
        client.update_feed(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gcc_feed.UpdateFeedRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_feed_source_type_schemas_empty_call_rest():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_feed_source_type_schemas), "__call__"
    ) as call:
        client.list_feed_source_type_schemas(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListFeedSourceTypeSchemasRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_log_type_schemas_empty_call_rest():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_log_type_schemas), "__call__"
    ) as call:
        client.list_log_type_schemas(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ListLogTypeSchemasRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_import_push_logs_empty_call_rest():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.import_push_logs), "__call__") as call:
        client.import_push_logs(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.ImportPushLogsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_generate_secret_empty_call_rest():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.generate_secret), "__call__") as call:
        client.generate_secret(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = feed.GenerateSecretRequest()
        assert args[0] == request_msg


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.FeedsServiceGrpcTransport,
    )


def test_feeds_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.FeedsServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_feeds_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.chronicle_v1.services.feeds_service.transports.FeedsServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.FeedsServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "fetch_service_account_for_customer",
        "create_feed",
        "get_feed",
        "delete_feed",
        "enable_feed",
        "disable_feed",
        "list_feeds",
        "list_feed_packs",
        "get_feed_pack",
        "update_feed",
        "list_feed_source_type_schemas",
        "list_log_type_schemas",
        "import_push_logs",
        "generate_secret",
        "get_operation",
        "cancel_operation",
        "delete_operation",
        "list_operations",
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


def test_feeds_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.cloud.chronicle_v1.services.feeds_service.transports.FeedsServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.FeedsServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/chronicle",
                "https://www.googleapis.com/auth/chronicle.readonly",
                "https://www.googleapis.com/auth/cloud-platform",
            ),
            quota_project_id="octopus",
        )


def test_feeds_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.cloud.chronicle_v1.services.feeds_service.transports.FeedsServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.FeedsServiceTransport()
        adc.assert_called_once()


def test_feeds_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        FeedsServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/chronicle",
                "https://www.googleapis.com/auth/chronicle.readonly",
                "https://www.googleapis.com/auth/cloud-platform",
            ),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.FeedsServiceGrpcTransport,
        transports.FeedsServiceGrpcAsyncIOTransport,
    ],
)
def test_feeds_service_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(
                "https://www.googleapis.com/auth/chronicle",
                "https://www.googleapis.com/auth/chronicle.readonly",
                "https://www.googleapis.com/auth/cloud-platform",
            ),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.FeedsServiceGrpcTransport,
        transports.FeedsServiceGrpcAsyncIOTransport,
        transports.FeedsServiceRestTransport,
    ],
)
def test_feeds_service_transport_auth_gdch_credentials(transport_class):
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
        (transports.FeedsServiceGrpcTransport, grpc_helpers),
        (transports.FeedsServiceGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_feeds_service_transport_create_channel(transport_class, grpc_helpers):
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
            "chronicle.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
                "https://www.googleapis.com/auth/chronicle",
                "https://www.googleapis.com/auth/chronicle.readonly",
                "https://www.googleapis.com/auth/cloud-platform",
            ),
            scopes=["1", "2"],
            default_host="chronicle.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [transports.FeedsServiceGrpcTransport, transports.FeedsServiceGrpcAsyncIOTransport],
)
def test_feeds_service_grpc_transport_client_cert_source_for_mtls(transport_class):
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


def test_feeds_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.FeedsServiceRestTransport(
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
def test_feeds_service_host_no_port(transport_name):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="chronicle.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "chronicle.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://chronicle.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_feeds_service_host_with_port(transport_name):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="chronicle.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "chronicle.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://chronicle.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_feeds_service_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = FeedsServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = FeedsServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.fetch_service_account_for_customer._session
    session2 = client2.transport.fetch_service_account_for_customer._session
    assert session1 != session2
    session1 = client1.transport.create_feed._session
    session2 = client2.transport.create_feed._session
    assert session1 != session2
    session1 = client1.transport.get_feed._session
    session2 = client2.transport.get_feed._session
    assert session1 != session2
    session1 = client1.transport.delete_feed._session
    session2 = client2.transport.delete_feed._session
    assert session1 != session2
    session1 = client1.transport.enable_feed._session
    session2 = client2.transport.enable_feed._session
    assert session1 != session2
    session1 = client1.transport.disable_feed._session
    session2 = client2.transport.disable_feed._session
    assert session1 != session2
    session1 = client1.transport.list_feeds._session
    session2 = client2.transport.list_feeds._session
    assert session1 != session2
    session1 = client1.transport.list_feed_packs._session
    session2 = client2.transport.list_feed_packs._session
    assert session1 != session2
    session1 = client1.transport.get_feed_pack._session
    session2 = client2.transport.get_feed_pack._session
    assert session1 != session2
    session1 = client1.transport.update_feed._session
    session2 = client2.transport.update_feed._session
    assert session1 != session2
    session1 = client1.transport.list_feed_source_type_schemas._session
    session2 = client2.transport.list_feed_source_type_schemas._session
    assert session1 != session2
    session1 = client1.transport.list_log_type_schemas._session
    session2 = client2.transport.list_log_type_schemas._session
    assert session1 != session2
    session1 = client1.transport.import_push_logs._session
    session2 = client2.transport.import_push_logs._session
    assert session1 != session2
    session1 = client1.transport.generate_secret._session
    session2 = client2.transport.generate_secret._session
    assert session1 != session2


def test_feeds_service_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.FeedsServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_feeds_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.FeedsServiceGrpcAsyncIOTransport(
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
    [transports.FeedsServiceGrpcTransport, transports.FeedsServiceGrpcAsyncIOTransport],
)
def test_feeds_service_transport_channel_mtls_with_client_cert_source(transport_class):
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
    [transports.FeedsServiceGrpcTransport, transports.FeedsServiceGrpcAsyncIOTransport],
)
def test_feeds_service_transport_channel_mtls_with_adc(transport_class):
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


def test_feed_path():
    project = "squid"
    location = "clam"
    instance = "whelk"
    feed = "octopus"
    expected = "projects/{project}/locations/{location}/instances/{instance}/feeds/{feed}".format(
        project=project,
        location=location,
        instance=instance,
        feed=feed,
    )
    actual = FeedsServiceClient.feed_path(project, location, instance, feed)
    assert expected == actual


def test_parse_feed_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
        "instance": "cuttlefish",
        "feed": "mussel",
    }
    path = FeedsServiceClient.feed_path(**expected)

    # Check that the path construction is reversible.
    actual = FeedsServiceClient.parse_feed_path(path)
    assert expected == actual


def test_feed_pack_path():
    project = "winkle"
    location = "nautilus"
    instance = "scallop"
    feed_pack = "abalone"
    expected = "projects/{project}/locations/{location}/instances/{instance}/feedPacks/{feed_pack}".format(
        project=project,
        location=location,
        instance=instance,
        feed_pack=feed_pack,
    )
    actual = FeedsServiceClient.feed_pack_path(project, location, instance, feed_pack)
    assert expected == actual


def test_parse_feed_pack_path():
    expected = {
        "project": "squid",
        "location": "clam",
        "instance": "whelk",
        "feed_pack": "octopus",
    }
    path = FeedsServiceClient.feed_pack_path(**expected)

    # Check that the path construction is reversible.
    actual = FeedsServiceClient.parse_feed_pack_path(path)
    assert expected == actual


def test_feed_service_account_path():
    project = "oyster"
    location = "nudibranch"
    instance = "cuttlefish"
    feed_service_account = "mussel"
    expected = "projects/{project}/locations/{location}/instances/{instance}/feedServiceAccounts/{feed_service_account}".format(
        project=project,
        location=location,
        instance=instance,
        feed_service_account=feed_service_account,
    )
    actual = FeedsServiceClient.feed_service_account_path(
        project, location, instance, feed_service_account
    )
    assert expected == actual


def test_parse_feed_service_account_path():
    expected = {
        "project": "winkle",
        "location": "nautilus",
        "instance": "scallop",
        "feed_service_account": "abalone",
    }
    path = FeedsServiceClient.feed_service_account_path(**expected)

    # Check that the path construction is reversible.
    actual = FeedsServiceClient.parse_feed_service_account_path(path)
    assert expected == actual


def test_feed_source_type_schema_path():
    project = "squid"
    location = "clam"
    instance = "whelk"
    feed_source_type = "octopus"
    expected = "projects/{project}/locations/{location}/instances/{instance}/feedSourceTypeSchemas/{feed_source_type}".format(
        project=project,
        location=location,
        instance=instance,
        feed_source_type=feed_source_type,
    )
    actual = FeedsServiceClient.feed_source_type_schema_path(
        project, location, instance, feed_source_type
    )
    assert expected == actual


def test_parse_feed_source_type_schema_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
        "instance": "cuttlefish",
        "feed_source_type": "mussel",
    }
    path = FeedsServiceClient.feed_source_type_schema_path(**expected)

    # Check that the path construction is reversible.
    actual = FeedsServiceClient.parse_feed_source_type_schema_path(path)
    assert expected == actual


def test_log_type_path():
    project = "winkle"
    location = "nautilus"
    instance = "scallop"
    log_type = "abalone"
    expected = "projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}".format(
        project=project,
        location=location,
        instance=instance,
        log_type=log_type,
    )
    actual = FeedsServiceClient.log_type_path(project, location, instance, log_type)
    assert expected == actual


def test_parse_log_type_path():
    expected = {
        "project": "squid",
        "location": "clam",
        "instance": "whelk",
        "log_type": "octopus",
    }
    path = FeedsServiceClient.log_type_path(**expected)

    # Check that the path construction is reversible.
    actual = FeedsServiceClient.parse_log_type_path(path)
    assert expected == actual


def test_log_type_schema_path():
    project = "oyster"
    location = "nudibranch"
    instance = "cuttlefish"
    feed_source_type = "mussel"
    log_type = "winkle"
    expected = "projects/{project}/locations/{location}/instances/{instance}/feedSourceTypeSchemas/{feed_source_type}/logTypeSchemas/{log_type}".format(
        project=project,
        location=location,
        instance=instance,
        feed_source_type=feed_source_type,
        log_type=log_type,
    )
    actual = FeedsServiceClient.log_type_schema_path(
        project, location, instance, feed_source_type, log_type
    )
    assert expected == actual


def test_parse_log_type_schema_path():
    expected = {
        "project": "nautilus",
        "location": "scallop",
        "instance": "abalone",
        "feed_source_type": "squid",
        "log_type": "clam",
    }
    path = FeedsServiceClient.log_type_schema_path(**expected)

    # Check that the path construction is reversible.
    actual = FeedsServiceClient.parse_log_type_schema_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "whelk"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = FeedsServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "octopus",
    }
    path = FeedsServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = FeedsServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "oyster"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = FeedsServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "nudibranch",
    }
    path = FeedsServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = FeedsServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "cuttlefish"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = FeedsServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "mussel",
    }
    path = FeedsServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = FeedsServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "winkle"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = FeedsServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "nautilus",
    }
    path = FeedsServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = FeedsServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "scallop"
    location = "abalone"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = FeedsServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "squid",
        "location": "clam",
    }
    path = FeedsServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = FeedsServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.FeedsServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = FeedsServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.FeedsServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = FeedsServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_delete_operation(transport: str = "grpc"):
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
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
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = operations_pb2.DeleteOperationRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_operation(request)
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_operation_field_headers():
    client = FeedsServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.DeleteOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        call.return_value = None

        client.delete_operation(request)
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
async def test_delete_operation_field_headers_async():
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = operations_pb2.DeleteOperationRequest()
    request.name = "locations"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_operation(request)
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


def test_delete_operation_from_dict():
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_operation(
            request={
                "name": "locations",
            }
        )
        call.assert_called()


def test_delete_operation_flattened():
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )
    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.delete_operation), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_operation()
        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == operations_pb2.DeleteOperationRequest()


def test_cancel_operation(transport: str = "grpc"):
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
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
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
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
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
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
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
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
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
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
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
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
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
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
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
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
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
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
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
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
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
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
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
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
    client = FeedsServiceClient(
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
    client = FeedsServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = FeedsServiceClient(
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
        client = FeedsServiceClient(
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
        (FeedsServiceClient, transports.FeedsServiceGrpcTransport),
        (FeedsServiceAsyncClient, transports.FeedsServiceGrpcAsyncIOTransport),
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
