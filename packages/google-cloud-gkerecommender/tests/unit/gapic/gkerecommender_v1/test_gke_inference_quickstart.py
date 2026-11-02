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

from google.cloud.gkerecommender_v1.services.gke_inference_quickstart import (
    GkeInferenceQuickstartAsyncClient,
    GkeInferenceQuickstartClient,
    pagers,
    transports,
)
from google.cloud.gkerecommender_v1.types import gkerecommender

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

    assert GkeInferenceQuickstartClient._get_client_cert_source(None, False) is None
    assert (
        GkeInferenceQuickstartClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        GkeInferenceQuickstartClient._get_client_cert_source(
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
                GkeInferenceQuickstartClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                GkeInferenceQuickstartClient._get_client_cert_source(
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
    client = GkeInferenceQuickstartClient(credentials=cred)
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
    client = GkeInferenceQuickstartClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (GkeInferenceQuickstartClient, "grpc"),
        (GkeInferenceQuickstartAsyncClient, "grpc_asyncio"),
        (GkeInferenceQuickstartClient, "rest"),
    ],
)
def test_gke_inference_quickstart_client_from_service_account_info(
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
            "gkerecommender.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://gkerecommender.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.GkeInferenceQuickstartGrpcTransport, "grpc"),
        (transports.GkeInferenceQuickstartGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.GkeInferenceQuickstartRestTransport, "rest"),
    ],
)
def test_gke_inference_quickstart_client_service_account_always_use_jwt(
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
        (GkeInferenceQuickstartClient, "grpc"),
        (GkeInferenceQuickstartAsyncClient, "grpc_asyncio"),
        (GkeInferenceQuickstartClient, "rest"),
    ],
)
def test_gke_inference_quickstart_client_from_service_account_file(
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
            "gkerecommender.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://gkerecommender.googleapis.com"
        )


def test_gke_inference_quickstart_client_get_transport_class():
    transport = GkeInferenceQuickstartClient.get_transport_class()
    available_transports = [
        transports.GkeInferenceQuickstartGrpcTransport,
        transports.GkeInferenceQuickstartRestTransport,
    ]
    assert transport in available_transports

    transport = GkeInferenceQuickstartClient.get_transport_class("grpc")
    assert transport == transports.GkeInferenceQuickstartGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            GkeInferenceQuickstartClient,
            transports.GkeInferenceQuickstartGrpcTransport,
            "grpc",
        ),
        (
            GkeInferenceQuickstartAsyncClient,
            transports.GkeInferenceQuickstartGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            GkeInferenceQuickstartClient,
            transports.GkeInferenceQuickstartRestTransport,
            "rest",
        ),
    ],
)
@mock.patch.object(
    GkeInferenceQuickstartClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(GkeInferenceQuickstartClient),
)
@mock.patch.object(
    GkeInferenceQuickstartAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(GkeInferenceQuickstartAsyncClient),
)
def test_gke_inference_quickstart_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(GkeInferenceQuickstartClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(GkeInferenceQuickstartClient, "get_transport_class") as gtc:
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
            GkeInferenceQuickstartClient,
            transports.GkeInferenceQuickstartGrpcTransport,
            "grpc",
            "true",
        ),
        (
            GkeInferenceQuickstartAsyncClient,
            transports.GkeInferenceQuickstartGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            GkeInferenceQuickstartClient,
            transports.GkeInferenceQuickstartGrpcTransport,
            "grpc",
            "false",
        ),
        (
            GkeInferenceQuickstartAsyncClient,
            transports.GkeInferenceQuickstartGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (
            GkeInferenceQuickstartClient,
            transports.GkeInferenceQuickstartRestTransport,
            "rest",
            "true",
        ),
        (
            GkeInferenceQuickstartClient,
            transports.GkeInferenceQuickstartRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    GkeInferenceQuickstartClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(GkeInferenceQuickstartClient),
)
@mock.patch.object(
    GkeInferenceQuickstartAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(GkeInferenceQuickstartAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_gke_inference_quickstart_client_mtls_env_auto(
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
    "client_class", [GkeInferenceQuickstartClient, GkeInferenceQuickstartAsyncClient]
)
@mock.patch.object(
    GkeInferenceQuickstartClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(GkeInferenceQuickstartClient),
)
@mock.patch.object(
    GkeInferenceQuickstartAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(GkeInferenceQuickstartAsyncClient),
)
def test_gke_inference_quickstart_client_get_mtls_endpoint_and_cert_source(
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
    "client_class", [GkeInferenceQuickstartClient, GkeInferenceQuickstartAsyncClient]
)
@mock.patch.object(
    GkeInferenceQuickstartClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(GkeInferenceQuickstartClient),
)
@mock.patch.object(
    GkeInferenceQuickstartAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(GkeInferenceQuickstartAsyncClient),
)
def test_gke_inference_quickstart_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = GkeInferenceQuickstartClient._DEFAULT_UNIVERSE
    default_endpoint = GkeInferenceQuickstartClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = GkeInferenceQuickstartClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
            GkeInferenceQuickstartClient,
            transports.GkeInferenceQuickstartGrpcTransport,
            "grpc",
        ),
        (
            GkeInferenceQuickstartAsyncClient,
            transports.GkeInferenceQuickstartGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            GkeInferenceQuickstartClient,
            transports.GkeInferenceQuickstartRestTransport,
            "rest",
        ),
    ],
)
def test_gke_inference_quickstart_client_client_options_scopes(
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
            GkeInferenceQuickstartClient,
            transports.GkeInferenceQuickstartGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            GkeInferenceQuickstartAsyncClient,
            transports.GkeInferenceQuickstartGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (
            GkeInferenceQuickstartClient,
            transports.GkeInferenceQuickstartRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_gke_inference_quickstart_client_client_options_credentials_file(
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


def test_gke_inference_quickstart_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.gkerecommender_v1.services.gke_inference_quickstart.transports.GkeInferenceQuickstartGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = GkeInferenceQuickstartClient(
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
            GkeInferenceQuickstartClient,
            transports.GkeInferenceQuickstartGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            GkeInferenceQuickstartAsyncClient,
            transports.GkeInferenceQuickstartGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_gke_inference_quickstart_client_create_channel_credentials_file(
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
            "gkerecommender.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=None,
            default_host="gkerecommender.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchModelsRequest(),
        {},
    ],
)
def test_fetch_models(request_type, transport: str = "grpc"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_models), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gkerecommender.FetchModelsResponse(
            models=["models_value"],
            next_page_token="next_page_token_value",
        )
        response = client.fetch_models(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gkerecommender.FetchModelsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.FetchModelsPager)
    assert response.models == ["models_value"]
    assert response.next_page_token == "next_page_token_value"


def test_fetch_models_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gkerecommender.FetchModelsRequest(
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_models), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.fetch_models(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchModelsRequest(
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_fetch_models_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.fetch_models in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.fetch_models] = mock_rpc
        request = {}
        client.fetch_models(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fetch_models(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_fetch_models_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.fetch_models
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.fetch_models
        ] = mock_rpc

        request = {}
        await client.fetch_models(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.fetch_models(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchModelsRequest(),
        {},
    ],
)
async def test_fetch_models_async(request_type, transport: str = "grpc_asyncio"):
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_models), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gkerecommender.FetchModelsResponse(
                models=["models_value"],
                next_page_token="next_page_token_value",
            )
        )
        response = await client.fetch_models(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gkerecommender.FetchModelsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.FetchModelsAsyncPager)
    assert response.models == ["models_value"]
    assert response.next_page_token == "next_page_token_value"


def test_fetch_models_pager(transport_name: str = "grpc"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_models), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelsResponse(
                models=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        pager = client.fetch_models(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, str) for i in results)


def test_fetch_models_pages(transport_name: str = "grpc"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_models), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelsResponse(
                models=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.fetch_models(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_fetch_models_async_pager():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_models), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelsResponse(
                models=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.fetch_models(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, str) for i in responses)


@pytest.mark.asyncio
async def test_fetch_models_async_pages():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_models), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelsResponse(
                models=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.fetch_models(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchModelServersRequest(),
        {},
    ],
)
def test_fetch_model_servers(request_type, transport: str = "grpc"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_servers), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gkerecommender.FetchModelServersResponse(
            model_servers=["model_servers_value"],
            next_page_token="next_page_token_value",
        )
        response = client.fetch_model_servers(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gkerecommender.FetchModelServersRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.FetchModelServersPager)
    assert response.model_servers == ["model_servers_value"]
    assert response.next_page_token == "next_page_token_value"


def test_fetch_model_servers_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gkerecommender.FetchModelServersRequest(
        model="model_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_servers), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.fetch_model_servers(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchModelServersRequest(
            model="model_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_fetch_model_servers_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.fetch_model_servers in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.fetch_model_servers] = (
            mock_rpc
        )
        request = {}
        client.fetch_model_servers(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fetch_model_servers(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_fetch_model_servers_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.fetch_model_servers
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.fetch_model_servers
        ] = mock_rpc

        request = {}
        await client.fetch_model_servers(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.fetch_model_servers(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchModelServersRequest(),
        {},
    ],
)
async def test_fetch_model_servers_async(request_type, transport: str = "grpc_asyncio"):
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_servers), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gkerecommender.FetchModelServersResponse(
                model_servers=["model_servers_value"],
                next_page_token="next_page_token_value",
            )
        )
        response = await client.fetch_model_servers(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gkerecommender.FetchModelServersRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.FetchModelServersAsyncPager)
    assert response.model_servers == ["model_servers_value"]
    assert response.next_page_token == "next_page_token_value"


def test_fetch_model_servers_pager(transport_name: str = "grpc"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_servers), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        pager = client.fetch_model_servers(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, str) for i in results)


def test_fetch_model_servers_pages(transport_name: str = "grpc"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_servers), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.fetch_model_servers(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_fetch_model_servers_async_pager():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_servers),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.fetch_model_servers(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, str) for i in responses)


@pytest.mark.asyncio
async def test_fetch_model_servers_async_pages():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_servers),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.fetch_model_servers(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchModelServerVersionsRequest(),
        {},
    ],
)
def test_fetch_model_server_versions(request_type, transport: str = "grpc"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_server_versions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gkerecommender.FetchModelServerVersionsResponse(
            model_server_versions=["model_server_versions_value"],
            next_page_token="next_page_token_value",
        )
        response = client.fetch_model_server_versions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gkerecommender.FetchModelServerVersionsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.FetchModelServerVersionsPager)
    assert response.model_server_versions == ["model_server_versions_value"]
    assert response.next_page_token == "next_page_token_value"


def test_fetch_model_server_versions_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gkerecommender.FetchModelServerVersionsRequest(
        model="model_value",
        model_server="model_server_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_server_versions), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.fetch_model_server_versions(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchModelServerVersionsRequest(
            model="model_value",
            model_server="model_server_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_fetch_model_server_versions_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.fetch_model_server_versions
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.fetch_model_server_versions
        ] = mock_rpc
        request = {}
        client.fetch_model_server_versions(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fetch_model_server_versions(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_fetch_model_server_versions_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.fetch_model_server_versions
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.fetch_model_server_versions
        ] = mock_rpc

        request = {}
        await client.fetch_model_server_versions(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.fetch_model_server_versions(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchModelServerVersionsRequest(),
        {},
    ],
)
async def test_fetch_model_server_versions_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_server_versions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=["model_server_versions_value"],
                next_page_token="next_page_token_value",
            )
        )
        response = await client.fetch_model_server_versions(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gkerecommender.FetchModelServerVersionsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.FetchModelServerVersionsAsyncPager)
    assert response.model_server_versions == ["model_server_versions_value"]
    assert response.next_page_token == "next_page_token_value"


def test_fetch_model_server_versions_pager(transport_name: str = "grpc"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_server_versions), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        pager = client.fetch_model_server_versions(
            request={}, retry=retry, timeout=timeout
        )

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, str) for i in results)


def test_fetch_model_server_versions_pages(transport_name: str = "grpc"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_server_versions), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.fetch_model_server_versions(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_fetch_model_server_versions_async_pager():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_server_versions),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.fetch_model_server_versions(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, str) for i in responses)


@pytest.mark.asyncio
async def test_fetch_model_server_versions_async_pages():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_server_versions),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                    str(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.fetch_model_server_versions(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchProfilesRequest(),
        {},
    ],
)
def test_fetch_profiles(request_type, transport: str = "grpc"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_profiles), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = gkerecommender.FetchProfilesResponse(
            comments="comments_value",
            next_page_token="next_page_token_value",
        )
        response = client.fetch_profiles(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gkerecommender.FetchProfilesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.FetchProfilesPager)
    assert response.comments == "comments_value"
    assert response.next_page_token == "next_page_token_value"


def test_fetch_profiles_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gkerecommender.FetchProfilesRequest(
        model="model_value",
        model_server="model_server_value",
        model_server_version="model_server_version_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_profiles), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.fetch_profiles(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchProfilesRequest(
            model="model_value",
            model_server="model_server_value",
            model_server_version="model_server_version_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_fetch_profiles_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.fetch_profiles in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.fetch_profiles] = mock_rpc
        request = {}
        client.fetch_profiles(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fetch_profiles(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_fetch_profiles_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.fetch_profiles
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.fetch_profiles
        ] = mock_rpc

        request = {}
        await client.fetch_profiles(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.fetch_profiles(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchProfilesRequest(),
        {},
    ],
)
async def test_fetch_profiles_async(request_type, transport: str = "grpc_asyncio"):
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_profiles), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gkerecommender.FetchProfilesResponse(
                comments="comments_value",
                next_page_token="next_page_token_value",
            )
        )
        response = await client.fetch_profiles(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gkerecommender.FetchProfilesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.FetchProfilesAsyncPager)
    assert response.comments == "comments_value"
    assert response.next_page_token == "next_page_token_value"


def test_fetch_profiles_pager(transport_name: str = "grpc"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_profiles), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[],
                next_page_token="def",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        pager = client.fetch_profiles(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, gkerecommender.Profile) for i in results)


def test_fetch_profiles_pages(transport_name: str = "grpc"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.fetch_profiles), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[],
                next_page_token="def",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.fetch_profiles(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_fetch_profiles_async_pager():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_profiles), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[],
                next_page_token="def",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.fetch_profiles(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, gkerecommender.Profile) for i in responses)


@pytest.mark.asyncio
async def test_fetch_profiles_async_pages():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_profiles), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[],
                next_page_token="def",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.fetch_profiles(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.GenerateOptimizedManifestRequest(),
        {},
    ],
)
def test_generate_optimized_manifest(request_type, transport: str = "grpc"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_optimized_manifest), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gkerecommender.GenerateOptimizedManifestResponse(
            comments=["comments_value"],
            manifest_version="manifest_version_value",
        )
        response = client.generate_optimized_manifest(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gkerecommender.GenerateOptimizedManifestRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gkerecommender.GenerateOptimizedManifestResponse)
    assert response.comments == ["comments_value"]
    assert response.manifest_version == "manifest_version_value"


def test_generate_optimized_manifest_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gkerecommender.GenerateOptimizedManifestRequest(
        accelerator_type="accelerator_type_value",
        kubernetes_namespace="kubernetes_namespace_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_optimized_manifest), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.generate_optimized_manifest(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.GenerateOptimizedManifestRequest(
            accelerator_type="accelerator_type_value",
            kubernetes_namespace="kubernetes_namespace_value",
        )
        assert args[0] == request_msg


def test_generate_optimized_manifest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.generate_optimized_manifest
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.generate_optimized_manifest
        ] = mock_rpc
        request = {}
        client.generate_optimized_manifest(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.generate_optimized_manifest(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_generate_optimized_manifest_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.generate_optimized_manifest
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.generate_optimized_manifest
        ] = mock_rpc

        request = {}
        await client.generate_optimized_manifest(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.generate_optimized_manifest(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.GenerateOptimizedManifestRequest(),
        {},
    ],
)
async def test_generate_optimized_manifest_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_optimized_manifest), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gkerecommender.GenerateOptimizedManifestResponse(
                comments=["comments_value"],
                manifest_version="manifest_version_value",
            )
        )
        response = await client.generate_optimized_manifest(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gkerecommender.GenerateOptimizedManifestRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gkerecommender.GenerateOptimizedManifestResponse)
    assert response.comments == ["comments_value"]
    assert response.manifest_version == "manifest_version_value"


@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchBenchmarkingDataRequest(),
        {},
    ],
)
def test_fetch_benchmarking_data(request_type, transport: str = "grpc"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_benchmarking_data), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = gkerecommender.FetchBenchmarkingDataResponse()
        response = client.fetch_benchmarking_data(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = gkerecommender.FetchBenchmarkingDataRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gkerecommender.FetchBenchmarkingDataResponse)


def test_fetch_benchmarking_data_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = gkerecommender.FetchBenchmarkingDataRequest(
        instance_type="instance_type_value",
        pricing_model="pricing_model_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_benchmarking_data), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.fetch_benchmarking_data(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchBenchmarkingDataRequest(
            instance_type="instance_type_value",
            pricing_model="pricing_model_value",
        )
        assert args[0] == request_msg


def test_fetch_benchmarking_data_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.fetch_benchmarking_data
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.fetch_benchmarking_data
        ] = mock_rpc
        request = {}
        client.fetch_benchmarking_data(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fetch_benchmarking_data(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_fetch_benchmarking_data_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.fetch_benchmarking_data
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.fetch_benchmarking_data
        ] = mock_rpc

        request = {}
        await client.fetch_benchmarking_data(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.fetch_benchmarking_data(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchBenchmarkingDataRequest(),
        {},
    ],
)
async def test_fetch_benchmarking_data_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_benchmarking_data), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gkerecommender.FetchBenchmarkingDataResponse()
        )
        response = await client.fetch_benchmarking_data(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = gkerecommender.FetchBenchmarkingDataRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, gkerecommender.FetchBenchmarkingDataResponse)


def test_fetch_models_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.fetch_models in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.fetch_models] = mock_rpc

        request = {}
        client.fetch_models(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fetch_models(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_fetch_models_rest_pager(transport: str = "rest"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelsResponse(
                models=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelsResponse(
                models=[
                    str(),
                    str(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            gkerecommender.FetchModelsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {}

        pager = client.fetch_models(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, str) for i in results)

        pages = list(client.fetch_models(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_fetch_model_servers_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.fetch_model_servers in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.fetch_model_servers] = (
            mock_rpc
        )

        request = {}
        client.fetch_model_servers(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fetch_model_servers(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_fetch_model_servers_rest_required_fields(
    request_type=gkerecommender.FetchModelServersRequest,
):
    transport_class = transports.GkeInferenceQuickstartRestTransport

    request_init = {}
    request_init["model"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped
    assert "model" not in jsonified_request

    default_values = getattr(
        transport_class._BaseFetchModelServers,
        "_BaseFetchModelServers__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "model" in jsonified_request
    assert jsonified_request["model"] == request_init["model"]

    jsonified_request["model"] = "model_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "model",
            "pageSize",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "model" in jsonified_request
    assert jsonified_request["model"] == "model_value"

    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gkerecommender.FetchModelServersResponse()
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
            return_value = gkerecommender.FetchModelServersResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.fetch_model_servers(request)

            expected_params = [
                (
                    "model",
                    "",
                ),
                ("$alt", "json;enum-encoding=int"),
            ]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_fetch_model_servers_rest_pager(transport: str = "rest"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelServersResponse(
                model_servers=[
                    str(),
                    str(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            gkerecommender.FetchModelServersResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {}

        pager = client.fetch_model_servers(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, str) for i in results)

        pages = list(client.fetch_model_servers(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_fetch_model_server_versions_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.fetch_model_server_versions
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.fetch_model_server_versions
        ] = mock_rpc

        request = {}
        client.fetch_model_server_versions(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fetch_model_server_versions(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_fetch_model_server_versions_rest_required_fields(
    request_type=gkerecommender.FetchModelServerVersionsRequest,
):
    transport_class = transports.GkeInferenceQuickstartRestTransport

    request_init = {}
    request_init["model"] = ""
    request_init["model_server"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped
    assert "model" not in jsonified_request
    assert "modelServer" not in jsonified_request

    default_values = getattr(
        transport_class._BaseFetchModelServerVersions,
        "_BaseFetchModelServerVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "model" in jsonified_request
    assert jsonified_request["model"] == request_init["model"]
    assert "modelServer" in jsonified_request
    assert jsonified_request["modelServer"] == request_init["model_server"]

    jsonified_request["model"] = "model_value"
    jsonified_request["modelServer"] = "model_server_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "model",
            "modelServer",
            "pageSize",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "model" in jsonified_request
    assert jsonified_request["model"] == "model_value"
    assert "modelServer" in jsonified_request
    assert jsonified_request["modelServer"] == "model_server_value"

    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gkerecommender.FetchModelServerVersionsResponse()
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
            return_value = gkerecommender.FetchModelServerVersionsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.fetch_model_server_versions(request)

            expected_params = [
                (
                    "model",
                    "",
                ),
                (
                    "modelServer",
                    "",
                ),
                ("$alt", "json;enum-encoding=int"),
            ]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_fetch_model_server_versions_rest_pager(transport: str = "rest"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                    str(),
                    str(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[],
                next_page_token="def",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=[
                    str(),
                    str(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            gkerecommender.FetchModelServerVersionsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {}

        pager = client.fetch_model_server_versions(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, str) for i in results)

        pages = list(client.fetch_model_server_versions(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_fetch_profiles_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.fetch_profiles in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.fetch_profiles] = mock_rpc

        request = {}
        client.fetch_profiles(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fetch_profiles(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_fetch_profiles_rest_pager(transport: str = "rest"):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                ],
                next_page_token="abc",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[],
                next_page_token="def",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                ],
                next_page_token="ghi",
            ),
            gkerecommender.FetchProfilesResponse(
                profile=[
                    gkerecommender.Profile(),
                    gkerecommender.Profile(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            gkerecommender.FetchProfilesResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {}

        pager = client.fetch_profiles(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, gkerecommender.Profile) for i in results)

        pages = list(client.fetch_profiles(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_generate_optimized_manifest_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.generate_optimized_manifest
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.generate_optimized_manifest
        ] = mock_rpc

        request = {}
        client.generate_optimized_manifest(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.generate_optimized_manifest(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_generate_optimized_manifest_rest_required_fields(
    request_type=gkerecommender.GenerateOptimizedManifestRequest,
):
    transport_class = transports.GkeInferenceQuickstartRestTransport

    request_init = {}
    request_init["accelerator_type"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGenerateOptimizedManifest,
        "_BaseGenerateOptimizedManifest__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["acceleratorType"] = "accelerator_type_value"

    # verify required fields with non-default values are left alone
    assert "acceleratorType" in jsonified_request
    assert jsonified_request["acceleratorType"] == "accelerator_type_value"

    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gkerecommender.GenerateOptimizedManifestResponse()
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
            return_value = gkerecommender.GenerateOptimizedManifestResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.generate_optimized_manifest(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_fetch_benchmarking_data_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = GkeInferenceQuickstartClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.fetch_benchmarking_data
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.fetch_benchmarking_data
        ] = mock_rpc

        request = {}
        client.fetch_benchmarking_data(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fetch_benchmarking_data(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_fetch_benchmarking_data_rest_required_fields(
    request_type=gkerecommender.FetchBenchmarkingDataRequest,
):
    transport_class = transports.GkeInferenceQuickstartRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseFetchBenchmarkingData,
        "_BaseFetchBenchmarkingData__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    # verify required fields with non-default values are left alone

    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = gkerecommender.FetchBenchmarkingDataResponse()
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
            return_value = gkerecommender.FetchBenchmarkingDataResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.fetch_benchmarking_data(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.GkeInferenceQuickstartGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = GkeInferenceQuickstartClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.GkeInferenceQuickstartGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = GkeInferenceQuickstartClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.GkeInferenceQuickstartGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = GkeInferenceQuickstartClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = GkeInferenceQuickstartClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.GkeInferenceQuickstartGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = GkeInferenceQuickstartClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.GkeInferenceQuickstartGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = GkeInferenceQuickstartClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.GkeInferenceQuickstartGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.GkeInferenceQuickstartGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.GkeInferenceQuickstartGrpcTransport,
        transports.GkeInferenceQuickstartGrpcAsyncIOTransport,
        transports.GkeInferenceQuickstartRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = GkeInferenceQuickstartClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fetch_models_empty_call_grpc():
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.fetch_models), "__call__") as call:
        call.return_value = gkerecommender.FetchModelsResponse()
        client.fetch_models(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchModelsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fetch_model_servers_empty_call_grpc():
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_servers), "__call__"
    ) as call:
        call.return_value = gkerecommender.FetchModelServersResponse()
        client.fetch_model_servers(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchModelServersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fetch_model_server_versions_empty_call_grpc():
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_server_versions), "__call__"
    ) as call:
        call.return_value = gkerecommender.FetchModelServerVersionsResponse()
        client.fetch_model_server_versions(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchModelServerVersionsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fetch_profiles_empty_call_grpc():
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.fetch_profiles), "__call__") as call:
        call.return_value = gkerecommender.FetchProfilesResponse()
        client.fetch_profiles(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchProfilesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_generate_optimized_manifest_empty_call_grpc():
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_optimized_manifest), "__call__"
    ) as call:
        call.return_value = gkerecommender.GenerateOptimizedManifestResponse()
        client.generate_optimized_manifest(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.GenerateOptimizedManifestRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fetch_benchmarking_data_empty_call_grpc():
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_benchmarking_data), "__call__"
    ) as call:
        call.return_value = gkerecommender.FetchBenchmarkingDataResponse()
        client.fetch_benchmarking_data(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchBenchmarkingDataRequest()
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = GkeInferenceQuickstartAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_fetch_models_empty_call_grpc_asyncio():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.fetch_models), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gkerecommender.FetchModelsResponse(
                models=["models_value"],
                next_page_token="next_page_token_value",
            )
        )
        await client.fetch_models(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchModelsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_fetch_model_servers_empty_call_grpc_asyncio():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_servers), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gkerecommender.FetchModelServersResponse(
                model_servers=["model_servers_value"],
                next_page_token="next_page_token_value",
            )
        )
        await client.fetch_model_servers(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchModelServersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_fetch_model_server_versions_empty_call_grpc_asyncio():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_server_versions), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gkerecommender.FetchModelServerVersionsResponse(
                model_server_versions=["model_server_versions_value"],
                next_page_token="next_page_token_value",
            )
        )
        await client.fetch_model_server_versions(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchModelServerVersionsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_fetch_profiles_empty_call_grpc_asyncio():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.fetch_profiles), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gkerecommender.FetchProfilesResponse(
                comments="comments_value",
                next_page_token="next_page_token_value",
            )
        )
        await client.fetch_profiles(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchProfilesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_generate_optimized_manifest_empty_call_grpc_asyncio():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_optimized_manifest), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gkerecommender.GenerateOptimizedManifestResponse(
                comments=["comments_value"],
                manifest_version="manifest_version_value",
            )
        )
        await client.generate_optimized_manifest(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.GenerateOptimizedManifestRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_fetch_benchmarking_data_empty_call_grpc_asyncio():
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_benchmarking_data), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            gkerecommender.FetchBenchmarkingDataResponse()
        )
        await client.fetch_benchmarking_data(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchBenchmarkingDataRequest()
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = GkeInferenceQuickstartClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_fetch_models_rest_bad_request(request_type=gkerecommender.FetchModelsRequest):
    client = GkeInferenceQuickstartClient(
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
        client.fetch_models(request)


@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchModelsRequest,
        dict,
    ],
)
def test_fetch_models_rest_call_success(request_type):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gkerecommender.FetchModelsResponse(
            models=["models_value"],
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gkerecommender.FetchModelsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.fetch_models(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.FetchModelsPager)
    assert response.models == ["models_value"]
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_fetch_models_rest_interceptors(null_interceptor):
    transport = transports.GkeInferenceQuickstartRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.GkeInferenceQuickstartRestInterceptor(),
    )
    client = GkeInferenceQuickstartClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor, "post_fetch_models"
        ) as post,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor,
            "post_fetch_models_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor, "pre_fetch_models"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gkerecommender.FetchModelsRequest.pb(
            gkerecommender.FetchModelsRequest()
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
        return_value = gkerecommender.FetchModelsResponse.to_json(
            gkerecommender.FetchModelsResponse()
        )
        req.return_value.content = return_value

        request = gkerecommender.FetchModelsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gkerecommender.FetchModelsResponse()
        post_with_metadata.return_value = gkerecommender.FetchModelsResponse(), metadata

        client.fetch_models(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_fetch_model_servers_rest_bad_request(
    request_type=gkerecommender.FetchModelServersRequest,
):
    client = GkeInferenceQuickstartClient(
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
        client.fetch_model_servers(request)


@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchModelServersRequest,
        dict,
    ],
)
def test_fetch_model_servers_rest_call_success(request_type):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gkerecommender.FetchModelServersResponse(
            model_servers=["model_servers_value"],
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gkerecommender.FetchModelServersResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.fetch_model_servers(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.FetchModelServersPager)
    assert response.model_servers == ["model_servers_value"]
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_fetch_model_servers_rest_interceptors(null_interceptor):
    transport = transports.GkeInferenceQuickstartRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.GkeInferenceQuickstartRestInterceptor(),
    )
    client = GkeInferenceQuickstartClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor, "post_fetch_model_servers"
        ) as post,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor,
            "post_fetch_model_servers_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor, "pre_fetch_model_servers"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gkerecommender.FetchModelServersRequest.pb(
            gkerecommender.FetchModelServersRequest()
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
        return_value = gkerecommender.FetchModelServersResponse.to_json(
            gkerecommender.FetchModelServersResponse()
        )
        req.return_value.content = return_value

        request = gkerecommender.FetchModelServersRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gkerecommender.FetchModelServersResponse()
        post_with_metadata.return_value = (
            gkerecommender.FetchModelServersResponse(),
            metadata,
        )

        client.fetch_model_servers(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_fetch_model_server_versions_rest_bad_request(
    request_type=gkerecommender.FetchModelServerVersionsRequest,
):
    client = GkeInferenceQuickstartClient(
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
        client.fetch_model_server_versions(request)


@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchModelServerVersionsRequest,
        dict,
    ],
)
def test_fetch_model_server_versions_rest_call_success(request_type):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gkerecommender.FetchModelServerVersionsResponse(
            model_server_versions=["model_server_versions_value"],
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gkerecommender.FetchModelServerVersionsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.fetch_model_server_versions(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.FetchModelServerVersionsPager)
    assert response.model_server_versions == ["model_server_versions_value"]
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_fetch_model_server_versions_rest_interceptors(null_interceptor):
    transport = transports.GkeInferenceQuickstartRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.GkeInferenceQuickstartRestInterceptor(),
    )
    client = GkeInferenceQuickstartClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor,
            "post_fetch_model_server_versions",
        ) as post,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor,
            "post_fetch_model_server_versions_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor,
            "pre_fetch_model_server_versions",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gkerecommender.FetchModelServerVersionsRequest.pb(
            gkerecommender.FetchModelServerVersionsRequest()
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
        return_value = gkerecommender.FetchModelServerVersionsResponse.to_json(
            gkerecommender.FetchModelServerVersionsResponse()
        )
        req.return_value.content = return_value

        request = gkerecommender.FetchModelServerVersionsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gkerecommender.FetchModelServerVersionsResponse()
        post_with_metadata.return_value = (
            gkerecommender.FetchModelServerVersionsResponse(),
            metadata,
        )

        client.fetch_model_server_versions(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_fetch_profiles_rest_bad_request(
    request_type=gkerecommender.FetchProfilesRequest,
):
    client = GkeInferenceQuickstartClient(
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
        client.fetch_profiles(request)


@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchProfilesRequest,
        dict,
    ],
)
def test_fetch_profiles_rest_call_success(request_type):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gkerecommender.FetchProfilesResponse(
            comments="comments_value",
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gkerecommender.FetchProfilesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.fetch_profiles(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.FetchProfilesPager)
    assert response.comments == "comments_value"
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_fetch_profiles_rest_interceptors(null_interceptor):
    transport = transports.GkeInferenceQuickstartRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.GkeInferenceQuickstartRestInterceptor(),
    )
    client = GkeInferenceQuickstartClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor, "post_fetch_profiles"
        ) as post,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor,
            "post_fetch_profiles_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor, "pre_fetch_profiles"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gkerecommender.FetchProfilesRequest.pb(
            gkerecommender.FetchProfilesRequest()
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
        return_value = gkerecommender.FetchProfilesResponse.to_json(
            gkerecommender.FetchProfilesResponse()
        )
        req.return_value.content = return_value

        request = gkerecommender.FetchProfilesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gkerecommender.FetchProfilesResponse()
        post_with_metadata.return_value = (
            gkerecommender.FetchProfilesResponse(),
            metadata,
        )

        client.fetch_profiles(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_generate_optimized_manifest_rest_bad_request(
    request_type=gkerecommender.GenerateOptimizedManifestRequest,
):
    client = GkeInferenceQuickstartClient(
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
        client.generate_optimized_manifest(request)


@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.GenerateOptimizedManifestRequest,
        dict,
    ],
)
def test_generate_optimized_manifest_rest_call_success(request_type):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gkerecommender.GenerateOptimizedManifestResponse(
            comments=["comments_value"],
            manifest_version="manifest_version_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gkerecommender.GenerateOptimizedManifestResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.generate_optimized_manifest(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gkerecommender.GenerateOptimizedManifestResponse)
    assert response.comments == ["comments_value"]
    assert response.manifest_version == "manifest_version_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_generate_optimized_manifest_rest_interceptors(null_interceptor):
    transport = transports.GkeInferenceQuickstartRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.GkeInferenceQuickstartRestInterceptor(),
    )
    client = GkeInferenceQuickstartClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor,
            "post_generate_optimized_manifest",
        ) as post,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor,
            "post_generate_optimized_manifest_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor,
            "pre_generate_optimized_manifest",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gkerecommender.GenerateOptimizedManifestRequest.pb(
            gkerecommender.GenerateOptimizedManifestRequest()
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
        return_value = gkerecommender.GenerateOptimizedManifestResponse.to_json(
            gkerecommender.GenerateOptimizedManifestResponse()
        )
        req.return_value.content = return_value

        request = gkerecommender.GenerateOptimizedManifestRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gkerecommender.GenerateOptimizedManifestResponse()
        post_with_metadata.return_value = (
            gkerecommender.GenerateOptimizedManifestResponse(),
            metadata,
        )

        client.generate_optimized_manifest(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_fetch_benchmarking_data_rest_bad_request(
    request_type=gkerecommender.FetchBenchmarkingDataRequest,
):
    client = GkeInferenceQuickstartClient(
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
        client.fetch_benchmarking_data(request)


@pytest.mark.parametrize(
    "request_type",
    [
        gkerecommender.FetchBenchmarkingDataRequest,
        dict,
    ],
)
def test_fetch_benchmarking_data_rest_call_success(request_type):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = gkerecommender.FetchBenchmarkingDataResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = gkerecommender.FetchBenchmarkingDataResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.fetch_benchmarking_data(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, gkerecommender.FetchBenchmarkingDataResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_fetch_benchmarking_data_rest_interceptors(null_interceptor):
    transport = transports.GkeInferenceQuickstartRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.GkeInferenceQuickstartRestInterceptor(),
    )
    client = GkeInferenceQuickstartClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor,
            "post_fetch_benchmarking_data",
        ) as post,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor,
            "post_fetch_benchmarking_data_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.GkeInferenceQuickstartRestInterceptor,
            "pre_fetch_benchmarking_data",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = gkerecommender.FetchBenchmarkingDataRequest.pb(
            gkerecommender.FetchBenchmarkingDataRequest()
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
        return_value = gkerecommender.FetchBenchmarkingDataResponse.to_json(
            gkerecommender.FetchBenchmarkingDataResponse()
        )
        req.return_value.content = return_value

        request = gkerecommender.FetchBenchmarkingDataRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = gkerecommender.FetchBenchmarkingDataResponse()
        post_with_metadata.return_value = (
            gkerecommender.FetchBenchmarkingDataResponse(),
            metadata,
        )

        client.fetch_benchmarking_data(
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
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fetch_models_empty_call_rest():
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.fetch_models), "__call__") as call:
        client.fetch_models(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchModelsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fetch_model_servers_empty_call_rest():
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_servers), "__call__"
    ) as call:
        client.fetch_model_servers(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchModelServersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fetch_model_server_versions_empty_call_rest():
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_model_server_versions), "__call__"
    ) as call:
        client.fetch_model_server_versions(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchModelServerVersionsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fetch_profiles_empty_call_rest():
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.fetch_profiles), "__call__") as call:
        client.fetch_profiles(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchProfilesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_generate_optimized_manifest_empty_call_rest():
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.generate_optimized_manifest), "__call__"
    ) as call:
        client.generate_optimized_manifest(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.GenerateOptimizedManifestRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fetch_benchmarking_data_empty_call_rest():
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_benchmarking_data), "__call__"
    ) as call:
        client.fetch_benchmarking_data(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = gkerecommender.FetchBenchmarkingDataRequest()
        assert args[0] == request_msg


def test_transport_grpc_default():
    # A client should use the gRPC transport by default.
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.GkeInferenceQuickstartGrpcTransport,
    )


def test_gke_inference_quickstart_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.GkeInferenceQuickstartTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_gke_inference_quickstart_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.gkerecommender_v1.services.gke_inference_quickstart.transports.GkeInferenceQuickstartTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.GkeInferenceQuickstartTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "fetch_models",
        "fetch_model_servers",
        "fetch_model_server_versions",
        "fetch_profiles",
        "generate_optimized_manifest",
        "fetch_benchmarking_data",
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


def test_gke_inference_quickstart_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.cloud.gkerecommender_v1.services.gke_inference_quickstart.transports.GkeInferenceQuickstartTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.GkeInferenceQuickstartTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


def test_gke_inference_quickstart_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.cloud.gkerecommender_v1.services.gke_inference_quickstart.transports.GkeInferenceQuickstartTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.GkeInferenceQuickstartTransport()
        adc.assert_called_once()


def test_gke_inference_quickstart_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        GkeInferenceQuickstartClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.GkeInferenceQuickstartGrpcTransport,
        transports.GkeInferenceQuickstartGrpcAsyncIOTransport,
    ],
)
def test_gke_inference_quickstart_transport_auth_adc(transport_class):
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
        transports.GkeInferenceQuickstartGrpcTransport,
        transports.GkeInferenceQuickstartGrpcAsyncIOTransport,
        transports.GkeInferenceQuickstartRestTransport,
    ],
)
def test_gke_inference_quickstart_transport_auth_gdch_credentials(transport_class):
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
        (transports.GkeInferenceQuickstartGrpcTransport, grpc_helpers),
        (transports.GkeInferenceQuickstartGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_gke_inference_quickstart_transport_create_channel(
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
            "gkerecommender.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=["1", "2"],
            default_host="gkerecommender.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.GkeInferenceQuickstartGrpcTransport,
        transports.GkeInferenceQuickstartGrpcAsyncIOTransport,
    ],
)
def test_gke_inference_quickstart_grpc_transport_client_cert_source_for_mtls(
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


def test_gke_inference_quickstart_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.GkeInferenceQuickstartRestTransport(
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
def test_gke_inference_quickstart_host_no_port(transport_name):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="gkerecommender.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "gkerecommender.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://gkerecommender.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_gke_inference_quickstart_host_with_port(transport_name):
    client = GkeInferenceQuickstartClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="gkerecommender.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "gkerecommender.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://gkerecommender.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_gke_inference_quickstart_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = GkeInferenceQuickstartClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = GkeInferenceQuickstartClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.fetch_models._session
    session2 = client2.transport.fetch_models._session
    assert session1 != session2
    session1 = client1.transport.fetch_model_servers._session
    session2 = client2.transport.fetch_model_servers._session
    assert session1 != session2
    session1 = client1.transport.fetch_model_server_versions._session
    session2 = client2.transport.fetch_model_server_versions._session
    assert session1 != session2
    session1 = client1.transport.fetch_profiles._session
    session2 = client2.transport.fetch_profiles._session
    assert session1 != session2
    session1 = client1.transport.generate_optimized_manifest._session
    session2 = client2.transport.generate_optimized_manifest._session
    assert session1 != session2
    session1 = client1.transport.fetch_benchmarking_data._session
    session2 = client2.transport.fetch_benchmarking_data._session
    assert session1 != session2


def test_gke_inference_quickstart_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.GkeInferenceQuickstartGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_gke_inference_quickstart_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.GkeInferenceQuickstartGrpcAsyncIOTransport(
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
        transports.GkeInferenceQuickstartGrpcTransport,
        transports.GkeInferenceQuickstartGrpcAsyncIOTransport,
    ],
)
def test_gke_inference_quickstart_transport_channel_mtls_with_client_cert_source(
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
        transports.GkeInferenceQuickstartGrpcTransport,
        transports.GkeInferenceQuickstartGrpcAsyncIOTransport,
    ],
)
def test_gke_inference_quickstart_transport_channel_mtls_with_adc(transport_class):
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


def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = GkeInferenceQuickstartClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = GkeInferenceQuickstartClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = GkeInferenceQuickstartClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = GkeInferenceQuickstartClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = GkeInferenceQuickstartClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = GkeInferenceQuickstartClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = GkeInferenceQuickstartClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = GkeInferenceQuickstartClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = GkeInferenceQuickstartClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = GkeInferenceQuickstartClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = GkeInferenceQuickstartClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = GkeInferenceQuickstartClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = GkeInferenceQuickstartClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = GkeInferenceQuickstartClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = GkeInferenceQuickstartClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.GkeInferenceQuickstartTransport, "_prep_wrapped_messages"
    ) as prep:
        client = GkeInferenceQuickstartClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.GkeInferenceQuickstartTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = GkeInferenceQuickstartClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_grpc():
    client = GkeInferenceQuickstartClient(
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
    client = GkeInferenceQuickstartAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = GkeInferenceQuickstartClient(
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
        client = GkeInferenceQuickstartClient(
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
        (GkeInferenceQuickstartClient, transports.GkeInferenceQuickstartGrpcTransport),
        (
            GkeInferenceQuickstartAsyncClient,
            transports.GkeInferenceQuickstartGrpcAsyncIOTransport,
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
