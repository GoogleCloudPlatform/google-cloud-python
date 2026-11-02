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
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
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

from google.ads.marketingplatform_admin_v1alpha.services.marketingplatform_admin_service import (
    MarketingplatformAdminServiceAsyncClient,
    MarketingplatformAdminServiceClient,
    pagers,
    transports,
)
from google.ads.marketingplatform_admin_v1alpha.types import (
    marketingplatform_admin,
    resources,
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

    assert (
        MarketingplatformAdminServiceClient._get_client_cert_source(None, False) is None
    )
    assert (
        MarketingplatformAdminServiceClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        MarketingplatformAdminServiceClient._get_client_cert_source(
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
                MarketingplatformAdminServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                MarketingplatformAdminServiceClient._get_client_cert_source(
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
    client = MarketingplatformAdminServiceClient(credentials=cred)
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
    client = MarketingplatformAdminServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (MarketingplatformAdminServiceClient, "grpc"),
        (MarketingplatformAdminServiceAsyncClient, "grpc_asyncio"),
        (MarketingplatformAdminServiceClient, "rest"),
    ],
)
def test_marketingplatform_admin_service_client_from_service_account_info(
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
            "marketingplatformadmin.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://marketingplatformadmin.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.MarketingplatformAdminServiceGrpcTransport, "grpc"),
        (transports.MarketingplatformAdminServiceGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.MarketingplatformAdminServiceRestTransport, "rest"),
    ],
)
def test_marketingplatform_admin_service_client_service_account_always_use_jwt(
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
        (MarketingplatformAdminServiceClient, "grpc"),
        (MarketingplatformAdminServiceAsyncClient, "grpc_asyncio"),
        (MarketingplatformAdminServiceClient, "rest"),
    ],
)
def test_marketingplatform_admin_service_client_from_service_account_file(
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
            "marketingplatformadmin.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://marketingplatformadmin.googleapis.com"
        )


def test_marketingplatform_admin_service_client_get_transport_class():
    transport = MarketingplatformAdminServiceClient.get_transport_class()
    available_transports = [
        transports.MarketingplatformAdminServiceGrpcTransport,
        transports.MarketingplatformAdminServiceRestTransport,
    ]
    assert transport in available_transports

    transport = MarketingplatformAdminServiceClient.get_transport_class("grpc")
    assert transport == transports.MarketingplatformAdminServiceGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            MarketingplatformAdminServiceClient,
            transports.MarketingplatformAdminServiceGrpcTransport,
            "grpc",
        ),
        (
            MarketingplatformAdminServiceAsyncClient,
            transports.MarketingplatformAdminServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            MarketingplatformAdminServiceClient,
            transports.MarketingplatformAdminServiceRestTransport,
            "rest",
        ),
    ],
)
@mock.patch.object(
    MarketingplatformAdminServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(MarketingplatformAdminServiceClient),
)
@mock.patch.object(
    MarketingplatformAdminServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(MarketingplatformAdminServiceAsyncClient),
)
def test_marketingplatform_admin_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(
        MarketingplatformAdminServiceClient, "get_transport_class"
    ) as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(
        MarketingplatformAdminServiceClient, "get_transport_class"
    ) as gtc:
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
            MarketingplatformAdminServiceClient,
            transports.MarketingplatformAdminServiceGrpcTransport,
            "grpc",
            "true",
        ),
        (
            MarketingplatformAdminServiceAsyncClient,
            transports.MarketingplatformAdminServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            MarketingplatformAdminServiceClient,
            transports.MarketingplatformAdminServiceGrpcTransport,
            "grpc",
            "false",
        ),
        (
            MarketingplatformAdminServiceAsyncClient,
            transports.MarketingplatformAdminServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (
            MarketingplatformAdminServiceClient,
            transports.MarketingplatformAdminServiceRestTransport,
            "rest",
            "true",
        ),
        (
            MarketingplatformAdminServiceClient,
            transports.MarketingplatformAdminServiceRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    MarketingplatformAdminServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(MarketingplatformAdminServiceClient),
)
@mock.patch.object(
    MarketingplatformAdminServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(MarketingplatformAdminServiceAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_marketingplatform_admin_service_client_mtls_env_auto(
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
    "client_class",
    [MarketingplatformAdminServiceClient, MarketingplatformAdminServiceAsyncClient],
)
@mock.patch.object(
    MarketingplatformAdminServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(MarketingplatformAdminServiceClient),
)
@mock.patch.object(
    MarketingplatformAdminServiceAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(MarketingplatformAdminServiceAsyncClient),
)
def test_marketingplatform_admin_service_client_get_mtls_endpoint_and_cert_source(
    client_class,
):
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
    "client_class",
    [MarketingplatformAdminServiceClient, MarketingplatformAdminServiceAsyncClient],
)
@mock.patch.object(
    MarketingplatformAdminServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(MarketingplatformAdminServiceClient),
)
@mock.patch.object(
    MarketingplatformAdminServiceAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(MarketingplatformAdminServiceAsyncClient),
)
def test_marketingplatform_admin_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = MarketingplatformAdminServiceClient._DEFAULT_UNIVERSE
    default_endpoint = (
        MarketingplatformAdminServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
            UNIVERSE_DOMAIN=default_universe
        )
    )
    mock_universe = "bar.com"
    mock_endpoint = (
        MarketingplatformAdminServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
            UNIVERSE_DOMAIN=mock_universe
        )
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
            MarketingplatformAdminServiceClient,
            transports.MarketingplatformAdminServiceGrpcTransport,
            "grpc",
        ),
        (
            MarketingplatformAdminServiceAsyncClient,
            transports.MarketingplatformAdminServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            MarketingplatformAdminServiceClient,
            transports.MarketingplatformAdminServiceRestTransport,
            "rest",
        ),
    ],
)
def test_marketingplatform_admin_service_client_client_options_scopes(
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
            MarketingplatformAdminServiceClient,
            transports.MarketingplatformAdminServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            MarketingplatformAdminServiceAsyncClient,
            transports.MarketingplatformAdminServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (
            MarketingplatformAdminServiceClient,
            transports.MarketingplatformAdminServiceRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_marketingplatform_admin_service_client_client_options_credentials_file(
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


def test_marketingplatform_admin_service_client_client_options_from_dict():
    with mock.patch(
        "google.ads.marketingplatform_admin_v1alpha.services.marketingplatform_admin_service.transports.MarketingplatformAdminServiceGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = MarketingplatformAdminServiceClient(
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
            MarketingplatformAdminServiceClient,
            transports.MarketingplatformAdminServiceGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            MarketingplatformAdminServiceAsyncClient,
            transports.MarketingplatformAdminServiceGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_marketingplatform_admin_service_client_create_channel_credentials_file(
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
            "marketingplatformadmin.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=(
                "https://www.googleapis.com/auth/marketingplatformadmin.analytics.read",
                "https://www.googleapis.com/auth/marketingplatformadmin.analytics.update",
            ),
            scopes=None,
            default_host="marketingplatformadmin.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.GetOrganizationRequest(),
        {},
    ],
)
def test_get_organization(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_organization), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Organization(
            name="name_value",
            display_name="display_name_value",
        )
        response = client.get_organization(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.GetOrganizationRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Organization)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"


def test_get_organization_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.GetOrganizationRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_organization), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_organization(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetOrganizationRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_organization_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_organization in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_organization] = (
            mock_rpc
        )
        request = {}
        client.get_organization(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_organization(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_organization_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_organization
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_organization
        ] = mock_rpc

        request = {}
        await client.get_organization(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_organization(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.GetOrganizationRequest(),
        {},
    ],
)
async def test_get_organization_async(request_type, transport: str = "grpc_asyncio"):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_organization), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Organization(
                name="name_value",
                display_name="display_name_value",
            )
        )
        response = await client.get_organization(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.GetOrganizationRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Organization)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"


def test_get_organization_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.GetOrganizationRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_organization), "__call__") as call:
        call.return_value = resources.Organization()
        client.get_organization(request)

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
async def test_get_organization_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.GetOrganizationRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_organization), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Organization()
        )
        await client.get_organization(request)

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


def test_get_organization_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_organization), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Organization()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_organization(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_organization_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_organization(
            marketingplatform_admin.GetOrganizationRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_organization_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_organization), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.Organization()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Organization()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_organization(
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
async def test_get_organization_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_organization(
            marketingplatform_admin.GetOrganizationRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListOrganizationsRequest(),
        {},
    ],
)
def test_list_organizations(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_organizations), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ListOrganizationsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_organizations(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.ListOrganizationsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOrganizationsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_organizations_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.ListOrganizationsRequest(
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_organizations), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_organizations(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListOrganizationsRequest(
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_organizations_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_organizations in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_organizations] = (
            mock_rpc
        )
        request = {}
        client.list_organizations(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_organizations(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_organizations_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_organizations
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_organizations
        ] = mock_rpc

        request = {}
        await client.list_organizations(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_organizations(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListOrganizationsRequest(),
        {},
    ],
)
async def test_list_organizations_async(request_type, transport: str = "grpc_asyncio"):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_organizations), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListOrganizationsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_organizations(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.ListOrganizationsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOrganizationsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_organizations_pager(transport_name: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_organizations), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                    resources.Organization(),
                    resources.Organization(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                    resources.Organization(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        pager = client.list_organizations(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.Organization) for i in results)


def test_list_organizations_pages(transport_name: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_organizations), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                    resources.Organization(),
                    resources.Organization(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                    resources.Organization(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_organizations(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_organizations_async_pager():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_organizations),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                    resources.Organization(),
                    resources.Organization(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                    resources.Organization(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_organizations(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, resources.Organization) for i in responses)


@pytest.mark.asyncio
async def test_list_organizations_async_pages():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_organizations),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                    resources.Organization(),
                    resources.Organization(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                    resources.Organization(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_organizations(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.FindSalesPartnerManagedClientsRequest(),
        {},
    ],
)
def test_find_sales_partner_managed_clients(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.find_sales_partner_managed_clients), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            marketingplatform_admin.FindSalesPartnerManagedClientsResponse()
        )
        response = client.find_sales_partner_managed_clients(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.FindSalesPartnerManagedClientsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, marketingplatform_admin.FindSalesPartnerManagedClientsResponse
    )


def test_find_sales_partner_managed_clients_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.FindSalesPartnerManagedClientsRequest(
        organization="organization_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.find_sales_partner_managed_clients), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.find_sales_partner_managed_clients(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.FindSalesPartnerManagedClientsRequest(
            organization="organization_value",
        )
        assert args[0] == request_msg


def test_find_sales_partner_managed_clients_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.find_sales_partner_managed_clients
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.find_sales_partner_managed_clients
        ] = mock_rpc
        request = {}
        client.find_sales_partner_managed_clients(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.find_sales_partner_managed_clients(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_find_sales_partner_managed_clients_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.find_sales_partner_managed_clients
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.find_sales_partner_managed_clients
        ] = mock_rpc

        request = {}
        await client.find_sales_partner_managed_clients(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.find_sales_partner_managed_clients(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.FindSalesPartnerManagedClientsRequest(),
        {},
    ],
)
async def test_find_sales_partner_managed_clients_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.find_sales_partner_managed_clients), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.FindSalesPartnerManagedClientsResponse()
        )
        response = await client.find_sales_partner_managed_clients(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.FindSalesPartnerManagedClientsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, marketingplatform_admin.FindSalesPartnerManagedClientsResponse
    )


def test_find_sales_partner_managed_clients_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.FindSalesPartnerManagedClientsRequest()

    request.organization = "organization_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.find_sales_partner_managed_clients), "__call__"
    ) as call:
        call.return_value = (
            marketingplatform_admin.FindSalesPartnerManagedClientsResponse()
        )
        client.find_sales_partner_managed_clients(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "organization=organization_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_find_sales_partner_managed_clients_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.FindSalesPartnerManagedClientsRequest()

    request.organization = "organization_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.find_sales_partner_managed_clients), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.FindSalesPartnerManagedClientsResponse()
        )
        await client.find_sales_partner_managed_clients(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "organization=organization_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListAnalyticsAccountLinksRequest(),
        {},
    ],
)
def test_list_analytics_account_links(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_analytics_account_links), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ListAnalyticsAccountLinksResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_analytics_account_links(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.ListAnalyticsAccountLinksRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListAnalyticsAccountLinksPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_analytics_account_links_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.ListAnalyticsAccountLinksRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_analytics_account_links), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_analytics_account_links(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListAnalyticsAccountLinksRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_analytics_account_links_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_analytics_account_links
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_analytics_account_links
        ] = mock_rpc
        request = {}
        client.list_analytics_account_links(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_analytics_account_links(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_analytics_account_links_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_analytics_account_links
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_analytics_account_links
        ] = mock_rpc

        request = {}
        await client.list_analytics_account_links(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_analytics_account_links(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListAnalyticsAccountLinksRequest(),
        {},
    ],
)
async def test_list_analytics_account_links_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_analytics_account_links), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_analytics_account_links(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.ListAnalyticsAccountLinksRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListAnalyticsAccountLinksAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_analytics_account_links_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.ListAnalyticsAccountLinksRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_analytics_account_links), "__call__"
    ) as call:
        call.return_value = marketingplatform_admin.ListAnalyticsAccountLinksResponse()
        client.list_analytics_account_links(request)

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
async def test_list_analytics_account_links_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.ListAnalyticsAccountLinksRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_analytics_account_links), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListAnalyticsAccountLinksResponse()
        )
        await client.list_analytics_account_links(request)

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


def test_list_analytics_account_links_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_analytics_account_links), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ListAnalyticsAccountLinksResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_analytics_account_links(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_analytics_account_links_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_analytics_account_links(
            marketingplatform_admin.ListAnalyticsAccountLinksRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_analytics_account_links_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_analytics_account_links), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ListAnalyticsAccountLinksResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListAnalyticsAccountLinksResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_analytics_account_links(
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
async def test_list_analytics_account_links_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_analytics_account_links(
            marketingplatform_admin.ListAnalyticsAccountLinksRequest(),
            parent="parent_value",
        )


def test_list_analytics_account_links_pager(transport_name: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_analytics_account_links), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
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
        pager = client.list_analytics_account_links(
            request={}, retry=retry, timeout=timeout
        )

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.AnalyticsAccountLink) for i in results)


def test_list_analytics_account_links_pages(transport_name: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_analytics_account_links), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_analytics_account_links(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_analytics_account_links_async_pager():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_analytics_account_links),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_analytics_account_links(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, resources.AnalyticsAccountLink) for i in responses)


@pytest.mark.asyncio
async def test_list_analytics_account_links_async_pages():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_analytics_account_links),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.list_analytics_account_links(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.CreateAnalyticsAccountLinkRequest(),
        {},
    ],
)
def test_create_analytics_account_link(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_analytics_account_link), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.AnalyticsAccountLink(
            name="name_value",
            analytics_account="analytics_account_value",
            display_name="display_name_value",
            link_verification_state=resources.LinkVerificationState.LINK_VERIFICATION_STATE_VERIFIED,
        )
        response = client.create_analytics_account_link(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.CreateAnalyticsAccountLinkRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.AnalyticsAccountLink)
    assert response.name == "name_value"
    assert response.analytics_account == "analytics_account_value"
    assert response.display_name == "display_name_value"
    assert (
        response.link_verification_state
        == resources.LinkVerificationState.LINK_VERIFICATION_STATE_VERIFIED
    )


def test_create_analytics_account_link_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.CreateAnalyticsAccountLinkRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_analytics_account_link), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_analytics_account_link(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateAnalyticsAccountLinkRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_create_analytics_account_link_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_analytics_account_link
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.create_analytics_account_link
        ] = mock_rpc
        request = {}
        client.create_analytics_account_link(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_analytics_account_link(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_analytics_account_link_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_analytics_account_link
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_analytics_account_link
        ] = mock_rpc

        request = {}
        await client.create_analytics_account_link(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.create_analytics_account_link(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.CreateAnalyticsAccountLinkRequest(),
        {},
    ],
)
async def test_create_analytics_account_link_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_analytics_account_link), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AnalyticsAccountLink(
                name="name_value",
                analytics_account="analytics_account_value",
                display_name="display_name_value",
                link_verification_state=resources.LinkVerificationState.LINK_VERIFICATION_STATE_VERIFIED,
            )
        )
        response = await client.create_analytics_account_link(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.CreateAnalyticsAccountLinkRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.AnalyticsAccountLink)
    assert response.name == "name_value"
    assert response.analytics_account == "analytics_account_value"
    assert response.display_name == "display_name_value"
    assert (
        response.link_verification_state
        == resources.LinkVerificationState.LINK_VERIFICATION_STATE_VERIFIED
    )


def test_create_analytics_account_link_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.CreateAnalyticsAccountLinkRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_analytics_account_link), "__call__"
    ) as call:
        call.return_value = resources.AnalyticsAccountLink()
        client.create_analytics_account_link(request)

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
async def test_create_analytics_account_link_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.CreateAnalyticsAccountLinkRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_analytics_account_link), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AnalyticsAccountLink()
        )
        await client.create_analytics_account_link(request)

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


def test_create_analytics_account_link_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_analytics_account_link), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.AnalyticsAccountLink()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_analytics_account_link(
            parent="parent_value",
            analytics_account_link=resources.AnalyticsAccountLink(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].analytics_account_link
        mock_val = resources.AnalyticsAccountLink(name="name_value")
        assert arg == mock_val


def test_create_analytics_account_link_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_analytics_account_link(
            marketingplatform_admin.CreateAnalyticsAccountLinkRequest(),
            parent="parent_value",
            analytics_account_link=resources.AnalyticsAccountLink(name="name_value"),
        )


@pytest.mark.asyncio
async def test_create_analytics_account_link_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_analytics_account_link), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.AnalyticsAccountLink()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AnalyticsAccountLink()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_analytics_account_link(
            parent="parent_value",
            analytics_account_link=resources.AnalyticsAccountLink(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].analytics_account_link
        mock_val = resources.AnalyticsAccountLink(name="name_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_analytics_account_link_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_analytics_account_link(
            marketingplatform_admin.CreateAnalyticsAccountLinkRequest(),
            parent="parent_value",
            analytics_account_link=resources.AnalyticsAccountLink(name="name_value"),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.DeleteAnalyticsAccountLinkRequest(),
        {},
    ],
)
def test_delete_analytics_account_link(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_analytics_account_link), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_analytics_account_link(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.DeleteAnalyticsAccountLinkRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_analytics_account_link_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.DeleteAnalyticsAccountLinkRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_analytics_account_link), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.delete_analytics_account_link(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.DeleteAnalyticsAccountLinkRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_delete_analytics_account_link_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_analytics_account_link
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.delete_analytics_account_link
        ] = mock_rpc
        request = {}
        client.delete_analytics_account_link(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_analytics_account_link(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_delete_analytics_account_link_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.delete_analytics_account_link
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.delete_analytics_account_link
        ] = mock_rpc

        request = {}
        await client.delete_analytics_account_link(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.delete_analytics_account_link(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.DeleteAnalyticsAccountLinkRequest(),
        {},
    ],
)
async def test_delete_analytics_account_link_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_analytics_account_link), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_analytics_account_link(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.DeleteAnalyticsAccountLinkRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_analytics_account_link_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.DeleteAnalyticsAccountLinkRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_analytics_account_link), "__call__"
    ) as call:
        call.return_value = None
        client.delete_analytics_account_link(request)

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
async def test_delete_analytics_account_link_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.DeleteAnalyticsAccountLinkRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_analytics_account_link), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_analytics_account_link(request)

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


def test_delete_analytics_account_link_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_analytics_account_link), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_analytics_account_link(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_analytics_account_link_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_analytics_account_link(
            marketingplatform_admin.DeleteAnalyticsAccountLinkRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_analytics_account_link_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_analytics_account_link), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_analytics_account_link(
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
async def test_delete_analytics_account_link_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_analytics_account_link(
            marketingplatform_admin.DeleteAnalyticsAccountLinkRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.SetPropertyServiceLevelRequest(),
        {},
    ],
)
def test_set_property_service_level(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.set_property_service_level), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.SetPropertyServiceLevelResponse()
        response = client.set_property_service_level(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.SetPropertyServiceLevelRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, marketingplatform_admin.SetPropertyServiceLevelResponse)


def test_set_property_service_level_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.SetPropertyServiceLevelRequest(
        analytics_account_link="analytics_account_link_value",
        analytics_property="analytics_property_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.set_property_service_level), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.set_property_service_level(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.SetPropertyServiceLevelRequest(
            analytics_account_link="analytics_account_link_value",
            analytics_property="analytics_property_value",
        )
        assert args[0] == request_msg


def test_set_property_service_level_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.set_property_service_level
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.set_property_service_level
        ] = mock_rpc
        request = {}
        client.set_property_service_level(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.set_property_service_level(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_set_property_service_level_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.set_property_service_level
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.set_property_service_level
        ] = mock_rpc

        request = {}
        await client.set_property_service_level(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.set_property_service_level(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.SetPropertyServiceLevelRequest(),
        {},
    ],
)
async def test_set_property_service_level_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.set_property_service_level), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.SetPropertyServiceLevelResponse()
        )
        response = await client.set_property_service_level(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.SetPropertyServiceLevelRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, marketingplatform_admin.SetPropertyServiceLevelResponse)


def test_set_property_service_level_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.SetPropertyServiceLevelRequest()

    request.analytics_account_link = "analytics_account_link_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.set_property_service_level), "__call__"
    ) as call:
        call.return_value = marketingplatform_admin.SetPropertyServiceLevelResponse()
        client.set_property_service_level(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "analytics_account_link=analytics_account_link_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_set_property_service_level_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.SetPropertyServiceLevelRequest()

    request.analytics_account_link = "analytics_account_link_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.set_property_service_level), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.SetPropertyServiceLevelResponse()
        )
        await client.set_property_service_level(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "analytics_account_link=analytics_account_link_value",
    ) in kw["metadata"]


def test_set_property_service_level_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.set_property_service_level), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.SetPropertyServiceLevelResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.set_property_service_level(
            analytics_account_link="analytics_account_link_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].analytics_account_link
        mock_val = "analytics_account_link_value"
        assert arg == mock_val


def test_set_property_service_level_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.set_property_service_level(
            marketingplatform_admin.SetPropertyServiceLevelRequest(),
            analytics_account_link="analytics_account_link_value",
        )


@pytest.mark.asyncio
async def test_set_property_service_level_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.set_property_service_level), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.SetPropertyServiceLevelResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.SetPropertyServiceLevelResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.set_property_service_level(
            analytics_account_link="analytics_account_link_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].analytics_account_link
        mock_val = "analytics_account_link_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_set_property_service_level_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.set_property_service_level(
            marketingplatform_admin.SetPropertyServiceLevelRequest(),
            analytics_account_link="analytics_account_link_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ReportPropertyUsageRequest(),
        {},
    ],
)
def test_report_property_usage(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.report_property_usage), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ReportPropertyUsageResponse()
        response = client.report_property_usage(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.ReportPropertyUsageRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, marketingplatform_admin.ReportPropertyUsageResponse)


def test_report_property_usage_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.ReportPropertyUsageRequest(
        organization="organization_value",
        month="month_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.report_property_usage), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.report_property_usage(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ReportPropertyUsageRequest(
            organization="organization_value",
            month="month_value",
        )
        assert args[0] == request_msg


def test_report_property_usage_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.report_property_usage
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.report_property_usage] = (
            mock_rpc
        )
        request = {}
        client.report_property_usage(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.report_property_usage(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_report_property_usage_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.report_property_usage
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.report_property_usage
        ] = mock_rpc

        request = {}
        await client.report_property_usage(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.report_property_usage(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ReportPropertyUsageRequest(),
        {},
    ],
)
async def test_report_property_usage_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.report_property_usage), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ReportPropertyUsageResponse()
        )
        response = await client.report_property_usage(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.ReportPropertyUsageRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, marketingplatform_admin.ReportPropertyUsageResponse)


def test_report_property_usage_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.ReportPropertyUsageRequest()

    request.organization = "organization_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.report_property_usage), "__call__"
    ) as call:
        call.return_value = marketingplatform_admin.ReportPropertyUsageResponse()
        client.report_property_usage(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "organization=organization_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_report_property_usage_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.ReportPropertyUsageRequest()

    request.organization = "organization_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.report_property_usage), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ReportPropertyUsageResponse()
        )
        await client.report_property_usage(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "organization=organization_value",
    ) in kw["metadata"]


def test_report_property_usage_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.report_property_usage), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ReportPropertyUsageResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.report_property_usage(
            organization="organization_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].organization
        mock_val = "organization_value"
        assert arg == mock_val


def test_report_property_usage_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.report_property_usage(
            marketingplatform_admin.ReportPropertyUsageRequest(),
            organization="organization_value",
        )


@pytest.mark.asyncio
async def test_report_property_usage_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.report_property_usage), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ReportPropertyUsageResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ReportPropertyUsageResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.report_property_usage(
            organization="organization_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].organization
        mock_val = "organization_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_report_property_usage_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.report_property_usage(
            marketingplatform_admin.ReportPropertyUsageRequest(),
            organization="organization_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.GetUserGroupRequest(),
        {},
    ],
)
def test_get_user_group(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_user_group), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroup(
            name="name_value",
            display_name="display_name_value",
            description="description_value",
        )
        response = client.get_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.GetUserGroupRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroup)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.description == "description_value"


def test_get_user_group_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.GetUserGroupRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_user_group), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_user_group(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetUserGroupRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_user_group_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_user_group in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_user_group] = mock_rpc
        request = {}
        client.get_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_user_group(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_user_group_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_user_group
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_user_group
        ] = mock_rpc

        request = {}
        await client.get_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_user_group(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.GetUserGroupRequest(),
        {},
    ],
)
async def test_get_user_group_async(request_type, transport: str = "grpc_asyncio"):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_user_group), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroup(
                name="name_value",
                display_name="display_name_value",
                description="description_value",
            )
        )
        response = await client.get_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.GetUserGroupRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroup)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.description == "description_value"


def test_get_user_group_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.GetUserGroupRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_user_group), "__call__") as call:
        call.return_value = resources.UserGroup()
        client.get_user_group(request)

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
async def test_get_user_group_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.GetUserGroupRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_user_group), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(resources.UserGroup())
        await client.get_user_group(request)

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


def test_get_user_group_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_user_group), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroup()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_user_group(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_user_group_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_user_group(
            marketingplatform_admin.GetUserGroupRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_user_group_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_user_group), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroup()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(resources.UserGroup())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_user_group(
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
async def test_get_user_group_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_user_group(
            marketingplatform_admin.GetUserGroupRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListUserGroupsRequest(),
        {},
    ],
)
def test_list_user_groups(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_user_groups), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ListUserGroupsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_user_groups(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.ListUserGroupsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListUserGroupsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_user_groups_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.ListUserGroupsRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_user_groups), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_user_groups(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListUserGroupsRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_user_groups_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_user_groups in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_user_groups] = (
            mock_rpc
        )
        request = {}
        client.list_user_groups(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_user_groups(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_user_groups_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_user_groups
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_user_groups
        ] = mock_rpc

        request = {}
        await client.list_user_groups(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_user_groups(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListUserGroupsRequest(),
        {},
    ],
)
async def test_list_user_groups_async(request_type, transport: str = "grpc_asyncio"):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_user_groups), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListUserGroupsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_user_groups(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.ListUserGroupsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListUserGroupsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_user_groups_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.ListUserGroupsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_user_groups), "__call__") as call:
        call.return_value = marketingplatform_admin.ListUserGroupsResponse()
        client.list_user_groups(request)

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
async def test_list_user_groups_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.ListUserGroupsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_user_groups), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListUserGroupsResponse()
        )
        await client.list_user_groups(request)

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


def test_list_user_groups_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_user_groups), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ListUserGroupsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_user_groups(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_user_groups_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_user_groups(
            marketingplatform_admin.ListUserGroupsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_user_groups_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_user_groups), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ListUserGroupsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListUserGroupsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_user_groups(
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
async def test_list_user_groups_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_user_groups(
            marketingplatform_admin.ListUserGroupsRequest(),
            parent="parent_value",
        )


def test_list_user_groups_pager(transport_name: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_user_groups), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                    resources.UserGroup(),
                    resources.UserGroup(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                    resources.UserGroup(),
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
        pager = client.list_user_groups(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.UserGroup) for i in results)


def test_list_user_groups_pages(transport_name: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_user_groups), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                    resources.UserGroup(),
                    resources.UserGroup(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                    resources.UserGroup(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_user_groups(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_user_groups_async_pager():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_groups), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                    resources.UserGroup(),
                    resources.UserGroup(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                    resources.UserGroup(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_user_groups(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, resources.UserGroup) for i in responses)


@pytest.mark.asyncio
async def test_list_user_groups_async_pages():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_groups), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                    resources.UserGroup(),
                    resources.UserGroup(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                    resources.UserGroup(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_user_groups(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.CreateUserGroupRequest(),
        {},
    ],
)
def test_create_user_group(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroup(
            name="name_value",
            display_name="display_name_value",
            description="description_value",
        )
        response = client.create_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.CreateUserGroupRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroup)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.description == "description_value"


def test_create_user_group_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.CreateUserGroupRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_user_group(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateUserGroupRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_create_user_group_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_user_group in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_user_group] = (
            mock_rpc
        )
        request = {}
        client.create_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_user_group(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_user_group_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_user_group
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_user_group
        ] = mock_rpc

        request = {}
        await client.create_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.create_user_group(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.CreateUserGroupRequest(),
        {},
    ],
)
async def test_create_user_group_async(request_type, transport: str = "grpc_asyncio"):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroup(
                name="name_value",
                display_name="display_name_value",
                description="description_value",
            )
        )
        response = await client.create_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.CreateUserGroupRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroup)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.description == "description_value"


def test_create_user_group_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.CreateUserGroupRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group), "__call__"
    ) as call:
        call.return_value = resources.UserGroup()
        client.create_user_group(request)

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
async def test_create_user_group_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.CreateUserGroupRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(resources.UserGroup())
        await client.create_user_group(request)

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


def test_create_user_group_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroup()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_user_group(
            parent="parent_value",
            user_group=resources.UserGroup(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].user_group
        mock_val = resources.UserGroup(name="name_value")
        assert arg == mock_val


def test_create_user_group_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_user_group(
            marketingplatform_admin.CreateUserGroupRequest(),
            parent="parent_value",
            user_group=resources.UserGroup(name="name_value"),
        )


@pytest.mark.asyncio
async def test_create_user_group_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroup()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(resources.UserGroup())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_user_group(
            parent="parent_value",
            user_group=resources.UserGroup(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].user_group
        mock_val = resources.UserGroup(name="name_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_user_group_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_user_group(
            marketingplatform_admin.CreateUserGroupRequest(),
            parent="parent_value",
            user_group=resources.UserGroup(name="name_value"),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.UpdateUserGroupRequest(),
        {},
    ],
)
def test_update_user_group(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroup(
            name="name_value",
            display_name="display_name_value",
            description="description_value",
        )
        response = client.update_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.UpdateUserGroupRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroup)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.description == "description_value"


def test_update_user_group_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.UpdateUserGroupRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_user_group(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.UpdateUserGroupRequest()
        assert args[0] == request_msg


def test_update_user_group_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_user_group in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_user_group] = (
            mock_rpc
        )
        request = {}
        client.update_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_user_group(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_user_group_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_user_group
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_user_group
        ] = mock_rpc

        request = {}
        await client.update_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_user_group(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.UpdateUserGroupRequest(),
        {},
    ],
)
async def test_update_user_group_async(request_type, transport: str = "grpc_asyncio"):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroup(
                name="name_value",
                display_name="display_name_value",
                description="description_value",
            )
        )
        response = await client.update_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.UpdateUserGroupRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroup)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.description == "description_value"


def test_update_user_group_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.UpdateUserGroupRequest()

    request.user_group.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group), "__call__"
    ) as call:
        call.return_value = resources.UserGroup()
        client.update_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "user_group.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_user_group_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.UpdateUserGroupRequest()

    request.user_group.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(resources.UserGroup())
        await client.update_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "user_group.name=name_value",
    ) in kw["metadata"]


def test_update_user_group_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroup()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_user_group(
            user_group=resources.UserGroup(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].user_group
        mock_val = resources.UserGroup(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_user_group_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_user_group(
            marketingplatform_admin.UpdateUserGroupRequest(),
            user_group=resources.UserGroup(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_user_group_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroup()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(resources.UserGroup())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_user_group(
            user_group=resources.UserGroup(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].user_group
        mock_val = resources.UserGroup(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_user_group_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_user_group(
            marketingplatform_admin.UpdateUserGroupRequest(),
            user_group=resources.UserGroup(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.DeleteUserGroupRequest(),
        {},
    ],
)
def test_delete_user_group(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.DeleteUserGroupRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_user_group_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.DeleteUserGroupRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.delete_user_group(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.DeleteUserGroupRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_delete_user_group_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_user_group in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_user_group] = (
            mock_rpc
        )
        request = {}
        client.delete_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_user_group(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_delete_user_group_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.delete_user_group
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.delete_user_group
        ] = mock_rpc

        request = {}
        await client.delete_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.delete_user_group(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.DeleteUserGroupRequest(),
        {},
    ],
)
async def test_delete_user_group_async(request_type, transport: str = "grpc_asyncio"):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.DeleteUserGroupRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_user_group_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.DeleteUserGroupRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group), "__call__"
    ) as call:
        call.return_value = None
        client.delete_user_group(request)

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
async def test_delete_user_group_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.DeleteUserGroupRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_user_group(request)

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


def test_delete_user_group_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_user_group(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_user_group_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_user_group(
            marketingplatform_admin.DeleteUserGroupRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_user_group_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_user_group(
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
async def test_delete_user_group_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_user_group(
            marketingplatform_admin.DeleteUserGroupRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.GetUserGroupMemberRequest(),
        {},
    ],
)
def test_get_user_group_member(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroupMember(
            name="name_value",
            membership_role=resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER,
            user_email="user_email_value",
        )
        response = client.get_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.GetUserGroupMemberRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroupMember)
    assert response.name == "name_value"
    assert (
        response.membership_role
        == resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER
    )


def test_get_user_group_member_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.GetUserGroupMemberRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_user_group_member), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_user_group_member(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetUserGroupMemberRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_user_group_member_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_user_group_member
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_user_group_member] = (
            mock_rpc
        )
        request = {}
        client.get_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_user_group_member(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_user_group_member_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_user_group_member
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_user_group_member
        ] = mock_rpc

        request = {}
        await client.get_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_user_group_member(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.GetUserGroupMemberRequest(),
        {},
    ],
)
async def test_get_user_group_member_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroupMember(
                name="name_value",
                membership_role=resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER,
            )
        )
        response = await client.get_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.GetUserGroupMemberRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroupMember)
    assert response.name == "name_value"
    assert (
        response.membership_role
        == resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER
    )


def test_get_user_group_member_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.GetUserGroupMemberRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_user_group_member), "__call__"
    ) as call:
        call.return_value = resources.UserGroupMember()
        client.get_user_group_member(request)

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
async def test_get_user_group_member_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.GetUserGroupMemberRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_user_group_member), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroupMember()
        )
        await client.get_user_group_member(request)

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


def test_get_user_group_member_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroupMember()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_user_group_member(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_user_group_member_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_user_group_member(
            marketingplatform_admin.GetUserGroupMemberRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_user_group_member_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroupMember()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroupMember()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_user_group_member(
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
async def test_get_user_group_member_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_user_group_member(
            marketingplatform_admin.GetUserGroupMemberRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListUserGroupMembersRequest(),
        {},
    ],
)
def test_list_user_group_members(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_group_members), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ListUserGroupMembersResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_user_group_members(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.ListUserGroupMembersRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListUserGroupMembersPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_user_group_members_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.ListUserGroupMembersRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_group_members), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_user_group_members(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListUserGroupMembersRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_user_group_members_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_user_group_members
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_user_group_members
        ] = mock_rpc
        request = {}
        client.list_user_group_members(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_user_group_members(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_user_group_members_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_user_group_members
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_user_group_members
        ] = mock_rpc

        request = {}
        await client.list_user_group_members(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_user_group_members(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListUserGroupMembersRequest(),
        {},
    ],
)
async def test_list_user_group_members_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_group_members), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListUserGroupMembersResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_user_group_members(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.ListUserGroupMembersRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListUserGroupMembersAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_user_group_members_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.ListUserGroupMembersRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_group_members), "__call__"
    ) as call:
        call.return_value = marketingplatform_admin.ListUserGroupMembersResponse()
        client.list_user_group_members(request)

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
async def test_list_user_group_members_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.ListUserGroupMembersRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_group_members), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListUserGroupMembersResponse()
        )
        await client.list_user_group_members(request)

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


def test_list_user_group_members_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_group_members), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ListUserGroupMembersResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_user_group_members(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_user_group_members_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_user_group_members(
            marketingplatform_admin.ListUserGroupMembersRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_user_group_members_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_group_members), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ListUserGroupMembersResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListUserGroupMembersResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_user_group_members(
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
async def test_list_user_group_members_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_user_group_members(
            marketingplatform_admin.ListUserGroupMembersRequest(),
            parent="parent_value",
        )


def test_list_user_group_members_pager(transport_name: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_group_members), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
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
        pager = client.list_user_group_members(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.UserGroupMember) for i in results)


def test_list_user_group_members_pages(transport_name: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_group_members), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_user_group_members(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_user_group_members_async_pager():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_group_members),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_user_group_members(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, resources.UserGroupMember) for i in responses)


@pytest.mark.asyncio
async def test_list_user_group_members_async_pages():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_group_members),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_user_group_members(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.CreateUserGroupMemberRequest(),
        {},
    ],
)
def test_create_user_group_member(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroupMember(
            name="name_value",
            membership_role=resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER,
            user_email="user_email_value",
        )
        response = client.create_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.CreateUserGroupMemberRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroupMember)
    assert response.name == "name_value"
    assert (
        response.membership_role
        == resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER
    )


def test_create_user_group_member_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.CreateUserGroupMemberRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group_member), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_user_group_member(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateUserGroupMemberRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_create_user_group_member_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_user_group_member
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.create_user_group_member
        ] = mock_rpc
        request = {}
        client.create_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_user_group_member(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_user_group_member_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_user_group_member
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_user_group_member
        ] = mock_rpc

        request = {}
        await client.create_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.create_user_group_member(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.CreateUserGroupMemberRequest(),
        {},
    ],
)
async def test_create_user_group_member_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroupMember(
                name="name_value",
                membership_role=resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER,
            )
        )
        response = await client.create_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.CreateUserGroupMemberRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroupMember)
    assert response.name == "name_value"
    assert (
        response.membership_role
        == resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER
    )


def test_create_user_group_member_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.CreateUserGroupMemberRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group_member), "__call__"
    ) as call:
        call.return_value = resources.UserGroupMember()
        client.create_user_group_member(request)

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
async def test_create_user_group_member_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.CreateUserGroupMemberRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group_member), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroupMember()
        )
        await client.create_user_group_member(request)

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


def test_create_user_group_member_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroupMember()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_user_group_member(
            parent="parent_value",
            user_group_member=resources.UserGroupMember(user_email="user_email_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].user_group_member
        mock_val = resources.UserGroupMember(user_email="user_email_value")
        assert arg == mock_val


def test_create_user_group_member_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_user_group_member(
            marketingplatform_admin.CreateUserGroupMemberRequest(),
            parent="parent_value",
            user_group_member=resources.UserGroupMember(user_email="user_email_value"),
        )


@pytest.mark.asyncio
async def test_create_user_group_member_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroupMember()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroupMember()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_user_group_member(
            parent="parent_value",
            user_group_member=resources.UserGroupMember(user_email="user_email_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].user_group_member
        mock_val = resources.UserGroupMember(user_email="user_email_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_user_group_member_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_user_group_member(
            marketingplatform_admin.CreateUserGroupMemberRequest(),
            parent="parent_value",
            user_group_member=resources.UserGroupMember(user_email="user_email_value"),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.UpdateUserGroupMemberRequest(),
        {},
    ],
)
def test_update_user_group_member(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroupMember(
            name="name_value",
            membership_role=resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER,
            user_email="user_email_value",
        )
        response = client.update_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.UpdateUserGroupMemberRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroupMember)
    assert response.name == "name_value"
    assert (
        response.membership_role
        == resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER
    )


def test_update_user_group_member_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.UpdateUserGroupMemberRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group_member), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_user_group_member(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.UpdateUserGroupMemberRequest()
        assert args[0] == request_msg


def test_update_user_group_member_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_user_group_member
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_user_group_member
        ] = mock_rpc
        request = {}
        client.update_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_user_group_member(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_user_group_member_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_user_group_member
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_user_group_member
        ] = mock_rpc

        request = {}
        await client.update_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_user_group_member(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.UpdateUserGroupMemberRequest(),
        {},
    ],
)
async def test_update_user_group_member_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroupMember(
                name="name_value",
                membership_role=resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER,
            )
        )
        response = await client.update_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.UpdateUserGroupMemberRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroupMember)
    assert response.name == "name_value"
    assert (
        response.membership_role
        == resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER
    )


def test_update_user_group_member_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.UpdateUserGroupMemberRequest()

    request.user_group_member.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group_member), "__call__"
    ) as call:
        call.return_value = resources.UserGroupMember()
        client.update_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "user_group_member.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_user_group_member_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.UpdateUserGroupMemberRequest()

    request.user_group_member.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group_member), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroupMember()
        )
        await client.update_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "user_group_member.name=name_value",
    ) in kw["metadata"]


def test_update_user_group_member_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroupMember()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_user_group_member(
            user_group_member=resources.UserGroupMember(user_email="user_email_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].user_group_member
        mock_val = resources.UserGroupMember(user_email="user_email_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_user_group_member_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_user_group_member(
            marketingplatform_admin.UpdateUserGroupMemberRequest(),
            user_group_member=resources.UserGroupMember(user_email="user_email_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_user_group_member_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.UserGroupMember()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroupMember()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_user_group_member(
            user_group_member=resources.UserGroupMember(user_email="user_email_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].user_group_member
        mock_val = resources.UserGroupMember(user_email="user_email_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_user_group_member_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_user_group_member(
            marketingplatform_admin.UpdateUserGroupMemberRequest(),
            user_group_member=resources.UserGroupMember(user_email="user_email_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.DeleteUserGroupMemberRequest(),
        {},
    ],
)
def test_delete_user_group_member(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.DeleteUserGroupMemberRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_user_group_member_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.DeleteUserGroupMemberRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group_member), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.delete_user_group_member(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.DeleteUserGroupMemberRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_delete_user_group_member_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_user_group_member
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.delete_user_group_member
        ] = mock_rpc
        request = {}
        client.delete_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_user_group_member(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_delete_user_group_member_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.delete_user_group_member
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.delete_user_group_member
        ] = mock_rpc

        request = {}
        await client.delete_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.delete_user_group_member(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.DeleteUserGroupMemberRequest(),
        {},
    ],
)
async def test_delete_user_group_member_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.DeleteUserGroupMemberRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_user_group_member_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.DeleteUserGroupMemberRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group_member), "__call__"
    ) as call:
        call.return_value = None
        client.delete_user_group_member(request)

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
async def test_delete_user_group_member_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.DeleteUserGroupMemberRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group_member), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_user_group_member(request)

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


def test_delete_user_group_member_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_user_group_member(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_user_group_member_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_user_group_member(
            marketingplatform_admin.DeleteUserGroupMemberRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_user_group_member_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_user_group_member(
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
async def test_delete_user_group_member_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_user_group_member(
            marketingplatform_admin.DeleteUserGroupMemberRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.GetAdminAccessBindingRequest(),
        {},
    ],
)
def test_get_admin_access_binding(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.AdminAccessBinding(
            name="name_value",
            organization_roles=[resources.OrganizationRole.ORG_ADMIN_ROLE],
            user_email="user_email_value",
        )
        response = client.get_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.GetAdminAccessBindingRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.AdminAccessBinding)
    assert response.name == "name_value"
    assert response.organization_roles == [resources.OrganizationRole.ORG_ADMIN_ROLE]


def test_get_admin_access_binding_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.GetAdminAccessBindingRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_admin_access_binding), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_admin_access_binding(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetAdminAccessBindingRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_admin_access_binding_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_admin_access_binding
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_admin_access_binding
        ] = mock_rpc
        request = {}
        client.get_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_admin_access_binding(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_admin_access_binding_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_admin_access_binding
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_admin_access_binding
        ] = mock_rpc

        request = {}
        await client.get_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_admin_access_binding(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.GetAdminAccessBindingRequest(),
        {},
    ],
)
async def test_get_admin_access_binding_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AdminAccessBinding(
                name="name_value",
                organization_roles=[resources.OrganizationRole.ORG_ADMIN_ROLE],
            )
        )
        response = await client.get_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.GetAdminAccessBindingRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.AdminAccessBinding)
    assert response.name == "name_value"
    assert response.organization_roles == [resources.OrganizationRole.ORG_ADMIN_ROLE]


def test_get_admin_access_binding_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.GetAdminAccessBindingRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_admin_access_binding), "__call__"
    ) as call:
        call.return_value = resources.AdminAccessBinding()
        client.get_admin_access_binding(request)

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
async def test_get_admin_access_binding_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.GetAdminAccessBindingRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_admin_access_binding), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AdminAccessBinding()
        )
        await client.get_admin_access_binding(request)

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


def test_get_admin_access_binding_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.AdminAccessBinding()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_admin_access_binding(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_admin_access_binding_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_admin_access_binding(
            marketingplatform_admin.GetAdminAccessBindingRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_admin_access_binding_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.AdminAccessBinding()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AdminAccessBinding()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_admin_access_binding(
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
async def test_get_admin_access_binding_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_admin_access_binding(
            marketingplatform_admin.GetAdminAccessBindingRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListAdminAccessBindingsRequest(),
        {},
    ],
)
def test_list_admin_access_bindings(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_admin_access_bindings), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ListAdminAccessBindingsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_admin_access_bindings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.ListAdminAccessBindingsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListAdminAccessBindingsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_admin_access_bindings_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.ListAdminAccessBindingsRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_admin_access_bindings), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_admin_access_bindings(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListAdminAccessBindingsRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_admin_access_bindings_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_admin_access_bindings
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_admin_access_bindings
        ] = mock_rpc
        request = {}
        client.list_admin_access_bindings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_admin_access_bindings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_admin_access_bindings_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_admin_access_bindings
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_admin_access_bindings
        ] = mock_rpc

        request = {}
        await client.list_admin_access_bindings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_admin_access_bindings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListAdminAccessBindingsRequest(),
        {},
    ],
)
async def test_list_admin_access_bindings_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_admin_access_bindings), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_admin_access_bindings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.ListAdminAccessBindingsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListAdminAccessBindingsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_admin_access_bindings_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.ListAdminAccessBindingsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_admin_access_bindings), "__call__"
    ) as call:
        call.return_value = marketingplatform_admin.ListAdminAccessBindingsResponse()
        client.list_admin_access_bindings(request)

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
async def test_list_admin_access_bindings_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.ListAdminAccessBindingsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_admin_access_bindings), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListAdminAccessBindingsResponse()
        )
        await client.list_admin_access_bindings(request)

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


def test_list_admin_access_bindings_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_admin_access_bindings), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ListAdminAccessBindingsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_admin_access_bindings(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_admin_access_bindings_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_admin_access_bindings(
            marketingplatform_admin.ListAdminAccessBindingsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_admin_access_bindings_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_admin_access_bindings), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = marketingplatform_admin.ListAdminAccessBindingsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListAdminAccessBindingsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_admin_access_bindings(
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
async def test_list_admin_access_bindings_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_admin_access_bindings(
            marketingplatform_admin.ListAdminAccessBindingsRequest(),
            parent="parent_value",
        )


def test_list_admin_access_bindings_pager(transport_name: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_admin_access_bindings), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
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
        pager = client.list_admin_access_bindings(
            request={}, retry=retry, timeout=timeout
        )

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.AdminAccessBinding) for i in results)


def test_list_admin_access_bindings_pages(transport_name: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_admin_access_bindings), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_admin_access_bindings(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_admin_access_bindings_async_pager():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_admin_access_bindings),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_admin_access_bindings(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, resources.AdminAccessBinding) for i in responses)


@pytest.mark.asyncio
async def test_list_admin_access_bindings_async_pages():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_admin_access_bindings),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_admin_access_bindings(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.CreateAdminAccessBindingRequest(),
        {},
    ],
)
def test_create_admin_access_binding(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.AdminAccessBinding(
            name="name_value",
            organization_roles=[resources.OrganizationRole.ORG_ADMIN_ROLE],
            user_email="user_email_value",
        )
        response = client.create_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.CreateAdminAccessBindingRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.AdminAccessBinding)
    assert response.name == "name_value"
    assert response.organization_roles == [resources.OrganizationRole.ORG_ADMIN_ROLE]


def test_create_admin_access_binding_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.CreateAdminAccessBindingRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_admin_access_binding), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_admin_access_binding(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateAdminAccessBindingRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_create_admin_access_binding_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_admin_access_binding
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.create_admin_access_binding
        ] = mock_rpc
        request = {}
        client.create_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_admin_access_binding(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_admin_access_binding_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_admin_access_binding
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_admin_access_binding
        ] = mock_rpc

        request = {}
        await client.create_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.create_admin_access_binding(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.CreateAdminAccessBindingRequest(),
        {},
    ],
)
async def test_create_admin_access_binding_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AdminAccessBinding(
                name="name_value",
                organization_roles=[resources.OrganizationRole.ORG_ADMIN_ROLE],
            )
        )
        response = await client.create_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.CreateAdminAccessBindingRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.AdminAccessBinding)
    assert response.name == "name_value"
    assert response.organization_roles == [resources.OrganizationRole.ORG_ADMIN_ROLE]


def test_create_admin_access_binding_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.CreateAdminAccessBindingRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_admin_access_binding), "__call__"
    ) as call:
        call.return_value = resources.AdminAccessBinding()
        client.create_admin_access_binding(request)

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
async def test_create_admin_access_binding_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.CreateAdminAccessBindingRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_admin_access_binding), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AdminAccessBinding()
        )
        await client.create_admin_access_binding(request)

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


def test_create_admin_access_binding_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.AdminAccessBinding()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_admin_access_binding(
            parent="parent_value",
            admin_access_binding=resources.AdminAccessBinding(
                user_email="user_email_value"
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].admin_access_binding
        mock_val = resources.AdminAccessBinding(user_email="user_email_value")
        assert arg == mock_val


def test_create_admin_access_binding_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_admin_access_binding(
            marketingplatform_admin.CreateAdminAccessBindingRequest(),
            parent="parent_value",
            admin_access_binding=resources.AdminAccessBinding(
                user_email="user_email_value"
            ),
        )


@pytest.mark.asyncio
async def test_create_admin_access_binding_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.AdminAccessBinding()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AdminAccessBinding()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_admin_access_binding(
            parent="parent_value",
            admin_access_binding=resources.AdminAccessBinding(
                user_email="user_email_value"
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].admin_access_binding
        mock_val = resources.AdminAccessBinding(user_email="user_email_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_admin_access_binding_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_admin_access_binding(
            marketingplatform_admin.CreateAdminAccessBindingRequest(),
            parent="parent_value",
            admin_access_binding=resources.AdminAccessBinding(
                user_email="user_email_value"
            ),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.UpdateAdminAccessBindingRequest(),
        {},
    ],
)
def test_update_admin_access_binding(request_type, transport: str = "grpc"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.AdminAccessBinding(
            name="name_value",
            organization_roles=[resources.OrganizationRole.ORG_ADMIN_ROLE],
            user_email="user_email_value",
        )
        response = client.update_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.UpdateAdminAccessBindingRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.AdminAccessBinding)
    assert response.name == "name_value"
    assert response.organization_roles == [resources.OrganizationRole.ORG_ADMIN_ROLE]


def test_update_admin_access_binding_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = marketingplatform_admin.UpdateAdminAccessBindingRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_admin_access_binding), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_admin_access_binding(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.UpdateAdminAccessBindingRequest()
        assert args[0] == request_msg


def test_update_admin_access_binding_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_admin_access_binding
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_admin_access_binding
        ] = mock_rpc
        request = {}
        client.update_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_admin_access_binding(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_admin_access_binding_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_admin_access_binding
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_admin_access_binding
        ] = mock_rpc

        request = {}
        await client.update_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_admin_access_binding(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.UpdateAdminAccessBindingRequest(),
        {},
    ],
)
async def test_update_admin_access_binding_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AdminAccessBinding(
                name="name_value",
                organization_roles=[resources.OrganizationRole.ORG_ADMIN_ROLE],
            )
        )
        response = await client.update_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = marketingplatform_admin.UpdateAdminAccessBindingRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.AdminAccessBinding)
    assert response.name == "name_value"
    assert response.organization_roles == [resources.OrganizationRole.ORG_ADMIN_ROLE]


def test_update_admin_access_binding_field_headers():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.UpdateAdminAccessBindingRequest()

    request.admin_access_binding.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_admin_access_binding), "__call__"
    ) as call:
        call.return_value = resources.AdminAccessBinding()
        client.update_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "admin_access_binding.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_admin_access_binding_field_headers_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = marketingplatform_admin.UpdateAdminAccessBindingRequest()

    request.admin_access_binding.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_admin_access_binding), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AdminAccessBinding()
        )
        await client.update_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "admin_access_binding.name=name_value",
    ) in kw["metadata"]


def test_update_admin_access_binding_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.AdminAccessBinding()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_admin_access_binding(
            admin_access_binding=resources.AdminAccessBinding(
                user_email="user_email_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].admin_access_binding
        mock_val = resources.AdminAccessBinding(user_email="user_email_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_admin_access_binding_flattened_error():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_admin_access_binding(
            marketingplatform_admin.UpdateAdminAccessBindingRequest(),
            admin_access_binding=resources.AdminAccessBinding(
                user_email="user_email_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_admin_access_binding_flattened_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = resources.AdminAccessBinding()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AdminAccessBinding()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_admin_access_binding(
            admin_access_binding=resources.AdminAccessBinding(
                user_email="user_email_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].admin_access_binding
        mock_val = resources.AdminAccessBinding(user_email="user_email_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_admin_access_binding_flattened_error_async():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_admin_access_binding(
            marketingplatform_admin.UpdateAdminAccessBindingRequest(),
            admin_access_binding=resources.AdminAccessBinding(
                user_email="user_email_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_get_organization_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_organization in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_organization] = (
            mock_rpc
        )

        request = {}
        client.get_organization(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_organization(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_organization_rest_required_fields(
    request_type=marketingplatform_admin.GetOrganizationRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetOrganization,
        "_BaseGetOrganization__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.Organization()
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
            return_value = resources.Organization.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_organization(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_organization_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.Organization()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "organizations/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = resources.Organization.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_organization(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{name=organizations/*}" % client.transport._host, args[1]
        )


def test_get_organization_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_organization(
            marketingplatform_admin.GetOrganizationRequest(),
            name="name_value",
        )


def test_list_organizations_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_organizations in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_organizations] = (
            mock_rpc
        )

        request = {}
        client.list_organizations(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_organizations(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_organizations_rest_pager(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                    resources.Organization(),
                    resources.Organization(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListOrganizationsResponse(
                organizations=[
                    resources.Organization(),
                    resources.Organization(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            marketingplatform_admin.ListOrganizationsResponse.to_json(x)
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {}

        pager = client.list_organizations(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.Organization) for i in results)

        pages = list(client.list_organizations(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_find_sales_partner_managed_clients_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.find_sales_partner_managed_clients
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.find_sales_partner_managed_clients
        ] = mock_rpc

        request = {}
        client.find_sales_partner_managed_clients(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.find_sales_partner_managed_clients(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_find_sales_partner_managed_clients_rest_required_fields(
    request_type=marketingplatform_admin.FindSalesPartnerManagedClientsRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["organization"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseFindSalesPartnerManagedClients,
        "_BaseFindSalesPartnerManagedClients__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["organization"] = "organization_value"

    # verify required fields with non-default values are left alone
    assert "organization" in jsonified_request
    assert jsonified_request["organization"] == "organization_value"

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = marketingplatform_admin.FindSalesPartnerManagedClientsResponse()
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
            return_value = (
                marketingplatform_admin.FindSalesPartnerManagedClientsResponse.pb(
                    return_value
                )
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.find_sales_partner_managed_clients(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_analytics_account_links_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_analytics_account_links
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_analytics_account_links
        ] = mock_rpc

        request = {}
        client.list_analytics_account_links(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_analytics_account_links(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_analytics_account_links_rest_required_fields(
    request_type=marketingplatform_admin.ListAnalyticsAccountLinksRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListAnalyticsAccountLinks,
        "_BaseListAnalyticsAccountLinks__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = marketingplatform_admin.ListAnalyticsAccountLinksResponse()
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
            return_value = marketingplatform_admin.ListAnalyticsAccountLinksResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_analytics_account_links(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_analytics_account_links_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = marketingplatform_admin.ListAnalyticsAccountLinksResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "organizations/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = marketingplatform_admin.ListAnalyticsAccountLinksResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_analytics_account_links(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{parent=organizations/*}/analyticsAccountLinks"
            % client.transport._host,
            args[1],
        )


def test_list_analytics_account_links_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_analytics_account_links(
            marketingplatform_admin.ListAnalyticsAccountLinksRequest(),
            parent="parent_value",
        )


def test_list_analytics_account_links_rest_pager(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                analytics_account_links=[
                    resources.AnalyticsAccountLink(),
                    resources.AnalyticsAccountLink(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            marketingplatform_admin.ListAnalyticsAccountLinksResponse.to_json(x)
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "organizations/sample1"}

        pager = client.list_analytics_account_links(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.AnalyticsAccountLink) for i in results)

        pages = list(client.list_analytics_account_links(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_create_analytics_account_link_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_analytics_account_link
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.create_analytics_account_link
        ] = mock_rpc

        request = {}
        client.create_analytics_account_link(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_analytics_account_link(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_analytics_account_link_rest_required_fields(
    request_type=marketingplatform_admin.CreateAnalyticsAccountLinkRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateAnalyticsAccountLink,
        "_BaseCreateAnalyticsAccountLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.AnalyticsAccountLink()
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
            return_value = resources.AnalyticsAccountLink.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_analytics_account_link(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_analytics_account_link_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.AnalyticsAccountLink()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "organizations/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            analytics_account_link=resources.AnalyticsAccountLink(name="name_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = resources.AnalyticsAccountLink.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_analytics_account_link(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{parent=organizations/*}/analyticsAccountLinks"
            % client.transport._host,
            args[1],
        )


def test_create_analytics_account_link_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_analytics_account_link(
            marketingplatform_admin.CreateAnalyticsAccountLinkRequest(),
            parent="parent_value",
            analytics_account_link=resources.AnalyticsAccountLink(name="name_value"),
        )


def test_delete_analytics_account_link_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_analytics_account_link
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.delete_analytics_account_link
        ] = mock_rpc

        request = {}
        client.delete_analytics_account_link(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_analytics_account_link(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_analytics_account_link_rest_required_fields(
    request_type=marketingplatform_admin.DeleteAnalyticsAccountLinkRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeleteAnalyticsAccountLink,
        "_BaseDeleteAnalyticsAccountLink__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
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

            response = client.delete_analytics_account_link(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_analytics_account_link_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "organizations/sample1/analyticsAccountLinks/sample2"}

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

        client.delete_analytics_account_link(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{name=organizations/*/analyticsAccountLinks/*}"
            % client.transport._host,
            args[1],
        )


def test_delete_analytics_account_link_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_analytics_account_link(
            marketingplatform_admin.DeleteAnalyticsAccountLinkRequest(),
            name="name_value",
        )


def test_set_property_service_level_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.set_property_service_level
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.set_property_service_level
        ] = mock_rpc

        request = {}
        client.set_property_service_level(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.set_property_service_level(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_set_property_service_level_rest_required_fields(
    request_type=marketingplatform_admin.SetPropertyServiceLevelRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["analytics_account_link"] = ""
    request_init["analytics_property"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseSetPropertyServiceLevel,
        "_BaseSetPropertyServiceLevel__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["analyticsAccountLink"] = "analytics_account_link_value"
    jsonified_request["analyticsProperty"] = "analytics_property_value"

    # verify required fields with non-default values are left alone
    assert "analyticsAccountLink" in jsonified_request
    assert jsonified_request["analyticsAccountLink"] == "analytics_account_link_value"
    assert "analyticsProperty" in jsonified_request
    assert jsonified_request["analyticsProperty"] == "analytics_property_value"

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = marketingplatform_admin.SetPropertyServiceLevelResponse()
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
            return_value = marketingplatform_admin.SetPropertyServiceLevelResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.set_property_service_level(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_set_property_service_level_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = marketingplatform_admin.SetPropertyServiceLevelResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "analytics_account_link": "organizations/sample1/analyticsAccountLinks/sample2"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            analytics_account_link="analytics_account_link_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = marketingplatform_admin.SetPropertyServiceLevelResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.set_property_service_level(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{analytics_account_link=organizations/*/analyticsAccountLinks/*}:setPropertyServiceLevel"
            % client.transport._host,
            args[1],
        )


def test_set_property_service_level_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.set_property_service_level(
            marketingplatform_admin.SetPropertyServiceLevelRequest(),
            analytics_account_link="analytics_account_link_value",
        )


def test_report_property_usage_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.report_property_usage
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.report_property_usage] = (
            mock_rpc
        )

        request = {}
        client.report_property_usage(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.report_property_usage(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_report_property_usage_rest_required_fields(
    request_type=marketingplatform_admin.ReportPropertyUsageRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["organization"] = ""
    request_init["month"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseReportPropertyUsage,
        "_BaseReportPropertyUsage__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["organization"] = "organization_value"
    jsonified_request["month"] = "month_value"

    # verify required fields with non-default values are left alone
    assert "organization" in jsonified_request
    assert jsonified_request["organization"] == "organization_value"
    assert "month" in jsonified_request
    assert jsonified_request["month"] == "month_value"

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = marketingplatform_admin.ReportPropertyUsageResponse()
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
            return_value = marketingplatform_admin.ReportPropertyUsageResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.report_property_usage(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_report_property_usage_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = marketingplatform_admin.ReportPropertyUsageResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"organization": "organizations/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            organization="organization_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = marketingplatform_admin.ReportPropertyUsageResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.report_property_usage(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{organization=organizations/*}:reportPropertyUsage"
            % client.transport._host,
            args[1],
        )


def test_report_property_usage_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.report_property_usage(
            marketingplatform_admin.ReportPropertyUsageRequest(),
            organization="organization_value",
        )


def test_get_user_group_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_user_group in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_user_group] = mock_rpc

        request = {}
        client.get_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_user_group(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_user_group_rest_required_fields(
    request_type=marketingplatform_admin.GetUserGroupRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetUserGroup,
        "_BaseGetUserGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.UserGroup()
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
            return_value = resources.UserGroup.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_user_group(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_user_group_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.UserGroup()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "organizations/sample1/userGroups/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = resources.UserGroup.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_user_group(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{name=organizations/*/userGroups/*}" % client.transport._host,
            args[1],
        )


def test_get_user_group_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_user_group(
            marketingplatform_admin.GetUserGroupRequest(),
            name="name_value",
        )


def test_list_user_groups_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_user_groups in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_user_groups] = (
            mock_rpc
        )

        request = {}
        client.list_user_groups(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_user_groups(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_user_groups_rest_required_fields(
    request_type=marketingplatform_admin.ListUserGroupsRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListUserGroups,
        "_BaseListUserGroups__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = marketingplatform_admin.ListUserGroupsResponse()
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
            return_value = marketingplatform_admin.ListUserGroupsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_user_groups(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_user_groups_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = marketingplatform_admin.ListUserGroupsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "organizations/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = marketingplatform_admin.ListUserGroupsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_user_groups(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{parent=organizations/*}/userGroups" % client.transport._host,
            args[1],
        )


def test_list_user_groups_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_user_groups(
            marketingplatform_admin.ListUserGroupsRequest(),
            parent="parent_value",
        )


def test_list_user_groups_rest_pager(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                    resources.UserGroup(),
                    resources.UserGroup(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListUserGroupsResponse(
                user_groups=[
                    resources.UserGroup(),
                    resources.UserGroup(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            marketingplatform_admin.ListUserGroupsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "organizations/sample1"}

        pager = client.list_user_groups(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.UserGroup) for i in results)

        pages = list(client.list_user_groups(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_create_user_group_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_user_group in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_user_group] = (
            mock_rpc
        )

        request = {}
        client.create_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_user_group(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_user_group_rest_required_fields(
    request_type=marketingplatform_admin.CreateUserGroupRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateUserGroup,
        "_BaseCreateUserGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.UserGroup()
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
            return_value = resources.UserGroup.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_user_group(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_user_group_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.UserGroup()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "organizations/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            user_group=resources.UserGroup(name="name_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = resources.UserGroup.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_user_group(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{parent=organizations/*}/userGroups" % client.transport._host,
            args[1],
        )


def test_create_user_group_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_user_group(
            marketingplatform_admin.CreateUserGroupRequest(),
            parent="parent_value",
            user_group=resources.UserGroup(name="name_value"),
        )


def test_update_user_group_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_user_group in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_user_group] = (
            mock_rpc
        )

        request = {}
        client.update_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_user_group(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_user_group_rest_required_fields(
    request_type=marketingplatform_admin.UpdateUserGroupRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateUserGroup,
        "_BaseUpdateUserGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.UserGroup()
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
            return_value = resources.UserGroup.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_user_group(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_user_group_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.UserGroup()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "user_group": {"name": "organizations/sample1/userGroups/sample2"}
        }

        # get truthy value for each flattened field
        mock_args = dict(
            user_group=resources.UserGroup(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = resources.UserGroup.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_user_group(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{user_group.name=organizations/*/userGroups/*}"
            % client.transport._host,
            args[1],
        )


def test_update_user_group_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_user_group(
            marketingplatform_admin.UpdateUserGroupRequest(),
            user_group=resources.UserGroup(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_delete_user_group_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_user_group in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_user_group] = (
            mock_rpc
        )

        request = {}
        client.delete_user_group(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_user_group(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_user_group_rest_required_fields(
    request_type=marketingplatform_admin.DeleteUserGroupRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeleteUserGroup,
        "_BaseDeleteUserGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
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

            response = client.delete_user_group(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_user_group_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "organizations/sample1/userGroups/sample2"}

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

        client.delete_user_group(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{name=organizations/*/userGroups/*}" % client.transport._host,
            args[1],
        )


def test_delete_user_group_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_user_group(
            marketingplatform_admin.DeleteUserGroupRequest(),
            name="name_value",
        )


def test_get_user_group_member_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_user_group_member
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_user_group_member] = (
            mock_rpc
        )

        request = {}
        client.get_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_user_group_member(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_user_group_member_rest_required_fields(
    request_type=marketingplatform_admin.GetUserGroupMemberRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetUserGroupMember,
        "_BaseGetUserGroupMember__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.UserGroupMember()
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
            return_value = resources.UserGroupMember.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_user_group_member(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_user_group_member_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.UserGroupMember()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "organizations/sample1/userGroups/sample2/members/sample3"
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
        return_value = resources.UserGroupMember.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_user_group_member(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{name=organizations/*/userGroups/*/members/*}"
            % client.transport._host,
            args[1],
        )


def test_get_user_group_member_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_user_group_member(
            marketingplatform_admin.GetUserGroupMemberRequest(),
            name="name_value",
        )


def test_list_user_group_members_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_user_group_members
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_user_group_members
        ] = mock_rpc

        request = {}
        client.list_user_group_members(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_user_group_members(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_user_group_members_rest_required_fields(
    request_type=marketingplatform_admin.ListUserGroupMembersRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListUserGroupMembers,
        "_BaseListUserGroupMembers__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = marketingplatform_admin.ListUserGroupMembersResponse()
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
            return_value = marketingplatform_admin.ListUserGroupMembersResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_user_group_members(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_user_group_members_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = marketingplatform_admin.ListUserGroupMembersResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "organizations/sample1/userGroups/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = marketingplatform_admin.ListUserGroupMembersResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_user_group_members(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{parent=organizations/*/userGroups/*}/members"
            % client.transport._host,
            args[1],
        )


def test_list_user_group_members_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_user_group_members(
            marketingplatform_admin.ListUserGroupMembersRequest(),
            parent="parent_value",
        )


def test_list_user_group_members_rest_pager(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListUserGroupMembersResponse(
                user_group_members=[
                    resources.UserGroupMember(),
                    resources.UserGroupMember(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            marketingplatform_admin.ListUserGroupMembersResponse.to_json(x)
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "organizations/sample1/userGroups/sample2"}

        pager = client.list_user_group_members(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.UserGroupMember) for i in results)

        pages = list(client.list_user_group_members(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_create_user_group_member_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_user_group_member
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.create_user_group_member
        ] = mock_rpc

        request = {}
        client.create_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_user_group_member(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_user_group_member_rest_required_fields(
    request_type=marketingplatform_admin.CreateUserGroupMemberRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateUserGroupMember,
        "_BaseCreateUserGroupMember__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.UserGroupMember()
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
            return_value = resources.UserGroupMember.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_user_group_member(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_user_group_member_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.UserGroupMember()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "organizations/sample1/userGroups/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            user_group_member=resources.UserGroupMember(user_email="user_email_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = resources.UserGroupMember.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_user_group_member(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{parent=organizations/*/userGroups/*}/members"
            % client.transport._host,
            args[1],
        )


def test_create_user_group_member_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_user_group_member(
            marketingplatform_admin.CreateUserGroupMemberRequest(),
            parent="parent_value",
            user_group_member=resources.UserGroupMember(user_email="user_email_value"),
        )


def test_update_user_group_member_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_user_group_member
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_user_group_member
        ] = mock_rpc

        request = {}
        client.update_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_user_group_member(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_user_group_member_rest_required_fields(
    request_type=marketingplatform_admin.UpdateUserGroupMemberRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateUserGroupMember,
        "_BaseUpdateUserGroupMember__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.UserGroupMember()
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
            return_value = resources.UserGroupMember.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_user_group_member(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_user_group_member_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.UserGroupMember()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "user_group_member": {
                "name": "organizations/sample1/userGroups/sample2/members/sample3"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            user_group_member=resources.UserGroupMember(user_email="user_email_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = resources.UserGroupMember.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_user_group_member(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{user_group_member.name=organizations/*/userGroups/*/members/*}"
            % client.transport._host,
            args[1],
        )


def test_update_user_group_member_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_user_group_member(
            marketingplatform_admin.UpdateUserGroupMemberRequest(),
            user_group_member=resources.UserGroupMember(user_email="user_email_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_delete_user_group_member_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_user_group_member
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.delete_user_group_member
        ] = mock_rpc

        request = {}
        client.delete_user_group_member(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_user_group_member(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_user_group_member_rest_required_fields(
    request_type=marketingplatform_admin.DeleteUserGroupMemberRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeleteUserGroupMember,
        "_BaseDeleteUserGroupMember__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
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

            response = client.delete_user_group_member(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_user_group_member_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "organizations/sample1/userGroups/sample2/members/sample3"
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

        client.delete_user_group_member(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{name=organizations/*/userGroups/*/members/*}"
            % client.transport._host,
            args[1],
        )


def test_delete_user_group_member_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_user_group_member(
            marketingplatform_admin.DeleteUserGroupMemberRequest(),
            name="name_value",
        )


def test_get_admin_access_binding_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_admin_access_binding
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_admin_access_binding
        ] = mock_rpc

        request = {}
        client.get_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_admin_access_binding(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_admin_access_binding_rest_required_fields(
    request_type=marketingplatform_admin.GetAdminAccessBindingRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetAdminAccessBinding,
        "_BaseGetAdminAccessBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.AdminAccessBinding()
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
            return_value = resources.AdminAccessBinding.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_admin_access_binding(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_admin_access_binding_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.AdminAccessBinding()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "organizations/sample1/adminAccessBindings/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = resources.AdminAccessBinding.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_admin_access_binding(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{name=organizations/*/adminAccessBindings/*}"
            % client.transport._host,
            args[1],
        )


def test_get_admin_access_binding_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_admin_access_binding(
            marketingplatform_admin.GetAdminAccessBindingRequest(),
            name="name_value",
        )


def test_list_admin_access_bindings_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_admin_access_bindings
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_admin_access_bindings
        ] = mock_rpc

        request = {}
        client.list_admin_access_bindings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_admin_access_bindings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_admin_access_bindings_rest_required_fields(
    request_type=marketingplatform_admin.ListAdminAccessBindingsRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListAdminAccessBindings,
        "_BaseListAdminAccessBindings__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = marketingplatform_admin.ListAdminAccessBindingsResponse()
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
            return_value = marketingplatform_admin.ListAdminAccessBindingsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_admin_access_bindings(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_admin_access_bindings_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = marketingplatform_admin.ListAdminAccessBindingsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "organizations/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = marketingplatform_admin.ListAdminAccessBindingsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_admin_access_bindings(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{parent=organizations/*}/adminAccessBindings"
            % client.transport._host,
            args[1],
        )


def test_list_admin_access_bindings_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_admin_access_bindings(
            marketingplatform_admin.ListAdminAccessBindingsRequest(),
            parent="parent_value",
        )


def test_list_admin_access_bindings_rest_pager(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
                ],
                next_page_token="abc",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[],
                next_page_token="def",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                ],
                next_page_token="ghi",
            ),
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                admin_access_bindings=[
                    resources.AdminAccessBinding(),
                    resources.AdminAccessBinding(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            marketingplatform_admin.ListAdminAccessBindingsResponse.to_json(x)
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "organizations/sample1"}

        pager = client.list_admin_access_bindings(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, resources.AdminAccessBinding) for i in results)

        pages = list(client.list_admin_access_bindings(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_create_admin_access_binding_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_admin_access_binding
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.create_admin_access_binding
        ] = mock_rpc

        request = {}
        client.create_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_admin_access_binding(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_admin_access_binding_rest_required_fields(
    request_type=marketingplatform_admin.CreateAdminAccessBindingRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateAdminAccessBinding,
        "_BaseCreateAdminAccessBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.AdminAccessBinding()
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
            return_value = resources.AdminAccessBinding.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_admin_access_binding(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_admin_access_binding_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.AdminAccessBinding()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "organizations/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            admin_access_binding=resources.AdminAccessBinding(
                user_email="user_email_value"
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = resources.AdminAccessBinding.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_admin_access_binding(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{parent=organizations/*}/adminAccessBindings"
            % client.transport._host,
            args[1],
        )


def test_create_admin_access_binding_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_admin_access_binding(
            marketingplatform_admin.CreateAdminAccessBindingRequest(),
            parent="parent_value",
            admin_access_binding=resources.AdminAccessBinding(
                user_email="user_email_value"
            ),
        )


def test_update_admin_access_binding_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_admin_access_binding
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_admin_access_binding
        ] = mock_rpc

        request = {}
        client.update_admin_access_binding(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_admin_access_binding(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_admin_access_binding_rest_required_fields(
    request_type=marketingplatform_admin.UpdateAdminAccessBindingRequest,
):
    transport_class = transports.MarketingplatformAdminServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateAdminAccessBinding,
        "_BaseUpdateAdminAccessBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = resources.AdminAccessBinding()
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
            return_value = resources.AdminAccessBinding.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_admin_access_binding(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_admin_access_binding_rest_flattened():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.AdminAccessBinding()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "admin_access_binding": {
                "name": "organizations/sample1/adminAccessBindings/sample2"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            admin_access_binding=resources.AdminAccessBinding(
                user_email="user_email_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = resources.AdminAccessBinding.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_admin_access_binding(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1alpha/{admin_access_binding.name=organizations/*/adminAccessBindings/*}"
            % client.transport._host,
            args[1],
        )


def test_update_admin_access_binding_rest_flattened_error(transport: str = "rest"):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_admin_access_binding(
            marketingplatform_admin.UpdateAdminAccessBindingRequest(),
            admin_access_binding=resources.AdminAccessBinding(
                user_email="user_email_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.MarketingplatformAdminServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.MarketingplatformAdminServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = MarketingplatformAdminServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.MarketingplatformAdminServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = MarketingplatformAdminServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = MarketingplatformAdminServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.MarketingplatformAdminServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = MarketingplatformAdminServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.MarketingplatformAdminServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.MarketingplatformAdminServiceGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.MarketingplatformAdminServiceGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.MarketingplatformAdminServiceGrpcTransport,
        transports.MarketingplatformAdminServiceGrpcAsyncIOTransport,
        transports.MarketingplatformAdminServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = MarketingplatformAdminServiceClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_organization_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_organization), "__call__") as call:
        call.return_value = resources.Organization()
        client.get_organization(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetOrganizationRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_organizations_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_organizations), "__call__"
    ) as call:
        call.return_value = marketingplatform_admin.ListOrganizationsResponse()
        client.list_organizations(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListOrganizationsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_find_sales_partner_managed_clients_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.find_sales_partner_managed_clients), "__call__"
    ) as call:
        call.return_value = (
            marketingplatform_admin.FindSalesPartnerManagedClientsResponse()
        )
        client.find_sales_partner_managed_clients(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.FindSalesPartnerManagedClientsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_analytics_account_links_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_analytics_account_links), "__call__"
    ) as call:
        call.return_value = marketingplatform_admin.ListAnalyticsAccountLinksResponse()
        client.list_analytics_account_links(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListAnalyticsAccountLinksRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_analytics_account_link_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_analytics_account_link), "__call__"
    ) as call:
        call.return_value = resources.AnalyticsAccountLink()
        client.create_analytics_account_link(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateAnalyticsAccountLinkRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_analytics_account_link_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_analytics_account_link), "__call__"
    ) as call:
        call.return_value = None
        client.delete_analytics_account_link(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.DeleteAnalyticsAccountLinkRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_set_property_service_level_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.set_property_service_level), "__call__"
    ) as call:
        call.return_value = marketingplatform_admin.SetPropertyServiceLevelResponse()
        client.set_property_service_level(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.SetPropertyServiceLevelRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_report_property_usage_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.report_property_usage), "__call__"
    ) as call:
        call.return_value = marketingplatform_admin.ReportPropertyUsageResponse()
        client.report_property_usage(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ReportPropertyUsageRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_user_group_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_user_group), "__call__") as call:
        call.return_value = resources.UserGroup()
        client.get_user_group(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetUserGroupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_user_groups_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_user_groups), "__call__") as call:
        call.return_value = marketingplatform_admin.ListUserGroupsResponse()
        client.list_user_groups(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListUserGroupsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_user_group_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group), "__call__"
    ) as call:
        call.return_value = resources.UserGroup()
        client.create_user_group(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateUserGroupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_user_group_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group), "__call__"
    ) as call:
        call.return_value = resources.UserGroup()
        client.update_user_group(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.UpdateUserGroupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_user_group_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group), "__call__"
    ) as call:
        call.return_value = None
        client.delete_user_group(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.DeleteUserGroupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_user_group_member_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_user_group_member), "__call__"
    ) as call:
        call.return_value = resources.UserGroupMember()
        client.get_user_group_member(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetUserGroupMemberRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_user_group_members_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_group_members), "__call__"
    ) as call:
        call.return_value = marketingplatform_admin.ListUserGroupMembersResponse()
        client.list_user_group_members(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListUserGroupMembersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_user_group_member_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group_member), "__call__"
    ) as call:
        call.return_value = resources.UserGroupMember()
        client.create_user_group_member(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateUserGroupMemberRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_user_group_member_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group_member), "__call__"
    ) as call:
        call.return_value = resources.UserGroupMember()
        client.update_user_group_member(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.UpdateUserGroupMemberRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_user_group_member_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group_member), "__call__"
    ) as call:
        call.return_value = None
        client.delete_user_group_member(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.DeleteUserGroupMemberRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_admin_access_binding_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_admin_access_binding), "__call__"
    ) as call:
        call.return_value = resources.AdminAccessBinding()
        client.get_admin_access_binding(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetAdminAccessBindingRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_admin_access_bindings_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_admin_access_bindings), "__call__"
    ) as call:
        call.return_value = marketingplatform_admin.ListAdminAccessBindingsResponse()
        client.list_admin_access_bindings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListAdminAccessBindingsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_admin_access_binding_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_admin_access_binding), "__call__"
    ) as call:
        call.return_value = resources.AdminAccessBinding()
        client.create_admin_access_binding(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateAdminAccessBindingRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_admin_access_binding_empty_call_grpc():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_admin_access_binding), "__call__"
    ) as call:
        call.return_value = resources.AdminAccessBinding()
        client.update_admin_access_binding(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.UpdateAdminAccessBindingRequest()
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = MarketingplatformAdminServiceAsyncClient.get_transport_class(
        "grpc_asyncio"
    )(credentials=async_anonymous_credentials())
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_organization_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_organization), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.Organization(
                name="name_value",
                display_name="display_name_value",
            )
        )
        await client.get_organization(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetOrganizationRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_organizations_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_organizations), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListOrganizationsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_organizations(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListOrganizationsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_find_sales_partner_managed_clients_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.find_sales_partner_managed_clients), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.FindSalesPartnerManagedClientsResponse()
        )
        await client.find_sales_partner_managed_clients(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.FindSalesPartnerManagedClientsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_analytics_account_links_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_analytics_account_links), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_analytics_account_links(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListAnalyticsAccountLinksRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_analytics_account_link_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_analytics_account_link), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AnalyticsAccountLink(
                name="name_value",
                analytics_account="analytics_account_value",
                display_name="display_name_value",
                link_verification_state=resources.LinkVerificationState.LINK_VERIFICATION_STATE_VERIFIED,
            )
        )
        await client.create_analytics_account_link(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateAnalyticsAccountLinkRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_analytics_account_link_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_analytics_account_link), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_analytics_account_link(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.DeleteAnalyticsAccountLinkRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_set_property_service_level_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.set_property_service_level), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.SetPropertyServiceLevelResponse()
        )
        await client.set_property_service_level(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.SetPropertyServiceLevelRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_report_property_usage_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.report_property_usage), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ReportPropertyUsageResponse()
        )
        await client.report_property_usage(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ReportPropertyUsageRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_user_group_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_user_group), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroup(
                name="name_value",
                display_name="display_name_value",
                description="description_value",
            )
        )
        await client.get_user_group(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetUserGroupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_user_groups_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_user_groups), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListUserGroupsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_user_groups(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListUserGroupsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_user_group_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroup(
                name="name_value",
                display_name="display_name_value",
                description="description_value",
            )
        )
        await client.create_user_group(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateUserGroupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_user_group_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroup(
                name="name_value",
                display_name="display_name_value",
                description="description_value",
            )
        )
        await client.update_user_group(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.UpdateUserGroupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_user_group_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_user_group(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.DeleteUserGroupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_user_group_member_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroupMember(
                name="name_value",
                membership_role=resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER,
            )
        )
        await client.get_user_group_member(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetUserGroupMemberRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_user_group_members_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_group_members), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListUserGroupMembersResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_user_group_members(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListUserGroupMembersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_user_group_member_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroupMember(
                name="name_value",
                membership_role=resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER,
            )
        )
        await client.create_user_group_member(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateUserGroupMemberRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_user_group_member_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.UserGroupMember(
                name="name_value",
                membership_role=resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER,
            )
        )
        await client.update_user_group_member(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.UpdateUserGroupMemberRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_user_group_member_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group_member), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_user_group_member(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.DeleteUserGroupMemberRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_admin_access_binding_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AdminAccessBinding(
                name="name_value",
                organization_roles=[resources.OrganizationRole.ORG_ADMIN_ROLE],
            )
        )
        await client.get_admin_access_binding(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetAdminAccessBindingRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_admin_access_bindings_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_admin_access_bindings), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            marketingplatform_admin.ListAdminAccessBindingsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_admin_access_bindings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListAdminAccessBindingsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_admin_access_binding_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AdminAccessBinding(
                name="name_value",
                organization_roles=[resources.OrganizationRole.ORG_ADMIN_ROLE],
            )
        )
        await client.create_admin_access_binding(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateAdminAccessBindingRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_admin_access_binding_empty_call_grpc_asyncio():
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_admin_access_binding), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            resources.AdminAccessBinding(
                name="name_value",
                organization_roles=[resources.OrganizationRole.ORG_ADMIN_ROLE],
            )
        )
        await client.update_admin_access_binding(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.UpdateAdminAccessBindingRequest()
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = MarketingplatformAdminServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_get_organization_rest_bad_request(
    request_type=marketingplatform_admin.GetOrganizationRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "organizations/sample1"}
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
        client.get_organization(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.GetOrganizationRequest,
        dict,
    ],
)
def test_get_organization_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "organizations/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.Organization(
            name="name_value",
            display_name="display_name_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = resources.Organization.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_organization(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.Organization)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_organization_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_get_organization",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_get_organization_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_get_organization",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.GetOrganizationRequest.pb(
            marketingplatform_admin.GetOrganizationRequest()
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
        return_value = resources.Organization.to_json(resources.Organization())
        req.return_value.content = return_value

        request = marketingplatform_admin.GetOrganizationRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.Organization()
        post_with_metadata.return_value = resources.Organization(), metadata

        client.get_organization(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_organizations_rest_bad_request(
    request_type=marketingplatform_admin.ListOrganizationsRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {}
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
        client.list_organizations(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListOrganizationsRequest,
        dict,
    ],
)
def test_list_organizations_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = marketingplatform_admin.ListOrganizationsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = marketingplatform_admin.ListOrganizationsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_organizations(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListOrganizationsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_organizations_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_list_organizations",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_list_organizations_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_list_organizations",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.ListOrganizationsRequest.pb(
            marketingplatform_admin.ListOrganizationsRequest()
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
        return_value = marketingplatform_admin.ListOrganizationsResponse.to_json(
            marketingplatform_admin.ListOrganizationsResponse()
        )
        req.return_value.content = return_value

        request = marketingplatform_admin.ListOrganizationsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = marketingplatform_admin.ListOrganizationsResponse()
        post_with_metadata.return_value = (
            marketingplatform_admin.ListOrganizationsResponse(),
            metadata,
        )

        client.list_organizations(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_find_sales_partner_managed_clients_rest_bad_request(
    request_type=marketingplatform_admin.FindSalesPartnerManagedClientsRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"organization": "organizations/sample1"}
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
        client.find_sales_partner_managed_clients(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.FindSalesPartnerManagedClientsRequest,
        dict,
    ],
)
def test_find_sales_partner_managed_clients_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"organization": "organizations/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = marketingplatform_admin.FindSalesPartnerManagedClientsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = (
            marketingplatform_admin.FindSalesPartnerManagedClientsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.find_sales_partner_managed_clients(request)

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, marketingplatform_admin.FindSalesPartnerManagedClientsResponse
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_find_sales_partner_managed_clients_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_find_sales_partner_managed_clients",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_find_sales_partner_managed_clients_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_find_sales_partner_managed_clients",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.FindSalesPartnerManagedClientsRequest.pb(
            marketingplatform_admin.FindSalesPartnerManagedClientsRequest()
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
        return_value = (
            marketingplatform_admin.FindSalesPartnerManagedClientsResponse.to_json(
                marketingplatform_admin.FindSalesPartnerManagedClientsResponse()
            )
        )
        req.return_value.content = return_value

        request = marketingplatform_admin.FindSalesPartnerManagedClientsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            marketingplatform_admin.FindSalesPartnerManagedClientsResponse()
        )
        post_with_metadata.return_value = (
            marketingplatform_admin.FindSalesPartnerManagedClientsResponse(),
            metadata,
        )

        client.find_sales_partner_managed_clients(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_analytics_account_links_rest_bad_request(
    request_type=marketingplatform_admin.ListAnalyticsAccountLinksRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1"}
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
        client.list_analytics_account_links(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListAnalyticsAccountLinksRequest,
        dict,
    ],
)
def test_list_analytics_account_links_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = marketingplatform_admin.ListAnalyticsAccountLinksResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = marketingplatform_admin.ListAnalyticsAccountLinksResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_analytics_account_links(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListAnalyticsAccountLinksPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_analytics_account_links_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_list_analytics_account_links",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_list_analytics_account_links_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_list_analytics_account_links",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.ListAnalyticsAccountLinksRequest.pb(
            marketingplatform_admin.ListAnalyticsAccountLinksRequest()
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
        return_value = (
            marketingplatform_admin.ListAnalyticsAccountLinksResponse.to_json(
                marketingplatform_admin.ListAnalyticsAccountLinksResponse()
            )
        )
        req.return_value.content = return_value

        request = marketingplatform_admin.ListAnalyticsAccountLinksRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = marketingplatform_admin.ListAnalyticsAccountLinksResponse()
        post_with_metadata.return_value = (
            marketingplatform_admin.ListAnalyticsAccountLinksResponse(),
            metadata,
        )

        client.list_analytics_account_links(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_analytics_account_link_rest_bad_request(
    request_type=marketingplatform_admin.CreateAnalyticsAccountLinkRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1"}
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
        client.create_analytics_account_link(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.CreateAnalyticsAccountLinkRequest,
        dict,
    ],
)
def test_create_analytics_account_link_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1"}
    request_init["analytics_account_link"] = {
        "name": "name_value",
        "analytics_account": "analytics_account_value",
        "display_name": "display_name_value",
        "link_verification_state": 1,
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = marketingplatform_admin.CreateAnalyticsAccountLinkRequest.meta.fields[
        "analytics_account_link"
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
    for field, value in request_init[
        "analytics_account_link"
    ].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["analytics_account_link"][field])):
                    del request_init["analytics_account_link"][field][i][subfield]
            else:
                del request_init["analytics_account_link"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.AnalyticsAccountLink(
            name="name_value",
            analytics_account="analytics_account_value",
            display_name="display_name_value",
            link_verification_state=resources.LinkVerificationState.LINK_VERIFICATION_STATE_VERIFIED,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = resources.AnalyticsAccountLink.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_analytics_account_link(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.AnalyticsAccountLink)
    assert response.name == "name_value"
    assert response.analytics_account == "analytics_account_value"
    assert response.display_name == "display_name_value"
    assert (
        response.link_verification_state
        == resources.LinkVerificationState.LINK_VERIFICATION_STATE_VERIFIED
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_analytics_account_link_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_create_analytics_account_link",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_create_analytics_account_link_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_create_analytics_account_link",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.CreateAnalyticsAccountLinkRequest.pb(
            marketingplatform_admin.CreateAnalyticsAccountLinkRequest()
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
        return_value = resources.AnalyticsAccountLink.to_json(
            resources.AnalyticsAccountLink()
        )
        req.return_value.content = return_value

        request = marketingplatform_admin.CreateAnalyticsAccountLinkRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.AnalyticsAccountLink()
        post_with_metadata.return_value = resources.AnalyticsAccountLink(), metadata

        client.create_analytics_account_link(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_analytics_account_link_rest_bad_request(
    request_type=marketingplatform_admin.DeleteAnalyticsAccountLinkRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "organizations/sample1/analyticsAccountLinks/sample2"}
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
        client.delete_analytics_account_link(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.DeleteAnalyticsAccountLinkRequest,
        dict,
    ],
)
def test_delete_analytics_account_link_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "organizations/sample1/analyticsAccountLinks/sample2"}
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
        response = client.delete_analytics_account_link(request)

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_analytics_account_link_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_delete_analytics_account_link",
        ) as pre,
    ):
        pre.assert_not_called()
        pb_message = marketingplatform_admin.DeleteAnalyticsAccountLinkRequest.pb(
            marketingplatform_admin.DeleteAnalyticsAccountLinkRequest()
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

        request = marketingplatform_admin.DeleteAnalyticsAccountLinkRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata

        client.delete_analytics_account_link(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()


def test_set_property_service_level_rest_bad_request(
    request_type=marketingplatform_admin.SetPropertyServiceLevelRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "analytics_account_link": "organizations/sample1/analyticsAccountLinks/sample2"
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
        client.set_property_service_level(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.SetPropertyServiceLevelRequest,
        dict,
    ],
)
def test_set_property_service_level_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "analytics_account_link": "organizations/sample1/analyticsAccountLinks/sample2"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = marketingplatform_admin.SetPropertyServiceLevelResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = marketingplatform_admin.SetPropertyServiceLevelResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.set_property_service_level(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, marketingplatform_admin.SetPropertyServiceLevelResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_set_property_service_level_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_set_property_service_level",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_set_property_service_level_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_set_property_service_level",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.SetPropertyServiceLevelRequest.pb(
            marketingplatform_admin.SetPropertyServiceLevelRequest()
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
        return_value = marketingplatform_admin.SetPropertyServiceLevelResponse.to_json(
            marketingplatform_admin.SetPropertyServiceLevelResponse()
        )
        req.return_value.content = return_value

        request = marketingplatform_admin.SetPropertyServiceLevelRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = marketingplatform_admin.SetPropertyServiceLevelResponse()
        post_with_metadata.return_value = (
            marketingplatform_admin.SetPropertyServiceLevelResponse(),
            metadata,
        )

        client.set_property_service_level(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_report_property_usage_rest_bad_request(
    request_type=marketingplatform_admin.ReportPropertyUsageRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"organization": "organizations/sample1"}
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
        client.report_property_usage(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ReportPropertyUsageRequest,
        dict,
    ],
)
def test_report_property_usage_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"organization": "organizations/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = marketingplatform_admin.ReportPropertyUsageResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = marketingplatform_admin.ReportPropertyUsageResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.report_property_usage(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, marketingplatform_admin.ReportPropertyUsageResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_report_property_usage_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_report_property_usage",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_report_property_usage_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_report_property_usage",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.ReportPropertyUsageRequest.pb(
            marketingplatform_admin.ReportPropertyUsageRequest()
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
        return_value = marketingplatform_admin.ReportPropertyUsageResponse.to_json(
            marketingplatform_admin.ReportPropertyUsageResponse()
        )
        req.return_value.content = return_value

        request = marketingplatform_admin.ReportPropertyUsageRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = marketingplatform_admin.ReportPropertyUsageResponse()
        post_with_metadata.return_value = (
            marketingplatform_admin.ReportPropertyUsageResponse(),
            metadata,
        )

        client.report_property_usage(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_user_group_rest_bad_request(
    request_type=marketingplatform_admin.GetUserGroupRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "organizations/sample1/userGroups/sample2"}
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
        client.get_user_group(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.GetUserGroupRequest,
        dict,
    ],
)
def test_get_user_group_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "organizations/sample1/userGroups/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.UserGroup(
            name="name_value",
            display_name="display_name_value",
            description="description_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = resources.UserGroup.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_user_group(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroup)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.description == "description_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_user_group_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_get_user_group",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_get_user_group_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_get_user_group",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.GetUserGroupRequest.pb(
            marketingplatform_admin.GetUserGroupRequest()
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
        return_value = resources.UserGroup.to_json(resources.UserGroup())
        req.return_value.content = return_value

        request = marketingplatform_admin.GetUserGroupRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.UserGroup()
        post_with_metadata.return_value = resources.UserGroup(), metadata

        client.get_user_group(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_user_groups_rest_bad_request(
    request_type=marketingplatform_admin.ListUserGroupsRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1"}
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
        client.list_user_groups(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListUserGroupsRequest,
        dict,
    ],
)
def test_list_user_groups_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = marketingplatform_admin.ListUserGroupsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = marketingplatform_admin.ListUserGroupsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_user_groups(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListUserGroupsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_user_groups_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_list_user_groups",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_list_user_groups_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_list_user_groups",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.ListUserGroupsRequest.pb(
            marketingplatform_admin.ListUserGroupsRequest()
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
        return_value = marketingplatform_admin.ListUserGroupsResponse.to_json(
            marketingplatform_admin.ListUserGroupsResponse()
        )
        req.return_value.content = return_value

        request = marketingplatform_admin.ListUserGroupsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = marketingplatform_admin.ListUserGroupsResponse()
        post_with_metadata.return_value = (
            marketingplatform_admin.ListUserGroupsResponse(),
            metadata,
        )

        client.list_user_groups(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_user_group_rest_bad_request(
    request_type=marketingplatform_admin.CreateUserGroupRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1"}
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
        client.create_user_group(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.CreateUserGroupRequest,
        dict,
    ],
)
def test_create_user_group_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1"}
    request_init["user_group"] = {
        "name": "name_value",
        "display_name": "display_name_value",
        "description": "description_value",
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = marketingplatform_admin.CreateUserGroupRequest.meta.fields[
        "user_group"
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
    for field, value in request_init["user_group"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["user_group"][field])):
                    del request_init["user_group"][field][i][subfield]
            else:
                del request_init["user_group"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.UserGroup(
            name="name_value",
            display_name="display_name_value",
            description="description_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = resources.UserGroup.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_user_group(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroup)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.description == "description_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_user_group_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_create_user_group",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_create_user_group_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_create_user_group",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.CreateUserGroupRequest.pb(
            marketingplatform_admin.CreateUserGroupRequest()
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
        return_value = resources.UserGroup.to_json(resources.UserGroup())
        req.return_value.content = return_value

        request = marketingplatform_admin.CreateUserGroupRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.UserGroup()
        post_with_metadata.return_value = resources.UserGroup(), metadata

        client.create_user_group(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_user_group_rest_bad_request(
    request_type=marketingplatform_admin.UpdateUserGroupRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"user_group": {"name": "organizations/sample1/userGroups/sample2"}}
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
        client.update_user_group(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.UpdateUserGroupRequest,
        dict,
    ],
)
def test_update_user_group_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"user_group": {"name": "organizations/sample1/userGroups/sample2"}}
    request_init["user_group"] = {
        "name": "organizations/sample1/userGroups/sample2",
        "display_name": "display_name_value",
        "description": "description_value",
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = marketingplatform_admin.UpdateUserGroupRequest.meta.fields[
        "user_group"
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
    for field, value in request_init["user_group"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["user_group"][field])):
                    del request_init["user_group"][field][i][subfield]
            else:
                del request_init["user_group"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.UserGroup(
            name="name_value",
            display_name="display_name_value",
            description="description_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = resources.UserGroup.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_user_group(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroup)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.description == "description_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_user_group_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_update_user_group",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_update_user_group_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_update_user_group",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.UpdateUserGroupRequest.pb(
            marketingplatform_admin.UpdateUserGroupRequest()
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
        return_value = resources.UserGroup.to_json(resources.UserGroup())
        req.return_value.content = return_value

        request = marketingplatform_admin.UpdateUserGroupRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.UserGroup()
        post_with_metadata.return_value = resources.UserGroup(), metadata

        client.update_user_group(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_user_group_rest_bad_request(
    request_type=marketingplatform_admin.DeleteUserGroupRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "organizations/sample1/userGroups/sample2"}
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
        client.delete_user_group(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.DeleteUserGroupRequest,
        dict,
    ],
)
def test_delete_user_group_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "organizations/sample1/userGroups/sample2"}
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
        response = client.delete_user_group(request)

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_user_group_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_delete_user_group",
        ) as pre,
    ):
        pre.assert_not_called()
        pb_message = marketingplatform_admin.DeleteUserGroupRequest.pb(
            marketingplatform_admin.DeleteUserGroupRequest()
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

        request = marketingplatform_admin.DeleteUserGroupRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata

        client.delete_user_group(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()


def test_get_user_group_member_rest_bad_request(
    request_type=marketingplatform_admin.GetUserGroupMemberRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "organizations/sample1/userGroups/sample2/members/sample3"}
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
        client.get_user_group_member(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.GetUserGroupMemberRequest,
        dict,
    ],
)
def test_get_user_group_member_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "organizations/sample1/userGroups/sample2/members/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.UserGroupMember(
            name="name_value",
            membership_role=resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER,
            user_email="user_email_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = resources.UserGroupMember.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_user_group_member(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroupMember)
    assert response.name == "name_value"
    assert (
        response.membership_role
        == resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_user_group_member_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_get_user_group_member",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_get_user_group_member_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_get_user_group_member",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.GetUserGroupMemberRequest.pb(
            marketingplatform_admin.GetUserGroupMemberRequest()
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
        return_value = resources.UserGroupMember.to_json(resources.UserGroupMember())
        req.return_value.content = return_value

        request = marketingplatform_admin.GetUserGroupMemberRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.UserGroupMember()
        post_with_metadata.return_value = resources.UserGroupMember(), metadata

        client.get_user_group_member(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_user_group_members_rest_bad_request(
    request_type=marketingplatform_admin.ListUserGroupMembersRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1/userGroups/sample2"}
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
        client.list_user_group_members(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListUserGroupMembersRequest,
        dict,
    ],
)
def test_list_user_group_members_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1/userGroups/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = marketingplatform_admin.ListUserGroupMembersResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = marketingplatform_admin.ListUserGroupMembersResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_user_group_members(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListUserGroupMembersPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_user_group_members_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_list_user_group_members",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_list_user_group_members_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_list_user_group_members",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.ListUserGroupMembersRequest.pb(
            marketingplatform_admin.ListUserGroupMembersRequest()
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
        return_value = marketingplatform_admin.ListUserGroupMembersResponse.to_json(
            marketingplatform_admin.ListUserGroupMembersResponse()
        )
        req.return_value.content = return_value

        request = marketingplatform_admin.ListUserGroupMembersRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = marketingplatform_admin.ListUserGroupMembersResponse()
        post_with_metadata.return_value = (
            marketingplatform_admin.ListUserGroupMembersResponse(),
            metadata,
        )

        client.list_user_group_members(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_user_group_member_rest_bad_request(
    request_type=marketingplatform_admin.CreateUserGroupMemberRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1/userGroups/sample2"}
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
        client.create_user_group_member(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.CreateUserGroupMemberRequest,
        dict,
    ],
)
def test_create_user_group_member_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1/userGroups/sample2"}
    request_init["user_group_member"] = {
        "user_email": "user_email_value",
        "user_group": "user_group_value",
        "name": "name_value",
        "membership_role": 1,
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = marketingplatform_admin.CreateUserGroupMemberRequest.meta.fields[
        "user_group_member"
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
    for field, value in request_init["user_group_member"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["user_group_member"][field])):
                    del request_init["user_group_member"][field][i][subfield]
            else:
                del request_init["user_group_member"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.UserGroupMember(
            name="name_value",
            membership_role=resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER,
            user_email="user_email_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = resources.UserGroupMember.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_user_group_member(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroupMember)
    assert response.name == "name_value"
    assert (
        response.membership_role
        == resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_user_group_member_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_create_user_group_member",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_create_user_group_member_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_create_user_group_member",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.CreateUserGroupMemberRequest.pb(
            marketingplatform_admin.CreateUserGroupMemberRequest()
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
        return_value = resources.UserGroupMember.to_json(resources.UserGroupMember())
        req.return_value.content = return_value

        request = marketingplatform_admin.CreateUserGroupMemberRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.UserGroupMember()
        post_with_metadata.return_value = resources.UserGroupMember(), metadata

        client.create_user_group_member(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_user_group_member_rest_bad_request(
    request_type=marketingplatform_admin.UpdateUserGroupMemberRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "user_group_member": {
            "name": "organizations/sample1/userGroups/sample2/members/sample3"
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
        client.update_user_group_member(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.UpdateUserGroupMemberRequest,
        dict,
    ],
)
def test_update_user_group_member_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "user_group_member": {
            "name": "organizations/sample1/userGroups/sample2/members/sample3"
        }
    }
    request_init["user_group_member"] = {
        "user_email": "user_email_value",
        "user_group": "user_group_value",
        "name": "organizations/sample1/userGroups/sample2/members/sample3",
        "membership_role": 1,
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = marketingplatform_admin.UpdateUserGroupMemberRequest.meta.fields[
        "user_group_member"
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
    for field, value in request_init["user_group_member"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["user_group_member"][field])):
                    del request_init["user_group_member"][field][i][subfield]
            else:
                del request_init["user_group_member"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.UserGroupMember(
            name="name_value",
            membership_role=resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER,
            user_email="user_email_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = resources.UserGroupMember.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_user_group_member(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.UserGroupMember)
    assert response.name == "name_value"
    assert (
        response.membership_role
        == resources.UserGroupMember.MembershipRole.MEMBERSHIP_ROLE_OWNER
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_user_group_member_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_update_user_group_member",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_update_user_group_member_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_update_user_group_member",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.UpdateUserGroupMemberRequest.pb(
            marketingplatform_admin.UpdateUserGroupMemberRequest()
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
        return_value = resources.UserGroupMember.to_json(resources.UserGroupMember())
        req.return_value.content = return_value

        request = marketingplatform_admin.UpdateUserGroupMemberRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.UserGroupMember()
        post_with_metadata.return_value = resources.UserGroupMember(), metadata

        client.update_user_group_member(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_user_group_member_rest_bad_request(
    request_type=marketingplatform_admin.DeleteUserGroupMemberRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "organizations/sample1/userGroups/sample2/members/sample3"}
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
        client.delete_user_group_member(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.DeleteUserGroupMemberRequest,
        dict,
    ],
)
def test_delete_user_group_member_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "organizations/sample1/userGroups/sample2/members/sample3"}
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
        response = client.delete_user_group_member(request)

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_user_group_member_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_delete_user_group_member",
        ) as pre,
    ):
        pre.assert_not_called()
        pb_message = marketingplatform_admin.DeleteUserGroupMemberRequest.pb(
            marketingplatform_admin.DeleteUserGroupMemberRequest()
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

        request = marketingplatform_admin.DeleteUserGroupMemberRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata

        client.delete_user_group_member(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()


def test_get_admin_access_binding_rest_bad_request(
    request_type=marketingplatform_admin.GetAdminAccessBindingRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "organizations/sample1/adminAccessBindings/sample2"}
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
        client.get_admin_access_binding(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.GetAdminAccessBindingRequest,
        dict,
    ],
)
def test_get_admin_access_binding_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "organizations/sample1/adminAccessBindings/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.AdminAccessBinding(
            name="name_value",
            organization_roles=[resources.OrganizationRole.ORG_ADMIN_ROLE],
            user_email="user_email_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = resources.AdminAccessBinding.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_admin_access_binding(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.AdminAccessBinding)
    assert response.name == "name_value"
    assert response.organization_roles == [resources.OrganizationRole.ORG_ADMIN_ROLE]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_admin_access_binding_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_get_admin_access_binding",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_get_admin_access_binding_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_get_admin_access_binding",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.GetAdminAccessBindingRequest.pb(
            marketingplatform_admin.GetAdminAccessBindingRequest()
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
        return_value = resources.AdminAccessBinding.to_json(
            resources.AdminAccessBinding()
        )
        req.return_value.content = return_value

        request = marketingplatform_admin.GetAdminAccessBindingRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.AdminAccessBinding()
        post_with_metadata.return_value = resources.AdminAccessBinding(), metadata

        client.get_admin_access_binding(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_admin_access_bindings_rest_bad_request(
    request_type=marketingplatform_admin.ListAdminAccessBindingsRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1"}
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
        client.list_admin_access_bindings(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.ListAdminAccessBindingsRequest,
        dict,
    ],
)
def test_list_admin_access_bindings_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = marketingplatform_admin.ListAdminAccessBindingsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = marketingplatform_admin.ListAdminAccessBindingsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_admin_access_bindings(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListAdminAccessBindingsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_admin_access_bindings_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_list_admin_access_bindings",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_list_admin_access_bindings_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_list_admin_access_bindings",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.ListAdminAccessBindingsRequest.pb(
            marketingplatform_admin.ListAdminAccessBindingsRequest()
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
        return_value = marketingplatform_admin.ListAdminAccessBindingsResponse.to_json(
            marketingplatform_admin.ListAdminAccessBindingsResponse()
        )
        req.return_value.content = return_value

        request = marketingplatform_admin.ListAdminAccessBindingsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = marketingplatform_admin.ListAdminAccessBindingsResponse()
        post_with_metadata.return_value = (
            marketingplatform_admin.ListAdminAccessBindingsResponse(),
            metadata,
        )

        client.list_admin_access_bindings(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_admin_access_binding_rest_bad_request(
    request_type=marketingplatform_admin.CreateAdminAccessBindingRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1"}
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
        client.create_admin_access_binding(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.CreateAdminAccessBindingRequest,
        dict,
    ],
)
def test_create_admin_access_binding_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1"}
    request_init["admin_access_binding"] = {
        "user_email": "user_email_value",
        "user_group": "user_group_value",
        "name": "name_value",
        "organization_roles": [1],
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = marketingplatform_admin.CreateAdminAccessBindingRequest.meta.fields[
        "admin_access_binding"
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
    for field, value in request_init[
        "admin_access_binding"
    ].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["admin_access_binding"][field])):
                    del request_init["admin_access_binding"][field][i][subfield]
            else:
                del request_init["admin_access_binding"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.AdminAccessBinding(
            name="name_value",
            organization_roles=[resources.OrganizationRole.ORG_ADMIN_ROLE],
            user_email="user_email_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = resources.AdminAccessBinding.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_admin_access_binding(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.AdminAccessBinding)
    assert response.name == "name_value"
    assert response.organization_roles == [resources.OrganizationRole.ORG_ADMIN_ROLE]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_admin_access_binding_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_create_admin_access_binding",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_create_admin_access_binding_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_create_admin_access_binding",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.CreateAdminAccessBindingRequest.pb(
            marketingplatform_admin.CreateAdminAccessBindingRequest()
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
        return_value = resources.AdminAccessBinding.to_json(
            resources.AdminAccessBinding()
        )
        req.return_value.content = return_value

        request = marketingplatform_admin.CreateAdminAccessBindingRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.AdminAccessBinding()
        post_with_metadata.return_value = resources.AdminAccessBinding(), metadata

        client.create_admin_access_binding(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_admin_access_binding_rest_bad_request(
    request_type=marketingplatform_admin.UpdateAdminAccessBindingRequest,
):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "admin_access_binding": {
            "name": "organizations/sample1/adminAccessBindings/sample2"
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
        client.update_admin_access_binding(request)


@pytest.mark.parametrize(
    "request_type",
    [
        marketingplatform_admin.UpdateAdminAccessBindingRequest,
        dict,
    ],
)
def test_update_admin_access_binding_rest_call_success(request_type):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "admin_access_binding": {
            "name": "organizations/sample1/adminAccessBindings/sample2"
        }
    }
    request_init["admin_access_binding"] = {
        "user_email": "user_email_value",
        "user_group": "user_group_value",
        "name": "organizations/sample1/adminAccessBindings/sample2",
        "organization_roles": [1],
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = marketingplatform_admin.UpdateAdminAccessBindingRequest.meta.fields[
        "admin_access_binding"
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
    for field, value in request_init[
        "admin_access_binding"
    ].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["admin_access_binding"][field])):
                    del request_init["admin_access_binding"][field][i][subfield]
            else:
                del request_init["admin_access_binding"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = resources.AdminAccessBinding(
            name="name_value",
            organization_roles=[resources.OrganizationRole.ORG_ADMIN_ROLE],
            user_email="user_email_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = resources.AdminAccessBinding.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_admin_access_binding(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, resources.AdminAccessBinding)
    assert response.name == "name_value"
    assert response.organization_roles == [resources.OrganizationRole.ORG_ADMIN_ROLE]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_admin_access_binding_rest_interceptors(null_interceptor):
    transport = transports.MarketingplatformAdminServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.MarketingplatformAdminServiceRestInterceptor(),
    )
    client = MarketingplatformAdminServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_update_admin_access_binding",
        ) as post,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "post_update_admin_access_binding_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.MarketingplatformAdminServiceRestInterceptor,
            "pre_update_admin_access_binding",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = marketingplatform_admin.UpdateAdminAccessBindingRequest.pb(
            marketingplatform_admin.UpdateAdminAccessBindingRequest()
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
        return_value = resources.AdminAccessBinding.to_json(
            resources.AdminAccessBinding()
        )
        req.return_value.content = return_value

        request = marketingplatform_admin.UpdateAdminAccessBindingRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = resources.AdminAccessBinding()
        post_with_metadata.return_value = resources.AdminAccessBinding(), metadata

        client.update_admin_access_binding(
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
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_organization_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_organization), "__call__") as call:
        client.get_organization(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetOrganizationRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_organizations_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_organizations), "__call__"
    ) as call:
        client.list_organizations(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListOrganizationsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_find_sales_partner_managed_clients_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.find_sales_partner_managed_clients), "__call__"
    ) as call:
        client.find_sales_partner_managed_clients(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.FindSalesPartnerManagedClientsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_analytics_account_links_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_analytics_account_links), "__call__"
    ) as call:
        client.list_analytics_account_links(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListAnalyticsAccountLinksRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_analytics_account_link_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_analytics_account_link), "__call__"
    ) as call:
        client.create_analytics_account_link(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateAnalyticsAccountLinkRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_analytics_account_link_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_analytics_account_link), "__call__"
    ) as call:
        client.delete_analytics_account_link(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.DeleteAnalyticsAccountLinkRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_set_property_service_level_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.set_property_service_level), "__call__"
    ) as call:
        client.set_property_service_level(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.SetPropertyServiceLevelRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_report_property_usage_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.report_property_usage), "__call__"
    ) as call:
        client.report_property_usage(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ReportPropertyUsageRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_user_group_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_user_group), "__call__") as call:
        client.get_user_group(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetUserGroupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_user_groups_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_user_groups), "__call__") as call:
        client.list_user_groups(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListUserGroupsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_user_group_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group), "__call__"
    ) as call:
        client.create_user_group(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateUserGroupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_user_group_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group), "__call__"
    ) as call:
        client.update_user_group(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.UpdateUserGroupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_user_group_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group), "__call__"
    ) as call:
        client.delete_user_group(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.DeleteUserGroupRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_user_group_member_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_user_group_member), "__call__"
    ) as call:
        client.get_user_group_member(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetUserGroupMemberRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_user_group_members_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_user_group_members), "__call__"
    ) as call:
        client.list_user_group_members(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListUserGroupMembersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_user_group_member_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_user_group_member), "__call__"
    ) as call:
        client.create_user_group_member(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateUserGroupMemberRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_user_group_member_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_user_group_member), "__call__"
    ) as call:
        client.update_user_group_member(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.UpdateUserGroupMemberRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_user_group_member_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_user_group_member), "__call__"
    ) as call:
        client.delete_user_group_member(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.DeleteUserGroupMemberRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_admin_access_binding_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_admin_access_binding), "__call__"
    ) as call:
        client.get_admin_access_binding(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.GetAdminAccessBindingRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_admin_access_bindings_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_admin_access_bindings), "__call__"
    ) as call:
        client.list_admin_access_bindings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.ListAdminAccessBindingsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_admin_access_binding_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_admin_access_binding), "__call__"
    ) as call:
        client.create_admin_access_binding(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.CreateAdminAccessBindingRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_admin_access_binding_empty_call_rest():
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_admin_access_binding), "__call__"
    ) as call:
        client.update_admin_access_binding(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = marketingplatform_admin.UpdateAdminAccessBindingRequest()
        assert args[0] == request_msg


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.MarketingplatformAdminServiceGrpcTransport,
    )


def test_marketingplatform_admin_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.MarketingplatformAdminServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_marketingplatform_admin_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.ads.marketingplatform_admin_v1alpha.services.marketingplatform_admin_service.transports.MarketingplatformAdminServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.MarketingplatformAdminServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "get_organization",
        "list_organizations",
        "find_sales_partner_managed_clients",
        "list_analytics_account_links",
        "create_analytics_account_link",
        "delete_analytics_account_link",
        "set_property_service_level",
        "report_property_usage",
        "get_user_group",
        "list_user_groups",
        "create_user_group",
        "update_user_group",
        "delete_user_group",
        "get_user_group_member",
        "list_user_group_members",
        "create_user_group_member",
        "update_user_group_member",
        "delete_user_group_member",
        "get_admin_access_binding",
        "list_admin_access_bindings",
        "create_admin_access_binding",
        "update_admin_access_binding",
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


def test_marketingplatform_admin_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.ads.marketingplatform_admin_v1alpha.services.marketingplatform_admin_service.transports.MarketingplatformAdminServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.MarketingplatformAdminServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/marketingplatformadmin.analytics.read",
                "https://www.googleapis.com/auth/marketingplatformadmin.analytics.update",
            ),
            quota_project_id="octopus",
        )


def test_marketingplatform_admin_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.ads.marketingplatform_admin_v1alpha.services.marketingplatform_admin_service.transports.MarketingplatformAdminServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.MarketingplatformAdminServiceTransport()
        adc.assert_called_once()


def test_marketingplatform_admin_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        MarketingplatformAdminServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/marketingplatformadmin.analytics.read",
                "https://www.googleapis.com/auth/marketingplatformadmin.analytics.update",
            ),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.MarketingplatformAdminServiceGrpcTransport,
        transports.MarketingplatformAdminServiceGrpcAsyncIOTransport,
    ],
)
def test_marketingplatform_admin_service_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=(
                "https://www.googleapis.com/auth/marketingplatformadmin.analytics.read",
                "https://www.googleapis.com/auth/marketingplatformadmin.analytics.update",
            ),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.MarketingplatformAdminServiceGrpcTransport,
        transports.MarketingplatformAdminServiceGrpcAsyncIOTransport,
        transports.MarketingplatformAdminServiceRestTransport,
    ],
)
def test_marketingplatform_admin_service_transport_auth_gdch_credentials(
    transport_class,
):
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
        (transports.MarketingplatformAdminServiceGrpcTransport, grpc_helpers),
        (
            transports.MarketingplatformAdminServiceGrpcAsyncIOTransport,
            grpc_helpers_async,
        ),
    ],
)
def test_marketingplatform_admin_service_transport_create_channel(
    transport_class, grpc_helpers
):
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
            "marketingplatformadmin.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=(
                "https://www.googleapis.com/auth/marketingplatformadmin.analytics.read",
                "https://www.googleapis.com/auth/marketingplatformadmin.analytics.update",
            ),
            scopes=["1", "2"],
            default_host="marketingplatformadmin.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.MarketingplatformAdminServiceGrpcTransport,
        transports.MarketingplatformAdminServiceGrpcAsyncIOTransport,
    ],
)
def test_marketingplatform_admin_service_grpc_transport_client_cert_source_for_mtls(
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


def test_marketingplatform_admin_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.MarketingplatformAdminServiceRestTransport(
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
def test_marketingplatform_admin_service_host_no_port(transport_name):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="marketingplatformadmin.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "marketingplatformadmin.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://marketingplatformadmin.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_marketingplatform_admin_service_host_with_port(transport_name):
    client = MarketingplatformAdminServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="marketingplatformadmin.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "marketingplatformadmin.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://marketingplatformadmin.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_marketingplatform_admin_service_client_transport_session_collision(
    transport_name,
):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = MarketingplatformAdminServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = MarketingplatformAdminServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.get_organization._session
    session2 = client2.transport.get_organization._session
    assert session1 != session2
    session1 = client1.transport.list_organizations._session
    session2 = client2.transport.list_organizations._session
    assert session1 != session2
    session1 = client1.transport.find_sales_partner_managed_clients._session
    session2 = client2.transport.find_sales_partner_managed_clients._session
    assert session1 != session2
    session1 = client1.transport.list_analytics_account_links._session
    session2 = client2.transport.list_analytics_account_links._session
    assert session1 != session2
    session1 = client1.transport.create_analytics_account_link._session
    session2 = client2.transport.create_analytics_account_link._session
    assert session1 != session2
    session1 = client1.transport.delete_analytics_account_link._session
    session2 = client2.transport.delete_analytics_account_link._session
    assert session1 != session2
    session1 = client1.transport.set_property_service_level._session
    session2 = client2.transport.set_property_service_level._session
    assert session1 != session2
    session1 = client1.transport.report_property_usage._session
    session2 = client2.transport.report_property_usage._session
    assert session1 != session2
    session1 = client1.transport.get_user_group._session
    session2 = client2.transport.get_user_group._session
    assert session1 != session2
    session1 = client1.transport.list_user_groups._session
    session2 = client2.transport.list_user_groups._session
    assert session1 != session2
    session1 = client1.transport.create_user_group._session
    session2 = client2.transport.create_user_group._session
    assert session1 != session2
    session1 = client1.transport.update_user_group._session
    session2 = client2.transport.update_user_group._session
    assert session1 != session2
    session1 = client1.transport.delete_user_group._session
    session2 = client2.transport.delete_user_group._session
    assert session1 != session2
    session1 = client1.transport.get_user_group_member._session
    session2 = client2.transport.get_user_group_member._session
    assert session1 != session2
    session1 = client1.transport.list_user_group_members._session
    session2 = client2.transport.list_user_group_members._session
    assert session1 != session2
    session1 = client1.transport.create_user_group_member._session
    session2 = client2.transport.create_user_group_member._session
    assert session1 != session2
    session1 = client1.transport.update_user_group_member._session
    session2 = client2.transport.update_user_group_member._session
    assert session1 != session2
    session1 = client1.transport.delete_user_group_member._session
    session2 = client2.transport.delete_user_group_member._session
    assert session1 != session2
    session1 = client1.transport.get_admin_access_binding._session
    session2 = client2.transport.get_admin_access_binding._session
    assert session1 != session2
    session1 = client1.transport.list_admin_access_bindings._session
    session2 = client2.transport.list_admin_access_bindings._session
    assert session1 != session2
    session1 = client1.transport.create_admin_access_binding._session
    session2 = client2.transport.create_admin_access_binding._session
    assert session1 != session2
    session1 = client1.transport.update_admin_access_binding._session
    session2 = client2.transport.update_admin_access_binding._session
    assert session1 != session2


def test_marketingplatform_admin_service_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.MarketingplatformAdminServiceGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_marketingplatform_admin_service_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.MarketingplatformAdminServiceGrpcAsyncIOTransport(
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
        transports.MarketingplatformAdminServiceGrpcTransport,
        transports.MarketingplatformAdminServiceGrpcAsyncIOTransport,
    ],
)
def test_marketingplatform_admin_service_transport_channel_mtls_with_client_cert_source(
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
        transports.MarketingplatformAdminServiceGrpcTransport,
        transports.MarketingplatformAdminServiceGrpcAsyncIOTransport,
    ],
)
def test_marketingplatform_admin_service_transport_channel_mtls_with_adc(
    transport_class,
):
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


def test_account_path():
    account = "squid"
    expected = "accounts/{account}".format(
        account=account,
    )
    actual = MarketingplatformAdminServiceClient.account_path(account)
    assert expected == actual


def test_parse_account_path():
    expected = {
        "account": "clam",
    }
    path = MarketingplatformAdminServiceClient.account_path(**expected)

    # Check that the path construction is reversible.
    actual = MarketingplatformAdminServiceClient.parse_account_path(path)
    assert expected == actual


def test_admin_access_binding_path():
    organization = "whelk"
    admin_access_binding = "octopus"
    expected = "organizations/{organization}/adminAccessBindings/{admin_access_binding}".format(
        organization=organization,
        admin_access_binding=admin_access_binding,
    )
    actual = MarketingplatformAdminServiceClient.admin_access_binding_path(
        organization, admin_access_binding
    )
    assert expected == actual


def test_parse_admin_access_binding_path():
    expected = {
        "organization": "oyster",
        "admin_access_binding": "nudibranch",
    }
    path = MarketingplatformAdminServiceClient.admin_access_binding_path(**expected)

    # Check that the path construction is reversible.
    actual = MarketingplatformAdminServiceClient.parse_admin_access_binding_path(path)
    assert expected == actual


def test_analytics_account_link_path():
    organization = "cuttlefish"
    analytics_account_link = "mussel"
    expected = "organizations/{organization}/analyticsAccountLinks/{analytics_account_link}".format(
        organization=organization,
        analytics_account_link=analytics_account_link,
    )
    actual = MarketingplatformAdminServiceClient.analytics_account_link_path(
        organization, analytics_account_link
    )
    assert expected == actual


def test_parse_analytics_account_link_path():
    expected = {
        "organization": "winkle",
        "analytics_account_link": "nautilus",
    }
    path = MarketingplatformAdminServiceClient.analytics_account_link_path(**expected)

    # Check that the path construction is reversible.
    actual = MarketingplatformAdminServiceClient.parse_analytics_account_link_path(path)
    assert expected == actual


def test_organization_path():
    organization = "scallop"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = MarketingplatformAdminServiceClient.organization_path(organization)
    assert expected == actual


def test_parse_organization_path():
    expected = {
        "organization": "abalone",
    }
    path = MarketingplatformAdminServiceClient.organization_path(**expected)

    # Check that the path construction is reversible.
    actual = MarketingplatformAdminServiceClient.parse_organization_path(path)
    assert expected == actual


def test_property_path():
    property = "squid"
    expected = "properties/{property}".format(
        property=property,
    )
    actual = MarketingplatformAdminServiceClient.property_path(property)
    assert expected == actual


def test_parse_property_path():
    expected = {
        "property": "clam",
    }
    path = MarketingplatformAdminServiceClient.property_path(**expected)

    # Check that the path construction is reversible.
    actual = MarketingplatformAdminServiceClient.parse_property_path(path)
    assert expected == actual


def test_user_group_path():
    organization = "whelk"
    user_group = "octopus"
    expected = "organizations/{organization}/userGroups/{user_group}".format(
        organization=organization,
        user_group=user_group,
    )
    actual = MarketingplatformAdminServiceClient.user_group_path(
        organization, user_group
    )
    assert expected == actual


def test_parse_user_group_path():
    expected = {
        "organization": "oyster",
        "user_group": "nudibranch",
    }
    path = MarketingplatformAdminServiceClient.user_group_path(**expected)

    # Check that the path construction is reversible.
    actual = MarketingplatformAdminServiceClient.parse_user_group_path(path)
    assert expected == actual


def test_user_group_member_path():
    organization = "cuttlefish"
    user_group = "mussel"
    member = "winkle"
    expected = (
        "organizations/{organization}/userGroups/{user_group}/members/{member}".format(
            organization=organization,
            user_group=user_group,
            member=member,
        )
    )
    actual = MarketingplatformAdminServiceClient.user_group_member_path(
        organization, user_group, member
    )
    assert expected == actual


def test_parse_user_group_member_path():
    expected = {
        "organization": "nautilus",
        "user_group": "scallop",
        "member": "abalone",
    }
    path = MarketingplatformAdminServiceClient.user_group_member_path(**expected)

    # Check that the path construction is reversible.
    actual = MarketingplatformAdminServiceClient.parse_user_group_member_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = MarketingplatformAdminServiceClient.common_billing_account_path(
        billing_account
    )
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = MarketingplatformAdminServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = MarketingplatformAdminServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = MarketingplatformAdminServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = MarketingplatformAdminServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = MarketingplatformAdminServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = MarketingplatformAdminServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = MarketingplatformAdminServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = MarketingplatformAdminServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = MarketingplatformAdminServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = MarketingplatformAdminServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = MarketingplatformAdminServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = MarketingplatformAdminServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = MarketingplatformAdminServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = MarketingplatformAdminServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.MarketingplatformAdminServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = MarketingplatformAdminServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.MarketingplatformAdminServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = MarketingplatformAdminServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_grpc():
    client = MarketingplatformAdminServiceClient(
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
    client = MarketingplatformAdminServiceAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = MarketingplatformAdminServiceClient(
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
        client = MarketingplatformAdminServiceClient(
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
        (
            MarketingplatformAdminServiceClient,
            transports.MarketingplatformAdminServiceGrpcTransport,
        ),
        (
            MarketingplatformAdminServiceAsyncClient,
            transports.MarketingplatformAdminServiceGrpcAsyncIOTransport,
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
