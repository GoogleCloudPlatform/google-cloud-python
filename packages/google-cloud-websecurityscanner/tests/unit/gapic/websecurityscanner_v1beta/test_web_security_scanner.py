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
from google.oauth2 import service_account

from google.cloud.websecurityscanner_v1beta.services.web_security_scanner import (
    WebSecurityScannerAsyncClient,
    WebSecurityScannerClient,
    pagers,
    transports,
)
from google.cloud.websecurityscanner_v1beta.types import (
    crawled_url,
    finding,
    finding_addon,
    finding_type_stats,
    scan_config,
    scan_config_error,
    scan_run,
    scan_run_error_trace,
    scan_run_warning_trace,
    web_security_scanner,
)
from google.cloud.websecurityscanner_v1beta.types import scan_config as gcw_scan_config

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

    assert WebSecurityScannerClient._get_client_cert_source(None, False) is None
    assert (
        WebSecurityScannerClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        WebSecurityScannerClient._get_client_cert_source(
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
                WebSecurityScannerClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                WebSecurityScannerClient._get_client_cert_source(
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
    client = WebSecurityScannerClient(credentials=cred)
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
    client = WebSecurityScannerClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (WebSecurityScannerClient, "grpc"),
        (WebSecurityScannerAsyncClient, "grpc_asyncio"),
        (WebSecurityScannerClient, "rest"),
    ],
)
def test_web_security_scanner_client_from_service_account_info(
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
            "websecurityscanner.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://websecurityscanner.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.WebSecurityScannerGrpcTransport, "grpc"),
        (transports.WebSecurityScannerGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.WebSecurityScannerRestTransport, "rest"),
    ],
)
def test_web_security_scanner_client_service_account_always_use_jwt(
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
        (WebSecurityScannerClient, "grpc"),
        (WebSecurityScannerAsyncClient, "grpc_asyncio"),
        (WebSecurityScannerClient, "rest"),
    ],
)
def test_web_security_scanner_client_from_service_account_file(
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
            "websecurityscanner.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://websecurityscanner.googleapis.com"
        )


def test_web_security_scanner_client_get_transport_class():
    transport = WebSecurityScannerClient.get_transport_class()
    available_transports = [
        transports.WebSecurityScannerGrpcTransport,
        transports.WebSecurityScannerRestTransport,
    ]
    assert transport in available_transports

    transport = WebSecurityScannerClient.get_transport_class("grpc")
    assert transport == transports.WebSecurityScannerGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (WebSecurityScannerClient, transports.WebSecurityScannerGrpcTransport, "grpc"),
        (
            WebSecurityScannerAsyncClient,
            transports.WebSecurityScannerGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (WebSecurityScannerClient, transports.WebSecurityScannerRestTransport, "rest"),
    ],
)
@mock.patch.object(
    WebSecurityScannerClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(WebSecurityScannerClient),
)
@mock.patch.object(
    WebSecurityScannerAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(WebSecurityScannerAsyncClient),
)
def test_web_security_scanner_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(WebSecurityScannerClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(WebSecurityScannerClient, "get_transport_class") as gtc:
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
            WebSecurityScannerClient,
            transports.WebSecurityScannerGrpcTransport,
            "grpc",
            "true",
        ),
        (
            WebSecurityScannerAsyncClient,
            transports.WebSecurityScannerGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            WebSecurityScannerClient,
            transports.WebSecurityScannerGrpcTransport,
            "grpc",
            "false",
        ),
        (
            WebSecurityScannerAsyncClient,
            transports.WebSecurityScannerGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (
            WebSecurityScannerClient,
            transports.WebSecurityScannerRestTransport,
            "rest",
            "true",
        ),
        (
            WebSecurityScannerClient,
            transports.WebSecurityScannerRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    WebSecurityScannerClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(WebSecurityScannerClient),
)
@mock.patch.object(
    WebSecurityScannerAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(WebSecurityScannerAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_web_security_scanner_client_mtls_env_auto(
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
    "client_class", [WebSecurityScannerClient, WebSecurityScannerAsyncClient]
)
@mock.patch.object(
    WebSecurityScannerClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(WebSecurityScannerClient),
)
@mock.patch.object(
    WebSecurityScannerAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(WebSecurityScannerAsyncClient),
)
def test_web_security_scanner_client_get_mtls_endpoint_and_cert_source(client_class):
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
    "client_class", [WebSecurityScannerClient, WebSecurityScannerAsyncClient]
)
@mock.patch.object(
    WebSecurityScannerClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(WebSecurityScannerClient),
)
@mock.patch.object(
    WebSecurityScannerAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(WebSecurityScannerAsyncClient),
)
def test_web_security_scanner_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = WebSecurityScannerClient._DEFAULT_UNIVERSE
    default_endpoint = WebSecurityScannerClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = WebSecurityScannerClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
        (WebSecurityScannerClient, transports.WebSecurityScannerGrpcTransport, "grpc"),
        (
            WebSecurityScannerAsyncClient,
            transports.WebSecurityScannerGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (WebSecurityScannerClient, transports.WebSecurityScannerRestTransport, "rest"),
    ],
)
def test_web_security_scanner_client_client_options_scopes(
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
            WebSecurityScannerClient,
            transports.WebSecurityScannerGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            WebSecurityScannerAsyncClient,
            transports.WebSecurityScannerGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (
            WebSecurityScannerClient,
            transports.WebSecurityScannerRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_web_security_scanner_client_client_options_credentials_file(
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


def test_web_security_scanner_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.websecurityscanner_v1beta.services.web_security_scanner.transports.WebSecurityScannerGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = WebSecurityScannerClient(
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
            WebSecurityScannerClient,
            transports.WebSecurityScannerGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            WebSecurityScannerAsyncClient,
            transports.WebSecurityScannerGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_web_security_scanner_client_create_channel_credentials_file(
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
            "websecurityscanner.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=None,
            default_host="websecurityscanner.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.CreateScanConfigRequest(),
        {},
    ],
)
def test_create_scan_config(request_type, transport: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcw_scan_config.ScanConfig(
            name="name_value",
            display_name="display_name_value",
            max_qps=761,
            starting_urls=["starting_urls_value"],
            user_agent=gcw_scan_config.ScanConfig.UserAgent.CHROME_LINUX,
            blacklist_patterns=["blacklist_patterns_value"],
            target_platforms=[gcw_scan_config.ScanConfig.TargetPlatform.APP_ENGINE],
            export_to_security_command_center=gcw_scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED,
            risk_level=gcw_scan_config.ScanConfig.RiskLevel.NORMAL,
        )
        response = client.create_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.CreateScanConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcw_scan_config.ScanConfig)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.max_qps == 761
    assert response.starting_urls == ["starting_urls_value"]
    assert response.user_agent == gcw_scan_config.ScanConfig.UserAgent.CHROME_LINUX
    assert response.blacklist_patterns == ["blacklist_patterns_value"]
    assert response.target_platforms == [
        gcw_scan_config.ScanConfig.TargetPlatform.APP_ENGINE
    ]
    assert (
        response.export_to_security_command_center
        == gcw_scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED
    )
    assert response.risk_level == gcw_scan_config.ScanConfig.RiskLevel.NORMAL


def test_create_scan_config_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = web_security_scanner.CreateScanConfigRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_scan_config), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_scan_config(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.CreateScanConfigRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_create_scan_config_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_scan_config in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_scan_config] = (
            mock_rpc
        )
        request = {}
        client.create_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_scan_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_scan_config_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = WebSecurityScannerAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_scan_config
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_scan_config
        ] = mock_rpc

        request = {}
        await client.create_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.create_scan_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.CreateScanConfigRequest(),
        {},
    ],
)
async def test_create_scan_config_async(request_type, transport: str = "grpc_asyncio"):
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcw_scan_config.ScanConfig(
                name="name_value",
                display_name="display_name_value",
                max_qps=761,
                starting_urls=["starting_urls_value"],
                user_agent=gcw_scan_config.ScanConfig.UserAgent.CHROME_LINUX,
                blacklist_patterns=["blacklist_patterns_value"],
                target_platforms=[gcw_scan_config.ScanConfig.TargetPlatform.APP_ENGINE],
                export_to_security_command_center=gcw_scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED,
                risk_level=gcw_scan_config.ScanConfig.RiskLevel.NORMAL,
            )
        )
        response = await client.create_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.CreateScanConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcw_scan_config.ScanConfig)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.max_qps == 761
    assert response.starting_urls == ["starting_urls_value"]
    assert response.user_agent == gcw_scan_config.ScanConfig.UserAgent.CHROME_LINUX
    assert response.blacklist_patterns == ["blacklist_patterns_value"]
    assert response.target_platforms == [
        gcw_scan_config.ScanConfig.TargetPlatform.APP_ENGINE
    ]
    assert (
        response.export_to_security_command_center
        == gcw_scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED
    )
    assert response.risk_level == gcw_scan_config.ScanConfig.RiskLevel.NORMAL


def test_create_scan_config_field_headers():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.CreateScanConfigRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_scan_config), "__call__"
    ) as call:
        call.return_value = gcw_scan_config.ScanConfig()
        client.create_scan_config(request)

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
async def test_create_scan_config_field_headers_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.CreateScanConfigRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_scan_config), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcw_scan_config.ScanConfig()
        )
        await client.create_scan_config(request)

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


def test_create_scan_config_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcw_scan_config.ScanConfig()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_scan_config(
            parent="parent_value",
            scan_config=gcw_scan_config.ScanConfig(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].scan_config
        mock_val = gcw_scan_config.ScanConfig(name="name_value")
        assert arg == mock_val


def test_create_scan_config_flattened_error():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_scan_config(
            web_security_scanner.CreateScanConfigRequest(),
            parent="parent_value",
            scan_config=gcw_scan_config.ScanConfig(name="name_value"),
        )


@pytest.mark.asyncio
async def test_create_scan_config_flattened_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcw_scan_config.ScanConfig()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcw_scan_config.ScanConfig()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_scan_config(
            parent="parent_value",
            scan_config=gcw_scan_config.ScanConfig(name="name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].scan_config
        mock_val = gcw_scan_config.ScanConfig(name="name_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_scan_config_flattened_error_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_scan_config(
            web_security_scanner.CreateScanConfigRequest(),
            parent="parent_value",
            scan_config=gcw_scan_config.ScanConfig(name="name_value"),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.DeleteScanConfigRequest(),
        {},
    ],
)
def test_delete_scan_config(request_type, transport: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.DeleteScanConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_scan_config_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = web_security_scanner.DeleteScanConfigRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_scan_config), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.delete_scan_config(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.DeleteScanConfigRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_delete_scan_config_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_scan_config in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_scan_config] = (
            mock_rpc
        )
        request = {}
        client.delete_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_scan_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_delete_scan_config_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = WebSecurityScannerAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.delete_scan_config
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.delete_scan_config
        ] = mock_rpc

        request = {}
        await client.delete_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.delete_scan_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.DeleteScanConfigRequest(),
        {},
    ],
)
async def test_delete_scan_config_async(request_type, transport: str = "grpc_asyncio"):
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.DeleteScanConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_scan_config_field_headers():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.DeleteScanConfigRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_scan_config), "__call__"
    ) as call:
        call.return_value = None
        client.delete_scan_config(request)

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
async def test_delete_scan_config_field_headers_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.DeleteScanConfigRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_scan_config), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_scan_config(request)

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


def test_delete_scan_config_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_scan_config(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_scan_config_flattened_error():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_scan_config(
            web_security_scanner.DeleteScanConfigRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_scan_config_flattened_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_scan_config(
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
async def test_delete_scan_config_flattened_error_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_scan_config(
            web_security_scanner.DeleteScanConfigRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.GetScanConfigRequest(),
        {},
    ],
)
def test_get_scan_config(request_type, transport: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_config), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = scan_config.ScanConfig(
            name="name_value",
            display_name="display_name_value",
            max_qps=761,
            starting_urls=["starting_urls_value"],
            user_agent=scan_config.ScanConfig.UserAgent.CHROME_LINUX,
            blacklist_patterns=["blacklist_patterns_value"],
            target_platforms=[scan_config.ScanConfig.TargetPlatform.APP_ENGINE],
            export_to_security_command_center=scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED,
            risk_level=scan_config.ScanConfig.RiskLevel.NORMAL,
        )
        response = client.get_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.GetScanConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, scan_config.ScanConfig)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.max_qps == 761
    assert response.starting_urls == ["starting_urls_value"]
    assert response.user_agent == scan_config.ScanConfig.UserAgent.CHROME_LINUX
    assert response.blacklist_patterns == ["blacklist_patterns_value"]
    assert response.target_platforms == [
        scan_config.ScanConfig.TargetPlatform.APP_ENGINE
    ]
    assert (
        response.export_to_security_command_center
        == scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED
    )
    assert response.risk_level == scan_config.ScanConfig.RiskLevel.NORMAL


def test_get_scan_config_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = web_security_scanner.GetScanConfigRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_config), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_scan_config(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.GetScanConfigRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_scan_config_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_scan_config in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_scan_config] = mock_rpc
        request = {}
        client.get_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_scan_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_scan_config_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = WebSecurityScannerAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_scan_config
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_scan_config
        ] = mock_rpc

        request = {}
        await client.get_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_scan_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.GetScanConfigRequest(),
        {},
    ],
)
async def test_get_scan_config_async(request_type, transport: str = "grpc_asyncio"):
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_config), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            scan_config.ScanConfig(
                name="name_value",
                display_name="display_name_value",
                max_qps=761,
                starting_urls=["starting_urls_value"],
                user_agent=scan_config.ScanConfig.UserAgent.CHROME_LINUX,
                blacklist_patterns=["blacklist_patterns_value"],
                target_platforms=[scan_config.ScanConfig.TargetPlatform.APP_ENGINE],
                export_to_security_command_center=scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED,
                risk_level=scan_config.ScanConfig.RiskLevel.NORMAL,
            )
        )
        response = await client.get_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.GetScanConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, scan_config.ScanConfig)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.max_qps == 761
    assert response.starting_urls == ["starting_urls_value"]
    assert response.user_agent == scan_config.ScanConfig.UserAgent.CHROME_LINUX
    assert response.blacklist_patterns == ["blacklist_patterns_value"]
    assert response.target_platforms == [
        scan_config.ScanConfig.TargetPlatform.APP_ENGINE
    ]
    assert (
        response.export_to_security_command_center
        == scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED
    )
    assert response.risk_level == scan_config.ScanConfig.RiskLevel.NORMAL


def test_get_scan_config_field_headers():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.GetScanConfigRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_config), "__call__") as call:
        call.return_value = scan_config.ScanConfig()
        client.get_scan_config(request)

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
async def test_get_scan_config_field_headers_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.GetScanConfigRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_config), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            scan_config.ScanConfig()
        )
        await client.get_scan_config(request)

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


def test_get_scan_config_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_config), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = scan_config.ScanConfig()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_scan_config(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_scan_config_flattened_error():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_scan_config(
            web_security_scanner.GetScanConfigRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_scan_config_flattened_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_config), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = scan_config.ScanConfig()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            scan_config.ScanConfig()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_scan_config(
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
async def test_get_scan_config_flattened_error_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_scan_config(
            web_security_scanner.GetScanConfigRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListScanConfigsRequest(),
        {},
    ],
)
def test_list_scan_configs(request_type, transport: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_configs), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListScanConfigsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_scan_configs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.ListScanConfigsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListScanConfigsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_scan_configs_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = web_security_scanner.ListScanConfigsRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_configs), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_scan_configs(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListScanConfigsRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_scan_configs_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_scan_configs in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_scan_configs] = (
            mock_rpc
        )
        request = {}
        client.list_scan_configs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_scan_configs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_scan_configs_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = WebSecurityScannerAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_scan_configs
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_scan_configs
        ] = mock_rpc

        request = {}
        await client.list_scan_configs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_scan_configs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListScanConfigsRequest(),
        {},
    ],
)
async def test_list_scan_configs_async(request_type, transport: str = "grpc_asyncio"):
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_configs), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListScanConfigsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_scan_configs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.ListScanConfigsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListScanConfigsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_scan_configs_field_headers():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.ListScanConfigsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_configs), "__call__"
    ) as call:
        call.return_value = web_security_scanner.ListScanConfigsResponse()
        client.list_scan_configs(request)

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
async def test_list_scan_configs_field_headers_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.ListScanConfigsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_configs), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListScanConfigsResponse()
        )
        await client.list_scan_configs(request)

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


def test_list_scan_configs_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_configs), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListScanConfigsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_scan_configs(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_scan_configs_flattened_error():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_scan_configs(
            web_security_scanner.ListScanConfigsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_scan_configs_flattened_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_configs), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListScanConfigsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListScanConfigsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_scan_configs(
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
async def test_list_scan_configs_flattened_error_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_scan_configs(
            web_security_scanner.ListScanConfigsRequest(),
            parent="parent_value",
        )


def test_list_scan_configs_pager(transport_name: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_configs), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[],
                next_page_token="def",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
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
        pager = client.list_scan_configs(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, scan_config.ScanConfig) for i in results)


def test_list_scan_configs_pages(transport_name: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_configs), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[],
                next_page_token="def",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_scan_configs(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_scan_configs_async_pager():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_configs),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[],
                next_page_token="def",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_scan_configs(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, scan_config.ScanConfig) for i in responses)


@pytest.mark.asyncio
async def test_list_scan_configs_async_pages():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_configs),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[],
                next_page_token="def",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_scan_configs(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.UpdateScanConfigRequest(),
        {},
    ],
)
def test_update_scan_config(request_type, transport: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcw_scan_config.ScanConfig(
            name="name_value",
            display_name="display_name_value",
            max_qps=761,
            starting_urls=["starting_urls_value"],
            user_agent=gcw_scan_config.ScanConfig.UserAgent.CHROME_LINUX,
            blacklist_patterns=["blacklist_patterns_value"],
            target_platforms=[gcw_scan_config.ScanConfig.TargetPlatform.APP_ENGINE],
            export_to_security_command_center=gcw_scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED,
            risk_level=gcw_scan_config.ScanConfig.RiskLevel.NORMAL,
        )
        response = client.update_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.UpdateScanConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcw_scan_config.ScanConfig)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.max_qps == 761
    assert response.starting_urls == ["starting_urls_value"]
    assert response.user_agent == gcw_scan_config.ScanConfig.UserAgent.CHROME_LINUX
    assert response.blacklist_patterns == ["blacklist_patterns_value"]
    assert response.target_platforms == [
        gcw_scan_config.ScanConfig.TargetPlatform.APP_ENGINE
    ]
    assert (
        response.export_to_security_command_center
        == gcw_scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED
    )
    assert response.risk_level == gcw_scan_config.ScanConfig.RiskLevel.NORMAL


def test_update_scan_config_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = web_security_scanner.UpdateScanConfigRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_scan_config), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_scan_config(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.UpdateScanConfigRequest()
        assert args[0] == request_msg


def test_update_scan_config_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_scan_config in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_scan_config] = (
            mock_rpc
        )
        request = {}
        client.update_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_scan_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_scan_config_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = WebSecurityScannerAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_scan_config
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_scan_config
        ] = mock_rpc

        request = {}
        await client.update_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_scan_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.UpdateScanConfigRequest(),
        {},
    ],
)
async def test_update_scan_config_async(request_type, transport: str = "grpc_asyncio"):
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcw_scan_config.ScanConfig(
                name="name_value",
                display_name="display_name_value",
                max_qps=761,
                starting_urls=["starting_urls_value"],
                user_agent=gcw_scan_config.ScanConfig.UserAgent.CHROME_LINUX,
                blacklist_patterns=["blacklist_patterns_value"],
                target_platforms=[gcw_scan_config.ScanConfig.TargetPlatform.APP_ENGINE],
                export_to_security_command_center=gcw_scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED,
                risk_level=gcw_scan_config.ScanConfig.RiskLevel.NORMAL,
            )
        )
        response = await client.update_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.UpdateScanConfigRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcw_scan_config.ScanConfig)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.max_qps == 761
    assert response.starting_urls == ["starting_urls_value"]
    assert response.user_agent == gcw_scan_config.ScanConfig.UserAgent.CHROME_LINUX
    assert response.blacklist_patterns == ["blacklist_patterns_value"]
    assert response.target_platforms == [
        gcw_scan_config.ScanConfig.TargetPlatform.APP_ENGINE
    ]
    assert (
        response.export_to_security_command_center
        == gcw_scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED
    )
    assert response.risk_level == gcw_scan_config.ScanConfig.RiskLevel.NORMAL


def test_update_scan_config_field_headers():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.UpdateScanConfigRequest()

    request.scan_config.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_scan_config), "__call__"
    ) as call:
        call.return_value = gcw_scan_config.ScanConfig()
        client.update_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "scan_config.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_scan_config_field_headers_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.UpdateScanConfigRequest()

    request.scan_config.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_scan_config), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcw_scan_config.ScanConfig()
        )
        await client.update_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "scan_config.name=name_value",
    ) in kw["metadata"]


def test_update_scan_config_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcw_scan_config.ScanConfig()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_scan_config(
            scan_config=gcw_scan_config.ScanConfig(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].scan_config
        mock_val = gcw_scan_config.ScanConfig(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_scan_config_flattened_error():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_scan_config(
            web_security_scanner.UpdateScanConfigRequest(),
            scan_config=gcw_scan_config.ScanConfig(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_scan_config_flattened_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gcw_scan_config.ScanConfig()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcw_scan_config.ScanConfig()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_scan_config(
            scan_config=gcw_scan_config.ScanConfig(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].scan_config
        mock_val = gcw_scan_config.ScanConfig(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_scan_config_flattened_error_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_scan_config(
            web_security_scanner.UpdateScanConfigRequest(),
            scan_config=gcw_scan_config.ScanConfig(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.StartScanRunRequest(),
        {},
    ],
)
def test_start_scan_run(request_type, transport: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.start_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = scan_run.ScanRun(
            name="name_value",
            execution_state=scan_run.ScanRun.ExecutionState.QUEUED,
            result_state=scan_run.ScanRun.ResultState.SUCCESS,
            urls_crawled_count=1935,
            urls_tested_count=1846,
            has_vulnerabilities=True,
            progress_percent=1733,
        )
        response = client.start_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.StartScanRunRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, scan_run.ScanRun)
    assert response.name == "name_value"
    assert response.execution_state == scan_run.ScanRun.ExecutionState.QUEUED
    assert response.result_state == scan_run.ScanRun.ResultState.SUCCESS
    assert response.urls_crawled_count == 1935
    assert response.urls_tested_count == 1846
    assert response.has_vulnerabilities is True
    assert response.progress_percent == 1733


def test_start_scan_run_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = web_security_scanner.StartScanRunRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.start_scan_run), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.start_scan_run(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.StartScanRunRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_start_scan_run_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.start_scan_run in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.start_scan_run] = mock_rpc
        request = {}
        client.start_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.start_scan_run(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_start_scan_run_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = WebSecurityScannerAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.start_scan_run
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.start_scan_run
        ] = mock_rpc

        request = {}
        await client.start_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.start_scan_run(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.StartScanRunRequest(),
        {},
    ],
)
async def test_start_scan_run_async(request_type, transport: str = "grpc_asyncio"):
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.start_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            scan_run.ScanRun(
                name="name_value",
                execution_state=scan_run.ScanRun.ExecutionState.QUEUED,
                result_state=scan_run.ScanRun.ResultState.SUCCESS,
                urls_crawled_count=1935,
                urls_tested_count=1846,
                has_vulnerabilities=True,
                progress_percent=1733,
            )
        )
        response = await client.start_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.StartScanRunRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, scan_run.ScanRun)
    assert response.name == "name_value"
    assert response.execution_state == scan_run.ScanRun.ExecutionState.QUEUED
    assert response.result_state == scan_run.ScanRun.ResultState.SUCCESS
    assert response.urls_crawled_count == 1935
    assert response.urls_tested_count == 1846
    assert response.has_vulnerabilities is True
    assert response.progress_percent == 1733


def test_start_scan_run_field_headers():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.StartScanRunRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.start_scan_run), "__call__") as call:
        call.return_value = scan_run.ScanRun()
        client.start_scan_run(request)

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
async def test_start_scan_run_field_headers_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.StartScanRunRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.start_scan_run), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(scan_run.ScanRun())
        await client.start_scan_run(request)

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


def test_start_scan_run_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.start_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = scan_run.ScanRun()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.start_scan_run(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_start_scan_run_flattened_error():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.start_scan_run(
            web_security_scanner.StartScanRunRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_start_scan_run_flattened_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.start_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = scan_run.ScanRun()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(scan_run.ScanRun())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.start_scan_run(
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
async def test_start_scan_run_flattened_error_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.start_scan_run(
            web_security_scanner.StartScanRunRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.GetScanRunRequest(),
        {},
    ],
)
def test_get_scan_run(request_type, transport: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = scan_run.ScanRun(
            name="name_value",
            execution_state=scan_run.ScanRun.ExecutionState.QUEUED,
            result_state=scan_run.ScanRun.ResultState.SUCCESS,
            urls_crawled_count=1935,
            urls_tested_count=1846,
            has_vulnerabilities=True,
            progress_percent=1733,
        )
        response = client.get_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.GetScanRunRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, scan_run.ScanRun)
    assert response.name == "name_value"
    assert response.execution_state == scan_run.ScanRun.ExecutionState.QUEUED
    assert response.result_state == scan_run.ScanRun.ResultState.SUCCESS
    assert response.urls_crawled_count == 1935
    assert response.urls_tested_count == 1846
    assert response.has_vulnerabilities is True
    assert response.progress_percent == 1733


def test_get_scan_run_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = web_security_scanner.GetScanRunRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_run), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_scan_run(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.GetScanRunRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_scan_run_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_scan_run in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_scan_run] = mock_rpc
        request = {}
        client.get_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_scan_run(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_scan_run_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = WebSecurityScannerAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_scan_run
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_scan_run
        ] = mock_rpc

        request = {}
        await client.get_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_scan_run(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.GetScanRunRequest(),
        {},
    ],
)
async def test_get_scan_run_async(request_type, transport: str = "grpc_asyncio"):
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            scan_run.ScanRun(
                name="name_value",
                execution_state=scan_run.ScanRun.ExecutionState.QUEUED,
                result_state=scan_run.ScanRun.ResultState.SUCCESS,
                urls_crawled_count=1935,
                urls_tested_count=1846,
                has_vulnerabilities=True,
                progress_percent=1733,
            )
        )
        response = await client.get_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.GetScanRunRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, scan_run.ScanRun)
    assert response.name == "name_value"
    assert response.execution_state == scan_run.ScanRun.ExecutionState.QUEUED
    assert response.result_state == scan_run.ScanRun.ResultState.SUCCESS
    assert response.urls_crawled_count == 1935
    assert response.urls_tested_count == 1846
    assert response.has_vulnerabilities is True
    assert response.progress_percent == 1733


def test_get_scan_run_field_headers():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.GetScanRunRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_run), "__call__") as call:
        call.return_value = scan_run.ScanRun()
        client.get_scan_run(request)

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
async def test_get_scan_run_field_headers_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.GetScanRunRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_run), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(scan_run.ScanRun())
        await client.get_scan_run(request)

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


def test_get_scan_run_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = scan_run.ScanRun()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_scan_run(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_scan_run_flattened_error():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_scan_run(
            web_security_scanner.GetScanRunRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_scan_run_flattened_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = scan_run.ScanRun()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(scan_run.ScanRun())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_scan_run(
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
async def test_get_scan_run_flattened_error_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_scan_run(
            web_security_scanner.GetScanRunRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListScanRunsRequest(),
        {},
    ],
)
def test_list_scan_runs(request_type, transport: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_scan_runs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListScanRunsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_scan_runs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.ListScanRunsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListScanRunsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_scan_runs_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = web_security_scanner.ListScanRunsRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_scan_runs), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_scan_runs(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListScanRunsRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_scan_runs_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_scan_runs in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_scan_runs] = mock_rpc
        request = {}
        client.list_scan_runs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_scan_runs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_scan_runs_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = WebSecurityScannerAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_scan_runs
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_scan_runs
        ] = mock_rpc

        request = {}
        await client.list_scan_runs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_scan_runs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListScanRunsRequest(),
        {},
    ],
)
async def test_list_scan_runs_async(request_type, transport: str = "grpc_asyncio"):
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_scan_runs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListScanRunsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_scan_runs(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.ListScanRunsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListScanRunsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_scan_runs_field_headers():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.ListScanRunsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_scan_runs), "__call__") as call:
        call.return_value = web_security_scanner.ListScanRunsResponse()
        client.list_scan_runs(request)

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
async def test_list_scan_runs_field_headers_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.ListScanRunsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_scan_runs), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListScanRunsResponse()
        )
        await client.list_scan_runs(request)

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


def test_list_scan_runs_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_scan_runs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListScanRunsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_scan_runs(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_scan_runs_flattened_error():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_scan_runs(
            web_security_scanner.ListScanRunsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_scan_runs_flattened_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_scan_runs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListScanRunsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListScanRunsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_scan_runs(
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
async def test_list_scan_runs_flattened_error_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_scan_runs(
            web_security_scanner.ListScanRunsRequest(),
            parent="parent_value",
        )


def test_list_scan_runs_pager(transport_name: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_scan_runs), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[],
                next_page_token="def",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
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
        pager = client.list_scan_runs(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, scan_run.ScanRun) for i in results)


def test_list_scan_runs_pages(transport_name: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_scan_runs), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[],
                next_page_token="def",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_scan_runs(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_scan_runs_async_pager():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_runs), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[],
                next_page_token="def",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_scan_runs(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, scan_run.ScanRun) for i in responses)


@pytest.mark.asyncio
async def test_list_scan_runs_async_pages():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_runs), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[],
                next_page_token="def",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_scan_runs(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.StopScanRunRequest(),
        {},
    ],
)
def test_stop_scan_run(request_type, transport: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.stop_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = scan_run.ScanRun(
            name="name_value",
            execution_state=scan_run.ScanRun.ExecutionState.QUEUED,
            result_state=scan_run.ScanRun.ResultState.SUCCESS,
            urls_crawled_count=1935,
            urls_tested_count=1846,
            has_vulnerabilities=True,
            progress_percent=1733,
        )
        response = client.stop_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.StopScanRunRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, scan_run.ScanRun)
    assert response.name == "name_value"
    assert response.execution_state == scan_run.ScanRun.ExecutionState.QUEUED
    assert response.result_state == scan_run.ScanRun.ResultState.SUCCESS
    assert response.urls_crawled_count == 1935
    assert response.urls_tested_count == 1846
    assert response.has_vulnerabilities is True
    assert response.progress_percent == 1733


def test_stop_scan_run_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = web_security_scanner.StopScanRunRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.stop_scan_run), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.stop_scan_run(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.StopScanRunRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_stop_scan_run_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.stop_scan_run in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.stop_scan_run] = mock_rpc
        request = {}
        client.stop_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.stop_scan_run(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_stop_scan_run_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = WebSecurityScannerAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.stop_scan_run
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.stop_scan_run
        ] = mock_rpc

        request = {}
        await client.stop_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.stop_scan_run(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.StopScanRunRequest(),
        {},
    ],
)
async def test_stop_scan_run_async(request_type, transport: str = "grpc_asyncio"):
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.stop_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            scan_run.ScanRun(
                name="name_value",
                execution_state=scan_run.ScanRun.ExecutionState.QUEUED,
                result_state=scan_run.ScanRun.ResultState.SUCCESS,
                urls_crawled_count=1935,
                urls_tested_count=1846,
                has_vulnerabilities=True,
                progress_percent=1733,
            )
        )
        response = await client.stop_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.StopScanRunRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, scan_run.ScanRun)
    assert response.name == "name_value"
    assert response.execution_state == scan_run.ScanRun.ExecutionState.QUEUED
    assert response.result_state == scan_run.ScanRun.ResultState.SUCCESS
    assert response.urls_crawled_count == 1935
    assert response.urls_tested_count == 1846
    assert response.has_vulnerabilities is True
    assert response.progress_percent == 1733


def test_stop_scan_run_field_headers():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.StopScanRunRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.stop_scan_run), "__call__") as call:
        call.return_value = scan_run.ScanRun()
        client.stop_scan_run(request)

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
async def test_stop_scan_run_field_headers_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.StopScanRunRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.stop_scan_run), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(scan_run.ScanRun())
        await client.stop_scan_run(request)

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


def test_stop_scan_run_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.stop_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = scan_run.ScanRun()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.stop_scan_run(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_stop_scan_run_flattened_error():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.stop_scan_run(
            web_security_scanner.StopScanRunRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_stop_scan_run_flattened_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.stop_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = scan_run.ScanRun()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(scan_run.ScanRun())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.stop_scan_run(
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
async def test_stop_scan_run_flattened_error_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.stop_scan_run(
            web_security_scanner.StopScanRunRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListCrawledUrlsRequest(),
        {},
    ],
)
def test_list_crawled_urls(request_type, transport: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_crawled_urls), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListCrawledUrlsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_crawled_urls(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.ListCrawledUrlsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCrawledUrlsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_crawled_urls_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = web_security_scanner.ListCrawledUrlsRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_crawled_urls), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_crawled_urls(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListCrawledUrlsRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_crawled_urls_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_crawled_urls in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_crawled_urls] = (
            mock_rpc
        )
        request = {}
        client.list_crawled_urls(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_crawled_urls(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_crawled_urls_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = WebSecurityScannerAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_crawled_urls
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_crawled_urls
        ] = mock_rpc

        request = {}
        await client.list_crawled_urls(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_crawled_urls(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListCrawledUrlsRequest(),
        {},
    ],
)
async def test_list_crawled_urls_async(request_type, transport: str = "grpc_asyncio"):
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_crawled_urls), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListCrawledUrlsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_crawled_urls(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.ListCrawledUrlsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCrawledUrlsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_crawled_urls_field_headers():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.ListCrawledUrlsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_crawled_urls), "__call__"
    ) as call:
        call.return_value = web_security_scanner.ListCrawledUrlsResponse()
        client.list_crawled_urls(request)

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
async def test_list_crawled_urls_field_headers_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.ListCrawledUrlsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_crawled_urls), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListCrawledUrlsResponse()
        )
        await client.list_crawled_urls(request)

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


def test_list_crawled_urls_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_crawled_urls), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListCrawledUrlsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_crawled_urls(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_crawled_urls_flattened_error():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_crawled_urls(
            web_security_scanner.ListCrawledUrlsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_crawled_urls_flattened_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_crawled_urls), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListCrawledUrlsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListCrawledUrlsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_crawled_urls(
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
async def test_list_crawled_urls_flattened_error_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_crawled_urls(
            web_security_scanner.ListCrawledUrlsRequest(),
            parent="parent_value",
        )


def test_list_crawled_urls_pager(transport_name: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_crawled_urls), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[],
                next_page_token="def",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
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
        pager = client.list_crawled_urls(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, crawled_url.CrawledUrl) for i in results)


def test_list_crawled_urls_pages(transport_name: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_crawled_urls), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[],
                next_page_token="def",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_crawled_urls(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_crawled_urls_async_pager():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_crawled_urls),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[],
                next_page_token="def",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_crawled_urls(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, crawled_url.CrawledUrl) for i in responses)


@pytest.mark.asyncio
async def test_list_crawled_urls_async_pages():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_crawled_urls),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[],
                next_page_token="def",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_crawled_urls(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.GetFindingRequest(),
        {},
    ],
)
def test_get_finding(request_type, transport: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_finding), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = finding.Finding(
            name="name_value",
            finding_type="finding_type_value",
            http_method="http_method_value",
            fuzzed_url="fuzzed_url_value",
            body="body_value",
            description="description_value",
            reproduction_url="reproduction_url_value",
            frame_url="frame_url_value",
            final_url="final_url_value",
            tracking_id="tracking_id_value",
        )
        response = client.get_finding(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.GetFindingRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, finding.Finding)
    assert response.name == "name_value"
    assert response.finding_type == "finding_type_value"
    assert response.http_method == "http_method_value"
    assert response.fuzzed_url == "fuzzed_url_value"
    assert response.body == "body_value"
    assert response.description == "description_value"
    assert response.reproduction_url == "reproduction_url_value"
    assert response.frame_url == "frame_url_value"
    assert response.final_url == "final_url_value"
    assert response.tracking_id == "tracking_id_value"


def test_get_finding_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = web_security_scanner.GetFindingRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_finding), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_finding(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.GetFindingRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_finding_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_finding in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_finding] = mock_rpc
        request = {}
        client.get_finding(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_finding(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_finding_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = WebSecurityScannerAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_finding
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_finding
        ] = mock_rpc

        request = {}
        await client.get_finding(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_finding(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.GetFindingRequest(),
        {},
    ],
)
async def test_get_finding_async(request_type, transport: str = "grpc_asyncio"):
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_finding), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            finding.Finding(
                name="name_value",
                finding_type="finding_type_value",
                http_method="http_method_value",
                fuzzed_url="fuzzed_url_value",
                body="body_value",
                description="description_value",
                reproduction_url="reproduction_url_value",
                frame_url="frame_url_value",
                final_url="final_url_value",
                tracking_id="tracking_id_value",
            )
        )
        response = await client.get_finding(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.GetFindingRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, finding.Finding)
    assert response.name == "name_value"
    assert response.finding_type == "finding_type_value"
    assert response.http_method == "http_method_value"
    assert response.fuzzed_url == "fuzzed_url_value"
    assert response.body == "body_value"
    assert response.description == "description_value"
    assert response.reproduction_url == "reproduction_url_value"
    assert response.frame_url == "frame_url_value"
    assert response.final_url == "final_url_value"
    assert response.tracking_id == "tracking_id_value"


def test_get_finding_field_headers():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.GetFindingRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_finding), "__call__") as call:
        call.return_value = finding.Finding()
        client.get_finding(request)

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
async def test_get_finding_field_headers_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.GetFindingRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_finding), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(finding.Finding())
        await client.get_finding(request)

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


def test_get_finding_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_finding), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = finding.Finding()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_finding(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_finding_flattened_error():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_finding(
            web_security_scanner.GetFindingRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_finding_flattened_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_finding), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = finding.Finding()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(finding.Finding())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_finding(
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
async def test_get_finding_flattened_error_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_finding(
            web_security_scanner.GetFindingRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListFindingsRequest(),
        {},
    ],
)
def test_list_findings(request_type, transport: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_findings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListFindingsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_findings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.ListFindingsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFindingsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_findings_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = web_security_scanner.ListFindingsRequest(
        parent="parent_value",
        filter="filter_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_findings), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_findings(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListFindingsRequest(
            parent="parent_value",
            filter="filter_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_findings_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_findings in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_findings] = mock_rpc
        request = {}
        client.list_findings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_findings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_findings_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = WebSecurityScannerAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_findings
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_findings
        ] = mock_rpc

        request = {}
        await client.list_findings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_findings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListFindingsRequest(),
        {},
    ],
)
async def test_list_findings_async(request_type, transport: str = "grpc_asyncio"):
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_findings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListFindingsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_findings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.ListFindingsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFindingsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_findings_field_headers():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.ListFindingsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_findings), "__call__") as call:
        call.return_value = web_security_scanner.ListFindingsResponse()
        client.list_findings(request)

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
async def test_list_findings_field_headers_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.ListFindingsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_findings), "__call__") as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListFindingsResponse()
        )
        await client.list_findings(request)

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


def test_list_findings_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_findings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListFindingsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_findings(
            parent="parent_value",
            filter="filter_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].filter
        mock_val = "filter_value"
        assert arg == mock_val


def test_list_findings_flattened_error():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_findings(
            web_security_scanner.ListFindingsRequest(),
            parent="parent_value",
            filter="filter_value",
        )


@pytest.mark.asyncio
async def test_list_findings_flattened_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_findings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListFindingsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListFindingsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_findings(
            parent="parent_value",
            filter="filter_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].filter
        mock_val = "filter_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_findings_flattened_error_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_findings(
            web_security_scanner.ListFindingsRequest(),
            parent="parent_value",
            filter="filter_value",
        )


def test_list_findings_pager(transport_name: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_findings), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                    finding.Finding(),
                    finding.Finding(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[],
                next_page_token="def",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                    finding.Finding(),
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
        pager = client.list_findings(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, finding.Finding) for i in results)


def test_list_findings_pages(transport_name: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_findings), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                    finding.Finding(),
                    finding.Finding(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[],
                next_page_token="def",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                    finding.Finding(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_findings(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_findings_async_pager():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                    finding.Finding(),
                    finding.Finding(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[],
                next_page_token="def",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                    finding.Finding(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_findings(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, finding.Finding) for i in responses)


@pytest.mark.asyncio
async def test_list_findings_async_pages():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_findings), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                    finding.Finding(),
                    finding.Finding(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[],
                next_page_token="def",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                    finding.Finding(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_findings(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListFindingTypeStatsRequest(),
        {},
    ],
)
def test_list_finding_type_stats(request_type, transport: str = "grpc"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_finding_type_stats), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListFindingTypeStatsResponse()
        response = client.list_finding_type_stats(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.ListFindingTypeStatsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, web_security_scanner.ListFindingTypeStatsResponse)


def test_list_finding_type_stats_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = web_security_scanner.ListFindingTypeStatsRequest(
        parent="parent_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_finding_type_stats), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_finding_type_stats(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListFindingTypeStatsRequest(
            parent="parent_value",
        )
        assert args[0] == request_msg


def test_list_finding_type_stats_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_finding_type_stats
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_finding_type_stats
        ] = mock_rpc
        request = {}
        client.list_finding_type_stats(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_finding_type_stats(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_finding_type_stats_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = WebSecurityScannerAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_finding_type_stats
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_finding_type_stats
        ] = mock_rpc

        request = {}
        await client.list_finding_type_stats(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_finding_type_stats(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListFindingTypeStatsRequest(),
        {},
    ],
)
async def test_list_finding_type_stats_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_finding_type_stats), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListFindingTypeStatsResponse()
        )
        response = await client.list_finding_type_stats(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = web_security_scanner.ListFindingTypeStatsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, web_security_scanner.ListFindingTypeStatsResponse)


def test_list_finding_type_stats_field_headers():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.ListFindingTypeStatsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_finding_type_stats), "__call__"
    ) as call:
        call.return_value = web_security_scanner.ListFindingTypeStatsResponse()
        client.list_finding_type_stats(request)

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
async def test_list_finding_type_stats_field_headers_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = web_security_scanner.ListFindingTypeStatsRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_finding_type_stats), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListFindingTypeStatsResponse()
        )
        await client.list_finding_type_stats(request)

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


def test_list_finding_type_stats_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_finding_type_stats), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListFindingTypeStatsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_finding_type_stats(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_finding_type_stats_flattened_error():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_finding_type_stats(
            web_security_scanner.ListFindingTypeStatsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_finding_type_stats_flattened_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_finding_type_stats), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = web_security_scanner.ListFindingTypeStatsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListFindingTypeStatsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_finding_type_stats(
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
async def test_list_finding_type_stats_flattened_error_async():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_finding_type_stats(
            web_security_scanner.ListFindingTypeStatsRequest(),
            parent="parent_value",
        )


def test_create_scan_config_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_scan_config in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_scan_config] = (
            mock_rpc
        )

        request = {}
        client.create_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_scan_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_scan_config_rest_required_fields(
    request_type=web_security_scanner.CreateScanConfigRequest,
):
    transport_class = transports.WebSecurityScannerRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateScanConfig,
        "_BaseCreateScanConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gcw_scan_config.ScanConfig()
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
            return_value = gcw_scan_config.ScanConfig.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_scan_config(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_scan_config_rest_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcw_scan_config.ScanConfig()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            scan_config=gcw_scan_config.ScanConfig(name="name_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = gcw_scan_config.ScanConfig.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_scan_config(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{parent=projects/*}/scanConfigs" % client.transport._host,
            args[1],
        )


def test_create_scan_config_rest_flattened_error(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_scan_config(
            web_security_scanner.CreateScanConfigRequest(),
            parent="parent_value",
            scan_config=gcw_scan_config.ScanConfig(name="name_value"),
        )


def test_delete_scan_config_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_scan_config in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_scan_config] = (
            mock_rpc
        )

        request = {}
        client.delete_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_scan_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_scan_config_rest_required_fields(
    request_type=web_security_scanner.DeleteScanConfigRequest,
):
    transport_class = transports.WebSecurityScannerRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeleteScanConfig,
        "_BaseDeleteScanConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = WebSecurityScannerClient(
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

            response = client.delete_scan_config(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_scan_config_rest_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/scanConfigs/sample2"}

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

        client.delete_scan_config(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{name=projects/*/scanConfigs/*}" % client.transport._host,
            args[1],
        )


def test_delete_scan_config_rest_flattened_error(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_scan_config(
            web_security_scanner.DeleteScanConfigRequest(),
            name="name_value",
        )


def test_get_scan_config_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_scan_config in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_scan_config] = mock_rpc

        request = {}
        client.get_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_scan_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_scan_config_rest_required_fields(
    request_type=web_security_scanner.GetScanConfigRequest,
):
    transport_class = transports.WebSecurityScannerRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetScanConfig,
        "_BaseGetScanConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = scan_config.ScanConfig()
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
            return_value = scan_config.ScanConfig.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_scan_config(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_scan_config_rest_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = scan_config.ScanConfig()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/scanConfigs/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = scan_config.ScanConfig.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_scan_config(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{name=projects/*/scanConfigs/*}" % client.transport._host,
            args[1],
        )


def test_get_scan_config_rest_flattened_error(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_scan_config(
            web_security_scanner.GetScanConfigRequest(),
            name="name_value",
        )


def test_list_scan_configs_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_scan_configs in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_scan_configs] = (
            mock_rpc
        )

        request = {}
        client.list_scan_configs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_scan_configs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_scan_configs_rest_required_fields(
    request_type=web_security_scanner.ListScanConfigsRequest,
):
    transport_class = transports.WebSecurityScannerRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListScanConfigs,
        "_BaseListScanConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = web_security_scanner.ListScanConfigsResponse()
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
            return_value = web_security_scanner.ListScanConfigsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_scan_configs(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_scan_configs_rest_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = web_security_scanner.ListScanConfigsResponse()

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
        return_value = web_security_scanner.ListScanConfigsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_scan_configs(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{parent=projects/*}/scanConfigs" % client.transport._host,
            args[1],
        )


def test_list_scan_configs_rest_flattened_error(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_scan_configs(
            web_security_scanner.ListScanConfigsRequest(),
            parent="parent_value",
        )


def test_list_scan_configs_rest_pager(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[],
                next_page_token="def",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListScanConfigsResponse(
                scan_configs=[
                    scan_config.ScanConfig(),
                    scan_config.ScanConfig(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            web_security_scanner.ListScanConfigsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "projects/sample1"}

        pager = client.list_scan_configs(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, scan_config.ScanConfig) for i in results)

        pages = list(client.list_scan_configs(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_update_scan_config_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_scan_config in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_scan_config] = (
            mock_rpc
        )

        request = {}
        client.update_scan_config(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_scan_config(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_scan_config_rest_required_fields(
    request_type=web_security_scanner.UpdateScanConfigRequest,
):
    transport_class = transports.WebSecurityScannerRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateScanConfig,
        "_BaseUpdateScanConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gcw_scan_config.ScanConfig()
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
            return_value = gcw_scan_config.ScanConfig.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_scan_config(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_scan_config_rest_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcw_scan_config.ScanConfig()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "scan_config": {"name": "projects/sample1/scanConfigs/sample2"}
        }

        # get truthy value for each flattened field
        mock_args = dict(
            scan_config=gcw_scan_config.ScanConfig(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = gcw_scan_config.ScanConfig.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_scan_config(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{scan_config.name=projects/*/scanConfigs/*}"
            % client.transport._host,
            args[1],
        )


def test_update_scan_config_rest_flattened_error(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_scan_config(
            web_security_scanner.UpdateScanConfigRequest(),
            scan_config=gcw_scan_config.ScanConfig(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_start_scan_run_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.start_scan_run in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.start_scan_run] = mock_rpc

        request = {}
        client.start_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.start_scan_run(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_start_scan_run_rest_required_fields(
    request_type=web_security_scanner.StartScanRunRequest,
):
    transport_class = transports.WebSecurityScannerRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseStartScanRun,
        "_BaseStartScanRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = scan_run.ScanRun()
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
            return_value = scan_run.ScanRun.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.start_scan_run(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_start_scan_run_rest_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = scan_run.ScanRun()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/scanConfigs/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = scan_run.ScanRun.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.start_scan_run(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{name=projects/*/scanConfigs/*}:start" % client.transport._host,
            args[1],
        )


def test_start_scan_run_rest_flattened_error(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.start_scan_run(
            web_security_scanner.StartScanRunRequest(),
            name="name_value",
        )


def test_get_scan_run_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_scan_run in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_scan_run] = mock_rpc

        request = {}
        client.get_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_scan_run(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_scan_run_rest_required_fields(
    request_type=web_security_scanner.GetScanRunRequest,
):
    transport_class = transports.WebSecurityScannerRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetScanRun,
        "_BaseGetScanRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = scan_run.ScanRun()
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
            return_value = scan_run.ScanRun.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_scan_run(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_scan_run_rest_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = scan_run.ScanRun()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"
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
        return_value = scan_run.ScanRun.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_scan_run(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*}"
            % client.transport._host,
            args[1],
        )


def test_get_scan_run_rest_flattened_error(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_scan_run(
            web_security_scanner.GetScanRunRequest(),
            name="name_value",
        )


def test_list_scan_runs_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_scan_runs in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_scan_runs] = mock_rpc

        request = {}
        client.list_scan_runs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_scan_runs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_scan_runs_rest_required_fields(
    request_type=web_security_scanner.ListScanRunsRequest,
):
    transport_class = transports.WebSecurityScannerRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListScanRuns,
        "_BaseListScanRuns__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = web_security_scanner.ListScanRunsResponse()
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
            return_value = web_security_scanner.ListScanRunsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_scan_runs(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_scan_runs_rest_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = web_security_scanner.ListScanRunsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1/scanConfigs/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = web_security_scanner.ListScanRunsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_scan_runs(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{parent=projects/*/scanConfigs/*}/scanRuns"
            % client.transport._host,
            args[1],
        )


def test_list_scan_runs_rest_flattened_error(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_scan_runs(
            web_security_scanner.ListScanRunsRequest(),
            parent="parent_value",
        )


def test_list_scan_runs_rest_pager(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[],
                next_page_token="def",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListScanRunsResponse(
                scan_runs=[
                    scan_run.ScanRun(),
                    scan_run.ScanRun(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            web_security_scanner.ListScanRunsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "projects/sample1/scanConfigs/sample2"}

        pager = client.list_scan_runs(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, scan_run.ScanRun) for i in results)

        pages = list(client.list_scan_runs(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_stop_scan_run_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.stop_scan_run in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.stop_scan_run] = mock_rpc

        request = {}
        client.stop_scan_run(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.stop_scan_run(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_stop_scan_run_rest_required_fields(
    request_type=web_security_scanner.StopScanRunRequest,
):
    transport_class = transports.WebSecurityScannerRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseStopScanRun,
        "_BaseStopScanRun__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = scan_run.ScanRun()
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
            return_value = scan_run.ScanRun.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.stop_scan_run(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_stop_scan_run_rest_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = scan_run.ScanRun()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"
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
        return_value = scan_run.ScanRun.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.stop_scan_run(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*}:stop"
            % client.transport._host,
            args[1],
        )


def test_stop_scan_run_rest_flattened_error(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.stop_scan_run(
            web_security_scanner.StopScanRunRequest(),
            name="name_value",
        )


def test_list_crawled_urls_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_crawled_urls in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_crawled_urls] = (
            mock_rpc
        )

        request = {}
        client.list_crawled_urls(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_crawled_urls(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_crawled_urls_rest_required_fields(
    request_type=web_security_scanner.ListCrawledUrlsRequest,
):
    transport_class = transports.WebSecurityScannerRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListCrawledUrls,
        "_BaseListCrawledUrls__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = web_security_scanner.ListCrawledUrlsResponse()
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
            return_value = web_security_scanner.ListCrawledUrlsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_crawled_urls(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_crawled_urls_rest_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = web_security_scanner.ListCrawledUrlsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"
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
        return_value = web_security_scanner.ListCrawledUrlsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_crawled_urls(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/crawledUrls"
            % client.transport._host,
            args[1],
        )


def test_list_crawled_urls_rest_flattened_error(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_crawled_urls(
            web_security_scanner.ListCrawledUrlsRequest(),
            parent="parent_value",
        )


def test_list_crawled_urls_rest_pager(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[],
                next_page_token="def",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListCrawledUrlsResponse(
                crawled_urls=[
                    crawled_url.CrawledUrl(),
                    crawled_url.CrawledUrl(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            web_security_scanner.ListCrawledUrlsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "parent": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"
        }

        pager = client.list_crawled_urls(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, crawled_url.CrawledUrl) for i in results)

        pages = list(client.list_crawled_urls(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_get_finding_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_finding in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_finding] = mock_rpc

        request = {}
        client.get_finding(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_finding(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_finding_rest_required_fields(
    request_type=web_security_scanner.GetFindingRequest,
):
    transport_class = transports.WebSecurityScannerRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetFinding,
        "_BaseGetFinding__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = finding.Finding()
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
            return_value = finding.Finding.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_finding(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_finding_rest_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = finding.Finding()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/scanConfigs/sample2/scanRuns/sample3/findings/sample4"
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
        return_value = finding.Finding.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_finding(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{name=projects/*/scanConfigs/*/scanRuns/*/findings/*}"
            % client.transport._host,
            args[1],
        )


def test_get_finding_rest_flattened_error(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_finding(
            web_security_scanner.GetFindingRequest(),
            name="name_value",
        )


def test_list_findings_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_findings in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_findings] = mock_rpc

        request = {}
        client.list_findings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_findings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_findings_rest_required_fields(
    request_type=web_security_scanner.ListFindingsRequest,
):
    transport_class = transports.WebSecurityScannerRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["filter"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped
    assert "filter" not in jsonified_request

    default_values = getattr(
        transport_class._BaseListFindings,
        "_BaseListFindings__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "filter" in jsonified_request
    assert jsonified_request["filter"] == request_init["filter"]

    jsonified_request["parent"] = "parent_value"
    jsonified_request["filter"] = "filter_value"

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
    assert "filter" in jsonified_request
    assert jsonified_request["filter"] == "filter_value"

    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = web_security_scanner.ListFindingsResponse()
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
            return_value = web_security_scanner.ListFindingsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_findings(request)

            expected_params = [
                (
                    "filter",
                    "",
                ),
                ("$alt", "json;enum-encoding=int"),
            ]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_findings_rest_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = web_security_scanner.ListFindingsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            filter="filter_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = web_security_scanner.ListFindingsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_findings(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/findings"
            % client.transport._host,
            args[1],
        )


def test_list_findings_rest_flattened_error(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_findings(
            web_security_scanner.ListFindingsRequest(),
            parent="parent_value",
            filter="filter_value",
        )


def test_list_findings_rest_pager(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                    finding.Finding(),
                    finding.Finding(),
                ],
                next_page_token="abc",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[],
                next_page_token="def",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                ],
                next_page_token="ghi",
            ),
            web_security_scanner.ListFindingsResponse(
                findings=[
                    finding.Finding(),
                    finding.Finding(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            web_security_scanner.ListFindingsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "parent": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"
        }

        pager = client.list_findings(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, finding.Finding) for i in results)

        pages = list(client.list_findings(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_list_finding_type_stats_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_finding_type_stats
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_finding_type_stats
        ] = mock_rpc

        request = {}
        client.list_finding_type_stats(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_finding_type_stats(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_finding_type_stats_rest_required_fields(
    request_type=web_security_scanner.ListFindingTypeStatsRequest,
):
    transport_class = transports.WebSecurityScannerRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListFindingTypeStats,
        "_BaseListFindingTypeStats__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = web_security_scanner.ListFindingTypeStatsResponse()
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
            return_value = web_security_scanner.ListFindingTypeStatsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_finding_type_stats(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_finding_type_stats_rest_flattened():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = web_security_scanner.ListFindingTypeStatsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "parent": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"
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
        return_value = web_security_scanner.ListFindingTypeStatsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_finding_type_stats(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1beta/{parent=projects/*/scanConfigs/*/scanRuns/*}/findingTypeStats"
            % client.transport._host,
            args[1],
        )


def test_list_finding_type_stats_rest_flattened_error(transport: str = "rest"):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_finding_type_stats(
            web_security_scanner.ListFindingTypeStatsRequest(),
            parent="parent_value",
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.WebSecurityScannerGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.WebSecurityScannerGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = WebSecurityScannerClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.WebSecurityScannerGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = WebSecurityScannerClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = WebSecurityScannerClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.WebSecurityScannerGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = WebSecurityScannerClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.WebSecurityScannerGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = WebSecurityScannerClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.WebSecurityScannerGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.WebSecurityScannerGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.WebSecurityScannerGrpcTransport,
        transports.WebSecurityScannerGrpcAsyncIOTransport,
        transports.WebSecurityScannerRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = WebSecurityScannerClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_scan_config_empty_call_grpc():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_scan_config), "__call__"
    ) as call:
        call.return_value = gcw_scan_config.ScanConfig()
        client.create_scan_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.CreateScanConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_scan_config_empty_call_grpc():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_scan_config), "__call__"
    ) as call:
        call.return_value = None
        client.delete_scan_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.DeleteScanConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_scan_config_empty_call_grpc():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_config), "__call__") as call:
        call.return_value = scan_config.ScanConfig()
        client.get_scan_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.GetScanConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_scan_configs_empty_call_grpc():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_configs), "__call__"
    ) as call:
        call.return_value = web_security_scanner.ListScanConfigsResponse()
        client.list_scan_configs(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListScanConfigsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_scan_config_empty_call_grpc():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_scan_config), "__call__"
    ) as call:
        call.return_value = gcw_scan_config.ScanConfig()
        client.update_scan_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.UpdateScanConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_start_scan_run_empty_call_grpc():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.start_scan_run), "__call__") as call:
        call.return_value = scan_run.ScanRun()
        client.start_scan_run(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.StartScanRunRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_scan_run_empty_call_grpc():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_run), "__call__") as call:
        call.return_value = scan_run.ScanRun()
        client.get_scan_run(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.GetScanRunRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_scan_runs_empty_call_grpc():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_scan_runs), "__call__") as call:
        call.return_value = web_security_scanner.ListScanRunsResponse()
        client.list_scan_runs(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListScanRunsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_stop_scan_run_empty_call_grpc():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.stop_scan_run), "__call__") as call:
        call.return_value = scan_run.ScanRun()
        client.stop_scan_run(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.StopScanRunRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_crawled_urls_empty_call_grpc():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_crawled_urls), "__call__"
    ) as call:
        call.return_value = web_security_scanner.ListCrawledUrlsResponse()
        client.list_crawled_urls(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListCrawledUrlsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_finding_empty_call_grpc():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_finding), "__call__") as call:
        call.return_value = finding.Finding()
        client.get_finding(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.GetFindingRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_findings_empty_call_grpc():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_findings), "__call__") as call:
        call.return_value = web_security_scanner.ListFindingsResponse()
        client.list_findings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListFindingsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_finding_type_stats_empty_call_grpc():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_finding_type_stats), "__call__"
    ) as call:
        call.return_value = web_security_scanner.ListFindingTypeStatsResponse()
        client.list_finding_type_stats(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListFindingTypeStatsRequest()
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = WebSecurityScannerAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_scan_config_empty_call_grpc_asyncio():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcw_scan_config.ScanConfig(
                name="name_value",
                display_name="display_name_value",
                max_qps=761,
                starting_urls=["starting_urls_value"],
                user_agent=gcw_scan_config.ScanConfig.UserAgent.CHROME_LINUX,
                blacklist_patterns=["blacklist_patterns_value"],
                target_platforms=[gcw_scan_config.ScanConfig.TargetPlatform.APP_ENGINE],
                export_to_security_command_center=gcw_scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED,
                risk_level=gcw_scan_config.ScanConfig.RiskLevel.NORMAL,
            )
        )
        await client.create_scan_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.CreateScanConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_scan_config_empty_call_grpc_asyncio():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_scan_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.DeleteScanConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_scan_config_empty_call_grpc_asyncio():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_config), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            scan_config.ScanConfig(
                name="name_value",
                display_name="display_name_value",
                max_qps=761,
                starting_urls=["starting_urls_value"],
                user_agent=scan_config.ScanConfig.UserAgent.CHROME_LINUX,
                blacklist_patterns=["blacklist_patterns_value"],
                target_platforms=[scan_config.ScanConfig.TargetPlatform.APP_ENGINE],
                export_to_security_command_center=scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED,
                risk_level=scan_config.ScanConfig.RiskLevel.NORMAL,
            )
        )
        await client.get_scan_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.GetScanConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_scan_configs_empty_call_grpc_asyncio():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_configs), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListScanConfigsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_scan_configs(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListScanConfigsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_scan_config_empty_call_grpc_asyncio():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_scan_config), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gcw_scan_config.ScanConfig(
                name="name_value",
                display_name="display_name_value",
                max_qps=761,
                starting_urls=["starting_urls_value"],
                user_agent=gcw_scan_config.ScanConfig.UserAgent.CHROME_LINUX,
                blacklist_patterns=["blacklist_patterns_value"],
                target_platforms=[gcw_scan_config.ScanConfig.TargetPlatform.APP_ENGINE],
                export_to_security_command_center=gcw_scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED,
                risk_level=gcw_scan_config.ScanConfig.RiskLevel.NORMAL,
            )
        )
        await client.update_scan_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.UpdateScanConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_start_scan_run_empty_call_grpc_asyncio():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.start_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            scan_run.ScanRun(
                name="name_value",
                execution_state=scan_run.ScanRun.ExecutionState.QUEUED,
                result_state=scan_run.ScanRun.ResultState.SUCCESS,
                urls_crawled_count=1935,
                urls_tested_count=1846,
                has_vulnerabilities=True,
                progress_percent=1733,
            )
        )
        await client.start_scan_run(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.StartScanRunRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_scan_run_empty_call_grpc_asyncio():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            scan_run.ScanRun(
                name="name_value",
                execution_state=scan_run.ScanRun.ExecutionState.QUEUED,
                result_state=scan_run.ScanRun.ResultState.SUCCESS,
                urls_crawled_count=1935,
                urls_tested_count=1846,
                has_vulnerabilities=True,
                progress_percent=1733,
            )
        )
        await client.get_scan_run(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.GetScanRunRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_scan_runs_empty_call_grpc_asyncio():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_scan_runs), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListScanRunsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_scan_runs(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListScanRunsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_stop_scan_run_empty_call_grpc_asyncio():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.stop_scan_run), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            scan_run.ScanRun(
                name="name_value",
                execution_state=scan_run.ScanRun.ExecutionState.QUEUED,
                result_state=scan_run.ScanRun.ResultState.SUCCESS,
                urls_crawled_count=1935,
                urls_tested_count=1846,
                has_vulnerabilities=True,
                progress_percent=1733,
            )
        )
        await client.stop_scan_run(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.StopScanRunRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_crawled_urls_empty_call_grpc_asyncio():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_crawled_urls), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListCrawledUrlsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_crawled_urls(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListCrawledUrlsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_finding_empty_call_grpc_asyncio():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_finding), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            finding.Finding(
                name="name_value",
                finding_type="finding_type_value",
                http_method="http_method_value",
                fuzzed_url="fuzzed_url_value",
                body="body_value",
                description="description_value",
                reproduction_url="reproduction_url_value",
                frame_url="frame_url_value",
                final_url="final_url_value",
                tracking_id="tracking_id_value",
            )
        )
        await client.get_finding(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.GetFindingRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_findings_empty_call_grpc_asyncio():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_findings), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListFindingsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_findings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListFindingsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_finding_type_stats_empty_call_grpc_asyncio():
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_finding_type_stats), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            web_security_scanner.ListFindingTypeStatsResponse()
        )
        await client.list_finding_type_stats(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListFindingTypeStatsRequest()
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = WebSecurityScannerClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_create_scan_config_rest_bad_request(
    request_type=web_security_scanner.CreateScanConfigRequest,
):
    client = WebSecurityScannerClient(
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
        client.create_scan_config(request)


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.CreateScanConfigRequest,
        dict,
    ],
)
def test_create_scan_config_rest_call_success(request_type):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request_init["scan_config"] = {
        "name": "name_value",
        "display_name": "display_name_value",
        "max_qps": 761,
        "starting_urls": ["starting_urls_value1", "starting_urls_value2"],
        "authentication": {
            "google_account": {
                "username": "username_value",
                "password": "password_value",
            },
            "custom_account": {
                "username": "username_value",
                "password": "password_value",
                "login_url": "login_url_value",
            },
        },
        "user_agent": 1,
        "blacklist_patterns": [
            "blacklist_patterns_value1",
            "blacklist_patterns_value2",
        ],
        "schedule": {
            "schedule_time": {"seconds": 751, "nanos": 543},
            "interval_duration_days": 2362,
        },
        "target_platforms": [1],
        "export_to_security_command_center": 1,
        "latest_run": {
            "name": "name_value",
            "execution_state": 1,
            "result_state": 1,
            "start_time": {},
            "end_time": {},
            "urls_crawled_count": 1935,
            "urls_tested_count": 1846,
            "has_vulnerabilities": True,
            "progress_percent": 1733,
            "error_trace": {
                "code": 1,
                "scan_config_error": {"code": 1, "field_name": "field_name_value"},
                "most_common_http_error_code": 2893,
            },
            "warning_traces": [{"code": 1}],
        },
        "risk_level": 1,
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = web_security_scanner.CreateScanConfigRequest.meta.fields["scan_config"]

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
    for field, value in request_init["scan_config"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["scan_config"][field])):
                    del request_init["scan_config"][field][i][subfield]
            else:
                del request_init["scan_config"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcw_scan_config.ScanConfig(
            name="name_value",
            display_name="display_name_value",
            max_qps=761,
            starting_urls=["starting_urls_value"],
            user_agent=gcw_scan_config.ScanConfig.UserAgent.CHROME_LINUX,
            blacklist_patterns=["blacklist_patterns_value"],
            target_platforms=[gcw_scan_config.ScanConfig.TargetPlatform.APP_ENGINE],
            export_to_security_command_center=gcw_scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED,
            risk_level=gcw_scan_config.ScanConfig.RiskLevel.NORMAL,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gcw_scan_config.ScanConfig.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_scan_config(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcw_scan_config.ScanConfig)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.max_qps == 761
    assert response.starting_urls == ["starting_urls_value"]
    assert response.user_agent == gcw_scan_config.ScanConfig.UserAgent.CHROME_LINUX
    assert response.blacklist_patterns == ["blacklist_patterns_value"]
    assert response.target_platforms == [
        gcw_scan_config.ScanConfig.TargetPlatform.APP_ENGINE
    ]
    assert (
        response.export_to_security_command_center
        == gcw_scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED
    )
    assert response.risk_level == gcw_scan_config.ScanConfig.RiskLevel.NORMAL


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_scan_config_rest_interceptors(null_interceptor):
    transport = transports.WebSecurityScannerRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.WebSecurityScannerRestInterceptor(),
    )
    client = WebSecurityScannerClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "post_create_scan_config"
        ) as post,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor,
            "post_create_scan_config_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "pre_create_scan_config"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = web_security_scanner.CreateScanConfigRequest.pb(
            web_security_scanner.CreateScanConfigRequest()
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
        return_value = gcw_scan_config.ScanConfig.to_json(gcw_scan_config.ScanConfig())
        req.return_value.content = return_value

        request = web_security_scanner.CreateScanConfigRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gcw_scan_config.ScanConfig()
        post_with_metadata.return_value = gcw_scan_config.ScanConfig(), metadata

        client.create_scan_config(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_scan_config_rest_bad_request(
    request_type=web_security_scanner.DeleteScanConfigRequest,
):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/scanConfigs/sample2"}
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
        client.delete_scan_config(request)


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.DeleteScanConfigRequest,
        dict,
    ],
)
def test_delete_scan_config_rest_call_success(request_type):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/scanConfigs/sample2"}
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
        response = client.delete_scan_config(request)

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_scan_config_rest_interceptors(null_interceptor):
    transport = transports.WebSecurityScannerRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.WebSecurityScannerRestInterceptor(),
    )
    client = WebSecurityScannerClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "pre_delete_scan_config"
        ) as pre,
    ):
        pre.assert_not_called()
        pb_message = web_security_scanner.DeleteScanConfigRequest.pb(
            web_security_scanner.DeleteScanConfigRequest()
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

        request = web_security_scanner.DeleteScanConfigRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata

        client.delete_scan_config(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()


def test_get_scan_config_rest_bad_request(
    request_type=web_security_scanner.GetScanConfigRequest,
):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/scanConfigs/sample2"}
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
        client.get_scan_config(request)


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.GetScanConfigRequest,
        dict,
    ],
)
def test_get_scan_config_rest_call_success(request_type):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/scanConfigs/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = scan_config.ScanConfig(
            name="name_value",
            display_name="display_name_value",
            max_qps=761,
            starting_urls=["starting_urls_value"],
            user_agent=scan_config.ScanConfig.UserAgent.CHROME_LINUX,
            blacklist_patterns=["blacklist_patterns_value"],
            target_platforms=[scan_config.ScanConfig.TargetPlatform.APP_ENGINE],
            export_to_security_command_center=scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED,
            risk_level=scan_config.ScanConfig.RiskLevel.NORMAL,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = scan_config.ScanConfig.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_scan_config(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, scan_config.ScanConfig)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.max_qps == 761
    assert response.starting_urls == ["starting_urls_value"]
    assert response.user_agent == scan_config.ScanConfig.UserAgent.CHROME_LINUX
    assert response.blacklist_patterns == ["blacklist_patterns_value"]
    assert response.target_platforms == [
        scan_config.ScanConfig.TargetPlatform.APP_ENGINE
    ]
    assert (
        response.export_to_security_command_center
        == scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED
    )
    assert response.risk_level == scan_config.ScanConfig.RiskLevel.NORMAL


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_scan_config_rest_interceptors(null_interceptor):
    transport = transports.WebSecurityScannerRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.WebSecurityScannerRestInterceptor(),
    )
    client = WebSecurityScannerClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "post_get_scan_config"
        ) as post,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor,
            "post_get_scan_config_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "pre_get_scan_config"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = web_security_scanner.GetScanConfigRequest.pb(
            web_security_scanner.GetScanConfigRequest()
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
        return_value = scan_config.ScanConfig.to_json(scan_config.ScanConfig())
        req.return_value.content = return_value

        request = web_security_scanner.GetScanConfigRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = scan_config.ScanConfig()
        post_with_metadata.return_value = scan_config.ScanConfig(), metadata

        client.get_scan_config(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_scan_configs_rest_bad_request(
    request_type=web_security_scanner.ListScanConfigsRequest,
):
    client = WebSecurityScannerClient(
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
        client.list_scan_configs(request)


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListScanConfigsRequest,
        dict,
    ],
)
def test_list_scan_configs_rest_call_success(request_type):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = web_security_scanner.ListScanConfigsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = web_security_scanner.ListScanConfigsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_scan_configs(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListScanConfigsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_scan_configs_rest_interceptors(null_interceptor):
    transport = transports.WebSecurityScannerRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.WebSecurityScannerRestInterceptor(),
    )
    client = WebSecurityScannerClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "post_list_scan_configs"
        ) as post,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor,
            "post_list_scan_configs_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "pre_list_scan_configs"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = web_security_scanner.ListScanConfigsRequest.pb(
            web_security_scanner.ListScanConfigsRequest()
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
        return_value = web_security_scanner.ListScanConfigsResponse.to_json(
            web_security_scanner.ListScanConfigsResponse()
        )
        req.return_value.content = return_value

        request = web_security_scanner.ListScanConfigsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = web_security_scanner.ListScanConfigsResponse()
        post_with_metadata.return_value = (
            web_security_scanner.ListScanConfigsResponse(),
            metadata,
        )

        client.list_scan_configs(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_scan_config_rest_bad_request(
    request_type=web_security_scanner.UpdateScanConfigRequest,
):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"scan_config": {"name": "projects/sample1/scanConfigs/sample2"}}
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
        client.update_scan_config(request)


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.UpdateScanConfigRequest,
        dict,
    ],
)
def test_update_scan_config_rest_call_success(request_type):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"scan_config": {"name": "projects/sample1/scanConfigs/sample2"}}
    request_init["scan_config"] = {
        "name": "projects/sample1/scanConfigs/sample2",
        "display_name": "display_name_value",
        "max_qps": 761,
        "starting_urls": ["starting_urls_value1", "starting_urls_value2"],
        "authentication": {
            "google_account": {
                "username": "username_value",
                "password": "password_value",
            },
            "custom_account": {
                "username": "username_value",
                "password": "password_value",
                "login_url": "login_url_value",
            },
        },
        "user_agent": 1,
        "blacklist_patterns": [
            "blacklist_patterns_value1",
            "blacklist_patterns_value2",
        ],
        "schedule": {
            "schedule_time": {"seconds": 751, "nanos": 543},
            "interval_duration_days": 2362,
        },
        "target_platforms": [1],
        "export_to_security_command_center": 1,
        "latest_run": {
            "name": "name_value",
            "execution_state": 1,
            "result_state": 1,
            "start_time": {},
            "end_time": {},
            "urls_crawled_count": 1935,
            "urls_tested_count": 1846,
            "has_vulnerabilities": True,
            "progress_percent": 1733,
            "error_trace": {
                "code": 1,
                "scan_config_error": {"code": 1, "field_name": "field_name_value"},
                "most_common_http_error_code": 2893,
            },
            "warning_traces": [{"code": 1}],
        },
        "risk_level": 1,
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = web_security_scanner.UpdateScanConfigRequest.meta.fields["scan_config"]

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
    for field, value in request_init["scan_config"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["scan_config"][field])):
                    del request_init["scan_config"][field][i][subfield]
            else:
                del request_init["scan_config"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gcw_scan_config.ScanConfig(
            name="name_value",
            display_name="display_name_value",
            max_qps=761,
            starting_urls=["starting_urls_value"],
            user_agent=gcw_scan_config.ScanConfig.UserAgent.CHROME_LINUX,
            blacklist_patterns=["blacklist_patterns_value"],
            target_platforms=[gcw_scan_config.ScanConfig.TargetPlatform.APP_ENGINE],
            export_to_security_command_center=gcw_scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED,
            risk_level=gcw_scan_config.ScanConfig.RiskLevel.NORMAL,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gcw_scan_config.ScanConfig.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_scan_config(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gcw_scan_config.ScanConfig)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.max_qps == 761
    assert response.starting_urls == ["starting_urls_value"]
    assert response.user_agent == gcw_scan_config.ScanConfig.UserAgent.CHROME_LINUX
    assert response.blacklist_patterns == ["blacklist_patterns_value"]
    assert response.target_platforms == [
        gcw_scan_config.ScanConfig.TargetPlatform.APP_ENGINE
    ]
    assert (
        response.export_to_security_command_center
        == gcw_scan_config.ScanConfig.ExportToSecurityCommandCenter.ENABLED
    )
    assert response.risk_level == gcw_scan_config.ScanConfig.RiskLevel.NORMAL


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_scan_config_rest_interceptors(null_interceptor):
    transport = transports.WebSecurityScannerRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.WebSecurityScannerRestInterceptor(),
    )
    client = WebSecurityScannerClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "post_update_scan_config"
        ) as post,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor,
            "post_update_scan_config_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "pre_update_scan_config"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = web_security_scanner.UpdateScanConfigRequest.pb(
            web_security_scanner.UpdateScanConfigRequest()
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
        return_value = gcw_scan_config.ScanConfig.to_json(gcw_scan_config.ScanConfig())
        req.return_value.content = return_value

        request = web_security_scanner.UpdateScanConfigRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gcw_scan_config.ScanConfig()
        post_with_metadata.return_value = gcw_scan_config.ScanConfig(), metadata

        client.update_scan_config(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_start_scan_run_rest_bad_request(
    request_type=web_security_scanner.StartScanRunRequest,
):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/scanConfigs/sample2"}
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
        client.start_scan_run(request)


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.StartScanRunRequest,
        dict,
    ],
)
def test_start_scan_run_rest_call_success(request_type):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/scanConfigs/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = scan_run.ScanRun(
            name="name_value",
            execution_state=scan_run.ScanRun.ExecutionState.QUEUED,
            result_state=scan_run.ScanRun.ResultState.SUCCESS,
            urls_crawled_count=1935,
            urls_tested_count=1846,
            has_vulnerabilities=True,
            progress_percent=1733,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = scan_run.ScanRun.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.start_scan_run(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, scan_run.ScanRun)
    assert response.name == "name_value"
    assert response.execution_state == scan_run.ScanRun.ExecutionState.QUEUED
    assert response.result_state == scan_run.ScanRun.ResultState.SUCCESS
    assert response.urls_crawled_count == 1935
    assert response.urls_tested_count == 1846
    assert response.has_vulnerabilities is True
    assert response.progress_percent == 1733


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_start_scan_run_rest_interceptors(null_interceptor):
    transport = transports.WebSecurityScannerRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.WebSecurityScannerRestInterceptor(),
    )
    client = WebSecurityScannerClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "post_start_scan_run"
        ) as post,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor,
            "post_start_scan_run_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "pre_start_scan_run"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = web_security_scanner.StartScanRunRequest.pb(
            web_security_scanner.StartScanRunRequest()
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
        return_value = scan_run.ScanRun.to_json(scan_run.ScanRun())
        req.return_value.content = return_value

        request = web_security_scanner.StartScanRunRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = scan_run.ScanRun()
        post_with_metadata.return_value = scan_run.ScanRun(), metadata

        client.start_scan_run(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_scan_run_rest_bad_request(
    request_type=web_security_scanner.GetScanRunRequest,
):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"}
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
        client.get_scan_run(request)


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.GetScanRunRequest,
        dict,
    ],
)
def test_get_scan_run_rest_call_success(request_type):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = scan_run.ScanRun(
            name="name_value",
            execution_state=scan_run.ScanRun.ExecutionState.QUEUED,
            result_state=scan_run.ScanRun.ResultState.SUCCESS,
            urls_crawled_count=1935,
            urls_tested_count=1846,
            has_vulnerabilities=True,
            progress_percent=1733,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = scan_run.ScanRun.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_scan_run(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, scan_run.ScanRun)
    assert response.name == "name_value"
    assert response.execution_state == scan_run.ScanRun.ExecutionState.QUEUED
    assert response.result_state == scan_run.ScanRun.ResultState.SUCCESS
    assert response.urls_crawled_count == 1935
    assert response.urls_tested_count == 1846
    assert response.has_vulnerabilities is True
    assert response.progress_percent == 1733


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_scan_run_rest_interceptors(null_interceptor):
    transport = transports.WebSecurityScannerRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.WebSecurityScannerRestInterceptor(),
    )
    client = WebSecurityScannerClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "post_get_scan_run"
        ) as post,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor,
            "post_get_scan_run_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "pre_get_scan_run"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = web_security_scanner.GetScanRunRequest.pb(
            web_security_scanner.GetScanRunRequest()
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
        return_value = scan_run.ScanRun.to_json(scan_run.ScanRun())
        req.return_value.content = return_value

        request = web_security_scanner.GetScanRunRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = scan_run.ScanRun()
        post_with_metadata.return_value = scan_run.ScanRun(), metadata

        client.get_scan_run(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_scan_runs_rest_bad_request(
    request_type=web_security_scanner.ListScanRunsRequest,
):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/scanConfigs/sample2"}
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
        client.list_scan_runs(request)


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListScanRunsRequest,
        dict,
    ],
)
def test_list_scan_runs_rest_call_success(request_type):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/scanConfigs/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = web_security_scanner.ListScanRunsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = web_security_scanner.ListScanRunsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_scan_runs(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListScanRunsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_scan_runs_rest_interceptors(null_interceptor):
    transport = transports.WebSecurityScannerRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.WebSecurityScannerRestInterceptor(),
    )
    client = WebSecurityScannerClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "post_list_scan_runs"
        ) as post,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor,
            "post_list_scan_runs_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "pre_list_scan_runs"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = web_security_scanner.ListScanRunsRequest.pb(
            web_security_scanner.ListScanRunsRequest()
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
        return_value = web_security_scanner.ListScanRunsResponse.to_json(
            web_security_scanner.ListScanRunsResponse()
        )
        req.return_value.content = return_value

        request = web_security_scanner.ListScanRunsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = web_security_scanner.ListScanRunsResponse()
        post_with_metadata.return_value = (
            web_security_scanner.ListScanRunsResponse(),
            metadata,
        )

        client.list_scan_runs(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_stop_scan_run_rest_bad_request(
    request_type=web_security_scanner.StopScanRunRequest,
):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"}
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
        client.stop_scan_run(request)


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.StopScanRunRequest,
        dict,
    ],
)
def test_stop_scan_run_rest_call_success(request_type):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = scan_run.ScanRun(
            name="name_value",
            execution_state=scan_run.ScanRun.ExecutionState.QUEUED,
            result_state=scan_run.ScanRun.ResultState.SUCCESS,
            urls_crawled_count=1935,
            urls_tested_count=1846,
            has_vulnerabilities=True,
            progress_percent=1733,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = scan_run.ScanRun.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.stop_scan_run(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, scan_run.ScanRun)
    assert response.name == "name_value"
    assert response.execution_state == scan_run.ScanRun.ExecutionState.QUEUED
    assert response.result_state == scan_run.ScanRun.ResultState.SUCCESS
    assert response.urls_crawled_count == 1935
    assert response.urls_tested_count == 1846
    assert response.has_vulnerabilities is True
    assert response.progress_percent == 1733


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_stop_scan_run_rest_interceptors(null_interceptor):
    transport = transports.WebSecurityScannerRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.WebSecurityScannerRestInterceptor(),
    )
    client = WebSecurityScannerClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "post_stop_scan_run"
        ) as post,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor,
            "post_stop_scan_run_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "pre_stop_scan_run"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = web_security_scanner.StopScanRunRequest.pb(
            web_security_scanner.StopScanRunRequest()
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
        return_value = scan_run.ScanRun.to_json(scan_run.ScanRun())
        req.return_value.content = return_value

        request = web_security_scanner.StopScanRunRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = scan_run.ScanRun()
        post_with_metadata.return_value = scan_run.ScanRun(), metadata

        client.stop_scan_run(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_crawled_urls_rest_bad_request(
    request_type=web_security_scanner.ListCrawledUrlsRequest,
):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"}
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
        client.list_crawled_urls(request)


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListCrawledUrlsRequest,
        dict,
    ],
)
def test_list_crawled_urls_rest_call_success(request_type):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = web_security_scanner.ListCrawledUrlsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = web_security_scanner.ListCrawledUrlsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_crawled_urls(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListCrawledUrlsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_crawled_urls_rest_interceptors(null_interceptor):
    transport = transports.WebSecurityScannerRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.WebSecurityScannerRestInterceptor(),
    )
    client = WebSecurityScannerClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "post_list_crawled_urls"
        ) as post,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor,
            "post_list_crawled_urls_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "pre_list_crawled_urls"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = web_security_scanner.ListCrawledUrlsRequest.pb(
            web_security_scanner.ListCrawledUrlsRequest()
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
        return_value = web_security_scanner.ListCrawledUrlsResponse.to_json(
            web_security_scanner.ListCrawledUrlsResponse()
        )
        req.return_value.content = return_value

        request = web_security_scanner.ListCrawledUrlsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = web_security_scanner.ListCrawledUrlsResponse()
        post_with_metadata.return_value = (
            web_security_scanner.ListCrawledUrlsResponse(),
            metadata,
        )

        client.list_crawled_urls(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_finding_rest_bad_request(
    request_type=web_security_scanner.GetFindingRequest,
):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/scanConfigs/sample2/scanRuns/sample3/findings/sample4"
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
        client.get_finding(request)


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.GetFindingRequest,
        dict,
    ],
)
def test_get_finding_rest_call_success(request_type):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "projects/sample1/scanConfigs/sample2/scanRuns/sample3/findings/sample4"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = finding.Finding(
            name="name_value",
            finding_type="finding_type_value",
            http_method="http_method_value",
            fuzzed_url="fuzzed_url_value",
            body="body_value",
            description="description_value",
            reproduction_url="reproduction_url_value",
            frame_url="frame_url_value",
            final_url="final_url_value",
            tracking_id="tracking_id_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = finding.Finding.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_finding(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, finding.Finding)
    assert response.name == "name_value"
    assert response.finding_type == "finding_type_value"
    assert response.http_method == "http_method_value"
    assert response.fuzzed_url == "fuzzed_url_value"
    assert response.body == "body_value"
    assert response.description == "description_value"
    assert response.reproduction_url == "reproduction_url_value"
    assert response.frame_url == "frame_url_value"
    assert response.final_url == "final_url_value"
    assert response.tracking_id == "tracking_id_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_finding_rest_interceptors(null_interceptor):
    transport = transports.WebSecurityScannerRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.WebSecurityScannerRestInterceptor(),
    )
    client = WebSecurityScannerClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "post_get_finding"
        ) as post,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor,
            "post_get_finding_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "pre_get_finding"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = web_security_scanner.GetFindingRequest.pb(
            web_security_scanner.GetFindingRequest()
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
        return_value = finding.Finding.to_json(finding.Finding())
        req.return_value.content = return_value

        request = web_security_scanner.GetFindingRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = finding.Finding()
        post_with_metadata.return_value = finding.Finding(), metadata

        client.get_finding(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_findings_rest_bad_request(
    request_type=web_security_scanner.ListFindingsRequest,
):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"}
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
        client.list_findings(request)


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListFindingsRequest,
        dict,
    ],
)
def test_list_findings_rest_call_success(request_type):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = web_security_scanner.ListFindingsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = web_security_scanner.ListFindingsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_findings(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListFindingsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_findings_rest_interceptors(null_interceptor):
    transport = transports.WebSecurityScannerRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.WebSecurityScannerRestInterceptor(),
    )
    client = WebSecurityScannerClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "post_list_findings"
        ) as post,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor,
            "post_list_findings_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "pre_list_findings"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = web_security_scanner.ListFindingsRequest.pb(
            web_security_scanner.ListFindingsRequest()
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
        return_value = web_security_scanner.ListFindingsResponse.to_json(
            web_security_scanner.ListFindingsResponse()
        )
        req.return_value.content = return_value

        request = web_security_scanner.ListFindingsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = web_security_scanner.ListFindingsResponse()
        post_with_metadata.return_value = (
            web_security_scanner.ListFindingsResponse(),
            metadata,
        )

        client.list_findings(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_finding_type_stats_rest_bad_request(
    request_type=web_security_scanner.ListFindingTypeStatsRequest,
):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"}
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
        client.list_finding_type_stats(request)


@pytest.mark.parametrize(
    "request_type",
    [
        web_security_scanner.ListFindingTypeStatsRequest,
        dict,
    ],
)
def test_list_finding_type_stats_rest_call_success(request_type):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/scanConfigs/sample2/scanRuns/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = web_security_scanner.ListFindingTypeStatsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = web_security_scanner.ListFindingTypeStatsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_finding_type_stats(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, web_security_scanner.ListFindingTypeStatsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_finding_type_stats_rest_interceptors(null_interceptor):
    transport = transports.WebSecurityScannerRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.WebSecurityScannerRestInterceptor(),
    )
    client = WebSecurityScannerClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "post_list_finding_type_stats"
        ) as post,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor,
            "post_list_finding_type_stats_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.WebSecurityScannerRestInterceptor, "pre_list_finding_type_stats"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = web_security_scanner.ListFindingTypeStatsRequest.pb(
            web_security_scanner.ListFindingTypeStatsRequest()
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
        return_value = web_security_scanner.ListFindingTypeStatsResponse.to_json(
            web_security_scanner.ListFindingTypeStatsResponse()
        )
        req.return_value.content = return_value

        request = web_security_scanner.ListFindingTypeStatsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = web_security_scanner.ListFindingTypeStatsResponse()
        post_with_metadata.return_value = (
            web_security_scanner.ListFindingTypeStatsResponse(),
            metadata,
        )

        client.list_finding_type_stats(
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
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_scan_config_empty_call_rest():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_scan_config), "__call__"
    ) as call:
        client.create_scan_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.CreateScanConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_scan_config_empty_call_rest():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_scan_config), "__call__"
    ) as call:
        client.delete_scan_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.DeleteScanConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_scan_config_empty_call_rest():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_config), "__call__") as call:
        client.get_scan_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.GetScanConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_scan_configs_empty_call_rest():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_scan_configs), "__call__"
    ) as call:
        client.list_scan_configs(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListScanConfigsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_scan_config_empty_call_rest():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_scan_config), "__call__"
    ) as call:
        client.update_scan_config(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.UpdateScanConfigRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_start_scan_run_empty_call_rest():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.start_scan_run), "__call__") as call:
        client.start_scan_run(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.StartScanRunRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_scan_run_empty_call_rest():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_scan_run), "__call__") as call:
        client.get_scan_run(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.GetScanRunRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_scan_runs_empty_call_rest():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_scan_runs), "__call__") as call:
        client.list_scan_runs(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListScanRunsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_stop_scan_run_empty_call_rest():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.stop_scan_run), "__call__") as call:
        client.stop_scan_run(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.StopScanRunRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_crawled_urls_empty_call_rest():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_crawled_urls), "__call__"
    ) as call:
        client.list_crawled_urls(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListCrawledUrlsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_finding_empty_call_rest():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_finding), "__call__") as call:
        client.get_finding(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.GetFindingRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_findings_empty_call_rest():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_findings), "__call__") as call:
        client.list_findings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListFindingsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_finding_type_stats_empty_call_rest():
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_finding_type_stats), "__call__"
    ) as call:
        client.list_finding_type_stats(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = web_security_scanner.ListFindingTypeStatsRequest()
        assert args[0] == request_msg


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.WebSecurityScannerGrpcTransport,
    )


def test_web_security_scanner_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.WebSecurityScannerTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_web_security_scanner_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.websecurityscanner_v1beta.services.web_security_scanner.transports.WebSecurityScannerTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.WebSecurityScannerTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "create_scan_config",
        "delete_scan_config",
        "get_scan_config",
        "list_scan_configs",
        "update_scan_config",
        "start_scan_run",
        "get_scan_run",
        "list_scan_runs",
        "stop_scan_run",
        "list_crawled_urls",
        "get_finding",
        "list_findings",
        "list_finding_type_stats",
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


def test_web_security_scanner_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.cloud.websecurityscanner_v1beta.services.web_security_scanner.transports.WebSecurityScannerTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.WebSecurityScannerTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


def test_web_security_scanner_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.cloud.websecurityscanner_v1beta.services.web_security_scanner.transports.WebSecurityScannerTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.WebSecurityScannerTransport()
        adc.assert_called_once()


def test_web_security_scanner_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        WebSecurityScannerClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.WebSecurityScannerGrpcTransport,
        transports.WebSecurityScannerGrpcAsyncIOTransport,
    ],
)
def test_web_security_scanner_transport_auth_adc(transport_class):
    # If credentials and host are not provided, the transport class should use
    # ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class(quota_project_id="octopus", scopes=["1", "2"])
        adc.assert_called_once_with(
            scopes=["1", "2"],
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.WebSecurityScannerGrpcTransport,
        transports.WebSecurityScannerGrpcAsyncIOTransport,
        transports.WebSecurityScannerRestTransport,
    ],
)
def test_web_security_scanner_transport_auth_gdch_credentials(transport_class):
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
        (transports.WebSecurityScannerGrpcTransport, grpc_helpers),
        (transports.WebSecurityScannerGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_web_security_scanner_transport_create_channel(transport_class, grpc_helpers):
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
            "websecurityscanner.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=["1", "2"],
            default_host="websecurityscanner.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.WebSecurityScannerGrpcTransport,
        transports.WebSecurityScannerGrpcAsyncIOTransport,
    ],
)
def test_web_security_scanner_grpc_transport_client_cert_source_for_mtls(
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


def test_web_security_scanner_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.WebSecurityScannerRestTransport(
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
def test_web_security_scanner_host_no_port(transport_name):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="websecurityscanner.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "websecurityscanner.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://websecurityscanner.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_web_security_scanner_host_with_port(transport_name):
    client = WebSecurityScannerClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="websecurityscanner.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "websecurityscanner.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://websecurityscanner.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_web_security_scanner_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = WebSecurityScannerClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = WebSecurityScannerClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.create_scan_config._session
    session2 = client2.transport.create_scan_config._session
    assert session1 != session2
    session1 = client1.transport.delete_scan_config._session
    session2 = client2.transport.delete_scan_config._session
    assert session1 != session2
    session1 = client1.transport.get_scan_config._session
    session2 = client2.transport.get_scan_config._session
    assert session1 != session2
    session1 = client1.transport.list_scan_configs._session
    session2 = client2.transport.list_scan_configs._session
    assert session1 != session2
    session1 = client1.transport.update_scan_config._session
    session2 = client2.transport.update_scan_config._session
    assert session1 != session2
    session1 = client1.transport.start_scan_run._session
    session2 = client2.transport.start_scan_run._session
    assert session1 != session2
    session1 = client1.transport.get_scan_run._session
    session2 = client2.transport.get_scan_run._session
    assert session1 != session2
    session1 = client1.transport.list_scan_runs._session
    session2 = client2.transport.list_scan_runs._session
    assert session1 != session2
    session1 = client1.transport.stop_scan_run._session
    session2 = client2.transport.stop_scan_run._session
    assert session1 != session2
    session1 = client1.transport.list_crawled_urls._session
    session2 = client2.transport.list_crawled_urls._session
    assert session1 != session2
    session1 = client1.transport.get_finding._session
    session2 = client2.transport.get_finding._session
    assert session1 != session2
    session1 = client1.transport.list_findings._session
    session2 = client2.transport.list_findings._session
    assert session1 != session2
    session1 = client1.transport.list_finding_type_stats._session
    session2 = client2.transport.list_finding_type_stats._session
    assert session1 != session2


def test_web_security_scanner_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.WebSecurityScannerGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_web_security_scanner_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.WebSecurityScannerGrpcAsyncIOTransport(
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
        transports.WebSecurityScannerGrpcTransport,
        transports.WebSecurityScannerGrpcAsyncIOTransport,
    ],
)
def test_web_security_scanner_transport_channel_mtls_with_client_cert_source(
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
        transports.WebSecurityScannerGrpcTransport,
        transports.WebSecurityScannerGrpcAsyncIOTransport,
    ],
)
def test_web_security_scanner_transport_channel_mtls_with_adc(transport_class):
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


def test_finding_path():
    project = "squid"
    scan_config = "clam"
    scan_run = "whelk"
    finding = "octopus"
    expected = "projects/{project}/scanConfigs/{scan_config}/scanRuns/{scan_run}/findings/{finding}".format(
        project=project,
        scan_config=scan_config,
        scan_run=scan_run,
        finding=finding,
    )
    actual = WebSecurityScannerClient.finding_path(
        project, scan_config, scan_run, finding
    )
    assert expected == actual


def test_parse_finding_path():
    expected = {
        "project": "oyster",
        "scan_config": "nudibranch",
        "scan_run": "cuttlefish",
        "finding": "mussel",
    }
    path = WebSecurityScannerClient.finding_path(**expected)

    # Check that the path construction is reversible.
    actual = WebSecurityScannerClient.parse_finding_path(path)
    assert expected == actual


def test_scan_config_path():
    project = "winkle"
    scan_config = "nautilus"
    expected = "projects/{project}/scanConfigs/{scan_config}".format(
        project=project,
        scan_config=scan_config,
    )
    actual = WebSecurityScannerClient.scan_config_path(project, scan_config)
    assert expected == actual


def test_parse_scan_config_path():
    expected = {
        "project": "scallop",
        "scan_config": "abalone",
    }
    path = WebSecurityScannerClient.scan_config_path(**expected)

    # Check that the path construction is reversible.
    actual = WebSecurityScannerClient.parse_scan_config_path(path)
    assert expected == actual


def test_scan_run_path():
    project = "squid"
    scan_config = "clam"
    scan_run = "whelk"
    expected = (
        "projects/{project}/scanConfigs/{scan_config}/scanRuns/{scan_run}".format(
            project=project,
            scan_config=scan_config,
            scan_run=scan_run,
        )
    )
    actual = WebSecurityScannerClient.scan_run_path(project, scan_config, scan_run)
    assert expected == actual


def test_parse_scan_run_path():
    expected = {
        "project": "octopus",
        "scan_config": "oyster",
        "scan_run": "nudibranch",
    }
    path = WebSecurityScannerClient.scan_run_path(**expected)

    # Check that the path construction is reversible.
    actual = WebSecurityScannerClient.parse_scan_run_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "cuttlefish"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = WebSecurityScannerClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "mussel",
    }
    path = WebSecurityScannerClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = WebSecurityScannerClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "winkle"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = WebSecurityScannerClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "nautilus",
    }
    path = WebSecurityScannerClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = WebSecurityScannerClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "scallop"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = WebSecurityScannerClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "abalone",
    }
    path = WebSecurityScannerClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = WebSecurityScannerClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "squid"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = WebSecurityScannerClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "clam",
    }
    path = WebSecurityScannerClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = WebSecurityScannerClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "whelk"
    location = "octopus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = WebSecurityScannerClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
    }
    path = WebSecurityScannerClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = WebSecurityScannerClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.WebSecurityScannerTransport, "_prep_wrapped_messages"
    ) as prep:
        client = WebSecurityScannerClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.WebSecurityScannerTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = WebSecurityScannerClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_grpc():
    client = WebSecurityScannerClient(
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
    client = WebSecurityScannerAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = WebSecurityScannerClient(
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
        client = WebSecurityScannerClient(
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
        (WebSecurityScannerClient, transports.WebSecurityScannerGrpcTransport),
        (
            WebSecurityScannerAsyncClient,
            transports.WebSecurityScannerGrpcAsyncIOTransport,
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
