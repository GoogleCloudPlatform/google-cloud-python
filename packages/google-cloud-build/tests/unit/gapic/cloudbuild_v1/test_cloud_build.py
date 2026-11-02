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
import google.api_core.operation_async as operation_async  # type: ignore
import google.auth
import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
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

from google.cloud.devtools.cloudbuild_v1.services.cloud_build import (
    CloudBuildAsyncClient,
    CloudBuildClient,
    pagers,
    transports,
)
from google.cloud.devtools.cloudbuild_v1.types import cloudbuild

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

    assert CloudBuildClient._get_client_cert_source(None, False) is None
    assert (
        CloudBuildClient._get_client_cert_source(mock_provided_cert_source, False)
        is None
    )
    assert (
        CloudBuildClient._get_client_cert_source(mock_provided_cert_source, True)
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
                CloudBuildClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                CloudBuildClient._get_client_cert_source(
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
    client = CloudBuildClient(credentials=cred)
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
    client = CloudBuildClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (CloudBuildClient, "grpc"),
        (CloudBuildAsyncClient, "grpc_asyncio"),
        (CloudBuildClient, "rest"),
    ],
)
def test_cloud_build_client_from_service_account_info(client_class, transport_name):
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
            "cloudbuild.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://cloudbuild.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.CloudBuildGrpcTransport, "grpc"),
        (transports.CloudBuildGrpcAsyncIOTransport, "grpc_asyncio"),
        (transports.CloudBuildRestTransport, "rest"),
    ],
)
def test_cloud_build_client_service_account_always_use_jwt(
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
        (CloudBuildClient, "grpc"),
        (CloudBuildAsyncClient, "grpc_asyncio"),
        (CloudBuildClient, "rest"),
    ],
)
def test_cloud_build_client_from_service_account_file(client_class, transport_name):
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
            "cloudbuild.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://cloudbuild.googleapis.com"
        )


def test_cloud_build_client_get_transport_class():
    transport = CloudBuildClient.get_transport_class()
    available_transports = [
        transports.CloudBuildGrpcTransport,
        transports.CloudBuildRestTransport,
    ]
    assert transport in available_transports

    transport = CloudBuildClient.get_transport_class("grpc")
    assert transport == transports.CloudBuildGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (CloudBuildClient, transports.CloudBuildGrpcTransport, "grpc"),
        (
            CloudBuildAsyncClient,
            transports.CloudBuildGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (CloudBuildClient, transports.CloudBuildRestTransport, "rest"),
    ],
)
@mock.patch.object(
    CloudBuildClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(CloudBuildClient),
)
@mock.patch.object(
    CloudBuildAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(CloudBuildAsyncClient),
)
def test_cloud_build_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(CloudBuildClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(CloudBuildClient, "get_transport_class") as gtc:
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
        (CloudBuildClient, transports.CloudBuildGrpcTransport, "grpc", "true"),
        (
            CloudBuildAsyncClient,
            transports.CloudBuildGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (CloudBuildClient, transports.CloudBuildGrpcTransport, "grpc", "false"),
        (
            CloudBuildAsyncClient,
            transports.CloudBuildGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (CloudBuildClient, transports.CloudBuildRestTransport, "rest", "true"),
        (CloudBuildClient, transports.CloudBuildRestTransport, "rest", "false"),
    ],
)
@mock.patch.object(
    CloudBuildClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(CloudBuildClient),
)
@mock.patch.object(
    CloudBuildAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(CloudBuildAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_cloud_build_client_mtls_env_auto(
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


@pytest.mark.parametrize("client_class", [CloudBuildClient, CloudBuildAsyncClient])
@mock.patch.object(
    CloudBuildClient, "DEFAULT_ENDPOINT", modify_default_endpoint(CloudBuildClient)
)
@mock.patch.object(
    CloudBuildAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(CloudBuildAsyncClient),
)
def test_cloud_build_client_get_mtls_endpoint_and_cert_source(client_class):
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


@pytest.mark.parametrize("client_class", [CloudBuildClient, CloudBuildAsyncClient])
@mock.patch.object(
    CloudBuildClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(CloudBuildClient),
)
@mock.patch.object(
    CloudBuildAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(CloudBuildAsyncClient),
)
def test_cloud_build_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = CloudBuildClient._DEFAULT_UNIVERSE
    default_endpoint = CloudBuildClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = CloudBuildClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
        (CloudBuildClient, transports.CloudBuildGrpcTransport, "grpc"),
        (
            CloudBuildAsyncClient,
            transports.CloudBuildGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (CloudBuildClient, transports.CloudBuildRestTransport, "rest"),
    ],
)
def test_cloud_build_client_client_options_scopes(
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
        (CloudBuildClient, transports.CloudBuildGrpcTransport, "grpc", grpc_helpers),
        (
            CloudBuildAsyncClient,
            transports.CloudBuildGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (CloudBuildClient, transports.CloudBuildRestTransport, "rest", None),
    ],
)
def test_cloud_build_client_client_options_credentials_file(
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


def test_cloud_build_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.devtools.cloudbuild_v1.services.cloud_build.transports.CloudBuildGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = CloudBuildClient(client_options={"api_endpoint": "squid.clam.whelk"})
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
        (CloudBuildClient, transports.CloudBuildGrpcTransport, "grpc", grpc_helpers),
        (
            CloudBuildAsyncClient,
            transports.CloudBuildGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_cloud_build_client_create_channel_credentials_file(
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
            "cloudbuild.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=None,
            default_host="cloudbuild.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.CreateBuildRequest(),
        {},
    ],
)
def test_create_build(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.create_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.CreateBuildRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_build_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.CreateBuildRequest(
        parent="parent_value",
        project_id="project_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_build), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_build(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CreateBuildRequest(
            parent="parent_value",
            project_id="project_id_value",
        )
        assert args[0] == request_msg


def test_create_build_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_build in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_build] = mock_rpc
        request = {}
        client.create_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.create_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_build_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_build
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_build
        ] = mock_rpc

        request = {}
        await client.create_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.create_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.CreateBuildRequest(),
        {},
    ],
)
async def test_create_build_async(request_type, transport: str = "grpc_asyncio"):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.create_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.CreateBuildRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_build_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_build(
            project_id="project_id_value",
            build=cloudbuild.Build(name="name_value"),
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].build
        mock_val = cloudbuild.Build(name="name_value")
        assert arg == mock_val
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_create_build_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_build(
            cloudbuild.CreateBuildRequest(),
            project_id="project_id_value",
            build=cloudbuild.Build(name="name_value"),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_create_build_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.create_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_build(
            project_id="project_id_value",
            build=cloudbuild.Build(name="name_value"),
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].build
        mock_val = cloudbuild.Build(name="name_value")
        assert arg == mock_val
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_build_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_build(
            cloudbuild.CreateBuildRequest(),
            project_id="project_id_value",
            build=cloudbuild.Build(name="name_value"),
            parent="parent_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.GetBuildRequest(),
        {},
    ],
)
def test_get_build(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.Build(
            name="name_value",
            id="id_value",
            project_id="project_id_value",
            status=cloudbuild.Build.Status.PENDING,
            status_detail="status_detail_value",
            images=["images_value"],
            logs_bucket="logs_bucket_value",
            build_trigger_id="build_trigger_id_value",
            log_url="log_url_value",
            tags=["tags_value"],
            service_account="service_account_value",
        )
        response = client.get_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.GetBuildRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.Build)
    assert response.name == "name_value"
    assert response.id == "id_value"
    assert response.project_id == "project_id_value"
    assert response.status == cloudbuild.Build.Status.PENDING
    assert response.status_detail == "status_detail_value"
    assert response.images == ["images_value"]
    assert response.logs_bucket == "logs_bucket_value"
    assert response.build_trigger_id == "build_trigger_id_value"
    assert response.log_url == "log_url_value"
    assert response.tags == ["tags_value"]
    assert response.service_account == "service_account_value"


def test_get_build_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.GetBuildRequest(
        name="name_value",
        project_id="project_id_value",
        id="id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_build), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_build(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetBuildRequest(
            name="name_value",
            project_id="project_id_value",
            id="id_value",
        )
        assert args[0] == request_msg


def test_get_build_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_build in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_build] = mock_rpc
        request = {}
        client.get_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_build_async_use_cached_wrapped_rpc(transport: str = "grpc_asyncio"):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_build
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_build
        ] = mock_rpc

        request = {}
        await client.get_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.GetBuildRequest(),
        {},
    ],
)
async def test_get_build_async(request_type, transport: str = "grpc_asyncio"):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.Build(
                name="name_value",
                id="id_value",
                project_id="project_id_value",
                status=cloudbuild.Build.Status.PENDING,
                status_detail="status_detail_value",
                images=["images_value"],
                logs_bucket="logs_bucket_value",
                build_trigger_id="build_trigger_id_value",
                log_url="log_url_value",
                tags=["tags_value"],
                service_account="service_account_value",
            )
        )
        response = await client.get_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.GetBuildRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.Build)
    assert response.name == "name_value"
    assert response.id == "id_value"
    assert response.project_id == "project_id_value"
    assert response.status == cloudbuild.Build.Status.PENDING
    assert response.status_detail == "status_detail_value"
    assert response.images == ["images_value"]
    assert response.logs_bucket == "logs_bucket_value"
    assert response.build_trigger_id == "build_trigger_id_value"
    assert response.log_url == "log_url_value"
    assert response.tags == ["tags_value"]
    assert response.service_account == "service_account_value"


def test_get_build_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.Build()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_build(
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].id
        mock_val = "id_value"
        assert arg == mock_val
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_build_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_build(
            cloudbuild.GetBuildRequest(),
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_build_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.Build()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(cloudbuild.Build())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_build(
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].id
        mock_val = "id_value"
        assert arg == mock_val
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_build_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_build(
            cloudbuild.GetBuildRequest(),
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ListBuildsRequest(),
        {},
    ],
)
def test_list_builds(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_builds), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.ListBuildsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_builds(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.ListBuildsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListBuildsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_builds_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.ListBuildsRequest(
        parent="parent_value",
        project_id="project_id_value",
        page_token="page_token_value",
        filter="filter_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_builds), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_builds(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ListBuildsRequest(
            parent="parent_value",
            project_id="project_id_value",
            page_token="page_token_value",
            filter="filter_value",
        )
        assert args[0] == request_msg


def test_list_builds_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_builds in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_builds] = mock_rpc
        request = {}
        client.list_builds(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_builds(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_builds_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_builds
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_builds
        ] = mock_rpc

        request = {}
        await client.list_builds(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_builds(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ListBuildsRequest(),
        {},
    ],
)
async def test_list_builds_async(request_type, transport: str = "grpc_asyncio"):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_builds), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ListBuildsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_builds(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.ListBuildsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListBuildsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_builds_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_builds), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.ListBuildsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_builds(
            project_id="project_id_value",
            filter="filter_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].filter
        mock_val = "filter_value"
        assert arg == mock_val


def test_list_builds_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_builds(
            cloudbuild.ListBuildsRequest(),
            project_id="project_id_value",
            filter="filter_value",
        )


@pytest.mark.asyncio
async def test_list_builds_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_builds), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.ListBuildsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ListBuildsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_builds(
            project_id="project_id_value",
            filter="filter_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].filter
        mock_val = "filter_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_builds_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_builds(
            cloudbuild.ListBuildsRequest(),
            project_id="project_id_value",
            filter="filter_value",
        )


def test_list_builds_pager(transport_name: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_builds), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[],
                next_page_token="def",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        pager = client.list_builds(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, cloudbuild.Build) for i in results)


def test_list_builds_pages(transport_name: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.list_builds), "__call__") as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[],
                next_page_token="def",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_builds(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_builds_async_pager():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_builds), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[],
                next_page_token="def",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_builds(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, cloudbuild.Build) for i in responses)


@pytest.mark.asyncio
async def test_list_builds_async_pages():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_builds), "__call__", new_callable=mock.AsyncMock
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[],
                next_page_token="def",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_builds(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.CancelBuildRequest(),
        {},
    ],
)
def test_cancel_build(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.Build(
            name="name_value",
            id="id_value",
            project_id="project_id_value",
            status=cloudbuild.Build.Status.PENDING,
            status_detail="status_detail_value",
            images=["images_value"],
            logs_bucket="logs_bucket_value",
            build_trigger_id="build_trigger_id_value",
            log_url="log_url_value",
            tags=["tags_value"],
            service_account="service_account_value",
        )
        response = client.cancel_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.CancelBuildRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.Build)
    assert response.name == "name_value"
    assert response.id == "id_value"
    assert response.project_id == "project_id_value"
    assert response.status == cloudbuild.Build.Status.PENDING
    assert response.status_detail == "status_detail_value"
    assert response.images == ["images_value"]
    assert response.logs_bucket == "logs_bucket_value"
    assert response.build_trigger_id == "build_trigger_id_value"
    assert response.log_url == "log_url_value"
    assert response.tags == ["tags_value"]
    assert response.service_account == "service_account_value"


def test_cancel_build_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.CancelBuildRequest(
        name="name_value",
        project_id="project_id_value",
        id="id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_build), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.cancel_build(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CancelBuildRequest(
            name="name_value",
            project_id="project_id_value",
            id="id_value",
        )
        assert args[0] == request_msg


def test_cancel_build_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.cancel_build in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.cancel_build] = mock_rpc
        request = {}
        client.cancel_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.cancel_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_cancel_build_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.cancel_build
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.cancel_build
        ] = mock_rpc

        request = {}
        await client.cancel_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.cancel_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.CancelBuildRequest(),
        {},
    ],
)
async def test_cancel_build_async(request_type, transport: str = "grpc_asyncio"):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.Build(
                name="name_value",
                id="id_value",
                project_id="project_id_value",
                status=cloudbuild.Build.Status.PENDING,
                status_detail="status_detail_value",
                images=["images_value"],
                logs_bucket="logs_bucket_value",
                build_trigger_id="build_trigger_id_value",
                log_url="log_url_value",
                tags=["tags_value"],
                service_account="service_account_value",
            )
        )
        response = await client.cancel_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.CancelBuildRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.Build)
    assert response.name == "name_value"
    assert response.id == "id_value"
    assert response.project_id == "project_id_value"
    assert response.status == cloudbuild.Build.Status.PENDING
    assert response.status_detail == "status_detail_value"
    assert response.images == ["images_value"]
    assert response.logs_bucket == "logs_bucket_value"
    assert response.build_trigger_id == "build_trigger_id_value"
    assert response.log_url == "log_url_value"
    assert response.tags == ["tags_value"]
    assert response.service_account == "service_account_value"


def test_cancel_build_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.Build()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.cancel_build(
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].id
        mock_val = "id_value"
        assert arg == mock_val
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_cancel_build_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.cancel_build(
            cloudbuild.CancelBuildRequest(),
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )


@pytest.mark.asyncio
async def test_cancel_build_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.cancel_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.Build()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(cloudbuild.Build())
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.cancel_build(
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].id
        mock_val = "id_value"
        assert arg == mock_val
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_cancel_build_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.cancel_build(
            cloudbuild.CancelBuildRequest(),
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.RetryBuildRequest(),
        {},
    ],
)
def test_retry_build(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.retry_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.retry_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.RetryBuildRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_retry_build_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.RetryBuildRequest(
        name="name_value",
        project_id="project_id_value",
        id="id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.retry_build), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.retry_build(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.RetryBuildRequest(
            name="name_value",
            project_id="project_id_value",
            id="id_value",
        )
        assert args[0] == request_msg


def test_retry_build_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.retry_build in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.retry_build] = mock_rpc
        request = {}
        client.retry_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.retry_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_retry_build_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.retry_build
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.retry_build
        ] = mock_rpc

        request = {}
        await client.retry_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.retry_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.RetryBuildRequest(),
        {},
    ],
)
async def test_retry_build_async(request_type, transport: str = "grpc_asyncio"):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.retry_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.retry_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.RetryBuildRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_retry_build_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.retry_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.retry_build(
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].id
        mock_val = "id_value"
        assert arg == mock_val
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_retry_build_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.retry_build(
            cloudbuild.RetryBuildRequest(),
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )


@pytest.mark.asyncio
async def test_retry_build_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.retry_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.retry_build(
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].id
        mock_val = "id_value"
        assert arg == mock_val
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_retry_build_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.retry_build(
            cloudbuild.RetryBuildRequest(),
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ApproveBuildRequest(),
        {},
    ],
)
def test_approve_build(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.approve_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.approve_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.ApproveBuildRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_approve_build_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.ApproveBuildRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.approve_build), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.approve_build(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ApproveBuildRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_approve_build_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.approve_build in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.approve_build] = mock_rpc
        request = {}
        client.approve_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.approve_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_approve_build_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.approve_build
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.approve_build
        ] = mock_rpc

        request = {}
        await client.approve_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.approve_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ApproveBuildRequest(),
        {},
    ],
)
async def test_approve_build_async(request_type, transport: str = "grpc_asyncio"):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.approve_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.approve_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.ApproveBuildRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_approve_build_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.approve_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.approve_build(
            name="name_value",
            approval_result=cloudbuild.ApprovalResult(
                approver_account="approver_account_value"
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].approval_result
        mock_val = cloudbuild.ApprovalResult(approver_account="approver_account_value")
        assert arg == mock_val


def test_approve_build_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.approve_build(
            cloudbuild.ApproveBuildRequest(),
            name="name_value",
            approval_result=cloudbuild.ApprovalResult(
                approver_account="approver_account_value"
            ),
        )


@pytest.mark.asyncio
async def test_approve_build_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.approve_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.approve_build(
            name="name_value",
            approval_result=cloudbuild.ApprovalResult(
                approver_account="approver_account_value"
            ),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val
        arg = args[0].approval_result
        mock_val = cloudbuild.ApprovalResult(approver_account="approver_account_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_approve_build_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.approve_build(
            cloudbuild.ApproveBuildRequest(),
            name="name_value",
            approval_result=cloudbuild.ApprovalResult(
                approver_account="approver_account_value"
            ),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.CreateBuildTriggerRequest(),
        {},
    ],
)
def test_create_build_trigger(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.BuildTrigger(
            resource_name="resource_name_value",
            id="id_value",
            description="description_value",
            name="name_value",
            tags=["tags_value"],
            disabled=True,
            ignored_files=["ignored_files_value"],
            included_files=["included_files_value"],
            filter="filter_value",
            service_account="service_account_value",
            autodetect=True,
        )
        response = client.create_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.CreateBuildTriggerRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.BuildTrigger)
    assert response.resource_name == "resource_name_value"
    assert response.id == "id_value"
    assert response.description == "description_value"
    assert response.name == "name_value"
    assert response.tags == ["tags_value"]
    assert response.disabled is True
    assert response.ignored_files == ["ignored_files_value"]
    assert response.included_files == ["included_files_value"]
    assert response.filter == "filter_value"
    assert response.service_account == "service_account_value"


def test_create_build_trigger_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.CreateBuildTriggerRequest(
        parent="parent_value",
        project_id="project_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_build_trigger), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_build_trigger(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CreateBuildTriggerRequest(
            parent="parent_value",
            project_id="project_id_value",
        )
        assert args[0] == request_msg


def test_create_build_trigger_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_build_trigger in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_build_trigger] = (
            mock_rpc
        )
        request = {}
        client.create_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_build_trigger_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_build_trigger
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_build_trigger
        ] = mock_rpc

        request = {}
        await client.create_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.create_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.CreateBuildTriggerRequest(),
        {},
    ],
)
async def test_create_build_trigger_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.BuildTrigger(
                resource_name="resource_name_value",
                id="id_value",
                description="description_value",
                name="name_value",
                tags=["tags_value"],
                disabled=True,
                ignored_files=["ignored_files_value"],
                included_files=["included_files_value"],
                filter="filter_value",
                service_account="service_account_value",
            )
        )
        response = await client.create_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.CreateBuildTriggerRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.BuildTrigger)
    assert response.resource_name == "resource_name_value"
    assert response.id == "id_value"
    assert response.description == "description_value"
    assert response.name == "name_value"
    assert response.tags == ["tags_value"]
    assert response.disabled is True
    assert response.ignored_files == ["ignored_files_value"]
    assert response.included_files == ["included_files_value"]
    assert response.filter == "filter_value"
    assert response.service_account == "service_account_value"


def test_create_build_trigger_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.BuildTrigger()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_build_trigger(
            project_id="project_id_value",
            trigger=cloudbuild.BuildTrigger(resource_name="resource_name_value"),
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].trigger
        mock_val = cloudbuild.BuildTrigger(resource_name="resource_name_value")
        assert arg == mock_val
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_create_build_trigger_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_build_trigger(
            cloudbuild.CreateBuildTriggerRequest(),
            project_id="project_id_value",
            trigger=cloudbuild.BuildTrigger(resource_name="resource_name_value"),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_create_build_trigger_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.BuildTrigger()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.BuildTrigger()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_build_trigger(
            project_id="project_id_value",
            trigger=cloudbuild.BuildTrigger(resource_name="resource_name_value"),
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].trigger
        mock_val = cloudbuild.BuildTrigger(resource_name="resource_name_value")
        assert arg == mock_val
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_build_trigger_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_build_trigger(
            cloudbuild.CreateBuildTriggerRequest(),
            project_id="project_id_value",
            trigger=cloudbuild.BuildTrigger(resource_name="resource_name_value"),
            parent="parent_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.GetBuildTriggerRequest(),
        {},
    ],
)
def test_get_build_trigger(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.BuildTrigger(
            resource_name="resource_name_value",
            id="id_value",
            description="description_value",
            name="name_value",
            tags=["tags_value"],
            disabled=True,
            ignored_files=["ignored_files_value"],
            included_files=["included_files_value"],
            filter="filter_value",
            service_account="service_account_value",
            autodetect=True,
        )
        response = client.get_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.GetBuildTriggerRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.BuildTrigger)
    assert response.resource_name == "resource_name_value"
    assert response.id == "id_value"
    assert response.description == "description_value"
    assert response.name == "name_value"
    assert response.tags == ["tags_value"]
    assert response.disabled is True
    assert response.ignored_files == ["ignored_files_value"]
    assert response.included_files == ["included_files_value"]
    assert response.filter == "filter_value"
    assert response.service_account == "service_account_value"


def test_get_build_trigger_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.GetBuildTriggerRequest(
        name="name_value",
        project_id="project_id_value",
        trigger_id="trigger_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_build_trigger), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_build_trigger(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetBuildTriggerRequest(
            name="name_value",
            project_id="project_id_value",
            trigger_id="trigger_id_value",
        )
        assert args[0] == request_msg


def test_get_build_trigger_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_build_trigger in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_build_trigger] = (
            mock_rpc
        )
        request = {}
        client.get_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_build_trigger_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_build_trigger
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_build_trigger
        ] = mock_rpc

        request = {}
        await client.get_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.GetBuildTriggerRequest(),
        {},
    ],
)
async def test_get_build_trigger_async(request_type, transport: str = "grpc_asyncio"):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.BuildTrigger(
                resource_name="resource_name_value",
                id="id_value",
                description="description_value",
                name="name_value",
                tags=["tags_value"],
                disabled=True,
                ignored_files=["ignored_files_value"],
                included_files=["included_files_value"],
                filter="filter_value",
                service_account="service_account_value",
            )
        )
        response = await client.get_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.GetBuildTriggerRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.BuildTrigger)
    assert response.resource_name == "resource_name_value"
    assert response.id == "id_value"
    assert response.description == "description_value"
    assert response.name == "name_value"
    assert response.tags == ["tags_value"]
    assert response.disabled is True
    assert response.ignored_files == ["ignored_files_value"]
    assert response.included_files == ["included_files_value"]
    assert response.filter == "filter_value"
    assert response.service_account == "service_account_value"


def test_get_build_trigger_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.BuildTrigger()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_build_trigger(
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].trigger_id
        mock_val = "trigger_id_value"
        assert arg == mock_val
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_build_trigger_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_build_trigger(
            cloudbuild.GetBuildTriggerRequest(),
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_build_trigger_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.BuildTrigger()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.BuildTrigger()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_build_trigger(
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].trigger_id
        mock_val = "trigger_id_value"
        assert arg == mock_val
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_get_build_trigger_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_build_trigger(
            cloudbuild.GetBuildTriggerRequest(),
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ListBuildTriggersRequest(),
        {},
    ],
)
def test_list_build_triggers(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.ListBuildTriggersResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_build_triggers(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.ListBuildTriggersRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListBuildTriggersPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_build_triggers_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.ListBuildTriggersRequest(
        parent="parent_value",
        project_id="project_id_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_build_triggers(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ListBuildTriggersRequest(
            parent="parent_value",
            project_id="project_id_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_build_triggers_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_build_triggers in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_build_triggers] = (
            mock_rpc
        )
        request = {}
        client.list_build_triggers(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_build_triggers(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_build_triggers_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_build_triggers
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_build_triggers
        ] = mock_rpc

        request = {}
        await client.list_build_triggers(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_build_triggers(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ListBuildTriggersRequest(),
        {},
    ],
)
async def test_list_build_triggers_async(request_type, transport: str = "grpc_asyncio"):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ListBuildTriggersResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_build_triggers(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.ListBuildTriggersRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListBuildTriggersAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_build_triggers_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.ListBuildTriggersResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_build_triggers(
            project_id="project_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val


def test_list_build_triggers_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_build_triggers(
            cloudbuild.ListBuildTriggersRequest(),
            project_id="project_id_value",
        )


@pytest.mark.asyncio
async def test_list_build_triggers_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.ListBuildTriggersResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ListBuildTriggersResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_build_triggers(
            project_id="project_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_list_build_triggers_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_build_triggers(
            cloudbuild.ListBuildTriggersRequest(),
            project_id="project_id_value",
        )


def test_list_build_triggers_pager(transport_name: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[],
                next_page_token="def",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        pager = client.list_build_triggers(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, cloudbuild.BuildTrigger) for i in results)


def test_list_build_triggers_pages(transport_name: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[],
                next_page_token="def",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_build_triggers(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_build_triggers_async_pager():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[],
                next_page_token="def",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_build_triggers(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, cloudbuild.BuildTrigger) for i in responses)


@pytest.mark.asyncio
async def test_list_build_triggers_async_pages():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[],
                next_page_token="def",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_build_triggers(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.DeleteBuildTriggerRequest(),
        {},
    ],
)
def test_delete_build_trigger(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        response = client.delete_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.DeleteBuildTriggerRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_build_trigger_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.DeleteBuildTriggerRequest(
        name="name_value",
        project_id="project_id_value",
        trigger_id="trigger_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_build_trigger), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.delete_build_trigger(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.DeleteBuildTriggerRequest(
            name="name_value",
            project_id="project_id_value",
            trigger_id="trigger_id_value",
        )
        assert args[0] == request_msg


def test_delete_build_trigger_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_build_trigger in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_build_trigger] = (
            mock_rpc
        )
        request = {}
        client.delete_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_delete_build_trigger_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.delete_build_trigger
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.delete_build_trigger
        ] = mock_rpc

        request = {}
        await client.delete_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.delete_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.DeleteBuildTriggerRequest(),
        {},
    ],
)
async def test_delete_build_trigger_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        response = await client.delete_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.DeleteBuildTriggerRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert response is None


def test_delete_build_trigger_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_build_trigger(
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].trigger_id
        mock_val = "trigger_id_value"
        assert arg == mock_val
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_build_trigger_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_build_trigger(
            cloudbuild.DeleteBuildTriggerRequest(),
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_build_trigger_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = None

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_build_trigger(
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].trigger_id
        mock_val = "trigger_id_value"
        assert arg == mock_val
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_delete_build_trigger_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_build_trigger(
            cloudbuild.DeleteBuildTriggerRequest(),
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.UpdateBuildTriggerRequest(),
        {},
    ],
)
def test_update_build_trigger(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.BuildTrigger(
            resource_name="resource_name_value",
            id="id_value",
            description="description_value",
            name="name_value",
            tags=["tags_value"],
            disabled=True,
            ignored_files=["ignored_files_value"],
            included_files=["included_files_value"],
            filter="filter_value",
            service_account="service_account_value",
            autodetect=True,
        )
        response = client.update_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.UpdateBuildTriggerRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.BuildTrigger)
    assert response.resource_name == "resource_name_value"
    assert response.id == "id_value"
    assert response.description == "description_value"
    assert response.name == "name_value"
    assert response.tags == ["tags_value"]
    assert response.disabled is True
    assert response.ignored_files == ["ignored_files_value"]
    assert response.included_files == ["included_files_value"]
    assert response.filter == "filter_value"
    assert response.service_account == "service_account_value"


def test_update_build_trigger_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.UpdateBuildTriggerRequest(
        project_id="project_id_value",
        trigger_id="trigger_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_build_trigger), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_build_trigger(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.UpdateBuildTriggerRequest(
            project_id="project_id_value",
            trigger_id="trigger_id_value",
        )
        assert args[0] == request_msg


def test_update_build_trigger_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_build_trigger in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_build_trigger] = (
            mock_rpc
        )
        request = {}
        client.update_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_build_trigger_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_build_trigger
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_build_trigger
        ] = mock_rpc

        request = {}
        await client.update_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.update_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.UpdateBuildTriggerRequest(),
        {},
    ],
)
async def test_update_build_trigger_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.BuildTrigger(
                resource_name="resource_name_value",
                id="id_value",
                description="description_value",
                name="name_value",
                tags=["tags_value"],
                disabled=True,
                ignored_files=["ignored_files_value"],
                included_files=["included_files_value"],
                filter="filter_value",
                service_account="service_account_value",
            )
        )
        response = await client.update_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.UpdateBuildTriggerRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.BuildTrigger)
    assert response.resource_name == "resource_name_value"
    assert response.id == "id_value"
    assert response.description == "description_value"
    assert response.name == "name_value"
    assert response.tags == ["tags_value"]
    assert response.disabled is True
    assert response.ignored_files == ["ignored_files_value"]
    assert response.included_files == ["included_files_value"]
    assert response.filter == "filter_value"
    assert response.service_account == "service_account_value"


def test_update_build_trigger_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.BuildTrigger()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_build_trigger(
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            trigger=cloudbuild.BuildTrigger(resource_name="resource_name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].trigger_id
        mock_val = "trigger_id_value"
        assert arg == mock_val
        arg = args[0].trigger
        mock_val = cloudbuild.BuildTrigger(resource_name="resource_name_value")
        assert arg == mock_val


def test_update_build_trigger_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_build_trigger(
            cloudbuild.UpdateBuildTriggerRequest(),
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            trigger=cloudbuild.BuildTrigger(resource_name="resource_name_value"),
        )


@pytest.mark.asyncio
async def test_update_build_trigger_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.BuildTrigger()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.BuildTrigger()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_build_trigger(
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            trigger=cloudbuild.BuildTrigger(resource_name="resource_name_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].trigger_id
        mock_val = "trigger_id_value"
        assert arg == mock_val
        arg = args[0].trigger
        mock_val = cloudbuild.BuildTrigger(resource_name="resource_name_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_build_trigger_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_build_trigger(
            cloudbuild.UpdateBuildTriggerRequest(),
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            trigger=cloudbuild.BuildTrigger(resource_name="resource_name_value"),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.RunBuildTriggerRequest(),
        {},
    ],
)
def test_run_build_trigger(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.run_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.run_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.RunBuildTriggerRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_run_build_trigger_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.RunBuildTriggerRequest(
        name="name_value",
        project_id="project_id_value",
        trigger_id="trigger_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.run_build_trigger), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.run_build_trigger(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.RunBuildTriggerRequest(
            name="name_value",
            project_id="project_id_value",
            trigger_id="trigger_id_value",
        )
        assert args[0] == request_msg


def test_run_build_trigger_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.run_build_trigger in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.run_build_trigger] = (
            mock_rpc
        )
        request = {}
        client.run_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.run_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_run_build_trigger_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.run_build_trigger
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.run_build_trigger
        ] = mock_rpc

        request = {}
        await client.run_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.run_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.RunBuildTriggerRequest(),
        {},
    ],
)
async def test_run_build_trigger_async(request_type, transport: str = "grpc_asyncio"):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.run_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.run_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.RunBuildTriggerRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_run_build_trigger_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.run_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.run_build_trigger(
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            source=cloudbuild.RepoSource(project_id="project_id_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].trigger_id
        mock_val = "trigger_id_value"
        assert arg == mock_val
        arg = args[0].source
        mock_val = cloudbuild.RepoSource(project_id="project_id_value")
        assert arg == mock_val


def test_run_build_trigger_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.run_build_trigger(
            cloudbuild.RunBuildTriggerRequest(),
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            source=cloudbuild.RepoSource(project_id="project_id_value"),
        )


@pytest.mark.asyncio
async def test_run_build_trigger_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.run_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.run_build_trigger(
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            source=cloudbuild.RepoSource(project_id="project_id_value"),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].project_id
        mock_val = "project_id_value"
        assert arg == mock_val
        arg = args[0].trigger_id
        mock_val = "trigger_id_value"
        assert arg == mock_val
        arg = args[0].source
        mock_val = cloudbuild.RepoSource(project_id="project_id_value")
        assert arg == mock_val


@pytest.mark.asyncio
async def test_run_build_trigger_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.run_build_trigger(
            cloudbuild.RunBuildTriggerRequest(),
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            source=cloudbuild.RepoSource(project_id="project_id_value"),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ReceiveTriggerWebhookRequest(),
        {},
    ],
)
def test_receive_trigger_webhook(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.receive_trigger_webhook), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.ReceiveTriggerWebhookResponse()
        response = client.receive_trigger_webhook(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.ReceiveTriggerWebhookRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.ReceiveTriggerWebhookResponse)


def test_receive_trigger_webhook_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.ReceiveTriggerWebhookRequest(
        name="name_value",
        project_id="project_id_value",
        trigger="trigger_value",
        secret="secret_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.receive_trigger_webhook), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.receive_trigger_webhook(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ReceiveTriggerWebhookRequest(
            name="name_value",
            project_id="project_id_value",
            trigger="trigger_value",
            secret="secret_value",
        )
        assert args[0] == request_msg


def test_receive_trigger_webhook_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.receive_trigger_webhook
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.receive_trigger_webhook
        ] = mock_rpc
        request = {}
        client.receive_trigger_webhook(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.receive_trigger_webhook(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_receive_trigger_webhook_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.receive_trigger_webhook
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.receive_trigger_webhook
        ] = mock_rpc

        request = {}
        await client.receive_trigger_webhook(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.receive_trigger_webhook(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ReceiveTriggerWebhookRequest(),
        {},
    ],
)
async def test_receive_trigger_webhook_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.receive_trigger_webhook), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ReceiveTriggerWebhookResponse()
        )
        response = await client.receive_trigger_webhook(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.ReceiveTriggerWebhookRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.ReceiveTriggerWebhookResponse)


def test_receive_trigger_webhook_field_headers():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloudbuild.ReceiveTriggerWebhookRequest()

    request.project_id = "project_id_value"
    request.trigger = "trigger_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.receive_trigger_webhook), "__call__"
    ) as call:
        call.return_value = cloudbuild.ReceiveTriggerWebhookResponse()
        client.receive_trigger_webhook(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project_id=project_id_value&trigger=trigger_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_receive_trigger_webhook_field_headers_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = cloudbuild.ReceiveTriggerWebhookRequest()

    request.project_id = "project_id_value"
    request.trigger = "trigger_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.receive_trigger_webhook), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ReceiveTriggerWebhookResponse()
        )
        await client.receive_trigger_webhook(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "project_id=project_id_value&trigger=trigger_value",
    ) in kw["metadata"]


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.CreateWorkerPoolRequest(),
        {},
    ],
)
def test_create_worker_pool(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.create_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.CreateWorkerPoolRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_worker_pool_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.CreateWorkerPoolRequest(
        parent="parent_value",
        worker_pool_id="worker_pool_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_worker_pool), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_worker_pool(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CreateWorkerPoolRequest(
            parent="parent_value",
            worker_pool_id="worker_pool_id_value",
        )
        assert args[0] == request_msg


def test_create_worker_pool_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_worker_pool in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_worker_pool] = (
            mock_rpc
        )
        request = {}
        client.create_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.create_worker_pool(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_worker_pool_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_worker_pool
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_worker_pool
        ] = mock_rpc

        request = {}
        await client.create_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.create_worker_pool(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.CreateWorkerPoolRequest(),
        {},
    ],
)
async def test_create_worker_pool_async(request_type, transport: str = "grpc_asyncio"):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.create_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.CreateWorkerPoolRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_worker_pool_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_worker_pool(
            parent="parent_value",
            worker_pool=cloudbuild.WorkerPool(name="name_value"),
            worker_pool_id="worker_pool_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].worker_pool
        mock_val = cloudbuild.WorkerPool(name="name_value")
        assert arg == mock_val
        arg = args[0].worker_pool_id
        mock_val = "worker_pool_id_value"
        assert arg == mock_val


def test_create_worker_pool_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_worker_pool(
            cloudbuild.CreateWorkerPoolRequest(),
            parent="parent_value",
            worker_pool=cloudbuild.WorkerPool(name="name_value"),
            worker_pool_id="worker_pool_id_value",
        )


@pytest.mark.asyncio
async def test_create_worker_pool_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_worker_pool(
            parent="parent_value",
            worker_pool=cloudbuild.WorkerPool(name="name_value"),
            worker_pool_id="worker_pool_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].worker_pool
        mock_val = cloudbuild.WorkerPool(name="name_value")
        assert arg == mock_val
        arg = args[0].worker_pool_id
        mock_val = "worker_pool_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_worker_pool_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_worker_pool(
            cloudbuild.CreateWorkerPoolRequest(),
            parent="parent_value",
            worker_pool=cloudbuild.WorkerPool(name="name_value"),
            worker_pool_id="worker_pool_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.GetWorkerPoolRequest(),
        {},
    ],
)
def test_get_worker_pool(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_worker_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.WorkerPool(
            name="name_value",
            display_name="display_name_value",
            uid="uid_value",
            state=cloudbuild.WorkerPool.State.CREATING,
            etag="etag_value",
        )
        response = client.get_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.GetWorkerPoolRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.WorkerPool)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.uid == "uid_value"
    assert response.state == cloudbuild.WorkerPool.State.CREATING
    assert response.etag == "etag_value"


def test_get_worker_pool_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.GetWorkerPoolRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_worker_pool), "__call__") as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_worker_pool(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetWorkerPoolRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_worker_pool_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_worker_pool in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_worker_pool] = mock_rpc
        request = {}
        client.get_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_worker_pool(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_worker_pool_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_worker_pool
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_worker_pool
        ] = mock_rpc

        request = {}
        await client.get_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_worker_pool(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.GetWorkerPoolRequest(),
        {},
    ],
)
async def test_get_worker_pool_async(request_type, transport: str = "grpc_asyncio"):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_worker_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.WorkerPool(
                name="name_value",
                display_name="display_name_value",
                uid="uid_value",
                state=cloudbuild.WorkerPool.State.CREATING,
                etag="etag_value",
            )
        )
        response = await client.get_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.GetWorkerPoolRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.WorkerPool)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.uid == "uid_value"
    assert response.state == cloudbuild.WorkerPool.State.CREATING
    assert response.etag == "etag_value"


def test_get_worker_pool_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_worker_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.WorkerPool()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_worker_pool(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_worker_pool_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_worker_pool(
            cloudbuild.GetWorkerPoolRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_worker_pool_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(type(client.transport.get_worker_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.WorkerPool()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.WorkerPool()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_worker_pool(
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
async def test_get_worker_pool_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_worker_pool(
            cloudbuild.GetWorkerPoolRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.DeleteWorkerPoolRequest(),
        {},
    ],
)
def test_delete_worker_pool(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.delete_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.DeleteWorkerPoolRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_worker_pool_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.DeleteWorkerPoolRequest(
        name="name_value",
        etag="etag_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_worker_pool), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.delete_worker_pool(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.DeleteWorkerPoolRequest(
            name="name_value",
            etag="etag_value",
        )
        assert args[0] == request_msg


def test_delete_worker_pool_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_worker_pool in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_worker_pool] = (
            mock_rpc
        )
        request = {}
        client.delete_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.delete_worker_pool(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_delete_worker_pool_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.delete_worker_pool
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.delete_worker_pool
        ] = mock_rpc

        request = {}
        await client.delete_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.delete_worker_pool(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.DeleteWorkerPoolRequest(),
        {},
    ],
)
async def test_delete_worker_pool_async(request_type, transport: str = "grpc_asyncio"):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.delete_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.DeleteWorkerPoolRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_worker_pool_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_worker_pool(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_worker_pool_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_worker_pool(
            cloudbuild.DeleteWorkerPoolRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_worker_pool_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_worker_pool(
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
async def test_delete_worker_pool_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_worker_pool(
            cloudbuild.DeleteWorkerPoolRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.UpdateWorkerPoolRequest(),
        {},
    ],
)
def test_update_worker_pool(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.update_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.UpdateWorkerPoolRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_worker_pool_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.UpdateWorkerPoolRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_worker_pool), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_worker_pool(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.UpdateWorkerPoolRequest()
        assert args[0] == request_msg


def test_update_worker_pool_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_worker_pool in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_worker_pool] = (
            mock_rpc
        )
        request = {}
        client.update_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.update_worker_pool(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_worker_pool_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_worker_pool
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_worker_pool
        ] = mock_rpc

        request = {}
        await client.update_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.update_worker_pool(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.UpdateWorkerPoolRequest(),
        {},
    ],
)
async def test_update_worker_pool_async(request_type, transport: str = "grpc_asyncio"):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.update_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.UpdateWorkerPoolRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_worker_pool_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_worker_pool(
            worker_pool=cloudbuild.WorkerPool(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].worker_pool
        mock_val = cloudbuild.WorkerPool(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_worker_pool_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_worker_pool(
            cloudbuild.UpdateWorkerPoolRequest(),
            worker_pool=cloudbuild.WorkerPool(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_worker_pool_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_worker_pool(
            worker_pool=cloudbuild.WorkerPool(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].worker_pool
        mock_val = cloudbuild.WorkerPool(name="name_value")
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_worker_pool_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_worker_pool(
            cloudbuild.UpdateWorkerPoolRequest(),
            worker_pool=cloudbuild.WorkerPool(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ListWorkerPoolsRequest(),
        {},
    ],
)
def test_list_worker_pools(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.ListWorkerPoolsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_worker_pools(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.ListWorkerPoolsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListWorkerPoolsPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_worker_pools_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.ListWorkerPoolsRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_worker_pools(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ListWorkerPoolsRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_worker_pools_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_worker_pools in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_worker_pools] = (
            mock_rpc
        )
        request = {}
        client.list_worker_pools(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_worker_pools(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_worker_pools_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_worker_pools
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_worker_pools
        ] = mock_rpc

        request = {}
        await client.list_worker_pools(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_worker_pools(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ListWorkerPoolsRequest(),
        {},
    ],
)
async def test_list_worker_pools_async(request_type, transport: str = "grpc_asyncio"):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ListWorkerPoolsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_worker_pools(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.ListWorkerPoolsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListWorkerPoolsAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_worker_pools_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.ListWorkerPoolsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_worker_pools(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_worker_pools_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_worker_pools(
            cloudbuild.ListWorkerPoolsRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_worker_pools_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.ListWorkerPoolsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ListWorkerPoolsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_worker_pools(
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
async def test_list_worker_pools_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_worker_pools(
            cloudbuild.ListWorkerPoolsRequest(),
            parent="parent_value",
        )


def test_list_worker_pools_pager(transport_name: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[],
                next_page_token="def",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        pager = client.list_worker_pools(request={}, retry=retry, timeout=timeout)

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, cloudbuild.WorkerPool) for i in results)


def test_list_worker_pools_pages(transport_name: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[],
                next_page_token="def",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_worker_pools(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_worker_pools_async_pager():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[],
                next_page_token="def",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_worker_pools(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(isinstance(i, cloudbuild.WorkerPool) for i in responses)


@pytest.mark.asyncio
async def test_list_worker_pools_async_pages():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[],
                next_page_token="def",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (await client.list_worker_pools(request={})).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.GetDefaultServiceAccountRequest(),
        {},
    ],
)
def test_get_default_service_account(request_type, transport: str = "grpc"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_default_service_account), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.DefaultServiceAccount(
            name="name_value",
            service_account_email="service_account_email_value",
        )
        response = client.get_default_service_account(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.GetDefaultServiceAccountRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.DefaultServiceAccount)
    assert response.name == "name_value"
    assert response.service_account_email == "service_account_email_value"


def test_get_default_service_account_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = cloudbuild.GetDefaultServiceAccountRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_default_service_account), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_default_service_account(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetDefaultServiceAccountRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_default_service_account_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_default_service_account
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_default_service_account
        ] = mock_rpc
        request = {}
        client.get_default_service_account(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_default_service_account(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_default_service_account_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = CloudBuildAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_default_service_account
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_default_service_account
        ] = mock_rpc

        request = {}
        await client.get_default_service_account(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_default_service_account(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.GetDefaultServiceAccountRequest(),
        {},
    ],
)
async def test_get_default_service_account_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_default_service_account), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.DefaultServiceAccount(
                name="name_value",
                service_account_email="service_account_email_value",
            )
        )
        response = await client.get_default_service_account(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = cloudbuild.GetDefaultServiceAccountRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.DefaultServiceAccount)
    assert response.name == "name_value"
    assert response.service_account_email == "service_account_email_value"


def test_get_default_service_account_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_default_service_account), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.DefaultServiceAccount()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_default_service_account(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_default_service_account_flattened_error():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_default_service_account(
            cloudbuild.GetDefaultServiceAccountRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_default_service_account_flattened_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_default_service_account), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = cloudbuild.DefaultServiceAccount()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.DefaultServiceAccount()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_default_service_account(
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
async def test_get_default_service_account_flattened_error_async():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_default_service_account(
            cloudbuild.GetDefaultServiceAccountRequest(),
            name="name_value",
        )


def test_create_build_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_build in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_build] = mock_rpc

        request = {}
        client.create_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.create_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_build_rest_required_fields(request_type=cloudbuild.CreateBuildRequest):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["project_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateBuild,
        "_BaseCreateBuild__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["projectId"] = "project_id_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("parent",))

    # verify required fields with non-default values are left alone
    assert "projectId" in jsonified_request
    assert jsonified_request["projectId"] == "project_id_value"

    client = CloudBuildClient(
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

            response = client.create_build(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_build_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {"project_id": "sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            project_id="project_id_value",
            build=cloudbuild.Build(name="name_value"),
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

        client.create_build(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/projects/{project_id}/builds" % client.transport._host, args[1]
        )


def test_create_build_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_build(
            cloudbuild.CreateBuildRequest(),
            project_id="project_id_value",
            build=cloudbuild.Build(name="name_value"),
            parent="parent_value",
        )


def test_get_build_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_build in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_build] = mock_rpc

        request = {}
        client.get_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_build_rest_required_fields(request_type=cloudbuild.GetBuildRequest):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["project_id"] = ""
    request_init["id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetBuild,
        "_BaseGetBuild__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["projectId"] = "project_id_value"
    jsonified_request["id"] = "id_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("name",))

    # verify required fields with non-default values are left alone
    assert "projectId" in jsonified_request
    assert jsonified_request["projectId"] == "project_id_value"
    assert "id" in jsonified_request
    assert jsonified_request["id"] == "id_value"

    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloudbuild.Build()
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
            return_value = cloudbuild.Build.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_build(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_build_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.Build()

        # get arguments that satisfy an http rule for this method
        sample_request = {"project_id": "sample1", "id": "sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = cloudbuild.Build.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_build(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/projects/{project_id}/builds/{id}" % client.transport._host, args[1]
        )


def test_get_build_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_build(
            cloudbuild.GetBuildRequest(),
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )


def test_list_builds_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_builds in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_builds] = mock_rpc

        request = {}
        client.list_builds(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_builds(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_builds_rest_required_fields(request_type=cloudbuild.ListBuildsRequest):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["project_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListBuilds,
        "_BaseListBuilds__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["projectId"] = "project_id_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "pageSize",
            "pageToken",
            "parent",
        )
    )

    # verify required fields with non-default values are left alone
    assert "projectId" in jsonified_request
    assert jsonified_request["projectId"] == "project_id_value"

    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloudbuild.ListBuildsResponse()
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
            return_value = cloudbuild.ListBuildsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_builds(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_builds_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.ListBuildsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"project_id": "sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            project_id="project_id_value",
            filter="filter_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = cloudbuild.ListBuildsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_builds(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/projects/{project_id}/builds" % client.transport._host, args[1]
        )


def test_list_builds_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_builds(
            cloudbuild.ListBuildsRequest(),
            project_id="project_id_value",
            filter="filter_value",
        )


def test_list_builds_rest_pager(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[],
                next_page_token="def",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListBuildsResponse(
                builds=[
                    cloudbuild.Build(),
                    cloudbuild.Build(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(cloudbuild.ListBuildsResponse.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"project_id": "sample1"}

        pager = client.list_builds(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, cloudbuild.Build) for i in results)

        pages = list(client.list_builds(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_cancel_build_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.cancel_build in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.cancel_build] = mock_rpc

        request = {}
        client.cancel_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.cancel_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_cancel_build_rest_required_fields(request_type=cloudbuild.CancelBuildRequest):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["project_id"] = ""
    request_init["id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCancelBuild,
        "_BaseCancelBuild__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["projectId"] = "project_id_value"
    jsonified_request["id"] = "id_value"

    # verify required fields with non-default values are left alone
    assert "projectId" in jsonified_request
    assert jsonified_request["projectId"] == "project_id_value"
    assert "id" in jsonified_request
    assert jsonified_request["id"] == "id_value"

    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloudbuild.Build()
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
            return_value = cloudbuild.Build.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.cancel_build(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_cancel_build_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.Build()

        # get arguments that satisfy an http rule for this method
        sample_request = {"project_id": "sample1", "id": "sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = cloudbuild.Build.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.cancel_build(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/projects/{project_id}/builds/{id}:cancel" % client.transport._host,
            args[1],
        )


def test_cancel_build_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.cancel_build(
            cloudbuild.CancelBuildRequest(),
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )


def test_retry_build_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.retry_build in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.retry_build] = mock_rpc

        request = {}
        client.retry_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.retry_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_retry_build_rest_required_fields(request_type=cloudbuild.RetryBuildRequest):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["project_id"] = ""
    request_init["id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseRetryBuild,
        "_BaseRetryBuild__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["projectId"] = "project_id_value"
    jsonified_request["id"] = "id_value"

    # verify required fields with non-default values are left alone
    assert "projectId" in jsonified_request
    assert jsonified_request["projectId"] == "project_id_value"
    assert "id" in jsonified_request
    assert jsonified_request["id"] == "id_value"

    client = CloudBuildClient(
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

            response = client.retry_build(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_retry_build_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {"project_id": "sample1", "id": "sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.retry_build(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/projects/{project_id}/builds/{id}:retry" % client.transport._host,
            args[1],
        )


def test_retry_build_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.retry_build(
            cloudbuild.RetryBuildRequest(),
            project_id="project_id_value",
            id="id_value",
            name="name_value",
        )


def test_approve_build_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.approve_build in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.approve_build] = mock_rpc

        request = {}
        client.approve_build(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.approve_build(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_approve_build_rest_required_fields(
    request_type=cloudbuild.ApproveBuildRequest,
):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseApproveBuild,
        "_BaseApproveBuild__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = CloudBuildClient(
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

            response = client.approve_build(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_approve_build_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "projects/sample1/builds/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
            approval_result=cloudbuild.ApprovalResult(
                approver_account="approver_account_value"
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

        client.approve_build(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/builds/*}:approve" % client.transport._host, args[1]
        )


def test_approve_build_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.approve_build(
            cloudbuild.ApproveBuildRequest(),
            name="name_value",
            approval_result=cloudbuild.ApprovalResult(
                approver_account="approver_account_value"
            ),
        )


def test_create_build_trigger_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_build_trigger in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_build_trigger] = (
            mock_rpc
        )

        request = {}
        client.create_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_build_trigger_rest_required_fields(
    request_type=cloudbuild.CreateBuildTriggerRequest,
):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["project_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateBuildTrigger,
        "_BaseCreateBuildTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["projectId"] = "project_id_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("parent",))

    # verify required fields with non-default values are left alone
    assert "projectId" in jsonified_request
    assert jsonified_request["projectId"] == "project_id_value"

    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloudbuild.BuildTrigger()
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
            return_value = cloudbuild.BuildTrigger.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_build_trigger(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_build_trigger_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.BuildTrigger()

        # get arguments that satisfy an http rule for this method
        sample_request = {"project_id": "sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            project_id="project_id_value",
            trigger=cloudbuild.BuildTrigger(resource_name="resource_name_value"),
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = cloudbuild.BuildTrigger.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_build_trigger(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/projects/{project_id}/triggers" % client.transport._host, args[1]
        )


def test_create_build_trigger_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_build_trigger(
            cloudbuild.CreateBuildTriggerRequest(),
            project_id="project_id_value",
            trigger=cloudbuild.BuildTrigger(resource_name="resource_name_value"),
            parent="parent_value",
        )


def test_get_build_trigger_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_build_trigger in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_build_trigger] = (
            mock_rpc
        )

        request = {}
        client.get_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_build_trigger_rest_required_fields(
    request_type=cloudbuild.GetBuildTriggerRequest,
):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["project_id"] = ""
    request_init["trigger_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetBuildTrigger,
        "_BaseGetBuildTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["projectId"] = "project_id_value"
    jsonified_request["triggerId"] = "trigger_id_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("name",))

    # verify required fields with non-default values are left alone
    assert "projectId" in jsonified_request
    assert jsonified_request["projectId"] == "project_id_value"
    assert "triggerId" in jsonified_request
    assert jsonified_request["triggerId"] == "trigger_id_value"

    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloudbuild.BuildTrigger()
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
            return_value = cloudbuild.BuildTrigger.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_build_trigger(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_build_trigger_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.BuildTrigger()

        # get arguments that satisfy an http rule for this method
        sample_request = {"project_id": "sample1", "trigger_id": "sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = cloudbuild.BuildTrigger.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_build_trigger(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/projects/{project_id}/triggers/{trigger_id}"
            % client.transport._host,
            args[1],
        )


def test_get_build_trigger_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_build_trigger(
            cloudbuild.GetBuildTriggerRequest(),
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            name="name_value",
        )


def test_list_build_triggers_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_build_triggers in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_build_triggers] = (
            mock_rpc
        )

        request = {}
        client.list_build_triggers(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_build_triggers(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_build_triggers_rest_required_fields(
    request_type=cloudbuild.ListBuildTriggersRequest,
):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["project_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListBuildTriggers,
        "_BaseListBuildTriggers__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["projectId"] = "project_id_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "pageSize",
            "pageToken",
            "parent",
        )
    )

    # verify required fields with non-default values are left alone
    assert "projectId" in jsonified_request
    assert jsonified_request["projectId"] == "project_id_value"

    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloudbuild.ListBuildTriggersResponse()
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
            return_value = cloudbuild.ListBuildTriggersResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_build_triggers(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_build_triggers_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.ListBuildTriggersResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"project_id": "sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            project_id="project_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = cloudbuild.ListBuildTriggersResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_build_triggers(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/projects/{project_id}/triggers" % client.transport._host, args[1]
        )


def test_list_build_triggers_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_build_triggers(
            cloudbuild.ListBuildTriggersRequest(),
            project_id="project_id_value",
        )


def test_list_build_triggers_rest_pager(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[],
                next_page_token="def",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListBuildTriggersResponse(
                triggers=[
                    cloudbuild.BuildTrigger(),
                    cloudbuild.BuildTrigger(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            cloudbuild.ListBuildTriggersResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"project_id": "sample1"}

        pager = client.list_build_triggers(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, cloudbuild.BuildTrigger) for i in results)

        pages = list(client.list_build_triggers(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_delete_build_trigger_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_build_trigger in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_build_trigger] = (
            mock_rpc
        )

        request = {}
        client.delete_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.delete_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_build_trigger_rest_required_fields(
    request_type=cloudbuild.DeleteBuildTriggerRequest,
):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["project_id"] = ""
    request_init["trigger_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeleteBuildTrigger,
        "_BaseDeleteBuildTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["projectId"] = "project_id_value"
    jsonified_request["triggerId"] = "trigger_id_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("name",))

    # verify required fields with non-default values are left alone
    assert "projectId" in jsonified_request
    assert jsonified_request["projectId"] == "project_id_value"
    assert "triggerId" in jsonified_request
    assert jsonified_request["triggerId"] == "trigger_id_value"

    client = CloudBuildClient(
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

            response = client.delete_build_trigger(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_build_trigger_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # get arguments that satisfy an http rule for this method
        sample_request = {"project_id": "sample1", "trigger_id": "sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            project_id="project_id_value",
            trigger_id="trigger_id_value",
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

        client.delete_build_trigger(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/projects/{project_id}/triggers/{trigger_id}"
            % client.transport._host,
            args[1],
        )


def test_delete_build_trigger_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_build_trigger(
            cloudbuild.DeleteBuildTriggerRequest(),
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            name="name_value",
        )


def test_update_build_trigger_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_build_trigger in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_build_trigger] = (
            mock_rpc
        )

        request = {}
        client.update_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_build_trigger_rest_required_fields(
    request_type=cloudbuild.UpdateBuildTriggerRequest,
):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["project_id"] = ""
    request_init["trigger_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateBuildTrigger,
        "_BaseUpdateBuildTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["projectId"] = "project_id_value"
    jsonified_request["triggerId"] = "trigger_id_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("updateMask",))

    # verify required fields with non-default values are left alone
    assert "projectId" in jsonified_request
    assert jsonified_request["projectId"] == "project_id_value"
    assert "triggerId" in jsonified_request
    assert jsonified_request["triggerId"] == "trigger_id_value"

    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloudbuild.BuildTrigger()
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
            return_value = cloudbuild.BuildTrigger.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_build_trigger(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_build_trigger_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.BuildTrigger()

        # get arguments that satisfy an http rule for this method
        sample_request = {"project_id": "sample1", "trigger_id": "sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            trigger=cloudbuild.BuildTrigger(resource_name="resource_name_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = cloudbuild.BuildTrigger.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_build_trigger(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/projects/{project_id}/triggers/{trigger_id}"
            % client.transport._host,
            args[1],
        )


def test_update_build_trigger_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_build_trigger(
            cloudbuild.UpdateBuildTriggerRequest(),
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            trigger=cloudbuild.BuildTrigger(resource_name="resource_name_value"),
        )


def test_run_build_trigger_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.run_build_trigger in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.run_build_trigger] = (
            mock_rpc
        )

        request = {}
        client.run_build_trigger(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.run_build_trigger(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_run_build_trigger_rest_required_fields(
    request_type=cloudbuild.RunBuildTriggerRequest,
):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["project_id"] = ""
    request_init["trigger_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseRunBuildTrigger,
        "_BaseRunBuildTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["projectId"] = "project_id_value"
    jsonified_request["triggerId"] = "trigger_id_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("name",))

    # verify required fields with non-default values are left alone
    assert "projectId" in jsonified_request
    assert jsonified_request["projectId"] == "project_id_value"
    assert "triggerId" in jsonified_request
    assert jsonified_request["triggerId"] == "trigger_id_value"

    client = CloudBuildClient(
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

            response = client.run_build_trigger(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_run_build_trigger_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {"project_id": "sample1", "trigger_id": "sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            source=cloudbuild.RepoSource(project_id="project_id_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.run_build_trigger(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/projects/{project_id}/triggers/{trigger_id}:run"
            % client.transport._host,
            args[1],
        )


def test_run_build_trigger_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.run_build_trigger(
            cloudbuild.RunBuildTriggerRequest(),
            project_id="project_id_value",
            trigger_id="trigger_id_value",
            source=cloudbuild.RepoSource(project_id="project_id_value"),
        )


def test_receive_trigger_webhook_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.receive_trigger_webhook
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.receive_trigger_webhook
        ] = mock_rpc

        request = {}
        client.receive_trigger_webhook(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.receive_trigger_webhook(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_worker_pool_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_worker_pool in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_worker_pool] = (
            mock_rpc
        )

        request = {}
        client.create_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.create_worker_pool(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_worker_pool_rest_required_fields(
    request_type=cloudbuild.CreateWorkerPoolRequest,
):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["worker_pool_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped
    assert "workerPoolId" not in jsonified_request

    default_values = getattr(
        transport_class._BaseCreateWorkerPool,
        "_BaseCreateWorkerPool__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "workerPoolId" in jsonified_request
    assert jsonified_request["workerPoolId"] == request_init["worker_pool_id"]

    jsonified_request["parent"] = "parent_value"
    jsonified_request["workerPoolId"] = "worker_pool_id_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "validateOnly",
            "workerPoolId",
        )
    )

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "workerPoolId" in jsonified_request
    assert jsonified_request["workerPoolId"] == "worker_pool_id_value"

    client = CloudBuildClient(
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

            response = client.create_worker_pool(request)

            expected_params = [
                (
                    "workerPoolId",
                    "",
                ),
                ("$alt", "json;enum-encoding=int"),
            ]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_worker_pool_rest_flattened():
    client = CloudBuildClient(
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
            worker_pool=cloudbuild.WorkerPool(name="name_value"),
            worker_pool_id="worker_pool_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_worker_pool(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*}/workerPools"
            % client.transport._host,
            args[1],
        )


def test_create_worker_pool_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_worker_pool(
            cloudbuild.CreateWorkerPoolRequest(),
            parent="parent_value",
            worker_pool=cloudbuild.WorkerPool(name="name_value"),
            worker_pool_id="worker_pool_id_value",
        )


def test_get_worker_pool_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_worker_pool in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_worker_pool] = mock_rpc

        request = {}
        client.get_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_worker_pool(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_worker_pool_rest_required_fields(
    request_type=cloudbuild.GetWorkerPoolRequest,
):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetWorkerPool,
        "_BaseGetWorkerPool__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloudbuild.WorkerPool()
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
            return_value = cloudbuild.WorkerPool.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_worker_pool(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_worker_pool_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.WorkerPool()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/workerPools/sample3"
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
        return_value = cloudbuild.WorkerPool.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_worker_pool(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/workerPools/*}"
            % client.transport._host,
            args[1],
        )


def test_get_worker_pool_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_worker_pool(
            cloudbuild.GetWorkerPoolRequest(),
            name="name_value",
        )


def test_delete_worker_pool_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_worker_pool in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_worker_pool] = (
            mock_rpc
        )

        request = {}
        client.delete_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.delete_worker_pool(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_worker_pool_rest_required_fields(
    request_type=cloudbuild.DeleteWorkerPoolRequest,
):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeleteWorkerPool,
        "_BaseDeleteWorkerPool__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "allowMissing",
            "etag",
            "validateOnly",
        )
    )

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = CloudBuildClient(
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
                "method": "delete",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.delete_worker_pool(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_worker_pool_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/workerPools/sample3"
        }

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.delete_worker_pool(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/workerPools/*}"
            % client.transport._host,
            args[1],
        )


def test_delete_worker_pool_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_worker_pool(
            cloudbuild.DeleteWorkerPoolRequest(),
            name="name_value",
        )


def test_update_worker_pool_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_worker_pool in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_worker_pool] = (
            mock_rpc
        )

        request = {}
        client.update_worker_pool(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.update_worker_pool(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_worker_pool_rest_required_fields(
    request_type=cloudbuild.UpdateWorkerPoolRequest,
):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateWorkerPool,
        "_BaseUpdateWorkerPool__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "updateMask",
            "validateOnly",
        )
    )

    # verify required fields with non-default values are left alone

    client = CloudBuildClient(
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

            response = client.update_worker_pool(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_worker_pool_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "worker_pool": {
                "name": "projects/sample1/locations/sample2/workerPools/sample3"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            worker_pool=cloudbuild.WorkerPool(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_worker_pool(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{worker_pool.name=projects/*/locations/*/workerPools/*}"
            % client.transport._host,
            args[1],
        )


def test_update_worker_pool_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_worker_pool(
            cloudbuild.UpdateWorkerPoolRequest(),
            worker_pool=cloudbuild.WorkerPool(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_list_worker_pools_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_worker_pools in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_worker_pools] = (
            mock_rpc
        )

        request = {}
        client.list_worker_pools(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_worker_pools(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_worker_pools_rest_required_fields(
    request_type=cloudbuild.ListWorkerPoolsRequest,
):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListWorkerPools,
        "_BaseListWorkerPools__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloudbuild.ListWorkerPoolsResponse()
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
            return_value = cloudbuild.ListWorkerPoolsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_worker_pools(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_worker_pools_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.ListWorkerPoolsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "projects/sample1/locations/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = cloudbuild.ListWorkerPoolsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_worker_pools(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=projects/*/locations/*}/workerPools"
            % client.transport._host,
            args[1],
        )


def test_list_worker_pools_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_worker_pools(
            cloudbuild.ListWorkerPoolsRequest(),
            parent="parent_value",
        )


def test_list_worker_pools_rest_pager(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                ],
                next_page_token="abc",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[],
                next_page_token="def",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                ],
                next_page_token="ghi",
            ),
            cloudbuild.ListWorkerPoolsResponse(
                worker_pools=[
                    cloudbuild.WorkerPool(),
                    cloudbuild.WorkerPool(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            cloudbuild.ListWorkerPoolsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "projects/sample1/locations/sample2"}

        pager = client.list_worker_pools(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, cloudbuild.WorkerPool) for i in results)

        pages = list(client.list_worker_pools(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_get_default_service_account_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_default_service_account
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_default_service_account
        ] = mock_rpc

        request = {}
        client.get_default_service_account(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_default_service_account(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_default_service_account_rest_required_fields(
    request_type=cloudbuild.GetDefaultServiceAccountRequest,
):
    transport_class = transports.CloudBuildRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetDefaultServiceAccount,
        "_BaseGetDefaultServiceAccount__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = cloudbuild.DefaultServiceAccount()
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
            return_value = cloudbuild.DefaultServiceAccount.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_default_service_account(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_default_service_account_rest_flattened():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.DefaultServiceAccount()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "projects/sample1/locations/sample2/defaultServiceAccount"
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
        return_value = cloudbuild.DefaultServiceAccount.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_default_service_account(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=projects/*/locations/*/defaultServiceAccount}"
            % client.transport._host,
            args[1],
        )


def test_get_default_service_account_rest_flattened_error(transport: str = "rest"):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_default_service_account(
            cloudbuild.GetDefaultServiceAccountRequest(),
            name="name_value",
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.CloudBuildGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.CloudBuildGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = CloudBuildClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.CloudBuildGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = CloudBuildClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = CloudBuildClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.CloudBuildGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = CloudBuildClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.CloudBuildGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = CloudBuildClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.CloudBuildGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.CloudBuildGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.CloudBuildGrpcTransport,
        transports.CloudBuildGrpcAsyncIOTransport,
        transports.CloudBuildRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = CloudBuildClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_build_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_build), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CreateBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_build_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_build), "__call__") as call:
        call.return_value = cloudbuild.Build()
        client.get_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_builds_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_builds), "__call__") as call:
        call.return_value = cloudbuild.ListBuildsResponse()
        client.list_builds(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ListBuildsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_cancel_build_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.cancel_build), "__call__") as call:
        call.return_value = cloudbuild.Build()
        client.cancel_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CancelBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_retry_build_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.retry_build), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.retry_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.RetryBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_approve_build_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.approve_build), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.approve_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ApproveBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_build_trigger_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_build_trigger), "__call__"
    ) as call:
        call.return_value = cloudbuild.BuildTrigger()
        client.create_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CreateBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_build_trigger_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_build_trigger), "__call__"
    ) as call:
        call.return_value = cloudbuild.BuildTrigger()
        client.get_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_build_triggers_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers), "__call__"
    ) as call:
        call.return_value = cloudbuild.ListBuildTriggersResponse()
        client.list_build_triggers(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ListBuildTriggersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_build_trigger_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_build_trigger), "__call__"
    ) as call:
        call.return_value = None
        client.delete_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.DeleteBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_build_trigger_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_build_trigger), "__call__"
    ) as call:
        call.return_value = cloudbuild.BuildTrigger()
        client.update_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.UpdateBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_run_build_trigger_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.run_build_trigger), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.run_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.RunBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_receive_trigger_webhook_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.receive_trigger_webhook), "__call__"
    ) as call:
        call.return_value = cloudbuild.ReceiveTriggerWebhookResponse()
        client.receive_trigger_webhook(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ReceiveTriggerWebhookRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_worker_pool_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_worker_pool), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_worker_pool(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CreateWorkerPoolRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_worker_pool_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_worker_pool), "__call__") as call:
        call.return_value = cloudbuild.WorkerPool()
        client.get_worker_pool(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetWorkerPoolRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_worker_pool_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_worker_pool), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.delete_worker_pool(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.DeleteWorkerPoolRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_worker_pool_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_worker_pool), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.update_worker_pool(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.UpdateWorkerPoolRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_worker_pools_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools), "__call__"
    ) as call:
        call.return_value = cloudbuild.ListWorkerPoolsResponse()
        client.list_worker_pools(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ListWorkerPoolsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_default_service_account_empty_call_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_default_service_account), "__call__"
    ) as call:
        call.return_value = cloudbuild.DefaultServiceAccount()
        client.get_default_service_account(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetDefaultServiceAccountRequest()
        assert args[0] == request_msg


def test_create_build_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_build), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_build(request={"parent": "projects/sample1/locations/sample2"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.CreateBuildRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_get_build_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_build), "__call__") as call:
        call.return_value = cloudbuild.Build()
        client.get_build(
            request={"name": "projects/sample1/locations/sample2/builds/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.GetBuildRequest(
            **{"name": "projects/sample1/locations/sample2/builds/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_list_builds_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_builds), "__call__") as call:
        call.return_value = cloudbuild.ListBuildsResponse()
        client.list_builds(request={"parent": "projects/sample1/locations/sample2"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.ListBuildsRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_cancel_build_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.cancel_build), "__call__") as call:
        call.return_value = cloudbuild.Build()
        client.cancel_build(
            request={"name": "projects/sample1/locations/sample2/builds/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.CancelBuildRequest(
            **{"name": "projects/sample1/locations/sample2/builds/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_retry_build_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.retry_build), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.retry_build(
            request={"name": "projects/sample1/locations/sample2/builds/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.RetryBuildRequest(
            **{"name": "projects/sample1/locations/sample2/builds/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_approve_build_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.approve_build), "__call__") as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.approve_build(
            request={"name": "projects/sample1/locations/sample2/builds/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.ApproveBuildRequest(
            **{"name": "projects/sample1/locations/sample2/builds/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_create_build_trigger_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_build_trigger), "__call__"
    ) as call:
        call.return_value = cloudbuild.BuildTrigger()
        client.create_build_trigger(
            request={"parent": "projects/sample1/locations/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.CreateBuildTriggerRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_get_build_trigger_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_build_trigger), "__call__"
    ) as call:
        call.return_value = cloudbuild.BuildTrigger()
        client.get_build_trigger(
            request={"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.GetBuildTriggerRequest(
            **{"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_list_build_triggers_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers), "__call__"
    ) as call:
        call.return_value = cloudbuild.ListBuildTriggersResponse()
        client.list_build_triggers(
            request={"parent": "projects/sample1/locations/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.ListBuildTriggersRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_delete_build_trigger_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_build_trigger), "__call__"
    ) as call:
        call.return_value = None
        client.delete_build_trigger(
            request={"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.DeleteBuildTriggerRequest(
            **{"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_update_build_trigger_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_build_trigger), "__call__"
    ) as call:
        call.return_value = cloudbuild.BuildTrigger()
        client.update_build_trigger(
            request={
                "trigger": {
                    "resource_name": "projects/sample1/locations/sample2/triggers/sample3"
                }
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.UpdateBuildTriggerRequest(
            **{
                "trigger": {
                    "resource_name": "projects/sample1/locations/sample2/triggers/sample3"
                }
            }
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_run_build_trigger_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.run_build_trigger), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.run_build_trigger(
            request={"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.RunBuildTriggerRequest(
            **{"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_create_worker_pool_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_worker_pool), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_worker_pool(
            request={"parent": "projects/sample1/locations/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.CreateWorkerPoolRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_get_worker_pool_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_worker_pool), "__call__") as call:
        call.return_value = cloudbuild.WorkerPool()
        client.get_worker_pool(
            request={"name": "projects/sample1/locations/sample2/workerPools/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.GetWorkerPoolRequest(
            **{"name": "projects/sample1/locations/sample2/workerPools/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_delete_worker_pool_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_worker_pool), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.delete_worker_pool(
            request={"name": "projects/sample1/locations/sample2/workerPools/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.DeleteWorkerPoolRequest(
            **{"name": "projects/sample1/locations/sample2/workerPools/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_update_worker_pool_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_worker_pool), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.update_worker_pool(
            request={
                "worker_pool": {
                    "name": "projects/sample1/locations/sample2/workerPools/sample3"
                }
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.UpdateWorkerPoolRequest(
            **{
                "worker_pool": {
                    "name": "projects/sample1/locations/sample2/workerPools/sample3"
                }
            }
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_list_worker_pools_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools), "__call__"
    ) as call:
        call.return_value = cloudbuild.ListWorkerPoolsResponse()
        client.list_worker_pools(
            request={"parent": "projects/sample1/locations/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.ListWorkerPoolsRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_get_default_service_account_routing_parameters_request_1_grpc():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_default_service_account), "__call__"
    ) as call:
        call.return_value = cloudbuild.DefaultServiceAccount()
        client.get_default_service_account(
            request={"name": "projects/sample1/locations/sample2/defaultServiceAccount"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.GetDefaultServiceAccountRequest(
            **{"name": "projects/sample1/locations/sample2/defaultServiceAccount"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_transport_kind_grpc_asyncio():
    transport = CloudBuildAsyncClient.get_transport_class("grpc_asyncio")(
        credentials=async_anonymous_credentials()
    )
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_build_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.create_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CreateBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_build_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.Build(
                name="name_value",
                id="id_value",
                project_id="project_id_value",
                status=cloudbuild.Build.Status.PENDING,
                status_detail="status_detail_value",
                images=["images_value"],
                logs_bucket="logs_bucket_value",
                build_trigger_id="build_trigger_id_value",
                log_url="log_url_value",
                tags=["tags_value"],
                service_account="service_account_value",
            )
        )
        await client.get_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_builds_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_builds), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ListBuildsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_builds(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ListBuildsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_cancel_build_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.cancel_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.Build(
                name="name_value",
                id="id_value",
                project_id="project_id_value",
                status=cloudbuild.Build.Status.PENDING,
                status_detail="status_detail_value",
                images=["images_value"],
                logs_bucket="logs_bucket_value",
                build_trigger_id="build_trigger_id_value",
                log_url="log_url_value",
                tags=["tags_value"],
                service_account="service_account_value",
            )
        )
        await client.cancel_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CancelBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_retry_build_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.retry_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.retry_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.RetryBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_approve_build_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.approve_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.approve_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ApproveBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_build_trigger_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.BuildTrigger(
                resource_name="resource_name_value",
                id="id_value",
                description="description_value",
                name="name_value",
                tags=["tags_value"],
                disabled=True,
                ignored_files=["ignored_files_value"],
                included_files=["included_files_value"],
                filter="filter_value",
                service_account="service_account_value",
            )
        )
        await client.create_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CreateBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_build_trigger_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.BuildTrigger(
                resource_name="resource_name_value",
                id="id_value",
                description="description_value",
                name="name_value",
                tags=["tags_value"],
                disabled=True,
                ignored_files=["ignored_files_value"],
                included_files=["included_files_value"],
                filter="filter_value",
                service_account="service_account_value",
            )
        )
        await client.get_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_build_triggers_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ListBuildTriggersResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_build_triggers(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ListBuildTriggersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_build_trigger_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.DeleteBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_build_trigger_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.BuildTrigger(
                resource_name="resource_name_value",
                id="id_value",
                description="description_value",
                name="name_value",
                tags=["tags_value"],
                disabled=True,
                ignored_files=["ignored_files_value"],
                included_files=["included_files_value"],
                filter="filter_value",
                service_account="service_account_value",
            )
        )
        await client.update_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.UpdateBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_run_build_trigger_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.run_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.run_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.RunBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_receive_trigger_webhook_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.receive_trigger_webhook), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ReceiveTriggerWebhookResponse()
        )
        await client.receive_trigger_webhook(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ReceiveTriggerWebhookRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_worker_pool_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.create_worker_pool(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CreateWorkerPoolRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_worker_pool_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_worker_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.WorkerPool(
                name="name_value",
                display_name="display_name_value",
                uid="uid_value",
                state=cloudbuild.WorkerPool.State.CREATING,
                etag="etag_value",
            )
        )
        await client.get_worker_pool(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetWorkerPoolRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_worker_pool_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.delete_worker_pool(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.DeleteWorkerPoolRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_worker_pool_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.update_worker_pool(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.UpdateWorkerPoolRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_worker_pools_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ListWorkerPoolsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_worker_pools(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ListWorkerPoolsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_default_service_account_empty_call_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_default_service_account), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.DefaultServiceAccount(
                name="name_value",
                service_account_email="service_account_email_value",
            )
        )
        await client.get_default_service_account(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetDefaultServiceAccountRequest()
        assert args[0] == request_msg


@pytest.mark.asyncio
async def test_create_build_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.create_build(
            request={"parent": "projects/sample1/locations/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.CreateBuildRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_get_build_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.Build(
                name="name_value",
                id="id_value",
                project_id="project_id_value",
                status=cloudbuild.Build.Status.PENDING,
                status_detail="status_detail_value",
                images=["images_value"],
                logs_bucket="logs_bucket_value",
                build_trigger_id="build_trigger_id_value",
                log_url="log_url_value",
                tags=["tags_value"],
                service_account="service_account_value",
            )
        )
        await client.get_build(
            request={"name": "projects/sample1/locations/sample2/builds/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.GetBuildRequest(
            **{"name": "projects/sample1/locations/sample2/builds/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_list_builds_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_builds), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ListBuildsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_builds(
            request={"parent": "projects/sample1/locations/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.ListBuildsRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_cancel_build_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.cancel_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.Build(
                name="name_value",
                id="id_value",
                project_id="project_id_value",
                status=cloudbuild.Build.Status.PENDING,
                status_detail="status_detail_value",
                images=["images_value"],
                logs_bucket="logs_bucket_value",
                build_trigger_id="build_trigger_id_value",
                log_url="log_url_value",
                tags=["tags_value"],
                service_account="service_account_value",
            )
        )
        await client.cancel_build(
            request={"name": "projects/sample1/locations/sample2/builds/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.CancelBuildRequest(
            **{"name": "projects/sample1/locations/sample2/builds/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_retry_build_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.retry_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.retry_build(
            request={"name": "projects/sample1/locations/sample2/builds/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.RetryBuildRequest(
            **{"name": "projects/sample1/locations/sample2/builds/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_approve_build_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.approve_build), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.approve_build(
            request={"name": "projects/sample1/locations/sample2/builds/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.ApproveBuildRequest(
            **{"name": "projects/sample1/locations/sample2/builds/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_create_build_trigger_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.BuildTrigger(
                resource_name="resource_name_value",
                id="id_value",
                description="description_value",
                name="name_value",
                tags=["tags_value"],
                disabled=True,
                ignored_files=["ignored_files_value"],
                included_files=["included_files_value"],
                filter="filter_value",
                service_account="service_account_value",
            )
        )
        await client.create_build_trigger(
            request={"parent": "projects/sample1/locations/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.CreateBuildTriggerRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_get_build_trigger_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.BuildTrigger(
                resource_name="resource_name_value",
                id="id_value",
                description="description_value",
                name="name_value",
                tags=["tags_value"],
                disabled=True,
                ignored_files=["ignored_files_value"],
                included_files=["included_files_value"],
                filter="filter_value",
                service_account="service_account_value",
            )
        )
        await client.get_build_trigger(
            request={"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.GetBuildTriggerRequest(
            **{"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_list_build_triggers_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ListBuildTriggersResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_build_triggers(
            request={"parent": "projects/sample1/locations/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.ListBuildTriggersRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_delete_build_trigger_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(None)
        await client.delete_build_trigger(
            request={"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.DeleteBuildTriggerRequest(
            **{"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_update_build_trigger_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.BuildTrigger(
                resource_name="resource_name_value",
                id="id_value",
                description="description_value",
                name="name_value",
                tags=["tags_value"],
                disabled=True,
                ignored_files=["ignored_files_value"],
                included_files=["included_files_value"],
                filter="filter_value",
                service_account="service_account_value",
            )
        )
        await client.update_build_trigger(
            request={
                "trigger": {
                    "resource_name": "projects/sample1/locations/sample2/triggers/sample3"
                }
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.UpdateBuildTriggerRequest(
            **{
                "trigger": {
                    "resource_name": "projects/sample1/locations/sample2/triggers/sample3"
                }
            }
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_run_build_trigger_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.run_build_trigger), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.run_build_trigger(
            request={"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.RunBuildTriggerRequest(
            **{"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_create_worker_pool_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.create_worker_pool(
            request={"parent": "projects/sample1/locations/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.CreateWorkerPoolRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_get_worker_pool_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_worker_pool), "__call__") as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.WorkerPool(
                name="name_value",
                display_name="display_name_value",
                uid="uid_value",
                state=cloudbuild.WorkerPool.State.CREATING,
                etag="etag_value",
            )
        )
        await client.get_worker_pool(
            request={"name": "projects/sample1/locations/sample2/workerPools/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.GetWorkerPoolRequest(
            **{"name": "projects/sample1/locations/sample2/workerPools/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_delete_worker_pool_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.delete_worker_pool(
            request={"name": "projects/sample1/locations/sample2/workerPools/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.DeleteWorkerPoolRequest(
            **{"name": "projects/sample1/locations/sample2/workerPools/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_update_worker_pool_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_worker_pool), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.update_worker_pool(
            request={
                "worker_pool": {
                    "name": "projects/sample1/locations/sample2/workerPools/sample3"
                }
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.UpdateWorkerPoolRequest(
            **{
                "worker_pool": {
                    "name": "projects/sample1/locations/sample2/workerPools/sample3"
                }
            }
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_list_worker_pools_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.ListWorkerPoolsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_worker_pools(
            request={"parent": "projects/sample1/locations/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.ListWorkerPoolsRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


@pytest.mark.asyncio
async def test_get_default_service_account_routing_parameters_request_1_grpc_asyncio():
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_default_service_account), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            cloudbuild.DefaultServiceAccount(
                name="name_value",
                service_account_email="service_account_email_value",
            )
        )
        await client.get_default_service_account(
            request={"name": "projects/sample1/locations/sample2/defaultServiceAccount"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.GetDefaultServiceAccountRequest(
            **{"name": "projects/sample1/locations/sample2/defaultServiceAccount"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_transport_kind_rest():
    transport = CloudBuildClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_create_build_rest_bad_request(request_type=cloudbuild.CreateBuildRequest):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1"}
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
        client.create_build(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.CreateBuildRequest,
        dict,
    ],
)
def test_create_build_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1"}
    request_init["build"] = {
        "name": "name_value",
        "id": "id_value",
        "project_id": "project_id_value",
        "status": 10,
        "status_detail": "status_detail_value",
        "source": {
            "storage_source": {
                "bucket": "bucket_value",
                "object_": "object__value",
                "generation": 1068,
                "source_fetcher": 1,
            },
            "repo_source": {
                "project_id": "project_id_value",
                "repo_name": "repo_name_value",
                "branch_name": "branch_name_value",
                "tag_name": "tag_name_value",
                "commit_sha": "commit_sha_value",
                "dir_": "dir__value",
                "invert_regex": True,
                "substitutions": {},
            },
            "git_source": {
                "url": "url_value",
                "dir_": "dir__value",
                "revision": "revision_value",
            },
            "storage_source_manifest": {
                "bucket": "bucket_value",
                "object_": "object__value",
                "generation": 1068,
            },
            "connected_repository": {
                "repository": "repository_value",
                "dir_": "dir__value",
                "revision": "revision_value",
            },
        },
        "steps": [
            {
                "name": "name_value",
                "env": ["env_value1", "env_value2"],
                "args": ["args_value1", "args_value2"],
                "dir_": "dir__value",
                "id": "id_value",
                "wait_for": ["wait_for_value1", "wait_for_value2"],
                "entrypoint": "entrypoint_value",
                "secret_env": ["secret_env_value1", "secret_env_value2"],
                "volumes": [{"name": "name_value", "path": "path_value"}],
                "timing": {
                    "start_time": {"seconds": 751, "nanos": 543},
                    "end_time": {},
                },
                "pull_timing": {},
                "timeout": {"seconds": 751, "nanos": 543},
                "status": 10,
                "allow_failure": True,
                "exit_code": 948,
                "allow_exit_codes": [1702, 1703],
                "script": "script_value",
                "automap_substitutions": True,
            }
        ],
        "results": {
            "images": [
                {
                    "name": "name_value",
                    "digest": "digest_value",
                    "push_timing": {},
                    "artifact_registry_package": "artifact_registry_package_value",
                }
            ],
            "build_step_images": [
                "build_step_images_value1",
                "build_step_images_value2",
            ],
            "artifact_manifest": "artifact_manifest_value",
            "num_artifacts": 1392,
            "build_step_outputs": [
                b"build_step_outputs_blob1",
                b"build_step_outputs_blob2",
            ],
            "artifact_timing": {},
            "python_packages": [
                {
                    "uri": "uri_value",
                    "file_hashes": {
                        "file_hash": [{"type_": 1, "value": b"value_blob"}]
                    },
                    "push_timing": {},
                    "artifact_registry_package": "artifact_registry_package_value",
                }
            ],
            "maven_artifacts": [
                {
                    "uri": "uri_value",
                    "file_hashes": {},
                    "push_timing": {},
                    "artifact_registry_package": "artifact_registry_package_value",
                }
            ],
            "go_modules": [
                {
                    "uri": "uri_value",
                    "file_hashes": {},
                    "push_timing": {},
                    "artifact_registry_package": "artifact_registry_package_value",
                }
            ],
            "npm_packages": [
                {
                    "uri": "uri_value",
                    "file_hashes": {},
                    "push_timing": {},
                    "artifact_registry_package": "artifact_registry_package_value",
                }
            ],
        },
        "create_time": {},
        "start_time": {},
        "finish_time": {},
        "timeout": {},
        "images": ["images_value1", "images_value2"],
        "queue_ttl": {},
        "artifacts": {
            "images": ["images_value1", "images_value2"],
            "objects": {
                "location": "location_value",
                "paths": ["paths_value1", "paths_value2"],
                "timing": {},
            },
            "maven_artifacts": [
                {
                    "repository": "repository_value",
                    "path": "path_value",
                    "artifact_id": "artifact_id_value",
                    "group_id": "group_id_value",
                    "version": "version_value",
                }
            ],
            "go_modules": [
                {
                    "repository_name": "repository_name_value",
                    "repository_location": "repository_location_value",
                    "repository_project_id": "repository_project_id_value",
                    "source_path": "source_path_value",
                    "module_path": "module_path_value",
                    "module_version": "module_version_value",
                }
            ],
            "python_packages": [
                {
                    "repository": "repository_value",
                    "paths": ["paths_value1", "paths_value2"],
                }
            ],
            "npm_packages": [
                {"repository": "repository_value", "package_path": "package_path_value"}
            ],
        },
        "logs_bucket": "logs_bucket_value",
        "source_provenance": {
            "resolved_storage_source": {},
            "resolved_repo_source": {},
            "resolved_storage_source_manifest": {},
            "resolved_connected_repository": {},
            "resolved_git_source": {},
            "file_hashes": {},
        },
        "build_trigger_id": "build_trigger_id_value",
        "options": {
            "source_provenance_hash": [1],
            "requested_verify_option": 1,
            "machine_type": 1,
            "disk_size_gb": 1261,
            "substitution_option": 1,
            "dynamic_substitutions": True,
            "automap_substitutions": True,
            "log_streaming_option": 1,
            "worker_pool": "worker_pool_value",
            "pool": {
                "name": "name_value",
                "worker_release": "worker_release_value",
                "resolved_worker_release": "resolved_worker_release_value",
            },
            "logging": 1,
            "env": ["env_value1", "env_value2"],
            "secret_env": ["secret_env_value1", "secret_env_value2"],
            "volumes": {},
            "default_logs_bucket_behavior": 1,
            "enable_structured_logging": True,
            "worker_release": "worker_release_value",
            "resolved_worker_release": "resolved_worker_release_value",
        },
        "log_url": "log_url_value",
        "substitutions": {},
        "tags": ["tags_value1", "tags_value2"],
        "secrets": [{"kms_key_name": "kms_key_name_value", "secret_env": {}}],
        "timing": {},
        "approval": {
            "state": 1,
            "config": {"approval_required": True},
            "result": {
                "approver_account": "approver_account_value",
                "approval_time": {},
                "decision": 1,
                "comment": "comment_value",
                "url": "url_value",
            },
        },
        "service_account": "service_account_value",
        "available_secrets": {
            "secret_manager": [
                {"version_name": "version_name_value", "env": "env_value"}
            ],
            "inline": [{"kms_key_name": "kms_key_name_value", "env_map": {}}],
        },
        "warnings": [{"text": "text_value", "priority": 1}],
        "git_config": {
            "http": {"proxy_secret_version_name": "proxy_secret_version_name_value"}
        },
        "failure_info": {"type_": 1, "detail": "detail_value"},
        "dependencies": [
            {
                "empty": True,
                "git_source": {
                    "repository": {
                        "url": "url_value",
                        "developer_connect": "developer_connect_value",
                    },
                    "revision": "revision_value",
                    "recurse_submodules": True,
                    "depth": 533,
                    "dest_path": "dest_path_value",
                    "fetch_tags": True,
                },
            }
        ],
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = cloudbuild.CreateBuildRequest.meta.fields["build"]

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
    for field, value in request_init["build"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["build"][field])):
                    del request_init["build"][field][i][subfield]
            else:
                del request_init["build"][field][subfield]
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
        response = client.create_build(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_build_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_create_build"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_create_build_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_create_build"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.CreateBuildRequest.pb(cloudbuild.CreateBuildRequest())
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

        request = cloudbuild.CreateBuildRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.create_build(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_build_rest_bad_request(request_type=cloudbuild.GetBuildRequest):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "id": "sample2"}
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
        client.get_build(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.GetBuildRequest,
        dict,
    ],
)
def test_get_build_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "id": "sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.Build(
            name="name_value",
            id="id_value",
            project_id="project_id_value",
            status=cloudbuild.Build.Status.PENDING,
            status_detail="status_detail_value",
            images=["images_value"],
            logs_bucket="logs_bucket_value",
            build_trigger_id="build_trigger_id_value",
            log_url="log_url_value",
            tags=["tags_value"],
            service_account="service_account_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloudbuild.Build.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_build(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.Build)
    assert response.name == "name_value"
    assert response.id == "id_value"
    assert response.project_id == "project_id_value"
    assert response.status == cloudbuild.Build.Status.PENDING
    assert response.status_detail == "status_detail_value"
    assert response.images == ["images_value"]
    assert response.logs_bucket == "logs_bucket_value"
    assert response.build_trigger_id == "build_trigger_id_value"
    assert response.log_url == "log_url_value"
    assert response.tags == ["tags_value"]
    assert response.service_account == "service_account_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_build_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_get_build"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_get_build_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(transports.CloudBuildRestInterceptor, "pre_get_build") as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.GetBuildRequest.pb(cloudbuild.GetBuildRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = cloudbuild.Build.to_json(cloudbuild.Build())
        req.return_value.content = return_value

        request = cloudbuild.GetBuildRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloudbuild.Build()
        post_with_metadata.return_value = cloudbuild.Build(), metadata

        client.get_build(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_builds_rest_bad_request(request_type=cloudbuild.ListBuildsRequest):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1"}
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
        client.list_builds(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ListBuildsRequest,
        dict,
    ],
)
def test_list_builds_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.ListBuildsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloudbuild.ListBuildsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_builds(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListBuildsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_builds_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_list_builds"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_list_builds_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_list_builds"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.ListBuildsRequest.pb(cloudbuild.ListBuildsRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = cloudbuild.ListBuildsResponse.to_json(
            cloudbuild.ListBuildsResponse()
        )
        req.return_value.content = return_value

        request = cloudbuild.ListBuildsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloudbuild.ListBuildsResponse()
        post_with_metadata.return_value = cloudbuild.ListBuildsResponse(), metadata

        client.list_builds(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_cancel_build_rest_bad_request(request_type=cloudbuild.CancelBuildRequest):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "id": "sample2"}
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
        client.cancel_build(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.CancelBuildRequest,
        dict,
    ],
)
def test_cancel_build_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "id": "sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.Build(
            name="name_value",
            id="id_value",
            project_id="project_id_value",
            status=cloudbuild.Build.Status.PENDING,
            status_detail="status_detail_value",
            images=["images_value"],
            logs_bucket="logs_bucket_value",
            build_trigger_id="build_trigger_id_value",
            log_url="log_url_value",
            tags=["tags_value"],
            service_account="service_account_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloudbuild.Build.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.cancel_build(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.Build)
    assert response.name == "name_value"
    assert response.id == "id_value"
    assert response.project_id == "project_id_value"
    assert response.status == cloudbuild.Build.Status.PENDING
    assert response.status_detail == "status_detail_value"
    assert response.images == ["images_value"]
    assert response.logs_bucket == "logs_bucket_value"
    assert response.build_trigger_id == "build_trigger_id_value"
    assert response.log_url == "log_url_value"
    assert response.tags == ["tags_value"]
    assert response.service_account == "service_account_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_cancel_build_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_cancel_build"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_cancel_build_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_cancel_build"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.CancelBuildRequest.pb(cloudbuild.CancelBuildRequest())
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = cloudbuild.Build.to_json(cloudbuild.Build())
        req.return_value.content = return_value

        request = cloudbuild.CancelBuildRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloudbuild.Build()
        post_with_metadata.return_value = cloudbuild.Build(), metadata

        client.cancel_build(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_retry_build_rest_bad_request(request_type=cloudbuild.RetryBuildRequest):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "id": "sample2"}
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
        client.retry_build(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.RetryBuildRequest,
        dict,
    ],
)
def test_retry_build_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "id": "sample2"}
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
        response = client.retry_build(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_retry_build_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_retry_build"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_retry_build_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_retry_build"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.RetryBuildRequest.pb(cloudbuild.RetryBuildRequest())
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

        request = cloudbuild.RetryBuildRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.retry_build(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_approve_build_rest_bad_request(request_type=cloudbuild.ApproveBuildRequest):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/builds/sample2"}
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
        client.approve_build(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ApproveBuildRequest,
        dict,
    ],
)
def test_approve_build_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/builds/sample2"}
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
        response = client.approve_build(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_approve_build_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_approve_build"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_approve_build_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_approve_build"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.ApproveBuildRequest.pb(cloudbuild.ApproveBuildRequest())
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

        request = cloudbuild.ApproveBuildRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.approve_build(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_build_trigger_rest_bad_request(
    request_type=cloudbuild.CreateBuildTriggerRequest,
):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1"}
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
        client.create_build_trigger(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.CreateBuildTriggerRequest,
        dict,
    ],
)
def test_create_build_trigger_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1"}
    request_init["trigger"] = {
        "resource_name": "resource_name_value",
        "id": "id_value",
        "description": "description_value",
        "name": "name_value",
        "tags": ["tags_value1", "tags_value2"],
        "trigger_template": {
            "project_id": "project_id_value",
            "repo_name": "repo_name_value",
            "branch_name": "branch_name_value",
            "tag_name": "tag_name_value",
            "commit_sha": "commit_sha_value",
            "dir_": "dir__value",
            "invert_regex": True,
            "substitutions": {},
        },
        "github": {
            "installation_id": 1598,
            "owner": "owner_value",
            "name": "name_value",
            "pull_request": {
                "branch": "branch_value",
                "comment_control": 1,
                "invert_regex": True,
            },
            "push": {
                "branch": "branch_value",
                "tag": "tag_value",
                "invert_regex": True,
            },
        },
        "pubsub_config": {
            "subscription": "subscription_value",
            "topic": "topic_value",
            "service_account_email": "service_account_email_value",
            "state": 1,
        },
        "webhook_config": {"secret": "secret_value", "state": 1},
        "autodetect": True,
        "build": {
            "name": "name_value",
            "id": "id_value",
            "project_id": "project_id_value",
            "status": 10,
            "status_detail": "status_detail_value",
            "source": {
                "storage_source": {
                    "bucket": "bucket_value",
                    "object_": "object__value",
                    "generation": 1068,
                    "source_fetcher": 1,
                },
                "repo_source": {},
                "git_source": {
                    "url": "url_value",
                    "dir_": "dir__value",
                    "revision": "revision_value",
                },
                "storage_source_manifest": {
                    "bucket": "bucket_value",
                    "object_": "object__value",
                    "generation": 1068,
                },
                "connected_repository": {
                    "repository": "repository_value",
                    "dir_": "dir__value",
                    "revision": "revision_value",
                },
            },
            "steps": [
                {
                    "name": "name_value",
                    "env": ["env_value1", "env_value2"],
                    "args": ["args_value1", "args_value2"],
                    "dir_": "dir__value",
                    "id": "id_value",
                    "wait_for": ["wait_for_value1", "wait_for_value2"],
                    "entrypoint": "entrypoint_value",
                    "secret_env": ["secret_env_value1", "secret_env_value2"],
                    "volumes": [{"name": "name_value", "path": "path_value"}],
                    "timing": {
                        "start_time": {"seconds": 751, "nanos": 543},
                        "end_time": {},
                    },
                    "pull_timing": {},
                    "timeout": {"seconds": 751, "nanos": 543},
                    "status": 10,
                    "allow_failure": True,
                    "exit_code": 948,
                    "allow_exit_codes": [1702, 1703],
                    "script": "script_value",
                    "automap_substitutions": True,
                }
            ],
            "results": {
                "images": [
                    {
                        "name": "name_value",
                        "digest": "digest_value",
                        "push_timing": {},
                        "artifact_registry_package": "artifact_registry_package_value",
                    }
                ],
                "build_step_images": [
                    "build_step_images_value1",
                    "build_step_images_value2",
                ],
                "artifact_manifest": "artifact_manifest_value",
                "num_artifacts": 1392,
                "build_step_outputs": [
                    b"build_step_outputs_blob1",
                    b"build_step_outputs_blob2",
                ],
                "artifact_timing": {},
                "python_packages": [
                    {
                        "uri": "uri_value",
                        "file_hashes": {
                            "file_hash": [{"type_": 1, "value": b"value_blob"}]
                        },
                        "push_timing": {},
                        "artifact_registry_package": "artifact_registry_package_value",
                    }
                ],
                "maven_artifacts": [
                    {
                        "uri": "uri_value",
                        "file_hashes": {},
                        "push_timing": {},
                        "artifact_registry_package": "artifact_registry_package_value",
                    }
                ],
                "go_modules": [
                    {
                        "uri": "uri_value",
                        "file_hashes": {},
                        "push_timing": {},
                        "artifact_registry_package": "artifact_registry_package_value",
                    }
                ],
                "npm_packages": [
                    {
                        "uri": "uri_value",
                        "file_hashes": {},
                        "push_timing": {},
                        "artifact_registry_package": "artifact_registry_package_value",
                    }
                ],
            },
            "create_time": {},
            "start_time": {},
            "finish_time": {},
            "timeout": {},
            "images": ["images_value1", "images_value2"],
            "queue_ttl": {},
            "artifacts": {
                "images": ["images_value1", "images_value2"],
                "objects": {
                    "location": "location_value",
                    "paths": ["paths_value1", "paths_value2"],
                    "timing": {},
                },
                "maven_artifacts": [
                    {
                        "repository": "repository_value",
                        "path": "path_value",
                        "artifact_id": "artifact_id_value",
                        "group_id": "group_id_value",
                        "version": "version_value",
                    }
                ],
                "go_modules": [
                    {
                        "repository_name": "repository_name_value",
                        "repository_location": "repository_location_value",
                        "repository_project_id": "repository_project_id_value",
                        "source_path": "source_path_value",
                        "module_path": "module_path_value",
                        "module_version": "module_version_value",
                    }
                ],
                "python_packages": [
                    {
                        "repository": "repository_value",
                        "paths": ["paths_value1", "paths_value2"],
                    }
                ],
                "npm_packages": [
                    {
                        "repository": "repository_value",
                        "package_path": "package_path_value",
                    }
                ],
            },
            "logs_bucket": "logs_bucket_value",
            "source_provenance": {
                "resolved_storage_source": {},
                "resolved_repo_source": {},
                "resolved_storage_source_manifest": {},
                "resolved_connected_repository": {},
                "resolved_git_source": {},
                "file_hashes": {},
            },
            "build_trigger_id": "build_trigger_id_value",
            "options": {
                "source_provenance_hash": [1],
                "requested_verify_option": 1,
                "machine_type": 1,
                "disk_size_gb": 1261,
                "substitution_option": 1,
                "dynamic_substitutions": True,
                "automap_substitutions": True,
                "log_streaming_option": 1,
                "worker_pool": "worker_pool_value",
                "pool": {
                    "name": "name_value",
                    "worker_release": "worker_release_value",
                    "resolved_worker_release": "resolved_worker_release_value",
                },
                "logging": 1,
                "env": ["env_value1", "env_value2"],
                "secret_env": ["secret_env_value1", "secret_env_value2"],
                "volumes": {},
                "default_logs_bucket_behavior": 1,
                "enable_structured_logging": True,
                "worker_release": "worker_release_value",
                "resolved_worker_release": "resolved_worker_release_value",
            },
            "log_url": "log_url_value",
            "substitutions": {},
            "tags": ["tags_value1", "tags_value2"],
            "secrets": [{"kms_key_name": "kms_key_name_value", "secret_env": {}}],
            "timing": {},
            "approval": {
                "state": 1,
                "config": {"approval_required": True},
                "result": {
                    "approver_account": "approver_account_value",
                    "approval_time": {},
                    "decision": 1,
                    "comment": "comment_value",
                    "url": "url_value",
                },
            },
            "service_account": "service_account_value",
            "available_secrets": {
                "secret_manager": [
                    {"version_name": "version_name_value", "env": "env_value"}
                ],
                "inline": [{"kms_key_name": "kms_key_name_value", "env_map": {}}],
            },
            "warnings": [{"text": "text_value", "priority": 1}],
            "git_config": {
                "http": {"proxy_secret_version_name": "proxy_secret_version_name_value"}
            },
            "failure_info": {"type_": 1, "detail": "detail_value"},
            "dependencies": [
                {
                    "empty": True,
                    "git_source": {
                        "repository": {
                            "url": "url_value",
                            "developer_connect": "developer_connect_value",
                        },
                        "revision": "revision_value",
                        "recurse_submodules": True,
                        "depth": 533,
                        "dest_path": "dest_path_value",
                        "fetch_tags": True,
                    },
                }
            ],
        },
        "filename": "filename_value",
        "git_file_source": {
            "path": "path_value",
            "uri": "uri_value",
            "repository": "repository_value",
            "repo_type": 1,
            "revision": "revision_value",
            "github_enterprise_config": "github_enterprise_config_value",
        },
        "create_time": {},
        "disabled": True,
        "substitutions": {},
        "ignored_files": ["ignored_files_value1", "ignored_files_value2"],
        "included_files": ["included_files_value1", "included_files_value2"],
        "filter": "filter_value",
        "source_to_build": {
            "uri": "uri_value",
            "repository": "repository_value",
            "ref": "ref_value",
            "repo_type": 1,
            "github_enterprise_config": "github_enterprise_config_value",
        },
        "approval_config": {},
        "service_account": "service_account_value",
        "repository_event_config": {
            "repository": "repository_value",
            "repository_type": 1,
            "pull_request": {},
            "push": {},
        },
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = cloudbuild.CreateBuildTriggerRequest.meta.fields["trigger"]

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
    for field, value in request_init["trigger"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["trigger"][field])):
                    del request_init["trigger"][field][i][subfield]
            else:
                del request_init["trigger"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.BuildTrigger(
            resource_name="resource_name_value",
            id="id_value",
            description="description_value",
            name="name_value",
            tags=["tags_value"],
            disabled=True,
            ignored_files=["ignored_files_value"],
            included_files=["included_files_value"],
            filter="filter_value",
            service_account="service_account_value",
            autodetect=True,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloudbuild.BuildTrigger.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_build_trigger(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.BuildTrigger)
    assert response.resource_name == "resource_name_value"
    assert response.id == "id_value"
    assert response.description == "description_value"
    assert response.name == "name_value"
    assert response.tags == ["tags_value"]
    assert response.disabled is True
    assert response.ignored_files == ["ignored_files_value"]
    assert response.included_files == ["included_files_value"]
    assert response.filter == "filter_value"
    assert response.service_account == "service_account_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_build_trigger_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_create_build_trigger"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor,
            "post_create_build_trigger_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_create_build_trigger"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.CreateBuildTriggerRequest.pb(
            cloudbuild.CreateBuildTriggerRequest()
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
        return_value = cloudbuild.BuildTrigger.to_json(cloudbuild.BuildTrigger())
        req.return_value.content = return_value

        request = cloudbuild.CreateBuildTriggerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloudbuild.BuildTrigger()
        post_with_metadata.return_value = cloudbuild.BuildTrigger(), metadata

        client.create_build_trigger(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_build_trigger_rest_bad_request(
    request_type=cloudbuild.GetBuildTriggerRequest,
):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "trigger_id": "sample2"}
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
        client.get_build_trigger(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.GetBuildTriggerRequest,
        dict,
    ],
)
def test_get_build_trigger_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "trigger_id": "sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.BuildTrigger(
            resource_name="resource_name_value",
            id="id_value",
            description="description_value",
            name="name_value",
            tags=["tags_value"],
            disabled=True,
            ignored_files=["ignored_files_value"],
            included_files=["included_files_value"],
            filter="filter_value",
            service_account="service_account_value",
            autodetect=True,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloudbuild.BuildTrigger.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_build_trigger(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.BuildTrigger)
    assert response.resource_name == "resource_name_value"
    assert response.id == "id_value"
    assert response.description == "description_value"
    assert response.name == "name_value"
    assert response.tags == ["tags_value"]
    assert response.disabled is True
    assert response.ignored_files == ["ignored_files_value"]
    assert response.included_files == ["included_files_value"]
    assert response.filter == "filter_value"
    assert response.service_account == "service_account_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_build_trigger_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_get_build_trigger"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_get_build_trigger_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_get_build_trigger"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.GetBuildTriggerRequest.pb(
            cloudbuild.GetBuildTriggerRequest()
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
        return_value = cloudbuild.BuildTrigger.to_json(cloudbuild.BuildTrigger())
        req.return_value.content = return_value

        request = cloudbuild.GetBuildTriggerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloudbuild.BuildTrigger()
        post_with_metadata.return_value = cloudbuild.BuildTrigger(), metadata

        client.get_build_trigger(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_build_triggers_rest_bad_request(
    request_type=cloudbuild.ListBuildTriggersRequest,
):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1"}
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
        client.list_build_triggers(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ListBuildTriggersRequest,
        dict,
    ],
)
def test_list_build_triggers_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.ListBuildTriggersResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloudbuild.ListBuildTriggersResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_build_triggers(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListBuildTriggersPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_build_triggers_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_list_build_triggers"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor,
            "post_list_build_triggers_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_list_build_triggers"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.ListBuildTriggersRequest.pb(
            cloudbuild.ListBuildTriggersRequest()
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
        return_value = cloudbuild.ListBuildTriggersResponse.to_json(
            cloudbuild.ListBuildTriggersResponse()
        )
        req.return_value.content = return_value

        request = cloudbuild.ListBuildTriggersRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloudbuild.ListBuildTriggersResponse()
        post_with_metadata.return_value = (
            cloudbuild.ListBuildTriggersResponse(),
            metadata,
        )

        client.list_build_triggers(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_build_trigger_rest_bad_request(
    request_type=cloudbuild.DeleteBuildTriggerRequest,
):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "trigger_id": "sample2"}
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
        client.delete_build_trigger(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.DeleteBuildTriggerRequest,
        dict,
    ],
)
def test_delete_build_trigger_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "trigger_id": "sample2"}
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
        response = client.delete_build_trigger(request)

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_build_trigger_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_delete_build_trigger"
        ) as pre,
    ):
        pre.assert_not_called()
        pb_message = cloudbuild.DeleteBuildTriggerRequest.pb(
            cloudbuild.DeleteBuildTriggerRequest()
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

        request = cloudbuild.DeleteBuildTriggerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata

        client.delete_build_trigger(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()


def test_update_build_trigger_rest_bad_request(
    request_type=cloudbuild.UpdateBuildTriggerRequest,
):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "trigger_id": "sample2"}
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
        client.update_build_trigger(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.UpdateBuildTriggerRequest,
        dict,
    ],
)
def test_update_build_trigger_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "trigger_id": "sample2"}
    request_init["trigger"] = {
        "resource_name": "resource_name_value",
        "id": "id_value",
        "description": "description_value",
        "name": "name_value",
        "tags": ["tags_value1", "tags_value2"],
        "trigger_template": {
            "project_id": "project_id_value",
            "repo_name": "repo_name_value",
            "branch_name": "branch_name_value",
            "tag_name": "tag_name_value",
            "commit_sha": "commit_sha_value",
            "dir_": "dir__value",
            "invert_regex": True,
            "substitutions": {},
        },
        "github": {
            "installation_id": 1598,
            "owner": "owner_value",
            "name": "name_value",
            "pull_request": {
                "branch": "branch_value",
                "comment_control": 1,
                "invert_regex": True,
            },
            "push": {
                "branch": "branch_value",
                "tag": "tag_value",
                "invert_regex": True,
            },
        },
        "pubsub_config": {
            "subscription": "subscription_value",
            "topic": "topic_value",
            "service_account_email": "service_account_email_value",
            "state": 1,
        },
        "webhook_config": {"secret": "secret_value", "state": 1},
        "autodetect": True,
        "build": {
            "name": "name_value",
            "id": "id_value",
            "project_id": "project_id_value",
            "status": 10,
            "status_detail": "status_detail_value",
            "source": {
                "storage_source": {
                    "bucket": "bucket_value",
                    "object_": "object__value",
                    "generation": 1068,
                    "source_fetcher": 1,
                },
                "repo_source": {},
                "git_source": {
                    "url": "url_value",
                    "dir_": "dir__value",
                    "revision": "revision_value",
                },
                "storage_source_manifest": {
                    "bucket": "bucket_value",
                    "object_": "object__value",
                    "generation": 1068,
                },
                "connected_repository": {
                    "repository": "repository_value",
                    "dir_": "dir__value",
                    "revision": "revision_value",
                },
            },
            "steps": [
                {
                    "name": "name_value",
                    "env": ["env_value1", "env_value2"],
                    "args": ["args_value1", "args_value2"],
                    "dir_": "dir__value",
                    "id": "id_value",
                    "wait_for": ["wait_for_value1", "wait_for_value2"],
                    "entrypoint": "entrypoint_value",
                    "secret_env": ["secret_env_value1", "secret_env_value2"],
                    "volumes": [{"name": "name_value", "path": "path_value"}],
                    "timing": {
                        "start_time": {"seconds": 751, "nanos": 543},
                        "end_time": {},
                    },
                    "pull_timing": {},
                    "timeout": {"seconds": 751, "nanos": 543},
                    "status": 10,
                    "allow_failure": True,
                    "exit_code": 948,
                    "allow_exit_codes": [1702, 1703],
                    "script": "script_value",
                    "automap_substitutions": True,
                }
            ],
            "results": {
                "images": [
                    {
                        "name": "name_value",
                        "digest": "digest_value",
                        "push_timing": {},
                        "artifact_registry_package": "artifact_registry_package_value",
                    }
                ],
                "build_step_images": [
                    "build_step_images_value1",
                    "build_step_images_value2",
                ],
                "artifact_manifest": "artifact_manifest_value",
                "num_artifacts": 1392,
                "build_step_outputs": [
                    b"build_step_outputs_blob1",
                    b"build_step_outputs_blob2",
                ],
                "artifact_timing": {},
                "python_packages": [
                    {
                        "uri": "uri_value",
                        "file_hashes": {
                            "file_hash": [{"type_": 1, "value": b"value_blob"}]
                        },
                        "push_timing": {},
                        "artifact_registry_package": "artifact_registry_package_value",
                    }
                ],
                "maven_artifacts": [
                    {
                        "uri": "uri_value",
                        "file_hashes": {},
                        "push_timing": {},
                        "artifact_registry_package": "artifact_registry_package_value",
                    }
                ],
                "go_modules": [
                    {
                        "uri": "uri_value",
                        "file_hashes": {},
                        "push_timing": {},
                        "artifact_registry_package": "artifact_registry_package_value",
                    }
                ],
                "npm_packages": [
                    {
                        "uri": "uri_value",
                        "file_hashes": {},
                        "push_timing": {},
                        "artifact_registry_package": "artifact_registry_package_value",
                    }
                ],
            },
            "create_time": {},
            "start_time": {},
            "finish_time": {},
            "timeout": {},
            "images": ["images_value1", "images_value2"],
            "queue_ttl": {},
            "artifacts": {
                "images": ["images_value1", "images_value2"],
                "objects": {
                    "location": "location_value",
                    "paths": ["paths_value1", "paths_value2"],
                    "timing": {},
                },
                "maven_artifacts": [
                    {
                        "repository": "repository_value",
                        "path": "path_value",
                        "artifact_id": "artifact_id_value",
                        "group_id": "group_id_value",
                        "version": "version_value",
                    }
                ],
                "go_modules": [
                    {
                        "repository_name": "repository_name_value",
                        "repository_location": "repository_location_value",
                        "repository_project_id": "repository_project_id_value",
                        "source_path": "source_path_value",
                        "module_path": "module_path_value",
                        "module_version": "module_version_value",
                    }
                ],
                "python_packages": [
                    {
                        "repository": "repository_value",
                        "paths": ["paths_value1", "paths_value2"],
                    }
                ],
                "npm_packages": [
                    {
                        "repository": "repository_value",
                        "package_path": "package_path_value",
                    }
                ],
            },
            "logs_bucket": "logs_bucket_value",
            "source_provenance": {
                "resolved_storage_source": {},
                "resolved_repo_source": {},
                "resolved_storage_source_manifest": {},
                "resolved_connected_repository": {},
                "resolved_git_source": {},
                "file_hashes": {},
            },
            "build_trigger_id": "build_trigger_id_value",
            "options": {
                "source_provenance_hash": [1],
                "requested_verify_option": 1,
                "machine_type": 1,
                "disk_size_gb": 1261,
                "substitution_option": 1,
                "dynamic_substitutions": True,
                "automap_substitutions": True,
                "log_streaming_option": 1,
                "worker_pool": "worker_pool_value",
                "pool": {
                    "name": "name_value",
                    "worker_release": "worker_release_value",
                    "resolved_worker_release": "resolved_worker_release_value",
                },
                "logging": 1,
                "env": ["env_value1", "env_value2"],
                "secret_env": ["secret_env_value1", "secret_env_value2"],
                "volumes": {},
                "default_logs_bucket_behavior": 1,
                "enable_structured_logging": True,
                "worker_release": "worker_release_value",
                "resolved_worker_release": "resolved_worker_release_value",
            },
            "log_url": "log_url_value",
            "substitutions": {},
            "tags": ["tags_value1", "tags_value2"],
            "secrets": [{"kms_key_name": "kms_key_name_value", "secret_env": {}}],
            "timing": {},
            "approval": {
                "state": 1,
                "config": {"approval_required": True},
                "result": {
                    "approver_account": "approver_account_value",
                    "approval_time": {},
                    "decision": 1,
                    "comment": "comment_value",
                    "url": "url_value",
                },
            },
            "service_account": "service_account_value",
            "available_secrets": {
                "secret_manager": [
                    {"version_name": "version_name_value", "env": "env_value"}
                ],
                "inline": [{"kms_key_name": "kms_key_name_value", "env_map": {}}],
            },
            "warnings": [{"text": "text_value", "priority": 1}],
            "git_config": {
                "http": {"proxy_secret_version_name": "proxy_secret_version_name_value"}
            },
            "failure_info": {"type_": 1, "detail": "detail_value"},
            "dependencies": [
                {
                    "empty": True,
                    "git_source": {
                        "repository": {
                            "url": "url_value",
                            "developer_connect": "developer_connect_value",
                        },
                        "revision": "revision_value",
                        "recurse_submodules": True,
                        "depth": 533,
                        "dest_path": "dest_path_value",
                        "fetch_tags": True,
                    },
                }
            ],
        },
        "filename": "filename_value",
        "git_file_source": {
            "path": "path_value",
            "uri": "uri_value",
            "repository": "repository_value",
            "repo_type": 1,
            "revision": "revision_value",
            "github_enterprise_config": "github_enterprise_config_value",
        },
        "create_time": {},
        "disabled": True,
        "substitutions": {},
        "ignored_files": ["ignored_files_value1", "ignored_files_value2"],
        "included_files": ["included_files_value1", "included_files_value2"],
        "filter": "filter_value",
        "source_to_build": {
            "uri": "uri_value",
            "repository": "repository_value",
            "ref": "ref_value",
            "repo_type": 1,
            "github_enterprise_config": "github_enterprise_config_value",
        },
        "approval_config": {},
        "service_account": "service_account_value",
        "repository_event_config": {
            "repository": "repository_value",
            "repository_type": 1,
            "pull_request": {},
            "push": {},
        },
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = cloudbuild.UpdateBuildTriggerRequest.meta.fields["trigger"]

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
    for field, value in request_init["trigger"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["trigger"][field])):
                    del request_init["trigger"][field][i][subfield]
            else:
                del request_init["trigger"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.BuildTrigger(
            resource_name="resource_name_value",
            id="id_value",
            description="description_value",
            name="name_value",
            tags=["tags_value"],
            disabled=True,
            ignored_files=["ignored_files_value"],
            included_files=["included_files_value"],
            filter="filter_value",
            service_account="service_account_value",
            autodetect=True,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloudbuild.BuildTrigger.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_build_trigger(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.BuildTrigger)
    assert response.resource_name == "resource_name_value"
    assert response.id == "id_value"
    assert response.description == "description_value"
    assert response.name == "name_value"
    assert response.tags == ["tags_value"]
    assert response.disabled is True
    assert response.ignored_files == ["ignored_files_value"]
    assert response.included_files == ["included_files_value"]
    assert response.filter == "filter_value"
    assert response.service_account == "service_account_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_build_trigger_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_update_build_trigger"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor,
            "post_update_build_trigger_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_update_build_trigger"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.UpdateBuildTriggerRequest.pb(
            cloudbuild.UpdateBuildTriggerRequest()
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
        return_value = cloudbuild.BuildTrigger.to_json(cloudbuild.BuildTrigger())
        req.return_value.content = return_value

        request = cloudbuild.UpdateBuildTriggerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloudbuild.BuildTrigger()
        post_with_metadata.return_value = cloudbuild.BuildTrigger(), metadata

        client.update_build_trigger(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_run_build_trigger_rest_bad_request(
    request_type=cloudbuild.RunBuildTriggerRequest,
):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "trigger_id": "sample2"}
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
        client.run_build_trigger(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.RunBuildTriggerRequest,
        dict,
    ],
)
def test_run_build_trigger_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "trigger_id": "sample2"}
    request_init["source"] = {
        "project_id": "project_id_value",
        "repo_name": "repo_name_value",
        "branch_name": "branch_name_value",
        "tag_name": "tag_name_value",
        "commit_sha": "commit_sha_value",
        "dir_": "dir__value",
        "invert_regex": True,
        "substitutions": {},
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = cloudbuild.RunBuildTriggerRequest.meta.fields["source"]

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
    for field, value in request_init["source"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["source"][field])):
                    del request_init["source"][field][i][subfield]
            else:
                del request_init["source"][field][subfield]
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
        response = client.run_build_trigger(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_run_build_trigger_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_run_build_trigger"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_run_build_trigger_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_run_build_trigger"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.RunBuildTriggerRequest.pb(
            cloudbuild.RunBuildTriggerRequest()
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

        request = cloudbuild.RunBuildTriggerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.run_build_trigger(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_receive_trigger_webhook_rest_bad_request(
    request_type=cloudbuild.ReceiveTriggerWebhookRequest,
):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "trigger": "sample2"}
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
        client.receive_trigger_webhook(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ReceiveTriggerWebhookRequest,
        dict,
    ],
)
def test_receive_trigger_webhook_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project_id": "sample1", "trigger": "sample2"}
    request_init["body"] = {
        "content_type": "content_type_value",
        "data": b"data_blob",
        "extensions": [
            {
                "type_url": "type.googleapis.com/google.protobuf.Duration",
                "value": b"\x08\x0c\x10\xdb\x07",
            }
        ],
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = cloudbuild.ReceiveTriggerWebhookRequest.meta.fields["body"]

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
    for field, value in request_init["body"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["body"][field])):
                    del request_init["body"][field][i][subfield]
            else:
                del request_init["body"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.ReceiveTriggerWebhookResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloudbuild.ReceiveTriggerWebhookResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.receive_trigger_webhook(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.ReceiveTriggerWebhookResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_receive_trigger_webhook_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_receive_trigger_webhook"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor,
            "post_receive_trigger_webhook_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_receive_trigger_webhook"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.ReceiveTriggerWebhookRequest.pb(
            cloudbuild.ReceiveTriggerWebhookRequest()
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
        return_value = cloudbuild.ReceiveTriggerWebhookResponse.to_json(
            cloudbuild.ReceiveTriggerWebhookResponse()
        )
        req.return_value.content = return_value

        request = cloudbuild.ReceiveTriggerWebhookRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloudbuild.ReceiveTriggerWebhookResponse()
        post_with_metadata.return_value = (
            cloudbuild.ReceiveTriggerWebhookResponse(),
            metadata,
        )

        client.receive_trigger_webhook(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_worker_pool_rest_bad_request(
    request_type=cloudbuild.CreateWorkerPoolRequest,
):
    client = CloudBuildClient(
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
        client.create_worker_pool(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.CreateWorkerPoolRequest,
        dict,
    ],
)
def test_create_worker_pool_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request_init["worker_pool"] = {
        "name": "name_value",
        "display_name": "display_name_value",
        "uid": "uid_value",
        "annotations": {},
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "delete_time": {},
        "state": 1,
        "private_pool_v1_config": {
            "worker_config": {
                "machine_type": "machine_type_value",
                "disk_size_gb": 1261,
                "enable_nested_virtualization": True,
                "worker_release": "worker_release_value",
            },
            "network_config": {
                "peered_network": "peered_network_value",
                "egress_option": 1,
                "peered_network_ip_range": "peered_network_ip_range_value",
            },
            "private_service_connect": {
                "network_attachment": "network_attachment_value",
                "public_ip_address_disabled": True,
                "route_all_traffic": True,
            },
        },
        "etag": "etag_value",
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = cloudbuild.CreateWorkerPoolRequest.meta.fields["worker_pool"]

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
    for field, value in request_init["worker_pool"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["worker_pool"][field])):
                    del request_init["worker_pool"][field][i][subfield]
            else:
                del request_init["worker_pool"][field][subfield]
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
        response = client.create_worker_pool(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_worker_pool_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_create_worker_pool"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor,
            "post_create_worker_pool_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_create_worker_pool"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.CreateWorkerPoolRequest.pb(
            cloudbuild.CreateWorkerPoolRequest()
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

        request = cloudbuild.CreateWorkerPoolRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.create_worker_pool(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_worker_pool_rest_bad_request(request_type=cloudbuild.GetWorkerPoolRequest):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/locations/sample2/workerPools/sample3"}
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
        client.get_worker_pool(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.GetWorkerPoolRequest,
        dict,
    ],
)
def test_get_worker_pool_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/locations/sample2/workerPools/sample3"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.WorkerPool(
            name="name_value",
            display_name="display_name_value",
            uid="uid_value",
            state=cloudbuild.WorkerPool.State.CREATING,
            etag="etag_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloudbuild.WorkerPool.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_worker_pool(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.WorkerPool)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.uid == "uid_value"
    assert response.state == cloudbuild.WorkerPool.State.CREATING
    assert response.etag == "etag_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_worker_pool_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_get_worker_pool"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_get_worker_pool_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_get_worker_pool"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.GetWorkerPoolRequest.pb(
            cloudbuild.GetWorkerPoolRequest()
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
        return_value = cloudbuild.WorkerPool.to_json(cloudbuild.WorkerPool())
        req.return_value.content = return_value

        request = cloudbuild.GetWorkerPoolRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloudbuild.WorkerPool()
        post_with_metadata.return_value = cloudbuild.WorkerPool(), metadata

        client.get_worker_pool(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_worker_pool_rest_bad_request(
    request_type=cloudbuild.DeleteWorkerPoolRequest,
):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/locations/sample2/workerPools/sample3"}
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
        client.delete_worker_pool(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.DeleteWorkerPoolRequest,
        dict,
    ],
)
def test_delete_worker_pool_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/locations/sample2/workerPools/sample3"}
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
        response = client.delete_worker_pool(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_worker_pool_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_delete_worker_pool"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor,
            "post_delete_worker_pool_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_delete_worker_pool"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.DeleteWorkerPoolRequest.pb(
            cloudbuild.DeleteWorkerPoolRequest()
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

        request = cloudbuild.DeleteWorkerPoolRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.delete_worker_pool(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_worker_pool_rest_bad_request(
    request_type=cloudbuild.UpdateWorkerPoolRequest,
):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "worker_pool": {
            "name": "projects/sample1/locations/sample2/workerPools/sample3"
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
        client.update_worker_pool(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.UpdateWorkerPoolRequest,
        dict,
    ],
)
def test_update_worker_pool_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "worker_pool": {
            "name": "projects/sample1/locations/sample2/workerPools/sample3"
        }
    }
    request_init["worker_pool"] = {
        "name": "projects/sample1/locations/sample2/workerPools/sample3",
        "display_name": "display_name_value",
        "uid": "uid_value",
        "annotations": {},
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "delete_time": {},
        "state": 1,
        "private_pool_v1_config": {
            "worker_config": {
                "machine_type": "machine_type_value",
                "disk_size_gb": 1261,
                "enable_nested_virtualization": True,
                "worker_release": "worker_release_value",
            },
            "network_config": {
                "peered_network": "peered_network_value",
                "egress_option": 1,
                "peered_network_ip_range": "peered_network_ip_range_value",
            },
            "private_service_connect": {
                "network_attachment": "network_attachment_value",
                "public_ip_address_disabled": True,
                "route_all_traffic": True,
            },
        },
        "etag": "etag_value",
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = cloudbuild.UpdateWorkerPoolRequest.meta.fields["worker_pool"]

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
    for field, value in request_init["worker_pool"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["worker_pool"][field])):
                    del request_init["worker_pool"][field][i][subfield]
            else:
                del request_init["worker_pool"][field][subfield]
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
        response = client.update_worker_pool(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_worker_pool_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_update_worker_pool"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor,
            "post_update_worker_pool_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_update_worker_pool"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.UpdateWorkerPoolRequest.pb(
            cloudbuild.UpdateWorkerPoolRequest()
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

        request = cloudbuild.UpdateWorkerPoolRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.update_worker_pool(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_worker_pools_rest_bad_request(
    request_type=cloudbuild.ListWorkerPoolsRequest,
):
    client = CloudBuildClient(
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
        client.list_worker_pools(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.ListWorkerPoolsRequest,
        dict,
    ],
)
def test_list_worker_pools_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "projects/sample1/locations/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.ListWorkerPoolsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloudbuild.ListWorkerPoolsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_worker_pools(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListWorkerPoolsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_worker_pools_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_list_worker_pools"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_list_worker_pools_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_list_worker_pools"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.ListWorkerPoolsRequest.pb(
            cloudbuild.ListWorkerPoolsRequest()
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
        return_value = cloudbuild.ListWorkerPoolsResponse.to_json(
            cloudbuild.ListWorkerPoolsResponse()
        )
        req.return_value.content = return_value

        request = cloudbuild.ListWorkerPoolsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloudbuild.ListWorkerPoolsResponse()
        post_with_metadata.return_value = cloudbuild.ListWorkerPoolsResponse(), metadata

        client.list_worker_pools(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_default_service_account_rest_bad_request(
    request_type=cloudbuild.GetDefaultServiceAccountRequest,
):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/locations/sample2/defaultServiceAccount"}
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
        client.get_default_service_account(request)


@pytest.mark.parametrize(
    "request_type",
    [
        cloudbuild.GetDefaultServiceAccountRequest,
        dict,
    ],
)
def test_get_default_service_account_rest_call_success(request_type):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "projects/sample1/locations/sample2/defaultServiceAccount"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = cloudbuild.DefaultServiceAccount(
            name="name_value",
            service_account_email="service_account_email_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = cloudbuild.DefaultServiceAccount.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_default_service_account(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, cloudbuild.DefaultServiceAccount)
    assert response.name == "name_value"
    assert response.service_account_email == "service_account_email_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_default_service_account_rest_interceptors(null_interceptor):
    transport = transports.CloudBuildRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.CloudBuildRestInterceptor(),
    )
    client = CloudBuildClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "post_get_default_service_account"
        ) as post,
        mock.patch.object(
            transports.CloudBuildRestInterceptor,
            "post_get_default_service_account_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.CloudBuildRestInterceptor, "pre_get_default_service_account"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = cloudbuild.GetDefaultServiceAccountRequest.pb(
            cloudbuild.GetDefaultServiceAccountRequest()
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
        return_value = cloudbuild.DefaultServiceAccount.to_json(
            cloudbuild.DefaultServiceAccount()
        )
        req.return_value.content = return_value

        request = cloudbuild.GetDefaultServiceAccountRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = cloudbuild.DefaultServiceAccount()
        post_with_metadata.return_value = cloudbuild.DefaultServiceAccount(), metadata

        client.get_default_service_account(
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
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_build_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_build), "__call__") as call:
        client.create_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CreateBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_build_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_build), "__call__") as call:
        client.get_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_builds_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_builds), "__call__") as call:
        client.list_builds(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ListBuildsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_cancel_build_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.cancel_build), "__call__") as call:
        client.cancel_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CancelBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_retry_build_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.retry_build), "__call__") as call:
        client.retry_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.RetryBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_approve_build_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.approve_build), "__call__") as call:
        client.approve_build(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ApproveBuildRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_build_trigger_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_build_trigger), "__call__"
    ) as call:
        client.create_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CreateBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_build_trigger_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_build_trigger), "__call__"
    ) as call:
        client.get_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_build_triggers_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers), "__call__"
    ) as call:
        client.list_build_triggers(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ListBuildTriggersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_build_trigger_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_build_trigger), "__call__"
    ) as call:
        client.delete_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.DeleteBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_build_trigger_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_build_trigger), "__call__"
    ) as call:
        client.update_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.UpdateBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_run_build_trigger_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.run_build_trigger), "__call__"
    ) as call:
        client.run_build_trigger(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.RunBuildTriggerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_receive_trigger_webhook_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.receive_trigger_webhook), "__call__"
    ) as call:
        client.receive_trigger_webhook(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ReceiveTriggerWebhookRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_worker_pool_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_worker_pool), "__call__"
    ) as call:
        client.create_worker_pool(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.CreateWorkerPoolRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_worker_pool_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_worker_pool), "__call__") as call:
        client.get_worker_pool(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetWorkerPoolRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_worker_pool_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_worker_pool), "__call__"
    ) as call:
        client.delete_worker_pool(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.DeleteWorkerPoolRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_worker_pool_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_worker_pool), "__call__"
    ) as call:
        client.update_worker_pool(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.UpdateWorkerPoolRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_worker_pools_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools), "__call__"
    ) as call:
        client.list_worker_pools(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.ListWorkerPoolsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_default_service_account_empty_call_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_default_service_account), "__call__"
    ) as call:
        client.get_default_service_account(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = cloudbuild.GetDefaultServiceAccountRequest()
        assert args[0] == request_msg


def test_create_build_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_build), "__call__") as call:
        client.create_build(request={"parent": "projects/sample1/locations/sample2"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.CreateBuildRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_get_build_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_build), "__call__") as call:
        client.get_build(
            request={"name": "projects/sample1/locations/sample2/builds/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.GetBuildRequest(
            **{"name": "projects/sample1/locations/sample2/builds/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_list_builds_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_builds), "__call__") as call:
        client.list_builds(request={"parent": "projects/sample1/locations/sample2"})

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.ListBuildsRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_cancel_build_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.cancel_build), "__call__") as call:
        client.cancel_build(
            request={"name": "projects/sample1/locations/sample2/builds/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.CancelBuildRequest(
            **{"name": "projects/sample1/locations/sample2/builds/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_retry_build_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.retry_build), "__call__") as call:
        client.retry_build(
            request={"name": "projects/sample1/locations/sample2/builds/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.RetryBuildRequest(
            **{"name": "projects/sample1/locations/sample2/builds/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_approve_build_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.approve_build), "__call__") as call:
        client.approve_build(
            request={"name": "projects/sample1/locations/sample2/builds/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.ApproveBuildRequest(
            **{"name": "projects/sample1/locations/sample2/builds/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_create_build_trigger_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_build_trigger), "__call__"
    ) as call:
        client.create_build_trigger(
            request={"parent": "projects/sample1/locations/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.CreateBuildTriggerRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_get_build_trigger_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_build_trigger), "__call__"
    ) as call:
        client.get_build_trigger(
            request={"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.GetBuildTriggerRequest(
            **{"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_list_build_triggers_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_build_triggers), "__call__"
    ) as call:
        client.list_build_triggers(
            request={"parent": "projects/sample1/locations/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.ListBuildTriggersRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_delete_build_trigger_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_build_trigger), "__call__"
    ) as call:
        client.delete_build_trigger(
            request={"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.DeleteBuildTriggerRequest(
            **{"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_update_build_trigger_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_build_trigger), "__call__"
    ) as call:
        client.update_build_trigger(
            request={
                "trigger": {
                    "resource_name": "projects/sample1/locations/sample2/triggers/sample3"
                }
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.UpdateBuildTriggerRequest(
            **{
                "trigger": {
                    "resource_name": "projects/sample1/locations/sample2/triggers/sample3"
                }
            }
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_run_build_trigger_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.run_build_trigger), "__call__"
    ) as call:
        client.run_build_trigger(
            request={"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.RunBuildTriggerRequest(
            **{"name": "projects/sample1/locations/sample2/triggers/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_create_worker_pool_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_worker_pool), "__call__"
    ) as call:
        client.create_worker_pool(
            request={"parent": "projects/sample1/locations/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.CreateWorkerPoolRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_get_worker_pool_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_worker_pool), "__call__") as call:
        client.get_worker_pool(
            request={"name": "projects/sample1/locations/sample2/workerPools/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.GetWorkerPoolRequest(
            **{"name": "projects/sample1/locations/sample2/workerPools/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_delete_worker_pool_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_worker_pool), "__call__"
    ) as call:
        client.delete_worker_pool(
            request={"name": "projects/sample1/locations/sample2/workerPools/sample3"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.DeleteWorkerPoolRequest(
            **{"name": "projects/sample1/locations/sample2/workerPools/sample3"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_update_worker_pool_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_worker_pool), "__call__"
    ) as call:
        client.update_worker_pool(
            request={
                "worker_pool": {
                    "name": "projects/sample1/locations/sample2/workerPools/sample3"
                }
            }
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.UpdateWorkerPoolRequest(
            **{
                "worker_pool": {
                    "name": "projects/sample1/locations/sample2/workerPools/sample3"
                }
            }
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_list_worker_pools_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_worker_pools), "__call__"
    ) as call:
        client.list_worker_pools(
            request={"parent": "projects/sample1/locations/sample2"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.ListWorkerPoolsRequest(
            **{"parent": "projects/sample1/locations/sample2"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_get_default_service_account_routing_parameters_request_1_rest():
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_default_service_account), "__call__"
    ) as call:
        client.get_default_service_account(
            request={"name": "projects/sample1/locations/sample2/defaultServiceAccount"}
        )

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, kw = call.mock_calls[0]
        request_msg = cloudbuild.GetDefaultServiceAccountRequest(
            **{"name": "projects/sample1/locations/sample2/defaultServiceAccount"}
        )
        assert args[0] == request_msg

        expected_headers = {"location": "sample2"}
        assert (
            gapic_v1.routing_header.to_grpc_metadata(expected_headers) in kw["metadata"]
        )


def test_cloud_build_rest_lro_client():
    client = CloudBuildClient(
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
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.CloudBuildGrpcTransport,
    )


def test_cloud_build_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.CloudBuildTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_cloud_build_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.devtools.cloudbuild_v1.services.cloud_build.transports.CloudBuildTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.CloudBuildTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "create_build",
        "get_build",
        "list_builds",
        "cancel_build",
        "retry_build",
        "approve_build",
        "create_build_trigger",
        "get_build_trigger",
        "list_build_triggers",
        "delete_build_trigger",
        "update_build_trigger",
        "run_build_trigger",
        "receive_trigger_webhook",
        "create_worker_pool",
        "get_worker_pool",
        "delete_worker_pool",
        "update_worker_pool",
        "list_worker_pools",
        "get_default_service_account",
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


def test_cloud_build_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.cloud.devtools.cloudbuild_v1.services.cloud_build.transports.CloudBuildTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.CloudBuildTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


def test_cloud_build_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.cloud.devtools.cloudbuild_v1.services.cloud_build.transports.CloudBuildTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.CloudBuildTransport()
        adc.assert_called_once()


def test_cloud_build_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        CloudBuildClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.CloudBuildGrpcTransport,
        transports.CloudBuildGrpcAsyncIOTransport,
    ],
)
def test_cloud_build_transport_auth_adc(transport_class):
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
        transports.CloudBuildGrpcTransport,
        transports.CloudBuildGrpcAsyncIOTransport,
        transports.CloudBuildRestTransport,
    ],
)
def test_cloud_build_transport_auth_gdch_credentials(transport_class):
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
        (transports.CloudBuildGrpcTransport, grpc_helpers),
        (transports.CloudBuildGrpcAsyncIOTransport, grpc_helpers_async),
    ],
)
def test_cloud_build_transport_create_channel(transport_class, grpc_helpers):
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
            "cloudbuild.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=["1", "2"],
            default_host="cloudbuild.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [transports.CloudBuildGrpcTransport, transports.CloudBuildGrpcAsyncIOTransport],
)
def test_cloud_build_grpc_transport_client_cert_source_for_mtls(transport_class):
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


def test_cloud_build_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.CloudBuildRestTransport(
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
def test_cloud_build_host_no_port(transport_name):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="cloudbuild.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "cloudbuild.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://cloudbuild.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_cloud_build_host_with_port(transport_name):
    client = CloudBuildClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="cloudbuild.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "cloudbuild.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://cloudbuild.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_cloud_build_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = CloudBuildClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = CloudBuildClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.create_build._session
    session2 = client2.transport.create_build._session
    assert session1 != session2
    session1 = client1.transport.get_build._session
    session2 = client2.transport.get_build._session
    assert session1 != session2
    session1 = client1.transport.list_builds._session
    session2 = client2.transport.list_builds._session
    assert session1 != session2
    session1 = client1.transport.cancel_build._session
    session2 = client2.transport.cancel_build._session
    assert session1 != session2
    session1 = client1.transport.retry_build._session
    session2 = client2.transport.retry_build._session
    assert session1 != session2
    session1 = client1.transport.approve_build._session
    session2 = client2.transport.approve_build._session
    assert session1 != session2
    session1 = client1.transport.create_build_trigger._session
    session2 = client2.transport.create_build_trigger._session
    assert session1 != session2
    session1 = client1.transport.get_build_trigger._session
    session2 = client2.transport.get_build_trigger._session
    assert session1 != session2
    session1 = client1.transport.list_build_triggers._session
    session2 = client2.transport.list_build_triggers._session
    assert session1 != session2
    session1 = client1.transport.delete_build_trigger._session
    session2 = client2.transport.delete_build_trigger._session
    assert session1 != session2
    session1 = client1.transport.update_build_trigger._session
    session2 = client2.transport.update_build_trigger._session
    assert session1 != session2
    session1 = client1.transport.run_build_trigger._session
    session2 = client2.transport.run_build_trigger._session
    assert session1 != session2
    session1 = client1.transport.receive_trigger_webhook._session
    session2 = client2.transport.receive_trigger_webhook._session
    assert session1 != session2
    session1 = client1.transport.create_worker_pool._session
    session2 = client2.transport.create_worker_pool._session
    assert session1 != session2
    session1 = client1.transport.get_worker_pool._session
    session2 = client2.transport.get_worker_pool._session
    assert session1 != session2
    session1 = client1.transport.delete_worker_pool._session
    session2 = client2.transport.delete_worker_pool._session
    assert session1 != session2
    session1 = client1.transport.update_worker_pool._session
    session2 = client2.transport.update_worker_pool._session
    assert session1 != session2
    session1 = client1.transport.list_worker_pools._session
    session2 = client2.transport.list_worker_pools._session
    assert session1 != session2
    session1 = client1.transport.get_default_service_account._session
    session2 = client2.transport.get_default_service_account._session
    assert session1 != session2


def test_cloud_build_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.CloudBuildGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_cloud_build_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.CloudBuildGrpcAsyncIOTransport(
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
    [transports.CloudBuildGrpcTransport, transports.CloudBuildGrpcAsyncIOTransport],
)
def test_cloud_build_transport_channel_mtls_with_client_cert_source(transport_class):
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
    [transports.CloudBuildGrpcTransport, transports.CloudBuildGrpcAsyncIOTransport],
)
def test_cloud_build_transport_channel_mtls_with_adc(transport_class):
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


def test_cloud_build_grpc_lro_client():
    client = CloudBuildClient(
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


def test_cloud_build_grpc_lro_async_client():
    client = CloudBuildAsyncClient(
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


def test_build_path():
    project = "squid"
    build = "clam"
    expected = "projects/{project}/builds/{build}".format(
        project=project,
        build=build,
    )
    actual = CloudBuildClient.build_path(project, build)
    assert expected == actual


def test_parse_build_path():
    expected = {
        "project": "whelk",
        "build": "octopus",
    }
    path = CloudBuildClient.build_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_build_path(path)
    assert expected == actual


def test_build_trigger_path():
    project = "oyster"
    trigger = "nudibranch"
    expected = "projects/{project}/triggers/{trigger}".format(
        project=project,
        trigger=trigger,
    )
    actual = CloudBuildClient.build_trigger_path(project, trigger)
    assert expected == actual


def test_parse_build_trigger_path():
    expected = {
        "project": "cuttlefish",
        "trigger": "mussel",
    }
    path = CloudBuildClient.build_trigger_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_build_trigger_path(path)
    assert expected == actual


def test_crypto_key_path():
    project = "winkle"
    location = "nautilus"
    keyring = "scallop"
    key = "abalone"
    expected = "projects/{project}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key}".format(
        project=project,
        location=location,
        keyring=keyring,
        key=key,
    )
    actual = CloudBuildClient.crypto_key_path(project, location, keyring, key)
    assert expected == actual


def test_parse_crypto_key_path():
    expected = {
        "project": "squid",
        "location": "clam",
        "keyring": "whelk",
        "key": "octopus",
    }
    path = CloudBuildClient.crypto_key_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_crypto_key_path(path)
    assert expected == actual


def test_default_service_account_path():
    project = "oyster"
    location = "nudibranch"
    expected = "projects/{project}/locations/{location}/defaultServiceAccount".format(
        project=project,
        location=location,
    )
    actual = CloudBuildClient.default_service_account_path(project, location)
    assert expected == actual


def test_parse_default_service_account_path():
    expected = {
        "project": "cuttlefish",
        "location": "mussel",
    }
    path = CloudBuildClient.default_service_account_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_default_service_account_path(path)
    assert expected == actual


def test_github_enterprise_config_path():
    project = "winkle"
    config = "nautilus"
    expected = "projects/{project}/githubEnterpriseConfigs/{config}".format(
        project=project,
        config=config,
    )
    actual = CloudBuildClient.github_enterprise_config_path(project, config)
    assert expected == actual


def test_parse_github_enterprise_config_path():
    expected = {
        "project": "scallop",
        "config": "abalone",
    }
    path = CloudBuildClient.github_enterprise_config_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_github_enterprise_config_path(path)
    assert expected == actual


def test_git_repository_link_path():
    project = "squid"
    location = "clam"
    connection = "whelk"
    git_repository_link = "octopus"
    expected = "projects/{project}/locations/{location}/connections/{connection}/gitRepositoryLinks/{git_repository_link}".format(
        project=project,
        location=location,
        connection=connection,
        git_repository_link=git_repository_link,
    )
    actual = CloudBuildClient.git_repository_link_path(
        project, location, connection, git_repository_link
    )
    assert expected == actual


def test_parse_git_repository_link_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
        "connection": "cuttlefish",
        "git_repository_link": "mussel",
    }
    path = CloudBuildClient.git_repository_link_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_git_repository_link_path(path)
    assert expected == actual


def test_network_path():
    project = "winkle"
    network = "nautilus"
    expected = "projects/{project}/global/networks/{network}".format(
        project=project,
        network=network,
    )
    actual = CloudBuildClient.network_path(project, network)
    assert expected == actual


def test_parse_network_path():
    expected = {
        "project": "scallop",
        "network": "abalone",
    }
    path = CloudBuildClient.network_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_network_path(path)
    assert expected == actual


def test_network_attachment_path():
    project = "squid"
    region = "clam"
    networkattachment = "whelk"
    expected = "projects/{project}/regions/{region}/networkAttachments/{networkattachment}".format(
        project=project,
        region=region,
        networkattachment=networkattachment,
    )
    actual = CloudBuildClient.network_attachment_path(
        project, region, networkattachment
    )
    assert expected == actual


def test_parse_network_attachment_path():
    expected = {
        "project": "octopus",
        "region": "oyster",
        "networkattachment": "nudibranch",
    }
    path = CloudBuildClient.network_attachment_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_network_attachment_path(path)
    assert expected == actual


def test_repository_path():
    project = "cuttlefish"
    location = "mussel"
    connection = "winkle"
    repository = "nautilus"
    expected = "projects/{project}/locations/{location}/connections/{connection}/repositories/{repository}".format(
        project=project,
        location=location,
        connection=connection,
        repository=repository,
    )
    actual = CloudBuildClient.repository_path(project, location, connection, repository)
    assert expected == actual


def test_parse_repository_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
        "connection": "squid",
        "repository": "clam",
    }
    path = CloudBuildClient.repository_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_repository_path(path)
    assert expected == actual


def test_secret_version_path():
    project = "whelk"
    secret = "octopus"
    version = "oyster"
    expected = "projects/{project}/secrets/{secret}/versions/{version}".format(
        project=project,
        secret=secret,
        version=version,
    )
    actual = CloudBuildClient.secret_version_path(project, secret, version)
    assert expected == actual


def test_parse_secret_version_path():
    expected = {
        "project": "nudibranch",
        "secret": "cuttlefish",
        "version": "mussel",
    }
    path = CloudBuildClient.secret_version_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_secret_version_path(path)
    assert expected == actual


def test_service_account_path():
    project = "winkle"
    service_account = "nautilus"
    expected = "projects/{project}/serviceAccounts/{service_account}".format(
        project=project,
        service_account=service_account,
    )
    actual = CloudBuildClient.service_account_path(project, service_account)
    assert expected == actual


def test_parse_service_account_path():
    expected = {
        "project": "scallop",
        "service_account": "abalone",
    }
    path = CloudBuildClient.service_account_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_service_account_path(path)
    assert expected == actual


def test_subscription_path():
    project = "squid"
    subscription = "clam"
    expected = "projects/{project}/subscriptions/{subscription}".format(
        project=project,
        subscription=subscription,
    )
    actual = CloudBuildClient.subscription_path(project, subscription)
    assert expected == actual


def test_parse_subscription_path():
    expected = {
        "project": "whelk",
        "subscription": "octopus",
    }
    path = CloudBuildClient.subscription_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_subscription_path(path)
    assert expected == actual


def test_topic_path():
    project = "oyster"
    topic = "nudibranch"
    expected = "projects/{project}/topics/{topic}".format(
        project=project,
        topic=topic,
    )
    actual = CloudBuildClient.topic_path(project, topic)
    assert expected == actual


def test_parse_topic_path():
    expected = {
        "project": "cuttlefish",
        "topic": "mussel",
    }
    path = CloudBuildClient.topic_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_topic_path(path)
    assert expected == actual


def test_worker_pool_path():
    project = "winkle"
    location = "nautilus"
    worker_pool = "scallop"
    expected = (
        "projects/{project}/locations/{location}/workerPools/{worker_pool}".format(
            project=project,
            location=location,
            worker_pool=worker_pool,
        )
    )
    actual = CloudBuildClient.worker_pool_path(project, location, worker_pool)
    assert expected == actual


def test_parse_worker_pool_path():
    expected = {
        "project": "abalone",
        "location": "squid",
        "worker_pool": "clam",
    }
    path = CloudBuildClient.worker_pool_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_worker_pool_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "whelk"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = CloudBuildClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "octopus",
    }
    path = CloudBuildClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "oyster"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = CloudBuildClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "nudibranch",
    }
    path = CloudBuildClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "cuttlefish"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = CloudBuildClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "mussel",
    }
    path = CloudBuildClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "winkle"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = CloudBuildClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "nautilus",
    }
    path = CloudBuildClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "scallop"
    location = "abalone"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = CloudBuildClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "squid",
        "location": "clam",
    }
    path = CloudBuildClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = CloudBuildClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.CloudBuildTransport, "_prep_wrapped_messages"
    ) as prep:
        client = CloudBuildClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.CloudBuildTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = CloudBuildClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_grpc():
    client = CloudBuildClient(
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
    client = CloudBuildAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = CloudBuildClient(
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
        client = CloudBuildClient(
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
        (CloudBuildClient, transports.CloudBuildGrpcTransport),
        (CloudBuildAsyncClient, transports.CloudBuildGrpcAsyncIOTransport),
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
