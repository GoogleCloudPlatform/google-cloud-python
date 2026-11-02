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

from google.ads.admanager_v1.services.live_stream_service import (
    LiveStreamServiceClient,
    pagers,
    transports,
)
from google.ads.admanager_v1.types import (
    live_stream_event_enums,
    live_stream_messages,
    live_stream_service,
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

    assert LiveStreamServiceClient._get_client_cert_source(None, False) is None
    assert (
        LiveStreamServiceClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        LiveStreamServiceClient._get_client_cert_source(mock_provided_cert_source, True)
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
                LiveStreamServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                LiveStreamServiceClient._get_client_cert_source(
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
    client = LiveStreamServiceClient(credentials=cred)
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
    client = LiveStreamServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (LiveStreamServiceClient, "rest"),
    ],
)
def test_live_stream_service_client_from_service_account_info(
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
            "admanager.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://admanager.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.LiveStreamServiceRestTransport, "rest"),
    ],
)
def test_live_stream_service_client_service_account_always_use_jwt(
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
        (LiveStreamServiceClient, "rest"),
    ],
)
def test_live_stream_service_client_from_service_account_file(
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
            "admanager.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://admanager.googleapis.com"
        )


def test_live_stream_service_client_get_transport_class():
    transport = LiveStreamServiceClient.get_transport_class()
    available_transports = [
        transports.LiveStreamServiceRestTransport,
    ]
    assert transport in available_transports

    transport = LiveStreamServiceClient.get_transport_class("rest")
    assert transport == transports.LiveStreamServiceRestTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (LiveStreamServiceClient, transports.LiveStreamServiceRestTransport, "rest"),
    ],
)
@mock.patch.object(
    LiveStreamServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(LiveStreamServiceClient),
)
def test_live_stream_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(LiveStreamServiceClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(LiveStreamServiceClient, "get_transport_class") as gtc:
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
            LiveStreamServiceClient,
            transports.LiveStreamServiceRestTransport,
            "rest",
            "true",
        ),
        (
            LiveStreamServiceClient,
            transports.LiveStreamServiceRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    LiveStreamServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(LiveStreamServiceClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_live_stream_service_client_mtls_env_auto(
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


@pytest.mark.parametrize("client_class", [LiveStreamServiceClient])
@mock.patch.object(
    LiveStreamServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(LiveStreamServiceClient),
)
def test_live_stream_service_client_get_mtls_endpoint_and_cert_source(client_class):
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


@pytest.mark.parametrize("client_class", [LiveStreamServiceClient])
@mock.patch.object(
    LiveStreamServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(LiveStreamServiceClient),
)
def test_live_stream_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = LiveStreamServiceClient._DEFAULT_UNIVERSE
    default_endpoint = LiveStreamServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = LiveStreamServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
        (LiveStreamServiceClient, transports.LiveStreamServiceRestTransport, "rest"),
    ],
)
def test_live_stream_service_client_client_options_scopes(
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
            LiveStreamServiceClient,
            transports.LiveStreamServiceRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_live_stream_service_client_client_options_credentials_file(
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


def test_get_live_stream_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LiveStreamServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_live_stream in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_live_stream] = mock_rpc

        request = {}
        client.get_live_stream(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_live_stream(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_live_stream_rest_required_fields(
    request_type=live_stream_service.GetLiveStreamRequest,
):
    transport_class = transports.LiveStreamServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetLiveStream,
        "_BaseGetLiveStream__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = live_stream_messages.LiveStream()
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
            return_value = live_stream_messages.LiveStream.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_live_stream(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_live_stream_rest_flattened():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_messages.LiveStream()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "networks/sample1/liveStreams/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = live_stream_messages.LiveStream.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_live_stream(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=networks/*/liveStreams/*}" % client.transport._host, args[1]
        )


def test_get_live_stream_rest_flattened_error(transport: str = "rest"):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_live_stream(
            live_stream_service.GetLiveStreamRequest(),
            name="name_value",
        )


def test_list_live_streams_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LiveStreamServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_live_streams in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_live_streams] = (
            mock_rpc
        )

        request = {}
        client.list_live_streams(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_live_streams(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_live_streams_rest_required_fields(
    request_type=live_stream_service.ListLiveStreamsRequest,
):
    transport_class = transports.LiveStreamServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListLiveStreams,
        "_BaseListLiveStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
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
            "orderBy",
            "pageSize",
            "pageToken",
            "skip",
        )
    )

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = live_stream_service.ListLiveStreamsResponse()
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
            return_value = live_stream_service.ListLiveStreamsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_live_streams(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_live_streams_rest_flattened():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.ListLiveStreamsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = live_stream_service.ListLiveStreamsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_live_streams(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/liveStreams" % client.transport._host, args[1]
        )


def test_list_live_streams_rest_flattened_error(transport: str = "rest"):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_live_streams(
            live_stream_service.ListLiveStreamsRequest(),
            parent="parent_value",
        )


def test_list_live_streams_rest_pager(transport: str = "rest"):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            live_stream_service.ListLiveStreamsResponse(
                live_streams=[
                    live_stream_messages.LiveStream(),
                    live_stream_messages.LiveStream(),
                    live_stream_messages.LiveStream(),
                ],
                next_page_token="abc",
            ),
            live_stream_service.ListLiveStreamsResponse(
                live_streams=[],
                next_page_token="def",
            ),
            live_stream_service.ListLiveStreamsResponse(
                live_streams=[
                    live_stream_messages.LiveStream(),
                ],
                next_page_token="ghi",
            ),
            live_stream_service.ListLiveStreamsResponse(
                live_streams=[
                    live_stream_messages.LiveStream(),
                    live_stream_messages.LiveStream(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            live_stream_service.ListLiveStreamsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "networks/sample1"}

        pager = client.list_live_streams(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, live_stream_messages.LiveStream) for i in results)

        pages = list(client.list_live_streams(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_create_live_stream_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LiveStreamServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_live_stream in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_live_stream] = (
            mock_rpc
        )

        request = {}
        client.create_live_stream(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_live_stream(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_live_stream_rest_required_fields(
    request_type=live_stream_service.CreateLiveStreamRequest,
):
    transport_class = transports.LiveStreamServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateLiveStream,
        "_BaseCreateLiveStream__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = live_stream_messages.LiveStream()
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
            return_value = live_stream_messages.LiveStream.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_live_stream(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_live_stream_rest_flattened():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_messages.LiveStream()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            live_stream=live_stream_messages.LiveStream(name="name_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = live_stream_messages.LiveStream.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_live_stream(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/liveStreams" % client.transport._host, args[1]
        )


def test_create_live_stream_rest_flattened_error(transport: str = "rest"):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_live_stream(
            live_stream_service.CreateLiveStreamRequest(),
            parent="parent_value",
            live_stream=live_stream_messages.LiveStream(name="name_value"),
        )


def test_batch_create_live_streams_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LiveStreamServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_create_live_streams
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_create_live_streams
        ] = mock_rpc

        request = {}
        client.batch_create_live_streams(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_create_live_streams(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_create_live_streams_rest_required_fields(
    request_type=live_stream_service.BatchCreateLiveStreamsRequest,
):
    transport_class = transports.LiveStreamServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchCreateLiveStreams,
        "_BaseBatchCreateLiveStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = live_stream_service.BatchCreateLiveStreamsResponse()
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
            return_value = live_stream_service.BatchCreateLiveStreamsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_create_live_streams(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_create_live_streams_rest_flattened():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.BatchCreateLiveStreamsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            requests=[
                live_stream_service.CreateLiveStreamRequest(parent="parent_value")
            ],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = live_stream_service.BatchCreateLiveStreamsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_create_live_streams(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/liveStreams:batchCreate"
            % client.transport._host,
            args[1],
        )


def test_batch_create_live_streams_rest_flattened_error(transport: str = "rest"):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_create_live_streams(
            live_stream_service.BatchCreateLiveStreamsRequest(),
            parent="parent_value",
            requests=[
                live_stream_service.CreateLiveStreamRequest(parent="parent_value")
            ],
        )


def test_update_live_stream_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LiveStreamServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_live_stream in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_live_stream] = (
            mock_rpc
        )

        request = {}
        client.update_live_stream(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_live_stream(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_live_stream_rest_required_fields(
    request_type=live_stream_service.UpdateLiveStreamRequest,
):
    transport_class = transports.LiveStreamServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateLiveStream,
        "_BaseUpdateLiveStream__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = live_stream_messages.LiveStream()
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
            return_value = live_stream_messages.LiveStream.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_live_stream(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_live_stream_rest_flattened():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_messages.LiveStream()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "live_stream": {"name": "networks/sample1/liveStreams/sample2"}
        }

        # get truthy value for each flattened field
        mock_args = dict(
            live_stream=live_stream_messages.LiveStream(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = live_stream_messages.LiveStream.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_live_stream(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{live_stream.name=networks/*/liveStreams/*}"
            % client.transport._host,
            args[1],
        )


def test_update_live_stream_rest_flattened_error(transport: str = "rest"):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_live_stream(
            live_stream_service.UpdateLiveStreamRequest(),
            live_stream=live_stream_messages.LiveStream(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_batch_update_live_streams_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LiveStreamServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_update_live_streams
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_update_live_streams
        ] = mock_rpc

        request = {}
        client.batch_update_live_streams(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_update_live_streams(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_update_live_streams_rest_required_fields(
    request_type=live_stream_service.BatchUpdateLiveStreamsRequest,
):
    transport_class = transports.LiveStreamServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchUpdateLiveStreams,
        "_BaseBatchUpdateLiveStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = live_stream_service.BatchUpdateLiveStreamsResponse()
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
            return_value = live_stream_service.BatchUpdateLiveStreamsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_update_live_streams(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_update_live_streams_rest_flattened():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.BatchUpdateLiveStreamsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            requests=[
                live_stream_service.UpdateLiveStreamRequest(
                    live_stream=live_stream_messages.LiveStream(name="name_value")
                )
            ],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = live_stream_service.BatchUpdateLiveStreamsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_update_live_streams(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/liveStreams:batchUpdate"
            % client.transport._host,
            args[1],
        )


def test_batch_update_live_streams_rest_flattened_error(transport: str = "rest"):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_update_live_streams(
            live_stream_service.BatchUpdateLiveStreamsRequest(),
            parent="parent_value",
            requests=[
                live_stream_service.UpdateLiveStreamRequest(
                    live_stream=live_stream_messages.LiveStream(name="name_value")
                )
            ],
        )


def test_batch_activate_live_streams_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LiveStreamServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_activate_live_streams
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_activate_live_streams
        ] = mock_rpc

        request = {}
        client.batch_activate_live_streams(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_activate_live_streams(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_activate_live_streams_rest_required_fields(
    request_type=live_stream_service.BatchActivateLiveStreamsRequest,
):
    transport_class = transports.LiveStreamServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchActivateLiveStreams,
        "_BaseBatchActivateLiveStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = live_stream_service.BatchActivateLiveStreamsResponse()
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
            return_value = live_stream_service.BatchActivateLiveStreamsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_activate_live_streams(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_activate_live_streams_rest_flattened():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.BatchActivateLiveStreamsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = live_stream_service.BatchActivateLiveStreamsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_activate_live_streams(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/liveStreams:batchActivate"
            % client.transport._host,
            args[1],
        )


def test_batch_activate_live_streams_rest_flattened_error(transport: str = "rest"):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_activate_live_streams(
            live_stream_service.BatchActivateLiveStreamsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_pause_live_streams_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LiveStreamServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_pause_live_streams
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_pause_live_streams
        ] = mock_rpc

        request = {}
        client.batch_pause_live_streams(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_pause_live_streams(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_pause_live_streams_rest_required_fields(
    request_type=live_stream_service.BatchPauseLiveStreamsRequest,
):
    transport_class = transports.LiveStreamServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchPauseLiveStreams,
        "_BaseBatchPauseLiveStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = live_stream_service.BatchPauseLiveStreamsResponse()
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
            return_value = live_stream_service.BatchPauseLiveStreamsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_pause_live_streams(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_pause_live_streams_rest_flattened():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.BatchPauseLiveStreamsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = live_stream_service.BatchPauseLiveStreamsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_pause_live_streams(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/liveStreams:batchPause" % client.transport._host,
            args[1],
        )


def test_batch_pause_live_streams_rest_flattened_error(transport: str = "rest"):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_pause_live_streams(
            live_stream_service.BatchPauseLiveStreamsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_archive_live_streams_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LiveStreamServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_archive_live_streams
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_archive_live_streams
        ] = mock_rpc

        request = {}
        client.batch_archive_live_streams(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_archive_live_streams(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_archive_live_streams_rest_required_fields(
    request_type=live_stream_service.BatchArchiveLiveStreamsRequest,
):
    transport_class = transports.LiveStreamServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchArchiveLiveStreams,
        "_BaseBatchArchiveLiveStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = live_stream_service.BatchArchiveLiveStreamsResponse()
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
            return_value = live_stream_service.BatchArchiveLiveStreamsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_archive_live_streams(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_archive_live_streams_rest_flattened():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.BatchArchiveLiveStreamsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = live_stream_service.BatchArchiveLiveStreamsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_archive_live_streams(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/liveStreams:batchArchive"
            % client.transport._host,
            args[1],
        )


def test_batch_archive_live_streams_rest_flattened_error(transport: str = "rest"):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_archive_live_streams(
            live_stream_service.BatchArchiveLiveStreamsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_pause_ads_live_streams_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LiveStreamServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_pause_ads_live_streams
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_pause_ads_live_streams
        ] = mock_rpc

        request = {}
        client.batch_pause_ads_live_streams(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_pause_ads_live_streams(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_pause_ads_live_streams_rest_required_fields(
    request_type=live_stream_service.BatchPauseAdsLiveStreamsRequest,
):
    transport_class = transports.LiveStreamServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchPauseAdsLiveStreams,
        "_BaseBatchPauseAdsLiveStreams__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = live_stream_service.BatchPauseAdsLiveStreamsResponse()
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
            return_value = live_stream_service.BatchPauseAdsLiveStreamsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_pause_ads_live_streams(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_pause_ads_live_streams_rest_flattened():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.BatchPauseAdsLiveStreamsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = live_stream_service.BatchPauseAdsLiveStreamsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_pause_ads_live_streams(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/liveStreams:batchPauseAds"
            % client.transport._host,
            args[1],
        )


def test_batch_pause_ads_live_streams_rest_flattened_error(transport: str = "rest"):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_pause_ads_live_streams(
            live_stream_service.BatchPauseAdsLiveStreamsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_refresh_master_playlists_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LiveStreamServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_refresh_master_playlists
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_refresh_master_playlists
        ] = mock_rpc

        request = {}
        client.batch_refresh_master_playlists(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_refresh_master_playlists(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_refresh_master_playlists_rest_required_fields(
    request_type=live_stream_service.BatchRefreshMasterPlaylistsRequest,
):
    transport_class = transports.LiveStreamServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchRefreshMasterPlaylists,
        "_BaseBatchRefreshMasterPlaylists__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = live_stream_service.BatchRefreshMasterPlaylistsResponse()
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
            return_value = live_stream_service.BatchRefreshMasterPlaylistsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_refresh_master_playlists(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_refresh_master_playlists_rest_flattened():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.BatchRefreshMasterPlaylistsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = live_stream_service.BatchRefreshMasterPlaylistsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_refresh_master_playlists(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/liveStreams:batchRefreshMasterPlaylists"
            % client.transport._host,
            args[1],
        )


def test_batch_refresh_master_playlists_rest_flattened_error(transport: str = "rest"):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_refresh_master_playlists(
            live_stream_service.BatchRefreshMasterPlaylistsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = LiveStreamServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = LiveStreamServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = LiveStreamServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = LiveStreamServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = LiveStreamServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = LiveStreamServiceClient(transport=transport)
    assert client.transport is transport


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.LiveStreamServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_rest():
    transport = LiveStreamServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_get_live_stream_rest_bad_request(
    request_type=live_stream_service.GetLiveStreamRequest,
):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "networks/sample1/liveStreams/sample2"}
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
        client.get_live_stream(request)


@pytest.mark.parametrize(
    "request_type",
    [
        live_stream_service.GetLiveStreamRequest,
        dict,
    ],
)
def test_get_live_stream_rest_call_success(request_type):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "networks/sample1/liveStreams/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_messages.LiveStream(
            name="name_value",
            display_name="display_name_value",
            status=live_stream_event_enums.LiveStreamEventStatusEnum.LiveStreamEventStatus.ACTIVE,
            end_time_unlimited=True,
            content_urls=["content_urls_value"],
            ad_tags=["ad_tags_value"],
            asset_key="asset_key_value",
            slate="slate_value",
            enable_dai_authentication_keys=True,
            ad_break_fill_type=live_stream_event_enums.AdBreakFillTypeEnum.AdBreakFillType.MINIMIZE_SLATE,
            underfill_ad_break_fill_type=live_stream_event_enums.AdBreakFillTypeEnum.AdBreakFillType.MINIMIZE_SLATE,
            enable_max_filler_duration=True,
            enable_durationless_ad_breaks=True,
            dai_authentication_keys=["dai_authentication_keys_value"],
            source_content_configurations=["source_content_configurations_value"],
            ad_media_delivery_config="ad_media_delivery_config_value",
            allowlisted_ips_enabled=True,
            dynamic_ad_insertion_type=live_stream_event_enums.DynamicAdInsertionTypeEnum.DynamicAdInsertionType.LINEAR,
            relative_playlist_delivery_enabled=True,
            streaming_format=live_stream_event_enums.LiveStreamEventStreamingFormatEnum.LiveStreamEventStreamingFormat.DASH,
            prefetch_enabled=True,
            forced_cue_in_enabled=True,
            short_segment_dropping_enabled=True,
            custom_asset_key="custom_asset_key_value",
            dai_encoding_profiles=["dai_encoding_profiles_value"],
            segment_url_authentication_keys=["segment_url_authentication_keys_value"],
            ad_break_markups=[
                live_stream_event_enums.AdBreakMarkupTypeEnum.AdBreakMarkupType.HLS_DATERANGE_SPLICE
            ],
            ad_break_markup_types_enabled=True,
            early_break_notification_multi_break_scheduling_enabled=True,
            effective_asset_key="effective_asset_key_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = live_stream_messages.LiveStream.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_live_stream(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, live_stream_messages.LiveStream)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert (
        response.status
        == live_stream_event_enums.LiveStreamEventStatusEnum.LiveStreamEventStatus.ACTIVE
    )
    assert response.end_time_unlimited is True
    assert response.content_urls == ["content_urls_value"]
    assert response.ad_tags == ["ad_tags_value"]
    assert response.asset_key == "asset_key_value"
    assert response.slate == "slate_value"
    assert response.enable_dai_authentication_keys is True
    assert (
        response.ad_break_fill_type
        == live_stream_event_enums.AdBreakFillTypeEnum.AdBreakFillType.MINIMIZE_SLATE
    )
    assert (
        response.underfill_ad_break_fill_type
        == live_stream_event_enums.AdBreakFillTypeEnum.AdBreakFillType.MINIMIZE_SLATE
    )
    assert response.enable_max_filler_duration is True
    assert response.enable_durationless_ad_breaks is True
    assert response.dai_authentication_keys == ["dai_authentication_keys_value"]
    assert response.source_content_configurations == [
        "source_content_configurations_value"
    ]
    assert response.ad_media_delivery_config == "ad_media_delivery_config_value"
    assert response.allowlisted_ips_enabled is True
    assert (
        response.dynamic_ad_insertion_type
        == live_stream_event_enums.DynamicAdInsertionTypeEnum.DynamicAdInsertionType.LINEAR
    )
    assert response.relative_playlist_delivery_enabled is True
    assert (
        response.streaming_format
        == live_stream_event_enums.LiveStreamEventStreamingFormatEnum.LiveStreamEventStreamingFormat.DASH
    )
    assert response.prefetch_enabled is True
    assert response.forced_cue_in_enabled is True
    assert response.short_segment_dropping_enabled is True
    assert response.custom_asset_key == "custom_asset_key_value"
    assert response.dai_encoding_profiles == ["dai_encoding_profiles_value"]
    assert response.segment_url_authentication_keys == [
        "segment_url_authentication_keys_value"
    ]
    assert response.ad_break_markups == [
        live_stream_event_enums.AdBreakMarkupTypeEnum.AdBreakMarkupType.HLS_DATERANGE_SPLICE
    ]
    assert response.ad_break_markup_types_enabled is True
    assert response.early_break_notification_multi_break_scheduling_enabled is True
    assert response.effective_asset_key == "effective_asset_key_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_live_stream_rest_interceptors(null_interceptor):
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LiveStreamServiceRestInterceptor(),
    )
    client = LiveStreamServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor, "post_get_live_stream"
        ) as post,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_get_live_stream_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor, "pre_get_live_stream"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = live_stream_service.GetLiveStreamRequest.pb(
            live_stream_service.GetLiveStreamRequest()
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
        return_value = live_stream_messages.LiveStream.to_json(
            live_stream_messages.LiveStream()
        )
        req.return_value.content = return_value

        request = live_stream_service.GetLiveStreamRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = live_stream_messages.LiveStream()
        post_with_metadata.return_value = live_stream_messages.LiveStream(), metadata

        client.get_live_stream(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_live_streams_rest_bad_request(
    request_type=live_stream_service.ListLiveStreamsRequest,
):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.list_live_streams(request)


@pytest.mark.parametrize(
    "request_type",
    [
        live_stream_service.ListLiveStreamsRequest,
        dict,
    ],
)
def test_list_live_streams_rest_call_success(request_type):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.ListLiveStreamsResponse(
            next_page_token="next_page_token_value",
            total_size=1086,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = live_stream_service.ListLiveStreamsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_live_streams(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListLiveStreamsPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.total_size == 1086


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_live_streams_rest_interceptors(null_interceptor):
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LiveStreamServiceRestInterceptor(),
    )
    client = LiveStreamServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor, "post_list_live_streams"
        ) as post,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_list_live_streams_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor, "pre_list_live_streams"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = live_stream_service.ListLiveStreamsRequest.pb(
            live_stream_service.ListLiveStreamsRequest()
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
        return_value = live_stream_service.ListLiveStreamsResponse.to_json(
            live_stream_service.ListLiveStreamsResponse()
        )
        req.return_value.content = return_value

        request = live_stream_service.ListLiveStreamsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = live_stream_service.ListLiveStreamsResponse()
        post_with_metadata.return_value = (
            live_stream_service.ListLiveStreamsResponse(),
            metadata,
        )

        client.list_live_streams(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_live_stream_rest_bad_request(
    request_type=live_stream_service.CreateLiveStreamRequest,
):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.create_live_stream(request)


@pytest.mark.parametrize(
    "request_type",
    [
        live_stream_service.CreateLiveStreamRequest,
        dict,
    ],
)
def test_create_live_stream_rest_call_success(request_type):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request_init["live_stream"] = {
        "name": "name_value",
        "display_name": "display_name_value",
        "status": 1,
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "start_time": {},
        "end_time": {},
        "end_time_unlimited": True,
        "content_urls": ["content_urls_value1", "content_urls_value2"],
        "ad_tags": ["ad_tags_value1", "ad_tags_value2"],
        "asset_key": "asset_key_value",
        "slate": "slate_value",
        "dvr_window_duration": {"seconds": 751, "nanos": 543},
        "enable_dai_authentication_keys": True,
        "ad_break_fill_type": 1,
        "underfill_ad_break_fill_type": 1,
        "ad_holiday_duration": {},
        "enable_max_filler_duration": True,
        "max_filler_duration": {},
        "pod_serving_segment_duration": {},
        "enable_durationless_ad_breaks": True,
        "default_ad_break_duration": {},
        "dai_authentication_keys": [
            "dai_authentication_keys_value1",
            "dai_authentication_keys_value2",
        ],
        "source_content_configurations": [
            "source_content_configurations_value1",
            "source_content_configurations_value2",
        ],
        "ad_media_delivery_config": "ad_media_delivery_config_value",
        "preroll_settings": {"ad_tag": "ad_tag_value", "max_ad_pod_duration": {}},
        "hls_settings": {
            "playlist_type": 1,
            "master_playlist_settings": {"refresh_type": 1},
        },
        "allowlisted_ips_enabled": True,
        "dynamic_ad_insertion_type": 1,
        "relative_playlist_delivery_enabled": True,
        "streaming_format": 1,
        "prefetch_enabled": True,
        "prefetch_settings": {"stage_one_ad_request_duration": {}},
        "forced_cue_in_enabled": True,
        "short_segment_dropping_enabled": True,
        "custom_asset_key": "custom_asset_key_value",
        "dai_encoding_profiles": [
            "dai_encoding_profiles_value1",
            "dai_encoding_profiles_value2",
        ],
        "segment_url_authentication_keys": [
            "segment_url_authentication_keys_value1",
            "segment_url_authentication_keys_value2",
        ],
        "ad_break_markups": [1],
        "ad_break_markup_types_enabled": True,
        "live_stream_conditioning": {"dash_bridge": {"enabled": True}},
        "early_break_notification_multi_break_scheduling_enabled": True,
        "ad_pod_trim_tolerance": {},
        "effective_asset_key": "effective_asset_key_value",
        "auxiliary_ad_settings": {"ad_tag_url": "ad_tag_url_value"},
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = live_stream_service.CreateLiveStreamRequest.meta.fields["live_stream"]

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
    for field, value in request_init["live_stream"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["live_stream"][field])):
                    del request_init["live_stream"][field][i][subfield]
            else:
                del request_init["live_stream"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_messages.LiveStream(
            name="name_value",
            display_name="display_name_value",
            status=live_stream_event_enums.LiveStreamEventStatusEnum.LiveStreamEventStatus.ACTIVE,
            end_time_unlimited=True,
            content_urls=["content_urls_value"],
            ad_tags=["ad_tags_value"],
            asset_key="asset_key_value",
            slate="slate_value",
            enable_dai_authentication_keys=True,
            ad_break_fill_type=live_stream_event_enums.AdBreakFillTypeEnum.AdBreakFillType.MINIMIZE_SLATE,
            underfill_ad_break_fill_type=live_stream_event_enums.AdBreakFillTypeEnum.AdBreakFillType.MINIMIZE_SLATE,
            enable_max_filler_duration=True,
            enable_durationless_ad_breaks=True,
            dai_authentication_keys=["dai_authentication_keys_value"],
            source_content_configurations=["source_content_configurations_value"],
            ad_media_delivery_config="ad_media_delivery_config_value",
            allowlisted_ips_enabled=True,
            dynamic_ad_insertion_type=live_stream_event_enums.DynamicAdInsertionTypeEnum.DynamicAdInsertionType.LINEAR,
            relative_playlist_delivery_enabled=True,
            streaming_format=live_stream_event_enums.LiveStreamEventStreamingFormatEnum.LiveStreamEventStreamingFormat.DASH,
            prefetch_enabled=True,
            forced_cue_in_enabled=True,
            short_segment_dropping_enabled=True,
            custom_asset_key="custom_asset_key_value",
            dai_encoding_profiles=["dai_encoding_profiles_value"],
            segment_url_authentication_keys=["segment_url_authentication_keys_value"],
            ad_break_markups=[
                live_stream_event_enums.AdBreakMarkupTypeEnum.AdBreakMarkupType.HLS_DATERANGE_SPLICE
            ],
            ad_break_markup_types_enabled=True,
            early_break_notification_multi_break_scheduling_enabled=True,
            effective_asset_key="effective_asset_key_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = live_stream_messages.LiveStream.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_live_stream(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, live_stream_messages.LiveStream)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert (
        response.status
        == live_stream_event_enums.LiveStreamEventStatusEnum.LiveStreamEventStatus.ACTIVE
    )
    assert response.end_time_unlimited is True
    assert response.content_urls == ["content_urls_value"]
    assert response.ad_tags == ["ad_tags_value"]
    assert response.asset_key == "asset_key_value"
    assert response.slate == "slate_value"
    assert response.enable_dai_authentication_keys is True
    assert (
        response.ad_break_fill_type
        == live_stream_event_enums.AdBreakFillTypeEnum.AdBreakFillType.MINIMIZE_SLATE
    )
    assert (
        response.underfill_ad_break_fill_type
        == live_stream_event_enums.AdBreakFillTypeEnum.AdBreakFillType.MINIMIZE_SLATE
    )
    assert response.enable_max_filler_duration is True
    assert response.enable_durationless_ad_breaks is True
    assert response.dai_authentication_keys == ["dai_authentication_keys_value"]
    assert response.source_content_configurations == [
        "source_content_configurations_value"
    ]
    assert response.ad_media_delivery_config == "ad_media_delivery_config_value"
    assert response.allowlisted_ips_enabled is True
    assert (
        response.dynamic_ad_insertion_type
        == live_stream_event_enums.DynamicAdInsertionTypeEnum.DynamicAdInsertionType.LINEAR
    )
    assert response.relative_playlist_delivery_enabled is True
    assert (
        response.streaming_format
        == live_stream_event_enums.LiveStreamEventStreamingFormatEnum.LiveStreamEventStreamingFormat.DASH
    )
    assert response.prefetch_enabled is True
    assert response.forced_cue_in_enabled is True
    assert response.short_segment_dropping_enabled is True
    assert response.custom_asset_key == "custom_asset_key_value"
    assert response.dai_encoding_profiles == ["dai_encoding_profiles_value"]
    assert response.segment_url_authentication_keys == [
        "segment_url_authentication_keys_value"
    ]
    assert response.ad_break_markups == [
        live_stream_event_enums.AdBreakMarkupTypeEnum.AdBreakMarkupType.HLS_DATERANGE_SPLICE
    ]
    assert response.ad_break_markup_types_enabled is True
    assert response.early_break_notification_multi_break_scheduling_enabled is True
    assert response.effective_asset_key == "effective_asset_key_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_live_stream_rest_interceptors(null_interceptor):
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LiveStreamServiceRestInterceptor(),
    )
    client = LiveStreamServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor, "post_create_live_stream"
        ) as post,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_create_live_stream_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor, "pre_create_live_stream"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = live_stream_service.CreateLiveStreamRequest.pb(
            live_stream_service.CreateLiveStreamRequest()
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
        return_value = live_stream_messages.LiveStream.to_json(
            live_stream_messages.LiveStream()
        )
        req.return_value.content = return_value

        request = live_stream_service.CreateLiveStreamRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = live_stream_messages.LiveStream()
        post_with_metadata.return_value = live_stream_messages.LiveStream(), metadata

        client.create_live_stream(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_create_live_streams_rest_bad_request(
    request_type=live_stream_service.BatchCreateLiveStreamsRequest,
):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_create_live_streams(request)


@pytest.mark.parametrize(
    "request_type",
    [
        live_stream_service.BatchCreateLiveStreamsRequest,
        dict,
    ],
)
def test_batch_create_live_streams_rest_call_success(request_type):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.BatchCreateLiveStreamsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = live_stream_service.BatchCreateLiveStreamsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_create_live_streams(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, live_stream_service.BatchCreateLiveStreamsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_create_live_streams_rest_interceptors(null_interceptor):
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LiveStreamServiceRestInterceptor(),
    )
    client = LiveStreamServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_batch_create_live_streams",
        ) as post,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_batch_create_live_streams_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor, "pre_batch_create_live_streams"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = live_stream_service.BatchCreateLiveStreamsRequest.pb(
            live_stream_service.BatchCreateLiveStreamsRequest()
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
        return_value = live_stream_service.BatchCreateLiveStreamsResponse.to_json(
            live_stream_service.BatchCreateLiveStreamsResponse()
        )
        req.return_value.content = return_value

        request = live_stream_service.BatchCreateLiveStreamsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = live_stream_service.BatchCreateLiveStreamsResponse()
        post_with_metadata.return_value = (
            live_stream_service.BatchCreateLiveStreamsResponse(),
            metadata,
        )

        client.batch_create_live_streams(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_live_stream_rest_bad_request(
    request_type=live_stream_service.UpdateLiveStreamRequest,
):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"live_stream": {"name": "networks/sample1/liveStreams/sample2"}}
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
        client.update_live_stream(request)


@pytest.mark.parametrize(
    "request_type",
    [
        live_stream_service.UpdateLiveStreamRequest,
        dict,
    ],
)
def test_update_live_stream_rest_call_success(request_type):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"live_stream": {"name": "networks/sample1/liveStreams/sample2"}}
    request_init["live_stream"] = {
        "name": "networks/sample1/liveStreams/sample2",
        "display_name": "display_name_value",
        "status": 1,
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "start_time": {},
        "end_time": {},
        "end_time_unlimited": True,
        "content_urls": ["content_urls_value1", "content_urls_value2"],
        "ad_tags": ["ad_tags_value1", "ad_tags_value2"],
        "asset_key": "asset_key_value",
        "slate": "slate_value",
        "dvr_window_duration": {"seconds": 751, "nanos": 543},
        "enable_dai_authentication_keys": True,
        "ad_break_fill_type": 1,
        "underfill_ad_break_fill_type": 1,
        "ad_holiday_duration": {},
        "enable_max_filler_duration": True,
        "max_filler_duration": {},
        "pod_serving_segment_duration": {},
        "enable_durationless_ad_breaks": True,
        "default_ad_break_duration": {},
        "dai_authentication_keys": [
            "dai_authentication_keys_value1",
            "dai_authentication_keys_value2",
        ],
        "source_content_configurations": [
            "source_content_configurations_value1",
            "source_content_configurations_value2",
        ],
        "ad_media_delivery_config": "ad_media_delivery_config_value",
        "preroll_settings": {"ad_tag": "ad_tag_value", "max_ad_pod_duration": {}},
        "hls_settings": {
            "playlist_type": 1,
            "master_playlist_settings": {"refresh_type": 1},
        },
        "allowlisted_ips_enabled": True,
        "dynamic_ad_insertion_type": 1,
        "relative_playlist_delivery_enabled": True,
        "streaming_format": 1,
        "prefetch_enabled": True,
        "prefetch_settings": {"stage_one_ad_request_duration": {}},
        "forced_cue_in_enabled": True,
        "short_segment_dropping_enabled": True,
        "custom_asset_key": "custom_asset_key_value",
        "dai_encoding_profiles": [
            "dai_encoding_profiles_value1",
            "dai_encoding_profiles_value2",
        ],
        "segment_url_authentication_keys": [
            "segment_url_authentication_keys_value1",
            "segment_url_authentication_keys_value2",
        ],
        "ad_break_markups": [1],
        "ad_break_markup_types_enabled": True,
        "live_stream_conditioning": {"dash_bridge": {"enabled": True}},
        "early_break_notification_multi_break_scheduling_enabled": True,
        "ad_pod_trim_tolerance": {},
        "effective_asset_key": "effective_asset_key_value",
        "auxiliary_ad_settings": {"ad_tag_url": "ad_tag_url_value"},
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = live_stream_service.UpdateLiveStreamRequest.meta.fields["live_stream"]

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
    for field, value in request_init["live_stream"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["live_stream"][field])):
                    del request_init["live_stream"][field][i][subfield]
            else:
                del request_init["live_stream"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_messages.LiveStream(
            name="name_value",
            display_name="display_name_value",
            status=live_stream_event_enums.LiveStreamEventStatusEnum.LiveStreamEventStatus.ACTIVE,
            end_time_unlimited=True,
            content_urls=["content_urls_value"],
            ad_tags=["ad_tags_value"],
            asset_key="asset_key_value",
            slate="slate_value",
            enable_dai_authentication_keys=True,
            ad_break_fill_type=live_stream_event_enums.AdBreakFillTypeEnum.AdBreakFillType.MINIMIZE_SLATE,
            underfill_ad_break_fill_type=live_stream_event_enums.AdBreakFillTypeEnum.AdBreakFillType.MINIMIZE_SLATE,
            enable_max_filler_duration=True,
            enable_durationless_ad_breaks=True,
            dai_authentication_keys=["dai_authentication_keys_value"],
            source_content_configurations=["source_content_configurations_value"],
            ad_media_delivery_config="ad_media_delivery_config_value",
            allowlisted_ips_enabled=True,
            dynamic_ad_insertion_type=live_stream_event_enums.DynamicAdInsertionTypeEnum.DynamicAdInsertionType.LINEAR,
            relative_playlist_delivery_enabled=True,
            streaming_format=live_stream_event_enums.LiveStreamEventStreamingFormatEnum.LiveStreamEventStreamingFormat.DASH,
            prefetch_enabled=True,
            forced_cue_in_enabled=True,
            short_segment_dropping_enabled=True,
            custom_asset_key="custom_asset_key_value",
            dai_encoding_profiles=["dai_encoding_profiles_value"],
            segment_url_authentication_keys=["segment_url_authentication_keys_value"],
            ad_break_markups=[
                live_stream_event_enums.AdBreakMarkupTypeEnum.AdBreakMarkupType.HLS_DATERANGE_SPLICE
            ],
            ad_break_markup_types_enabled=True,
            early_break_notification_multi_break_scheduling_enabled=True,
            effective_asset_key="effective_asset_key_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = live_stream_messages.LiveStream.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_live_stream(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, live_stream_messages.LiveStream)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert (
        response.status
        == live_stream_event_enums.LiveStreamEventStatusEnum.LiveStreamEventStatus.ACTIVE
    )
    assert response.end_time_unlimited is True
    assert response.content_urls == ["content_urls_value"]
    assert response.ad_tags == ["ad_tags_value"]
    assert response.asset_key == "asset_key_value"
    assert response.slate == "slate_value"
    assert response.enable_dai_authentication_keys is True
    assert (
        response.ad_break_fill_type
        == live_stream_event_enums.AdBreakFillTypeEnum.AdBreakFillType.MINIMIZE_SLATE
    )
    assert (
        response.underfill_ad_break_fill_type
        == live_stream_event_enums.AdBreakFillTypeEnum.AdBreakFillType.MINIMIZE_SLATE
    )
    assert response.enable_max_filler_duration is True
    assert response.enable_durationless_ad_breaks is True
    assert response.dai_authentication_keys == ["dai_authentication_keys_value"]
    assert response.source_content_configurations == [
        "source_content_configurations_value"
    ]
    assert response.ad_media_delivery_config == "ad_media_delivery_config_value"
    assert response.allowlisted_ips_enabled is True
    assert (
        response.dynamic_ad_insertion_type
        == live_stream_event_enums.DynamicAdInsertionTypeEnum.DynamicAdInsertionType.LINEAR
    )
    assert response.relative_playlist_delivery_enabled is True
    assert (
        response.streaming_format
        == live_stream_event_enums.LiveStreamEventStreamingFormatEnum.LiveStreamEventStreamingFormat.DASH
    )
    assert response.prefetch_enabled is True
    assert response.forced_cue_in_enabled is True
    assert response.short_segment_dropping_enabled is True
    assert response.custom_asset_key == "custom_asset_key_value"
    assert response.dai_encoding_profiles == ["dai_encoding_profiles_value"]
    assert response.segment_url_authentication_keys == [
        "segment_url_authentication_keys_value"
    ]
    assert response.ad_break_markups == [
        live_stream_event_enums.AdBreakMarkupTypeEnum.AdBreakMarkupType.HLS_DATERANGE_SPLICE
    ]
    assert response.ad_break_markup_types_enabled is True
    assert response.early_break_notification_multi_break_scheduling_enabled is True
    assert response.effective_asset_key == "effective_asset_key_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_live_stream_rest_interceptors(null_interceptor):
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LiveStreamServiceRestInterceptor(),
    )
    client = LiveStreamServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor, "post_update_live_stream"
        ) as post,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_update_live_stream_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor, "pre_update_live_stream"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = live_stream_service.UpdateLiveStreamRequest.pb(
            live_stream_service.UpdateLiveStreamRequest()
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
        return_value = live_stream_messages.LiveStream.to_json(
            live_stream_messages.LiveStream()
        )
        req.return_value.content = return_value

        request = live_stream_service.UpdateLiveStreamRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = live_stream_messages.LiveStream()
        post_with_metadata.return_value = live_stream_messages.LiveStream(), metadata

        client.update_live_stream(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_update_live_streams_rest_bad_request(
    request_type=live_stream_service.BatchUpdateLiveStreamsRequest,
):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_update_live_streams(request)


@pytest.mark.parametrize(
    "request_type",
    [
        live_stream_service.BatchUpdateLiveStreamsRequest,
        dict,
    ],
)
def test_batch_update_live_streams_rest_call_success(request_type):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.BatchUpdateLiveStreamsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = live_stream_service.BatchUpdateLiveStreamsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_update_live_streams(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, live_stream_service.BatchUpdateLiveStreamsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_update_live_streams_rest_interceptors(null_interceptor):
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LiveStreamServiceRestInterceptor(),
    )
    client = LiveStreamServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_batch_update_live_streams",
        ) as post,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_batch_update_live_streams_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor, "pre_batch_update_live_streams"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = live_stream_service.BatchUpdateLiveStreamsRequest.pb(
            live_stream_service.BatchUpdateLiveStreamsRequest()
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
        return_value = live_stream_service.BatchUpdateLiveStreamsResponse.to_json(
            live_stream_service.BatchUpdateLiveStreamsResponse()
        )
        req.return_value.content = return_value

        request = live_stream_service.BatchUpdateLiveStreamsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = live_stream_service.BatchUpdateLiveStreamsResponse()
        post_with_metadata.return_value = (
            live_stream_service.BatchUpdateLiveStreamsResponse(),
            metadata,
        )

        client.batch_update_live_streams(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_activate_live_streams_rest_bad_request(
    request_type=live_stream_service.BatchActivateLiveStreamsRequest,
):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_activate_live_streams(request)


@pytest.mark.parametrize(
    "request_type",
    [
        live_stream_service.BatchActivateLiveStreamsRequest,
        dict,
    ],
)
def test_batch_activate_live_streams_rest_call_success(request_type):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.BatchActivateLiveStreamsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = live_stream_service.BatchActivateLiveStreamsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_activate_live_streams(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, live_stream_service.BatchActivateLiveStreamsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_activate_live_streams_rest_interceptors(null_interceptor):
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LiveStreamServiceRestInterceptor(),
    )
    client = LiveStreamServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_batch_activate_live_streams",
        ) as post,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_batch_activate_live_streams_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "pre_batch_activate_live_streams",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = live_stream_service.BatchActivateLiveStreamsRequest.pb(
            live_stream_service.BatchActivateLiveStreamsRequest()
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
        return_value = live_stream_service.BatchActivateLiveStreamsResponse.to_json(
            live_stream_service.BatchActivateLiveStreamsResponse()
        )
        req.return_value.content = return_value

        request = live_stream_service.BatchActivateLiveStreamsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = live_stream_service.BatchActivateLiveStreamsResponse()
        post_with_metadata.return_value = (
            live_stream_service.BatchActivateLiveStreamsResponse(),
            metadata,
        )

        client.batch_activate_live_streams(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_pause_live_streams_rest_bad_request(
    request_type=live_stream_service.BatchPauseLiveStreamsRequest,
):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_pause_live_streams(request)


@pytest.mark.parametrize(
    "request_type",
    [
        live_stream_service.BatchPauseLiveStreamsRequest,
        dict,
    ],
)
def test_batch_pause_live_streams_rest_call_success(request_type):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.BatchPauseLiveStreamsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = live_stream_service.BatchPauseLiveStreamsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_pause_live_streams(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, live_stream_service.BatchPauseLiveStreamsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_pause_live_streams_rest_interceptors(null_interceptor):
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LiveStreamServiceRestInterceptor(),
    )
    client = LiveStreamServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor, "post_batch_pause_live_streams"
        ) as post,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_batch_pause_live_streams_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor, "pre_batch_pause_live_streams"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = live_stream_service.BatchPauseLiveStreamsRequest.pb(
            live_stream_service.BatchPauseLiveStreamsRequest()
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
        return_value = live_stream_service.BatchPauseLiveStreamsResponse.to_json(
            live_stream_service.BatchPauseLiveStreamsResponse()
        )
        req.return_value.content = return_value

        request = live_stream_service.BatchPauseLiveStreamsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = live_stream_service.BatchPauseLiveStreamsResponse()
        post_with_metadata.return_value = (
            live_stream_service.BatchPauseLiveStreamsResponse(),
            metadata,
        )

        client.batch_pause_live_streams(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_archive_live_streams_rest_bad_request(
    request_type=live_stream_service.BatchArchiveLiveStreamsRequest,
):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_archive_live_streams(request)


@pytest.mark.parametrize(
    "request_type",
    [
        live_stream_service.BatchArchiveLiveStreamsRequest,
        dict,
    ],
)
def test_batch_archive_live_streams_rest_call_success(request_type):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.BatchArchiveLiveStreamsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = live_stream_service.BatchArchiveLiveStreamsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_archive_live_streams(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, live_stream_service.BatchArchiveLiveStreamsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_archive_live_streams_rest_interceptors(null_interceptor):
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LiveStreamServiceRestInterceptor(),
    )
    client = LiveStreamServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_batch_archive_live_streams",
        ) as post,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_batch_archive_live_streams_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "pre_batch_archive_live_streams",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = live_stream_service.BatchArchiveLiveStreamsRequest.pb(
            live_stream_service.BatchArchiveLiveStreamsRequest()
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
        return_value = live_stream_service.BatchArchiveLiveStreamsResponse.to_json(
            live_stream_service.BatchArchiveLiveStreamsResponse()
        )
        req.return_value.content = return_value

        request = live_stream_service.BatchArchiveLiveStreamsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = live_stream_service.BatchArchiveLiveStreamsResponse()
        post_with_metadata.return_value = (
            live_stream_service.BatchArchiveLiveStreamsResponse(),
            metadata,
        )

        client.batch_archive_live_streams(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_pause_ads_live_streams_rest_bad_request(
    request_type=live_stream_service.BatchPauseAdsLiveStreamsRequest,
):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_pause_ads_live_streams(request)


@pytest.mark.parametrize(
    "request_type",
    [
        live_stream_service.BatchPauseAdsLiveStreamsRequest,
        dict,
    ],
)
def test_batch_pause_ads_live_streams_rest_call_success(request_type):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.BatchPauseAdsLiveStreamsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = live_stream_service.BatchPauseAdsLiveStreamsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_pause_ads_live_streams(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, live_stream_service.BatchPauseAdsLiveStreamsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_pause_ads_live_streams_rest_interceptors(null_interceptor):
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LiveStreamServiceRestInterceptor(),
    )
    client = LiveStreamServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_batch_pause_ads_live_streams",
        ) as post,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_batch_pause_ads_live_streams_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "pre_batch_pause_ads_live_streams",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = live_stream_service.BatchPauseAdsLiveStreamsRequest.pb(
            live_stream_service.BatchPauseAdsLiveStreamsRequest()
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
        return_value = live_stream_service.BatchPauseAdsLiveStreamsResponse.to_json(
            live_stream_service.BatchPauseAdsLiveStreamsResponse()
        )
        req.return_value.content = return_value

        request = live_stream_service.BatchPauseAdsLiveStreamsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = live_stream_service.BatchPauseAdsLiveStreamsResponse()
        post_with_metadata.return_value = (
            live_stream_service.BatchPauseAdsLiveStreamsResponse(),
            metadata,
        )

        client.batch_pause_ads_live_streams(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_refresh_master_playlists_rest_bad_request(
    request_type=live_stream_service.BatchRefreshMasterPlaylistsRequest,
):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_refresh_master_playlists(request)


@pytest.mark.parametrize(
    "request_type",
    [
        live_stream_service.BatchRefreshMasterPlaylistsRequest,
        dict,
    ],
)
def test_batch_refresh_master_playlists_rest_call_success(request_type):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = live_stream_service.BatchRefreshMasterPlaylistsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = live_stream_service.BatchRefreshMasterPlaylistsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_refresh_master_playlists(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, live_stream_service.BatchRefreshMasterPlaylistsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_refresh_master_playlists_rest_interceptors(null_interceptor):
    transport = transports.LiveStreamServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LiveStreamServiceRestInterceptor(),
    )
    client = LiveStreamServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_batch_refresh_master_playlists",
        ) as post,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "post_batch_refresh_master_playlists_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LiveStreamServiceRestInterceptor,
            "pre_batch_refresh_master_playlists",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = live_stream_service.BatchRefreshMasterPlaylistsRequest.pb(
            live_stream_service.BatchRefreshMasterPlaylistsRequest()
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
        return_value = live_stream_service.BatchRefreshMasterPlaylistsResponse.to_json(
            live_stream_service.BatchRefreshMasterPlaylistsResponse()
        )
        req.return_value.content = return_value

        request = live_stream_service.BatchRefreshMasterPlaylistsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = live_stream_service.BatchRefreshMasterPlaylistsResponse()
        post_with_metadata.return_value = (
            live_stream_service.BatchRefreshMasterPlaylistsResponse(),
            metadata,
        )

        client.batch_refresh_master_playlists(
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
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict(
        {"name": "networks/sample1/operations/reports/runs/sample2"}, request
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
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {"name": "networks/sample1/operations/reports/runs/sample2"}
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
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict(
        {"name": "networks/sample1/operations/reports/runs/sample2"}, request
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
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {"name": "networks/sample1/operations/reports/runs/sample2"}
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


def test_initialize_client_w_rest():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_live_stream_empty_call_rest():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_live_stream), "__call__") as call:
        client.get_live_stream(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = live_stream_service.GetLiveStreamRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_live_streams_empty_call_rest():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_live_streams), "__call__"
    ) as call:
        client.list_live_streams(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = live_stream_service.ListLiveStreamsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_live_stream_empty_call_rest():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_live_stream), "__call__"
    ) as call:
        client.create_live_stream(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = live_stream_service.CreateLiveStreamRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_create_live_streams_empty_call_rest():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_live_streams), "__call__"
    ) as call:
        client.batch_create_live_streams(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = live_stream_service.BatchCreateLiveStreamsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_live_stream_empty_call_rest():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_live_stream), "__call__"
    ) as call:
        client.update_live_stream(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = live_stream_service.UpdateLiveStreamRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_update_live_streams_empty_call_rest():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_update_live_streams), "__call__"
    ) as call:
        client.batch_update_live_streams(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = live_stream_service.BatchUpdateLiveStreamsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_activate_live_streams_empty_call_rest():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_activate_live_streams), "__call__"
    ) as call:
        client.batch_activate_live_streams(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = live_stream_service.BatchActivateLiveStreamsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_pause_live_streams_empty_call_rest():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_pause_live_streams), "__call__"
    ) as call:
        client.batch_pause_live_streams(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = live_stream_service.BatchPauseLiveStreamsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_archive_live_streams_empty_call_rest():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_archive_live_streams), "__call__"
    ) as call:
        client.batch_archive_live_streams(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = live_stream_service.BatchArchiveLiveStreamsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_pause_ads_live_streams_empty_call_rest():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_pause_ads_live_streams), "__call__"
    ) as call:
        client.batch_pause_ads_live_streams(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = live_stream_service.BatchPauseAdsLiveStreamsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_refresh_master_playlists_empty_call_rest():
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_refresh_master_playlists), "__call__"
    ) as call:
        client.batch_refresh_master_playlists(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = live_stream_service.BatchRefreshMasterPlaylistsRequest()
        assert args[0] == request_msg


def test_live_stream_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.LiveStreamServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_live_stream_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.ads.admanager_v1.services.live_stream_service.transports.LiveStreamServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.LiveStreamServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "get_live_stream",
        "list_live_streams",
        "create_live_stream",
        "batch_create_live_streams",
        "update_live_stream",
        "batch_update_live_streams",
        "batch_activate_live_streams",
        "batch_pause_live_streams",
        "batch_archive_live_streams",
        "batch_pause_ads_live_streams",
        "batch_refresh_master_playlists",
        "get_operation",
        "cancel_operation",
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


def test_live_stream_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.ads.admanager_v1.services.live_stream_service.transports.LiveStreamServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.LiveStreamServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/admanager",
                "https://www.googleapis.com/auth/admanager.readonly",
            ),
            quota_project_id="octopus",
        )


def test_live_stream_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.ads.admanager_v1.services.live_stream_service.transports.LiveStreamServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.LiveStreamServiceTransport()
        adc.assert_called_once()


def test_live_stream_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        LiveStreamServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/admanager",
                "https://www.googleapis.com/auth/admanager.readonly",
            ),
            quota_project_id=None,
        )


def test_live_stream_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.LiveStreamServiceRestTransport(
            credentials=cred, client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_live_stream_service_host_no_port(transport_name):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="admanager.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "admanager.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://admanager.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_live_stream_service_host_with_port(transport_name):
    client = LiveStreamServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="admanager.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "admanager.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://admanager.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_live_stream_service_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = LiveStreamServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = LiveStreamServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.get_live_stream._session
    session2 = client2.transport.get_live_stream._session
    assert session1 != session2
    session1 = client1.transport.list_live_streams._session
    session2 = client2.transport.list_live_streams._session
    assert session1 != session2
    session1 = client1.transport.create_live_stream._session
    session2 = client2.transport.create_live_stream._session
    assert session1 != session2
    session1 = client1.transport.batch_create_live_streams._session
    session2 = client2.transport.batch_create_live_streams._session
    assert session1 != session2
    session1 = client1.transport.update_live_stream._session
    session2 = client2.transport.update_live_stream._session
    assert session1 != session2
    session1 = client1.transport.batch_update_live_streams._session
    session2 = client2.transport.batch_update_live_streams._session
    assert session1 != session2
    session1 = client1.transport.batch_activate_live_streams._session
    session2 = client2.transport.batch_activate_live_streams._session
    assert session1 != session2
    session1 = client1.transport.batch_pause_live_streams._session
    session2 = client2.transport.batch_pause_live_streams._session
    assert session1 != session2
    session1 = client1.transport.batch_archive_live_streams._session
    session2 = client2.transport.batch_archive_live_streams._session
    assert session1 != session2
    session1 = client1.transport.batch_pause_ads_live_streams._session
    session2 = client2.transport.batch_pause_ads_live_streams._session
    assert session1 != session2
    session1 = client1.transport.batch_refresh_master_playlists._session
    session2 = client2.transport.batch_refresh_master_playlists._session
    assert session1 != session2


def test_cdn_config_path():
    network_code = "squid"
    cdn_config = "clam"
    expected = "networks/{network_code}/cdnConfigs/{cdn_config}".format(
        network_code=network_code,
        cdn_config=cdn_config,
    )
    actual = LiveStreamServiceClient.cdn_config_path(network_code, cdn_config)
    assert expected == actual


def test_parse_cdn_config_path():
    expected = {
        "network_code": "whelk",
        "cdn_config": "octopus",
    }
    path = LiveStreamServiceClient.cdn_config_path(**expected)

    # Check that the path construction is reversible.
    actual = LiveStreamServiceClient.parse_cdn_config_path(path)
    assert expected == actual


def test_dai_authentication_key_path():
    network_code = "oyster"
    dai_authentication_key = "nudibranch"
    expected = (
        "networks/{network_code}/daiAuthenticationKeys/{dai_authentication_key}".format(
            network_code=network_code,
            dai_authentication_key=dai_authentication_key,
        )
    )
    actual = LiveStreamServiceClient.dai_authentication_key_path(
        network_code, dai_authentication_key
    )
    assert expected == actual


def test_parse_dai_authentication_key_path():
    expected = {
        "network_code": "cuttlefish",
        "dai_authentication_key": "mussel",
    }
    path = LiveStreamServiceClient.dai_authentication_key_path(**expected)

    # Check that the path construction is reversible.
    actual = LiveStreamServiceClient.parse_dai_authentication_key_path(path)
    assert expected == actual


def test_dai_encoding_profile_path():
    network_code = "winkle"
    dai_encoding_profile = "nautilus"
    expected = (
        "networks/{network_code}/daiEncodingProfiles/{dai_encoding_profile}".format(
            network_code=network_code,
            dai_encoding_profile=dai_encoding_profile,
        )
    )
    actual = LiveStreamServiceClient.dai_encoding_profile_path(
        network_code, dai_encoding_profile
    )
    assert expected == actual


def test_parse_dai_encoding_profile_path():
    expected = {
        "network_code": "scallop",
        "dai_encoding_profile": "abalone",
    }
    path = LiveStreamServiceClient.dai_encoding_profile_path(**expected)

    # Check that the path construction is reversible.
    actual = LiveStreamServiceClient.parse_dai_encoding_profile_path(path)
    assert expected == actual


def test_live_stream_path():
    network_code = "squid"
    live_stream = "clam"
    expected = "networks/{network_code}/liveStreams/{live_stream}".format(
        network_code=network_code,
        live_stream=live_stream,
    )
    actual = LiveStreamServiceClient.live_stream_path(network_code, live_stream)
    assert expected == actual


def test_parse_live_stream_path():
    expected = {
        "network_code": "whelk",
        "live_stream": "octopus",
    }
    path = LiveStreamServiceClient.live_stream_path(**expected)

    # Check that the path construction is reversible.
    actual = LiveStreamServiceClient.parse_live_stream_path(path)
    assert expected == actual


def test_network_path():
    network_code = "oyster"
    expected = "networks/{network_code}".format(
        network_code=network_code,
    )
    actual = LiveStreamServiceClient.network_path(network_code)
    assert expected == actual


def test_parse_network_path():
    expected = {
        "network_code": "nudibranch",
    }
    path = LiveStreamServiceClient.network_path(**expected)

    # Check that the path construction is reversible.
    actual = LiveStreamServiceClient.parse_network_path(path)
    assert expected == actual


def test_slate_path():
    network_code = "cuttlefish"
    slate = "mussel"
    expected = "networks/{network_code}/slates/{slate}".format(
        network_code=network_code,
        slate=slate,
    )
    actual = LiveStreamServiceClient.slate_path(network_code, slate)
    assert expected == actual


def test_parse_slate_path():
    expected = {
        "network_code": "winkle",
        "slate": "nautilus",
    }
    path = LiveStreamServiceClient.slate_path(**expected)

    # Check that the path construction is reversible.
    actual = LiveStreamServiceClient.parse_slate_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "scallop"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = LiveStreamServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "abalone",
    }
    path = LiveStreamServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = LiveStreamServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "squid"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = LiveStreamServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "clam",
    }
    path = LiveStreamServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = LiveStreamServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "whelk"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = LiveStreamServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "octopus",
    }
    path = LiveStreamServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = LiveStreamServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "oyster"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = LiveStreamServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "nudibranch",
    }
    path = LiveStreamServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = LiveStreamServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "cuttlefish"
    location = "mussel"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = LiveStreamServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "winkle",
        "location": "nautilus",
    }
    path = LiveStreamServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = LiveStreamServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.LiveStreamServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = LiveStreamServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.LiveStreamServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = LiveStreamServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_rest():
    client = LiveStreamServiceClient(
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
    ]
    for transport in transports:
        client = LiveStreamServiceClient(
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
        (LiveStreamServiceClient, transports.LiveStreamServiceRestTransport),
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
