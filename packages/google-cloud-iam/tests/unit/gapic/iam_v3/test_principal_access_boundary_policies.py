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
from google.cloud.location import locations_pb2
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account

from google.cloud.iam_v3.services.principal_access_boundary_policies import (
    PrincipalAccessBoundaryPoliciesAsyncClient,
    PrincipalAccessBoundaryPoliciesClient,
    pagers,
    transports,
)
from google.cloud.iam_v3.types import (
    operation_metadata,
    policy_binding_resources,
    principal_access_boundary_policies_service,
    principal_access_boundary_policy_resources,
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
        PrincipalAccessBoundaryPoliciesClient._get_client_cert_source(None, False)
        is None
    )
    assert (
        PrincipalAccessBoundaryPoliciesClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        PrincipalAccessBoundaryPoliciesClient._get_client_cert_source(
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
                PrincipalAccessBoundaryPoliciesClient._get_client_cert_source(
                    None, True
                )
                is mock_default_cert_source
            )
            assert (
                PrincipalAccessBoundaryPoliciesClient._get_client_cert_source(
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
    client = PrincipalAccessBoundaryPoliciesClient(credentials=cred)
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
    client = PrincipalAccessBoundaryPoliciesClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (PrincipalAccessBoundaryPoliciesClient, "grpc"),
        (PrincipalAccessBoundaryPoliciesAsyncClient, "grpc_asyncio"),
        (PrincipalAccessBoundaryPoliciesClient, "rest"),
    ],
)
def test_principal_access_boundary_policies_client_from_service_account_info(
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
            "iam.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://iam.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.PrincipalAccessBoundaryPoliciesGrpcTransport, "grpc"),
        (
            transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (transports.PrincipalAccessBoundaryPoliciesRestTransport, "rest"),
    ],
)
def test_principal_access_boundary_policies_client_service_account_always_use_jwt(
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
        (PrincipalAccessBoundaryPoliciesClient, "grpc"),
        (PrincipalAccessBoundaryPoliciesAsyncClient, "grpc_asyncio"),
        (PrincipalAccessBoundaryPoliciesClient, "rest"),
    ],
)
def test_principal_access_boundary_policies_client_from_service_account_file(
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
            "iam.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://iam.googleapis.com"
        )


def test_principal_access_boundary_policies_client_get_transport_class():
    transport = PrincipalAccessBoundaryPoliciesClient.get_transport_class()
    available_transports = [
        transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
        transports.PrincipalAccessBoundaryPoliciesRestTransport,
    ]
    assert transport in available_transports

    transport = PrincipalAccessBoundaryPoliciesClient.get_transport_class("grpc")
    assert transport == transports.PrincipalAccessBoundaryPoliciesGrpcTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            PrincipalAccessBoundaryPoliciesClient,
            transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
            "grpc",
        ),
        (
            PrincipalAccessBoundaryPoliciesAsyncClient,
            transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            PrincipalAccessBoundaryPoliciesClient,
            transports.PrincipalAccessBoundaryPoliciesRestTransport,
            "rest",
        ),
    ],
)
@mock.patch.object(
    PrincipalAccessBoundaryPoliciesClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(PrincipalAccessBoundaryPoliciesClient),
)
@mock.patch.object(
    PrincipalAccessBoundaryPoliciesAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(PrincipalAccessBoundaryPoliciesAsyncClient),
)
def test_principal_access_boundary_policies_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(
        PrincipalAccessBoundaryPoliciesClient, "get_transport_class"
    ) as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(
        PrincipalAccessBoundaryPoliciesClient, "get_transport_class"
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
            PrincipalAccessBoundaryPoliciesClient,
            transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
            "grpc",
            "true",
        ),
        (
            PrincipalAccessBoundaryPoliciesAsyncClient,
            transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
            "grpc_asyncio",
            "true",
        ),
        (
            PrincipalAccessBoundaryPoliciesClient,
            transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
            "grpc",
            "false",
        ),
        (
            PrincipalAccessBoundaryPoliciesAsyncClient,
            transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
            "grpc_asyncio",
            "false",
        ),
        (
            PrincipalAccessBoundaryPoliciesClient,
            transports.PrincipalAccessBoundaryPoliciesRestTransport,
            "rest",
            "true",
        ),
        (
            PrincipalAccessBoundaryPoliciesClient,
            transports.PrincipalAccessBoundaryPoliciesRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    PrincipalAccessBoundaryPoliciesClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(PrincipalAccessBoundaryPoliciesClient),
)
@mock.patch.object(
    PrincipalAccessBoundaryPoliciesAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(PrincipalAccessBoundaryPoliciesAsyncClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_principal_access_boundary_policies_client_mtls_env_auto(
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
    [PrincipalAccessBoundaryPoliciesClient, PrincipalAccessBoundaryPoliciesAsyncClient],
)
@mock.patch.object(
    PrincipalAccessBoundaryPoliciesClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(PrincipalAccessBoundaryPoliciesClient),
)
@mock.patch.object(
    PrincipalAccessBoundaryPoliciesAsyncClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(PrincipalAccessBoundaryPoliciesAsyncClient),
)
def test_principal_access_boundary_policies_client_get_mtls_endpoint_and_cert_source(
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
    [PrincipalAccessBoundaryPoliciesClient, PrincipalAccessBoundaryPoliciesAsyncClient],
)
@mock.patch.object(
    PrincipalAccessBoundaryPoliciesClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(PrincipalAccessBoundaryPoliciesClient),
)
@mock.patch.object(
    PrincipalAccessBoundaryPoliciesAsyncClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(PrincipalAccessBoundaryPoliciesAsyncClient),
)
def test_principal_access_boundary_policies_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = PrincipalAccessBoundaryPoliciesClient._DEFAULT_UNIVERSE
    default_endpoint = (
        PrincipalAccessBoundaryPoliciesClient._DEFAULT_ENDPOINT_TEMPLATE.format(
            UNIVERSE_DOMAIN=default_universe
        )
    )
    mock_universe = "bar.com"
    mock_endpoint = (
        PrincipalAccessBoundaryPoliciesClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
            PrincipalAccessBoundaryPoliciesClient,
            transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
            "grpc",
        ),
        (
            PrincipalAccessBoundaryPoliciesAsyncClient,
            transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
            "grpc_asyncio",
        ),
        (
            PrincipalAccessBoundaryPoliciesClient,
            transports.PrincipalAccessBoundaryPoliciesRestTransport,
            "rest",
        ),
    ],
)
def test_principal_access_boundary_policies_client_client_options_scopes(
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
            PrincipalAccessBoundaryPoliciesClient,
            transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            PrincipalAccessBoundaryPoliciesAsyncClient,
            transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
        (
            PrincipalAccessBoundaryPoliciesClient,
            transports.PrincipalAccessBoundaryPoliciesRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_principal_access_boundary_policies_client_client_options_credentials_file(
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


def test_principal_access_boundary_policies_client_client_options_from_dict():
    with mock.patch(
        "google.cloud.iam_v3.services.principal_access_boundary_policies.transports.PrincipalAccessBoundaryPoliciesGrpcTransport.__init__"
    ) as grpc_transport:
        grpc_transport.return_value = None
        client = PrincipalAccessBoundaryPoliciesClient(
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
            PrincipalAccessBoundaryPoliciesClient,
            transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
            "grpc",
            grpc_helpers,
        ),
        (
            PrincipalAccessBoundaryPoliciesAsyncClient,
            transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
            "grpc_asyncio",
            grpc_helpers_async,
        ),
    ],
)
def test_principal_access_boundary_policies_client_create_channel_credentials_file(
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
            "iam.googleapis.com:443",
            credentials=file_creds,
            credentials_file=None,
            quota_project_id=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=None,
            default_host="iam.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest(),
        {},
    ],
)
def test_create_principal_access_boundary_policy(request_type, transport: str = "grpc"):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.create_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_principal_access_boundary_policy_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest(
        parent="parent_value",
        principal_access_boundary_policy_id="principal_access_boundary_policy_id_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.create_principal_access_boundary_policy(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest(
            parent="parent_value",
            principal_access_boundary_policy_id="principal_access_boundary_policy_id_value",
        )
        assert args[0] == request_msg


def test_create_principal_access_boundary_policy_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_principal_access_boundary_policy
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.create_principal_access_boundary_policy
        ] = mock_rpc
        request = {}
        client.create_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.create_principal_access_boundary_policy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_create_principal_access_boundary_policy_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.create_principal_access_boundary_policy
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.create_principal_access_boundary_policy
        ] = mock_rpc

        request = {}
        await client.create_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.create_principal_access_boundary_policy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest(),
        {},
    ],
)
async def test_create_principal_access_boundary_policy_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.create_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_create_principal_access_boundary_policy_field_headers():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_principal_access_boundary_policy(request)

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
async def test_create_principal_access_boundary_policy_field_headers_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.create_principal_access_boundary_policy(request)

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


def test_create_principal_access_boundary_policy_flattened():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.create_principal_access_boundary_policy(
            parent="parent_value",
            principal_access_boundary_policy=principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            ),
            principal_access_boundary_policy_id="principal_access_boundary_policy_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].principal_access_boundary_policy
        mock_val = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            )
        )
        assert arg == mock_val
        arg = args[0].principal_access_boundary_policy_id
        mock_val = "principal_access_boundary_policy_id_value"
        assert arg == mock_val


def test_create_principal_access_boundary_policy_flattened_error():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_principal_access_boundary_policy(
            principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest(),
            parent="parent_value",
            principal_access_boundary_policy=principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            ),
            principal_access_boundary_policy_id="principal_access_boundary_policy_id_value",
        )


@pytest.mark.asyncio
async def test_create_principal_access_boundary_policy_flattened_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.create_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.create_principal_access_boundary_policy(
            parent="parent_value",
            principal_access_boundary_policy=principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            ),
            principal_access_boundary_policy_id="principal_access_boundary_policy_id_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val
        arg = args[0].principal_access_boundary_policy
        mock_val = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            )
        )
        assert arg == mock_val
        arg = args[0].principal_access_boundary_policy_id
        mock_val = "principal_access_boundary_policy_id_value"
        assert arg == mock_val


@pytest.mark.asyncio
async def test_create_principal_access_boundary_policy_flattened_error_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.create_principal_access_boundary_policy(
            principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest(),
            parent="parent_value",
            principal_access_boundary_policy=principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            ),
            principal_access_boundary_policy_id="principal_access_boundary_policy_id_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest(),
        {},
    ],
)
def test_get_principal_access_boundary_policy(request_type, transport: str = "grpc"):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value",
                uid="uid_value",
                etag="etag_value",
                display_name="display_name_value",
            )
        )
        response = client.get_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response,
        principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy,
    )
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.etag == "etag_value"
    assert response.display_name == "display_name_value"


def test_get_principal_access_boundary_policy_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest(
        name="name_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.get_principal_access_boundary_policy(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest(
            name="name_value",
        )
        assert args[0] == request_msg


def test_get_principal_access_boundary_policy_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_principal_access_boundary_policy
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_principal_access_boundary_policy
        ] = mock_rpc
        request = {}
        client.get_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_principal_access_boundary_policy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_get_principal_access_boundary_policy_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.get_principal_access_boundary_policy
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.get_principal_access_boundary_policy
        ] = mock_rpc

        request = {}
        await client.get_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.get_principal_access_boundary_policy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest(),
        {},
    ],
)
async def test_get_principal_access_boundary_policy_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value",
                uid="uid_value",
                etag="etag_value",
                display_name="display_name_value",
            )
        )
        response = await client.get_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response,
        principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy,
    )
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.etag == "etag_value"
    assert response.display_name == "display_name_value"


def test_get_principal_access_boundary_policy_field_headers():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy()
        )
        client.get_principal_access_boundary_policy(request)

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
async def test_get_principal_access_boundary_policy_field_headers_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy()
        )
        await client.get_principal_access_boundary_policy(request)

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


def test_get_principal_access_boundary_policy_flattened():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.get_principal_access_boundary_policy(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_get_principal_access_boundary_policy_flattened_error():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_principal_access_boundary_policy(
            principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_get_principal_access_boundary_policy_flattened_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.get_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy()
        )

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.get_principal_access_boundary_policy(
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
async def test_get_principal_access_boundary_policy_flattened_error_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.get_principal_access_boundary_policy(
            principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest(),
        {},
    ],
)
def test_update_principal_access_boundary_policy(request_type, transport: str = "grpc"):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.update_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_principal_access_boundary_policy_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest()

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.update_principal_access_boundary_policy(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request_msg


def test_update_principal_access_boundary_policy_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_principal_access_boundary_policy
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_principal_access_boundary_policy
        ] = mock_rpc
        request = {}
        client.update_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.update_principal_access_boundary_policy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_update_principal_access_boundary_policy_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.update_principal_access_boundary_policy
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.update_principal_access_boundary_policy
        ] = mock_rpc

        request = {}
        await client.update_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.update_principal_access_boundary_policy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest(),
        {},
    ],
)
async def test_update_principal_access_boundary_policy_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.update_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_update_principal_access_boundary_policy_field_headers():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest()

    request.principal_access_boundary_policy.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.update_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "principal_access_boundary_policy.name=name_value",
    ) in kw["metadata"]


@pytest.mark.asyncio
async def test_update_principal_access_boundary_policy_field_headers_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest()

    request.principal_access_boundary_policy.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.update_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        assert args[0] == request

    # Establish that the field header was sent.
    _, _, kw = call.mock_calls[0]
    assert (
        "x-goog-request-params",
        "principal_access_boundary_policy.name=name_value",
    ) in kw["metadata"]


def test_update_principal_access_boundary_policy_flattened():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.update_principal_access_boundary_policy(
            principal_access_boundary_policy=principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].principal_access_boundary_policy
        mock_val = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            )
        )
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


def test_update_principal_access_boundary_policy_flattened_error():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_principal_access_boundary_policy(
            principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest(),
            principal_access_boundary_policy=principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.asyncio
async def test_update_principal_access_boundary_policy_flattened_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.update_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.update_principal_access_boundary_policy(
            principal_access_boundary_policy=principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        arg = args[0].principal_access_boundary_policy
        mock_val = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            )
        )
        assert arg == mock_val
        arg = args[0].update_mask
        mock_val = field_mask_pb2.FieldMask(paths=["paths_value"])
        assert arg == mock_val


@pytest.mark.asyncio
async def test_update_principal_access_boundary_policy_flattened_error_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.update_principal_access_boundary_policy(
            principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest(),
            principal_access_boundary_policy=principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest(),
        {},
    ],
)
def test_delete_principal_access_boundary_policy(request_type, transport: str = "grpc"):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/spam")
        response = client.delete_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_principal_access_boundary_policy_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest(
        name="name_value",
        etag="etag_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.delete_principal_access_boundary_policy(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest(
            name="name_value",
            etag="etag_value",
        )
        assert args[0] == request_msg


def test_delete_principal_access_boundary_policy_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_principal_access_boundary_policy
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.delete_principal_access_boundary_policy
        ] = mock_rpc
        request = {}
        client.delete_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.delete_principal_access_boundary_policy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_delete_principal_access_boundary_policy_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.delete_principal_access_boundary_policy
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.delete_principal_access_boundary_policy
        ] = mock_rpc

        request = {}
        await client.delete_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods call wrapper_fn to build a cached
        # client._transport.operations_client instance on first rpc call.
        # Subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        await client.delete_principal_access_boundary_policy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest(),
        {},
    ],
)
async def test_delete_principal_access_boundary_policy_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        response = await client.delete_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, future.Future)


def test_delete_principal_access_boundary_policy_field_headers():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.delete_principal_access_boundary_policy(request)

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
async def test_delete_principal_access_boundary_policy_field_headers_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/op")
        )
        await client.delete_principal_access_boundary_policy(request)

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


def test_delete_principal_access_boundary_policy_flattened():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.delete_principal_access_boundary_policy(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_delete_principal_access_boundary_policy_flattened_error():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_principal_access_boundary_policy(
            principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_delete_principal_access_boundary_policy_flattened_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = operations_pb2.Operation(name="operations/op")

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.delete_principal_access_boundary_policy(
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
async def test_delete_principal_access_boundary_policy_flattened_error_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.delete_principal_access_boundary_policy(
            principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest(),
            name="name_value",
        )


@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest(),
        {},
    ],
)
def test_list_principal_access_boundary_policies(request_type, transport: str = "grpc"):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_principal_access_boundary_policies), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
            next_page_token="next_page_token_value",
        )
        response = client.list_principal_access_boundary_policies(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListPrincipalAccessBoundaryPoliciesPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_principal_access_boundary_policies_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest(
        parent="parent_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_principal_access_boundary_policies), "__call__"
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.list_principal_access_boundary_policies(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest(
            parent="parent_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_list_principal_access_boundary_policies_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_principal_access_boundary_policies
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_principal_access_boundary_policies
        ] = mock_rpc
        request = {}
        client.list_principal_access_boundary_policies(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_principal_access_boundary_policies(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_list_principal_access_boundary_policies_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.list_principal_access_boundary_policies
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.list_principal_access_boundary_policies
        ] = mock_rpc

        request = {}
        await client.list_principal_access_boundary_policies(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.list_principal_access_boundary_policies(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest(),
        {},
    ],
)
async def test_list_principal_access_boundary_policies_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_principal_access_boundary_policies), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.list_principal_access_boundary_policies(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListPrincipalAccessBoundaryPoliciesAsyncPager)
    assert response.next_page_token == "next_page_token_value"


def test_list_principal_access_boundary_policies_field_headers():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_principal_access_boundary_policies), "__call__"
    ) as call:
        call.return_value = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse()
        client.list_principal_access_boundary_policies(request)

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
async def test_list_principal_access_boundary_policies_field_headers_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest()

    request.parent = "parent_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_principal_access_boundary_policies), "__call__"
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse()
        )
        await client.list_principal_access_boundary_policies(request)

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


def test_list_principal_access_boundary_policies_flattened():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_principal_access_boundary_policies), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.list_principal_access_boundary_policies(
            parent="parent_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].parent
        mock_val = "parent_value"
        assert arg == mock_val


def test_list_principal_access_boundary_policies_flattened_error():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_principal_access_boundary_policies(
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest(),
            parent="parent_value",
        )


@pytest.mark.asyncio
async def test_list_principal_access_boundary_policies_flattened_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_principal_access_boundary_policies), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.list_principal_access_boundary_policies(
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
async def test_list_principal_access_boundary_policies_flattened_error_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.list_principal_access_boundary_policies(
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest(),
            parent="parent_value",
        )


def test_list_principal_access_boundary_policies_pager(transport_name: str = "grpc"):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_principal_access_boundary_policies), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                ],
                next_page_token="abc",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[],
                next_page_token="def",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                ],
                next_page_token="ghi",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
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
        pager = client.list_principal_access_boundary_policies(
            request={}, retry=retry, timeout=timeout
        )

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(
            isinstance(
                i,
                principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy,
            )
            for i in results
        )


def test_list_principal_access_boundary_policies_pages(transport_name: str = "grpc"):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_principal_access_boundary_policies), "__call__"
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                ],
                next_page_token="abc",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[],
                next_page_token="def",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                ],
                next_page_token="ghi",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                ],
            ),
            RuntimeError,
        )
        pages = list(client.list_principal_access_boundary_policies(request={}).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_list_principal_access_boundary_policies_async_pager():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_principal_access_boundary_policies),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                ],
                next_page_token="abc",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[],
                next_page_token="def",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                ],
                next_page_token="ghi",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.list_principal_access_boundary_policies(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(
            isinstance(
                i,
                principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy,
            )
            for i in responses
        )


@pytest.mark.asyncio
async def test_list_principal_access_boundary_policies_async_pages():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.list_principal_access_boundary_policies),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                ],
                next_page_token="abc",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[],
                next_page_token="def",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                ],
                next_page_token="ghi",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.list_principal_access_boundary_policies(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest(),
        {},
    ],
)
def test_search_principal_access_boundary_policy_bindings(
    request_type, transport: str = "grpc"
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.search_principal_access_boundary_policy_bindings),
        "__call__",
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
            next_page_token="next_page_token_value",
        )
        response = client.search_principal_access_boundary_policy_bindings(request)

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        request = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.SearchPrincipalAccessBoundaryPolicyBindingsPager)
    assert response.next_page_token == "next_page_token_value"


def test_search_principal_access_boundary_policy_bindings_non_empty_request_with_auto_populated_field():
    # This test is a coverage failsafe to make sure that UUID4 fields are
    # automatically populated, according to AIP-4235, with non-empty requests.
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest(
        name="name_value",
        page_token="page_token_value",
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.search_principal_access_boundary_policy_bindings),
        "__call__",
    ) as call:
        call.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client.search_principal_access_boundary_policy_bindings(request=request)
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest(
            name="name_value",
            page_token="page_token_value",
        )
        assert args[0] == request_msg


def test_search_principal_access_boundary_policy_bindings_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="grpc",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.search_principal_access_boundary_policy_bindings
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.search_principal_access_boundary_policy_bindings
        ] = mock_rpc
        request = {}
        client.search_principal_access_boundary_policy_bindings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.search_principal_access_boundary_policy_bindings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
async def test_search_principal_access_boundary_policy_bindings_async_use_cached_wrapped_rpc(
    transport: str = "grpc_asyncio",
):
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method_async.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesAsyncClient(
            credentials=async_anonymous_credentials(),
            transport=transport,
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._client._transport.search_principal_access_boundary_policy_bindings
            in client._client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.AsyncMock()
        mock_rpc.return_value = mock.Mock()
        client._client._transport._wrapped_methods[
            client._client._transport.search_principal_access_boundary_policy_bindings
        ] = mock_rpc

        request = {}
        await client.search_principal_access_boundary_policy_bindings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        await client.search_principal_access_boundary_policy_bindings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest(),
        {},
    ],
)
async def test_search_principal_access_boundary_policy_bindings_async(
    request_type, transport: str = "grpc_asyncio"
):
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
        transport=transport,
    )

    # Everything is optional in proto3 as far as the runtime is concerned,
    # and we are mocking out the actual API, so just send an empty request.
    request = request_type

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.search_principal_access_boundary_policy_bindings),
        "__call__",
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                next_page_token="next_page_token_value",
            )
        )
        response = await client.search_principal_access_boundary_policy_bindings(
            request
        )

        # Establish that the underlying gRPC stub method was called.
        assert len(call.mock_calls)
        _, args, _ = call.mock_calls[0]
        request = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest()
        assert args[0] == request

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, pagers.SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager
    )
    assert response.next_page_token == "next_page_token_value"


def test_search_principal_access_boundary_policy_bindings_field_headers():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.search_principal_access_boundary_policy_bindings),
        "__call__",
    ) as call:
        call.return_value = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse()
        client.search_principal_access_boundary_policy_bindings(request)

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
async def test_search_principal_access_boundary_policy_bindings_field_headers_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Any value that is part of the HTTP/1.1 URI should be sent as
    # a field header. Set these to a non-empty value.
    request = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest()

    request.name = "name_value"

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.search_principal_access_boundary_policy_bindings),
        "__call__",
    ) as call:
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse()
        )
        await client.search_principal_access_boundary_policy_bindings(request)

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


def test_search_principal_access_boundary_policy_bindings_flattened():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.search_principal_access_boundary_policy_bindings),
        "__call__",
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse()
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        client.search_principal_access_boundary_policy_bindings(
            name="name_value",
        )

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(call.mock_calls) == 1
        _, args, _ = call.mock_calls[0]
        arg = args[0].name
        mock_val = "name_value"
        assert arg == mock_val


def test_search_principal_access_boundary_policy_bindings_flattened_error():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.search_principal_access_boundary_policy_bindings(
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest(),
            name="name_value",
        )


@pytest.mark.asyncio
async def test_search_principal_access_boundary_policy_bindings_flattened_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.search_principal_access_boundary_policy_bindings),
        "__call__",
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse()

        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse()
        )
        # Call the method with a truthy value for each flattened field,
        # using the keyword arguments to the method.
        response = await client.search_principal_access_boundary_policy_bindings(
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
async def test_search_principal_access_boundary_policy_bindings_flattened_error_async():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        await client.search_principal_access_boundary_policy_bindings(
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest(),
            name="name_value",
        )


def test_search_principal_access_boundary_policy_bindings_pager(
    transport_name: str = "grpc",
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.search_principal_access_boundary_policy_bindings),
        "__call__",
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                ],
                next_page_token="abc",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[],
                next_page_token="def",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                ],
                next_page_token="ghi",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                ],
            ),
            RuntimeError,
        )

        expected_metadata = ()
        retry = retries.Retry()
        timeout = 5
        expected_metadata = tuple(expected_metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", ""),)),
        )
        pager = client.search_principal_access_boundary_policy_bindings(
            request={}, retry=retry, timeout=timeout
        )

        assert pager._metadata == expected_metadata
        assert pager._retry == retry
        assert pager._timeout == timeout

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(
            isinstance(i, policy_binding_resources.PolicyBinding) for i in results
        )


def test_search_principal_access_boundary_policy_bindings_pages(
    transport_name: str = "grpc",
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport_name,
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.search_principal_access_boundary_policy_bindings),
        "__call__",
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                ],
                next_page_token="abc",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[],
                next_page_token="def",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                ],
                next_page_token="ghi",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                ],
            ),
            RuntimeError,
        )
        pages = list(
            client.search_principal_access_boundary_policy_bindings(request={}).pages
        )
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


@pytest.mark.asyncio
async def test_search_principal_access_boundary_policy_bindings_async_pager():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.search_principal_access_boundary_policy_bindings),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                ],
                next_page_token="abc",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[],
                next_page_token="def",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                ],
                next_page_token="ghi",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                ],
            ),
            RuntimeError,
        )
        async_pager = await client.search_principal_access_boundary_policy_bindings(
            request={},
        )
        assert async_pager.next_page_token == "abc"
        assert str(async_pager).startswith(f"{async_pager.__class__.__name__}<")

        responses = []
        async for response in async_pager:  # pragma: no branch
            responses.append(response)

        assert len(responses) == 6
        assert all(
            isinstance(i, policy_binding_resources.PolicyBinding) for i in responses
        )


@pytest.mark.asyncio
async def test_search_principal_access_boundary_policy_bindings_async_pages():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
        type(client.transport.search_principal_access_boundary_policy_bindings),
        "__call__",
        new_callable=mock.AsyncMock,
    ) as call:
        # Set the response to a series of pages.
        call.side_effect = (
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                ],
                next_page_token="abc",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[],
                next_page_token="def",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                ],
                next_page_token="ghi",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                ],
            ),
            RuntimeError,
        )
        pages = []
        async for page_ in (
            await client.search_principal_access_boundary_policy_bindings(request={})
        ).pages:
            pages.append(page_)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_create_principal_access_boundary_policy_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_principal_access_boundary_policy
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.create_principal_access_boundary_policy
        ] = mock_rpc

        request = {}
        client.create_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.create_principal_access_boundary_policy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_principal_access_boundary_policy_rest_required_fields(
    request_type=principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest,
):
    transport_class = transports.PrincipalAccessBoundaryPoliciesRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["principal_access_boundary_policy_id"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped
    assert "principalAccessBoundaryPolicyId" not in jsonified_request

    default_values = getattr(
        transport_class._BaseCreatePrincipalAccessBoundaryPolicy,
        "_BaseCreatePrincipalAccessBoundaryPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "principalAccessBoundaryPolicyId" in jsonified_request
    assert (
        jsonified_request["principalAccessBoundaryPolicyId"]
        == request_init["principal_access_boundary_policy_id"]
    )

    jsonified_request["parent"] = "parent_value"
    jsonified_request["principalAccessBoundaryPolicyId"] = (
        "principal_access_boundary_policy_id_value"
    )

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "principalAccessBoundaryPolicyId",
            "validateOnly",
        )
    )

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "principalAccessBoundaryPolicyId" in jsonified_request
    assert (
        jsonified_request["principalAccessBoundaryPolicyId"]
        == "principal_access_boundary_policy_id_value"
    )

    client = PrincipalAccessBoundaryPoliciesClient(
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

            response = client.create_principal_access_boundary_policy(request)

            expected_params = [
                (
                    "principalAccessBoundaryPolicyId",
                    "",
                ),
                ("$alt", "json;enum-encoding=int"),
            ]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_principal_access_boundary_policy_rest_flattened():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "organizations/sample1/locations/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            principal_access_boundary_policy=principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            ),
            principal_access_boundary_policy_id="principal_access_boundary_policy_id_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_principal_access_boundary_policy(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v3/{parent=organizations/*/locations/*}/principalAccessBoundaryPolicies"
            % client.transport._host,
            args[1],
        )


def test_create_principal_access_boundary_policy_rest_flattened_error(
    transport: str = "rest",
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_principal_access_boundary_policy(
            principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest(),
            parent="parent_value",
            principal_access_boundary_policy=principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            ),
            principal_access_boundary_policy_id="principal_access_boundary_policy_id_value",
        )


def test_get_principal_access_boundary_policy_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_principal_access_boundary_policy
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_principal_access_boundary_policy
        ] = mock_rpc

        request = {}
        client.get_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_principal_access_boundary_policy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_principal_access_boundary_policy_rest_required_fields(
    request_type=principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest,
):
    transport_class = transports.PrincipalAccessBoundaryPoliciesRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetPrincipalAccessBoundaryPolicy,
        "_BaseGetPrincipalAccessBoundaryPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = (
        principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy()
    )
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
            return_value = principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_principal_access_boundary_policy(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_principal_access_boundary_policy_rest_flattened():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy()
        )

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "organizations/sample1/locations/sample2/principalAccessBoundaryPolicies/sample3"
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
        return_value = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_principal_access_boundary_policy(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v3/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}"
            % client.transport._host,
            args[1],
        )


def test_get_principal_access_boundary_policy_rest_flattened_error(
    transport: str = "rest",
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_principal_access_boundary_policy(
            principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest(),
            name="name_value",
        )


def test_update_principal_access_boundary_policy_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_principal_access_boundary_policy
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_principal_access_boundary_policy
        ] = mock_rpc

        request = {}
        client.update_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.update_principal_access_boundary_policy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_principal_access_boundary_policy_rest_required_fields(
    request_type=principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest,
):
    transport_class = transports.PrincipalAccessBoundaryPoliciesRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdatePrincipalAccessBoundaryPolicy,
        "_BaseUpdatePrincipalAccessBoundaryPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = PrincipalAccessBoundaryPoliciesClient(
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

            response = client.update_principal_access_boundary_policy(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_principal_access_boundary_policy_rest_flattened():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "principal_access_boundary_policy": {
                "name": "organizations/sample1/locations/sample2/principalAccessBoundaryPolicies/sample3"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            principal_access_boundary_policy=principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            ),
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

        client.update_principal_access_boundary_policy(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v3/{principal_access_boundary_policy.name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}"
            % client.transport._host,
            args[1],
        )


def test_update_principal_access_boundary_policy_rest_flattened_error(
    transport: str = "rest",
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_principal_access_boundary_policy(
            principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest(),
            principal_access_boundary_policy=principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value"
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_delete_principal_access_boundary_policy_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_principal_access_boundary_policy
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.delete_principal_access_boundary_policy
        ] = mock_rpc

        request = {}
        client.delete_principal_access_boundary_policy(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.delete_principal_access_boundary_policy(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_principal_access_boundary_policy_rest_required_fields(
    request_type=principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest,
):
    transport_class = transports.PrincipalAccessBoundaryPoliciesRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeletePrincipalAccessBoundaryPolicy,
        "_BaseDeletePrincipalAccessBoundaryPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
            "etag",
            "force",
            "validateOnly",
        )
    )

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = PrincipalAccessBoundaryPoliciesClient(
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

            response = client.delete_principal_access_boundary_policy(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_principal_access_boundary_policy_rest_flattened():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation(name="operations/spam")

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "organizations/sample1/locations/sample2/principalAccessBoundaryPolicies/sample3"
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

        client.delete_principal_access_boundary_policy(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v3/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}"
            % client.transport._host,
            args[1],
        )


def test_delete_principal_access_boundary_policy_rest_flattened_error(
    transport: str = "rest",
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_principal_access_boundary_policy(
            principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest(),
            name="name_value",
        )


def test_list_principal_access_boundary_policies_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_principal_access_boundary_policies
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_principal_access_boundary_policies
        ] = mock_rpc

        request = {}
        client.list_principal_access_boundary_policies(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_principal_access_boundary_policies(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_principal_access_boundary_policies_rest_required_fields(
    request_type=principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest,
):
    transport_class = transports.PrincipalAccessBoundaryPoliciesRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListPrincipalAccessBoundaryPolicies,
        "_BaseListPrincipalAccessBoundaryPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse()
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
            return_value = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_principal_access_boundary_policies(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_principal_access_boundary_policies_rest_flattened():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "organizations/sample1/locations/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_principal_access_boundary_policies(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v3/{parent=organizations/*/locations/*}/principalAccessBoundaryPolicies"
            % client.transport._host,
            args[1],
        )


def test_list_principal_access_boundary_policies_rest_flattened_error(
    transport: str = "rest",
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_principal_access_boundary_policies(
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest(),
            parent="parent_value",
        )


def test_list_principal_access_boundary_policies_rest_pager(transport: str = "rest"):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                ],
                next_page_token="abc",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[],
                next_page_token="def",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                ],
                next_page_token="ghi",
            ),
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                principal_access_boundary_policies=[
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                    principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse.to_json(
                x
            )
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "organizations/sample1/locations/sample2"}

        pager = client.list_principal_access_boundary_policies(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(
            isinstance(
                i,
                principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy,
            )
            for i in results
        )

        pages = list(
            client.list_principal_access_boundary_policies(request=sample_request).pages
        )
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_search_principal_access_boundary_policy_bindings_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = PrincipalAccessBoundaryPoliciesClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.search_principal_access_boundary_policy_bindings
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.search_principal_access_boundary_policy_bindings
        ] = mock_rpc

        request = {}
        client.search_principal_access_boundary_policy_bindings(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.search_principal_access_boundary_policy_bindings(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_search_principal_access_boundary_policy_bindings_rest_required_fields(
    request_type=principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest,
):
    transport_class = transports.PrincipalAccessBoundaryPoliciesRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseSearchPrincipalAccessBoundaryPolicyBindings,
        "_BaseSearchPrincipalAccessBoundaryPolicyBindings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
            "pageSize",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse()
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
            return_value = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.search_principal_access_boundary_policy_bindings(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_search_principal_access_boundary_policy_bindings_rest_flattened():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "name": "organizations/sample1/locations/sample2/principalAccessBoundaryPolicies/sample3"
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
        return_value = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.search_principal_access_boundary_policy_bindings(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v3/{name=organizations/*/locations/*/principalAccessBoundaryPolicies/*}:searchPolicyBindings"
            % client.transport._host,
            args[1],
        )


def test_search_principal_access_boundary_policy_bindings_rest_flattened_error(
    transport: str = "rest",
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.search_principal_access_boundary_policy_bindings(
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest(),
            name="name_value",
        )


def test_search_principal_access_boundary_policy_bindings_rest_pager(
    transport: str = "rest",
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                ],
                next_page_token="abc",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[],
                next_page_token="def",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                ],
                next_page_token="ghi",
            ),
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                policy_bindings=[
                    policy_binding_resources.PolicyBinding(),
                    policy_binding_resources.PolicyBinding(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse.to_json(
                x
            )
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "name": "organizations/sample1/locations/sample2/principalAccessBoundaryPolicies/sample3"
        }

        pager = client.search_principal_access_boundary_policy_bindings(
            request=sample_request
        )

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(
            isinstance(i, policy_binding_resources.PolicyBinding) for i in results
        )

        pages = list(
            client.search_principal_access_boundary_policy_bindings(
                request=sample_request
            ).pages
        )
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.PrincipalAccessBoundaryPoliciesGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = PrincipalAccessBoundaryPoliciesClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.PrincipalAccessBoundaryPoliciesGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = PrincipalAccessBoundaryPoliciesClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.PrincipalAccessBoundaryPoliciesGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = PrincipalAccessBoundaryPoliciesClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = PrincipalAccessBoundaryPoliciesClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.PrincipalAccessBoundaryPoliciesGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = PrincipalAccessBoundaryPoliciesClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.PrincipalAccessBoundaryPoliciesGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = PrincipalAccessBoundaryPoliciesClient(transport=transport)
    assert client.transport is transport


def test_transport_get_channel():
    # A client may be instantiated with a custom transport instance.
    transport = transports.PrincipalAccessBoundaryPoliciesGrpcTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel

    transport = transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    channel = transport.grpc_channel
    assert channel


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
        transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
        transports.PrincipalAccessBoundaryPoliciesRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_grpc():
    transport = PrincipalAccessBoundaryPoliciesClient.get_transport_class("grpc")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "grpc"


def test_initialize_client_w_grpc():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="grpc"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_principal_access_boundary_policy_empty_call_grpc():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.create_principal_access_boundary_policy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_principal_access_boundary_policy_empty_call_grpc():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy()
        )
        client.get_principal_access_boundary_policy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_principal_access_boundary_policy_empty_call_grpc():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.update_principal_access_boundary_policy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_principal_access_boundary_policy_empty_call_grpc():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_principal_access_boundary_policy), "__call__"
    ) as call:
        call.return_value = operations_pb2.Operation(name="operations/op")
        client.delete_principal_access_boundary_policy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_principal_access_boundary_policies_empty_call_grpc():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_principal_access_boundary_policies), "__call__"
    ) as call:
        call.return_value = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse()
        client.list_principal_access_boundary_policies(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_search_principal_access_boundary_policy_bindings_empty_call_grpc():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="grpc",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.search_principal_access_boundary_policy_bindings),
        "__call__",
    ) as call:
        call.return_value = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse()
        client.search_principal_access_boundary_policy_bindings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest()
        assert args[0] == request_msg


def test_transport_kind_grpc_asyncio():
    transport = PrincipalAccessBoundaryPoliciesAsyncClient.get_transport_class(
        "grpc_asyncio"
    )(credentials=async_anonymous_credentials())
    assert transport.kind == "grpc_asyncio"


def test_initialize_client_w_grpc_asyncio():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_create_principal_access_boundary_policy_empty_call_grpc_asyncio():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.create_principal_access_boundary_policy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_get_principal_access_boundary_policy_empty_call_grpc_asyncio():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value",
                uid="uid_value",
                etag="etag_value",
                display_name="display_name_value",
            )
        )
        await client.get_principal_access_boundary_policy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_update_principal_access_boundary_policy_empty_call_grpc_asyncio():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.update_principal_access_boundary_policy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_delete_principal_access_boundary_policy_empty_call_grpc_asyncio():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_principal_access_boundary_policy), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            operations_pb2.Operation(name="operations/spam")
        )
        await client.delete_principal_access_boundary_policy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_list_principal_access_boundary_policies_empty_call_grpc_asyncio():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_principal_access_boundary_policies), "__call__"
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.list_principal_access_boundary_policies(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
@pytest.mark.asyncio
async def test_search_principal_access_boundary_policy_bindings_empty_call_grpc_asyncio():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(),
        transport="grpc_asyncio",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.search_principal_access_boundary_policy_bindings),
        "__call__",
    ) as call:
        # Designate an appropriate return value for the call.
        call.return_value = grpc_helpers_async.FakeUnaryUnaryCall(
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
                next_page_token="next_page_token_value",
            )
        )
        await client.search_principal_access_boundary_policy_bindings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest()
        assert args[0] == request_msg


def test_transport_kind_rest():
    transport = PrincipalAccessBoundaryPoliciesClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_create_principal_access_boundary_policy_rest_bad_request(
    request_type=principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest,
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1/locations/sample2"}
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
        client.create_principal_access_boundary_policy(request)


@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest,
        dict,
    ],
)
def test_create_principal_access_boundary_policy_rest_call_success(request_type):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1/locations/sample2"}
    request_init["principal_access_boundary_policy"] = {
        "name": "name_value",
        "uid": "uid_value",
        "etag": "etag_value",
        "display_name": "display_name_value",
        "annotations": {},
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "details": {
            "rules": [
                {
                    "description": "description_value",
                    "resources": ["resources_value1", "resources_value2"],
                    "effect": 1,
                }
            ],
            "enforcement_version": "enforcement_version_value",
        },
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest.meta.fields[
        "principal_access_boundary_policy"
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
        "principal_access_boundary_policy"
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
                for i in range(
                    0, len(request_init["principal_access_boundary_policy"][field])
                ):
                    del request_init["principal_access_boundary_policy"][field][i][
                        subfield
                    ]
            else:
                del request_init["principal_access_boundary_policy"][field][subfield]
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
        response = client.create_principal_access_boundary_policy(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_principal_access_boundary_policy_rest_interceptors(null_interceptor):
    transport = transports.PrincipalAccessBoundaryPoliciesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.PrincipalAccessBoundaryPoliciesRestInterceptor(),
    )
    client = PrincipalAccessBoundaryPoliciesClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "post_create_principal_access_boundary_policy",
        ) as post,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "post_create_principal_access_boundary_policy_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "pre_create_principal_access_boundary_policy",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest.pb(
            principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest()
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

        request = principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.create_principal_access_boundary_policy(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_principal_access_boundary_policy_rest_bad_request(
    request_type=principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest,
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "organizations/sample1/locations/sample2/principalAccessBoundaryPolicies/sample3"
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
        client.get_principal_access_boundary_policy(request)


@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest,
        dict,
    ],
)
def test_get_principal_access_boundary_policy_rest_call_success(request_type):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "organizations/sample1/locations/sample2/principalAccessBoundaryPolicies/sample3"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(
                name="name_value",
                uid="uid_value",
                etag="etag_value",
                display_name="display_name_value",
            )
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_principal_access_boundary_policy(request)

    # Establish that the response is the type that we expect.
    assert isinstance(
        response,
        principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy,
    )
    assert response.name == "name_value"
    assert response.uid == "uid_value"
    assert response.etag == "etag_value"
    assert response.display_name == "display_name_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_principal_access_boundary_policy_rest_interceptors(null_interceptor):
    transport = transports.PrincipalAccessBoundaryPoliciesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.PrincipalAccessBoundaryPoliciesRestInterceptor(),
    )
    client = PrincipalAccessBoundaryPoliciesClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "post_get_principal_access_boundary_policy",
        ) as post,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "post_get_principal_access_boundary_policy_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "pre_get_principal_access_boundary_policy",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest.pb(
            principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest()
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
        return_value = principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy.to_json(
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy()
        )
        req.return_value.content = return_value

        request = principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy()
        )
        post_with_metadata.return_value = (
            principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy(),
            metadata,
        )

        client.get_principal_access_boundary_policy(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_principal_access_boundary_policy_rest_bad_request(
    request_type=principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest,
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "principal_access_boundary_policy": {
            "name": "organizations/sample1/locations/sample2/principalAccessBoundaryPolicies/sample3"
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
        client.update_principal_access_boundary_policy(request)


@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest,
        dict,
    ],
)
def test_update_principal_access_boundary_policy_rest_call_success(request_type):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "principal_access_boundary_policy": {
            "name": "organizations/sample1/locations/sample2/principalAccessBoundaryPolicies/sample3"
        }
    }
    request_init["principal_access_boundary_policy"] = {
        "name": "organizations/sample1/locations/sample2/principalAccessBoundaryPolicies/sample3",
        "uid": "uid_value",
        "etag": "etag_value",
        "display_name": "display_name_value",
        "annotations": {},
        "create_time": {"seconds": 751, "nanos": 543},
        "update_time": {},
        "details": {
            "rules": [
                {
                    "description": "description_value",
                    "resources": ["resources_value1", "resources_value2"],
                    "effect": 1,
                }
            ],
            "enforcement_version": "enforcement_version_value",
        },
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest.meta.fields[
        "principal_access_boundary_policy"
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
        "principal_access_boundary_policy"
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
                for i in range(
                    0, len(request_init["principal_access_boundary_policy"][field])
                ):
                    del request_init["principal_access_boundary_policy"][field][i][
                        subfield
                    ]
            else:
                del request_init["principal_access_boundary_policy"][field][subfield]
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
        response = client.update_principal_access_boundary_policy(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_principal_access_boundary_policy_rest_interceptors(null_interceptor):
    transport = transports.PrincipalAccessBoundaryPoliciesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.PrincipalAccessBoundaryPoliciesRestInterceptor(),
    )
    client = PrincipalAccessBoundaryPoliciesClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "post_update_principal_access_boundary_policy",
        ) as post,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "post_update_principal_access_boundary_policy_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "pre_update_principal_access_boundary_policy",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest.pb(
            principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest()
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

        request = principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.update_principal_access_boundary_policy(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_principal_access_boundary_policy_rest_bad_request(
    request_type=principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest,
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "organizations/sample1/locations/sample2/principalAccessBoundaryPolicies/sample3"
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
        client.delete_principal_access_boundary_policy(request)


@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest,
        dict,
    ],
)
def test_delete_principal_access_boundary_policy_rest_call_success(request_type):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "organizations/sample1/locations/sample2/principalAccessBoundaryPolicies/sample3"
    }
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
        response = client.delete_principal_access_boundary_policy(request)

    # Establish that the response is the type that we expect.
    json_return_value = json_format.MessageToJson(return_value)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_principal_access_boundary_policy_rest_interceptors(null_interceptor):
    transport = transports.PrincipalAccessBoundaryPoliciesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.PrincipalAccessBoundaryPoliciesRestInterceptor(),
    )
    client = PrincipalAccessBoundaryPoliciesClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(operation.Operation, "_set_result_from_operation"),
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "post_delete_principal_access_boundary_policy",
        ) as post,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "post_delete_principal_access_boundary_policy_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "pre_delete_principal_access_boundary_policy",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest.pb(
            principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest()
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

        request = principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = operations_pb2.Operation()
        post_with_metadata.return_value = operations_pb2.Operation(), metadata

        client.delete_principal_access_boundary_policy(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_principal_access_boundary_policies_rest_bad_request(
    request_type=principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest,
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1/locations/sample2"}
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
        client.list_principal_access_boundary_policies(request)


@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest,
        dict,
    ],
)
def test_list_principal_access_boundary_policies_rest_call_success(request_type):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "organizations/sample1/locations/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_principal_access_boundary_policies(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListPrincipalAccessBoundaryPoliciesPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_principal_access_boundary_policies_rest_interceptors(null_interceptor):
    transport = transports.PrincipalAccessBoundaryPoliciesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.PrincipalAccessBoundaryPoliciesRestInterceptor(),
    )
    client = PrincipalAccessBoundaryPoliciesClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "post_list_principal_access_boundary_policies",
        ) as post,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "post_list_principal_access_boundary_policies_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "pre_list_principal_access_boundary_policies",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest.pb(
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest()
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
        return_value = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse.to_json(
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse()
        )
        req.return_value.content = return_value

        request = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse()
        post_with_metadata.return_value = (
            principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse(),
            metadata,
        )

        client.list_principal_access_boundary_policies(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_search_principal_access_boundary_policy_bindings_rest_bad_request(
    request_type=principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest,
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "name": "organizations/sample1/locations/sample2/principalAccessBoundaryPolicies/sample3"
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
        client.search_principal_access_boundary_policy_bindings(request)


@pytest.mark.parametrize(
    "request_type",
    [
        principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest,
        dict,
    ],
)
def test_search_principal_access_boundary_policy_bindings_rest_call_success(
    request_type,
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "name": "organizations/sample1/locations/sample2/principalAccessBoundaryPolicies/sample3"
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.search_principal_access_boundary_policy_bindings(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.SearchPrincipalAccessBoundaryPolicyBindingsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_search_principal_access_boundary_policy_bindings_rest_interceptors(
    null_interceptor,
):
    transport = transports.PrincipalAccessBoundaryPoliciesRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.PrincipalAccessBoundaryPoliciesRestInterceptor(),
    )
    client = PrincipalAccessBoundaryPoliciesClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "post_search_principal_access_boundary_policy_bindings",
        ) as post,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "post_search_principal_access_boundary_policy_bindings_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.PrincipalAccessBoundaryPoliciesRestInterceptor,
            "pre_search_principal_access_boundary_policy_bindings",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest.pb(
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest()
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
        return_value = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse.to_json(
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse()
        )
        req.return_value.content = return_value

        request = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse()
        post_with_metadata.return_value = (
            principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse(),
            metadata,
        )

        client.search_principal_access_boundary_policy_bindings(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_operation_rest_bad_request(
    request_type=operations_pb2.GetOperationRequest,
):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict(
        {"name": "projects/sample1/locations/sample2/operations/sample3"}, request
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
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {"name": "projects/sample1/locations/sample2/operations/sample3"}
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
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_principal_access_boundary_policy_empty_call_rest():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_principal_access_boundary_policy), "__call__"
    ) as call:
        client.create_principal_access_boundary_policy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_principal_access_boundary_policy_empty_call_rest():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_principal_access_boundary_policy), "__call__"
    ) as call:
        client.get_principal_access_boundary_policy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_principal_access_boundary_policy_empty_call_rest():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_principal_access_boundary_policy), "__call__"
    ) as call:
        client.update_principal_access_boundary_policy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_principal_access_boundary_policy_empty_call_rest():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_principal_access_boundary_policy), "__call__"
    ) as call:
        client.delete_principal_access_boundary_policy(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_principal_access_boundary_policies_empty_call_rest():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_principal_access_boundary_policies), "__call__"
    ) as call:
        client.list_principal_access_boundary_policies(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_search_principal_access_boundary_policy_bindings_empty_call_rest():
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.search_principal_access_boundary_policy_bindings),
        "__call__",
    ) as call:
        client.search_principal_access_boundary_policy_bindings(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest()
        assert args[0] == request_msg


def test_principal_access_boundary_policies_rest_lro_client():
    client = PrincipalAccessBoundaryPoliciesClient(
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
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    assert isinstance(
        client.transport,
        transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
    )


def test_principal_access_boundary_policies_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.PrincipalAccessBoundaryPoliciesTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_principal_access_boundary_policies_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.iam_v3.services.principal_access_boundary_policies.transports.PrincipalAccessBoundaryPoliciesTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.PrincipalAccessBoundaryPoliciesTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "create_principal_access_boundary_policy",
        "get_principal_access_boundary_policy",
        "update_principal_access_boundary_policy",
        "delete_principal_access_boundary_policy",
        "list_principal_access_boundary_policies",
        "search_principal_access_boundary_policy_bindings",
        "get_operation",
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


def test_principal_access_boundary_policies_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.cloud.iam_v3.services.principal_access_boundary_policies.transports.PrincipalAccessBoundaryPoliciesTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.PrincipalAccessBoundaryPoliciesTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id="octopus",
        )


def test_principal_access_boundary_policies_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.cloud.iam_v3.services.principal_access_boundary_policies.transports.PrincipalAccessBoundaryPoliciesTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.PrincipalAccessBoundaryPoliciesTransport()
        adc.assert_called_once()


def test_principal_access_boundary_policies_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        PrincipalAccessBoundaryPoliciesClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            quota_project_id=None,
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
        transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
    ],
)
def test_principal_access_boundary_policies_transport_auth_adc(transport_class):
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
        transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
        transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
        transports.PrincipalAccessBoundaryPoliciesRestTransport,
    ],
)
def test_principal_access_boundary_policies_transport_auth_gdch_credentials(
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
        (transports.PrincipalAccessBoundaryPoliciesGrpcTransport, grpc_helpers),
        (
            transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
            grpc_helpers_async,
        ),
    ],
)
def test_principal_access_boundary_policies_transport_create_channel(
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
            "iam.googleapis.com:443",
            credentials=creds,
            credentials_file=None,
            quota_project_id="octopus",
            default_scopes=("https://www.googleapis.com/auth/cloud-platform",),
            scopes=["1", "2"],
            default_host="iam.googleapis.com",
            ssl_credentials=None,
            options=[
                ("grpc.max_send_message_length", -1),
                ("grpc.max_receive_message_length", -1),
            ],
        )


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
        transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
    ],
)
def test_principal_access_boundary_policies_grpc_transport_client_cert_source_for_mtls(
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


def test_principal_access_boundary_policies_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.PrincipalAccessBoundaryPoliciesRestTransport(
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
def test_principal_access_boundary_policies_host_no_port(transport_name):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(api_endpoint="iam.googleapis.com"),
        transport=transport_name,
    )
    assert client.transport._host == (
        "iam.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://iam.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "grpc",
        "grpc_asyncio",
        "rest",
    ],
)
def test_principal_access_boundary_policies_host_with_port(transport_name):
    client = PrincipalAccessBoundaryPoliciesClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="iam.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "iam.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://iam.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_principal_access_boundary_policies_client_transport_session_collision(
    transport_name,
):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = PrincipalAccessBoundaryPoliciesClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = PrincipalAccessBoundaryPoliciesClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.create_principal_access_boundary_policy._session
    session2 = client2.transport.create_principal_access_boundary_policy._session
    assert session1 != session2
    session1 = client1.transport.get_principal_access_boundary_policy._session
    session2 = client2.transport.get_principal_access_boundary_policy._session
    assert session1 != session2
    session1 = client1.transport.update_principal_access_boundary_policy._session
    session2 = client2.transport.update_principal_access_boundary_policy._session
    assert session1 != session2
    session1 = client1.transport.delete_principal_access_boundary_policy._session
    session2 = client2.transport.delete_principal_access_boundary_policy._session
    assert session1 != session2
    session1 = client1.transport.list_principal_access_boundary_policies._session
    session2 = client2.transport.list_principal_access_boundary_policies._session
    assert session1 != session2
    session1 = (
        client1.transport.search_principal_access_boundary_policy_bindings._session
    )
    session2 = (
        client2.transport.search_principal_access_boundary_policy_bindings._session
    )
    assert session1 != session2


def test_principal_access_boundary_policies_grpc_transport_channel():
    channel = grpc.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.PrincipalAccessBoundaryPoliciesGrpcTransport(
        host="squid.clam.whelk",
        channel=channel,
    )
    assert transport.grpc_channel == channel
    assert transport._host == "squid.clam.whelk:443"
    assert transport._ssl_channel_credentials == None


def test_principal_access_boundary_policies_grpc_asyncio_transport_channel():
    channel = aio.secure_channel("http://localhost/", grpc.local_channel_credentials())

    # Check that channel is used if provided.
    transport = transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport(
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
        transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
        transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
    ],
)
def test_principal_access_boundary_policies_transport_channel_mtls_with_client_cert_source(
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
        transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
        transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
    ],
)
def test_principal_access_boundary_policies_transport_channel_mtls_with_adc(
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


def test_principal_access_boundary_policies_grpc_lro_client():
    client = PrincipalAccessBoundaryPoliciesClient(
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


def test_principal_access_boundary_policies_grpc_lro_async_client():
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
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


def test_policy_binding_path():
    organization = "squid"
    location = "clam"
    policy_binding = "whelk"
    expected = "organizations/{organization}/locations/{location}/policyBindings/{policy_binding}".format(
        organization=organization,
        location=location,
        policy_binding=policy_binding,
    )
    actual = PrincipalAccessBoundaryPoliciesClient.policy_binding_path(
        organization, location, policy_binding
    )
    assert expected == actual


def test_parse_policy_binding_path():
    expected = {
        "organization": "octopus",
        "location": "oyster",
        "policy_binding": "nudibranch",
    }
    path = PrincipalAccessBoundaryPoliciesClient.policy_binding_path(**expected)

    # Check that the path construction is reversible.
    actual = PrincipalAccessBoundaryPoliciesClient.parse_policy_binding_path(path)
    assert expected == actual


def test_principal_access_boundary_policy_path():
    organization = "cuttlefish"
    location = "mussel"
    principal_access_boundary_policy = "winkle"
    expected = "organizations/{organization}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy}".format(
        organization=organization,
        location=location,
        principal_access_boundary_policy=principal_access_boundary_policy,
    )
    actual = (
        PrincipalAccessBoundaryPoliciesClient.principal_access_boundary_policy_path(
            organization, location, principal_access_boundary_policy
        )
    )
    assert expected == actual


def test_parse_principal_access_boundary_policy_path():
    expected = {
        "organization": "nautilus",
        "location": "scallop",
        "principal_access_boundary_policy": "abalone",
    }
    path = PrincipalAccessBoundaryPoliciesClient.principal_access_boundary_policy_path(
        **expected
    )

    # Check that the path construction is reversible.
    actual = PrincipalAccessBoundaryPoliciesClient.parse_principal_access_boundary_policy_path(
        path
    )
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = PrincipalAccessBoundaryPoliciesClient.common_billing_account_path(
        billing_account
    )
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = PrincipalAccessBoundaryPoliciesClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = PrincipalAccessBoundaryPoliciesClient.parse_common_billing_account_path(
        path
    )
    assert expected == actual


def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = PrincipalAccessBoundaryPoliciesClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = PrincipalAccessBoundaryPoliciesClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = PrincipalAccessBoundaryPoliciesClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = PrincipalAccessBoundaryPoliciesClient.common_organization_path(
        organization
    )
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = PrincipalAccessBoundaryPoliciesClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = PrincipalAccessBoundaryPoliciesClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = PrincipalAccessBoundaryPoliciesClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = PrincipalAccessBoundaryPoliciesClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = PrincipalAccessBoundaryPoliciesClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = PrincipalAccessBoundaryPoliciesClient.common_location_path(
        project, location
    )
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = PrincipalAccessBoundaryPoliciesClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = PrincipalAccessBoundaryPoliciesClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.PrincipalAccessBoundaryPoliciesTransport, "_prep_wrapped_messages"
    ) as prep:
        client = PrincipalAccessBoundaryPoliciesClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.PrincipalAccessBoundaryPoliciesTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = PrincipalAccessBoundaryPoliciesClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_get_operation(transport: str = "grpc"):
    client = PrincipalAccessBoundaryPoliciesClient(
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
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
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
    client = PrincipalAccessBoundaryPoliciesClient(
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
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
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
    client = PrincipalAccessBoundaryPoliciesClient(
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
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
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
    client = PrincipalAccessBoundaryPoliciesClient(
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
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
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


def test_transport_close_grpc():
    client = PrincipalAccessBoundaryPoliciesClient(
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
    client = PrincipalAccessBoundaryPoliciesAsyncClient(
        credentials=async_anonymous_credentials(), transport="grpc_asyncio"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_grpc_channel")), "close"
    ) as close:
        async with client:
            close.assert_not_called()
        close.assert_called_once()


def test_transport_close_rest():
    client = PrincipalAccessBoundaryPoliciesClient(
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
        client = PrincipalAccessBoundaryPoliciesClient(
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
            PrincipalAccessBoundaryPoliciesClient,
            transports.PrincipalAccessBoundaryPoliciesGrpcTransport,
        ),
        (
            PrincipalAccessBoundaryPoliciesAsyncClient,
            transports.PrincipalAccessBoundaryPoliciesGrpcAsyncIOTransport,
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
